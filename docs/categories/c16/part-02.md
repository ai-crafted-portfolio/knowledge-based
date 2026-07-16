---
search:
  exclude: true
---

# IMS 15.5 — 詳細 (2/2)

[← IMS 15.5 の概要へ戻る](index.md)


## リスタート


<section class="kb-item" id="c16-i0180"><h3>リスタート IMS再始動点 変更後の確認 RST03</h3><p class="kb-meta">分類: リスタート ・ 難易度: 初級</p><p>変更後の確認では リスタート の 再始動記録 を主操作として RST03 を判定します。反映値と残存値への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST03 に残します。変更後の確認を補助する 通常再始動 では DFS058I を補助値として RST03 へ保存します。主判定の変更後の確認ではリスタート・再始動点の 再始動記録 から DFS3499I を読み RST03 へ残します。証跡照合の変更後の確認ではリスタート・再始動点の DFS3499I と DFS058I を RST03 に保存します。記録対応の変更後の確認ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で リスタート の 再始動記録 と 通常再始動 を用い 変更結果を検証 します。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS3499I で対象 RST03 の 使用チェックポイントとBUILDQ結果 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. IMS再始動点の停止または再定義を実施する。その後に/DISPLAY OLDSでDFS3499Iを採取する。</li><li>B. 障害診断のメッセージIDと理由コードを確認する。その値をリスタートのRST03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. /NRESTART BUILDQで周辺状態を押さえる。その後に/DISPLAY OLDSでDFS3499Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. /NRESTART BUILDQが成功したため/DISPLAY OLDSのDFS3499Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Cは再始動記録で DFS3499I を読み使用チェックポイントとBUILDQ結果の主値として変更結果を検証しRST03に残します。
内部の仕組み: 変更後の確認では通常再始動を補助操作としIMS再始動点の反映値と残存値をDFS058Iと対象RST03で照合します。
誤答を含む比較: 再始動記録と通常再始動の役割を分けるとA: 変更前の使用チェックポイントとBUILDQ結果を失う点で使用チェックポイントとBUILDQ結果を確認できません、B: 障害診断の値ではDFS3499Iを確認できないうえに追加前提も不正な点で通常再始動の範囲を越えます、C: 周辺状態の後にDFS3499Iを確認する点で現在値を示します、D: 補助操作の成功ではDFS3499Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のリスタート・再始動点で判定する対象は RST03 です。
用語定義: 変更後の確認で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 変更後の確認 RST03</strong></p><p>検証目的: リスタートのIMS再始動点について変更結果を検証し、RST03の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST03の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST03の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST03の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS3499I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0181"><h3>リスタート IMS再始動点 引継ぎ記録 RST09</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>引継ぎ記録では リスタート の 再始動記録 を主操作として RST09 を判定します。次担当者が追跡できる証跡への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST09 に残します。引継ぎ記録を補助する 通常再始動 では DFS058I を補助値として RST09 へ保存します。主判定の引継ぎ記録ではリスタート・再始動点の 再始動記録 から DFS3499I を読み RST09 へ残します。証跡照合の引継ぎ記録ではリスタート・再始動点の DFS3499I と DFS058I を RST09 に保存します。記録対応の引継ぎ記録ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で リスタート の 再始動記録 と 通常再始動 を用い 再現可能な記録を作成 します。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS3499I で対象 RST09 の 使用チェックポイントとBUILDQ結果 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 対象名RST09を指定して/DISPLAY OLDSを実行する。応答中のDFS3499Iと時刻を保存する。/NRESTART BUILDQで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. /NRESTART BUILDQが成功したため/DISPLAY OLDSのDFS3499Iも正常だと推定する。主出力は保存しない。</li><li>C. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をRST09の結果として記録する。</li><li>D. 前回保存した/DISPLAY OLDSの結果を使う。今回の/NRESTART BUILDQの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Aは再始動記録で DFS3499I を読み使用チェックポイントとBUILDQ結果の主値として再現可能な記録を作成しRST09に残します。
製品内の仕組み: 引継ぎ記録では通常再始動を補助操作としIMS再始動点の次担当者が追跡できる証跡をDFS058Iと対象RST09で照合します。
選択肢別の説明: 再始動記録と通常再始動の役割を分けるとA: DFS3499Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではDFS3499Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はRST09と確定できない点で再始動記録を代替しません、D: 採取時刻が異なる点でリスタートに使いません。結論として引継ぎ記録のリスタート・再始動点で判定する対象は RST09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 引継ぎ記録 RST09</strong></p><p>検証目的: リスタートのIMS再始動点について再現可能な記録を作成し、RST09の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST09の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST09の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST09の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS3499I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0182"><h3>リスタート IMS再始動点 復旧後の確認 RST06</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>復旧後の確認では リスタート の 再始動記録 を主操作として RST06 を判定します。再発していないことを示す値への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST06 に残します。復旧後の確認を補助する 通常再始動 では DFS058I を補助値として RST06 へ保存します。主判定の復旧後の確認ではリスタート・再始動点の 再始動記録 から DFS3499I を読み RST06 へ残します。証跡照合の復旧後の確認ではリスタート・再始動点の DFS3499I と DFS058I を RST06 に保存します。記録対応の復旧後の確認ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で リスタート の 再始動記録 と 通常再始動 の役割を分け 再発していないことを示す値 を調べます。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。対象 RST06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. リスタートの使用チェックポイントとBUILDQ結果を確認する。その値をリスタートのRST06にも適用する。</li><li>B. /DISPLAY OLDSでDFS3499Iを取得してから/ERESTART CHKPT 0でDFS680Iを照合する。RST06の使用チェックポイントとBUILDQ結果を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. /NRESTART BUILDQが成功したため/DISPLAY OLDSのDFS3499Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象RST06へ引き継げるものとする。IMS再始動点の再発していないことを示す値は確認済みとして扱う。さらに/ERESTART CHKPT 0のDFS680IをDFS3499Iと同種の値として併記する。</li><li>D. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をRST06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Bは再始動記録で DFS3499I を読み使用チェックポイントとBUILDQ結果の主値として復旧後の安定性を確認しRST06に残します。
構成上の背景: 復旧後の確認では通常再始動を補助操作としIMS再始動点の再発していないことを示す値をDFS058Iと対象RST06で照合します。
候補ごとの理由: 再始動記録と通常再始動の役割を分けるとA: リスタートの値ではDFS3499Iを確認できない点で通常再始動の範囲を越えます、B: DFS3499IとDFS680Iを順に照合する点で現在値を示します、C: 補助操作の成功ではDFS3499Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はRST06と確定できない点で再始動記録を代替しません。結論として復旧後の確認のリスタート・再始動点で判定する対象は RST06 です。
初出用語: 復旧後の確認で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 復旧後の確認 RST06</strong></p><p>検証目的: リスタートのIMS再始動点について復旧後の安定性を確認し、RST06の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST06の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST06の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST06の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS3499I が画面・出力に表示されること
② ステップ2 の DFS058I が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0183"><h3>リスタート IMS再始動点 復旧準備 RST05</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>復旧準備では リスタート の 緊急再始動 を主操作として RST05 を判定します。再開前に必要な整合性への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST05 に残します。復旧準備を補助する 再始動記録 では DFS3499I を補助値として RST05 へ保存します。主判定の復旧準備ではリスタート・再始動点の 緊急再始動 から DFS680I を読み RST05 へ残します。証跡照合の復旧準備ではリスタート・再始動点の DFS680I と DFS3499I を RST05 に保存します。記録対応の復旧準備ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で リスタート の 緊急再始動 と 再始動記録 を組み合わせる際は IMS再始動点 が停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みという仕組みを前提にします。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS680I と 使用チェックポイントとBUILDQ結果 を対象 RST05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 変更を加えず/ERESTART CHKPT 0を実行する。DFS680Iを保存する。差分は/DISPLAY OLDSの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存した/ERESTART CHKPT 0の結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのRST05の出力を再利用する。今回の/ERESTART CHKPT 0と/DISPLAY OLDSは実行済みとして扱う。</li><li>D. /DISPLAY OLDSのDFS3499Iを使用チェックポイントとBUILDQ結果の主判定に採用する。/ERESTART CHKPT 0の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aは緊急再始動で DFS680I を読み使用チェックポイントとBUILDQ結果の主値として復旧条件を確認しRST05に残します。
処理の仕組み: 復旧準備では再始動記録を補助操作としIMS再始動点の再開前に必要な整合性をDFS3499Iと対象RST05で照合します。
選択結果の内訳: 緊急再始動と再始動記録の役割を分けるとA: 変更前のDFS680Iを保存する点で緊急再始動に合います、B: 採取時刻が異なる点でリスタートに使いません、C: 過去出力では今回の復旧準備を示せない点でIMS再始動点に使えません、D: DFS3499IはDFS680Iを代替しないうえに追加前提も不正な点でRST05を採用できません。結論として復旧準備のリスタート・再始動点で判定する対象は RST05 です。
用語の説明: 復旧準備で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 復旧準備 RST05</strong></p><p>検証目的: リスタートのIMS再始動点について復旧条件を確認し、RST05の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST05の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST05の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST05の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS058I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0184"><h3>リスタート IMS再始動点 構成監査 RST08</h3><p class="kb-meta">分類: リスタート ・ 難易度: 中級</p><p>構成監査では リスタート の 緊急再始動 を主操作として RST08 を判定します。定義値と稼働値の一致への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST08 に残します。構成監査を補助する 再始動記録 では DFS3499I を補助値として RST08 へ保存します。主判定の構成監査ではリスタート・再始動点の 緊急再始動 から DFS680I を読み RST08 へ残します。証跡照合の構成監査ではリスタート・再始動点の DFS680I と DFS3499I を RST08 に保存します。記録対応の構成監査ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で リスタート の 緊急再始動 と 再始動記録 を実施し IMS再始動点 の役割を確認します。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。対象 RST08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのRST08の出力を再利用する。今回の/ERESTART CHKPT 0と/DISPLAY OLDSは実行済みとして扱う。</li><li>B. /DISPLAY OLDSのDFS3499Iを使用チェックポイントとBUILDQ結果の主判定に採用する。/ERESTART CHKPT 0の応答は採取対象から外す。</li><li>C. /NRESTART BUILDQのDFS058IをDFS680Iと同義の成功表示として扱う。/ERESTART CHKPT 0は実行しない。</li><li>D. /DISPLAY OLDSの結果だけでは確定しない。/ERESTART CHKPT 0のDFS680Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dは緊急再始動で DFS680I を読み使用チェックポイントとBUILDQ結果の主値として構成差分を監査しRST08に残します。
実行時の背景: 構成監査では再始動記録を補助操作としIMS再始動点の定義値と稼働値の一致をDFS3499Iと対象RST08で照合します。
四つの候補の理由: 緊急再始動と再始動記録の役割を分けるとA: 過去出力では今回の構成監査を示せない点でリスタートに使いません、B: DFS3499IはDFS680Iを代替しない点でIMS再始動点に使えません、C: DFS058IとDFS680Iは確認項目が異なる点でRST08を採用できません、D: DFS680Iを主証跡として区別する点で主証跡になります。結論として構成監査のリスタート・再始動点で判定する対象は RST08 です。
初出語定義: 構成監査で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 構成監査 RST08</strong></p><p>検証目的: リスタートのIMS再始動点について構成差分を監査し、RST08の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST08の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST08の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST08の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
② ステップ2 の DFS3499I が画面・出力に表示されること
③ ステップ3 の DFS058I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0185"><h3>リスタート IMS再始動点 通常状態の確認 RST01</h3><p class="kb-meta">分類: リスタート ・ 難易度: 初級</p><p>通常状態の確認では リスタート の 通常再始動 を主操作として RST01 を判定します。基準値と現在値の差への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST01 に残します。通常状態の確認を補助する 緊急再始動 では DFS680I を補助値として RST01 へ保存します。主判定の通常状態の確認ではリスタート・再始動点の 通常再始動 から DFS058I を読み RST01 へ残します。証跡照合の通常状態の確認ではリスタート・再始動点の DFS058I と DFS680I を RST01 に保存します。記録対応の通常状態の確認ではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で リスタート の 通常再始動 と 緊急再始動 を使い 通常状態を確定 します。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS058I を読み対象 RST01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. /NRESTART BUILDQを先に実行する。対象RST01のDFS058Iを使用チェックポイントとBUILDQ結果として記録する。続いて/ERESTART CHKPT 0で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. /ERESTART CHKPT 0のDFS680Iを使用チェックポイントとBUILDQ結果の主判定に採用する。/NRESTART BUILDQの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. /DISPLAY OLDSのDFS3499IをDFS058Iと同義の成功表示として扱う。/NRESTART BUILDQは実行しない。</li><li>D. /NRESTART BUILDQが応答を返した時点で正常とする。応答中のDFS058Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: Aは通常再始動で DFS058I を読み使用チェックポイントとBUILDQ結果の主値として通常状態を確定しRST01に残します。
背景・仕組み: 通常状態の確認では緊急再始動を補助操作としIMS再始動点の基準値と現在値の差をDFS680Iと対象RST01で照合します。
選択肢の理由: 通常再始動と緊急再始動の役割を分けるとA: DFS058Iを主値として補助結果と照合する点で正答です、B: DFS680IはDFS058Iを代替しないうえに追加前提も不正な点でRST01を採用できません、C: DFS3499IとDFS058Iは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけでは使用チェックポイントとBUILDQ結果を判定できない点で一次資料と一致しません。結論として通常状態の確認のリスタート・再始動点で判定する対象は RST01 です。
用語の初出定義: 通常状態の確認で使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 通常状態の確認 RST01</strong></p><p>検証目的: リスタートのIMS再始動点について通常状態を確定し、RST01の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST01の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST01の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST01の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の DFS3499I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0186"><h3>リスタート IMS再始動点 障害切り分け RST04</h3><p class="kb-meta">分類: リスタート ・ 難易度: 初級</p><p>障害切り分けでは リスタート の 通常再始動 を主操作として RST04 を判定します。最初に失敗した処理への注意として「誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います」を RST04 に残します。障害切り分けを補助する 緊急再始動 では DFS680I を補助値として RST04 へ保存します。主判定の障害切り分けではリスタート・再始動点の 通常再始動 から DFS058I を読み RST04 へ残します。証跡照合の障害切り分けではリスタート・再始動点の DFS058I と DFS680I を RST04 に保存します。記録対応の障害切り分けではリスタート・再始動点の 使用チェックポイントとBUILDQ結果 の証跡へ RST04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで リスタート の 通常再始動 と 緊急再始動 を照合し 最初に失敗した処理 を確かめます。IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みです。誤った再始動点を選ぶとメッセージキューまたは更新の整合を失います。DFS058I を読む前に対象 RST04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY OLDSのDFS3499IをDFS058Iと同義の成功表示として扱う。/NRESTART BUILDQは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. /NRESTART BUILDQが応答を返した時点で正常とする。応答中のDFS058Iの値は記録しない。</li><li>C. /NRESTART BUILDQのコマンド文字列だけを記録する。DFS058Iを含む応答行は保存しない。</li><li>D. /NRESTART BUILDQの出力でRST04とDFS058Iが同じ応答にあることを確認する。使用チェックポイントとBUILDQ結果をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: Dは通常再始動で DFS058I を読み使用チェックポイントとBUILDQ結果の主値として障害範囲を限定しRST04に残します。
技術的背景: 障害切り分けでは緊急再始動を補助操作としIMS再始動点の最初に失敗した処理をDFS680Iと対象RST04で照合します。
四択の評価: 通常再始動と緊急再始動の役割を分けるとA: DFS3499IとDFS058Iは確認項目が異なるうえに追加前提も不正な点でRST04を採用できません、B: 応答の有無だけでは使用チェックポイントとBUILDQ結果を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけでは使用チェックポイントとBUILDQ結果を証明できない点で一次資料と一致しません、D: RST04とDFS058Iを同じ応答で結ぶ点でRST04を判定できます。結論として障害切り分けのリスタート・再始動点で判定する対象は RST04 です。
初出語の意味: 障害切り分けで使う IMS再始動点 は停止チェックポイントとログを使い、通常再始動または緊急再始動の開始位置を選ぶ仕組みを表し使用チェックポイントとBUILDQ結果を判定する際にRST04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リスタート IMS再始動点 障害切り分け RST04</strong></p><p>検証目的: リスタートのIMS再始動点について障害範囲を限定し、RST04の使用チェックポイントとBUILDQ結果を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象RST04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/NRESTART BUILDQを指定し、RST04の通常再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /NRESTART BUILDQ
→ Enter を押す
［画面・出力］
DFS058I 08.58.20 NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
DFS994I *CHKPT 82170/090315**SIMPLE*
画面・出力にあるDFS058Iを読み、使用チェックポイントとBUILDQ結果と対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/ERESTART CHKPT 0を指定し、RST04の緊急再始動を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /ERESTART CHKPT 0
→ Enter を押す
［画面・出力］
DFS058I ERESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82120/101318
画面・出力にあるDFS680Iを読み、使用チェックポイントとBUILDQ結果と対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のリスタートを確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、RST04の再始動記録を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: MODBLKSA IMSACBA FORMATA MODSTAT ID: 1
DFS3804I LATEST RESTART CHKPT: 82120/101318
画面・出力にあるDFS3499Iを読み、使用チェックポイントとBUILDQ結果と対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS058I が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の DFS3499I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


