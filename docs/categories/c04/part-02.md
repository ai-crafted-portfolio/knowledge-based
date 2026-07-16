---
search:
  exclude: true
---

# CICS Transaction Server for z/OS 6.x — 詳細 (2/2)

[← CICS Transaction Server for z/OS 6.x の概要へ戻る](index.md)


## ファイル管理


<section class="kb-item" id="c04-i0180"><h3>ファイル管理 FILE資源 復旧後の確認 FILE06</h3><p class="kb-meta">分類: ファイル管理 ・ 難易度: 中級</p><p>復旧後の確認では ファイル管理 の 統計採取 を主操作として FILE06 を判定します。再発していないことを示す値への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE06 に残します。復旧後の確認を補助する ファイル照会 では File を補助値として FILE06 へ保存します。主判定の復旧後の確認ではファイル管理・資源の 統計採取 から DFHST0103I を読み FILE06 へ残します。証跡照合の復旧後の確認ではファイル管理・資源の DFHST0103I と File を FILE06 に保存します。記録対応の復旧後の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE06 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で ファイル管理 の 統計採取 と ファイル照会 を実施し FILE資源 の役割を確認します。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。対象 FILE06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. Liberty JVMのJVMSTATUSとPROFILEを確認する。その値をファイル管理のFILE06にも適用する。</li><li>B. CEMT PERFORM STATISTICS RECORD FILE(FILE06)でDFHST0103Iを取得してからCEMT INQUIRE DSNAME(APP.FILE06.DATA)でDsnを照合する。FILE06のOPENSTATUSとDSNAMEを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEMT INQUIRE FILE(FILE06)が成功したためCEMT PERFORM STATISTICS RECORD FILE(FILE06)のDFHST0103Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象FILE06へ引き継げるものとする。FILE資源の再発していないことを示す値は確認済みとして扱う。さらにCEMT INQUIRE DSNAME(APP.FILE06.DATA)のDsnをDFHST0103Iと同種の値として併記する。</li><li>D. CEMT PERFORM STATISTICS RECORD FILE(FILE06)を対象名なしで実行する。一覧の先頭行をFILE06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Bは統計採取で DFHST0103I を読みOPENSTATUSとDSNAMEの主値として復旧後の安定性を確認しFILE06に残します。
構成上の背景: 復旧後の確認ではファイル照会を補助操作としFILE資源の再発していないことを示す値をFileと対象FILE06で照合します。
候補ごとの理由: 統計採取とファイル照会の役割を分けるとA: Liberty JVMの値ではDFHST0103Iを確認できない点でファイル照会の範囲を越えます、B: DFHST0103IとDsnを順に照合する点で現在値を示します、C: 補助操作の成功ではDFHST0103Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はFILE06と確定できない点で統計採取を代替しません。結論として復旧後の確認のファイル管理・資源で判定する対象は FILE06 です。
初出用語: 復旧後の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE06へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ファイル管理 FILE資源 復旧後の確認 FILE06</strong></p><p>検証目的: ファイル管理のFILE資源について復旧後の安定性を確認し、FILE06のOPENSTATUSとDSNAMEを実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE06)を指定し、FILE06の統計採取を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD FILE(FILE06)
→ Enter を押す
［画面・出力］
DFHST0103I FILE FILE06 STATISTICS RECORDED
画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE06)を指定し、FILE06のファイル照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE06)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
File(FILE06) Ope Ena Rea Upd Dsname(APP.FILE06.DATA)
画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE06.DATA)を指定し、FILE06のデータセット照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE DSNAME(APP.FILE06.DATA)
→ Enter を押す
［画面・出力］
Dsn(APP.FILE06.DATA) Quiesced(No) Retlocks(No)
画面・出力にあるAPP.FILE06.DATAを読み、OPENSTATUSとDSNAMEと対象FILE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
② ステップ2 の File が画面・出力に表示されること
③ ステップ3 の APP.FILE06.DATA が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0181"><h3>ファイル管理 FILE資源 復旧準備 FILE05</h3><p class="kb-meta">分類: ファイル管理 ・ 難易度: 中級</p><p>復旧準備では ファイル管理 の データセット照会 を主操作として FILE05 を判定します。再開前に必要な整合性への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE05 に残します。復旧準備を補助する 統計採取 では DFHST0103I を補助値として FILE05 へ保存します。主判定の復旧準備ではファイル管理・資源の データセット照会 から Dsn を読み FILE05 へ残します。証跡照合の復旧準備ではファイル管理・資源の Dsn と DFHST0103I を FILE05 に保存します。記録対応の復旧準備ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE05 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で ファイル管理 の データセット照会 と 統計採取 を使い 復旧条件を確認 します。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。Dsn を読み対象 FILE05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずCEMT INQUIRE DSNAME(APP.FILE05.DATA)を実行する。Dsnを保存する。差分はCEMT PERFORM STATISTICS RECORD FILE(FILE05)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したCEMT INQUIRE DSNAME(APP.FILE05.DATA)の結果を使う。今回のCEMT PERFORM STATISTICS RECORD FILE(FILE05)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのFILE05の出力を再利用する。今回のCEMT INQUIRE DSNAME(APP.FILE05.DATA)とCEMT PERFORM STATISTICS RECORD FILE(FILE05)は実行済みとして扱う。</li><li>D. CEMT PERFORM STATISTICS RECORD FILE(FILE05)のDFHST0103IをOPENSTATUSとDSNAMEの主判定に採用する。CEMT INQUIRE DSNAME(APP.FILE05.DATA)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはデータセット照会で Dsn を読みOPENSTATUSとDSNAMEの主値として復旧条件を確認しFILE05に残します。
処理の仕組み: 復旧準備では統計採取を補助操作としFILE資源の再開前に必要な整合性をDFHST0103Iと対象FILE05で照合します。
選択結果の内訳: データセット照会と統計採取の役割を分けるとA: 変更前のDsnを保存する点でデータセット照会に合います、B: 採取時刻が異なる点でファイル管理に使いません、C: 過去出力では今回の復旧準備を示せない点でFILE資源に使えません、D: DFHST0103IはDsnを代替しないうえに追加前提も不正な点でFILE05を採用できません。結論として復旧準備のファイル管理・資源で判定する対象は FILE05 です。
用語の説明: 復旧準備で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE05へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ファイル管理 FILE資源 復旧準備 FILE05</strong></p><p>検証目的: ファイル管理のFILE資源について復旧条件を確認し、FILE05のOPENSTATUSとDSNAMEを実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE05.DATA)を指定し、FILE05のデータセット照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE DSNAME(APP.FILE05.DATA)
→ Enter を押す
［画面・出力］
Dsn(APP.FILE05.DATA) Quiesced(No) Retlocks(No)
画面・出力にあるAPP.FILE05.DATAを読み、OPENSTATUSとDSNAMEと対象FILE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE05)を指定し、FILE05の統計採取を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD FILE(FILE05)
→ Enter を押す
［画面・出力］
DFHST0103I FILE FILE05 STATISTICS RECORDED
画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE05)を指定し、FILE05のファイル照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE05)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
File(FILE05) Ope Ena Rea Upd Dsname(APP.FILE05.DATA)
画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の APP.FILE05.DATA が画面・出力に表示されること
② ステップ2 の DFHST0103I が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0182"><h3>ファイル管理 FILE資源 構成監査 FILE08</h3><p class="kb-meta">分類: ファイル管理 ・ 難易度: 中級</p><p>構成監査では ファイル管理 の データセット照会 を主操作として FILE08 を判定します。定義値と稼働値の一致への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE08 に残します。構成監査を補助する 統計採取 では DFHST0103I を補助値として FILE08 へ保存します。主判定の構成監査ではファイル管理・資源の データセット照会 から Dsn を読み FILE08 へ残します。証跡照合の構成監査ではファイル管理・資源の Dsn と DFHST0103I を FILE08 に保存します。記録対応の構成監査ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE08 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で ファイル管理 の データセット照会 と 統計採取 を照合し 定義値と稼働値の一致 を確かめます。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。Dsn を読む前に対象 FILE08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのFILE08の出力を再利用する。今回のCEMT INQUIRE DSNAME(APP.FILE08.DATA)とCEMT PERFORM STATISTICS RECORD FILE(FILE08)は実行済みとして扱う。</li><li>B. CEMT PERFORM STATISTICS RECORD FILE(FILE08)のDFHST0103IをOPENSTATUSとDSNAMEの主判定に採用する。CEMT INQUIRE DSNAME(APP.FILE08.DATA)の応答は採取対象から外す。</li><li>C. CEMT INQUIRE FILE(FILE08)のFileをDsnと同義の成功表示として扱う。CEMT INQUIRE DSNAME(APP.FILE08.DATA)は実行しない。</li><li>D. CEMT PERFORM STATISTICS RECORD FILE(FILE08)の結果だけでは確定しない。CEMT INQUIRE DSNAME(APP.FILE08.DATA)のDsnを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはデータセット照会で Dsn を読みOPENSTATUSとDSNAMEの主値として構成差分を監査しFILE08に残します。
実行時の背景: 構成監査では統計採取を補助操作としFILE資源の定義値と稼働値の一致をDFHST0103Iと対象FILE08で照合します。
四つの候補の理由: データセット照会と統計採取の役割を分けるとA: 過去出力では今回の構成監査を示せない点でファイル管理に使いません、B: DFHST0103IはDsnを代替しない点でFILE資源に使えません、C: FileとDsnは確認項目が異なる点でFILE08を採用できません、D: Dsnを主証跡として区別する点で主証跡になります。結論として構成監査のファイル管理・資源で判定する対象は FILE08 です。
初出語定義: 構成監査で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE08へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ファイル管理 FILE資源 構成監査 FILE08</strong></p><p>検証目的: ファイル管理のFILE資源について構成差分を監査し、FILE08のOPENSTATUSとDSNAMEを実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE08.DATA)を指定し、FILE08のデータセット照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE DSNAME(APP.FILE08.DATA)
→ Enter を押す
［画面・出力］
Dsn(APP.FILE08.DATA) Quiesced(No) Retlocks(No)
画面・出力にあるAPP.FILE08.DATAを読み、OPENSTATUSとDSNAMEと対象FILE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE08)を指定し、FILE08の統計採取を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD FILE(FILE08)
→ Enter を押す
［画面・出力］
DFHST0103I FILE FILE08 STATISTICS RECORDED
画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE08)を指定し、FILE08のファイル照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE08)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
File(FILE08) Ope Ena Rea Upd Dsname(APP.FILE08.DATA)
画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の APP.FILE08.DATA が画面・出力に表示されること
② ステップ2 の DFHST0103I が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0183"><h3>ファイル管理 FILE資源 通常状態の確認 FILE01</h3><p class="kb-meta">分類: ファイル管理 ・ 難易度: 中級</p><p>通常状態の確認では ファイル管理 の ファイル照会 を主操作として FILE01 を判定します。基準値と現在値の差への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE01 に残します。通常状態の確認を補助する データセット照会 では Dsn を補助値として FILE01 へ保存します。主判定の通常状態の確認ではファイル管理・資源の ファイル照会 から File を読み FILE01 へ残します。証跡照合の通常状態の確認ではファイル管理・資源の File と Dsn を FILE01 に保存します。記録対応の通常状態の確認ではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE01 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で ファイル管理 の ファイル照会 と データセット照会 を用い 通常状態を確定 します。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。File で対象 FILE01 の OPENSTATUSとDSNAME を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE FILE(FILE01)を先に実行する。対象FILE01のFileをOPENSTATUSとDSNAMEとして記録する。続いてCEMT INQUIRE DSNAME(APP.FILE01.DATA)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. CEMT INQUIRE DSNAME(APP.FILE01.DATA)のDsnをOPENSTATUSとDSNAMEの主判定に採用する。CEMT INQUIRE FILE(FILE01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. CEMT PERFORM STATISTICS RECORD FILE(FILE01)のDFHST0103IをFileと同義の成功表示として扱う。CEMT INQUIRE FILE(FILE01)は実行しない。</li><li>D. CEMT INQUIRE FILE(FILE01)が応答を返した時点で正常とする。応答中のFileの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Aはファイル照会で File を読みOPENSTATUSとDSNAMEの主値として通常状態を確定しFILE01に残します。
背景・仕組み: 通常状態の確認ではデータセット照会を補助操作としFILE資源の基準値と現在値の差をDsnと対象FILE01で照合します。
選択肢の理由: ファイル照会とデータセット照会の役割を分けるとA: Fileを主値として補助結果と照合する点で正答です、B: DsnはFileを代替しないうえに追加前提も不正な点でFILE01を採用できません、C: DFHST0103IとFileは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではOPENSTATUSとDSNAMEを判定できない点で一次資料と一致しません。結論として通常状態の確認のファイル管理・資源で判定する対象は FILE01 です。
用語の初出定義: 通常状態の確認で使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE01へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ファイル管理 FILE資源 通常状態の確認 FILE01</strong></p><p>検証目的: ファイル管理のFILE資源について通常状態を確定し、FILE01のOPENSTATUSとDSNAMEを実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE01)を指定し、FILE01のファイル照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE01)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
File(FILE01) Ope Ena Rea Upd Dsname(APP.FILE01.DATA)
画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE01.DATA)を指定し、FILE01のデータセット照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE DSNAME(APP.FILE01.DATA)
→ Enter を押す
［画面・出力］
Dsn(APP.FILE01.DATA) Quiesced(No) Retlocks(No)
画面・出力にあるAPP.FILE01.DATAを読み、OPENSTATUSとDSNAMEと対象FILE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE01)を指定し、FILE01の統計採取を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD FILE(FILE01)
→ Enter を押す
［画面・出力］
DFHST0103I FILE FILE01 STATISTICS RECORDED
画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の File が画面・出力に表示されること
② ステップ2 の APP.FILE01.DATA が画面・出力に表示されること
③ ステップ3 の DFHST0103I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0184"><h3>ファイル管理 FILE資源 障害切り分け FILE04</h3><p class="kb-meta">分類: ファイル管理 ・ 難易度: 中級</p><p>障害切り分けでは ファイル管理 の ファイル照会 を主操作として FILE04 を判定します。最初に失敗した処理への注意として「CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります」を FILE04 に残します。障害切り分けを補助する データセット照会 では Dsn を補助値として FILE04 へ保存します。主判定の障害切り分けではファイル管理・資源の ファイル照会 から File を読み FILE04 へ残します。証跡照合の障害切り分けではファイル管理・資源の File と Dsn を FILE04 に保存します。記録対応の障害切り分けではファイル管理・資源の OPENSTATUSとDSNAME の証跡へ FILE04 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで ファイル管理 の ファイル照会 と データセット照会 の役割を分け 最初に失敗した処理 を調べます。FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源です。CLOSEDやDISABLEDをVSAM障害だけと判断する危険があります。対象 FILE04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. CEMT PERFORM STATISTICS RECORD FILE(FILE04)のDFHST0103IをFileと同義の成功表示として扱う。CEMT INQUIRE FILE(FILE04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. CEMT INQUIRE FILE(FILE04)が応答を返した時点で正常とする。応答中のFileの値は記録しない。</li><li>C. CEMT INQUIRE FILE(FILE04)のコマンド文字列だけを記録する。Fileを含む応答行は保存しない。</li><li>D. CEMT INQUIRE FILE(FILE04)の出力でFILE04とFileが同じ応答にあることを確認する。OPENSTATUSとDSNAMEをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Dはファイル照会で File を読みOPENSTATUSとDSNAMEの主値として障害範囲を限定しFILE04に残します。
技術的背景: 障害切り分けではデータセット照会を補助操作としFILE資源の最初に失敗した処理をDsnと対象FILE04で照合します。
四択の評価: ファイル照会とデータセット照会の役割を分けるとA: DFHST0103IとFileは確認項目が異なるうえに追加前提も不正な点でFILE04を採用できません、B: 応答の有無だけではOPENSTATUSとDSNAMEを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではOPENSTATUSとDSNAMEを証明できない点で一次資料と一致しません、D: FILE04とFileを同じ応答で結ぶ点でFILE04を判定できます。結論として障害切り分けのファイル管理・資源で判定する対象は FILE04 です。
初出語の意味: 障害切り分けで使う FILE資源 はデータセット名、OPEN状態、READ/UPDATE権限、LSRプールをCICSへ定義する資源を表しOPENSTATUSとDSNAMEを判定する際にFILE04へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ファイル管理 FILE資源 障害切り分け FILE04</strong></p><p>検証目的: ファイル管理のFILE資源について障害範囲を限定し、FILE04のOPENSTATUSとDSNAMEを実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象FILE04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE FILE(FILE04)を指定し、FILE04のファイル照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE04)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
File(FILE04) Ope Ena Rea Upd Dsname(APP.FILE04.DATA)
画面・出力にあるFileを読み、OPENSTATUSとDSNAMEと対象FILE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE DSNAME(APP.FILE04.DATA)を指定し、FILE04のデータセット照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE DSNAME(APP.FILE04.DATA)
→ Enter を押す
［画面・出力］
Dsn(APP.FILE04.DATA) Quiesced(No) Retlocks(No)
画面・出力にあるAPP.FILE04.DATAを読み、OPENSTATUSとDSNAMEと対象FILE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのファイル管理を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD FILE(FILE04)を指定し、FILE04の統計採取を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD FILE(FILE04)
→ Enter を押す
［画面・出力］
DFHST0103I FILE FILE04 STATISTICS RECORDED
画面・出力にあるDFHST0103Iを読み、OPENSTATUSとDSNAMEと対象FILE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の File が画面・出力に表示されること
② ステップ2 の APP.FILE04.DATA が画面・出力に表示されること
③ ステップ3 の DFHST0103I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


## プログラム管理