## ログ管理


<section class="kb-item" id="c16-i0187"><h3>/CHECKPOINT DUMPQ 戻りコード確認 表形式</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>IMS 15.5 の ログ管理 で扱う「/CHECKPOINT DUMPQ 戻りコード確認 表形式」は、メッセージキューを保持して停止するためのチェックポイント操作を戻りコード確認の観点で確認する技術項目です。DFS058I 行とOLDS5を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT DUMPQ 戻りコード確認 表形式</strong></p><p>検証目的: ログ管理における/CHECKPOINT DUMPQの戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS5</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD095
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
DBDS DBD095.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0188"><h3>/CHECKPOINT DUMPQ 整合確認 チューニング値</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 中級</p><p>IMS 15.5 の ログ管理 で扱う「/CHECKPOINT DUMPQ 整合確認 チューニング値」は、メッセージキューを保持して停止するためのチェックポイント操作を整合確認の観点で確認する技術項目です。DFS058I 行とOLDS5を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT DUMPQ 整合確認 チューニング値</strong></p><p>検証目的: ログ管理における/CHECKPOINT DUMPQの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=OLDS5</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSUDMP0.CNTL(IMGCPY)
→ Enter を押す
［画面・出力］
DFSUDMP0 DATABASE IMAGE COPY UTILITY
DBDNAME=DBD035
IMAGE COPY DATA SET CREATED
RETURN CODE = 0000
画面・出力には DFSUDMP0 が含まれ、DFSUDMP0を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
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
DBDS DBD035.DBDS01 RECOVERED
RETURN CODE = 0000
画面・出力には DFSURDB0 が含まれ、DFSURDB0を残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSUDMP0 が画面・出力に表示されること
② ステップ2 の DFSUCUM0 が画面・出力に表示されること
③ ステップ3 の DFSURDB0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0189"><h3>DBRC RECON record 状態確認 照合単位</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 初級</p><p>IMS 15.5 の ログ管理 で扱う「DBRC RECON record 状態確認 照合単位」は、DBDS、イメージコピー、ログ、変更累積のリカバリ管理情報を保持するRECON記録を状態確認の観点で確認する技術項目です。DFS058I 行とDBD011を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC RECON record 状態確認 照合単位</strong></p><p>検証目的: ログ管理におけるDBRC RECON recordの状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD011</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY011
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY011 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD011
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD011 ACCESS UPDATES ALLOWED DBRC REGISTERED
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


<section class="kb-item" id="c16-i0190"><h3>DBRC RECON record 登録確認 状態確認</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 中級</p><p>IMS 15.5 の ログ管理 で扱う「DBRC RECON record 登録確認 状態確認」は、DBDS、イメージコピー、ログ、変更累積のリカバリ管理情報を保持するRECON記録を登録確認の観点で確認する技術項目です。DFS058I 行とDBD071を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC RECON record 登録確認 状態確認</strong></p><p>検証目的: ログ管理におけるDBRC RECON recordの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=DBD071</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY TRAN PAY071
→ Enter を押す
［画面・出力］
DFS000I TRANSACTION PAY071 CLASS 001 STATUS STARTED QUEUE 000000
画面・出力には DFS000I が含まれ、DFS000Iを確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD071
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD071 ACCESS UPDATES ALLOWED DBRC REGISTERED
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


<section class="kb-item" id="c16-i0191"><h3>DFS058I リカバリ確認 起動確認</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>IMS 15.5 の ログ管理 で扱う「DFS058I リカバリ確認 起動確認」は、/NRESTART処理開始を示すIMSメッセージをリカバリ確認の観点で確認する技術項目です。DFS058I 行と82122/082220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS058I リカバリ確認 起動確認</strong></p><p>検証目的: ログ管理におけるDFS058Iのリカバリ確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82122/082220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
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


<section class="kb-item" id="c16-i0192"><h3>DFS058I 登録確認 サンプル採取</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 中級</p><p>IMS 15.5 の ログ管理 で扱う「DFS058I 登録確認 サンプル採取」は、/NRESTART処理開始を示すIMSメッセージを登録確認の観点で確認する技術項目です。DFS058I 行と82132/082220を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS058I 登録確認 サンプル採取</strong></p><p>検証目的: ログ管理におけるDFS058Iの登録確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=82132/082220</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
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


<section class="kb-item" id="c16-i0193"><h3>DFSUCUM0 戻りコード確認 時刻情報</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 中級</p><p>IMS 15.5 の ログ管理 で扱う「DFSUCUM0 戻りコード確認 時刻情報」は、SLDS/RLDSの変更記録を変更累積データセットへまとめるIMSユーティリティを戻りコード確認の観点で確認する技術項目です。DFS058I 行とPORT2を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSUCUM0 戻りコード確認 時刻情報</strong></p><p>検証目的: ログ管理におけるDFSUCUM0の戻りコード確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PORT2</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; LIST.DBDS DBD(DBD047)
→ Enter を押す
［画面・出力］
DBRC LIST.DBDS
DBD=DBD047  DD=DBDS01  RECON=RECON2
IMAGE COPY NEEDED: NO
画面・出力には DBRC が含まれ、DBRCを確認し、再始動点の誤認を避けるため対象の現在値を固定する。
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


<section class="kb-item" id="c16-i0194"><h3>IMS catalog 出力項目確認 戻し条件</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 中級</p><p>IMS 15.5 の ログ管理 で扱う「IMS catalog 出力項目確認 戻し条件」は、IMS管理ACBでアクティブ定義の参照元になるカタログを出力項目確認の観点で確認する技術項目です。DFS058I 行とPSB059を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS catalog 出力項目確認 戻し条件</strong></p><p>検証目的: ログ管理におけるIMS catalogの出力項目確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PSB059</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMS TYPE(LCLPARM)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;lclparm&gt;DFSDF001&lt;/lclparm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; INIT.DBDS DBD(DBD059) DDN(DBDS01) CATALOG(IMSCD3)
→ Enter を押す
［画面・出力］
DBRC COMMAND COMPLETE
DBD DBD059 READ FROM IMS CATALOG IMSCD3
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


<section class="kb-item" id="c16-i0195"><h3>ログ管理 OLDSとSLDS管理 ログとの照合 LOG07</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>ログとの照合では ログ管理 の OLDS表示 を主操作として LOG07 を判定します。時刻と対象識別子への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG07 に残します。ログとの照合を補助する DBRCログ一覧 では SLDS を補助値として LOG07 へ保存します。主判定のログとの照合ではログ管理・管理の OLDS表示 から IMSLOGR を読み LOG07 へ残します。証跡照合のログとの照合ではログ管理・管理の IMSLOGR と SLDS を LOG07 に保存します。記録対応のログとの照合ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で ログ管理 の OLDS表示 と DBRCログ一覧 を用い 操作とログを対応 します。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。IMSLOGR で対象 LOG07 の アクティブログとアーカイブ先 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY OLDSが応答を返した時点で正常とする。応答中のIMSLOGRの値は記録しない。SIMPLEをIMSLOGRと同じ判定値とみなし対象LOG07の主証跡にする。</li><li>B. /DISPLAY OLDSのコマンド文字列だけを記録する。IMSLOGRを含む応答行は保存しない。</li><li>C. IMSLOGRを含むOLDS表示の応答行を保存する。その応答を得るため/DISPLAY OLDSを使用する。対象LOG07のアクティブログとアーカイブ先として記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. OLDSとSLDS管理の停止または再定義を実施する。その後に/DISPLAY OLDSでIMSLOGRを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: CはOLDS表示で IMSLOGR を読みアクティブログとアーカイブ先の主値として操作とログを対応しLOG07に残します。
機能の仕組み: ログとの照合ではDBRCログ一覧を補助操作としOLDSとSLDS管理の時刻と対象識別子をSLDSと対象LOG07で照合します。
各候補の評価: OLDS表示とDBRCログ一覧の役割を分けるとA: 応答の有無だけではアクティブログとアーカイブ先を判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではアクティブログとアーカイブ先を証明できない点で一次資料と一致しません、C: IMSLOGRの実値を対象別に残す点でLOG07を判定できます、D: 変更前のアクティブログとアーカイブ先を失う点でDBRCログ一覧の範囲を越えます。結論としてログとの照合のログ管理・管理で判定する対象は LOG07 です。
用語の定義: ログとの照合で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 ログとの照合 LOG07</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について操作とログを対応し、LOG07のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG07のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG07のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS07 ARCHIVED TO SLDS07
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG07の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100720**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSLOGR が画面・出力に表示されること
② ステップ2 の SLDS が画面・出力に表示されること
③ ステップ3 の SIMPLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0196"><h3>ログ管理 OLDSとSLDS管理 代替経路の確認 LOG10</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>代替経路の確認では ログ管理 の OLDS表示 を主操作として LOG10 を判定します。主経路との役割差への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG10 に残します。代替経路の確認を補助する DBRCログ一覧 では SLDS を補助値として LOG10 へ保存します。主判定の代替経路の確認ではログ管理・管理の OLDS表示 から IMSLOGR を読み LOG10 へ残します。証跡照合の代替経路の確認ではログ管理・管理の IMSLOGR と SLDS を LOG10 に保存します。記録対応の代替経路の確認ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で ログ管理 の OLDS表示 と DBRCログ一覧 の役割を分け 主経路との役割差 を調べます。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。対象 LOG10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY OLDSのコマンド文字列だけを記録する。IMSLOGRを含む応答行は保存しない。</li><li>B. /DISPLAY OLDSとLIST.LOG ALLの対象名をそろえる。前者のIMSLOGRをアクティブログとアーカイブ先の判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. OLDSとSLDS管理の停止または再定義を実施する。その後に/DISPLAY OLDSでIMSLOGRを採取する。</li><li>D. リスタートの使用チェックポイントとBUILDQ結果を確認する。その値をログ管理のLOG10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: BはOLDS表示で IMSLOGR を読みアクティブログとアーカイブ先の主値として代替手段の成立を確認しLOG10に残します。
運用上の背景: 代替経路の確認ではDBRCログ一覧を補助操作としOLDSとSLDS管理の主経路との役割差をSLDSと対象LOG10で照合します。
候補別の検討: OLDS表示とDBRCログ一覧の役割を分けるとA: 入力記録だけではアクティブログとアーカイブ先を証明できない点で一次資料と一致しません、B: 同じ対象名のIMSLOGRを採用する点でLOG10を判定できます、C: 変更前のアクティブログとアーカイブ先を失う点でDBRCログ一覧の範囲を越えます、D: リスタートの値ではIMSLOGRを確認できない点でLOG10の値を示しません。結論として代替経路の確認のログ管理・管理で判定する対象は LOG10 です。
重要用語の定義: 代替経路の確認で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 代替経路の確認 LOG10</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について代替手段の成立を確認し、LOG10のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG10のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG10のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS10 ARCHIVED TO SLDS10
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG10の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/101020**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSLOGR が画面・出力に表示されること
② ステップ2 の SLDS が画面・出力に表示されること
③ ステップ3 の SIMPLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0197"><h3>ログ管理 OLDSとSLDS管理 変更前の確認 LOG02</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>変更前の確認では ログ管理 の DBRCログ一覧 を主操作として LOG02 を判定します。変更対象と非対象の境界への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG02 に残します。変更前の確認を補助する 単純チェックポイント では SIMPLE を補助値として LOG02 へ保存します。主判定の変更前の確認ではログ管理・管理の DBRCログ一覧 から SLDS を読み LOG02 へ残します。証跡照合の変更前の確認ではログ管理・管理の SLDS と SIMPLE を LOG02 に保存します。記録対応の変更前の確認ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で ログ管理 の DBRCログ一覧 と 単純チェックポイント を照合し 変更対象と非対象の境界 を確かめます。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。SLDS を読む前に対象 LOG02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. LIST.LOG ALLを対象名なしで実行する。一覧の先頭行をLOG02の結果として記録する。</li><li>B. 対象LOG02についてLIST.LOG ALLの応答からSLDSを確認する。/CHECKPOINT SIMPLEは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したLIST.LOG ALLの結果を使う。今回の/CHECKPOINT SIMPLEの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのLOG02の出力を再利用する。今回のLIST.LOG ALLと/CHECKPOINT SIMPLEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用理由: BはDBRCログ一覧で SLDS を読みアクティブログとアーカイブ先の主値として変更前の証跡を保存しLOG02に残します。
動作の背景: 変更前の確認では単純チェックポイントを補助操作としOLDSとSLDS管理の変更対象と非対象の境界をSIMPLEと対象LOG02で照合します。
各選択肢の検討: DBRCログ一覧と単純チェックポイントの役割を分けるとA: 先頭行はLOG02と確定できない点で変更前の確認に合いません、B: SLDSと補助証跡の時刻を合わせる点でDBRCログ一覧に合います、C: 採取時刻が異なる点でログ管理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でOLDSとSLDS管理に使えません。結論として変更前の確認のログ管理・管理で判定する対象は LOG02 です。
初出用語の定義: 変更前の確認で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 変更前の確認 LOG02</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について変更前の証跡を保存し、LOG02のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG02のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS02 ARCHIVED TO SLDS02
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG02の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100220**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG02のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SLDS が画面・出力に表示されること
② ステップ2 の SIMPLE が画面・出力に表示されること
③ ステップ3 の IMSLOGR が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0198"><h3>ログ管理 OLDSとSLDS管理 変更後の確認 LOG03</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>変更後の確認では ログ管理 の 単純チェックポイント を主操作として LOG03 を判定します。反映値と残存値への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG03 に残します。変更後の確認を補助する OLDS表示 では IMSLOGR を補助値として LOG03 へ保存します。主判定の変更後の確認ではログ管理・管理の 単純チェックポイント から SIMPLE を読み LOG03 へ残します。証跡照合の変更後の確認ではログ管理・管理の SIMPLE と IMSLOGR を LOG03 に保存します。記録対応の変更後の確認ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で ログ管理 の 単純チェックポイント と OLDS表示 を組み合わせる際は OLDSとSLDS管理 がオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みという仕組みを前提にします。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。SIMPLE と アクティブログとアーカイブ先 を対象 LOG03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. OLDSとSLDS管理の停止または再定義を実施する。その後に/CHECKPOINT SIMPLEでSIMPLEを採取する。</li><li>B. IMS Connectのポートと接続先メンバーを確認する。その値をログ管理のLOG03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. /DISPLAY OLDSで周辺状態を押さえる。その後に/CHECKPOINT SIMPLEでSIMPLEを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. /DISPLAY OLDSが成功したため/CHECKPOINT SIMPLEのSIMPLEも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答の根拠: Cは単純チェックポイントで SIMPLE を読みアクティブログとアーカイブ先の主値として変更結果を検証しLOG03に残します。
内部の仕組み: 変更後の確認ではOLDS表示を補助操作としOLDSとSLDS管理の反映値と残存値をIMSLOGRと対象LOG03で照合します。
誤答を含む比較: 単純チェックポイントとOLDS表示の役割を分けるとA: 変更前のアクティブログとアーカイブ先を失う点でアクティブログとアーカイブ先を確認できません、B: IMS Connectの値ではSIMPLEを確認できないうえに追加前提も不正な点でOLDS表示の範囲を越えます、C: 周辺状態の後にSIMPLEを確認する点で現在値を示します、D: 補助操作の成功ではSIMPLEを確定できない点で変更後の確認に合いません。結論として変更後の確認のログ管理・管理で判定する対象は LOG03 です。
用語定義: 変更後の確認で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 変更後の確認 LOG03</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について変更結果を検証し、LOG03のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG03の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100320**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG03のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG03のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS03 ARCHIVED TO SLDS03
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SIMPLE が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の SLDS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0199"><h3>ログ管理 OLDSとSLDS管理 引継ぎ記録 LOG09</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>引継ぎ記録では ログ管理 の 単純チェックポイント を主操作として LOG09 を判定します。次担当者が追跡できる証跡への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG09 に残します。引継ぎ記録を補助する OLDS表示 では IMSLOGR を補助値として LOG09 へ保存します。主判定の引継ぎ記録ではログ管理・管理の 単純チェックポイント から SIMPLE を読み LOG09 へ残します。証跡照合の引継ぎ記録ではログ管理・管理の SIMPLE と IMSLOGR を LOG09 に保存します。記録対応の引継ぎ記録ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で ログ管理 の 単純チェックポイント と OLDS表示 を組み合わせる際は OLDSとSLDS管理 がオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みという仕組みを前提にします。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。SIMPLE と アクティブログとアーカイブ先 を対象 LOG09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 対象名LOG09を指定して/CHECKPOINT SIMPLEを実行する。応答中のSIMPLEと時刻を保存する。/DISPLAY OLDSで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. /DISPLAY OLDSが成功したため/CHECKPOINT SIMPLEのSIMPLEも正常だと推定する。主出力は保存しない。</li><li>C. /CHECKPOINT SIMPLEを対象名なしで実行する。一覧の先頭行をLOG09の結果として記録する。</li><li>D. 前回保存した/CHECKPOINT SIMPLEの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: Aは単純チェックポイントで SIMPLE を読みアクティブログとアーカイブ先の主値として再現可能な記録を作成しLOG09に残します。
製品内の仕組み: 引継ぎ記録ではOLDS表示を補助操作としOLDSとSLDS管理の次担当者が追跡できる証跡をIMSLOGRと対象LOG09で照合します。
選択肢別の説明: 単純チェックポイントとOLDS表示の役割を分けるとA: SIMPLEと時刻を保存する点で現在値を示します、B: 補助操作の成功ではSIMPLEを確定できない点で引継ぎ記録に合いません、C: 先頭行はLOG09と確定できない点で単純チェックポイントを代替しません、D: 採取時刻が異なる点でログ管理に使いません。結論として引継ぎ記録のログ管理・管理で判定する対象は LOG09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 引継ぎ記録 LOG09</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について再現可能な記録を作成し、LOG09のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG09の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100920**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG09のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG09のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS09 ARCHIVED TO SLDS09
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SIMPLE が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の SLDS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0200"><h3>ログ管理 OLDSとSLDS管理 復旧後の確認 LOG06</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>復旧後の確認では ログ管理 の 単純チェックポイント を主操作として LOG06 を判定します。再発していないことを示す値への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG06 に残します。復旧後の確認を補助する OLDS表示 では IMSLOGR を補助値として LOG06 へ保存します。主判定の復旧後の確認ではログ管理・管理の 単純チェックポイント から SIMPLE を読み LOG06 へ残します。証跡照合の復旧後の確認ではログ管理・管理の SIMPLE と IMSLOGR を LOG06 に保存します。記録対応の復旧後の確認ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で ログ管理 の 単純チェックポイント と OLDS表示 を実施し OLDSとSLDS管理 の役割を確認します。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。対象 LOG06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. ログ管理のアクティブログとアーカイブ先を確認する。その値をログ管理のLOG06にも適用する。</li><li>B. /CHECKPOINT SIMPLEでSIMPLEを取得してからLIST.LOG ALLでSLDSを照合する。LOG06のアクティブログとアーカイブ先を両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY OLDSが成功したため/CHECKPOINT SIMPLEのSIMPLEも正常だと推定する。主出力は保存しない。別資源で得た状態を対象LOG06へ引き継げるものとする。</li><li>D. /CHECKPOINT SIMPLEを対象名なしで実行する。一覧の先頭行をLOG06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答内容: Bは単純チェックポイントで SIMPLE を読みアクティブログとアーカイブ先の主値として復旧後の安定性を確認しLOG06に残します。
構成上の背景: 復旧後の確認ではOLDS表示を補助操作としOLDSとSLDS管理の再発していないことを示す値をIMSLOGRと対象LOG06で照合します。
候補ごとの理由: 単純チェックポイントとOLDS表示の役割を分けるとA: ログ管理の値ではSIMPLEを確認できない点でOLDS表示の範囲を越えます、B: SIMPLEとSLDSを順に照合する点で現在値を示します、C: 補助操作の成功ではSIMPLEを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はLOG06と確定できない点で単純チェックポイントを代替しません。結論として復旧後の確認のログ管理・管理で判定する対象は LOG06 です。
初出用語: 復旧後の確認で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 復旧後の確認 LOG06</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について復旧後の安定性を確認し、LOG06のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG06の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100620**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG06のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG06のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS06 ARCHIVED TO SLDS06
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SIMPLE が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の SLDS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0201"><h3>ログ管理 OLDSとSLDS管理 復旧準備 LOG05</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>復旧準備では ログ管理 の DBRCログ一覧 を主操作として LOG05 を判定します。再開前に必要な整合性への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG05 に残します。復旧準備を補助する 単純チェックポイント では SIMPLE を補助値として LOG05 へ保存します。主判定の復旧準備ではログ管理・管理の DBRCログ一覧 から SLDS を読み LOG05 へ残します。証跡照合の復旧準備ではログ管理・管理の SLDS と SIMPLE を LOG05 に保存します。記録対応の復旧準備ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で ログ管理 の DBRCログ一覧 と 単純チェックポイント を使い 復旧条件を確認 します。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。SLDS を読み対象 LOG05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずLIST.LOG ALLを実行する。SLDSを保存する。差分は/CHECKPOINT SIMPLEの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したLIST.LOG ALLの結果を使う。今回の/CHECKPOINT SIMPLEの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのLOG05の出力を再利用する。今回のLIST.LOG ALLと/CHECKPOINT SIMPLEは実行済みとして扱う。</li><li>D. /CHECKPOINT SIMPLEのSIMPLEをアクティブログとアーカイブ先の主判定に採用する。LIST.LOG ALLの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 選定理由: AはDBRCログ一覧で SLDS を読みアクティブログとアーカイブ先の主値として復旧条件を確認しLOG05に残します。
処理の仕組み: 復旧準備では単純チェックポイントを補助操作としOLDSとSLDS管理の再開前に必要な整合性をSIMPLEと対象LOG05で照合します。
選択結果の内訳: DBRCログ一覧と単純チェックポイントの役割を分けるとA: 変更前のSLDSを保存する点でDBRCログ一覧に合います、B: 採取時刻が異なる点でログ管理に使いません、C: 過去出力では今回の復旧準備を示せない点でOLDSとSLDS管理に使えません、D: SIMPLEはSLDSを代替しないうえに追加前提も不正な点でLOG05を採用できません。結論として復旧準備のログ管理・管理で判定する対象は LOG05 です。
用語の説明: 復旧準備で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 復旧準備 LOG05</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について復旧条件を確認し、LOG05のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG05のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS05 ARCHIVED TO SLDS05
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG05の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100520**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG05のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SLDS が画面・出力に表示されること
② ステップ2 の SIMPLE が画面・出力に表示されること
③ ステップ3 の IMSLOGR が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0202"><h3>ログ管理 OLDSとSLDS管理 構成監査 LOG08</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>構成監査では ログ管理 の DBRCログ一覧 を主操作として LOG08 を判定します。定義値と稼働値の一致への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG08 に残します。構成監査を補助する 単純チェックポイント では SIMPLE を補助値として LOG08 へ保存します。主判定の構成監査ではログ管理・管理の DBRCログ一覧 から SLDS を読み LOG08 へ残します。証跡照合の構成監査ではログ管理・管理の SLDS と SIMPLE を LOG08 に保存します。記録対応の構成監査ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で ログ管理 の DBRCログ一覧 と 単純チェックポイント を照合し 定義値と稼働値の一致 を確かめます。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。SLDS を読む前に対象 LOG08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのLOG08の出力を再利用する。今回のLIST.LOG ALLと/CHECKPOINT SIMPLEは実行済みとして扱う。</li><li>B. /CHECKPOINT SIMPLEのSIMPLEをアクティブログとアーカイブ先の主判定に採用する。LIST.LOG ALLの応答は採取対象から外す。</li><li>C. /DISPLAY OLDSのIMSLOGRをSLDSと同義の成功表示として扱う。LIST.LOG ALLは実行しない。</li><li>D. /CHECKPOINT SIMPLEの結果だけでは確定しない。LIST.LOG ALLのSLDSを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: DはDBRCログ一覧で SLDS を読みアクティブログとアーカイブ先の主値として構成差分を監査しLOG08に残します。
実行時の背景: 構成監査では単純チェックポイントを補助操作としOLDSとSLDS管理の定義値と稼働値の一致をSIMPLEと対象LOG08で照合します。
四つの候補の理由: DBRCログ一覧と単純チェックポイントの役割を分けるとA: 過去出力では今回の構成監査を示せない点でログ管理に使いません、B: SIMPLEはSLDSを代替しない点でOLDSとSLDS管理に使えません、C: IMSLOGRとSLDSは確認項目が異なる点でLOG08を採用できません、D: SLDSを主証跡として区別する点で主証跡になります。結論として構成監査のログ管理・管理で判定する対象は LOG08 です。
初出語定義: 構成監査で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 構成監査 LOG08</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について構成差分を監査し、LOG08のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG08のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS08 ARCHIVED TO SLDS08
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG08の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100820**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG08のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SLDS が画面・出力に表示されること
② ステップ2 の SIMPLE が画面・出力に表示されること
③ ステップ3 の IMSLOGR が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0203"><h3>ログ管理 OLDSとSLDS管理 通常状態の確認 LOG01</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>通常状態の確認では ログ管理 の OLDS表示 を主操作として LOG01 を判定します。基準値と現在値の差への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG01 に残します。通常状態の確認を補助する DBRCログ一覧 では SLDS を補助値として LOG01 へ保存します。主判定の通常状態の確認ではログ管理・管理の OLDS表示 から IMSLOGR を読み LOG01 へ残します。証跡照合の通常状態の確認ではログ管理・管理の IMSLOGR と SLDS を LOG01 に保存します。記録対応の通常状態の確認ではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で ログ管理 の OLDS表示 と DBRCログ一覧 を用い 通常状態を確定 します。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。IMSLOGR で対象 LOG01 の アクティブログとアーカイブ先 を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY OLDSを先に実行する。対象LOG01のIMSLOGRをアクティブログとアーカイブ先として記録する。続いてLIST.LOG ALLで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. LIST.LOG ALLのSLDSをアクティブログとアーカイブ先の主判定に採用する。/DISPLAY OLDSの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. /CHECKPOINT SIMPLEのSIMPLEをIMSLOGRと同義の成功表示として扱う。/DISPLAY OLDSは実行しない。</li><li>D. /DISPLAY OLDSが応答を返した時点で正常とする。応答中のIMSLOGRの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解の説明: AはOLDS表示で IMSLOGR を読みアクティブログとアーカイブ先の主値として通常状態を確定しLOG01に残します。
背景・仕組み: 通常状態の確認ではDBRCログ一覧を補助操作としOLDSとSLDS管理の基準値と現在値の差をSLDSと対象LOG01で照合します。
選択肢の理由: OLDS表示とDBRCログ一覧の役割を分けるとA: IMSLOGRを主値として補助結果と照合する点で正答です、B: SLDSはIMSLOGRを代替しないうえに追加前提も不正な点でLOG01を採用できません、C: SIMPLEとIMSLOGRは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではアクティブログとアーカイブ先を判定できない点で一次資料と一致しません。結論として通常状態の確認のログ管理・管理で判定する対象は LOG01 です。
用語の初出定義: 通常状態の確認で使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 通常状態の確認 LOG01</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について通常状態を確定し、LOG01のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG01のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG01のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS01 ARCHIVED TO SLDS01
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG01の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100120**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSLOGR が画面・出力に表示されること
② ステップ2 の SLDS が画面・出力に表示されること
③ ステップ3 の SIMPLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0204"><h3>ログ管理 OLDSとSLDS管理 障害切り分け LOG04</h3><p class="kb-meta">分類: ログ管理 ・ 難易度: 上級</p><p>障害切り分けでは ログ管理 の OLDS表示 を主操作として LOG04 を判定します。最初に失敗した処理への注意として「OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります」を LOG04 に残します。障害切り分けを補助する DBRCログ一覧 では SLDS を補助値として LOG04 へ保存します。主判定の障害切り分けではログ管理・管理の OLDS表示 から IMSLOGR を読み LOG04 へ残します。証跡照合の障害切り分けではログ管理・管理の IMSLOGR と SLDS を LOG04 に保存します。記録対応の障害切り分けではログ管理・管理の アクティブログとアーカイブ先 の証跡へ LOG04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで ログ管理 の OLDS表示 と DBRCログ一覧 の役割を分け 最初に失敗した処理 を調べます。OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みです。OLDS切替とSLDS登録の差を見落とすと復旧ログ範囲を誤ります。対象 LOG04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. /CHECKPOINT SIMPLEのSIMPLEをIMSLOGRと同義の成功表示として扱う。/DISPLAY OLDSは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. /DISPLAY OLDSが応答を返した時点で正常とする。応答中のIMSLOGRの値は記録しない。</li><li>C. /DISPLAY OLDSのコマンド文字列だけを記録する。IMSLOGRを含む応答行は保存しない。</li><li>D. /DISPLAY OLDSの出力でLOG04とIMSLOGRが同じ応答にあることを確認する。アクティブログとアーカイブ先をその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい操作の説明: DはOLDS表示で IMSLOGR を読みアクティブログとアーカイブ先の主値として障害範囲を限定しLOG04に残します。
技術的背景: 障害切り分けではDBRCログ一覧を補助操作としOLDSとSLDS管理の最初に失敗した処理をSLDSと対象LOG04で照合します。
四択の評価: OLDS表示とDBRCログ一覧の役割を分けるとA: SIMPLEとIMSLOGRは確認項目が異なるうえに追加前提も不正な点でLOG04を採用できません、B: 応答の有無だけではアクティブログとアーカイブ先を判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではアクティブログとアーカイブ先を証明できない点で一次資料と一致しません、D: LOG04とIMSLOGRを同じ応答で結ぶ点でLOG04を判定できます。結論として障害切り分けのログ管理・管理で判定する対象は LOG04 です。
初出語の意味: 障害切り分けで使う OLDSとSLDS管理 はオンラインログをOLDSへ記録し、アーカイブ後はSLDSまたはRLDSとしてDBRCへ登録する仕組みを表しアクティブログとアーカイブ先を判定する際にLOG04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ログ管理 OLDSとSLDS管理 障害切り分け LOG04</strong></p><p>検証目的: ログ管理のOLDSとSLDS管理について障害範囲を限定し、LOG04のアクティブログとアーカイブ先を実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象LOG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、LOG04のOLDS表示を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS3499I ACTIVE DDNAMES: OLDS1 OLDS2 IMSLOGR
DFS3804I LATEST RESTART CHKPT: 82170/085820
画面・出力にあるIMSLOGRを読み、アクティブログとアーカイブ先と対象LOG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へLIST.LOG ALLを指定し、LOG04のDBRCログ一覧を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; LIST.LOG ALL
→ Enter を押す
［画面・出力］
DBRC LIST.LOG
OLDS04 ARCHIVED TO SLDS04
RLDS STATUS AVAILABLE
画面・出力にあるSLDSを読み、アクティブログとアーカイブ先と対象LOG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5のログ管理を確認する入力画面です。COMMAND入力口へ/CHECKPOINT SIMPLEを指定し、LOG04の単純チェックポイントを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /CHECKPOINT SIMPLE
→ Enter を押す
［画面・出力］
DFS994I *CHKPT 82170/100420**SIMPLE*
画面・出力にあるSIMPLEを読み、アクティブログとアーカイブ先と対象LOG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IMSLOGR が画面・出力に表示されること
② ステップ2 の SLDS が画面・出力に表示されること
③ ステップ3 の SIMPLE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