<section class="kb-item" id="c04-i0185"><h3>CEDA DEFINE FILE 状態確認 理由コード</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEDA DEFINE FILE 状態確認 理由コード」は、VSAMなどのFILEリソースをCSDに定義し、データセット名や状態を管理するRDO操作を状態確認の観点で確認する技術項目です。MAX/CUR 欄とAEI8を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、未インストール定義の採用を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEDA DEFINE FILE 状態確認 理由コード</strong></p><p>検証目的: プログラム管理におけるCEDA DEFINE FILEの状態確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=AEI8</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; PUT CICS bridge message for CEMT INQUIRE TASK
→ Enter を押す
［画面・出力］
CICS-MQ BRIDGE REQUEST ACCEPTED
TRANSACTION CEMT
COMMAND CEMT INQUIRE TASK
画面・出力には CICS-MQ が含まれ、CICS-MQを確認し、未インストール定義の採用を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TASK TRAN(CWXN)
→ Enter を押す
［画面・出力］
Tas(0051988) Tra(CWXN) Sus Tas Pri(001) Sta(U) Use(WEBSRV)
Uow(C9D5F2EE2DEE8499) Hty(SOCKET) Hva(RECEIVE) Hti(200841) Bac Wai
画面・出力には CWXN が含まれ、CWXNを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TRANSACTION(CWXN)
→ Enter を押す
［画面・出力］
Tra(CWXN) Pri(001) Pro(DFHWBXN) Ena Sta Profile(DFHCICST)
画面・出力には CWXN が含まれ、CWXNを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CICS-MQ が画面・出力に表示されること
② ステップ2 の CWXN が画面・出力に表示されること
③ ステップ3 の CWXN が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0186"><h3>CEMT INQUIRE FILE 接続確認 属性確認</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEMT INQUIRE FILE 接続確認 属性確認」は、FILEリソースのOPEN/CLOSED、ENABLED/DISABLED、使用状態を確認するメイン端末コマンドを接続確認の観点で確認する技術項目です。FILE 欄とCIC04を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT INQUIRE FILE 接続確認 属性確認</strong></p><p>検証目的: プログラム管理におけるCEMT INQUIRE FILEの接続確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC04</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE TRANSACTION(PAY004) GROUP(TEST) PROGRAM(DFH004)
→ Enter を押す
［画面・出力］
CEDA DEF TRANSACTION(PAY004) GROUP(TEST)
PROGRAM ==&gt; DFH004
PROFILE ==&gt; DFHCICST
画面・出力には CEDA が含まれ、CEDAを確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE PROGRAM(DFH004) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF PROGRAM(DFH004) GROUP(TEST)
LANGUAGE ==&gt; COBOL
STATUS ==&gt; ENABLED
画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(TEST)
→ Enter を押す
［画面・出力］
INSTALL SUCCESSFUL FOR GROUP TEST
TRANSACTION PAY004 INSTALLED
PROGRAM DFH004 INSTALLED
画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
② ステップ2 の CEDA が画面・出力に表示されること
③ ステップ3 の INSTALL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0187"><h3>CEMT INQUIRE TCPIPSERVICE 戻りコード確認 表形式</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 上級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEMT INQUIRE TCPIPSERVICE 戻りコード確認 表形式」は、TCPIPSERVICEのOPEN/CLOSED、PORT、BACKLOG、URMを確認するメイン端末コマンドを戻りコード確認の観点で確認する技術項目です。Tas 行とTCP05を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT INQUIRE TCPIPSERVICE 戻りコード確認 表形式</strong></p><p>検証目的: プログラム管理におけるCEMT INQUIRE TCPIPSERVICEの戻りコード確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=TCP05</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE TCPIPSERVICE(TCP05) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF TCPIPSERVICE(TCP05) GROUP(TEST)
PROTOCOL ==&gt; HTTP
PORTNUMBER ==&gt; 08080
URM ==&gt; DFHWBAAX
画面・出力には CEDA が含まれ、CEDAを確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE URIMAP(URI05) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF URIMAP(URI05) GROUP(TEST)
PATH ==&gt; /pay/095
TRANSACTION ==&gt; CWBA
画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(TEST)
→ Enter を押す
［画面・出力］
INSTALL SUCCESSFUL FOR GROUP TEST
TCPIPSERVICE TCP05 INSTALLED
URIMAP URI05 INSTALLED
画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
② ステップ2 の CEDA が画面・出力に表示されること
③ ステップ3 の INSTALL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0188"><h3>CEMT SET TRD 接続確認 設定値</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CEMT SET TRD 接続確認 設定値」は、トランザクション異常終了コードに対するダンプ取得条件を設定する操作を接続確認の観点で確認する技術項目です。RC 欄とFILE082を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、タスク待機理由の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT SET TRD 接続確認 設定値</strong></p><p>検証目的: プログラム管理におけるCEMT SET TRDの接続確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=FILE082</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE082)
→ Enter を押す
［画面・出力］
Fil(FILE082) Vsa Ope Ena Rea Upd Add Bro Del Sha
画面・出力には FILE082 が含まれ、FILE082を確認し、タスク待機理由の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET FILE(FILE082) CLOSED ENABLED
→ Enter を押す
［画面・出力］
Fil(FILE082) Clo Ena Rea Upd Add Bro Del
画面・出力には FILE082 が含まれ、FILE082を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE082)
→ Enter を押す
［画面・出力］
Fil(FILE082) Clo Ena Rea Upd Add Bro Del
画面・出力には FILE082 が含まれ、FILE082を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の FILE082 が画面・出力に表示されること
② ステップ2 の FILE082 が画面・出力に表示されること
③ ステップ3 の FILE082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0189"><h3>CONFDATA trace setting 出力項目確認 キュー状態</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CONFDATA trace setting 出力項目確認 キュー状態」は、トレースに含める機密データ表示をHIDE/SHOWで制御する設定を出力項目確認の観点で確認する技術項目です。PORTNUMBER 欄とPAY030を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONFDATA trace setting 出力項目確認 キュー状態</strong></p><p>検証目的: プログラム管理におけるCONFDATA trace settingの出力項目確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=PAY030</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; Open Tasks view for CIC30
→ Enter を押す
［画面・出力］
Tasks view APPLID CIC30
Task 0051988 Transaction CWXN Status Suspended Wait RECEIVE
画面・出力には Tasks が含まれ、Tasksを確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; GET CICSDefinitionTCPIPService TCP30
→ Enter を押す
［画面・出力］
&lt;response&gt;&lt;TCPIPSERVICE name=&quot;TCP30&quot; status=&quot;OPEN&quot; port=&quot;8080&quot; protocol=&quot;HTTP&quot; /&gt;&lt;/response&gt;
画面・出力には response が含まれ、responseを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; GET CICSDefinitionTransaction PAY030
→ Enter を押す
［画面・出力］
&lt;response&gt;&lt;TRANSACTION name=&quot;PAY030&quot; program=&quot;DFH030&quot; status=&quot;ENABLED&quot; /&gt;&lt;/response&gt;
画面・出力には response が含まれ、responseを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の Tasks が画面・出力に表示されること
② ステップ2 の response が画面・出力に表示されること
③ ステップ3 の response が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0190"><h3>CWXN transaction リソース照合 処理範囲</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「CWXN transaction リソース照合 処理範囲」は、CICS Web SupportのHTTP要求処理に使われるCICS supplied transactionをリソース照合の観点で確認する技術項目です。DFH メッセージとURI26を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、TCP/IPサービス状態の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CWXN transaction リソース照合 処理範囲</strong></p><p>検証目的: プログラム管理におけるCWXN transactionのリソース照合を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=URI26</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET TRD(AEI5) SYS MAX(1) ADD
→ Enter を押す
［画面・出力］
Trd(AEI5) Sys Cur(000000) Max(000001) Add
画面・出力には AEI5 が含まれ、AEI5を確認し、TCP/IPサービス状態の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TRD(AEI5)
→ Enter を押す
［画面・出力］
Trd(AEI5) Sys Cur(000000) Max(000001) Add
画面・出力には AEI5 が含まれ、AEI5を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET SYD(12345) SYS MAX(1) ADD
→ Enter を押す
［画面・出力］
SYDUMP Syd(12345) Sys Cur(000000) Max(000001) Add
画面・出力には SYDUMP が含まれ、SYDUMPを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の AEI5 が画面・出力に表示されること
② ステップ2 の AEI5 が画面・出力に表示されること
③ ステップ3 の SYDUMP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0191"><h3>Liberty DataSource リソース照合 一致条件</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「Liberty DataSource リソース照合 一致条件」は、server.xmlでDb2 DataSourceを構成し、CICSのDB2CONNを経由する接続設定をリソース照合の観点で確認する技術項目です。TCPIPSERVICE 行とJVMSRV17を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Db2接続前提の欠落を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Liberty DataSource リソース照合 一致条件</strong></p><p>検証目的: プログラム管理におけるLiberty DataSourceのリソース照合を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=JVMSRV17</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CETR
→ Enter を押す
［画面・出力］
CETR CICS TRACE CONTROL
MAIN SYSTEM TRACE FLAG ==&gt; OFF
AUXILIARY TRACE STATUS ==&gt; STARTED
画面・出力には CETR が含まれ、CETRを確認し、Db2接続前提の欠落を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; VERBX DFHPD760 &#x27;TR=1&#x27;
→ Enter を押す
［画面・出力］
DFHPD760 CICS TRACE FORMATTER
TRACE ENTRIES SELECTED FOR APPLID CIC17
RETURN CODE = 0000
画面・出力には DFHPD760 が含まれ、DFHPD760を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; SUBMIT CICS.DFHTU760.CNTL(TRACE)
→ Enter を押す
［画面・出力］
DFHTU760 AUXILIARY TRACE PRINT UTILITY
ABBREVIATED TRACE PRINTED
RETURN CODE = 0000
画面・出力には DFHTU760 が含まれ、DFHTU760を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CETR が画面・出力に表示されること
② ステップ2 の DFHPD760 が画面・出力に表示されること
③ ステップ3 の DFHTU760 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0192"><h3>URIMAP resource 接続確認 復旧手掛かり</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の プログラム管理 で扱う「URIMAP resource 接続確認 復旧手掛かり」は、HTTP要求をTCPIPSERVICE、パス、alias transactionへ対応付けるWebサポート定義を接続確認の観点で確認する技術項目です。URIMAP 行と00142を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>URIMAP resource 接続確認 復旧手掛かり</strong></p><p>検証目的: プログラム管理におけるURIMAP resourceの接続確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=00142</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TCPIPSERVICE(TCP13)
→ Enter を押す
［画面・出力］
Tcp(TCP13) Ope Por(08080) Pro(Http) Backlog(00050) Urm(DFHWBAAX)
画面・出力には TCP13 が含まれ、TCP13を確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET TCPIPSERVICE(TCP13) OPEN
→ Enter を押す
［画面・出力］
Tcp(TCP13) Ope Por(08080) Pro(Http) Backlog(00050)
画面・出力には TCP13 が含まれ、TCP13を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TCPIP
→ Enter を押す
［画面・出力］
Tcpip Open ActSockets(000012) ActSslTcbs(000002)
画面・出力には Tcpip が含まれ、Tcpipを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の TCP13 が画面・出力に表示されること
② ステップ2 の TCP13 が画面・出力に表示されること
③ ステップ3 の Tcpip が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0193"><h3>プログラム管理 PROGRAM資源 ログとの照合 PGM07</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>ログとの照合では プログラム管理 の プログラム照会 を主操作として PGM07 を判定します。時刻と対象識別子への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM07 に残します。ログとの照合を補助する 使用タスク確認 では Status を補助値として PGM07 へ保存します。主判定のログとの照合ではプログラム管理・資源の プログラム照会 から Prog を読み PGM07 へ残します。証跡照合のログとの照合ではプログラム管理・資源の Prog と Status を PGM07 に保存します。記録対応のログとの照合ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM07 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で プログラム管理 の プログラム照会 と 使用タスク確認 を組み合わせる際は PROGRAM資源 がロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源という仕組みを前提にします。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。Prog と PROGRAM名とNEWCOPY結果 を対象 PGM07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. Progを含むプログラム照会の応答行を保存する。その応答を得るためCEMT INQUIRE PROGRAM(PGM07)を使用する。対象PGM07のPROGRAM名とNEWCOPY結果として記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. CEMT INQUIRE PROGRAM(PGM07)が応答を返した時点で正常とする。応答中のProgの値は記録しない。PROGRAMをProgと同じ判定値とみなし対象PGM07の主証跡にする。PROGRAM資源の時刻と対象識別子は確認済みとして扱う。さらにCEDA VIEW PROGRAM(PGM07) GROUP(GRP07)のPROGRAMをProgと同種の値として併記する。</li><li>C. CEMT INQUIRE PROGRAM(PGM07)のコマンド文字列だけを記録する。Progを含む応答行は保存しない。</li><li>D. PROGRAM資源の停止または再定義を実施する。その後にCEMT INQUIRE PROGRAM(PGM07)でProgを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として操作とログを対応しPGM07に残します。
機能の仕組み: ログとの照合では使用タスク確認を補助操作としPROGRAM資源の時刻と対象識別子をStatusと対象PGM07で照合します。
各候補の評価: プログラム照会と使用タスク確認の役割を分けるとA: Progの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではPROGRAM名とNEWCOPY結果を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではPROGRAM名とNEWCOPY結果を証明できない点でPROGRAM名とNEWCOPY結果を確認できません、D: 変更前のPROGRAM名とNEWCOPY結果を失う点で使用タスク確認の範囲を越えます。結論としてログとの照合のプログラム管理・資源で判定する対象は PGM07 です。
用語の定義: ログとの照合で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM07へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 ログとの照合 PGM07</strong></p><p>検証目的: プログラム管理のPROGRAM資源について操作とログを対応し、PGM07のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM07)を指定し、PGM07のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM07)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM07) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM07)を指定し、PGM07の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM07)
→ Enter を押す
［画面・出力］
Tas(0064107) Prog(PGM07) Tra(PAY07) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM07) GROUP(GRP07)を指定し、PGM07の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM07) GROUP(GRP07)
→ Enter を押す
［画面・出力］
PROGRAM(PGM07) GROUP(GRP07) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Prog が画面・出力に表示されること
② ステップ2 の Status が画面・出力に表示されること
③ ステップ3 の PROGRAM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0194"><h3>プログラム管理 PROGRAM資源 代替経路の確認 PGM10</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>代替経路の確認では プログラム管理 の プログラム照会 を主操作として PGM10 を判定します。主経路との役割差への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM10 に残します。代替経路の確認を補助する 使用タスク確認 では Status を補助値として PGM10 へ保存します。主判定の代替経路の確認ではプログラム管理・資源の プログラム照会 から Prog を読み PGM10 へ残します。証跡照合の代替経路の確認ではプログラム管理・資源の Prog と Status を PGM10 に保存します。記録対応の代替経路の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM10 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で プログラム管理 の プログラム照会 と 使用タスク確認 を実施し PROGRAM資源 の役割を確認します。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE PROGRAM(PGM10)のコマンド文字列だけを記録する。Progを含む応答行は保存しない。</li><li>B. PROGRAM資源の停止または再定義を実施する。その後にCEMT INQUIRE PROGRAM(PGM10)でProgを採取する。</li><li>C. リソース定義のグループ名とインストール結果を確認する。その値をプログラム管理のPGM10にも適用する。</li><li>D. CEMT INQUIRE PROGRAM(PGM10)とCEMT INQUIRE TASK PROGRAM(PGM10)の対象名をそろえる。前者のProgをPROGRAM名とNEWCOPY結果の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として代替手段の成立を確認しPGM10に残します。
運用上の背景: 代替経路の確認では使用タスク確認を補助操作としPROGRAM資源の主経路との役割差をStatusと対象PGM10で照合します。
候補別の検討: プログラム照会と使用タスク確認の役割を分けるとA: 入力記録だけではPROGRAM名とNEWCOPY結果を証明できない点で一次資料と一致しません、B: 変更前のPROGRAM名とNEWCOPY結果を失う点でPROGRAM名とNEWCOPY結果を確認できません、C: リソース定義の値ではProgを確認できない点で使用タスク確認の範囲を越えます、D: 同じ対象名のProgを採用する点で現在値を示します。結論として代替経路の確認のプログラム管理・資源で判定する対象は PGM10 です。
重要用語の定義: 代替経路の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM10へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 代替経路の確認 PGM10</strong></p><p>検証目的: プログラム管理のPROGRAM資源について代替手段の成立を確認し、PGM10のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM10)を指定し、PGM10のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM10)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM10) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM10)を指定し、PGM10の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM10)
→ Enter を押す
［画面・出力］
Tas(0064110) Prog(PGM10) Tra(PAY10) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM10) GROUP(GRP10)を指定し、PGM10の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM10) GROUP(GRP10)
→ Enter を押す
［画面・出力］
PROGRAM(PGM10) GROUP(GRP10) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Prog が画面・出力に表示されること
② ステップ2 の Status が画面・出力に表示されること
③ ステップ3 の PROGRAM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0195"><h3>プログラム管理 PROGRAM資源 変更前の確認 PGM02</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>変更前の確認では プログラム管理 の 使用タスク確認 を主操作として PGM02 を判定します。変更対象と非対象の境界への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM02 に残します。変更前の確認を補助する 定義参照 では PROGRAM を補助値として PGM02 へ保存します。主判定の変更前の確認ではプログラム管理・資源の 使用タスク確認 から Status を読み PGM02 へ残します。証跡照合の変更前の確認ではプログラム管理・資源の Status と PROGRAM を PGM02 に保存します。記録対応の変更前の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM02 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で プログラム管理 の 使用タスク確認 と 定義参照 の役割を分け 変更対象と非対象の境界 を調べます。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE TASK PROGRAM(PGM02)を対象名なしで実行する。一覧の先頭行をPGM02の結果として記録する。</li><li>B. 前回保存したCEMT INQUIRE TASK PROGRAM(PGM02)の結果を使う。今回のCEDA VIEW PROGRAM(PGM02) GROUP(GRP02)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのPGM02の出力を再利用する。今回のCEMT INQUIRE TASK PROGRAM(PGM02)とCEDA VIEW PROGRAM(PGM02) GROUP(GRP02)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象PGM02についてCEMT INQUIRE TASK PROGRAM(PGM02)の応答からStatusを確認する。CEDA VIEW PROGRAM(PGM02) GROUP(GRP02)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは使用タスク確認で Status を読みPROGRAM名とNEWCOPY結果の主値として変更前の証跡を保存しPGM02に残します。
動作の背景: 変更前の確認では定義参照を補助操作としPROGRAM資源の変更対象と非対象の境界をPROGRAMと対象PGM02で照合します。
各選択肢の検討: 使用タスク確認と定義参照の役割を分けるとA: 先頭行はPGM02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で使用タスク確認を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でプログラム管理に使いません、D: Statusと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のプログラム管理・資源で判定する対象は PGM02 です。
初出用語の定義: 変更前の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM02へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 変更前の確認 PGM02</strong></p><p>検証目的: プログラム管理のPROGRAM資源について変更前の証跡を保存し、PGM02のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM02)を指定し、PGM02の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM02)
→ Enter を押す
［画面・出力］
Tas(0064102) Prog(PGM02) Tra(PAY02) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM02) GROUP(GRP02)を指定し、PGM02の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM02) GROUP(GRP02)
→ Enter を押す
［画面・出力］
PROGRAM(PGM02) GROUP(GRP02) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM02)を指定し、PGM02のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM02)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM02) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Status が画面・出力に表示されること
② ステップ2 の PROGRAM が画面・出力に表示されること
③ ステップ3 の Prog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0196"><h3>プログラム管理 PROGRAM資源 変更後の確認 PGM03</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>変更後の確認では プログラム管理 の 定義参照 を主操作として PGM03 を判定します。反映値と残存値への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM03 に残します。変更後の確認を補助する プログラム照会 では Prog を補助値として PGM03 へ保存します。主判定の変更後の確認ではプログラム管理・資源の 定義参照 から PROGRAM を読み PGM03 へ残します。証跡照合の変更後の確認ではプログラム管理・資源の PROGRAM と Prog を PGM03 に保存します。記録対応の変更後の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM03 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で プログラム管理 の 定義参照 と プログラム照会 を使い 変更結果を検証 します。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。PROGRAM を読み対象 PGM03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE PROGRAM(PGM03)で周辺状態を押さえる。その後にCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)でPROGRAMを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. PROGRAM資源の停止または再定義を実施する。その後にCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)でPROGRAMを採取する。</li><li>C. Liberty JVMのJVMSTATUSとPROFILEを確認する。その値をプログラム管理のPGM03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。PROGRAM資源の反映値と残存値は確認済みとして扱う。さらにCEMT INQUIRE TASK PROGRAM(PGM03)のStatusをPROGRAMと同種の値として併記する。</li><li>D. CEMT INQUIRE PROGRAM(PGM03)が成功したためCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)のPROGRAMも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aは定義参照で PROGRAM を読みPROGRAM名とNEWCOPY結果の主値として変更結果を検証しPGM03に残します。
内部の仕組み: 変更後の確認ではプログラム照会を補助操作としPROGRAM資源の反映値と残存値をProgと対象PGM03で照合します。
誤答を含む比較: 定義参照とプログラム照会の役割を分けるとA: 周辺状態の後にPROGRAMを確認する点でPGM03を判定できます、B: 変更前のPROGRAM名とNEWCOPY結果を失う点でプログラム照会の範囲を越えます、C: Liberty JVMの値ではPROGRAMを確認できないうえに追加前提も不正な点でPGM03の値を示しません、D: 補助操作の成功ではPROGRAMを確定できない点で変更後の確認に合いません。結論として変更後の確認のプログラム管理・資源で判定する対象は PGM03 です。
用語定義: 変更後の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM03へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 変更後の確認 PGM03</strong></p><p>検証目的: プログラム管理のPROGRAM資源について変更結果を検証し、PGM03のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM03) GROUP(GRP03)を指定し、PGM03の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM03) GROUP(GRP03)
→ Enter を押す
［画面・出力］
PROGRAM(PGM03) GROUP(GRP03) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM03)を指定し、PGM03のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM03)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM03) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM03)を指定し、PGM03の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM03)
→ Enter を押す
［画面・出力］
Tas(0064103) Prog(PGM03) Tra(PAY03) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PROGRAM が画面・出力に表示されること
② ステップ2 の Prog が画面・出力に表示されること
③ ステップ3 の Status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0197"><h3>プログラム管理 PROGRAM資源 引継ぎ記録 PGM09</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>引継ぎ記録では プログラム管理 の 定義参照 を主操作として PGM09 を判定します。次担当者が追跡できる証跡への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM09 に残します。引継ぎ記録を補助する プログラム照会 では Prog を補助値として PGM09 へ保存します。主判定の引継ぎ記録ではプログラム管理・資源の 定義参照 から PROGRAM を読み PGM09 へ残します。証跡照合の引継ぎ記録ではプログラム管理・資源の PROGRAM と Prog を PGM09 に保存します。記録対応の引継ぎ記録ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM09 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で プログラム管理 の 定義参照 と プログラム照会 を使い 再現可能な記録を作成 します。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。PROGRAM を読み対象 PGM09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE PROGRAM(PGM09)が成功したためCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)のPROGRAMも正常だと推定する。主出力は保存しない。</li><li>B. CEDA VIEW PROGRAM(PGM09) GROUP(GRP09)を対象名なしで実行する。一覧の先頭行をPGM09の結果として記録する。</li><li>C. 対象名PGM09を指定してCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)を実行する。応答中のPROGRAMと時刻を保存する。CEMT INQUIRE PROGRAM(PGM09)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)の結果を使う。今回のCEMT INQUIRE PROGRAM(PGM09)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cは定義参照で PROGRAM を読みPROGRAM名とNEWCOPY結果の主値として再現可能な記録を作成しPGM09に残します。
製品内の仕組み: 引継ぎ記録ではプログラム照会を補助操作としPROGRAM資源の次担当者が追跡できる証跡をProgと対象PGM09で照合します。
選択肢別の説明: 定義参照とプログラム照会の役割を分けるとA: 補助操作の成功ではPROGRAMを確定できない点でPGM09の値を示しません、B: 先頭行はPGM09と確定できない点で引継ぎ記録に合いません、C: PROGRAMと時刻を保存する点で定義参照に合います、D: 採取時刻が異なる点でプログラム管理に使いません。結論として引継ぎ記録のプログラム管理・資源で判定する対象は PGM09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM09へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 引継ぎ記録 PGM09</strong></p><p>検証目的: プログラム管理のPROGRAM資源について再現可能な記録を作成し、PGM09のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM09) GROUP(GRP09)を指定し、PGM09の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM09) GROUP(GRP09)
→ Enter を押す
［画面・出力］
PROGRAM(PGM09) GROUP(GRP09) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM09)を指定し、PGM09のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM09)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM09) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM09)を指定し、PGM09の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM09)
→ Enter を押す
［画面・出力］
Tas(0064109) Prog(PGM09) Tra(PAY09) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PROGRAM が画面・出力に表示されること
② ステップ2 の Prog が画面・出力に表示されること
③ ステップ3 の Status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0198"><h3>プログラム管理 PROGRAM資源 復旧後の確認 PGM06</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>復旧後の確認では プログラム管理 の 定義参照 を主操作として PGM06 を判定します。再発していないことを示す値への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM06 に残します。復旧後の確認を補助する プログラム照会 では Prog を補助値として PGM06 へ保存します。主判定の復旧後の確認ではプログラム管理・資源の 定義参照 から PROGRAM を読み PGM06 へ残します。証跡照合の復旧後の確認ではプログラム管理・資源の PROGRAM と Prog を PGM06 に保存します。記録対応の復旧後の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM06 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で プログラム管理 の 定義参照 と プログラム照会 を照合し 再発していないことを示す値 を確かめます。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。PROGRAM を読む前に対象 PGM06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. トレースのTRACETYPEとSTATUSを確認する。その値をプログラム管理のPGM06にも適用する。</li><li>B. CEMT INQUIRE PROGRAM(PGM06)が成功したためCEDA VIEW PROGRAM(PGM06) GROUP(GRP06)のPROGRAMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象PGM06へ引き継げるものとする。PROGRAM資源の再発していないことを示す値は確認済みとして扱う。さらにCEMT INQUIRE TASK PROGRAM(PGM06)のStatusをPROGRAMと同種の値として併記する。</li><li>C. CEDA VIEW PROGRAM(PGM06) GROUP(GRP06)を対象名なしで実行する。一覧の先頭行をPGM06の結果として記録する。</li><li>D. CEDA VIEW PROGRAM(PGM06) GROUP(GRP06)でPROGRAMを取得してからCEMT INQUIRE TASK PROGRAM(PGM06)でStatusを照合する。PGM06のPROGRAM名とNEWCOPY結果を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dは定義参照で PROGRAM を読みPROGRAM名とNEWCOPY結果の主値として復旧後の安定性を確認しPGM06に残します。
構成上の背景: 復旧後の確認ではプログラム照会を補助操作としPROGRAM資源の再発していないことを示す値をProgと対象PGM06で照合します。
候補ごとの理由: 定義参照とプログラム照会の役割を分けるとA: トレースの値ではPROGRAMを確認できない点でプログラム照会の範囲を越えます、B: 補助操作の成功ではPROGRAMを確定できないうえに追加前提も不正な点でPGM06の値を示しません、C: 先頭行はPGM06と確定できない点で復旧後の確認に合いません、D: PROGRAMとStatusを順に照合する点で定義参照に合います。結論として復旧後の確認のプログラム管理・資源で判定する対象は PGM06 です。
初出用語: 復旧後の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM06へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 復旧後の確認 PGM06</strong></p><p>検証目的: プログラム管理のPROGRAM資源について復旧後の安定性を確認し、PGM06のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM06) GROUP(GRP06)を指定し、PGM06の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM06) GROUP(GRP06)
→ Enter を押す
［画面・出力］
PROGRAM(PGM06) GROUP(GRP06) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM06)を指定し、PGM06のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM06)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM06) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM06)を指定し、PGM06の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM06)
→ Enter を押す
［画面・出力］
Tas(0064106) Prog(PGM06) Tra(PAY06) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PROGRAM が画面・出力に表示されること
② ステップ2 の Prog が画面・出力に表示されること
③ ステップ3 の Status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0199"><h3>プログラム管理 PROGRAM資源 復旧準備 PGM05</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>復旧準備では プログラム管理 の 使用タスク確認 を主操作として PGM05 を判定します。再開前に必要な整合性への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM05 に残します。復旧準備を補助する 定義参照 では PROGRAM を補助値として PGM05 へ保存します。主判定の復旧準備ではプログラム管理・資源の 使用タスク確認 から Status を読み PGM05 へ残します。証跡照合の復旧準備ではプログラム管理・資源の Status と PROGRAM を PGM05 に保存します。記録対応の復旧準備ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM05 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で プログラム管理 の 使用タスク確認 と 定義参照 を用い 復旧条件を確認 します。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。Status で対象 PGM05 の PROGRAM名とNEWCOPY結果 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したCEMT INQUIRE TASK PROGRAM(PGM05)の結果を使う。今回のCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのPGM05の出力を再利用する。今回のCEMT INQUIRE TASK PROGRAM(PGM05)とCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)は実行済みとして扱う。</li><li>C. 変更を加えずCEMT INQUIRE TASK PROGRAM(PGM05)を実行する。Statusを保存する。差分はCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. CEDA VIEW PROGRAM(PGM05) GROUP(GRP05)のPROGRAMをPROGRAM名とNEWCOPY結果の主判定に採用する。CEMT INQUIRE TASK PROGRAM(PGM05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは使用タスク確認で Status を読みPROGRAM名とNEWCOPY結果の主値として復旧条件を確認しPGM05に残します。
処理の仕組み: 復旧準備では定義参照を補助操作としPROGRAM資源の再開前に必要な整合性をPROGRAMと対象PGM05で照合します。
選択結果の内訳: 使用タスク確認と定義参照の役割を分けるとA: 採取時刻が異なる点で使用タスク確認を代替しません、B: 過去出力では今回の復旧準備を示せない点でプログラム管理に使いません、C: 変更前のStatusを保存する点で正答です、D: PROGRAMはStatusを代替しないうえに追加前提も不正な点でPGM05を採用できません。結論として復旧準備のプログラム管理・資源で判定する対象は PGM05 です。
用語の説明: 復旧準備で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM05へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 復旧準備 PGM05</strong></p><p>検証目的: プログラム管理のPROGRAM資源について復旧条件を確認し、PGM05のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM05)を指定し、PGM05の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM05)
→ Enter を押す
［画面・出力］
Tas(0064105) Prog(PGM05) Tra(PAY05) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM05) GROUP(GRP05)を指定し、PGM05の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM05) GROUP(GRP05)
→ Enter を押す
［画面・出力］
PROGRAM(PGM05) GROUP(GRP05) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM05)を指定し、PGM05のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM05)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM05) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Status が画面・出力に表示されること
② ステップ2 の PROGRAM が画面・出力に表示されること
③ ステップ3 の Prog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0200"><h3>プログラム管理 PROGRAM資源 構成監査 PGM08</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>構成監査では プログラム管理 の 使用タスク確認 を主操作として PGM08 を判定します。定義値と稼働値の一致への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM08 に残します。構成監査を補助する 定義参照 では PROGRAM を補助値として PGM08 へ保存します。主判定の構成監査ではプログラム管理・資源の 使用タスク確認 から Status を読み PGM08 へ残します。証跡照合の構成監査ではプログラム管理・資源の Status と PROGRAM を PGM08 に保存します。記録対応の構成監査ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM08 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で プログラム管理 の 使用タスク確認 と 定義参照 の役割を分け 定義値と稼働値の一致 を調べます。PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源です。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのPGM08の出力を再利用する。今回のCEMT INQUIRE TASK PROGRAM(PGM08)とCEDA VIEW PROGRAM(PGM08) GROUP(GRP08)は実行済みとして扱う。</li><li>B. CEDA VIEW PROGRAM(PGM08) GROUP(GRP08)の結果だけでは確定しない。CEMT INQUIRE TASK PROGRAM(PGM08)のStatusを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEDA VIEW PROGRAM(PGM08) GROUP(GRP08)のPROGRAMをPROGRAM名とNEWCOPY結果の主判定に採用する。CEMT INQUIRE TASK PROGRAM(PGM08)の応答は採取対象から外す。</li><li>D. CEMT INQUIRE PROGRAM(PGM08)のProgをStatusと同義の成功表示として扱う。CEMT INQUIRE TASK PROGRAM(PGM08)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bは使用タスク確認で Status を読みPROGRAM名とNEWCOPY結果の主値として構成差分を監査しPGM08に残します。
実行時の背景: 構成監査では定義参照を補助操作としPROGRAM資源の定義値と稼働値の一致をPROGRAMと対象PGM08で照合します。
四つの候補の理由: 使用タスク確認と定義参照の役割を分けるとA: 過去出力では今回の構成監査を示せない点でプログラム管理に使いません、B: Statusを主証跡として区別する点で正答です、C: PROGRAMはStatusを代替しない点でPGM08を採用できません、D: ProgとStatusは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のプログラム管理・資源で判定する対象は PGM08 です。
初出語定義: 構成監査で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM08へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 構成監査 PGM08</strong></p><p>検証目的: プログラム管理のPROGRAM資源について構成差分を監査し、PGM08のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM08)を指定し、PGM08の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM08)
→ Enter を押す
［画面・出力］
Tas(0064108) Prog(PGM08) Tra(PAY08) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM08) GROUP(GRP08)を指定し、PGM08の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM08) GROUP(GRP08)
→ Enter を押す
［画面・出力］
PROGRAM(PGM08) GROUP(GRP08) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM08)を指定し、PGM08のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM08)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM08) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Status が画面・出力に表示されること
② ステップ2 の PROGRAM が画面・出力に表示されること
③ ステップ3 の Prog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0201"><h3>プログラム管理 PROGRAM資源 通常状態の確認 PGM01</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>通常状態の確認では プログラム管理 の プログラム照会 を主操作として PGM01 を判定します。基準値と現在値の差への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM01 に残します。通常状態の確認を補助する 使用タスク確認 では Status を補助値として PGM01 へ保存します。主判定の通常状態の確認ではプログラム管理・資源の プログラム照会 から Prog を読み PGM01 へ残します。証跡照合の通常状態の確認ではプログラム管理・資源の Prog と Status を PGM01 に保存します。記録対応の通常状態の確認ではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM01 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で プログラム管理 の プログラム照会 と 使用タスク確認 を組み合わせる際は PROGRAM資源 がロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源という仕組みを前提にします。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。Prog と PROGRAM名とNEWCOPY結果 を対象 PGM01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE TASK PROGRAM(PGM01)のStatusをPROGRAM名とNEWCOPY結果の主判定に採用する。CEMT INQUIRE PROGRAM(PGM01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. CEDA VIEW PROGRAM(PGM01) GROUP(GRP01)のPROGRAMをProgと同義の成功表示として扱う。CEMT INQUIRE PROGRAM(PGM01)は実行しない。</li><li>C. CEMT INQUIRE PROGRAM(PGM01)を先に実行する。対象PGM01のProgをPROGRAM名とNEWCOPY結果として記録する。続いてCEMT INQUIRE TASK PROGRAM(PGM01)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. CEMT INQUIRE PROGRAM(PGM01)が応答を返した時点で正常とする。応答中のProgの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として通常状態を確定しPGM01に残します。
背景・仕組み: 通常状態の確認では使用タスク確認を補助操作としPROGRAM資源の基準値と現在値の差をStatusと対象PGM01で照合します。
選択肢の理由: プログラム照会と使用タスク確認の役割を分けるとA: StatusはProgを代替しないうえに追加前提も不正な点でPROGRAM資源に使えません、B: PROGRAMとProgは確認項目が異なる点でPGM01を採用できません、C: Progを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではPROGRAM名とNEWCOPY結果を判定できない点で一次資料と一致しません。結論として通常状態の確認のプログラム管理・資源で判定する対象は PGM01 です。
用語の初出定義: 通常状態の確認で使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM01へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 通常状態の確認 PGM01</strong></p><p>検証目的: プログラム管理のPROGRAM資源について通常状態を確定し、PGM01のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM01)を指定し、PGM01のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM01)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM01) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM01)を指定し、PGM01の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM01)
→ Enter を押す
［画面・出力］
Tas(0064101) Prog(PGM01) Tra(PAY01) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM01) GROUP(GRP01)を指定し、PGM01の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM01) GROUP(GRP01)
→ Enter を押す
［画面・出力］
PROGRAM(PGM01) GROUP(GRP01) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Prog が画面・出力に表示されること
② ステップ2 の Status が画面・出力に表示されること
③ ステップ3 の PROGRAM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0202"><h3>プログラム管理 PROGRAM資源 障害切り分け PGM04</h3><p class="kb-meta">分類: プログラム管理 ・ 難易度: 中級</p><p>障害切り分けでは プログラム管理 の プログラム照会 を主操作として PGM04 を判定します。最初に失敗した処理への注意として「使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります」を PGM04 に残します。障害切り分けを補助する 使用タスク確認 では Status を補助値として PGM04 へ保存します。主判定の障害切り分けではプログラム管理・資源の プログラム照会 から Prog を読み PGM04 へ残します。証跡照合の障害切り分けではプログラム管理・資源の Prog と Status を PGM04 に保存します。記録対応の障害切り分けではプログラム管理・資源の PROGRAM名とNEWCOPY結果 の証跡へ PGM04 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで プログラム管理 の プログラム照会 と 使用タスク確認 を実施し PROGRAM資源 の役割を確認します。使用中プログラムへNEWCOPYを適用して実行世代を混在させる危険があります。対象 PGM04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. CEDA VIEW PROGRAM(PGM04) GROUP(GRP04)のPROGRAMをProgと同義の成功表示として扱う。CEMT INQUIRE PROGRAM(PGM04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. CEMT INQUIRE PROGRAM(PGM04)の出力でPGM04とProgが同じ応答にあることを確認する。PROGRAM名とNEWCOPY結果をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEMT INQUIRE PROGRAM(PGM04)が応答を返した時点で正常とする。応答中のProgの値は記録しない。</li><li>D. CEMT INQUIRE PROGRAM(PGM04)のコマンド文字列だけを記録する。Progを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bはプログラム照会で Prog を読みPROGRAM名とNEWCOPY結果の主値として障害範囲を限定しPGM04に残します。
技術的背景: 障害切り分けでは使用タスク確認を補助操作としPROGRAM資源の最初に失敗した処理をStatusと対象PGM04で照合します。
四択の評価: プログラム照会と使用タスク確認の役割を分けるとA: PROGRAMとProgは確認項目が異なるうえに追加前提も不正な点でPGM04を採用できません、B: PGM04とProgを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではPROGRAM名とNEWCOPY結果を判定できない点で一次資料と一致しません、D: 入力記録だけではPROGRAM名とNEWCOPY結果を証明できない点でPROGRAM名とNEWCOPY結果を確認できません。結論として障害切り分けのプログラム管理・資源で判定する対象は PGM04 です。
初出語の意味: 障害切り分けで使う PROGRAM資源 はロードモジュール名、言語、使用数、NEWCOPY状態をCICS領域内で管理する資源を表しPROGRAM名とNEWCOPY結果を判定する際にPGM04へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム管理 PROGRAM資源 障害切り分け PGM04</strong></p><p>検証目的: プログラム管理のPROGRAM資源について障害範囲を限定し、PGM04のPROGRAM名とNEWCOPY結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象PGM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE PROGRAM(PGM04)を指定し、PGM04のプログラム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(PGM04)
→ Enter を押す
［画面・出力］
STATUS: RESULTS
Prog(PGM04) Ena Resc Language(COBOL) Usecount(00000004)
画面・出力にあるProgを読み、PROGRAM名とNEWCOPY結果と対象PGM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEMT INQUIRE TASK PROGRAM(PGM04)を指定し、PGM04の使用タスク確認を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE TASK PROGRAM(PGM04)
→ Enter を押す
［画面・出力］
Tas(0064104) Prog(PGM04) Tra(PAY04) Status(RUNNING)
画面・出力にあるStatusを読み、PROGRAM名とNEWCOPY結果と対象PGM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのプログラム管理を確認する入力画面です。COMMAND入力口へCEDA VIEW PROGRAM(PGM04) GROUP(GRP04)を指定し、PGM04の定義参照を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA VIEW PROGRAM(PGM04) GROUP(GRP04)
→ Enter を押す
［画面・出力］
PROGRAM(PGM04) GROUP(GRP04) STATUS(ENABLED) DATALOCATION(ANY)
画面・出力にあるPROGRAMを読み、PROGRAM名とNEWCOPY結果と対象PGM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Prog が画面・出力に表示されること
② ステップ2 の Status が画面・出力に表示されること
③ ステップ3 の PROGRAM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