## 共通サービス


<section class="kb-item" id="c16-i0205"><h3>Operations Manager</h3><p class="kb-meta">分類: 共通サービス ・ 難易度: 上級</p><p>IMS 15.5 の 共通サービスで扱うOperations Managerは、IMSplex のコマンド処理と運用制御を支える共通サービスです。複数 IMS へのコマンド発行や応答管理に関わります。運用自動化では OM がどの IMS を対象にしているかを確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認の共通サービスに関する Operations Managerの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果を残さず値域確認の共通サービスの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の共通サービスの証跡として保存して根拠にする。</li><li>C. Operations Managerの変更点を出力本文から切り離して値域確認の共通サービスの承認欄のみ残す。</li><li>D. 同じ画面で対象行と DFS058I を読み、値域確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Operations Manager は「Operations Managerの状態と出力メッセージを結び付ける値域確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Operations Managerの出力行と DFS058I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Operations Managerを IMS 15.5の確認記録に残し、対象名は値域確認対象です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Operations Manager</strong></p><p>検証目的: 値域確認の共通サービスについて、IMS 15.5 の 共通サービスで扱う Operations Managerは、IMSplex のコマンド処理と運用制御を支える共通サービスです。複数 IMS へのコマンドに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、値域確認の共通サービスの確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にOperations Managerを指定し、OSKB010016の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND Operations Manager
CASE OSKB010016
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM Operations Manager
CASE OSKB010016
SOURCE IMS 15.5
Operations ManagerとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010016を同じ出力で読み、値域確認の共通サービスの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010016
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010016
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010016  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の Operations Manager と OSKB010016 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0206"><h3>Resource Manager</h3><p class="kb-meta">分類: 共通サービス ・ 難易度: 上級</p><p>IMS 15.5 の 共通サービスで扱うResource Managerは、IMSplex 内のリソース情報を管理する共通サービスです。リソース状態や定義情報を複数 IMS 間で扱う構成で使われます。IMSplex の問題では RM と各 IMS メンバーの情報差異を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認の共通サービスに関係する Resource Managerの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. Resource Managerの名称と担当者名のみを残して警告確認の共通サービスの表示本文を確認対象に含めない。</li><li>C. アイエムエス以外の画面で警告確認の共通サービスを確認し同じ証跡として扱ったことにする。</li><li>D. DFS058I の有無を見ず警告確認の共通サービスの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Resource Manager は「Resource Managerの用途をアイエムエスの表示で確認する警告確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IMS 15.5の Resource Managerと DFS058I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Resource Managerを IMS 15.5で扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Resource Manager</strong></p><p>検証目的: 警告確認の共通サービスについて、IMS 15.5 の 共通サービスで扱う Resource Managerは、IMSplex 内のリソース情報を管理する共通サービスです。リソース状態や定義情報を複数 IMSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、警告確認の共通サービスの確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にResource Managerを指定し、OSKB010017の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND Resource Manager
CASE OSKB010017
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM Resource Manager
CASE OSKB010017
SOURCE IMS 15.5
Resource ManagerとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010017を同じ出力で読み、警告確認の共通サービスの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010017
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010017
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010017  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の Resource Manager と OSKB010017 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## 回復管理


<section class="kb-item" id="c16-i0207"><h3>DBRC</h3><p class="kb-meta">分類: 回復管理 ・ 難易度: 中級</p><p>IMS 15.5 の 回復管理で扱うDBRCは、IMS データベースの回復に必要なログ、イメージコピー、データベース状態を管理する機能です。RECON データセットを通じて復旧可否や必要資源を判断します。リカバリ作業では DBRC 登録状態が前提になります</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認の回復管理に関する DBRC の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果を残さず優先確認の回復管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認の回復管理の証跡として保存して根拠にする。</li><li>C. DBRC の変更点を出力本文から切り離して優先確認の回復管理の承認欄のみ残す。</li><li>D. DFS058I を含む表示を保存し、説明欄との差分を優先確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では DBRC は「DBRC の状態と出力メッセージを結び付ける優先確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では DBRC の出力行と DFS058I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では DBRC を IMS 15.5の確認記録に残し、対象名は優先確認対象です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBRC</strong></p><p>検証目的: 優先確認の回復管理について、IMS 15.5 の 回復管理で扱う DBRC は、IMS データベースの回復に必要なログ、イメージコピー、データベース状態を管理する機能です。RECON データセットを通じてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、優先確認の回復管理の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にDBRCを指定し、OSKB010012の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND DBRC
CASE OSKB010012
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM DBRC
CASE OSKB010012
SOURCE IMS 15.5
DBRCとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010012を同じ出力で読み、優先確認の回復管理の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010012
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010012
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010012  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の DBRC と OSKB010012 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0208"><h3>Database Recovery utility DFSURDB0</h3><p class="kb-meta">分類: 回復管理 ・ 難易度: 上級</p><p>IMS 15.5 の 回復管理で扱うDatabase Recovery utility DFSURDB0は、DFSURDB0 は、IMS データベースの forward recovery を行う Database Recovery utility です。イメージコピーとログを使って障害後の状態を復元します。実行前に DBRC 情報と必要ログが揃っているかを確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較確認の回復管理で Database Recovery utilitの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. Database Recovery utilitの出力を取らず比較確認の回復管理の説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY TRANSACTION OSKB を省略して比較確認の回復管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認の回復管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では Database Recovery utilit は「比較確認の回復管理に関係する定義値と表示行を照合する比較確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では Database Recovery utilitの属性行と DFS058I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では Database Recovery utilitを IMS 15.5の運用手順で確認し、初出名は比較確認初出です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Database Recovery utility DFSURDB0</strong></p><p>検証目的: 比較確認の回復管理について、IMS 15.5 の 回復管理で扱う Database Recovery utility DFSURDB0 は、DFSURDB0 は、IMS データベースの forward rに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、比較確認の回復管理の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にDatabase Recovery を指定し、OSKB010014の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND Database Recovery 
CASE OSKB010014
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM Database Recovery 
CASE OSKB010014
SOURCE IMS 15.5
Database Recovery とOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010014を同じ出力で読み、比較確認の回復管理の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010014
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010014
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010014  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の Database Recovery  と OSKB010014 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0209"><h3>RECON データセット</h3><p class="kb-meta">分類: 回復管理 ・ 難易度: 中級</p><p>IMS 15.5 の 回復管理で扱うRECON データセットは、DBRC が管理する回復制御情報を保持する重要なデータセットです。データベース、ログ、コピー、サブシステムの履歴が含まれます。RECON の保全と多重化は、IMS 回復性の中心になります</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認のデータセットに関係する RECON データセットの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果から対象行を抜き出し、記録確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. RECON データセットの名称と担当者名のみを残して記録確認のデータセットの表示本文を確認対象に含めない。</li><li>C. アイエムエス以外の画面で記録確認のデータセットを確認し同じ証跡として扱ったことにする。</li><li>D. DFS058I の有無を見ず記録確認のデータセットの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では RECON データセット は「RECON データセットの用途をアイエムエスの表示で確認する記録確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では IMS 15.5の RECON データセットと DFS058I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では RECON データセットを IMS 15.5で扱う確認対象とし、用語名は記録確認用語です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECON データセット</strong></p><p>検証目的: 記録確認のデータセットについて、IMS 15.5 の 回復管理で扱う RECON データセットは、DBRC が管理する回復制御情報を保持する重要なデータセットです。データベース、ログ、コピー、サブシステムのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、記録確認のデータセットの確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にRECON データセットを指定し、OSKB010013の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND RECON データセット
CASE OSKB010013
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM RECON データセット
CASE OSKB010013
SOURCE IMS 15.5
RECON データセットとOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010013を同じ出力で読み、記録確認のデータセットの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010013
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010013
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010013  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の RECON データセット と OSKB010013 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## 基本概念


<section class="kb-item" id="c16-i0210"><h3>IMS Database Manager</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 中級</p><p>IMS 15.5 の 基本概念で扱うIMS Database Managerは、IMS データベースへのアクセス、更新、回復に関わる機能群です。DBD、PSB、DBRC と結び付いて、アプリケーションがどのデータ構造を使えるかを決めます。障害時はデータベース状態とログ、RECON 情報を合わせて確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認の基本概念で IMS Database Managerの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. IMS Database Managerの出力を取らず展開確認の基本概念の説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY TRANSACTION OSKB を省略して展開確認の基本概念の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認の基本概念へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では IMS Database Manager は「展開確認の基本概念に関係する定義値と表示行を照合する展開確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では IMS Database Managerの属性行と DFS058I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では IMS Database Managerを IMS 15.5の運用手順で確認し、初出名は展開確認初出です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Database Manager</strong></p><p>検証目的: 展開確認の基本概念について、IMS 15.5 の 基本概念で扱う IMS Database Managerは、IMS データベースへのアクセス、更新、回復に関わる機能群です。DBD、PSB、DBRC とに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、展開確認の基本概念の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にIMS Database Managを指定し、OSKB010002の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND IMS Database Manag
CASE OSKB010002
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM IMS Database Manag
CASE OSKB010002
SOURCE IMS 15.5
IMS Database ManagとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010002を同じ出力で読み、展開確認の基本概念の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010002
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010002
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010002  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の IMS Database Manag と OSKB010002 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0211"><h3>IMS Transaction Manager</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 中級</p><p>IMS 15.5 の 基本概念で扱うIMS Transaction Managerは、端末やアプリケーションからのトランザクションを受け付け、メッセージ処理プログラムへ渡す機能です。MPP や BMP などの領域種別と組み合わせて実行形態を決めます。遅延や滞留を見るときはキューと領域状態を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認の基本概念でアイエムエスの運用確認を行います。IMS Transaction Managerの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IMS 15.5と無関係な一覧で呼出確認の基本概念を確認した扱いにする。</li><li>B. DFS058I の有無を確認せず呼出確認の基本概念を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. IMS Transaction Managerの属性行を読まず呼出確認の基本概念の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では IMS Transaction Manager は「IMS 15.5で IMS Transaction Managerの扱いを記録する呼出確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では IMS Transaction Managerの表示結果と DFS058I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では IMS Transaction Managerの使い方を出典欄から追跡し、資料名は呼出確認資料です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Transaction Manager</strong></p><p>検証目的: 呼出確認の基本概念について、IMS 15.5 の 基本概念で扱う IMS Transaction Managerは、端末やアプリケーションからのトランザクションを受け付け、メッセージ処理プログラムへ渡すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、呼出確認の基本概念の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にIMS Transaction Maを指定し、OSKB010003の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND IMS Transaction Ma
CASE OSKB010003
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM IMS Transaction Ma
CASE OSKB010003
SOURCE IMS 15.5
IMS Transaction MaとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010003を同じ出力で読み、呼出確認の基本概念の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010003
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010003
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010003  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の IMS Transaction Ma と OSKB010003 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0212"><h3>IMS システム</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 初級</p><p>IMS 15.5 の 基本概念で扱うIMS システムは、階層型データベース管理とトランザクション処理を提供する z/OS 上の基幹処理基盤です。Database Manager と Transaction Manager の構成要素を分けて理解すると、DB 障害と端末処理障害を切り分けやすくなります。運用では制御領域、従属領域、共通サービスの状態を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認のシステムに関係する IMS システムの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果から対象行を抜き出し、構文確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. IMS システムの名称と担当者名のみを残して構文確認のシステムの表示本文を確認対象に含めない。</li><li>C. アイエムエス以外の画面で構文確認のシステムを確認し同じ証跡として扱ったことにする。</li><li>D. DFS058I の有無を見ず構文確認のシステムの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では IMS システム は「IMS システムの用途をアイエムエスの表示で確認する構文確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IMS 15.5の IMS システムと DFS058I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では IMS システムを IMS 15.5で扱う確認対象とし、用語名は構文確認用語です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS システム</strong></p><p>検証目的: 構文確認のシステムについて、IMS 15.5 の 基本概念で扱う IMS システムは、階層型データベース管理とトランザクション処理を提供する z/OS 上の基幹処理基盤です。Database Managに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、構文確認のシステムの確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にIMS システムを指定し、OSKB010001の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND IMS システム
CASE OSKB010001
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM IMS システム
CASE OSKB010001
SOURCE IMS 15.5
IMS システムとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010001を同じ出力で読み、構文確認のシステムの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010001
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010001
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010001  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の IMS システム と OSKB010001 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## 定義体


<section class="kb-item" id="c16-i0213"><h3>ACB</h3><p class="kb-meta">分類: 定義体 ・ 難易度: 中級</p><p>IMS 15.5 の 定義体で扱うACBは、DBD と PSB から生成される IMS 実行時用の制御情報です。オンライン実行時には ACBLIB やカタログ化された ACB が参照されます。定義変更後に ACB が更新されていないと、ソース定義と実行時の動きがずれます</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認の定義体でアイエムエスの運用確認を行います。ACB の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IMS 15.5と無関係な一覧で上書確認の定義体を確認した扱いにする。</li><li>B. DFS058I の有無を確認せず上書確認の定義体を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. ACB の属性行を読まず上書確認の定義体の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では ACB は「IMS 15.5で ACB の扱いを記録する上書確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では ACB の表示結果と DFS058I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では ACB の使い方を出典欄から追跡し、資料名は上書確認資料です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ACB</strong></p><p>検証目的: 上書確認の定義体について、IMS 15.5 の 定義体で扱う ACB は、DBD と PSB から生成される IMS 実行時用の制御情報です。オンライン実行時には ACBLIB やカタログ化された ACに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、上書確認の定義体の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にACBを指定し、OSKB010007の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND ACB
CASE OSKB010007
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM ACB
CASE OSKB010007
SOURCE IMS 15.5
ACBとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010007を同じ出力で読み、上書確認の定義体の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010007
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010007
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010007  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の ACB と OSKB010007 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0214"><h3>DBD</h3><p class="kb-meta">分類: 定義体 ・ 難易度: 初級</p><p>IMS 15.5 の 定義体で扱うDBDは、IMS データベースの構造、セグメント、アクセス方式を記述する定義体です。アプリケーションが実データを読む前提になるため、物理構造や索引の変更時には DBD の整合性が重要です。DBD ライブラリと ACB 生成の関係も確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認の定義体に関する DBD の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果を残さず置換確認の定義体の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認の定義体の証跡として保存して根拠にする。</li><li>C. DBD の変更点を出力本文から切り離して置換確認の定義体の承認欄のみ残す。</li><li>D. 同じ画面で対象行と DFS058I を読み、置換確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では DBD は「DBD の状態と出力メッセージを結び付ける置換確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では DBD の出力行と DFS058I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では DBD を IMS 15.5の確認記録に残し、対象名は置換確認対象です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD</strong></p><p>検証目的: 置換確認の定義体について、IMS 15.5 の 定義体で扱う DBD は、IMS データベースの構造、セグメント、アクセス方式を記述する定義体です。アプリケーションが実データを読む前提になるため、物理構に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、置換確認の定義体の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にDBDを指定し、OSKB010004の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND DBD
CASE OSKB010004
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM DBD
CASE OSKB010004
SOURCE IMS 15.5
DBDとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010004を同じ出力で読み、置換確認の定義体の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010004
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010004
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010004  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の DBD と OSKB010004 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0215"><h3>PCB</h3><p class="kb-meta">分類: 定義体 ・ 難易度: 中級</p><p>IMS 15.5 の 定義体で扱うPCBは、IMS アプリケーションがデータベースやメッセージキューへアクセスするための制御ブロックです。DB PCB と I/O PCB では役割が異なり、呼び出し時に使う PCB を間違えると処理対象も変わります。プログラム障害では PCB マスクとステータスコードを確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認の定義体で PCB の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. PCB の出力を取らず探索確認の定義体の説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY TRANSACTION OSKB を省略して探索確認の定義体の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認の定義体へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では PCB は「探索確認の定義体に関係する定義値と表示行を照合する探索確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では PCB の属性行と DFS058I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では PCB を IMS 15.5の運用手順で確認し、初出名は探索確認初出です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PCB</strong></p><p>検証目的: 探索確認の定義体について、IMS 15.5 の 定義体で扱う PCB は、IMS アプリケーションがデータベースやメッセージキューへアクセスするための制御ブロックです。DB PCB と I/O PCBに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、探索確認の定義体の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にPCBを指定し、OSKB010006の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND PCB
CASE OSKB010006
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM PCB
CASE OSKB010006
SOURCE IMS 15.5
PCBとOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010006を同じ出力で読み、探索確認の定義体の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010006
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010006
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010006  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の PCB と OSKB010006 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0216"><h3>PSB</h3><p class="kb-meta">分類: 定義体 ・ 難易度: 初級</p><p>IMS 15.5 の 定義体で扱うPSBは、IMS アプリケーションが利用する PCB をまとめたプログラム仕様ブロックです。プログラムがどのデータベースやメッセージキューにアクセスできるかを定義します。権限やデータ構造の問題を調べるときは、PSB と PCB の対応を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認の定義体に関係する PSB の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. PSB の名称と担当者名のみを残して終端確認の定義体の表示本文を確認対象に含めない。</li><li>C. アイエムエス以外の画面で終端確認の定義体を確認し同じ証跡として扱ったことにする。</li><li>D. DFS058I の有無を見ず終端確認の定義体の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では PSB は「PSB の用途をアイエムエスの表示で確認する終端確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IMS 15.5の PSB と DFS058I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では PSB を IMS 15.5で扱う確認対象とし、用語名は終端確認用語です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PSB</strong></p><p>検証目的: 終端確認の定義体について、IMS 15.5 の 定義体で扱う PSB は、IMS アプリケーションが利用する PCB をまとめたプログラム仕様ブロックです。プログラムがどのデータベースやメッセージキューに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、終端確認の定義体の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にPSBを指定し、OSKB010005の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND PSB
CASE OSKB010005
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM PSB
CASE OSKB010005
SOURCE IMS 15.5
PSBとOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010005を同じ出力で読み、終端確認の定義体の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010005
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010005
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010005  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の PSB と OSKB010005 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## 接続