## メイン端末運用


<section class="kb-item" id="c04-i0203"><h3>CEDA DEFINE TCPIPSERVICE 状態確認 出力比較</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEDA DEFINE TCPIPSERVICE 状態確認 出力比較」は、CICS Web SupportやIPICの入口となるTCPIPSERVICEを定義するRDO操作を状態確認の観点で確認する技術項目です。FILE 欄とPAY040を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、タスク待機理由の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEDA DEFINE TCPIPSERVICE 状態確認 出力比較</strong></p><p>検証目的: メイン端末運用におけるCEDA DEFINE TCPIPSERVICEの状態確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=PAY040</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; Open Tasks view for CIC40
→ Enter を押す
［画面・出力］
Tasks view APPLID CIC40
Task 0051988 Transaction CWXN Status Suspended Wait RECEIVE
画面・出力には Tasks が含まれ、Tasksを確認し、タスク待機理由の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; GET CICSDefinitionTCPIPService TCP10
→ Enter を押す
［画面・出力］
&lt;response&gt;&lt;TCPIPSERVICE name=&quot;TCP10&quot; status=&quot;OPEN&quot; port=&quot;8080&quot; protocol=&quot;HTTP&quot; /&gt;&lt;/response&gt;
画面・出力には response が含まれ、responseを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; GET CICSDefinitionTransaction PAY040
→ Enter を押す
［画面・出力］
&lt;response&gt;&lt;TRANSACTION name=&quot;PAY040&quot; program=&quot;DFH040&quot; status=&quot;ENABLED&quot; /&gt;&lt;/response&gt;
画面・出力には response が含まれ、responseを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の Tasks が画面・出力に表示されること
② ステップ2 の response が画面・出力に表示されること
③ ステップ3 の response が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0204"><h3>CEMT INQUIRE TASK 状態確認 状態確認</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT INQUIRE TASK 状態確認 状態確認」は、ユーザータスクのTASKID、TRANID、UOW、待機理由、TCB種別を表示するメイン端末コマンドを状態確認の観点で確認する技術項目です。Uow 欄とDFH001を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT INQUIRE TASK 状態確認 状態確認</strong></p><p>検証目的: メイン端末運用におけるCEMT INQUIRE TASKの状態確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=DFH001</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TASK
→ Enter を押す
［画面・出力］
Tas(0000100) Tra(PAY001) Sus Tas Pri(001) Sta(U) Use(USR001)
Uow(C9D5F2EE2DEE0000) Hty(SOCKET) Hva(RECEIVE) Bac Wai
画面・出力には PAY001 が含まれ、PAY001を確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TRANSACTION(PAY001)
→ Enter を押す
［画面・出力］
Tra(PAY001) Pri(001) Pro(DFH001) Ena Sta Pro Ena Resc(DFHPROF)
画面・出力には PAY001 が含まれ、PAY001を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(DFH001)
→ Enter を押す
［画面・出力］
Pro(DFH001) Leng(0001234) Resc(0001) Ced Ena Pri Dplsubsys(CICS)
画面・出力には DFH001 が含まれ、DFH001を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の PAY001 が画面・出力に表示されること
② ステップ2 の PAY001 が画面・出力に表示されること
③ ステップ3 の DFH001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0205"><h3>CEMT INQUIRE TRANSACTION トレース確認 再開位置</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 上級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT INQUIRE TRANSACTION トレース確認 再開位置」は、トランザクション定義、利用可否、プロファイル、実行属性を確認するメイン端末コマンドをトレース確認の観点で確認する技術項目です。DFH メッセージとFILE092を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT INQUIRE TRANSACTION トレース確認 再開位置</strong></p><p>検証目的: メイン端末運用におけるCEMT INQUIRE TRANSACTIONのトレース確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=FILE092</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE092)
→ Enter を押す
［画面・出力］
Fil(FILE092) Vsa Ope Ena Rea Upd Add Bro Del Sha
画面・出力には FILE092 が含まれ、FILE092を確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET FILE(FILE092) CLOSED ENABLED
→ Enter を押す
［画面・出力］
Fil(FILE092) Clo Ena Rea Upd Add Bro Del
画面・出力には FILE092 が含まれ、FILE092を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE092)
→ Enter を押す
［画面・出力］
Fil(FILE092) Clo Ena Rea Upd Add Bro Del
画面・出力には FILE092 が含まれ、FILE092を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の FILE092 が画面・出力に表示されること
② ステップ2 の FILE092 が画面・出力に表示されること
③ ステップ3 の FILE092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0206"><h3>CEMT SET SYD 接続確認 更新対象</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT SET SYD 接続確認 更新対象」は、DFHメッセージに対するシステムダンプ取得条件を設定する操作を接続確認の観点で確認する技術項目です。TCPIPSERVICE 行と00152を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT SET SYD 接続確認 更新対象</strong></p><p>検証目的: メイン端末運用におけるCEMT SET SYDの接続確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=00152</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TCPIPSERVICE(TCP23)
→ Enter を押す
［画面・出力］
Tcp(TCP23) Ope Por(08080) Pro(Http) Backlog(00050) Urm(DFHWBAAX)
画面・出力には TCP23 が含まれ、TCP23を確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET TCPIPSERVICE(TCP23) OPEN
→ Enter を押す
［画面・出力］
Tcp(TCP23) Ope Por(08080) Pro(Http) Backlog(00050)
画面・出力には TCP23 が含まれ、TCP23を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TCPIP
→ Enter を押す
［画面・出力］
Tcpip Open ActSockets(000012) ActSslTcbs(000002)
画面・出力には Tcpip が含まれ、Tcpipを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の TCP23 が画面・出力に表示されること
② ステップ2 の TCP23 が画面・出力に表示されること
③ ステップ3 の Tcpip が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0207"><h3>CEMT SET TCPIPSERVICE 戻りコード確認 実行順序</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CEMT SET TCPIPSERVICE 戻りコード確認 実行順序」は、TCP/IPサービスのOPEN/CLOSEやBACKLOGなどを即時変更するメイン端末操作を戻りコード確認の観点で確認する技術項目です。PORTNUMBER 欄とURI06を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Db2接続前提の欠落を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT SET TCPIPSERVICE 戻りコード確認 実行順序</strong></p><p>検証目的: メイン端末運用におけるCEMT SET TCPIPSERVICEの戻りコード確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=URI06</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET TRD(AEI5) SYS MAX(1) ADD
→ Enter を押す
［画面・出力］
Trd(AEI5) Sys Cur(000000) Max(000001) Add
画面・出力には AEI5 が含まれ、AEI5を確認し、Db2接続前提の欠落を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TRD(AEI5)
→ Enter を押す
［画面・出力］
Trd(AEI5) Sys Cur(000000) Max(000001) Add
画面・出力には AEI5 が含まれ、AEI5を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET SYD(12345) SYS MAX(1) ADD
→ Enter を押す
［画面・出力］
SYDUMP Syd(12345) Sys Cur(000000) Max(000001) Add
画面・出力には SYDUMP が含まれ、SYDUMPを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の AEI5 が画面・出力に表示されること
② ステップ2 の AEI5 が画面・出力に表示されること
③ ステップ3 の SYDUMP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0208"><h3>CICS Explorer Tasks view リソース照合 ボリューム状態</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CICS Explorer Tasks view リソース照合 ボリューム状態」は、CEMT INQUIRE TASK相当のタスク情報をGUIで確認するビューをリソース照合の観点で確認する技術項目です。PROGRAM 欄とJVMSRV07を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、未インストール定義の採用を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CICS Explorer Tasks view リソース照合 ボリューム状態</strong></p><p>検証目的: メイン端末運用におけるCICS Explorer Tasks viewのリソース照合を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=JVMSRV07</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CETR
→ Enter を押す
［画面・出力］
CETR CICS TRACE CONTROL
MAIN SYSTEM TRACE FLAG ==&gt; OFF
AUXILIARY TRACE STATUS ==&gt; STARTED
画面・出力には CETR が含まれ、CETRを確認し、未インストール定義の採用を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; VERBX DFHPD760 &#x27;TR=1&#x27;
→ Enter を押す
［画面・出力］
DFHPD760 CICS TRACE FORMATTER
TRACE ENTRIES SELECTED FOR APPLID CIC27
RETURN CODE = 0000
画面・出力には DFHPD760 が含まれ、DFHPD760を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; SUBMIT CICS.DFHTU760.CNTL(TRACE)
→ Enter を押す
［画面・出力］
DFHTU760 AUXILIARY TRACE PRINT UTILITY
ABBREVIATED TRACE PRINTED
RETURN CODE = 0000
画面・出力には DFHTU760 が含まれ、DFHTU760を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CETR が画面・出力に表示されること
② ステップ2 の DFHPD760 が画面・出力に表示されること
③ ステップ3 の DFHTU760 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0209"><h3>CICS-MQ bridge 接続確認 停止確認</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「CICS-MQ bridge 接続確認 停止確認」は、MQメッセージから3270トランザクションを起動し、CEMTなどを橋渡しする連携機能を接続確認の観点で確認する技術項目です。TCB 欄とCIC14を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、TCP/IPサービス状態の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CICS-MQ bridge 接続確認 停止確認</strong></p><p>検証目的: メイン端末運用におけるCICS-MQ bridgeの接続確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC14</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE TRANSACTION(PAY014) GROUP(TEST) PROGRAM(DFH014)
→ Enter を押す
［画面・出力］
CEDA DEF TRANSACTION(PAY014) GROUP(TEST)
PROGRAM ==&gt; DFH014
PROFILE ==&gt; DFHCICST
画面・出力には CEDA が含まれ、CEDAを確認し、TCP/IPサービス状態の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE PROGRAM(DFH014) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF PROGRAM(DFH014) GROUP(TEST)
LANGUAGE ==&gt; COBOL
STATUS ==&gt; ENABLED
画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(TEST)
→ Enter を押す
［画面・出力］
INSTALL SUCCESSFUL FOR GROUP TEST
TRANSACTION PAY014 INSTALLED
PROGRAM DFH014 INSTALLED
画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
② ステップ2 の CEDA が画面・出力に表示されること
③ ステップ3 の INSTALL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0210"><h3>DFHTU trace utility 状態確認 出力見出し</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の メイン端末運用 で扱う「DFHTU trace utility 状態確認 出力見出し」は、補助トレースデータを整形して問題判別に使うCICSトレースユーティリティを状態確認の観点で確認する技術項目です。URIMAP 行とAEI8を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFHTU trace utility 状態確認 出力見出し</strong></p><p>検証目的: メイン端末運用におけるDFHTU trace utilityの状態確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=AEI8</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; PUT CICS bridge message for CEMT INQUIRE TASK
→ Enter を押す
［画面・出力］
CICS-MQ BRIDGE REQUEST ACCEPTED
TRANSACTION CEMT
COMMAND CEMT INQUIRE TASK
画面・出力には CICS-MQ が含まれ、CICS-MQを確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TASK TRAN(CWXN)
→ Enter を押す
［画面・出力］
Tas(0051988) Tra(CWXN) Sus Tas Pri(001) Sta(U) Use(WEBSRV)
Uow(C9D5F2EE2DEE8499) Hty(SOCKET) Hva(RECEIVE) Hti(200841) Bac Wai
画面・出力には CWXN が含まれ、CWXNを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TRANSACTION(CWXN)
→ Enter を押す
［画面・出力］
Tra(CWXN) Pri(001) Pro(DFHWBXN) Ena Sta Profile(DFHCICST)
画面・出力には CWXN が含まれ、CWXNを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CICS-MQ が画面・出力に表示されること
② ステップ2 の CWXN が画面・出力に表示されること
③ ステップ3 の CWXN が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0211"><h3>メイン端末運用 CEMTシステム照会 ログとの照合 CIC07</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>ログとの照合では メイン端末運用 の システム照会 を主操作として CIC07 を判定します。時刻と対象識別子への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC07 に残します。ログとの照合を補助する 領域識別 では Applid を補助値として CIC07 へ保存します。主判定のログとの照合ではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC07 へ残します。証跡照合のログとの照合ではメイン端末運用・システム照会の STATUS と Applid を CIC07 に保存します。記録対応のログとの照合ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC07 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で メイン端末運用 の システム照会 と 領域識別 を組み合わせる際は CEMTシステム照会 がCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能という仕組みを前提にします。別領域のCEMT画面で変更を実行する危険があります。STATUS と APPLIDと領域状態 を対象 CIC07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE SYSTEMが応答を返した時点で正常とする。応答中のSTATUSの値は記録しない。DFHST0103IをSTATUSと同じ判定値とみなし対象CIC07の主証跡にする。</li><li>B. CEMT INQUIRE SYSTEMのコマンド文字列だけを記録する。STATUSを含む応答行は保存しない。</li><li>C. STATUSを含むシステム照会の応答行を保存する。その応答を得るためCEMT INQUIRE SYSTEMを使用する。対象CIC07のAPPLIDと領域状態として記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. CEMTシステム照会の停止または再定義を実施する。その後にCEMT INQUIRE SYSTEMでSTATUSを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 適切な判定: Cはシステム照会で STATUS を読みAPPLIDと領域状態の主値として操作とログを対応しCIC07に残します。
機能の仕組み: ログとの照合では領域識別を補助操作としCEMTシステム照会の時刻と対象識別子をApplidと対象CIC07で照合します。
各候補の評価: システム照会と領域識別の役割を分けるとA: 応答の有無だけではAPPLIDと領域状態を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではAPPLIDと領域状態を証明できない点で一次資料と一致しません、C: STATUSの実値を対象別に残す点でCIC07を判定できます、D: 変更前のAPPLIDと領域状態を失う点で領域識別の範囲を越えます。結論としてログとの照合のメイン端末運用・システム照会で判定する対象は CIC07 です。
用語の定義: ログとの照合で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC07へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 ログとの照合 CIC07</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について操作とログを対応し、CIC07のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC07のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC07) Applid(CIC07) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC07の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC07) Cicstslevel(060200) Sysid(CIC07)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC07の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC07 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
② ステップ2 の Applid が画面・出力に表示されること
③ ステップ3 の DFHST0103I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0212"><h3>メイン端末運用 CEMTシステム照会 代替経路の確認 CIC10</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>代替経路の確認では メイン端末運用 の システム照会 を主操作として CIC10 を判定します。主経路との役割差への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC10 に残します。代替経路の確認を補助する 領域識別 では Applid を補助値として CIC10 へ保存します。主判定の代替経路の確認ではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC10 へ残します。証跡照合の代替経路の確認ではメイン端末運用・システム照会の STATUS と Applid を CIC10 に保存します。記録対応の代替経路の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC10 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で メイン端末運用 の システム照会 と 領域識別 を実施し CEMTシステム照会 の役割を確認します。別領域のCEMT画面で変更を実行する危険があります。対象 CIC10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE SYSTEMのコマンド文字列だけを記録する。STATUSを含む応答行は保存しない。</li><li>B. CEMT INQUIRE SYSTEMとCEMT INQUIRE SYSTEM APPLIDの対象名をそろえる。前者のSTATUSをAPPLIDと領域状態の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEMTシステム照会の停止または再定義を実施する。その後にCEMT INQUIRE SYSTEMでSTATUSを採取する。</li><li>D. トレースのTRACETYPEとSTATUSを確認する。その値をメイン端末運用のCIC10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい判定結果: Bはシステム照会で STATUS を読みAPPLIDと領域状態の主値として代替手段の成立を確認しCIC10に残します。
運用上の背景: 代替経路の確認では領域識別を補助操作としCEMTシステム照会の主経路との役割差をApplidと対象CIC10で照合します。
候補別の検討: システム照会と領域識別の役割を分けるとA: 入力記録だけではAPPLIDと領域状態を証明できない点で一次資料と一致しません、B: 同じ対象名のSTATUSを採用する点でCIC10を判定できます、C: 変更前のAPPLIDと領域状態を失う点で領域識別の範囲を越えます、D: トレースの値ではSTATUSを確認できない点でCIC10の値を示しません。結論として代替経路の確認のメイン端末運用・システム照会で判定する対象は CIC10 です。
重要用語の定義: 代替経路の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC10へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 代替経路の確認 CIC10</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について代替手段の成立を確認し、CIC10のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC10のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC10) Applid(CIC10) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC10の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC10) Cicstslevel(060200) Sysid(CIC10)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC10の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC10 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
② ステップ2 の Applid が画面・出力に表示されること
③ ステップ3 の DFHST0103I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0213"><h3>メイン端末運用 CEMTシステム照会 変更前の確認 CIC02</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>変更前の確認では メイン端末運用 の 領域識別 を主操作として CIC02 を判定します。変更対象と非対象の境界への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC02 に残します。変更前の確認を補助する 統計記録 では DFHST0103I を補助値として CIC02 へ保存します。主判定の変更前の確認ではメイン端末運用・システム照会の 領域識別 から Applid を読み CIC02 へ残します。証跡照合の変更前の確認ではメイン端末運用・システム照会の Applid と DFHST0103I を CIC02 に保存します。記録対応の変更前の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC02 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で メイン端末運用 の 領域識別 と 統計記録 の役割を分け 変更対象と非対象の境界 を調べます。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。対象 CIC02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE SYSTEM APPLIDを対象名なしで実行する。一覧の先頭行をCIC02の結果として記録する。</li><li>B. 対象CIC02についてCEMT INQUIRE SYSTEM APPLIDの応答からApplidを確認する。CEMT PERFORM STATISTICS RECORD ALLは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したCEMT INQUIRE SYSTEM APPLIDの結果を使う。今回のCEMT PERFORM STATISTICS RECORD ALLの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのCIC02の出力を再利用する。今回のCEMT INQUIRE SYSTEM APPLIDとCEMT PERFORM STATISTICS RECORD ALLは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: Bは領域識別で Applid を読みAPPLIDと領域状態の主値として変更前の証跡を保存しCIC02に残します。
動作の背景: 変更前の確認では統計記録を補助操作としCEMTシステム照会の変更対象と非対象の境界をDFHST0103Iと対象CIC02で照合します。
各選択肢の検討: 領域識別と統計記録の役割を分けるとA: 先頭行はCIC02と確定できない点で変更前の確認に合いません、B: Applidと補助証跡の時刻を合わせる点で領域識別に合います、C: 採取時刻が異なる点でメイン端末運用に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でCEMTシステム照会に使えません。結論として変更前の確認のメイン端末運用・システム照会で判定する対象は CIC02 です。
初出用語の定義: 変更前の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC02へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 変更前の確認 CIC02</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について変更前の証跡を保存し、CIC02のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC02の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC02) Cicstslevel(060200) Sysid(CIC02)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC02の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC02 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC02のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC02) Applid(CIC02) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Applid が画面・出力に表示されること
② ステップ2 の DFHST0103I が画面・出力に表示されること
③ ステップ3 の STATUS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0214"><h3>メイン端末運用 CEMTシステム照会 変更後の確認 CIC03</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>変更後の確認では メイン端末運用 の 統計記録 を主操作として CIC03 を判定します。反映値と残存値への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC03 に残します。変更後の確認を補助する システム照会 では STATUS を補助値として CIC03 へ保存します。主判定の変更後の確認ではメイン端末運用・システム照会の 統計記録 から DFHST0103I を読み CIC03 へ残します。証跡照合の変更後の確認ではメイン端末運用・システム照会の DFHST0103I と STATUS を CIC03 に保存します。記録対応の変更後の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC03 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で メイン端末運用 の 統計記録 と システム照会 を使い 変更結果を検証 します。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。DFHST0103I を読み対象 CIC03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. CEMTシステム照会の停止または再定義を実施する。その後にCEMT PERFORM STATISTICS RECORD ALLでDFHST0103Iを採取する。</li><li>B. プログラム管理のPROGRAM名とNEWCOPY結果を確認する。その値をメイン端末運用のCIC03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。CEMTシステム照会の反映値と残存値は確認済みとして扱う。さらにCEMT INQUIRE SYSTEM APPLIDのApplidをDFHST0103Iと同種の値として併記する。</li><li>C. CEMT INQUIRE SYSTEMで周辺状態を押さえる。その後にCEMT PERFORM STATISTICS RECORD ALLでDFHST0103Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. CEMT INQUIRE SYSTEMが成功したためCEMT PERFORM STATISTICS RECORD ALLのDFHST0103Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Cは統計記録で DFHST0103I を読みAPPLIDと領域状態の主値として変更結果を検証しCIC03に残します。
内部の仕組み: 変更後の確認ではシステム照会を補助操作としCEMTシステム照会の反映値と残存値をSTATUSと対象CIC03で照合します。
誤答を含む比較: 統計記録とシステム照会の役割を分けるとA: 変更前のAPPLIDと領域状態を失う点でAPPLIDと領域状態を確認できません、B: プログラム管理の値ではDFHST0103Iを確認できないうえに追加前提も不正な点でシステム照会の範囲を越えます、C: 周辺状態の後にDFHST0103Iを確認する点で現在値を示します、D: 補助操作の成功ではDFHST0103Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のメイン端末運用・システム照会で判定する対象は CIC03 です。
用語定義: 変更後の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC03へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 変更後の確認 CIC03</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について変更結果を検証し、CIC03のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC03の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC03 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC03のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC03) Applid(CIC03) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC03の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC03) Cicstslevel(060200) Sysid(CIC03)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
② ステップ2 の STATUS が画面・出力に表示されること
③ ステップ3 の Applid が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0215"><h3>メイン端末運用 CEMTシステム照会 引継ぎ記録 CIC09</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>引継ぎ記録では メイン端末運用 の 統計記録 を主操作として CIC09 を判定します。次担当者が追跡できる証跡への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC09 に残します。引継ぎ記録を補助する システム照会 では STATUS を補助値として CIC09 へ保存します。主判定の引継ぎ記録ではメイン端末運用・システム照会の 統計記録 から DFHST0103I を読み CIC09 へ残します。証跡照合の引継ぎ記録ではメイン端末運用・システム照会の DFHST0103I と STATUS を CIC09 に保存します。記録対応の引継ぎ記録ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC09 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で メイン端末運用 の 統計記録 と システム照会 を使い 再現可能な記録を作成 します。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。DFHST0103I を読み対象 CIC09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 対象名CIC09を指定してCEMT PERFORM STATISTICS RECORD ALLを実行する。応答中のDFHST0103Iと時刻を保存する。CEMT INQUIRE SYSTEMで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. CEMT INQUIRE SYSTEMが成功したためCEMT PERFORM STATISTICS RECORD ALLのDFHST0103Iも正常だと推定する。主出力は保存しない。</li><li>C. CEMT PERFORM STATISTICS RECORD ALLを対象名なしで実行する。一覧の先頭行をCIC09の結果として記録する。</li><li>D. 前回保存したCEMT PERFORM STATISTICS RECORD ALLの結果を使う。今回のCEMT INQUIRE SYSTEMの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用操作の理由: Aは統計記録で DFHST0103I を読みAPPLIDと領域状態の主値として再現可能な記録を作成しCIC09に残します。
製品内の仕組み: 引継ぎ記録ではシステム照会を補助操作としCEMTシステム照会の次担当者が追跡できる証跡をSTATUSと対象CIC09で照合します。
選択肢別の説明: 統計記録とシステム照会の役割を分けるとA: DFHST0103Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではDFHST0103Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はCIC09と確定できない点で統計記録を代替しません、D: 採取時刻が異なる点でメイン端末運用に使いません。結論として引継ぎ記録のメイン端末運用・システム照会で判定する対象は CIC09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC09へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 引継ぎ記録 CIC09</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について再現可能な記録を作成し、CIC09のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC09の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC09 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC09のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC09) Applid(CIC09) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC09の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC09) Cicstslevel(060200) Sysid(CIC09)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
② ステップ2 の STATUS が画面・出力に表示されること
③ ステップ3 の Applid が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0216"><h3>メイン端末運用 CEMTシステム照会 復旧後の確認 CIC06</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>復旧後の確認では メイン端末運用 の 統計記録 を主操作として CIC06 を判定します。再発していないことを示す値への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC06 に残します。復旧後の確認を補助する システム照会 では STATUS を補助値として CIC06 へ保存します。主判定の復旧後の確認ではメイン端末運用・システム照会の 統計記録 から DFHST0103I を読み CIC06 へ残します。証跡照合の復旧後の確認ではメイン端末運用・システム照会の DFHST0103I と STATUS を CIC06 に保存します。記録対応の復旧後の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC06 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で メイン端末運用 の 統計記録 と システム照会 を照合し 再発していないことを示す値 を確かめます。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。DFHST0103I を読む前に対象 CIC06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. WebサポートのUSAGEとPATHを確認する。その値をメイン端末運用のCIC06にも適用する。</li><li>B. CEMT PERFORM STATISTICS RECORD ALLでDFHST0103Iを取得してからCEMT INQUIRE SYSTEM APPLIDでApplidを照合する。CIC06のAPPLIDと領域状態を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEMT INQUIRE SYSTEMが成功したためCEMT PERFORM STATISTICS RECORD ALLのDFHST0103Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象CIC06へ引き継げるものとする。CEMTシステム照会の再発していないことを示す値は確認済みとして扱う。さらにCEMT INQUIRE SYSTEM APPLIDのApplidをDFHST0103Iと同種の値として併記する。</li><li>D. CEMT PERFORM STATISTICS RECORD ALLを対象名なしで実行する。一覧の先頭行をCIC06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答内容: Bは統計記録で DFHST0103I を読みAPPLIDと領域状態の主値として復旧後の安定性を確認しCIC06に残します。
構成上の背景: 復旧後の確認ではシステム照会を補助操作としCEMTシステム照会の再発していないことを示す値をSTATUSと対象CIC06で照合します。
候補ごとの理由: 統計記録とシステム照会の役割を分けるとA: Webサポートの値ではDFHST0103Iを確認できない点でシステム照会の範囲を越えます、B: DFHST0103IとApplidを順に照合する点で現在値を示します、C: 補助操作の成功ではDFHST0103Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はCIC06と確定できない点で統計記録を代替しません。結論として復旧後の確認のメイン端末運用・システム照会で判定する対象は CIC06 です。
初出用語: 復旧後の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC06へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 復旧後の確認 CIC06</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について復旧後の安定性を確認し、CIC06のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC06の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC06 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC06のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC06) Applid(CIC06) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC06の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC06) Cicstslevel(060200) Sysid(CIC06)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHST0103I が画面・出力に表示されること
② ステップ2 の STATUS が画面・出力に表示されること
③ ステップ3 の Applid が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0217"><h3>メイン端末運用 CEMTシステム照会 復旧準備 CIC05</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>復旧準備では メイン端末運用 の 領域識別 を主操作として CIC05 を判定します。再開前に必要な整合性への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC05 に残します。復旧準備を補助する 統計記録 では DFHST0103I を補助値として CIC05 へ保存します。主判定の復旧準備ではメイン端末運用・システム照会の 領域識別 から Applid を読み CIC05 へ残します。証跡照合の復旧準備ではメイン端末運用・システム照会の Applid と DFHST0103I を CIC05 に保存します。記録対応の復旧準備ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC05 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で メイン端末運用 の 領域識別 と 統計記録 を用い 復旧条件を確認 します。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。Applid で対象 CIC05 の APPLIDと領域状態 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずCEMT INQUIRE SYSTEM APPLIDを実行する。Applidを保存する。差分はCEMT PERFORM STATISTICS RECORD ALLの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したCEMT INQUIRE SYSTEM APPLIDの結果を使う。今回のCEMT PERFORM STATISTICS RECORD ALLの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのCIC05の出力を再利用する。今回のCEMT INQUIRE SYSTEM APPLIDとCEMT PERFORM STATISTICS RECORD ALLは実行済みとして扱う。</li><li>D. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをAPPLIDと領域状態の主判定に採用する。CEMT INQUIRE SYSTEM APPLIDの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 選定理由: Aは領域識別で Applid を読みAPPLIDと領域状態の主値として復旧条件を確認しCIC05に残します。
処理の仕組み: 復旧準備では統計記録を補助操作としCEMTシステム照会の再開前に必要な整合性をDFHST0103Iと対象CIC05で照合します。
選択結果の内訳: 領域識別と統計記録の役割を分けるとA: 変更前のApplidを保存する点で領域識別に合います、B: 採取時刻が異なる点でメイン端末運用に使いません、C: 過去出力では今回の復旧準備を示せない点でCEMTシステム照会に使えません、D: DFHST0103IはApplidを代替しないうえに追加前提も不正な点でCIC05を採用できません。結論として復旧準備のメイン端末運用・システム照会で判定する対象は CIC05 です。
用語の説明: 復旧準備で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC05へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 復旧準備 CIC05</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について復旧条件を確認し、CIC05のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC05の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC05) Cicstslevel(060200) Sysid(CIC05)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC05の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC05 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC05のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC05) Applid(CIC05) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Applid が画面・出力に表示されること
② ステップ2 の DFHST0103I が画面・出力に表示されること
③ ステップ3 の STATUS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0218"><h3>メイン端末運用 CEMTシステム照会 構成監査 CIC08</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>構成監査では メイン端末運用 の 領域識別 を主操作として CIC08 を判定します。定義値と稼働値の一致への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC08 に残します。構成監査を補助する 統計記録 では DFHST0103I を補助値として CIC08 へ保存します。主判定の構成監査ではメイン端末運用・システム照会の 領域識別 から Applid を読み CIC08 へ残します。証跡照合の構成監査ではメイン端末運用・システム照会の Applid と DFHST0103I を CIC08 に保存します。記録対応の構成監査ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC08 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で メイン端末運用 の 領域識別 と 統計記録 の役割を分け 定義値と稼働値の一致 を調べます。CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能です。別領域のCEMT画面で変更を実行する危険があります。対象 CIC08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのCIC08の出力を再利用する。今回のCEMT INQUIRE SYSTEM APPLIDとCEMT PERFORM STATISTICS RECORD ALLは実行済みとして扱う。</li><li>B. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをAPPLIDと領域状態の主判定に採用する。CEMT INQUIRE SYSTEM APPLIDの応答は採取対象から外す。</li><li>C. CEMT INQUIRE SYSTEMのSTATUSをApplidと同義の成功表示として扱う。CEMT INQUIRE SYSTEM APPLIDは実行しない。</li><li>D. CEMT PERFORM STATISTICS RECORD ALLの結果だけでは確定しない。CEMT INQUIRE SYSTEM APPLIDのApplidを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 技術上の正答: Dは領域識別で Applid を読みAPPLIDと領域状態の主値として構成差分を監査しCIC08に残します。
実行時の背景: 構成監査では統計記録を補助操作としCEMTシステム照会の定義値と稼働値の一致をDFHST0103Iと対象CIC08で照合します。
四つの候補の理由: 領域識別と統計記録の役割を分けるとA: 過去出力では今回の構成監査を示せない点でメイン端末運用に使いません、B: DFHST0103IはApplidを代替しない点でCEMTシステム照会に使えません、C: STATUSとApplidは確認項目が異なる点でCIC08を採用できません、D: Applidを主証跡として区別する点で主証跡になります。結論として構成監査のメイン端末運用・システム照会で判定する対象は CIC08 です。
初出語定義: 構成監査で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC08へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 構成監査 CIC08</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について構成差分を監査し、CIC08のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC08の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC08) Cicstslevel(060200) Sysid(CIC08)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC08の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC08 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC08のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC08) Applid(CIC08) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Applid が画面・出力に表示されること
② ステップ2 の DFHST0103I が画面・出力に表示されること
③ ステップ3 の STATUS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0219"><h3>メイン端末運用 CEMTシステム照会 通常状態の確認 CIC01</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>通常状態の確認では メイン端末運用 の システム照会 を主操作として CIC01 を判定します。基準値と現在値の差への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC01 に残します。通常状態の確認を補助する 領域識別 では Applid を補助値として CIC01 へ保存します。主判定の通常状態の確認ではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC01 へ残します。証跡照合の通常状態の確認ではメイン端末運用・システム照会の STATUS と Applid を CIC01 に保存します。記録対応の通常状態の確認ではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC01 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で メイン端末運用 の システム照会 と 領域識別 を組み合わせる際は CEMTシステム照会 がCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能という仕組みを前提にします。別領域のCEMT画面で変更を実行する危険があります。STATUS と APPLIDと領域状態 を対象 CIC01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. CEMT INQUIRE SYSTEMを先に実行する。対象CIC01のSTATUSをAPPLIDと領域状態として記録する。続いてCEMT INQUIRE SYSTEM APPLIDで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. CEMT INQUIRE SYSTEM APPLIDのApplidをAPPLIDと領域状態の主判定に採用する。CEMT INQUIRE SYSTEMの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをSTATUSと同義の成功表示として扱う。CEMT INQUIRE SYSTEMは実行しない。</li><li>D. CEMT INQUIRE SYSTEMが応答を返した時点で正常とする。応答中のSTATUSの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: Aはシステム照会で STATUS を読みAPPLIDと領域状態の主値として通常状態を確定しCIC01に残します。
背景・仕組み: 通常状態の確認では領域識別を補助操作としCEMTシステム照会の基準値と現在値の差をApplidと対象CIC01で照合します。
選択肢の理由: システム照会と領域識別の役割を分けるとA: STATUSを主値として補助結果と照合する点で正答です、B: ApplidはSTATUSを代替しないうえに追加前提も不正な点でCIC01を採用できません、C: DFHST0103IとSTATUSは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではAPPLIDと領域状態を判定できない点で一次資料と一致しません。結論として通常状態の確認のメイン端末運用・システム照会で判定する対象は CIC01 です。
用語の初出定義: 通常状態の確認で使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC01へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 通常状態の確認 CIC01</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について通常状態を確定し、CIC01のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC01のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC01) Applid(CIC01) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC01の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC01) Cicstslevel(060200) Sysid(CIC01)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC01の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC01 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
② ステップ2 の Applid が画面・出力に表示されること
③ ステップ3 の DFHST0103I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0220"><h3>メイン端末運用 CEMTシステム照会 障害切り分け CIC04</h3><p class="kb-meta">分類: メイン端末運用 ・ 難易度: 初級</p><p>障害切り分けでは メイン端末運用 の システム照会 を主操作として CIC04 を判定します。最初に失敗した処理への注意として「別領域のCEMT画面で変更を実行する危険があります」を CIC04 に残します。障害切り分けを補助する 領域識別 では Applid を補助値として CIC04 へ保存します。主判定の障害切り分けではメイン端末運用・システム照会の システム照会 から STATUS を読み CIC04 へ残します。証跡照合の障害切り分けではメイン端末運用・システム照会の STATUS と Applid を CIC04 に保存します。記録対応の障害切り分けではメイン端末運用・システム照会の APPLIDと領域状態 の証跡へ CIC04 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで メイン端末運用 の システム照会 と 領域識別 を実施し CEMTシステム照会 の役割を確認します。別領域のCEMT画面で変更を実行する危険があります。対象 CIC04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. CEMT PERFORM STATISTICS RECORD ALLのDFHST0103IをSTATUSと同義の成功表示として扱う。CEMT INQUIRE SYSTEMは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. CEMT INQUIRE SYSTEMが応答を返した時点で正常とする。応答中のSTATUSの値は記録しない。</li><li>C. CEMT INQUIRE SYSTEMのコマンド文字列だけを記録する。STATUSを含む応答行は保存しない。</li><li>D. CEMT INQUIRE SYSTEMの出力でCIC04とSTATUSが同じ応答にあることを確認する。APPLIDと領域状態をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: Dはシステム照会で STATUS を読みAPPLIDと領域状態の主値として障害範囲を限定しCIC04に残します。
技術的背景: 障害切り分けでは領域識別を補助操作としCEMTシステム照会の最初に失敗した処理をApplidと対象CIC04で照合します。
四択の評価: システム照会と領域識別の役割を分けるとA: DFHST0103IとSTATUSは確認項目が異なるうえに追加前提も不正な点でCIC04を採用できません、B: 応答の有無だけではAPPLIDと領域状態を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではAPPLIDと領域状態を証明できない点で一次資料と一致しません、D: CIC04とSTATUSを同じ応答で結ぶ点でCIC04を判定できます。結論として障害切り分けのメイン端末運用・システム照会で判定する対象は CIC04 です。
初出語の意味: 障害切り分けで使う CEMTシステム照会 はCICS領域のAPPLID、稼働状態、システム属性を主端末トランザクションから表示する運用機能を表しAPPLIDと領域状態を判定する際にCIC04へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メイン端末運用 CEMTシステム照会 障害切り分け CIC04</strong></p><p>検証目的: メイン端末運用のCEMTシステム照会について障害範囲を限定し、CIC04のAPPLIDと領域状態を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象CIC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEMを指定し、CIC04のシステム照会を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM
→ Enter を押す
［画面・出力］
STATUS: RESULTS - OVERTYPE TO MODIFY
Sysid(CIC04) Applid(CIC04) Aging(1000) Maxtasks(120)
画面・出力にあるSTATUSを読み、APPLIDと領域状態と対象CIC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT INQUIRE SYSTEM APPLIDを指定し、CIC04の領域識別を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT INQUIRE SYSTEM APPLID
→ Enter を押す
［画面・出力］
Applid(CIC04) Cicstslevel(060200) Sysid(CIC04)
画面・出力にあるApplidを読み、APPLIDと領域状態と対象CIC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのメイン端末運用を確認する入力画面です。COMMAND入力口へCEMT PERFORM STATISTICS RECORD ALLを指定し、CIC04の統計記録を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEMT PERFORM STATISTICS RECORD ALL
→ Enter を押す
［画面・出力］
DFHST0103I CIC04 STATISTICS RECORDING REQUEST COMPLETED
画面・出力にあるDFHST0103Iを読み、APPLIDと領域状態と対象CIC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の STATUS が画面・出力に表示されること
② ステップ2 の Applid が画面・出力に表示されること
③ ステップ3 の DFHST0103I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