<section class="kb-item" id="c16-i0217"><h3>IMS Connect</h3><p class="kb-meta">分類: 接続 ・ 難易度: 中級</p><p>IMS 15.5 の 接続で扱うIMS Connectは、TCP/IP 経由で外部クライアントと IMS トランザクションやデータアクセスをつなぐ機能です。分散アプリケーションから IMS を利用する入口になるため、ポート、セキュリティ、OTMA 連携を確認します。障害時は IMS Connect と IMS 本体の境界を分けて見ます</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認の接続でアイエムエスの運用確認を行います。IMS Connectの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IMS 15.5と無関係な一覧で順序確認の接続を確認した扱いにする。</li><li>B. DFS058I の有無を確認せず順序確認の接続を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. IMS Connectの属性行を読まず順序確認の接続の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では IMS Connect は「IMS 15.5で IMS Connectの扱いを記録する順序確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では IMS Connectの表示結果と DFS058I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では IMS Connectの使い方を出典欄から追跡し、資料名は順序確認資料です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS Connect</strong></p><p>検証目的: 順序確認の接続について、IMS 15.5 の 接続で扱う IMS Connectは、TCP/IP 経由で外部クライアントと IMS トランザクションやデータアクセスをつなぐ機能です。分散アプリケーシに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、順序確認の接続の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にIMS Connectを指定し、OSKB010015の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND IMS Connect
CASE OSKB010015
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM IMS Connect
CASE OSKB010015
SOURCE IMS 15.5
IMS ConnectとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010015を同じ出力で読み、順序確認の接続の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010015
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010015
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010015  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の IMS Connect と OSKB010015 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## 運用


<section class="kb-item" id="c16-i0218"><h3>IMS チェックポイント</h3><p class="kb-meta">分類: 運用 ・ 難易度: 中級</p><p>IMS 15.5 の 運用で扱うIMS チェックポイントは、再始動や回復の基準点として処理状態を記録する仕組みです。BMP やオンライン処理では、チェックポイント間隔が回復時間と処理負荷に影響します。長時間処理ではチェックポイント設計を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認のチェックポイントに関する IMS チェックポイントの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果を残さず変更確認のチェックポイントの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認のチェックポイントの証跡として保存して根拠にする。</li><li>C. IMS チェックポイントの変更点を出力本文から切り離して変更確認のチェックポイントの承認欄のみ残す。</li><li>D. IMS 15.5の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では IMS チェックポイント は「IMS チェックポイントの状態と出力メッセージを結び付ける変更確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では IMS チェックポイントの出力行と DFS058I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では IMS チェックポイントを IMS 15.5の確認記録に残し、対象名は変更確認対象です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMS チェックポイント</strong></p><p>検証目的: 変更確認のチェックポイントについて、IMS 15.5 の 運用で扱う IMS チェックポイントは、再始動や回復の基準点として処理状態を記録する仕組みです。BMP やオンライン処理では、チェックポイント間隔が回復に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、変更確認のチェックポイントの確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にIMS チェックポイントを指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND IMS チェックポイント
CASE OSKB010020
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM IMS チェックポイント
CASE OSKB010020
SOURCE IMS 15.5
IMS チェックポイントとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010020を同じ出力で読み、変更確認のチェックポイントの根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010020
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010020
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010020  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の IMS チェックポイント と OSKB010020 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


## 障害診断


<section class="kb-item" id="c16-i0219"><h3>/CHECKPOINT PURGE 実行条件確認 ディスク状態</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>IMS 15.5 の 障害診断 で扱う「/CHECKPOINT PURGE 実行条件確認 ディスク状態」は、DBCTLでBMP完了を待つ停止系チェックポイント操作を実行条件確認の観点で確認する技術項目です。DFS680I 行とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT PURGE 実行条件確認 ディスク状態</strong></p><p>検証目的: 障害診断における/CHECKPOINT PURGEの実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD096
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
DBDNAME=DBD096
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD096
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD096 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0220"><h3>/CHECKPOINT PURGE 接続確認 オンライン状態</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 中級</p><p>IMS 15.5 の 障害診断 で扱う「/CHECKPOINT PURGE 接続確認 オンライン状態」は、DBCTLでBMP完了を待つ停止系チェックポイント操作を接続確認の観点で確認する技術項目です。DFS680I 行とODBM4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ログ入力DDの不足を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>/CHECKPOINT PURGE 接続確認 オンライン状態</strong></p><p>検証目的: 障害診断における/CHECKPOINT PURGEの接続確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=ODBM4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGU0.CNTL(UNLOAD)
→ Enter を押す
［画面・出力］
DFSURGU0 HD REORGANIZATION UNLOAD UTILITY
DBDNAME=DBD036
UNLOAD DATA SET WRITTEN
RETURN CODE = 0000
画面・出力には DFSURGU0 が含まれ、DFSURGU0を確認し、ログ入力DDの不足を避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; SUBMIT IMS.DFSURGL0.CNTL(RELOAD)
→ Enter を押す
［画面・出力］
DFSURGL0 HD REORGANIZATION RELOAD UTILITY
DBDNAME=DBD036
DATABASE RELOADED
RETURN CODE = 0000
画面・出力には DFSURGL0 が含まれ、DFSURGL0を読み、出典資料の出力項目と運用記録を対応させる。
――――
■ ステップ 3
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、後続確認用の表示または完了コードを採取する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; /DISPLAY DATABASE DBD036
→ Enter を押す
［画面・出力］
DFS000I DATABASE DBD036 ACCESS UPDATES ALLOWED AFTER RELOAD
画面・出力には DFS000I が含まれ、DFS000Iを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の DFSURGU0 が画面・出力に表示されること
② ステップ2 の DFSURGL0 が画面・出力に表示されること
③ ステップ3 の DFS000I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0221"><h3>DBD catalog reference ログ照合 詳細表示</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 中級</p><p>IMS 15.5 の 障害診断 で扱う「DBD catalog reference ログ照合 詳細表示」は、IMS管理ACB環境でDBRCがIMSカタログ上のアクティブDBDを参照する仕組みをログ照合の観点で確認する技術項目です。DFS680I 行とAREA8を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ODBM接続状態の誤読を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD catalog reference ログ照合 詳細表示</strong></p><p>検証目的: 障害診断におけるDBD catalog referenceのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA8</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
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


<section class="kb-item" id="c16-i0222"><h3>DBD catalog reference 再始動確認 設定値</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 初級</p><p>IMS 15.5 の 障害診断 で扱う「DBD catalog reference 再始動確認 設定値」は、IMS管理ACB環境でDBRCがIMSカタログ上のアクティブDBDを参照する仕組みを再始動確認の観点で確認する技術項目です。DFS680I 行とAREA4を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、再始動点の誤認を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DBD catalog reference 再始動確認 設定値</strong></p><p>検証目的: 障害診断におけるDBD catalog referenceの再始動確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=AREA4</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
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


<section class="kb-item" id="c16-i0223"><h3>DFS680I ログ照合 メッセージ行</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 中級</p><p>IMS 15.5 の 障害診断 で扱う「DFS680I ログ照合 メッセージ行」は、再始動で使用するチェックポイントを示すIMSメッセージをログ照合の観点で確認する技術項目です。DFS680I 行とRECON3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、ユーティリティ世代の不一致を名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS680I ログ照合 メッセージ行</strong></p><p>検証目的: 障害診断におけるDFS680Iのログ照合を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON3</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO024&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM4&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、ユーティリティ世代の不一致を避けるため対象の現在値を固定する。
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


<section class="kb-item" id="c16-i0224"><h3>DFS680I 整合確認 停止確認</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>IMS 15.5 の 障害診断 で扱う「DFS680I 整合確認 停止確認」は、再始動で使用するチェックポイントを示すIMSメッセージを整合確認の観点で確認する技術項目です。DFS680I 行とRECON3を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、キュー再構築条件の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFS680I 整合確認 停止確認</strong></p><p>検証目的: 障害診断におけるDFS680Iの整合確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=RECON3</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QUERY IMSCON TYPE(ODBM) SHOW(ALIAS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;HWS1&quot;&gt;&lt;typ&gt;IMSCON&lt;/typ&gt;&lt;alias&gt;IO084&lt;/alias&gt;&lt;astt&gt;ACTIVE&lt;/astt&gt;&lt;odbm&gt;ODBM4&lt;/odbm&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、キュー再構築条件の見落としを避けるため対象の現在値を固定する。
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


<section class="kb-item" id="c16-i0225"><h3>DFSURDB0 実行条件確認 統計値</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 中級</p><p>IMS 15.5 の 障害診断 で扱う「DFSURDB0 実行条件確認 統計値」は、イメージコピーと変更累積、ログを使ってDBDSを復旧するIMSユーティリティを実行条件確認の観点で確認する技術項目です。DFS680I 行とUTIL048を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、DBRC登録状態の取り違えを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSURDB0 実行条件確認 統計値</strong></p><p>検証目的: 障害診断におけるDFSURDB0の実行条件確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=UTIL048</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; BROWSE IMS.BMP.CNTL(PSB048)
→ Enter を押す
［画面・出力］
EXEC PGM=DFSRRC00,PARM=&#x27;BMP,PGM048,PSB048,CKPTID=LAST&#x27;
画面・出力には EXEC が含まれ、EXECを確認し、DBRC登録状態の取り違えを避けるため対象の現在値を固定する。
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
CHKPT ID 82170/085236 FOUND FOR PSB048
画面・出力には CHKPT が含まれ、CHKPTを残し、同じ手順を再実行したときの照合点にする。
――――</pre><p>合格条件: ① ステップ1 の EXEC が画面・出力に表示されること
② ステップ2 の IMSLOGR が画面・出力に表示されること
③ ステップ3 の CHKPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p></div></details></section>


<section class="kb-item" id="c16-i0226"><h3>MINVERS 状態確認 整合確認</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 中級</p><p>IMS 15.5 の 障害診断 で扱う「MINVERS 状態確認 整合確認」は、RECONデータセットで下位版戻し時のアクセス可否に影響する最小版数値を状態確認の観点で確認する技術項目です。DFS680I 行とPAY060を同じ運用記録へ残し、コマンド応答、DBRC/RECON情報、ログまたはユーティリティ出力の対応を見比べることで、HALDB索引整合の見落としを名前だけの判断にしないようにします。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Application_Programming / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MINVERS 状態確認 整合確認</strong></p><p>検証目的: 障害診断におけるMINVERSの状態確認を机上確認する。</p><p>前提条件: IMS 15.5 の操作権限、対象サブシステム、DBRC/RECONまたは該当JCLを確認済み。対象=PAY060</p><p>セッション環境: IMS terminal / TSO SPOC / JCL review</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、対象状態を確認し、IMSコマンドまたはJCLを投入する。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY TRAN NAME(PAY060) SHOW(ALL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;styp&gt;DBDC&lt;/styp&gt;&lt;tran&gt;PAY060&lt;/tran&gt;&lt;status&gt;STARTED&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力には name= が含まれ、name=を確認し、HALDB索引整合の見落としを避けるため対象の現在値を固定する。
――――
■ ステップ 2
現在の画面はIMS 15.5の確認画面です。入力口に対象操作を入れ、再始動、DBRC、接続、またはユーティリティの詳細出力を読む。
［操作（入力）］
IMS操作画面
COMMAND ===&gt; QRY DB NAME(DBD060) SHOW(GLOBAL)
→ Enter を押す
［画面・出力］
&lt;mbr name=&quot;IMS1&quot;&gt;&lt;db&gt;DBD060&lt;/db&gt;&lt;scope&gt;GLOBAL&lt;/scope&gt;&lt;status&gt;AVAILABLE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
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


<section class="kb-item" id="c16-i0227"><h3>障害診断 IMSメッセージ診断 ログとの照合 DIAG07</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>ログとの照合では 障害診断 の メンバー照会 を主操作として DIAG07 を判定します。時刻と対象識別子への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG07 に残します。ログとの照合を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG07 へ保存します。主判定のログとの照合では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG07 へ残します。証跡照合のログとの照合では障害診断・メッセージ診断の status と HWSQ2240W を DIAG07 に保存します。記録対応のログとの照合では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG07 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で 障害診断 の メンバー照会 と IMS Connect警告 を使い 操作とログを対応 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読み対象 DIAG07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. statusを含むメンバー照会の応答行を保存する。その応答を得るためQUERY MEMBER TYPE(IMS) SHOW(STATUS)を使用する。対象DIAG07のメッセージIDと理由コードとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。DFS680Iをstatusと同じ判定値とみなし対象DIAG07の主証跡にする。</li><li>C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。</li><li>D. IMSメッセージ診断の停止または再定義を実施する。その後にQUERY MEMBER TYPE(IMS) SHOW(STATUS)でstatusを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: Aはメンバー照会で status を読みメッセージIDと理由コードの主値として操作とログを対応しDIAG07に残します。
機能の仕組み: ログとの照合ではIMS Connect警告を補助操作としIMSメッセージ診断の時刻と対象識別子をHWSQ2240Wと対象DIAG07で照合します。
各候補の評価: メンバー照会とIMS Connect警告の役割を分けるとA: statusの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではメッセージIDと理由コードを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではメッセージIDと理由コードを証明できない点でメッセージIDと理由コードを確認できません、D: 変更前のメッセージIDと理由コードを失う点でIMS Connect警告の範囲を越えます。結論としてログとの照合の障害診断・メッセージ診断で判定する対象は DIAG07 です。
用語の定義: ログとの照合で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG07へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 ログとの照合 DIAG07</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について操作とログを対応し、DIAG07のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG07のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG07のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG07
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG07の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の HWSQ2240W が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0228"><h3>障害診断 IMSメッセージ診断 代替経路の確認 DIAG10</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>代替経路の確認では 障害診断 の メンバー照会 を主操作として DIAG10 を判定します。主経路との役割差への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG10 に残します。代替経路の確認を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG10 へ保存します。主判定の代替経路の確認では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG10 へ残します。証跡照合の代替経路の確認では障害診断・メッセージ診断の status と HWSQ2240W を DIAG10 に保存します。記録対応の代替経路の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG10 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で 障害診断 の メンバー照会 と IMS Connect警告 を照合し 主経路との役割差 を確かめます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読む前に対象 DIAG10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。</li><li>B. IMSメッセージ診断の停止または再定義を実施する。その後にQUERY MEMBER TYPE(IMS) SHOW(STATUS)でstatusを採取する。</li><li>C. DB/DC運用のSTATUSとQUEUEを確認する。その値を障害診断のDIAG10にも適用する。</li><li>D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)とF HWS1,VIEWPORT ALLの対象名をそろえる。前者のstatusをメッセージIDと理由コードの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: Dはメンバー照会で status を読みメッセージIDと理由コードの主値として代替手段の成立を確認しDIAG10に残します。
運用上の背景: 代替経路の確認ではIMS Connect警告を補助操作としIMSメッセージ診断の主経路との役割差をHWSQ2240Wと対象DIAG10で照合します。
候補別の検討: メンバー照会とIMS Connect警告の役割を分けるとA: 入力記録だけではメッセージIDと理由コードを証明できない点で一次資料と一致しません、B: 変更前のメッセージIDと理由コードを失う点でメッセージIDと理由コードを確認できません、C: DB/DC運用の値ではstatusを確認できない点でIMS Connect警告の範囲を越えます、D: 同じ対象名のstatusを採用する点で現在値を示します。結論として代替経路の確認の障害診断・メッセージ診断で判定する対象は DIAG10 です。
重要用語の定義: 代替経路の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG10へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 代替経路の確認 DIAG10</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について代替手段の成立を確認し、DIAG10のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG10のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG10のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG10
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG10の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の HWSQ2240W が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0229"><h3>障害診断 IMSメッセージ診断 変更前の確認 DIAG02</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>変更前の確認では 障害診断 の IMS Connect警告 を主操作として DIAG02 を判定します。変更対象と非対象の境界への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG02 に残します。変更前の確認を補助する 再始動メッセージ では DFS680I を補助値として DIAG02 へ保存します。主判定の変更前の確認では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG02 へ残します。証跡照合の変更前の確認では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG02 に保存します。記録対応の変更前の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG02 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で 障害診断 の IMS Connect警告 と 再始動メッセージ を実施し IMSメッセージ診断 の役割を確認します。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. F HWS1,VIEWPORT ALLを対象名なしで実行する。一覧の先頭行をDIAG02の結果として記録する。</li><li>B. 前回保存したF HWS1,VIEWPORT ALLの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのDIAG02の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象DIAG02についてF HWS1,VIEWPORT ALLの応答からHWSQ2240Wを確認する。/DISPLAY OLDSは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用理由: DはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として変更前の証跡を保存しDIAG02に残します。
動作の背景: 変更前の確認では再始動メッセージを補助操作としIMSメッセージ診断の変更対象と非対象の境界をDFS680Iと対象DIAG02で照合します。
各選択肢の検討: IMS Connect警告と再始動メッセージの役割を分けるとA: 先頭行はDIAG02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でIMS Connect警告を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で障害診断に使いません、D: HWSQ2240Wと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の障害診断・メッセージ診断で判定する対象は DIAG02 です。
初出用語の定義: 変更前の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG02へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 変更前の確認 DIAG02</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について変更前の証跡を保存し、DIAG02のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG02のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG02
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG02の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG02のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0230"><h3>障害診断 IMSメッセージ診断 変更後の確認 DIAG03</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>変更後の確認では 障害診断 の 再始動メッセージ を主操作として DIAG03 を判定します。反映値と残存値への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG03 に残します。変更後の確認を補助する メンバー照会 では status を補助値として DIAG03 へ保存します。主判定の変更後の確認では障害診断・メッセージ診断の 再始動メッセージ から DFS680I を読み DIAG03 へ残します。証跡照合の変更後の確認では障害診断・メッセージ診断の DFS680I と status を DIAG03 に保存します。記録対応の変更後の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG03 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で 障害診断 の 再始動メッセージ と メンバー照会 を用い 変更結果を検証 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。DFS680I で対象 DIAG03 の メッセージIDと理由コード を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)で周辺状態を押さえる。その後に/DISPLAY OLDSでDFS680Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. IMSメッセージ診断の停止または再定義を実施する。その後に/DISPLAY OLDSでDFS680Iを採取する。</li><li>C. HALDBの区画状態とILDS整合を確認する。その値を障害診断のDIAG03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IMSメッセージ診断の反映値と残存値は確認済みとして扱う。さらにF HWS1,VIEWPORT ALLのHWSQ2240WをDFS680Iと同種の値として併記する。</li><li>D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が成功したため/DISPLAY OLDSのDFS680Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答の根拠: Aは再始動メッセージで DFS680I を読みメッセージIDと理由コードの主値として変更結果を検証しDIAG03に残します。
内部の仕組み: 変更後の確認ではメンバー照会を補助操作としIMSメッセージ診断の反映値と残存値をstatusと対象DIAG03で照合します。
誤答を含む比較: 再始動メッセージとメンバー照会の役割を分けるとA: 周辺状態の後にDFS680Iを確認する点でDIAG03を判定できます、B: 変更前のメッセージIDと理由コードを失う点でメンバー照会の範囲を越えます、C: HALDBの値ではDFS680Iを確認できないうえに追加前提も不正な点でDIAG03の値を示しません、D: 補助操作の成功ではDFS680Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の障害診断・メッセージ診断で判定する対象は DIAG03 です。
用語定義: 変更後の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG03へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 変更後の確認 DIAG03</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について変更結果を検証し、DIAG03のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG03の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG03のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG03のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG03
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の HWSQ2240W が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0231"><h3>障害診断 IMSメッセージ診断 引継ぎ記録 DIAG09</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>引継ぎ記録では 障害診断 の 再始動メッセージ を主操作として DIAG09 を判定します。次担当者が追跡できる証跡への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG09 に残します。引継ぎ記録を補助する メンバー照会 では status を補助値として DIAG09 へ保存します。主判定の引継ぎ記録では障害診断・メッセージ診断の 再始動メッセージ から DFS680I を読み DIAG09 へ残します。証跡照合の引継ぎ記録では障害診断・メッセージ診断の DFS680I と status を DIAG09 に保存します。記録対応の引継ぎ記録では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG09 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で 障害診断 の 再始動メッセージ と メンバー照会 を用い 再現可能な記録を作成 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。DFS680I で対象 DIAG09 の メッセージIDと理由コード を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が成功したため/DISPLAY OLDSのDFS680Iも正常だと推定する。主出力は保存しない。</li><li>B. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をDIAG09の結果として記録する。</li><li>C. 対象名DIAG09を指定して/DISPLAY OLDSを実行する。応答中のDFS680Iと時刻を保存する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存した/DISPLAY OLDSの結果を使う。今回のQUERY MEMBER TYPE(IMS) SHOW(STATUS)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: Cは再始動メッセージで DFS680I を読みメッセージIDと理由コードの主値として再現可能な記録を作成しDIAG09に残します。
製品内の仕組み: 引継ぎ記録ではメンバー照会を補助操作としIMSメッセージ診断の次担当者が追跡できる証跡をstatusと対象DIAG09で照合します。
選択肢別の説明: 再始動メッセージとメンバー照会の役割を分けるとA: 補助操作の成功ではDFS680Iを確定できない点でDIAG09の値を示しません、B: 先頭行はDIAG09と確定できない点で引継ぎ記録に合いません、C: DFS680Iと時刻を保存する点で再始動メッセージに合います、D: 採取時刻が異なる点で障害診断に使いません。結論として引継ぎ記録の障害診断・メッセージ診断で判定する対象は DIAG09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG09へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 引継ぎ記録 DIAG09</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について再現可能な記録を作成し、DIAG09のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG09の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG09のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG09のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG09
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の HWSQ2240W が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0232"><h3>障害診断 IMSメッセージ診断 復旧後の確認 DIAG06</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>復旧後の確認では 障害診断 の 再始動メッセージ を主操作として DIAG06 を判定します。再発していないことを示す値への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG06 に残します。復旧後の確認を補助する メンバー照会 では status を補助値として DIAG06 へ保存します。主判定の復旧後の確認では障害診断・メッセージ診断の 再始動メッセージ から DFS680I を読み DIAG06 へ残します。証跡照合の復旧後の確認では障害診断・メッセージ診断の DFS680I と status を DIAG06 に保存します。記録対応の復旧後の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG06 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で 障害診断 の 再始動メッセージ と メンバー照会 の役割を分け 再発していないことを示す値 を調べます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. ODBM/OMのALIASと到達状態を確認する。その値を障害診断のDIAG06にも適用する。</li><li>B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が成功したため/DISPLAY OLDSのDFS680Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象DIAG06へ引き継げるものとする。</li><li>C. /DISPLAY OLDSを対象名なしで実行する。一覧の先頭行をDIAG06の結果として記録する。</li><li>D. /DISPLAY OLDSでDFS680Iを取得してからF HWS1,VIEWPORT ALLでHWSQ2240Wを照合する。DIAG06のメッセージIDと理由コードを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答内容: Dは再始動メッセージで DFS680I を読みメッセージIDと理由コードの主値として復旧後の安定性を確認しDIAG06に残します。
構成上の背景: 復旧後の確認ではメンバー照会を補助操作としIMSメッセージ診断の再発していないことを示す値をstatusと対象DIAG06で照合します。
候補ごとの理由: 再始動メッセージとメンバー照会の役割を分けるとA: ODBM/OMの値ではDFS680Iを確認できない点でメンバー照会の範囲を越えます、B: 補助操作の成功ではDFS680Iを確定できないうえに追加前提も不正な点でDIAG06の値を示しません、C: 先頭行はDIAG06と確定できない点で復旧後の確認に合いません、D: DFS680IとHWSQ2240Wを順に照合する点で再始動メッセージに合います。結論として復旧後の確認の障害診断・メッセージ診断で判定する対象は DIAG06 です。
初出用語: 復旧後の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG06へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 復旧後の確認 DIAG06</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について復旧後の安定性を確認し、DIAG06のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG06の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG06のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG06のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG06
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DFS680I が画面・出力に表示されること
② ステップ2 の status が画面・出力に表示されること
③ ステップ3 の HWSQ2240W が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0233"><h3>障害診断 IMSメッセージ診断 復旧準備 DIAG05</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>復旧準備では 障害診断 の IMS Connect警告 を主操作として DIAG05 を判定します。再開前に必要な整合性への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG05 に残します。復旧準備を補助する 再始動メッセージ では DFS680I を補助値として DIAG05 へ保存します。主判定の復旧準備では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG05 へ残します。証跡照合の復旧準備では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG05 に保存します。記録対応の復旧準備では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG05 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で 障害診断 の IMS Connect警告 と 再始動メッセージ を組み合わせる際は IMSメッセージ診断 がDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用という仕組みを前提にします。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。HWSQ2240W と メッセージIDと理由コード を対象 DIAG05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 前回保存したF HWS1,VIEWPORT ALLの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのDIAG05の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。</li><li>C. 変更を加えずF HWS1,VIEWPORT ALLを実行する。HWSQ2240Wを保存する。差分は/DISPLAY OLDSの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. /DISPLAY OLDSのDFS680IをメッセージIDと理由コードの主判定に採用する。F HWS1,VIEWPORT ALLの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 選定理由: CはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として復旧条件を確認しDIAG05に残します。
処理の仕組み: 復旧準備では再始動メッセージを補助操作としIMSメッセージ診断の再開前に必要な整合性をDFS680Iと対象DIAG05で照合します。
選択結果の内訳: IMS Connect警告と再始動メッセージの役割を分けるとA: 採取時刻が異なる点でIMS Connect警告を代替しません、B: 過去出力では今回の復旧準備を示せない点で障害診断に使いません、C: 変更前のHWSQ2240Wを保存する点で正答です、D: DFS680IはHWSQ2240Wを代替しないうえに追加前提も不正な点でDIAG05を採用できません。結論として復旧準備の障害診断・メッセージ診断で判定する対象は DIAG05 です。
用語の説明: 復旧準備で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG05へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 復旧準備 DIAG05</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について復旧条件を確認し、DIAG05のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG05のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG05
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG05の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG05のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0234"><h3>障害診断 IMSメッセージ診断 構成監査 DIAG08</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>構成監査では 障害診断 の IMS Connect警告 を主操作として DIAG08 を判定します。定義値と稼働値の一致への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG08 に残します。構成監査を補助する 再始動メッセージ では DFS680I を補助値として DIAG08 へ保存します。主判定の構成監査では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG08 へ残します。証跡照合の構成監査では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG08 に保存します。記録対応の構成監査では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG08 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で 障害診断 の IMS Connect警告 と 再始動メッセージ を実施し IMSメッセージ診断 の役割を確認します。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのDIAG08の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。</li><li>B. /DISPLAY OLDSの結果だけでは確定しない。F HWS1,VIEWPORT ALLのHWSQ2240Wを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY OLDSのDFS680IをメッセージIDと理由コードの主判定に採用する。F HWS1,VIEWPORT ALLの応答は採取対象から外す。</li><li>D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusをHWSQ2240Wと同義の成功表示として扱う。F HWS1,VIEWPORT ALLは実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: BはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として構成差分を監査しDIAG08に残します。
実行時の背景: 構成監査では再始動メッセージを補助操作としIMSメッセージ診断の定義値と稼働値の一致をDFS680Iと対象DIAG08で照合します。
四つの候補の理由: IMS Connect警告と再始動メッセージの役割を分けるとA: 過去出力では今回の構成監査を示せない点で障害診断に使いません、B: HWSQ2240Wを主証跡として区別する点で正答です、C: DFS680IはHWSQ2240Wを代替しない点でDIAG08を採用できません、D: statusとHWSQ2240Wは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の障害診断・メッセージ診断で判定する対象は DIAG08 です。
初出語定義: 構成監査で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG08へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 構成監査 DIAG08</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について構成差分を監査し、DIAG08のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG08のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG08
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG08の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG08のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
② ステップ2 の DFS680I が画面・出力に表示されること
③ ステップ3 の status が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0235"><h3>障害診断 IMSメッセージ診断 通常状態の確認 DIAG01</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>通常状態の確認では 障害診断 の メンバー照会 を主操作として DIAG01 を判定します。基準値と現在値の差への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG01 に残します。通常状態の確認を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG01 へ保存します。主判定の通常状態の確認では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG01 へ残します。証跡照合の通常状態の確認では障害診断・メッセージ診断の status と HWSQ2240W を DIAG01 に保存します。記録対応の通常状態の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG01 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で 障害診断 の メンバー照会 と IMS Connect警告 を使い 通常状態を確定 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読み対象 DIAG01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. F HWS1,VIEWPORT ALLのHWSQ2240WをメッセージIDと理由コードの主判定に採用する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. /DISPLAY OLDSのDFS680Iをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。</li><li>C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)を先に実行する。対象DIAG01のstatusをメッセージIDと理由コードとして記録する。続いてF HWS1,VIEWPORT ALLで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解の説明: Cはメンバー照会で status を読みメッセージIDと理由コードの主値として通常状態を確定しDIAG01に残します。
背景・仕組み: 通常状態の確認ではIMS Connect警告を補助操作としIMSメッセージ診断の基準値と現在値の差をHWSQ2240Wと対象DIAG01で照合します。
選択肢の理由: メンバー照会とIMS Connect警告の役割を分けるとA: HWSQ2240Wはstatusを代替しないうえに追加前提も不正な点でIMSメッセージ診断に使えません、B: DFS680Iとstatusは確認項目が異なる点でDIAG01を採用できません、C: statusを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではメッセージIDと理由コードを判定できない点で一次資料と一致しません。結論として通常状態の確認の障害診断・メッセージ診断で判定する対象は DIAG01 です。
用語の初出定義: 通常状態の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG01へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 通常状態の確認 DIAG01</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について通常状態を確定し、DIAG01のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG01のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG01のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG01
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG01の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の HWSQ2240W が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


<section class="kb-item" id="c16-i0236"><h3>障害診断 IMSメッセージ診断 障害切り分け DIAG04</h3><p class="kb-meta">分類: 障害診断 ・ 難易度: 上級</p><p>障害切り分けでは 障害診断 の メンバー照会 を主操作として DIAG04 を判定します。最初に失敗した処理への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG04 に残します。障害切り分けを補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG04 へ保存します。主判定の障害切り分けでは障害診断・メッセージ診断の メンバー照会 から status を読み DIAG04 へ残します。証跡照合の障害切り分けでは障害診断・メッセージ診断の status と HWSQ2240W を DIAG04 に保存します。記録対応の障害切り分けでは障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG04 を結びます。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで 障害診断 の メンバー照会 と IMS Connect警告 を照合し 最初に失敗した処理 を確かめます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読む前に対象 DIAG04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY OLDSのDFS680Iをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)の出力でDIAG04とstatusが同じ応答にあることを確認する。メッセージIDと理由コードをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。</li><li>D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい操作の説明: Bはメンバー照会で status を読みメッセージIDと理由コードの主値として障害範囲を限定しDIAG04に残します。
技術的背景: 障害切り分けではIMS Connect警告を補助操作としIMSメッセージ診断の最初に失敗した処理をHWSQ2240Wと対象DIAG04で照合します。
四択の評価: メンバー照会とIMS Connect警告の役割を分けるとA: DFS680Iとstatusは確認項目が異なるうえに追加前提も不正な点でDIAG04を採用できません、B: DIAG04とstatusを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではメッセージIDと理由コードを判定できない点で一次資料と一致しません、D: 入力記録だけではメッセージIDと理由コードを証明できない点でメッセージIDと理由コードを確認できません。結論として障害切り分けの障害診断・メッセージ診断で判定する対象は DIAG04 です。
初出語の意味: 障害切り分けで使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG04へ適用します。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>障害診断 IMSメッセージ診断 障害切り分け DIAG04</strong></p><p>検証目的: 障害診断のIMSメッセージ診断について障害範囲を限定し、DIAG04のメッセージIDと理由コードを実出力で確認する。</p><p>前提条件: IMS 15.5の参照権限を持ち、対象DIAG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IMS 15.5の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG04のメンバー照会を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; QUERY MEMBER TYPE(IMS) SHOW(STATUS)
→ Enter を押す
［画面・出力］
&lt;mbr name=&#x27;IMS1&#x27;&gt;&lt;typ&gt;IMS&lt;/typ&gt;&lt;status&gt;ACTIVE&lt;/status&gt;&lt;rc&gt;00000000&lt;/rc&gt;&lt;/mbr&gt;
画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG04のIMS Connect警告を表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; F HWS1,VIEWPORT ALL
→ Enter を押す
［画面・出力］
HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG04
IMS CONNECT CONTINUES TO RUN
画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG04の再始動メッセージを表示します。
［操作（入力）］
IMS 15.5 操作画面
COMMAND ===&gt; /DISPLAY OLDS
→ Enter を押す
［画面・出力］
DFS058I NRESTART COMMAND IN PROGRESS
DFS680I USING CHKPT 82170/085820
画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の status が画面・出力に表示されること
② ステップ2 の HWSQ2240W が画面・出力に表示されること
③ ステップ3 の DFS680I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages</p></div></details></section>


## 領域


<section class="kb-item" id="c16-i0237"><h3>BMP 領域</h3><p class="kb-meta">分類: 領域 ・ 難易度: 中級</p><p>IMS 15.5 の 領域で扱うBMP 領域は、バッチ処理で IMS データベースやメッセージキューへアクセスする従属領域です。オンライン稼働中のデータと整合させながらバッチ処理できる点が特徴です。排他、チェックポイント、再始動の設計が重要になります</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認の領域で BMP 領域の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. BMP 領域の出力を取らず区切確認の領域の説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. /DISPLAY TRANSACTION OSKB を省略して区切確認の領域の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の領域へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では BMP 領域 は「区切確認の領域に関係する定義値と表示行を照合する区切確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では BMP 領域の属性行と DFS058I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では BMP 領域を IMS 15.5の運用手順で確認し、初出名は区切確認初出です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BMP 領域</strong></p><p>検証目的: 区切確認の領域について、IMS 15.5 の 領域で扱う BMP 領域は、バッチ処理で IMS データベースやメッセージキューへアクセスする従属領域です。オンライン稼働中のデータと整合させながらバッに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、区切確認の領域の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にBMP 領域を指定し、OSKB010010の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND BMP 領域
CASE OSKB010010
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM BMP 領域
CASE OSKB010010
SOURCE IMS 15.5
BMP 領域とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010010を同じ出力で読み、区切確認の領域の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010010
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010010
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010010  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の BMP 領域 と OSKB010010 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0238"><h3>IFP 領域</h3><p class="kb-meta">分類: 領域 ・ 難易度: 上級</p><p>IMS 15.5 の 領域で扱うIFP 領域は、Fast Path 処理向けの IMS 従属領域です。高頻度で短いトランザクションを効率よく処理する用途で使われます。Fast Path データベースやルーティングの設計と合わせて確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認の領域でアイエムエスの運用確認を行います。IFP 領域の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IMS 15.5と無関係な一覧で範囲確認の領域を確認した扱いにする。</li><li>B. DFS058I の有無を確認せず範囲確認の領域を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. IFP 領域の属性行を読まず範囲確認の領域の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では IFP 領域 は「IMS 15.5で IFP 領域の扱いを記録する範囲確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では IFP 領域の表示結果と DFS058I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では IFP 領域の使い方を出典欄から追跡し、資料名は範囲確認資料です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IFP 領域</strong></p><p>検証目的: 範囲確認の領域について、IMS 15.5 の 領域で扱う IFP 領域は、Fast Path 処理向けの IMS 従属領域です。高頻度で短いトランザクションを効率よく処理する用途で使われます。Fasに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、範囲確認の領域の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にIFP 領域を指定し、OSKB010011の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND IFP 領域
CASE OSKB010011
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM IFP 領域
CASE OSKB010011
SOURCE IMS 15.5
IFP 領域とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010011を同じ出力で読み、範囲確認の領域の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010011
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010011
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010011  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の IFP 領域 と OSKB010011 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0239"><h3>MPP 領域</h3><p class="kb-meta">分類: 領域 ・ 難易度: 中級</p><p>IMS 15.5 の 領域で扱うMPP 領域は、メッセージ処理プログラムを実行する IMS の従属領域です。入力メッセージを受けて短時間のトランザクション処理を行う用途に向きます。処理遅延では、スケジューリング、キュー滞留、異常終了の有無を確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認の領域に関係する MPP 領域の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. MPP 領域の名称と担当者名のみを残して条件確認の領域の表示本文を確認対象に含めない。</li><li>C. アイエムエス以外の画面で条件確認の領域を確認し同じ証跡として扱ったことにする。</li><li>D. DFS058I の有無を見ず条件確認の領域の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では MPP 領域 は「MPP 領域の用途をアイエムエスの表示で確認する条件確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IMS 15.5の MPP 領域と DFS058I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では MPP 領域を IMS 15.5で扱う確認対象とし、用語名は条件確認用語です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MPP 領域</strong></p><p>検証目的: 条件確認の領域について、IMS 15.5 の 領域で扱う MPP 領域は、メッセージ処理プログラムを実行する IMS の従属領域です。入力メッセージを受けて短時間のトランザクション処理を行う用途に向に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、条件確認の領域の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄にMPP 領域を指定し、OSKB010009の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND MPP 領域
CASE OSKB010009
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM MPP 領域
CASE OSKB010009
SOURCE IMS 15.5
MPP 領域とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010009を同じ出力で読み、条件確認の領域の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010009
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010009
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010009  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の MPP 領域 と OSKB010009 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>


<section class="kb-item" id="c16-i0240"><h3>制御領域</h3><p class="kb-meta">分類: 領域 ・ 難易度: 初級</p><p>IMS 15.5 の 領域で扱う制御領域は、IMS 全体の制御と共通機能を担う中核のアドレス空間です。従属領域や通信、DBRC などの周辺機能と連携して処理を進めます。起動失敗や停止時は、制御領域のメッセージを最初に確認します</p><p class="kb-src"><strong>出典:</strong> IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認の制御領域に関する制御領域の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. /DISPLAY TRANSACTION OSKB の結果を残さず出力確認の制御領域の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の制御領域の証跡として保存して根拠にする。</li><li>C. 制御領域の変更点を出力本文から切り離して出力確認の制御領域の承認欄のみ残す。</li><li>D. IMS 15.5の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では制御領域は「制御領域の状態と出力メッセージを結び付ける出力確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では制御領域の出力行と DFS058I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では制御領域を IMS 15.5の確認記録に残し、対象名は出力確認対象です。</p><p class="kb-src"><strong>出典:</strong> IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>制御領域</strong></p><p>検証目的: 出力確認の制御領域について、IMS 15.5 の 領域で扱う制御領域は、IMS 全体の制御と共通機能を担う中核のアドレス空間です。従属領域や通信、DBRC などの周辺機能と連携して処理を進めます。起動に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。</p><p>セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===&gt; に /DISPLAY TRANSACTION OSKB を入力し、出力確認の制御領域の確認表示へ進みます。
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
現在の画面はIMS Terminalの表示結果です。FIND欄に制御領域を指定し、OSKB010008の対象行を見つけます。
［操作（入力）］
(IMS Terminal Result)
COMMAND INPUT ===&gt; FIND 制御領域
CASE OSKB010008
→ Enter を押す
［画面・出力］
(IMS Terminal Result)
ITEM 制御領域
CASE OSKB010008
SOURCE IMS 15.5
制御領域とOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010008を同じ出力で読み、出力確認の制御領域の根拠を記録します。
［操作（入力）］
(IMS Terminal Detail)
COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB
CASE OSKB010008
→ Enter を押す
［画面・出力］
IMS COMMAND RESPONSE OSKB010008
/DISPLAY TRANSACTION OSKB
TRAN  OSKB010008  STATUS STARTED  CLASS 1
DFS058I START COMMAND COMPLETED
DFS058IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
② ステップ2 の 制御領域 と OSKB010008 が画面・出力に表示されること
③ ステップ3 の DFS058I と OSKB010008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands</p></div></details></section>