## リソース定義


<section class="kb-item" id="c04-i0221"><h3>CEDA</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義で扱うCEDAは、CICS リソース定義をオンラインで追加、変更、インストールするためのトランザクションです。プログラム、ファイル、トランザクションなどをグループ単位で扱います。変更時は定義の保存とリージョンへの反映を分けて確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認のリソース定義でトランザクション管理の運用確認を行います。CEDA の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. CICS TS と無関係な一覧で上書確認のリソース定義を確認した扱いにする。</li><li>B. DFH4200A の有無を確認せず上書確認のリソース定義を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. CEDA の属性行を読まず上書確認のリソース定義の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では CEDA は「CICS TS で CEDA の扱いを記録する上書確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では CEDA の表示結果と DFH4200A を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では CEDA の使い方を出典欄から追跡し、資料名は上書確認資料です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEDA</strong></p><p>検証目的: 上書確認のリソース定義について、CICS Transaction Server for z/OS 6.x の リソース定義で扱う CEDA は、CICS リソース定義をオンラインで追加、変更、インストールするに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、上書確認のリソース定義の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCEDAを指定し、OSKB010007の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CEDA
CASE OSKB010007
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CEDA
CASE OSKB010007
SOURCE CICS TS
CEDAとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010007を同じ出力で読み、上書確認のリソース定義の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010007
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010007
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A CEDA RESPONSE DISPLAYED
DFH4200AとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の CEDA と OSKB010007 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0222"><h3>CEDA DEFINE TRANSACTION 実行条件確認 完了コード</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEDA DEFINE TRANSACTION 実行条件確認 完了コード」は、TRANSACTIONリソースをCSDに定義し、プログラムやプロファイルと結び付けるRDO操作を実行条件確認の観点で確認する技術項目です。URIMAP 行とJVMSRV07を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Web入口定義の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEDA DEFINE TRANSACTION 実行条件確認 完了コード</strong></p><p>検証目的: リソース定義におけるCEDA DEFINE TRANSACTIONの実行条件確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=JVMSRV07</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CETR
→ Enter を押す
［画面・出力］
CETR CICS TRACE CONTROL
MAIN SYSTEM TRACE FLAG ==&gt; OFF
AUXILIARY TRACE STATUS ==&gt; STARTED
画面・出力には CETR が含まれ、CETRを確認し、Web入口定義の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; VERBX DFHPD760 &#x27;TR=1&#x27;
→ Enter を押す
［画面・出力］
DFHPD760 CICS TRACE FORMATTER
TRACE ENTRIES SELECTED FOR APPLID CIC27
RETURN CODE = 0000
画面・出力には DFHPD760 が含まれ、DFHPD760を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; SUBMIT CICS.DFHTU760.CNTL(TRACE)
→ Enter を押す
［画面・出力］
DFHTU760 AUXILIARY TRACE PRINT UTILITY
ABBREVIATED TRACE PRINTED
RETURN CODE = 0000
画面・出力には DFHTU760 が含まれ、DFHTU760を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CETR が画面・出力に表示されること
② ステップ2 の DFHPD760 が画面・出力に表示されること
③ ステップ3 の DFHTU760 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0223"><h3>CEDA INSTALL GROUP 定義確認 資料見出し</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEDA INSTALL GROUP 定義確認 資料見出し」は、CSDグループ内の定義を稼働リージョンへインストールするRDO操作を定義確認の観点で確認する技術項目です。TCPIPSERVICE 行とDFH041を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、未インストール定義の採用を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEDA INSTALL GROUP 定義確認 資料見出し</strong></p><p>検証目的: リソース定義におけるCEDA INSTALL GROUPの定義確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=DFH041</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TASK
→ Enter を押す
［画面・出力］
Tas(0000140) Tra(PAY041) Sus Tas Pri(001) Sta(U) Use(USR041)
Uow(C9D5F2EE2DEE0040) Hty(SOCKET) Hva(RECEIVE) Bac Wai
画面・出力には PAY041 が含まれ、PAY041を確認し、未インストール定義の採用を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TRANSACTION(PAY041)
→ Enter を押す
［画面・出力］
Tra(PAY041) Pri(001) Pro(DFH041) Ena Sta Pro Ena Resc(DFHPROF)
画面・出力には PAY041 が含まれ、PAY041を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE PROGRAM(DFH041)
→ Enter を押す
［画面・出力］
Pro(DFH041) Leng(0001234) Resc(0001) Ced Ena Pri Dplsubsys(CICS)
画面・出力には DFH041 が含まれ、DFH041を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の PAY041 が画面・出力に表示されること
② ステップ2 の PAY041 が画面・出力に表示されること
③ ステップ3 の DFH041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0224"><h3>CEMT</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義で扱うCEMTは、CICS の稼働中リソース状態を表示、変更するためのマスター端末トランザクションです。タスク、ファイル、プログラム、端末などの状態確認に使います。緊急対応では変更操作の影響範囲と監査記録を確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認のリソース定義に関する CEMT の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず出力確認のリソース定義の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認のリソース定義の証跡として保存して根拠にする。</li><li>C. CEMT の変更点を出力本文から切り離して出力確認のリソース定義の承認欄のみ残す。</li><li>D. CICS TS の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では CEMT は「CEMT の状態と出力メッセージを結び付ける出力確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では CEMT の出力行と DFH4200A を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では CEMT を CICS TS の確認記録に残し、対象名は出力確認対象です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT</strong></p><p>検証目的: 出力確認のリソース定義について、CICS Transaction Server for z/OS 6.x の リソース定義で扱う CEMT は、CICS の稼働中リソース状態を表示、変更するためのマスター端末に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、出力確認のリソース定義の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCEMTを指定し、OSKB010008の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CEMT
CASE OSKB010008
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CEMT
CASE OSKB010008
SOURCE CICS TS
CEMTとOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010008を同じ出力で読み、出力確認のリソース定義の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010008
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010008
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A CEMT RESPONSE DISPLAYED
DFH4200AとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の CEMT と OSKB010008 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0225"><h3>CEMT INQUIRE PROGRAM ダンプ確認 サンプル採取</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 上級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEMT INQUIRE PROGRAM ダンプ確認 サンプル採取」は、PROGRAMリソースのロード状態、使用属性、インストール属性を確認するメイン端末コマンドをダンプ確認の観点で確認する技術項目です。MAX/CUR 欄と00192を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT INQUIRE PROGRAM ダンプ確認 サンプル採取</strong></p><p>検証目的: リソース定義におけるCEMT INQUIRE PROGRAMのダンプ確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=00192</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TCPIPSERVICE(TCP03)
→ Enter を押す
［画面・出力］
Tcp(TCP03) Ope Por(08080) Pro(Http) Backlog(00050) Urm(DFHWBAAX)
画面・出力には TCP03 が含まれ、TCP03を確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET TCPIPSERVICE(TCP03) OPEN
→ Enter を押す
［画面・出力］
Tcp(TCP03) Ope Por(08080) Pro(Http) Backlog(00050)
画面・出力には TCP03 が含まれ、TCP03を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE TCPIP
→ Enter を押す
［画面・出力］
Tcpip Open ActSockets(000012) ActSslTcbs(000002)
画面・出力には Tcpip が含まれ、Tcpipを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の TCP03 が画面・出力に表示されること
② ステップ2 の TCP03 が画面・出力に表示されること
③ ステップ3 の Tcpip が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0226"><h3>CEMT INQUIRE TRANSACTION 定義確認 詳細表示</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CEMT INQUIRE TRANSACTION 定義確認 詳細表示」は、トランザクション定義、利用可否、プロファイル、実行属性を確認するメイン端末コマンドを定義確認の観点で確認する技術項目です。TCB 欄とFILE002を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、トレース対象の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CEMT INQUIRE TRANSACTION 定義確認 詳細表示</strong></p><p>検証目的: リソース定義におけるCEMT INQUIRE TRANSACTIONの定義確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=FILE002</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE002)
→ Enter を押す
［画面・出力］
Fil(FILE002) Vsa Ope Ena Rea Upd Add Bro Del Sha
画面・出力には FILE002 が含まれ、FILE002を確認し、トレース対象の取り違えを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT SET FILE(FILE002) CLOSED ENABLED
→ Enter を押す
［画面・出力］
Fil(FILE002) Clo Ena Rea Upd Add Bro Del
画面・出力には FILE002 が含まれ、FILE002を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE FILE(FILE002)
→ Enter を押す
［画面・出力］
Fil(FILE002) Clo Ena Rea Upd Add Bro Del
画面・出力には FILE002 が含まれ、FILE002を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の FILE002 が画面・出力に表示されること
② ステップ2 の FILE002 が画面・出力に表示されること
③ ステップ3 の FILE002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0227"><h3>CMCI resource table 戻りコード確認 ページング状態</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「CMCI resource table 戻りコード確認 ページング状態」は、CICS定義や稼働リソースをAPI/WUI/Management Client Interfaceで扱う表を戻りコード確認の観点で確認する技術項目です。FILE 欄とDB2C08を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、TCP/IPサービス状態の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CMCI resource table 戻りコード確認 ページング状態</strong></p><p>検証目的: リソース定義におけるCMCI resource tableの戻りコード確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=DB2C08</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; view server.xml
→ Enter を押す
［画面・出力］
&lt;featureManager&gt;&lt;feature&gt;jdbc-4.2&lt;/feature&gt;&lt;/featureManager&gt;
&lt;dataSource jndiName=&quot;jdbc/defaultCICSDataSource&quot;&gt;
画面・出力には featureManager が含まれ、featureManagerを確認し、TCP/IPサービス状態の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE JVMSERVER(JVMSRV08)
→ Enter を押す
［画面・出力］
Jvm(JVMSRV08) Ena Sta Ope Profile(DFHWLP)
画面・出力には JVMSRV08 が含まれ、JVMSRV08を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEMT INQUIRE DB2CONN
→ Enter を押す
［画面・出力］
Db2conn Connected Db2id(DSN0) TcbLimit(0008) Comthread(0004)
画面・出力には Db2conn が含まれ、Db2connを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の featureManager が画面・出力に表示されること
② ステップ2 の JVMSRV08 が画面・出力に表示されること
③ ステップ3 の Db2conn が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0228"><h3>CSD</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義で扱うCSDは、CICS System Definition データセットとしてリソース定義を保持するデータセットです。CEDA などで管理する定義の保管先になり、グループやリストの単位でリージョンへ反映されます。移行時は CSD の内容と起動時のリスト指定を確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認のリソース定義に関係する CSD の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. CSD の名称と担当者名のみを残して条件確認のリソース定義の表示本文を確認対象に含めない。</li><li>C. トランザクション管理以外の画面で条件確認のリソース定義を確認し同じ証跡として扱ったことにする。</li><li>D. DFH4200A の有無を見ず条件確認のリソース定義の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では CSD は「CSD の用途をトランザクション管理の表示で確認する条件確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では CICS TS の CSD と DFH4200A を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では CSD を CICS Transaction Server for z/OS 6.xで扱う確認対象とし、用語名は条件確認用語です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CSD</strong></p><p>検証目的: 条件確認のリソース定義について、CICS Transaction Server for z/OS 6.x の リソース定義で扱う CSD は、CICS System Definition データセットとしてリに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、条件確認のリソース定義の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCSDを指定し、OSKB010009の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CSD
CASE OSKB010009
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CSD
CASE OSKB010009
SOURCE CICS TS
CSDとOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010009を同じ出力で読み、条件確認のリソース定義の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010009
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010009
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A CSD RESPONSE DISPLAYED
DFH4200AとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の CSD と OSKB010009 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0229"><h3>DB2CONN resource トレース確認 再読込</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「DB2CONN resource トレース確認 再読込」は、CICSとDb2の接続属性を管理し、JDBC type 2接続にも使われるリソースをトレース確認の観点で確認する技術項目です。PROGRAM 欄とTCP15を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、ダンプ取得条件の不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DB2CONN resource トレース確認 再読込</strong></p><p>検証目的: リソース定義におけるDB2CONN resourceのトレース確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=TCP15</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE TCPIPSERVICE(TCP15) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF TCPIPSERVICE(TCP15) GROUP(TEST)
PROTOCOL ==&gt; HTTP
PORTNUMBER ==&gt; 08080
URM ==&gt; DFHWBAAX
画面・出力には CEDA が含まれ、CEDAを確認し、ダンプ取得条件の不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE URIMAP(URI15) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF URIMAP(URI15) GROUP(TEST)
PATH ==&gt; /pay/015
TRANSACTION ==&gt; CWBA
画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(TEST)
→ Enter を押す
［画面・出力］
INSTALL SUCCESSFUL FOR GROUP TEST
TCPIPSERVICE TCP15 INSTALLED
URIMAP URI15 INSTALLED
画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
② ステップ2 の CEDA が画面・出力に表示されること
③ ステップ3 の INSTALL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0230"><h3>DFHDU dump utility 定義確認 保存場所</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「DFHDU dump utility 定義確認 保存場所」は、トランザクションダンプを整形し、該当タスクのトレースも確認するCICSダンプユーティリティを定義確認の観点で確認する技術項目です。DFH メッセージとPAY080を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、Db2接続前提の欠落を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFHDU dump utility 定義確認 保存場所</strong></p><p>検証目的: リソース定義におけるDFHDU dump utilityの定義確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=PAY080</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; Open Tasks view for CIC40
→ Enter を押す
［画面・出力］
Tasks view APPLID CIC40
Task 0051988 Transaction CWXN Status Suspended Wait RECEIVE
画面・出力には Tasks が含まれ、Tasksを確認し、Db2接続前提の欠落を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; GET CICSDefinitionTCPIPService TCP20
→ Enter を押す
［画面・出力］
&lt;response&gt;&lt;TCPIPSERVICE name=&quot;TCP20&quot; status=&quot;OPEN&quot; port=&quot;8080&quot; protocol=&quot;HTTP&quot; /&gt;&lt;/response&gt;
画面・出力には response が含まれ、responseを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; GET CICSDefinitionTransaction PAY080
→ Enter を押す
［画面・出力］
&lt;response&gt;&lt;TRANSACTION name=&quot;PAY080&quot; program=&quot;DFH080&quot; status=&quot;ENABLED&quot; /&gt;&lt;/response&gt;
画面・出力には response が含まれ、responseを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の Tasks が画面・出力に表示されること
② ステップ2 の response が画面・出力に表示されること
③ ステップ3 の response が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0231"><h3>DFHTR0130 トレース確認 待機状態</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の リソース定義 で扱う「DFHTR0130 トレース確認 待機状態」は、CICS内部トレース開始を示すDFHメッセージをトレース確認の観点で確認する技術項目です。PORTNUMBER 欄とCIC14を同じ運用記録へ残し、CEMT/CEDA応答、CSD/CMCI情報、トレースまたはダンプ出力の対応を見比べることで、タスク待機理由の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFHTR0130 トレース確認 待機状態</strong></p><p>検証目的: リソース定義におけるDFHTR0130のトレース確認を机上確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.x の操作権限、対象リージョン、CSD/CMCIまたは該当JCLを確認済み。対象=CIC14</p><p>セッション環境: CICS terminal / TSO / CICS Explorer / CMCI / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、対象状態を確認し、CEMT、CEDA、CMCI、またはJCLを投入する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE TRANSACTION(PAY054) GROUP(TEST) PROGRAM(DFH054)
→ Enter を押す
［画面・出力］
CEDA DEF TRANSACTION(PAY054) GROUP(TEST)
PROGRAM ==&gt; DFH054
PROFILE ==&gt; DFHCICST
画面・出力には CEDA が含まれ、CEDAを確認し、タスク待機理由の誤読を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、リソース定義、接続、トレース、またはダンプの詳細出力を読む。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA DEFINE PROGRAM(DFH054) GROUP(TEST)
→ Enter を押す
［画面・出力］
CEDA DEF PROGRAM(DFH054) GROUP(TEST)
LANGUAGE ==&gt; COBOL
STATUS ==&gt; ENABLED
画面・出力には CEDA が含まれ、CEDAを読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xの確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
CICS操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(TEST)
→ Enter を押す
［画面・出力］
INSTALL SUCCESSFUL FOR GROUP TEST
TRANSACTION PAY054 INSTALLED
PROGRAM DFH054 INSTALLED
画面・出力には INSTALL が含まれ、INSTALLを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の CEDA が画面・出力に表示されること
② ステップ2 の CEDA が画面・出力に表示されること
③ ステップ3 の INSTALL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0232"><h3>リソース定義 CEDA資源定義 ログとの照合 GRP07</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>ログとの照合では リソース定義 の グループ表示 を主操作として GRP07 を判定します。時刻と対象識別子への注意として「別グループの同名資源をインストールする危険があります」を GRP07 に残します。ログとの照合を補助する 定義検査 では DFHED1101 を補助値として GRP07 へ保存します。主判定のログとの照合ではリソース定義・資源定義の グループ表示 から GROUP を読み GRP07 へ残します。証跡照合のログとの照合ではリソース定義・資源定義の GROUP と DFHED1101 を GRP07 に保存します。記録対応のログとの照合ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP07 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で リソース定義 の グループ表示 と 定義検査 を用い 操作とログを対応 します。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。GROUP で対象 GRP07 の グループ名とインストール結果 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. GROUPを含むグループ表示の応答行を保存する。その応答を得るためCEDA DISPLAY GROUP(GRP07)を使用する。対象GRP07のグループ名とインストール結果として記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. CEDA DISPLAY GROUP(GRP07)が応答を返した時点で正常とする。応答中のGROUPの値は記録しない。DFHED1102をGROUPと同じ判定値とみなし対象GRP07の主証跡にする。</li><li>C. CEDA DISPLAY GROUP(GRP07)のコマンド文字列だけを記録する。GROUPを含む応答行は保存しない。</li><li>D. CEDA資源定義の停止または再定義を実施する。その後にCEDA DISPLAY GROUP(GRP07)でGROUPを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 適切な判定: Aはグループ表示で GROUP を読みグループ名とインストール結果の主値として操作とログを対応しGRP07に残します。
機能の仕組み: ログとの照合では定義検査を補助操作としCEDA資源定義の時刻と対象識別子をDFHED1101と対象GRP07で照合します。
各候補の評価: グループ表示と定義検査の役割を分けるとA: GROUPの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではグループ名とインストール結果を判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではグループ名とインストール結果を証明できない点でグループ名とインストール結果を確認できません、D: 変更前のグループ名とインストール結果を失う点で定義検査の範囲を越えます。結論としてログとの照合のリソース定義・資源定義で判定する対象は GRP07 です。
用語の定義: ログとの照合で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP07へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 ログとの照合 GRP07</strong></p><p>検証目的: リソース定義のCEDA資源定義について操作とログを対応し、GRP07のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP07)を指定し、GRP07のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP07)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP07)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP07)を指定し、GRP07の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP07)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP07 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP07)を指定し、GRP07のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP07)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP07 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
② ステップ2 の DFHED1101 が画面・出力に表示されること
③ ステップ3 の DFHED1102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0233"><h3>リソース定義 CEDA資源定義 代替経路の確認 GRP10</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>代替経路の確認では リソース定義 の グループ表示 を主操作として GRP10 を判定します。主経路との役割差への注意として「別グループの同名資源をインストールする危険があります」を GRP10 に残します。代替経路の確認を補助する 定義検査 では DFHED1101 を補助値として GRP10 へ保存します。主判定の代替経路の確認ではリソース定義・資源定義の グループ表示 から GROUP を読み GRP10 へ残します。証跡照合の代替経路の確認ではリソース定義・資源定義の GROUP と DFHED1101 を GRP10 に保存します。記録対応の代替経路の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP10 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で リソース定義 の グループ表示 と 定義検査 の役割を分け 主経路との役割差 を調べます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。対象 GRP10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. CEDA DISPLAY GROUP(GRP10)のコマンド文字列だけを記録する。GROUPを含む応答行は保存しない。</li><li>B. CEDA資源定義の停止または再定義を実施する。その後にCEDA DISPLAY GROUP(GRP10)でGROUPを採取する。</li><li>C. Liberty JVMのJVMSTATUSとPROFILEを確認する。その値をリソース定義のGRP10にも適用する。</li><li>D. CEDA DISPLAY GROUP(GRP10)とCEDA CHECK GROUP(GRP10)の対象名をそろえる。前者のGROUPをグループ名とインストール結果の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい判定結果: Dはグループ表示で GROUP を読みグループ名とインストール結果の主値として代替手段の成立を確認しGRP10に残します。
運用上の背景: 代替経路の確認では定義検査を補助操作としCEDA資源定義の主経路との役割差をDFHED1101と対象GRP10で照合します。
候補別の検討: グループ表示と定義検査の役割を分けるとA: 入力記録だけではグループ名とインストール結果を証明できない点で一次資料と一致しません、B: 変更前のグループ名とインストール結果を失う点でグループ名とインストール結果を確認できません、C: Liberty JVMの値ではGROUPを確認できない点で定義検査の範囲を越えます、D: 同じ対象名のGROUPを採用する点で現在値を示します。結論として代替経路の確認のリソース定義・資源定義で判定する対象は GRP10 です。
重要用語の定義: 代替経路の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP10へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 代替経路の確認 GRP10</strong></p><p>検証目的: リソース定義のCEDA資源定義について代替手段の成立を確認し、GRP10のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP10)を指定し、GRP10のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP10)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP10)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP10)を指定し、GRP10の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP10)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP10 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP10)を指定し、GRP10のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP10)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP10 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
② ステップ2 の DFHED1101 が画面・出力に表示されること
③ ステップ3 の DFHED1102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0234"><h3>リソース定義 CEDA資源定義 変更前の確認 GRP02</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>変更前の確認では リソース定義 の 定義検査 を主操作として GRP02 を判定します。変更対象と非対象の境界への注意として「別グループの同名資源をインストールする危険があります」を GRP02 に残します。変更前の確認を補助する グループ導入 では DFHED1102 を補助値として GRP02 へ保存します。主判定の変更前の確認ではリソース定義・資源定義の 定義検査 から DFHED1101 を読み GRP02 へ残します。証跡照合の変更前の確認ではリソース定義・資源定義の DFHED1101 と DFHED1102 を GRP02 に保存します。記録対応の変更前の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP02 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で リソース定義 の 定義検査 と グループ導入 を照合し 変更対象と非対象の境界 を確かめます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。DFHED1101 を読む前に対象 GRP02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. CEDA CHECK GROUP(GRP02)を対象名なしで実行する。一覧の先頭行をGRP02の結果として記録する。</li><li>B. 前回保存したCEDA CHECK GROUP(GRP02)の結果を使う。今回のCEDA INSTALL GROUP(GRP02)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのGRP02の出力を再利用する。今回のCEDA CHECK GROUP(GRP02)とCEDA INSTALL GROUP(GRP02)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象GRP02についてCEDA CHECK GROUP(GRP02)の応答からDFHED1101を確認する。CEDA INSTALL GROUP(GRP02)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: Dは定義検査で DFHED1101 を読みグループ名とインストール結果の主値として変更前の証跡を保存しGRP02に残します。
動作の背景: 変更前の確認ではグループ導入を補助操作としCEDA資源定義の変更対象と非対象の境界をDFHED1102と対象GRP02で照合します。
各選択肢の検討: 定義検査とグループ導入の役割を分けるとA: 先頭行はGRP02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で定義検査を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でリソース定義に使いません、D: DFHED1101と補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のリソース定義・資源定義で判定する対象は GRP02 です。
初出用語の定義: 変更前の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP02へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 変更前の確認 GRP02</strong></p><p>検証目的: リソース定義のCEDA資源定義について変更前の証跡を保存し、GRP02のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP02)を指定し、GRP02の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP02)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP02 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP02)を指定し、GRP02のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP02)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP02 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP02)を指定し、GRP02のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP02)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP02)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHED1101 が画面・出力に表示されること
② ステップ2 の DFHED1102 が画面・出力に表示されること
③ ステップ3 の GROUP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0235"><h3>リソース定義 CEDA資源定義 変更後の確認 GRP03</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>変更後の確認では リソース定義 の グループ導入 を主操作として GRP03 を判定します。反映値と残存値への注意として「別グループの同名資源をインストールする危険があります」を GRP03 に残します。変更後の確認を補助する グループ表示 では GROUP を補助値として GRP03 へ保存します。主判定の変更後の確認ではリソース定義・資源定義の グループ導入 から DFHED1102 を読み GRP03 へ残します。証跡照合の変更後の確認ではリソース定義・資源定義の DFHED1102 と GROUP を GRP03 に保存します。記録対応の変更後の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP03 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で リソース定義 の グループ導入 と グループ表示 を組み合わせる際は CEDA資源定義 がCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能という仕組みを前提にします。別グループの同名資源をインストールする危険があります。DFHED1102 と グループ名とインストール結果 を対象 GRP03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. CEDA DISPLAY GROUP(GRP03)で周辺状態を押さえる。その後にCEDA INSTALL GROUP(GRP03)でDFHED1102を確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. CEDA資源定義の停止または再定義を実施する。その後にCEDA INSTALL GROUP(GRP03)でDFHED1102を採取する。</li><li>C. メイン端末運用のAPPLIDと領域状態を確認する。その値をリソース定義のGRP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。CEDA資源定義の反映値と残存値は確認済みとして扱う。さらにCEDA CHECK GROUP(GRP03)のDFHED1101をDFHED1102と同種の値として併記する。</li><li>D. CEDA DISPLAY GROUP(GRP03)が成功したためCEDA INSTALL GROUP(GRP03)のDFHED1102も正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Aはグループ導入で DFHED1102 を読みグループ名とインストール結果の主値として変更結果を検証しGRP03に残します。
内部の仕組み: 変更後の確認ではグループ表示を補助操作としCEDA資源定義の反映値と残存値をGROUPと対象GRP03で照合します。
誤答を含む比較: グループ導入とグループ表示の役割を分けるとA: 周辺状態の後にDFHED1102を確認する点でGRP03を判定できます、B: 変更前のグループ名とインストール結果を失う点でグループ表示の範囲を越えます、C: メイン端末運用の値ではDFHED1102を確認できないうえに追加前提も不正な点でGRP03の値を示しません、D: 補助操作の成功ではDFHED1102を確定できない点で変更後の確認に合いません。結論として変更後の確認のリソース定義・資源定義で判定する対象は GRP03 です。
用語定義: 変更後の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP03へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 変更後の確認 GRP03</strong></p><p>検証目的: リソース定義のCEDA資源定義について変更結果を検証し、GRP03のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP03)を指定し、GRP03のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP03)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP03 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP03)を指定し、GRP03のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP03)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP03)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP03)を指定し、GRP03の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP03)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP03 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHED1102 が画面・出力に表示されること
② ステップ2 の GROUP が画面・出力に表示されること
③ ステップ3 の DFHED1101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0236"><h3>リソース定義 CEDA資源定義 引継ぎ記録 GRP09</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>引継ぎ記録では リソース定義 の グループ導入 を主操作として GRP09 を判定します。次担当者が追跡できる証跡への注意として「別グループの同名資源をインストールする危険があります」を GRP09 に残します。引継ぎ記録を補助する グループ表示 では GROUP を補助値として GRP09 へ保存します。主判定の引継ぎ記録ではリソース定義・資源定義の グループ導入 から DFHED1102 を読み GRP09 へ残します。証跡照合の引継ぎ記録ではリソース定義・資源定義の DFHED1102 と GROUP を GRP09 に保存します。記録対応の引継ぎ記録ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP09 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で リソース定義 の グループ導入 と グループ表示 を組み合わせる際は CEDA資源定義 がCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能という仕組みを前提にします。別グループの同名資源をインストールする危険があります。DFHED1102 と グループ名とインストール結果 を対象 GRP09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. CEDA DISPLAY GROUP(GRP09)が成功したためCEDA INSTALL GROUP(GRP09)のDFHED1102も正常だと推定する。主出力は保存しない。</li><li>B. CEDA INSTALL GROUP(GRP09)を対象名なしで実行する。一覧の先頭行をGRP09の結果として記録する。</li><li>C. 対象名GRP09を指定してCEDA INSTALL GROUP(GRP09)を実行する。応答中のDFHED1102と時刻を保存する。CEDA DISPLAY GROUP(GRP09)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したCEDA INSTALL GROUP(GRP09)の結果を使う。今回のCEDA DISPLAY GROUP(GRP09)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用操作の理由: Cはグループ導入で DFHED1102 を読みグループ名とインストール結果の主値として再現可能な記録を作成しGRP09に残します。
製品内の仕組み: 引継ぎ記録ではグループ表示を補助操作としCEDA資源定義の次担当者が追跡できる証跡をGROUPと対象GRP09で照合します。
選択肢別の説明: グループ導入とグループ表示の役割を分けるとA: 補助操作の成功ではDFHED1102を確定できない点でGRP09の値を示しません、B: 先頭行はGRP09と確定できない点で引継ぎ記録に合いません、C: DFHED1102と時刻を保存する点でグループ導入に合います、D: 採取時刻が異なる点でリソース定義に使いません。結論として引継ぎ記録のリソース定義・資源定義で判定する対象は GRP09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP09へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 引継ぎ記録 GRP09</strong></p><p>検証目的: リソース定義のCEDA資源定義について再現可能な記録を作成し、GRP09のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP09)を指定し、GRP09のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP09)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP09 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP09)を指定し、GRP09のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP09)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP09)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP09)を指定し、GRP09の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP09)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP09 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHED1102 が画面・出力に表示されること
② ステップ2 の GROUP が画面・出力に表示されること
③ ステップ3 の DFHED1101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0237"><h3>リソース定義 CEDA資源定義 復旧後の確認 GRP06</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>復旧後の確認では リソース定義 の グループ導入 を主操作として GRP06 を判定します。再発していないことを示す値への注意として「別グループの同名資源をインストールする危険があります」を GRP06 に残します。復旧後の確認を補助する グループ表示 では GROUP を補助値として GRP06 へ保存します。主判定の復旧後の確認ではリソース定義・資源定義の グループ導入 から DFHED1102 を読み GRP06 へ残します。証跡照合の復旧後の確認ではリソース定義・資源定義の DFHED1102 と GROUP を GRP06 に保存します。記録対応の復旧後の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP06 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で リソース定義 の グループ導入 と グループ表示 を実施し CEDA資源定義 の役割を確認します。別グループの同名資源をインストールする危険があります。対象 GRP06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. プログラム管理のPROGRAM名とNEWCOPY結果を確認する。その値をリソース定義のGRP06にも適用する。</li><li>B. CEDA DISPLAY GROUP(GRP06)が成功したためCEDA INSTALL GROUP(GRP06)のDFHED1102も正常だと推定する。主出力は保存しない。別資源で得た状態を対象GRP06へ引き継げるものとする。</li><li>C. CEDA INSTALL GROUP(GRP06)を対象名なしで実行する。一覧の先頭行をGRP06の結果として記録する。</li><li>D. CEDA INSTALL GROUP(GRP06)でDFHED1102を取得してからCEDA CHECK GROUP(GRP06)でDFHED1101を照合する。GRP06のグループ名とインストール結果を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答内容: Dはグループ導入で DFHED1102 を読みグループ名とインストール結果の主値として復旧後の安定性を確認しGRP06に残します。
構成上の背景: 復旧後の確認ではグループ表示を補助操作としCEDA資源定義の再発していないことを示す値をGROUPと対象GRP06で照合します。
候補ごとの理由: グループ導入とグループ表示の役割を分けるとA: プログラム管理の値ではDFHED1102を確認できない点でグループ表示の範囲を越えます、B: 補助操作の成功ではDFHED1102を確定できないうえに追加前提も不正な点でGRP06の値を示しません、C: 先頭行はGRP06と確定できない点で復旧後の確認に合いません、D: DFHED1102とDFHED1101を順に照合する点でグループ導入に合います。結論として復旧後の確認のリソース定義・資源定義で判定する対象は GRP06 です。
初出用語: 復旧後の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP06へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 復旧後の確認 GRP06</strong></p><p>検証目的: リソース定義のCEDA資源定義について復旧後の安定性を確認し、GRP06のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP06)を指定し、GRP06のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP06)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP06 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP06)を指定し、GRP06のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP06)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP06)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP06)を指定し、GRP06の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP06)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP06 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHED1102 が画面・出力に表示されること
② ステップ2 の GROUP が画面・出力に表示されること
③ ステップ3 の DFHED1101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0238"><h3>リソース定義 CEDA資源定義 復旧準備 GRP05</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>復旧準備では リソース定義 の 定義検査 を主操作として GRP05 を判定します。再開前に必要な整合性への注意として「別グループの同名資源をインストールする危険があります」を GRP05 に残します。復旧準備を補助する グループ導入 では DFHED1102 を補助値として GRP05 へ保存します。主判定の復旧準備ではリソース定義・資源定義の 定義検査 から DFHED1101 を読み GRP05 へ残します。証跡照合の復旧準備ではリソース定義・資源定義の DFHED1101 と DFHED1102 を GRP05 に保存します。記録対応の復旧準備ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP05 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で リソース定義 の 定義検査 と グループ導入 を使い 復旧条件を確認 します。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。DFHED1101 を読み対象 GRP05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したCEDA CHECK GROUP(GRP05)の結果を使う。今回のCEDA INSTALL GROUP(GRP05)の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのGRP05の出力を再利用する。今回のCEDA CHECK GROUP(GRP05)とCEDA INSTALL GROUP(GRP05)は実行済みとして扱う。</li><li>C. 変更を加えずCEDA CHECK GROUP(GRP05)を実行する。DFHED1101を保存する。差分はCEDA INSTALL GROUP(GRP05)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. CEDA INSTALL GROUP(GRP05)のDFHED1102をグループ名とインストール結果の主判定に採用する。CEDA CHECK GROUP(GRP05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 選定理由: Cは定義検査で DFHED1101 を読みグループ名とインストール結果の主値として復旧条件を確認しGRP05に残します。
処理の仕組み: 復旧準備ではグループ導入を補助操作としCEDA資源定義の再開前に必要な整合性をDFHED1102と対象GRP05で照合します。
選択結果の内訳: 定義検査とグループ導入の役割を分けるとA: 採取時刻が異なる点で定義検査を代替しません、B: 過去出力では今回の復旧準備を示せない点でリソース定義に使いません、C: 変更前のDFHED1101を保存する点で正答です、D: DFHED1102はDFHED1101を代替しないうえに追加前提も不正な点でGRP05を採用できません。結論として復旧準備のリソース定義・資源定義で判定する対象は GRP05 です。
用語の説明: 復旧準備で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP05へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 復旧準備 GRP05</strong></p><p>検証目的: リソース定義のCEDA資源定義について復旧条件を確認し、GRP05のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP05)を指定し、GRP05の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP05)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP05 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP05)を指定し、GRP05のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP05)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP05 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP05)を指定し、GRP05のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP05)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP05)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHED1101 が画面・出力に表示されること
② ステップ2 の DFHED1102 が画面・出力に表示されること
③ ステップ3 の GROUP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0239"><h3>リソース定義 CEDA資源定義 構成監査 GRP08</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>構成監査では リソース定義 の 定義検査 を主操作として GRP08 を判定します。定義値と稼働値の一致への注意として「別グループの同名資源をインストールする危険があります」を GRP08 に残します。構成監査を補助する グループ導入 では DFHED1102 を補助値として GRP08 へ保存します。主判定の構成監査ではリソース定義・資源定義の 定義検査 から DFHED1101 を読み GRP08 へ残します。証跡照合の構成監査ではリソース定義・資源定義の DFHED1101 と DFHED1102 を GRP08 に保存します。記録対応の構成監査ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP08 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で リソース定義 の 定義検査 と グループ導入 を照合し 定義値と稼働値の一致 を確かめます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。DFHED1101 を読む前に対象 GRP08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのGRP08の出力を再利用する。今回のCEDA CHECK GROUP(GRP08)とCEDA INSTALL GROUP(GRP08)は実行済みとして扱う。</li><li>B. CEDA INSTALL GROUP(GRP08)の結果だけでは確定しない。CEDA CHECK GROUP(GRP08)のDFHED1101を主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEDA INSTALL GROUP(GRP08)のDFHED1102をグループ名とインストール結果の主判定に採用する。CEDA CHECK GROUP(GRP08)の応答は採取対象から外す。</li><li>D. CEDA DISPLAY GROUP(GRP08)のGROUPをDFHED1101と同義の成功表示として扱う。CEDA CHECK GROUP(GRP08)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 技術上の正答: Bは定義検査で DFHED1101 を読みグループ名とインストール結果の主値として構成差分を監査しGRP08に残します。
実行時の背景: 構成監査ではグループ導入を補助操作としCEDA資源定義の定義値と稼働値の一致をDFHED1102と対象GRP08で照合します。
四つの候補の理由: 定義検査とグループ導入の役割を分けるとA: 過去出力では今回の構成監査を示せない点でリソース定義に使いません、B: DFHED1101を主証跡として区別する点で正答です、C: DFHED1102はDFHED1101を代替しない点でGRP08を採用できません、D: GROUPとDFHED1101は確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のリソース定義・資源定義で判定する対象は GRP08 です。
初出語定義: 構成監査で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP08へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 構成監査 GRP08</strong></p><p>検証目的: リソース定義のCEDA資源定義について構成差分を監査し、GRP08のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP08)を指定し、GRP08の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP08)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP08 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP08)を指定し、GRP08のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP08)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP08 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP08)を指定し、GRP08のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP08)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP08)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFHED1101 が画面・出力に表示されること
② ステップ2 の DFHED1102 が画面・出力に表示されること
③ ステップ3 の GROUP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0240"><h3>リソース定義 CEDA資源定義 通常状態の確認 GRP01</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>通常状態の確認では リソース定義 の グループ表示 を主操作として GRP01 を判定します。基準値と現在値の差への注意として「別グループの同名資源をインストールする危険があります」を GRP01 に残します。通常状態の確認を補助する 定義検査 では DFHED1101 を補助値として GRP01 へ保存します。主判定の通常状態の確認ではリソース定義・資源定義の グループ表示 から GROUP を読み GRP01 へ残します。証跡照合の通常状態の確認ではリソース定義・資源定義の GROUP と DFHED1101 を GRP01 に保存します。記録対応の通常状態の確認ではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP01 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で リソース定義 の グループ表示 と 定義検査 を用い 通常状態を確定 します。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。GROUP で対象 GRP01 の グループ名とインストール結果 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. CEDA CHECK GROUP(GRP01)のDFHED1101をグループ名とインストール結果の主判定に採用する。CEDA DISPLAY GROUP(GRP01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. CEDA INSTALL GROUP(GRP01)のDFHED1102をGROUPと同義の成功表示として扱う。CEDA DISPLAY GROUP(GRP01)は実行しない。</li><li>C. CEDA DISPLAY GROUP(GRP01)を先に実行する。対象GRP01のGROUPをグループ名とインストール結果として記録する。続いてCEDA CHECK GROUP(GRP01)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. CEDA DISPLAY GROUP(GRP01)が応答を返した時点で正常とする。応答中のGROUPの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: Cはグループ表示で GROUP を読みグループ名とインストール結果の主値として通常状態を確定しGRP01に残します。
背景・仕組み: 通常状態の確認では定義検査を補助操作としCEDA資源定義の基準値と現在値の差をDFHED1101と対象GRP01で照合します。
選択肢の理由: グループ表示と定義検査の役割を分けるとA: DFHED1101はGROUPを代替しないうえに追加前提も不正な点でCEDA資源定義に使えません、B: DFHED1102とGROUPは確認項目が異なる点でGRP01を採用できません、C: GROUPを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではグループ名とインストール結果を判定できない点で一次資料と一致しません。結論として通常状態の確認のリソース定義・資源定義で判定する対象は GRP01 です。
用語の初出定義: 通常状態の確認で使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP01へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 通常状態の確認 GRP01</strong></p><p>検証目的: リソース定義のCEDA資源定義について通常状態を確定し、GRP01のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP01)を指定し、GRP01のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP01)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP01)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP01)を指定し、GRP01の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP01)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP01 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP01)を指定し、GRP01のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP01)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP01 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
② ステップ2 の DFHED1101 が画面・出力に表示されること
③ ステップ3 の DFHED1102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


<section class="kb-item" id="c04-i0241"><h3>リソース定義 CEDA資源定義 障害切り分け GRP04</h3><p class="kb-meta">分類: リソース定義 ・ 難易度: 初級</p><p>障害切り分けでは リソース定義 の グループ表示 を主操作として GRP04 を判定します。最初に失敗した処理への注意として「別グループの同名資源をインストールする危険があります」を GRP04 に残します。障害切り分けを補助する 定義検査 では DFHED1101 を補助値として GRP04 へ保存します。主判定の障害切り分けではリソース定義・資源定義の グループ表示 から GROUP を読み GRP04 へ残します。証跡照合の障害切り分けではリソース定義・資源定義の GROUP と DFHED1101 を GRP04 に保存します。記録対応の障害切り分けではリソース定義・資源定義の グループ名とインストール結果 の証跡へ GRP04 を結びます。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで リソース定義 の グループ表示 と 定義検査 の役割を分け 最初に失敗した処理 を調べます。CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能です。別グループの同名資源をインストールする危険があります。対象 GRP04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. CEDA INSTALL GROUP(GRP04)のDFHED1102をGROUPと同義の成功表示として扱う。CEDA DISPLAY GROUP(GRP04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. CEDA DISPLAY GROUP(GRP04)の出力でGRP04とGROUPが同じ応答にあることを確認する。グループ名とインストール結果をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. CEDA DISPLAY GROUP(GRP04)が応答を返した時点で正常とする。応答中のGROUPの値は記録しない。</li><li>D. CEDA DISPLAY GROUP(GRP04)のコマンド文字列だけを記録する。GROUPを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: Bはグループ表示で GROUP を読みグループ名とインストール結果の主値として障害範囲を限定しGRP04に残します。
技術的背景: 障害切り分けでは定義検査を補助操作としCEDA資源定義の最初に失敗した処理をDFHED1101と対象GRP04で照合します。
四択の評価: グループ表示と定義検査の役割を分けるとA: DFHED1102とGROUPは確認項目が異なるうえに追加前提も不正な点でGRP04を採用できません、B: GRP04とGROUPを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではグループ名とインストール結果を判定できない点で一次資料と一致しません、D: 入力記録だけではグループ名とインストール結果を証明できない点でグループ名とインストール結果を確認できません。結論として障害切り分けのリソース定義・資源定義で判定する対象は GRP04 です。
初出語の意味: 障害切り分けで使う CEDA資源定義 はCSDグループ内のCICS資源を表示、変更、検査、インストールする資源定義オンライン機能を表しグループ名とインストール結果を判定する際にGRP04へ適用します。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リソース定義 CEDA資源定義 障害切り分け GRP04</strong></p><p>検証目的: リソース定義のCEDA資源定義について障害範囲を限定し、GRP04のグループ名とインストール結果を実出力で確認する。</p><p>前提条件: CICS Transaction Server for z/OS 6.xの参照権限を持ち、対象GRP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: CICS Transaction Server for z/OS 6.xの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA DISPLAY GROUP(GRP04)を指定し、GRP04のグループ表示を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA DISPLAY GROUP(GRP04)
→ Enter を押す
［画面・出力］
CEDA DISPLAY GROUP(GRP04)
PROGRAM TRANSACTION FILE TCPIPSERVICE
画面・出力にあるGROUPを読み、グループ名とインストール結果と対象GRP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA CHECK GROUP(GRP04)を指定し、GRP04の定義検査を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA CHECK GROUP(GRP04)
→ Enter を押す
［画面・出力］
DFHED1101 GROUP GRP04 CHECKED. NO ERRORS FOUND
画面・出力にあるDFHED1101を読み、グループ名とインストール結果と対象GRP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はCICS Transaction Server for z/OS 6.xのリソース定義を確認する入力画面です。COMMAND入力口へCEDA INSTALL GROUP(GRP04)を指定し、GRP04のグループ導入を表示します。
［操作（入力）］
CICS Transaction Server for z/OS 6.x 操作画面
COMMAND ===&gt; CEDA INSTALL GROUP(GRP04)
→ Enter を押す
［画面・出力］
DFHED1102 GROUP GRP04 INSTALL SUCCESSFUL
画面・出力にあるDFHED1102を読み、グループ名とインストール結果と対象GRP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の GROUP が画面・出力に表示されること
② ステップ2 の DFHED1101 が画面・出力に表示されること
③ ステップ3 の DFHED1102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: transactions-reference_pdf / configuring_pdf / troubleshooting-guide_pdf / cics-codes_pdf / java-applications_pdf / internet-guide_pdf / cics-mq_pdf</p></div></details></section>


## 一時記憶


<section class="kb-item" id="c04-i0242"><h3>Temporary Storage Queue</h3><p class="kb-meta">分類: 一時記憶 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の 一時記憶で扱うTemporary Storage Queueは、CICS 内で一時的なデータを保存するキューです。端末処理の中間データや複数タスク間の受け渡しに使われます。保存場所や有効期間を理解しないと、再始動後のデータ有無を誤解します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認の一時記憶でトランザクション管理の運用確認を行います。Temporary Storage Queueの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. CICS TS と無関係な一覧で範囲確認の一時記憶を確認した扱いにする。</li><li>B. DFH4200A の有無を確認せず範囲確認の一時記憶を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. Temporary Storage Queueの属性行を読まず範囲確認の一時記憶の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Temporary Storage Queue は「CICS TS で Temporary Storage Queueの扱いを記録する範囲確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Temporary Storage Queueの表示結果と DFH4200A を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Temporary Storage Queueの使い方を出典欄から追跡し、資料名は範囲確認資料です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Temporary Storage Queue</strong></p><p>検証目的: 範囲確認の一時記憶について、CICS Transaction Server for z/OS 6.x の 一時記憶で扱う Temporary Storage Queueは、CICS 内で一時的なデータをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、範囲確認の一時記憶の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にTemporary Storage を指定し、OSKB010011の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND Temporary Storage 
CASE OSKB010011
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM Temporary Storage 
CASE OSKB010011
SOURCE CICS TS
Temporary Storage とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010011を同じ出力で読み、範囲確認の一時記憶の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010011
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010011
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A Temporary Storage Queue RESPONSE DISPLAYED
DFH4200AとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の Temporary Storage  と OSKB010011 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0243"><h3>Transient Data Queue</h3><p class="kb-meta">分類: 一時記憶 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の 一時記憶で扱うTransient Data Queueは、CICS が順次データをキューとして扱う機能です。内部キューと外部キューがあり、ログ出力や他処理への引き渡しに使われます。処理漏れを調べるときはキュー定義と読み取り側の状態を確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認の一時記憶に関する Transient Data Queueの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず優先確認の一時記憶の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認の一時記憶の証跡として保存して根拠にする。</li><li>C. Transient Data Queueの変更点を出力本文から切り離して優先確認の一時記憶の承認欄のみ残す。</li><li>D. DFH4200A を含む表示を保存し、説明欄との差分を優先確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では Transient Data Queue は「Transient Data Queueの状態と出力メッセージを結び付ける優先確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では Transient Data Queueの出力行と DFH4200A を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では Transient Data Queueを CICS TS の確認記録に残し、対象名は優先確認対象です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Transient Data Queue</strong></p><p>検証目的: 優先確認の一時記憶について、CICS Transaction Server for z/OS 6.x の 一時記憶で扱う Transient Data Queueは、CICS が順次データをキューとしてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、優先確認の一時記憶の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にTransient Data Queを指定し、OSKB010012の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND Transient Data Que
CASE OSKB010012
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM Transient Data Que
CASE OSKB010012
SOURCE CICS TS
Transient Data QueとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010012を同じ出力で読み、優先確認の一時記憶の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010012
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010012
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A Transient Data Queue RESPONSE DISPLAYED
DFH4200AとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の Transient Data Que と OSKB010012 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


## 基本概念


<section class="kb-item" id="c04-i0244"><h3>CICS リージョン</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の 基本概念で扱うCICS リージョンは、トランザクション、プログラム、ファイル、通信資源を実行する z/OS 上のアドレス空間です。端末処理やオンライン業務の実行単位になるため、起動 JCL、SIT、リソース定義を合わせて確認します。障害時はリージョン単位のメッセージとダンプを確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認のリージョンに関係する CICS リージョンの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. F CICSA,CEMT I TRAN(OSKB)の結果から対象行を抜き出し、構文確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. CICS リージョンの名称と担当者名のみを残して構文確認のリージョンの表示本文を確認対象に含めない。</li><li>C. トランザクション管理以外の画面で構文確認のリージョンを確認し同じ証跡として扱ったことにする。</li><li>D. DFH4200A の有無を見ず構文確認のリージョンの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では CICS リージョン は「CICS リージョンの用途をトランザクション管理の表示で確認する構文確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では CICS TS の CICS リージョンと DFH4200A を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では CICS リージョンを CICS Transaction Server for z/OS 6.xで扱う確認対象とし、用語名は構文確認用語です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CICS リージョン</strong></p><p>検証目的: 構文確認のリージョンについて、CICS Transaction Server for z/OS 6.x の 基本概念で扱う CICS リージョンは、トランザクション、プログラム、ファイル、通信資源を実行すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、構文確認のリージョンの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCICS リージョンを指定し、OSKB010001の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CICS リージョン
CASE OSKB010001
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CICS リージョン
CASE OSKB010001
SOURCE CICS TS
CICS リージョンとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010001を同じ出力で読み、構文確認のリージョンの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010001
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010001
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A CICS リージョン RESPONSE DISPLAYED
DFH4200AとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の CICS リージョン と OSKB010001 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0245"><h3>トランザクション ID</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 初級</p><p>CICS Transaction Server for z/OS 6.x の 基本概念で扱うトランザクション IDは、CICS で業務処理を起動するための短い識別子です。端末やプログラムから入力され、対応するプログラムやプロファイルへ結び付けられます。障害時は入力された ID と実行されたプログラムの対応を確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認のトランザクションでトランザクション ID の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. トランザクション ID の出力を取らず展開確認のトランザクションの説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. F CICSA,CEMT I TRAN(OSKB)を省略して展開確認のトランザクションの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認のトランザクションへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠ではトランザクション ID は「展開確認のトランザクションに関係する定義値と表示行を照合する展開確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡ではトランザクション ID の属性行と DFH4200A を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出ではトランザクション ID を CICS Transaction Server for z/OS 6.xの運用手順で確認し、初出名は展開確認初出です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トランザクション ID</strong></p><p>検証目的: 展開確認のトランザクションについて、CICS Transaction Server for z/OS 6.x の 基本概念で扱うトランザクション ID は、CICS で業務処理を起動するための短い識別子です。端に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、展開確認のトランザクションの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にトランザクション IDを指定し、OSKB010002の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND トランザクション ID
CASE OSKB010002
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM トランザクション ID
CASE OSKB010002
SOURCE CICS TS
トランザクション IDとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010002を同じ出力で読み、展開確認のトランザクションの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010002
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010002
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A トランザクション ID RESPONSE DISPLAYED
DFH4200AとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の トランザクション ID と OSKB010002 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0246"><h3>プログラム定義</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の 基本概念で扱うプログラム定義は、CICS が実行するアプリケーションプログラムの属性を登録するリソース定義です。言語、実行モード、再入可能性、ロード先などが実行時の挙動に影響します。新規リリース時は定義とロードライブラリの整合を確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認のプログラム定義でトランザクション管理の運用確認を行います。プログラム定義の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. CICS TS と無関係な一覧で呼出確認のプログラム定義を確認した扱いにする。</li><li>B. DFH4200A の有無を確認せず呼出確認のプログラム定義を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. プログラム定義の属性行を読まず呼出確認のプログラム定義の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠ではプログラム定義は「CICS TS でプログラム定義の扱いを記録する呼出確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡ではプログラム定義の表示結果と DFH4200A を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料ではプログラム定義の使い方を出典欄から追跡し、資料名は呼出確認資料です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プログラム定義</strong></p><p>検証目的: 呼出確認のプログラム定義について、CICS Transaction Server for z/OS 6.x の 基本概念で扱うプログラム定義は、CICS が実行するアプリケーションプログラムの属性を登録するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、呼出確認のプログラム定義の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にプログラム定義を指定し、OSKB010003の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND プログラム定義
CASE OSKB010003
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM プログラム定義
CASE OSKB010003
SOURCE CICS TS
プログラム定義とOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010003を同じ出力で読み、呼出確認のプログラム定義の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010003
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010003
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A プログラム定義 RESPONSE DISPLAYED
DFH4200AとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の プログラム定義 と OSKB010003 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


## 監視


<section class="kb-item" id="c04-i0247"><h3>CICS 統計</h3><p class="kb-meta">分類: 監視 ・ 難易度: 中級</p><p>CICS Transaction Server for z/OS 6.x の 監視で扱うCICS 統計は、リージョン、トランザクション、ファイル、ストレージなどの利用状況を示す運用情報です。性能傾向や容量計画、障害前後の比較に使います。統計の取得間隔とリセットタイミングを理解して読む必要があります</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認の統計でトランザクション管理の運用確認を行います。CICS 統計の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. CICS TS と無関係な一覧で監査確認の統計を確認した扱いにする。</li><li>B. DFH4200A の有無を確認せず監査確認の統計を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. CICS 統計の属性行を読まず監査確認の統計の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では CICS 統計 は「CICS TS で CICS 統計の扱いを記録する監査確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では CICS 統計の表示結果と DFH4200A を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では CICS 統計の使い方を出典欄から追跡し、資料名は監査確認資料です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CICS 統計</strong></p><p>検証目的: 監査確認の統計について、CICS Transaction Server for z/OS 6.x の 監視で扱う CICS 統計は、リージョン、トランザクション、ファイル、ストレージなどの利用状況をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、監査確認の統計の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCICS 統計を指定し、OSKB010019の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CICS 統計
CASE OSKB010019
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CICS 統計
CASE OSKB010019
SOURCE CICS TS
CICS 統計とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010019を同じ出力で読み、監査確認の統計の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010019
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010019
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A CICS 統計 RESPONSE DISPLAYED
DFH4200AとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の CICS 統計 と OSKB010019 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


## 相互通信


<section class="kb-item" id="c04-i0248"><h3>IPIC</h3><p class="kb-meta">分類: 相互通信 ・ 難易度: 上級</p><p>CICS Transaction Server for z/OS 6.x の 相互通信で扱うIPICは、TCP/IP を使って CICS 領域間や外部クライアントと接続する通信方式です。サービス連携や分散構成で使われ、証明書やセキュリティ設定とも関わります。疎通障害では TCP/IP、CICS 定義、認証の順に切り分けます</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認の相互通信に関係する IPIC の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. F CICSA,CEMT I TRAN(OSKB)で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. IPIC の名称と担当者名のみを残して警告確認の相互通信の表示本文を確認対象に含めない。</li><li>C. トランザクション管理以外の画面で警告確認の相互通信を確認し同じ証跡として扱ったことにする。</li><li>D. DFH4200A の有無を見ず警告確認の相互通信の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では IPIC は「IPIC の用途をトランザクション管理の表示で確認する警告確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では CICS TS の IPIC と DFH4200A を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では IPIC を CICS Transaction Server for z/OS 6.xで扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IPIC</strong></p><p>検証目的: 警告確認の相互通信について、CICS Transaction Server for z/OS 6.x の 相互通信で扱う IPIC は、TCP/IP を使って CICS 領域間や外部クライアントと接続するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、警告確認の相互通信の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にIPICを指定し、OSKB010017の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND IPIC
CASE OSKB010017
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM IPIC
CASE OSKB010017
SOURCE CICS TS
IPICとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010017を同じ出力で読み、警告確認の相互通信の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010017
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010017
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A IPIC RESPONSE DISPLAYED
DFH4200AとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の IPIC と OSKB010017 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


<section class="kb-item" id="c04-i0249"><h3>MRO</h3><p class="kb-meta">分類: 相互通信 ・ 難易度: 上級</p><p>CICS Transaction Server for z/OS 6.x の 相互通信で扱うMROは、同一 z/OS イメージ内または近接する CICS リージョン間で通信するための方式です。トランザクションルーティングや機能分散に使われます。接続障害ではローカルとリモートの定義を両側で確認します</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認の相互通信に関する MRO の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず値域確認の相互通信の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の相互通信の証跡として保存して根拠にする。</li><li>C. MRO の変更点を出力本文から切り離して値域確認の相互通信の承認欄のみ残す。</li><li>D. 同じ画面で対象行と DFH4200A を読み、値域確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では MRO は「MRO の状態と出力メッセージを結び付ける値域確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では MRO の出力行と DFH4200A を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では MRO を CICS TS の確認記録に残し、対象名は値域確認対象です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MRO</strong></p><p>検証目的: 値域確認の相互通信について、CICS Transaction Server for z/OS 6.x の 相互通信で扱う MRO は、同一 z/OS イメージ内または近接する CICS リージョン間で通信に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、値域確認の相互通信の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にMROを指定し、OSKB010016の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND MRO
CASE OSKB010016
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM MRO
CASE OSKB010016
SOURCE CICS TS
MROとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010016を同じ出力で読み、値域確認の相互通信の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010016
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010016
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A MRO RESPONSE DISPLAYED
DFH4200AとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の MRO と OSKB010016 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>


## 診断


<section class="kb-item" id="c04-i0250"><h3>CICS トランザクションダンプ</h3><p class="kb-meta">分類: 診断 ・ 難易度: 上級</p><p>CICS Transaction Server for z/OS 6.x の 診断で扱うCICS トランザクションダンプは、特定トランザクションの異常時状態を記録する診断資料です。プログラム、EXEC CICS 応答、作業領域の状態を調べる入口になります。ダンプコード、タスク番号、発生時刻をメッセージと対応させます</p><p class="kb-src"><strong>出典:</strong> CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認のトランザクションダンプに関する CICS トランザクションダンプの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. F CICSA,CEMT I TRAN(OSKB)の結果を残さず変更確認のトランザクションダンプの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認のトランザクションダンプの証跡として保存して根拠にする。</li><li>C. CICS トランザクションダンプの変更点を出力本文から切り離して変更確認のトランザクションダンプの承認欄のみ残す。</li><li>D. CICS TS の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では CICS トランザクションダンプ は「CICS トランザクションダンプの状態と出力メッセージを結び付ける変更確認項目」と F CICSA,CEMT I TRAN(OSKB)または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では CICS トランザクションダンプの出力行と DFH4200A を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では CICS トランザクションダンプを CICS TS の確認記録に残し、対象名は変更確認対象です。</p><p class="kb-src"><strong>出典:</strong> transactions-reference_pdf / administering_pdf / troubleshooting-guide_pdf</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CICS トランザクションダンプ</strong></p><p>検証目的: 変更確認のトランザクションダンプについて、CICS Transaction Server for z/OS 6.x の 診断で扱う CICS トランザクションダンプは、特定トランザクションの異常時状態を記録する診断資に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでF CICSA,CEMT I TRAN(OSKB)を実行し、DFH4200Aを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に F CICSA,CEMT I TRAN(OSKB) を入力し、変更確認のトランザクションダンプの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
COMMAND INPUTにF CICSA,CEMT I TRAN(OSKB)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCICS トランザクションダンプを指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CICS トランザクションダンプ
CASE OSKB010020
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CICS トランザクションダンプ
CASE OSKB010020
SOURCE CICS TS
CICS トランザクションダンプとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。DFH4200AとOSKB010020を同じ出力で読み、変更確認のトランザクションダンプの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB)
CASE OSKB010020
→ Enter を押す
［画面・出力］
CICS CONSOLE RESPONSE OSKB010020
F CICSA,CEMT I TRAN(OSKB)
STATUS: RESULTS - OVERTYPE TO MODIFY
DFH4200A CICS トランザクションダンプ RESPONSE DISPLAYED
DFH4200AとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; F CICSA,CEMT I TRAN(OSKB) が画面・出力に表示されること
② ステップ2 の CICS トランザクションダンプ と OSKB010020 が画面・出力に表示されること
③ ステップ3 の DFH4200A と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: CICS Transaction Server for z / OS V6 Developing CICS Applications / Administering CICS / System Programming Reference / Security for CICS</p></div></details></section>
