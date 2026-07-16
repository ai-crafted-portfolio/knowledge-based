---
search:
  exclude: true
---

# IBM Workload Automation — 詳細 (2/2)

[← IBM Workload Automation の概要へ戻る](index.md)


## プロンプトと依存関係


<section class="kb-item" id="c15-i0166"><h3>プロンプトと依存関係 External Dependency and Prompt 復旧後の確認 DEP06</h3><p class="kb-meta">分類: プロンプトと依存関係 ・ 難易度: 中級</p><p>復旧後の確認では プロンプトと依存関係 の 日次計画警告 を主操作として DEP06 を判定します。再発していないことを示す値への注意として「未解決依存を手動完了して必要な先行処理を飛ばす危険があります」を DEP06 に残します。復旧後の確認を補助する 依存表示 では PREDECESSOR を補助値として DEP06 へ保存します。主判定の復旧後の確認ではプロンプトと依存関係の 日次計画警告 から EQQ0546W を読み DEP06 へ残します。証跡照合の復旧後の確認ではプロンプトと依存関係の EQQ0546W と PREDECESSOR を DEP06 に保存します。記録対応の復旧後の確認ではプロンプトと依存関係の PredecessorとResolution の証跡へ DEP06 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で プロンプトと依存関係 の 日次計画警告 と 依存表示 の役割を分け 再発していないことを示す値 を調べます。External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みです。未解決依存を手動完了して必要な先行処理を飛ばす危険があります。対象 DEP06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. WAPL 連携のCommandとReturn Codeを確認する。その値をプロンプトと依存関係のDEP06にも適用する。</li><li>B. SDSF browse SYSPRINT FIND EQQ0546WでEQQ0546Wを取得してからISPF Current Plan PROMPTS APP06でPROMPTを照合する。DEP06のPredecessorとResolutionを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. ISPF Current Plan DEPENDENCIES APP06が成功したためSDSF browse SYSPRINT FIND EQQ0546WのEQQ0546Wも正常だと推定する。主出力は保存しない。別資源で得た状態を対象DEP06へ引き継げるものとする。</li><li>D. SDSF browse SYSPRINT FIND EQQ0546Wを対象名なしで実行する。一覧の先頭行をDEP06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Bは日次計画警告で EQQ0546W を読みPredecessorとResolutionの主値として復旧後の安定性を確認しDEP06に残します。
構成上の背景: 復旧後の確認では依存表示を補助操作としExternal Dependency and Promptの再発していないことを示す値をPREDECESSORと対象DEP06で照合します。
候補ごとの理由: 日次計画警告と依存表示の役割を分けるとA: WAPL 連携の値ではEQQ0546Wを確認できない点で依存表示の範囲を越えます、B: EQQ0546WとPROMPTを順に照合する点で現在値を示します、C: 補助操作の成功ではEQQ0546Wを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はDEP06と確定できない点で日次計画警告を代替しません。結論として復旧後の確認のプロンプトと依存関係で判定する対象は DEP06 です。
初出用語: 復旧後の確認で使う External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みを表しPredecessorとResolutionを判定する際にDEP06へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロンプトと依存関係 External Dependency and Prompt 復旧後の確認 DEP06</strong></p><p>検証目的: プロンプトと依存関係のExternal Dependency and Promptについて復旧後の安定性を確認し、DEP06のPredecessorとResolutionを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象DEP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0546Wを指定し、DEP06の日次計画警告を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0546W
→ Enter を押す
［画面・出力］
EQQ0546W THE PREDECESSOR APPP06 FOR APPLICATION APP06 COULD NOT BE FOUND
画面・出力にあるEQQ0546Wを読み、PredecessorとResolutionと対象DEP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan DEPENDENCIES APP06を指定し、DEP06の依存表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan DEPENDENCIES APP06
→ Enter を押す
［画面・出力］
ADID APP06 OPNO 020 PREDECESSOR APPP06/010 STATUS COMPLETE
画面・出力にあるPREDECESSORを読み、PredecessorとResolutionと対象DEP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan PROMPTS APP06を指定し、DEP06のプロンプト表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan PROMPTS APP06
→ Enter を押す
［画面・出力］
PROMPT ID PR06 TEXT CONFIRM INPUT FILE STATUS ANSWERED BY OPC1
画面・出力にあるPROMPTを読み、PredecessorとResolutionと対象DEP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0546W が画面・出力に表示されること
② ステップ2 の PREDECESSOR が画面・出力に表示されること
③ ステップ3 の PROMPT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0167"><h3>プロンプトと依存関係 External Dependency and Prompt 復旧準備 DEP05</h3><p class="kb-meta">分類: プロンプトと依存関係 ・ 難易度: 中級</p><p>復旧準備では プロンプトと依存関係 の プロンプト表示 を主操作として DEP05 を判定します。再開前に必要な整合性への注意として「未解決依存を手動完了して必要な先行処理を飛ばす危険があります」を DEP05 に残します。復旧準備を補助する 日次計画警告 では EQQ0546W を補助値として DEP05 へ保存します。主判定の復旧準備ではプロンプトと依存関係の プロンプト表示 から PROMPT を読み DEP05 へ残します。証跡照合の復旧準備ではプロンプトと依存関係の PROMPT と EQQ0546W を DEP05 に保存します。記録対応の復旧準備ではプロンプトと依存関係の PredecessorとResolution の証跡へ DEP05 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で プロンプトと依存関係 の プロンプト表示 と 日次計画警告 を組み合わせる際は External Dependency and Prompt が先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みという仕組みを前提にします。未解決依存を手動完了して必要な先行処理を飛ばす危険があります。PROMPT と PredecessorとResolution を対象 DEP05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずISPF Current Plan PROMPTS APP05を実行する。PROMPTを保存する。差分はSDSF browse SYSPRINT FIND EQQ0546Wの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したISPF Current Plan PROMPTS APP05の結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0546Wの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのDEP05の出力を再利用する。今回のISPF Current Plan PROMPTS APP05とSDSF browse SYSPRINT FIND EQQ0546Wは実行済みとして扱う。</li><li>D. SDSF browse SYSPRINT FIND EQQ0546WのEQQ0546WをPredecessorとResolutionの主判定に採用する。ISPF Current Plan PROMPTS APP05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはプロンプト表示で PROMPT を読みPredecessorとResolutionの主値として復旧条件を確認しDEP05に残します。
処理の仕組み: 復旧準備では日次計画警告を補助操作としExternal Dependency and Promptの再開前に必要な整合性をEQQ0546Wと対象DEP05で照合します。
選択結果の内訳: プロンプト表示と日次計画警告の役割を分けるとA: 変更前のPROMPTを保存する点でプロンプト表示に合います、B: 採取時刻が異なる点でプロンプトと依存関係に使いません、C: 過去出力では今回の復旧準備を示せない点でExternal Dependency and Promptに使えません、D: EQQ0546WはPROMPTを代替しないうえに追加前提も不正な点でDEP05を採用できません。結論として復旧準備のプロンプトと依存関係で判定する対象は DEP05 です。
用語の説明: 復旧準備で使う External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みを表しPredecessorとResolutionを判定する際にDEP05へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロンプトと依存関係 External Dependency and Prompt 復旧準備 DEP05</strong></p><p>検証目的: プロンプトと依存関係のExternal Dependency and Promptについて復旧条件を確認し、DEP05のPredecessorとResolutionを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象DEP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan PROMPTS APP05を指定し、DEP05のプロンプト表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan PROMPTS APP05
→ Enter を押す
［画面・出力］
PROMPT ID PR05 TEXT CONFIRM INPUT FILE STATUS ANSWERED BY OPC1
画面・出力にあるPROMPTを読み、PredecessorとResolutionと対象DEP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0546Wを指定し、DEP05の日次計画警告を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0546W
→ Enter を押す
［画面・出力］
EQQ0546W THE PREDECESSOR APPP05 FOR APPLICATION APP05 COULD NOT BE FOUND
画面・出力にあるEQQ0546Wを読み、PredecessorとResolutionと対象DEP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan DEPENDENCIES APP05を指定し、DEP05の依存表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan DEPENDENCIES APP05
→ Enter を押す
［画面・出力］
ADID APP05 OPNO 020 PREDECESSOR APPP05/010 STATUS COMPLETE
画面・出力にあるPREDECESSORを読み、PredecessorとResolutionと対象DEP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PROMPT が画面・出力に表示されること
② ステップ2 の EQQ0546W が画面・出力に表示されること
③ ステップ3 の PREDECESSOR が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0168"><h3>プロンプトと依存関係 External Dependency and Prompt 構成監査 DEP08</h3><p class="kb-meta">分類: プロンプトと依存関係 ・ 難易度: 中級</p><p>構成監査では プロンプトと依存関係 の プロンプト表示 を主操作として DEP08 を判定します。定義値と稼働値の一致への注意として「未解決依存を手動完了して必要な先行処理を飛ばす危険があります」を DEP08 に残します。構成監査を補助する 日次計画警告 では EQQ0546W を補助値として DEP08 へ保存します。主判定の構成監査ではプロンプトと依存関係の プロンプト表示 から PROMPT を読み DEP08 へ残します。証跡照合の構成監査ではプロンプトと依存関係の PROMPT と EQQ0546W を DEP08 に保存します。記録対応の構成監査ではプロンプトと依存関係の PredecessorとResolution の証跡へ DEP08 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で プロンプトと依存関係 の プロンプト表示 と 日次計画警告 を実施し External Dependency and Prompt の役割を確認します。未解決依存を手動完了して必要な先行処理を飛ばす危険があります。対象 DEP08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのDEP08の出力を再利用する。今回のISPF Current Plan PROMPTS APP08とSDSF browse SYSPRINT FIND EQQ0546Wは実行済みとして扱う。</li><li>B. SDSF browse SYSPRINT FIND EQQ0546WのEQQ0546WをPredecessorとResolutionの主判定に採用する。ISPF Current Plan PROMPTS APP08の応答は採取対象から外す。</li><li>C. ISPF Current Plan DEPENDENCIES APP08のPREDECESSORをPROMPTと同義の成功表示として扱う。ISPF Current Plan PROMPTS APP08は実行しない。</li><li>D. SDSF browse SYSPRINT FIND EQQ0546Wの結果だけでは確定しない。ISPF Current Plan PROMPTS APP08のPROMPTを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはプロンプト表示で PROMPT を読みPredecessorとResolutionの主値として構成差分を監査しDEP08に残します。
実行時の背景: 構成監査では日次計画警告を補助操作としExternal Dependency and Promptの定義値と稼働値の一致をEQQ0546Wと対象DEP08で照合します。
四つの候補の理由: プロンプト表示と日次計画警告の役割を分けるとA: 過去出力では今回の構成監査を示せない点でプロンプトと依存関係に使いません、B: EQQ0546WはPROMPTを代替しない点でExternal Dependency and Promptに使えません、C: PREDECESSORとPROMPTは確認項目が異なる点でDEP08を採用できません、D: PROMPTを主証跡として区別する点で主証跡になります。結論として構成監査のプロンプトと依存関係で判定する対象は DEP08 です。
初出語定義: 構成監査で使う External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みを表しPredecessorとResolutionを判定する際にDEP08へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロンプトと依存関係 External Dependency and Prompt 構成監査 DEP08</strong></p><p>検証目的: プロンプトと依存関係のExternal Dependency and Promptについて構成差分を監査し、DEP08のPredecessorとResolutionを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象DEP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan PROMPTS APP08を指定し、DEP08のプロンプト表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan PROMPTS APP08
→ Enter を押す
［画面・出力］
PROMPT ID PR08 TEXT CONFIRM INPUT FILE STATUS ANSWERED BY OPC1
画面・出力にあるPROMPTを読み、PredecessorとResolutionと対象DEP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0546Wを指定し、DEP08の日次計画警告を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0546W
→ Enter を押す
［画面・出力］
EQQ0546W THE PREDECESSOR APPP08 FOR APPLICATION APP08 COULD NOT BE FOUND
画面・出力にあるEQQ0546Wを読み、PredecessorとResolutionと対象DEP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan DEPENDENCIES APP08を指定し、DEP08の依存表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan DEPENDENCIES APP08
→ Enter を押す
［画面・出力］
ADID APP08 OPNO 020 PREDECESSOR APPP08/010 STATUS COMPLETE
画面・出力にあるPREDECESSORを読み、PredecessorとResolutionと対象DEP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PROMPT が画面・出力に表示されること
② ステップ2 の EQQ0546W が画面・出力に表示されること
③ ステップ3 の PREDECESSOR が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0169"><h3>プロンプトと依存関係 External Dependency and Prompt 通常状態の確認 DEP01</h3><p class="kb-meta">分類: プロンプトと依存関係 ・ 難易度: 中級</p><p>通常状態の確認では プロンプトと依存関係 の 依存表示 を主操作として DEP01 を判定します。基準値と現在値の差への注意として「未解決依存を手動完了して必要な先行処理を飛ばす危険があります」を DEP01 に残します。通常状態の確認を補助する プロンプト表示 では PROMPT を補助値として DEP01 へ保存します。主判定の通常状態の確認ではプロンプトと依存関係の 依存表示 から PREDECESSOR を読み DEP01 へ残します。証跡照合の通常状態の確認ではプロンプトと依存関係の PREDECESSOR と PROMPT を DEP01 に保存します。記録対応の通常状態の確認ではプロンプトと依存関係の PredecessorとResolution の証跡へ DEP01 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で プロンプトと依存関係 の 依存表示 と プロンプト表示 を使い 通常状態を確定 します。External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みです。未解決依存を手動完了して必要な先行処理を飛ばす危険があります。PREDECESSOR を読み対象 DEP01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. ISPF Current Plan DEPENDENCIES APP01を先に実行する。対象DEP01のPREDECESSORをPredecessorとResolutionとして記録する。続いてISPF Current Plan PROMPTS APP01で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. ISPF Current Plan PROMPTS APP01のPROMPTをPredecessorとResolutionの主判定に採用する。ISPF Current Plan DEPENDENCIES APP01の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. SDSF browse SYSPRINT FIND EQQ0546WのEQQ0546WをPREDECESSORと同義の成功表示として扱う。ISPF Current Plan DEPENDENCIES APP01は実行しない。</li><li>D. ISPF Current Plan DEPENDENCIES APP01が応答を返した時点で正常とする。応答中のPREDECESSORの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Aは依存表示で PREDECESSOR を読みPredecessorとResolutionの主値として通常状態を確定しDEP01に残します。
背景・仕組み: 通常状態の確認ではプロンプト表示を補助操作としExternal Dependency and Promptの基準値と現在値の差をPROMPTと対象DEP01で照合します。
選択肢の理由: 依存表示とプロンプト表示の役割を分けるとA: PREDECESSORを主値として補助結果と照合する点で正答です、B: PROMPTはPREDECESSORを代替しないうえに追加前提も不正な点でDEP01を採用できません、C: EQQ0546WとPREDECESSORは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではPredecessorとResolutionを判定できない点で一次資料と一致しません。結論として通常状態の確認のプロンプトと依存関係で判定する対象は DEP01 です。
用語の初出定義: 通常状態の確認で使う External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みを表しPredecessorとResolutionを判定する際にDEP01へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロンプトと依存関係 External Dependency and Prompt 通常状態の確認 DEP01</strong></p><p>検証目的: プロンプトと依存関係のExternal Dependency and Promptについて通常状態を確定し、DEP01のPredecessorとResolutionを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象DEP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan DEPENDENCIES APP01を指定し、DEP01の依存表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan DEPENDENCIES APP01
→ Enter を押す
［画面・出力］
ADID APP01 OPNO 020 PREDECESSOR APPP01/010 STATUS COMPLETE
画面・出力にあるPREDECESSORを読み、PredecessorとResolutionと対象DEP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan PROMPTS APP01を指定し、DEP01のプロンプト表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan PROMPTS APP01
→ Enter を押す
［画面・出力］
PROMPT ID PR01 TEXT CONFIRM INPUT FILE STATUS ANSWERED BY OPC1
画面・出力にあるPROMPTを読み、PredecessorとResolutionと対象DEP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0546Wを指定し、DEP01の日次計画警告を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0546W
→ Enter を押す
［画面・出力］
EQQ0546W THE PREDECESSOR APPP01 FOR APPLICATION APP01 COULD NOT BE FOUND
画面・出力にあるEQQ0546Wを読み、PredecessorとResolutionと対象DEP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PREDECESSOR が画面・出力に表示されること
② ステップ2 の PROMPT が画面・出力に表示されること
③ ステップ3 の EQQ0546W が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0170"><h3>プロンプトと依存関係 External Dependency and Prompt 障害切り分け DEP04</h3><p class="kb-meta">分類: プロンプトと依存関係 ・ 難易度: 中級</p><p>障害切り分けでは プロンプトと依存関係 の 依存表示 を主操作として DEP04 を判定します。最初に失敗した処理への注意として「未解決依存を手動完了して必要な先行処理を飛ばす危険があります」を DEP04 に残します。障害切り分けを補助する プロンプト表示 では PROMPT を補助値として DEP04 へ保存します。主判定の障害切り分けではプロンプトと依存関係の 依存表示 から PREDECESSOR を読み DEP04 へ残します。証跡照合の障害切り分けではプロンプトと依存関係の PREDECESSOR と PROMPT を DEP04 に保存します。記録対応の障害切り分けではプロンプトと依存関係の PredecessorとResolution の証跡へ DEP04 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで プロンプトと依存関係 の 依存表示 と プロンプト表示 を照合し 最初に失敗した処理 を確かめます。External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みです。未解決依存を手動完了して必要な先行処理を飛ばす危険があります。PREDECESSOR を読む前に対象 DEP04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse SYSPRINT FIND EQQ0546WのEQQ0546WをPREDECESSORと同義の成功表示として扱う。ISPF Current Plan DEPENDENCIES APP04は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. ISPF Current Plan DEPENDENCIES APP04が応答を返した時点で正常とする。応答中のPREDECESSORの値は記録しない。</li><li>C. ISPF Current Plan DEPENDENCIES APP04のコマンド文字列だけを記録する。PREDECESSORを含む応答行は保存しない。</li><li>D. ISPF Current Plan DEPENDENCIES APP04の出力でDEP04とPREDECESSORが同じ応答にあることを確認する。PredecessorとResolutionをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Dは依存表示で PREDECESSOR を読みPredecessorとResolutionの主値として障害範囲を限定しDEP04に残します。
技術的背景: 障害切り分けではプロンプト表示を補助操作としExternal Dependency and Promptの最初に失敗した処理をPROMPTと対象DEP04で照合します。
四択の評価: 依存表示とプロンプト表示の役割を分けるとA: EQQ0546WとPREDECESSORは確認項目が異なるうえに追加前提も不正な点でDEP04を採用できません、B: 応答の有無だけではPredecessorとResolutionを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではPredecessorとResolutionを証明できない点で一次資料と一致しません、D: DEP04とPREDECESSORを同じ応答で結ぶ点でDEP04を判定できます。結論として障害切り分けのプロンプトと依存関係で判定する対象は DEP04 です。
初出語の意味: 障害切り分けで使う External Dependency and Prompt は先行オカレンス、外部依存、オペレータープロンプトを操作開始条件として管理する仕組みを表しPredecessorとResolutionを判定する際にDEP04へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロンプトと依存関係 External Dependency and Prompt 障害切り分け DEP04</strong></p><p>検証目的: プロンプトと依存関係のExternal Dependency and Promptについて障害範囲を限定し、DEP04のPredecessorとResolutionを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象DEP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan DEPENDENCIES APP04を指定し、DEP04の依存表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan DEPENDENCIES APP04
→ Enter を押す
［画面・出力］
ADID APP04 OPNO 020 PREDECESSOR APPP04/010 STATUS COMPLETE
画面・出力にあるPREDECESSORを読み、PredecessorとResolutionと対象DEP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へISPF Current Plan PROMPTS APP04を指定し、DEP04のプロンプト表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Current Plan PROMPTS APP04
→ Enter を押す
［画面・出力］
PROMPT ID PR04 TEXT CONFIRM INPUT FILE STATUS ANSWERED BY OPC1
画面・出力にあるPROMPTを読み、PredecessorとResolutionと対象DEP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのプロンプトと依存関係を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0546Wを指定し、DEP04の日次計画警告を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0546W
→ Enter を押す
［画面・出力］
EQQ0546W THE PREDECESSOR APPP04 FOR APPLICATION APP04 COULD NOT BE FOUND
画面・出力にあるEQQ0546Wを読み、PredecessorとResolutionと対象DEP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PREDECESSOR が画面・出力に表示されること
② ステップ2 の PROMPT が画面・出力に表示されること
③ ステップ3 の EQQ0546W が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


## レコード


<section class="kb-item" id="c15-i0171"><h3>Current plan special resource segment</h3><p class="kb-meta">分類: レコード ・ 難易度: 上級</p><p>IBM Workload Automation の レコードで扱うCurrent plan special resource segmentは、現在計画内で特殊資源の状態や関連操作を表す内部情報です。資源待ちや排他制御の調査で、どの操作が資源を使っているかを理解する助けになります。通常は直接編集せず、表示や診断の文脈で読みます</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認のレコードに関する Current plan special resの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. SRSTAT の結果を残さず変更確認のレコードの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認のレコードの証跡として保存して根拠にする。</li><li>C. Current plan special resの変更点を出力本文から切り離して変更確認のレコードの承認欄のみ残す。</li><li>D. IBM Workload Automationの表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では Current plan special res は「Current plan special resの状態と出力メッセージを結び付ける変更確認項目」と SRSTAT または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では Current plan special resの出力行と EQQZ045I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では Current plan special resを IBM Workload Automationの確認記録に残し、対象名は変更確認対象です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details></section>


## ワークステーション管理


<section class="kb-item" id="c15-i0172"><h3>WAPL INIT 変更反映 再計画019</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>第十九観点 ワークステーション管理 の 再計画019 では WAPL INIT を点検します。第十九観点 対象は Workload Automation Programming Language がです。第十九観点 操作番号とジョブ名を EQQ028 に結び付け、再表示時の照合点にします。第十九観点 計画反映後は long-term plan との差を IWA計画039で照合します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WAPL INIT 変更反映 再計画019</strong></p><p>検証目的: ワークステーション管理における WAPL INIT の変更反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ028</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、WAPL INIT の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /S EQQTRK
→ Enter を押す
［画面・出力］
EQQFSW1I WRITER TASK INITIALIZED FOR CPU07
EQQMLOG 039 TRACKER START CHECK
画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ028 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQFCC1I
→ Enter を押す
［画面・出力］
EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
TRACKER CPU07 CONNECTED TO CONTROLLER ZWS1
画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQTRK,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
TRACKER CPU07 EVENT QUEUE NORMAL
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0173"><h3>WAPL INIT 状態確認 導入確認079</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>第七十九観点 ワークステーション管理 の 導入確認079 では WAPL INIT を点検します。第七十九観点 対象は Workload Automation Programming Language がです。第七十九観点 操作番号とジョブ名を EQQ088 に結び付け、再表示時の照合点にします。第七十九観点 計画反映後は long-term plan との差を IWA計画099で照合します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WAPL INIT 状態確認 導入確認079</strong></p><p>検証目的: ワークステーション管理における WAPL INIT の状態確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ088</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、WAPL INIT の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /S EQQTRK
→ Enter を押す
［画面・出力］
EQQFSW1I WRITER TASK INITIALIZED FOR CPU07
EQQMLOG 099 TRACKER START CHECK
画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ088 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQFCC1I
→ Enter を押す
［画面・出力］
EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
TRACKER CPU07 CONNECTED TO CONTROLLER ZWS1
画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQTRK,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
TRACKER CPU07 EVENT QUEUE NORMAL
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0174"><h3>WAPL INIT 障害切分け 監視049</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>第四十九観点 WAPL INIT は IBM Workload Automation の ワークステーション管理 で扱う確認点です。第四十九観点 対象は Workload Automation Programming Language がです。第四十九観点 current plan の ADID/IADATE/OPNO と EQQ058 を同じ記録に残し、再実行前の Ready 変更を記録せずに原因追跡できなくなることを管理します。第四十九観点 確認経路は DWC、ISPF、conman、WAPL の別を IWA記録069に残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WAPL INIT 障害切分け 監視049</strong></p><p>検証目的: ワークステーション管理における WAPL INIT の障害切分けを机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ058</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、WAPL INIT の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /S EQQTRK
→ Enter を押す
［画面・出力］
EQQFSW1I WRITER TASK INITIALIZED FOR CPU01
EQQMLOG 069 TRACKER START CHECK
画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ058 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQFCC1I
→ Enter を押す
［画面・出力］
EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
TRACKER CPU01 CONNECTED TO CONTROLLER ZWS1
画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQTRK,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
TRACKER CPU01 EVENT QUEUE NORMAL
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0175"><h3>tracker ログ確認 依存確認064</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>第六十四観点 依存確認064 では ワークステーション管理 にある tracker を扱います。第六十四観点 対象は z/OS 側でジョブ投入、完了、戻りコード、イベントを controller へ通知です。第六十四観点 conman showjobs の Job Stream と Job 状態 を採る時点で CPU04 を明記し、変更反映の前提を守ります。第六十四観点 後続作業では同じ engine と current plan を見たことを IWA監査084で残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tracker ログ確認 依存確認064</strong></p><p>検証目的: ワークステーション管理における tracker のログ確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU04</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、tracker の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL084.IWAJOB084
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL084
Job: IWAJOB084
Workstation: CPU04
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU04 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL084
→ Enter を押す
［画面・出力］
Schedule PAYROLL084 submitted
Instance 2607150900 queued for workstation CPU04
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL084.IWAJOB084
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL084
Job: IWAJOB084
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0176"><h3>tracker 依存関係確認 再実行094</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 上級</p><p>第九十四観点 tracker の 再実行094 は IBM Workload Automation の ワークステーション管理 に属します。第九十四観点 対象は z/OS 側でジョブ投入、完了、戻りコード、イベントを controller へ通知です。第九十四観点 conman または WAPL の結果を使う時は、CPU10 の取得経路を残します。第九十四観点 WAPL を使う場合は subsystem 名を IWA言語114に残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tracker 依存関係確認 再実行094</strong></p><p>検証目的: ワークステーション管理における tracker の依存関係確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU10</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、tracker の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL114.IWAJOB114
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL114
Job: IWAJOB114
Workstation: CPU10
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU10 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL114
→ Enter を押す
［画面・出力］
Schedule PAYROLL114 submitted
Instance 2607150900 queued for workstation CPU10
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL114.IWAJOB114
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL114
Job: IWAJOB114
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0177"><h3>tracker 再実行判断 照合034</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>第三十四観点 tracker の 照合034 は IBM Workload Automation の ワークステーション管理 に属します。第三十四観点 対象は z/OS 側でジョブ投入、完了、戻りコード、イベントを controller へ通知です。第三十四観点 conman または WAPL の結果を使う時は、CPU10 の取得経路を残します。第三十四観点 WAPL を使う場合は subsystem 名を IWA言語054に残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tracker 再実行判断 照合034</strong></p><p>検証目的: ワークステーション管理における tracker の再実行判断を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU10</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、tracker の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL054.IWAJOB054
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL054
Job: IWAJOB054
Workstation: CPU10
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU10 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL054
→ Enter を押す
［画面・出力］
Schedule PAYROLL054 submitted
Instance 2607150900 queued for workstation CPU10
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL054.IWAJOB054
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL054
Job: IWAJOB054
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0178"><h3>tracker 実行監視 ログ採取004</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 初級</p><p>第四観点 ログ採取004 では ワークステーション管理 にある tracker を扱います。第四観点 対象は z/OS 側でジョブ投入、完了、戻りコード、イベントを controller へ通知です。第四観点 conman showjobs の Job Stream と Job 状態 を採る時点で CPU04 を明記し、変更反映の前提を守ります。第四観点 後続作業では同じ engine と current plan を見たことを IWA監査024で残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tracker 実行監視 ログ採取004</strong></p><p>検証目的: ワークステーション管理における tracker の実行監視を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU04</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、tracker の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL024.IWAJOB024
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL024
Job: IWAJOB024
Workstation: CPU04
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU04 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL024
→ Enter を押す
［画面・出力］
Schedule PAYROLL024 submitted
Instance 2607150900 queued for workstation CPU04
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL024.IWAJOB024
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL024
Job: IWAJOB024
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0179"><h3>ワークステーション管理 Workstation Definition ログとの照合 WS07</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>ログとの照合では ワークステーション管理 の ワークステーション表示 を主操作として WS07 を判定します。時刻と対象識別子への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS07 に残します。ログとの照合を補助する 現在計画状態 では PARALLEL を補助値として WS07 へ保存します。主判定のログとの照合ではワークステーション管理の ワークステーション表示 から WORKSTATION を読み WS07 へ残します。証跡照合のログとの照合ではワークステーション管理の WORKSTATION と PARALLEL を WS07 に保存します。記録対応のログとの照合ではワークステーション管理の WSIDとOpen Interval の証跡へ WS07 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で ワークステーション管理 の ワークステーション表示 と 現在計画状態 を組み合わせる際は Workstation Definition が操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素という仕組みを前提にします。削除済みワークステーションを計画内で使い続ける危険があります。WORKSTATION と WSIDとOpen Interval を対象 WS07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. WORKSTATIONを含むワークステーション表示の応答行を保存する。その応答を得るためISPF Workstation Description LIST WS07を使用する。対象WS07のWSIDとOpen Intervalとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. ISPF Workstation Description LIST WS07が応答を返した時点で正常とする。応答中のWORKSTATIONの値は記録しない。EQQ0356EをWORKSTATIONと同じ判定値とみなし対象WS07の主証跡にする。</li><li>C. ISPF Workstation Description LIST WS07のコマンド文字列だけを記録する。WORKSTATIONを含む応答行は保存しない。</li><li>D. Workstation Definitionの停止または再定義を実施する。その後にISPF Workstation Description LIST WS07でWORKSTATIONを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aはワークステーション表示で WORKSTATION を読みWSIDとOpen Intervalの主値として操作とログを対応しWS07に残します。
機能の仕組み: ログとの照合では現在計画状態を補助操作としWorkstation Definitionの時刻と対象識別子をPARALLELと対象WS07で照合します。
各候補の評価: ワークステーション表示と現在計画状態の役割を分けるとA: WORKSTATIONの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではWSIDとOpen Intervalを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではWSIDとOpen Intervalを証明できない点でWSIDとOpen Intervalを確認できません、D: 変更前のWSIDとOpen Intervalを失う点で現在計画状態の範囲を越えます。結論としてログとの照合のワークステーション管理で判定する対象は WS07 です。
用語の定義: ログとの照合で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS07へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition ログとの照合 WS07</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて操作とログを対応し、WS07のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS07を指定し、WS07のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS07
→ Enter を押す
［画面・出力］
WORKSTATION WS07
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS07の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS07 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS07の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS07
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の WORKSTATION が画面・出力に表示されること
② ステップ2 の PARALLEL が画面・出力に表示されること
③ ステップ3 の EQQ0356E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0180"><h3>ワークステーション管理 Workstation Definition 代替経路の確認 WS10</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>代替経路の確認では ワークステーション管理 の ワークステーション表示 を主操作として WS10 を判定します。主経路との役割差への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS10 に残します。代替経路の確認を補助する 現在計画状態 では PARALLEL を補助値として WS10 へ保存します。主判定の代替経路の確認ではワークステーション管理の ワークステーション表示 から WORKSTATION を読み WS10 へ残します。証跡照合の代替経路の確認ではワークステーション管理の WORKSTATION と PARALLEL を WS10 に保存します。記録対応の代替経路の確認ではワークステーション管理の WSIDとOpen Interval の証跡へ WS10 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で ワークステーション管理 の ワークステーション表示 と 現在計画状態 を実施し Workstation Definition の役割を確認します。削除済みワークステーションを計画内で使い続ける危険があります。対象 WS10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. ISPF Workstation Description LIST WS10のコマンド文字列だけを記録する。WORKSTATIONを含む応答行は保存しない。</li><li>B. Workstation Definitionの停止または再定義を実施する。その後にISPF Workstation Description LIST WS10でWORKSTATIONを採取する。</li><li>C. ISPF パネル運用のPanel IDとOptionを確認する。その値をワークステーション管理のWS10にも適用する。</li><li>D. ISPF Workstation Description LIST WS10とISPF EQQMTOPP option 5 WORK STATIONSの対象名をそろえる。前者のWORKSTATIONをWSIDとOpen Intervalの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dはワークステーション表示で WORKSTATION を読みWSIDとOpen Intervalの主値として代替手段の成立を確認しWS10に残します。
運用上の背景: 代替経路の確認では現在計画状態を補助操作としWorkstation Definitionの主経路との役割差をPARALLELと対象WS10で照合します。
候補別の検討: ワークステーション表示と現在計画状態の役割を分けるとA: 入力記録だけではWSIDとOpen Intervalを証明できない点で一次資料と一致しません、B: 変更前のWSIDとOpen Intervalを失う点でWSIDとOpen Intervalを確認できません、C: ISPF パネル運用の値ではWORKSTATIONを確認できない点で現在計画状態の範囲を越えます、D: 同じ対象名のWORKSTATIONを採用する点で現在値を示します。結論として代替経路の確認のワークステーション管理で判定する対象は WS10 です。
重要用語の定義: 代替経路の確認で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS10へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 代替経路の確認 WS10</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて代替手段の成立を確認し、WS10のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS10を指定し、WS10のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS10
→ Enter を押す
［画面・出力］
WORKSTATION WS10
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS10の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS10 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS10の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS10
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の WORKSTATION が画面・出力に表示されること
② ステップ2 の PARALLEL が画面・出力に表示されること
③ ステップ3 の EQQ0356E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0181"><h3>ワークステーション管理 Workstation Definition 変更前の確認 WS02</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>変更前の確認では ワークステーション管理 の 現在計画状態 を主操作として WS02 を判定します。変更対象と非対象の境界への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS02 に残します。変更前の確認を補助する 定義不整合 では EQQ0356E を補助値として WS02 へ保存します。主判定の変更前の確認ではワークステーション管理の 現在計画状態 から PARALLEL を読み WS02 へ残します。証跡照合の変更前の確認ではワークステーション管理の PARALLEL と EQQ0356E を WS02 に保存します。記録対応の変更前の確認ではワークステーション管理の WSIDとOpen Interval の証跡へ WS02 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で ワークステーション管理 の 現在計画状態 と 定義不整合 の役割を分け 変更対象と非対象の境界 を調べます。Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素です。削除済みワークステーションを計画内で使い続ける危険があります。対象 WS02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 5 WORK STATIONSを対象名なしで実行する。一覧の先頭行をWS02の結果として記録する。</li><li>B. 前回保存したISPF EQQMTOPP option 5 WORK STATIONSの結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0356Eの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのWS02の出力を再利用する。今回のISPF EQQMTOPP option 5 WORK STATIONSとSDSF browse SYSPRINT FIND EQQ0356Eは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象WS02についてISPF EQQMTOPP option 5 WORK STATIONSの応答からPARALLELを確認する。SDSF browse SYSPRINT FIND EQQ0356Eは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは現在計画状態で PARALLEL を読みWSIDとOpen Intervalの主値として変更前の証跡を保存しWS02に残します。
動作の背景: 変更前の確認では定義不整合を補助操作としWorkstation Definitionの変更対象と非対象の境界をEQQ0356Eと対象WS02で照合します。
各選択肢の検討: 現在計画状態と定義不整合の役割を分けるとA: 先頭行はWS02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で現在計画状態を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でワークステーション管理に使いません、D: PARALLELと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のワークステーション管理で判定する対象は WS02 です。
初出用語の定義: 変更前の確認で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS02へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 変更前の確認 WS02</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて変更前の証跡を保存し、WS02のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS02の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS02 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS02の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS02
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS02を指定し、WS02のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS02
→ Enter を押す
［画面・出力］
WORKSTATION WS02
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARALLEL が画面・出力に表示されること
② ステップ2 の EQQ0356E が画面・出力に表示されること
③ ステップ3 の WORKSTATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0182"><h3>ワークステーション管理 Workstation Definition 変更後の確認 WS03</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>変更後の確認では ワークステーション管理 の 定義不整合 を主操作として WS03 を判定します。反映値と残存値への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS03 に残します。変更後の確認を補助する ワークステーション表示 では WORKSTATION を補助値として WS03 へ保存します。主判定の変更後の確認ではワークステーション管理の 定義不整合 から EQQ0356E を読み WS03 へ残します。証跡照合の変更後の確認ではワークステーション管理の EQQ0356E と WORKSTATION を WS03 に保存します。記録対応の変更後の確認ではワークステーション管理の WSIDとOpen Interval の証跡へ WS03 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で ワークステーション管理 の 定義不整合 と ワークステーション表示 を使い 変更結果を検証 します。Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素です。削除済みワークステーションを計画内で使い続ける危険があります。EQQ0356E を読み対象 WS03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. ISPF Workstation Description LIST WS03で周辺状態を押さえる。その後にSDSF browse SYSPRINT FIND EQQ0356EでEQQ0356Eを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. Workstation Definitionの停止または再定義を実施する。その後にSDSF browse SYSPRINT FIND EQQ0356EでEQQ0356Eを採取する。</li><li>C. ワークステーション管理のWSIDとOpen Intervalを確認する。その値をワークステーション管理のWS03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Workstation Definitionの反映値と残存値は確認済みとして扱う。さらにISPF EQQMTOPP option 5 WORK STATIONSのPARALLELをEQQ0356Eと同種の値として併記する。</li><li>D. ISPF Workstation Description LIST WS03が成功したためSDSF browse SYSPRINT FIND EQQ0356EのEQQ0356Eも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aは定義不整合で EQQ0356E を読みWSIDとOpen Intervalの主値として変更結果を検証しWS03に残します。
内部の仕組み: 変更後の確認ではワークステーション表示を補助操作としWorkstation Definitionの反映値と残存値をWORKSTATIONと対象WS03で照合します。
誤答を含む比較: 定義不整合とワークステーション表示の役割を分けるとA: 周辺状態の後にEQQ0356Eを確認する点でWS03を判定できます、B: 変更前のWSIDとOpen Intervalを失う点でワークステーション表示の範囲を越えます、C: ワークステーション管理の値ではEQQ0356Eを確認できないうえに追加前提も不正な点でWS03の値を示しません、D: 補助操作の成功ではEQQ0356Eを確定できない点で変更後の確認に合いません。結論として変更後の確認のワークステーション管理で判定する対象は WS03 です。
用語定義: 変更後の確認で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS03へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 変更後の確認 WS03</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて変更結果を検証し、WS03のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS03の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS03
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS03を指定し、WS03のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS03
→ Enter を押す
［画面・出力］
WORKSTATION WS03
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS03の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS03 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0356E が画面・出力に表示されること
② ステップ2 の WORKSTATION が画面・出力に表示されること
③ ステップ3 の PARALLEL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0183"><h3>ワークステーション管理 Workstation Definition 引継ぎ記録 WS09</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>引継ぎ記録では ワークステーション管理 の 定義不整合 を主操作として WS09 を判定します。次担当者が追跡できる証跡への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS09 に残します。引継ぎ記録を補助する ワークステーション表示 では WORKSTATION を補助値として WS09 へ保存します。主判定の引継ぎ記録ではワークステーション管理の 定義不整合 から EQQ0356E を読み WS09 へ残します。証跡照合の引継ぎ記録ではワークステーション管理の EQQ0356E と WORKSTATION を WS09 に保存します。記録対応の引継ぎ記録ではワークステーション管理の WSIDとOpen Interval の証跡へ WS09 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で ワークステーション管理 の 定義不整合 と ワークステーション表示 を使い 再現可能な記録を作成 します。Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素です。削除済みワークステーションを計画内で使い続ける危険があります。EQQ0356E を読み対象 WS09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. ISPF Workstation Description LIST WS09が成功したためSDSF browse SYSPRINT FIND EQQ0356EのEQQ0356Eも正常だと推定する。主出力は保存しない。</li><li>B. SDSF browse SYSPRINT FIND EQQ0356Eを対象名なしで実行する。一覧の先頭行をWS09の結果として記録する。</li><li>C. 対象名WS09を指定してSDSF browse SYSPRINT FIND EQQ0356Eを実行する。応答中のEQQ0356Eと時刻を保存する。ISPF Workstation Description LIST WS09で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSDSF browse SYSPRINT FIND EQQ0356Eの結果を使う。今回のISPF Workstation Description LIST WS09の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cは定義不整合で EQQ0356E を読みWSIDとOpen Intervalの主値として再現可能な記録を作成しWS09に残します。
製品内の仕組み: 引継ぎ記録ではワークステーション表示を補助操作としWorkstation Definitionの次担当者が追跡できる証跡をWORKSTATIONと対象WS09で照合します。
選択肢別の説明: 定義不整合とワークステーション表示の役割を分けるとA: 補助操作の成功ではEQQ0356Eを確定できない点でWS09の値を示しません、B: 先頭行はWS09と確定できない点で引継ぎ記録に合いません、C: EQQ0356Eと時刻を保存する点で定義不整合に合います、D: 採取時刻が異なる点でワークステーション管理に使いません。結論として引継ぎ記録のワークステーション管理で判定する対象は WS09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS09へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 引継ぎ記録 WS09</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて再現可能な記録を作成し、WS09のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS09の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS09
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS09を指定し、WS09のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS09
→ Enter を押す
［画面・出力］
WORKSTATION WS09
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS09の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS09 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0356E が画面・出力に表示されること
② ステップ2 の WORKSTATION が画面・出力に表示されること
③ ステップ3 の PARALLEL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0184"><h3>ワークステーション管理 Workstation Definition 復旧後の確認 WS06</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>復旧後の確認では ワークステーション管理 の 定義不整合 を主操作として WS06 を判定します。再発していないことを示す値への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS06 に残します。復旧後の確認を補助する ワークステーション表示 では WORKSTATION を補助値として WS06 へ保存します。主判定の復旧後の確認ではワークステーション管理の 定義不整合 から EQQ0356E を読み WS06 へ残します。証跡照合の復旧後の確認ではワークステーション管理の EQQ0356E と WORKSTATION を WS06 に保存します。記録対応の復旧後の確認ではワークステーション管理の WSIDとOpen Interval の証跡へ WS06 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で ワークステーション管理 の 定義不整合 と ワークステーション表示 を照合し 再発していないことを示す値 を確かめます。Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素です。削除済みワークステーションを計画内で使い続ける危険があります。EQQ0356E を読む前に対象 WS06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. ジョブ監視のStatusとJob IDを確認する。その値をワークステーション管理のWS06にも適用する。</li><li>B. ISPF Workstation Description LIST WS06が成功したためSDSF browse SYSPRINT FIND EQQ0356EのEQQ0356Eも正常だと推定する。主出力は保存しない。別資源で得た状態を対象WS06へ引き継げるものとする。Workstation Definitionの再発していないことを示す値は確認済みとして扱う。さらにISPF EQQMTOPP option 5 WORK STATIONSのPARALLELをEQQ0356Eと同種の値として併記する。</li><li>C. SDSF browse SYSPRINT FIND EQQ0356Eを対象名なしで実行する。一覧の先頭行をWS06の結果として記録する。</li><li>D. SDSF browse SYSPRINT FIND EQQ0356EでEQQ0356Eを取得してからISPF EQQMTOPP option 5 WORK STATIONSでPARALLELを照合する。WS06のWSIDとOpen Intervalを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dは定義不整合で EQQ0356E を読みWSIDとOpen Intervalの主値として復旧後の安定性を確認しWS06に残します。
構成上の背景: 復旧後の確認ではワークステーション表示を補助操作としWorkstation Definitionの再発していないことを示す値をWORKSTATIONと対象WS06で照合します。
候補ごとの理由: 定義不整合とワークステーション表示の役割を分けるとA: ジョブ監視の値ではEQQ0356Eを確認できない点でワークステーション表示の範囲を越えます、B: 補助操作の成功ではEQQ0356Eを確定できないうえに追加前提も不正な点でWS06の値を示しません、C: 先頭行はWS06と確定できない点で復旧後の確認に合いません、D: EQQ0356EとPARALLELを順に照合する点で定義不整合に合います。結論として復旧後の確認のワークステーション管理で判定する対象は WS06 です。
初出用語: 復旧後の確認で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS06へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 復旧後の確認 WS06</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて復旧後の安定性を確認し、WS06のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS06の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS06
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS06を指定し、WS06のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS06
→ Enter を押す
［画面・出力］
WORKSTATION WS06
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS06の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS06 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0356E が画面・出力に表示されること
② ステップ2 の WORKSTATION が画面・出力に表示されること
③ ステップ3 の PARALLEL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0185"><h3>ワークステーション管理 Workstation Definition 復旧準備 WS05</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>復旧準備では ワークステーション管理 の 現在計画状態 を主操作として WS05 を判定します。再開前に必要な整合性への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS05 に残します。復旧準備を補助する 定義不整合 では EQQ0356E を補助値として WS05 へ保存します。主判定の復旧準備ではワークステーション管理の 現在計画状態 から PARALLEL を読み WS05 へ残します。証跡照合の復旧準備ではワークステーション管理の PARALLEL と EQQ0356E を WS05 に保存します。記録対応の復旧準備ではワークステーション管理の WSIDとOpen Interval の証跡へ WS05 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で ワークステーション管理 の 現在計画状態 と 定義不整合 を用い 復旧条件を確認 します。Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素です。削除済みワークステーションを計画内で使い続ける危険があります。PARALLEL で対象 WS05 の WSIDとOpen Interval を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したISPF EQQMTOPP option 5 WORK STATIONSの結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0356Eの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのWS05の出力を再利用する。今回のISPF EQQMTOPP option 5 WORK STATIONSとSDSF browse SYSPRINT FIND EQQ0356Eは実行済みとして扱う。</li><li>C. 変更を加えずISPF EQQMTOPP option 5 WORK STATIONSを実行する。PARALLELを保存する。差分はSDSF browse SYSPRINT FIND EQQ0356Eの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SDSF browse SYSPRINT FIND EQQ0356EのEQQ0356EをWSIDとOpen Intervalの主判定に採用する。ISPF EQQMTOPP option 5 WORK STATIONSの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは現在計画状態で PARALLEL を読みWSIDとOpen Intervalの主値として復旧条件を確認しWS05に残します。
処理の仕組み: 復旧準備では定義不整合を補助操作としWorkstation Definitionの再開前に必要な整合性をEQQ0356Eと対象WS05で照合します。
選択結果の内訳: 現在計画状態と定義不整合の役割を分けるとA: 採取時刻が異なる点で現在計画状態を代替しません、B: 過去出力では今回の復旧準備を示せない点でワークステーション管理に使いません、C: 変更前のPARALLELを保存する点で正答です、D: EQQ0356EはPARALLELを代替しないうえに追加前提も不正な点でWS05を採用できません。結論として復旧準備のワークステーション管理で判定する対象は WS05 です。
用語の説明: 復旧準備で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS05へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 復旧準備 WS05</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて復旧条件を確認し、WS05のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS05の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS05 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS05の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS05
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS05を指定し、WS05のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS05
→ Enter を押す
［画面・出力］
WORKSTATION WS05
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARALLEL が画面・出力に表示されること
② ステップ2 の EQQ0356E が画面・出力に表示されること
③ ステップ3 の WORKSTATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0186"><h3>ワークステーション管理 Workstation Definition 構成監査 WS08</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>構成監査では ワークステーション管理 の 現在計画状態 を主操作として WS08 を判定します。定義値と稼働値の一致への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS08 に残します。構成監査を補助する 定義不整合 では EQQ0356E を補助値として WS08 へ保存します。主判定の構成監査ではワークステーション管理の 現在計画状態 から PARALLEL を読み WS08 へ残します。証跡照合の構成監査ではワークステーション管理の PARALLEL と EQQ0356E を WS08 に保存します。記録対応の構成監査ではワークステーション管理の WSIDとOpen Interval の証跡へ WS08 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で ワークステーション管理 の 現在計画状態 と 定義不整合 の役割を分け 定義値と稼働値の一致 を調べます。Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素です。削除済みワークステーションを計画内で使い続ける危険があります。対象 WS08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのWS08の出力を再利用する。今回のISPF EQQMTOPP option 5 WORK STATIONSとSDSF browse SYSPRINT FIND EQQ0356Eは実行済みとして扱う。</li><li>B. SDSF browse SYSPRINT FIND EQQ0356Eの結果だけでは確定しない。ISPF EQQMTOPP option 5 WORK STATIONSのPARALLELを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SDSF browse SYSPRINT FIND EQQ0356EのEQQ0356EをWSIDとOpen Intervalの主判定に採用する。ISPF EQQMTOPP option 5 WORK STATIONSの応答は採取対象から外す。</li><li>D. ISPF Workstation Description LIST WS08のWORKSTATIONをPARALLELと同義の成功表示として扱う。ISPF EQQMTOPP option 5 WORK STATIONSは実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bは現在計画状態で PARALLEL を読みWSIDとOpen Intervalの主値として構成差分を監査しWS08に残します。
実行時の背景: 構成監査では定義不整合を補助操作としWorkstation Definitionの定義値と稼働値の一致をEQQ0356Eと対象WS08で照合します。
四つの候補の理由: 現在計画状態と定義不整合の役割を分けるとA: 過去出力では今回の構成監査を示せない点でワークステーション管理に使いません、B: PARALLELを主証跡として区別する点で正答です、C: EQQ0356EはPARALLELを代替しない点でWS08を採用できません、D: WORKSTATIONとPARALLELは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のワークステーション管理で判定する対象は WS08 です。
初出語定義: 構成監査で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS08へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 構成監査 WS08</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて構成差分を監査し、WS08のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS08の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS08 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS08の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS08
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS08を指定し、WS08のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS08
→ Enter を押す
［画面・出力］
WORKSTATION WS08
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の PARALLEL が画面・出力に表示されること
② ステップ2 の EQQ0356E が画面・出力に表示されること
③ ステップ3 の WORKSTATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0187"><h3>ワークステーション管理 Workstation Definition 通常状態の確認 WS01</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>通常状態の確認では ワークステーション管理 の ワークステーション表示 を主操作として WS01 を判定します。基準値と現在値の差への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS01 に残します。通常状態の確認を補助する 現在計画状態 では PARALLEL を補助値として WS01 へ保存します。主判定の通常状態の確認ではワークステーション管理の ワークステーション表示 から WORKSTATION を読み WS01 へ残します。証跡照合の通常状態の確認ではワークステーション管理の WORKSTATION と PARALLEL を WS01 に保存します。記録対応の通常状態の確認ではワークステーション管理の WSIDとOpen Interval の証跡へ WS01 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で ワークステーション管理 の ワークステーション表示 と 現在計画状態 を組み合わせる際は Workstation Definition が操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素という仕組みを前提にします。削除済みワークステーションを計画内で使い続ける危険があります。WORKSTATION と WSIDとOpen Interval を対象 WS01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 5 WORK STATIONSのPARALLELをWSIDとOpen Intervalの主判定に採用する。ISPF Workstation Description LIST WS01の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SDSF browse SYSPRINT FIND EQQ0356EのEQQ0356EをWORKSTATIONと同義の成功表示として扱う。ISPF Workstation Description LIST WS01は実行しない。</li><li>C. ISPF Workstation Description LIST WS01を先に実行する。対象WS01のWORKSTATIONをWSIDとOpen Intervalとして記録する。続いてISPF EQQMTOPP option 5 WORK STATIONSで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. ISPF Workstation Description LIST WS01が応答を返した時点で正常とする。応答中のWORKSTATIONの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cはワークステーション表示で WORKSTATION を読みWSIDとOpen Intervalの主値として通常状態を確定しWS01に残します。
背景・仕組み: 通常状態の確認では現在計画状態を補助操作としWorkstation Definitionの基準値と現在値の差をPARALLELと対象WS01で照合します。
選択肢の理由: ワークステーション表示と現在計画状態の役割を分けるとA: PARALLELはWORKSTATIONを代替しないうえに追加前提も不正な点でWorkstation Definitionに使えません、B: EQQ0356EとWORKSTATIONは確認項目が異なる点でWS01を採用できません、C: WORKSTATIONを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではWSIDとOpen Intervalを判定できない点で一次資料と一致しません。結論として通常状態の確認のワークステーション管理で判定する対象は WS01 です。
用語の初出定義: 通常状態の確認で使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS01へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 通常状態の確認 WS01</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて通常状態を確定し、WS01のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS01を指定し、WS01のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS01
→ Enter を押す
［画面・出力］
WORKSTATION WS01
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS01の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS01 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS01の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS01
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の WORKSTATION が画面・出力に表示されること
② ステップ2 の PARALLEL が画面・出力に表示されること
③ ステップ3 の EQQ0356E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0188"><h3>ワークステーション管理 Workstation Definition 障害切り分け WS04</h3><p class="kb-meta">分類: ワークステーション管理 ・ 難易度: 中級</p><p>障害切り分けでは ワークステーション管理 の ワークステーション表示 を主操作として WS04 を判定します。最初に失敗した処理への注意として「削除済みワークステーションを計画内で使い続ける危険があります」を WS04 に残します。障害切り分けを補助する 現在計画状態 では PARALLEL を補助値として WS04 へ保存します。主判定の障害切り分けではワークステーション管理の ワークステーション表示 から WORKSTATION を読み WS04 へ残します。証跡照合の障害切り分けではワークステーション管理の WORKSTATION と PARALLEL を WS04 に保存します。記録対応の障害切り分けではワークステーション管理の WSIDとOpen Interval の証跡へ WS04 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで ワークステーション管理 の ワークステーション表示 と 現在計画状態 を実施し Workstation Definition の役割を確認します。削除済みワークステーションを計画内で使い続ける危険があります。対象 WS04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse SYSPRINT FIND EQQ0356EのEQQ0356EをWORKSTATIONと同義の成功表示として扱う。ISPF Workstation Description LIST WS04は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. ISPF Workstation Description LIST WS04の出力でWS04とWORKSTATIONが同じ応答にあることを確認する。WSIDとOpen Intervalをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. ISPF Workstation Description LIST WS04が応答を返した時点で正常とする。応答中のWORKSTATIONの値は記録しない。</li><li>D. ISPF Workstation Description LIST WS04のコマンド文字列だけを記録する。WORKSTATIONを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bはワークステーション表示で WORKSTATION を読みWSIDとOpen Intervalの主値として障害範囲を限定しWS04に残します。
技術的背景: 障害切り分けでは現在計画状態を補助操作としWorkstation Definitionの最初に失敗した処理をPARALLELと対象WS04で照合します。
四択の評価: ワークステーション表示と現在計画状態の役割を分けるとA: EQQ0356EとWORKSTATIONは確認項目が異なるうえに追加前提も不正な点でWS04を採用できません、B: WS04とWORKSTATIONを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではWSIDとOpen Intervalを判定できない点で一次資料と一致しません、D: 入力記録だけではWSIDとOpen Intervalを証明できない点でWSIDとOpen Intervalを確認できません。結論として障害切り分けのワークステーション管理で判定する対象は WS04 です。
初出語の意味: 障害切り分けで使う Workstation Definition は操作の実行場所、種別、報告属性、稼働区間、宛先を定義してスケジューリング可否を決める要素を表しWSIDとOpen Intervalを判定する際にWS04へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション管理 Workstation Definition 障害切り分け WS04</strong></p><p>検証目的: ワークステーション管理のWorkstation Definitionについて障害範囲を限定し、WS04のWSIDとOpen Intervalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象WS04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF Workstation Description LIST WS04を指定し、WS04のワークステーション表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Workstation Description LIST WS04
→ Enter を押す
［画面・出力］
WORKSTATION WS04
TYPE COMPUTER
REPORTING ATTRIBUTE AUTOMATIC
OPEN INTERVAL 0000-2400
画面・出力にあるWORKSTATIONを読み、WSIDとOpen Intervalと対象WS04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 5 WORK STATIONSを指定し、WS04の現在計画状態を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 5 WORK STATIONS
→ Enter を押す
［画面・出力］
WSID WS04 STATUS OPEN PARALLEL SERVERS 04 LINK ACTIVE
画面・出力にあるPARALLELを読み、WSIDとOpen Intervalと対象WS04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationのワークステーション管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0356Eを指定し、WS04の定義不整合を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0356E
→ Enter を押す
［画面・出力］
EQQ0356E VIRTUAL FLAG CHANGED FOR WORKSTATION WS04
画面・出力にあるEQQ0356Eを読み、WSIDとOpen Intervalと対象WS04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の WORKSTATION が画面・出力に表示されること
② ステップ2 の PARALLEL が画面・出力に表示されること
③ ステップ3 の EQQ0356E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


## 依存関係


<section class="kb-item" id="c15-i0189"><h3>先行操作</h3><p class="kb-meta">分類: 依存関係 ・ 難易度: 初級</p><p>IBM Workload Automation の 依存関係で扱う先行操作は、ある操作を開始する前に完了している必要がある操作です。ジョブネットの順序制御の基本であり、未完了の先行操作があると後続は待機します。遅延調査ではどの先行条件で止まっているかを確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認の先行操作に関係する先行操作の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. 先行操作の名称と担当者名のみを残して条件確認の先行操作の表示本文を確認対象に含めない。</li><li>C. 作業スケジューラー以外の画面で条件確認の先行操作を確認し同じ証跡として扱ったことにする。</li><li>D. EQQZ045I の有無を見ず条件確認の先行操作の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では先行操作は「先行操作の用途を作業スケジューラーの表示で確認する条件確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IBM Workload Automationの先行操作と EQQZ045I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では先行操作を IBM Workload Automationで扱う確認対象とし、用語名は条件確認用語です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>先行操作</strong></p><p>検証目的: 条件確認の先行操作について、IBM Workload Automation の 依存関係で扱う先行操作は、ある操作を開始する前に完了している必要がある操作です。ジョブネットの順序制御の基本であり、未完に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、条件確認の先行操作の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄に先行操作を指定し、OSKB010009の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND 先行操作
CASE OSKB010009
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM 先行操作
CASE OSKB010009
SOURCE IBM Workload Automation
先行操作とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010009を同じ出力で読み、条件確認の先行操作の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010009
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010009
COMMAND ===&gt; OPSTAT
OPERATION OSKB010009 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の 先行操作 と OSKB010009 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0190"><h3>条件依存</h3><p class="kb-meta">分類: 依存関係 ・ 難易度: 上級</p><p>IBM Workload Automation の 依存関係で扱う条件依存は、単なる完了順序ではなく、戻りコードや条件の成立に基づいて後続操作を制御する仕組みです。異常終了時の迂回や代替処理で使われます。設定を誤ると失敗ジョブの後続が意図せず動くため注意します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認の条件依存で条件依存の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. 条件依存の出力を取らず区切確認の条件依存の説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. OPSTAT を省略して区切確認の条件依存の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の条件依存へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では条件依存は「区切確認の条件依存に関係する定義値と表示行を照合する区切確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では条件依存の属性行と EQQZ045I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では条件依存を IBM Workload Automationの運用手順で確認し、初出名は区切確認初出です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>条件依存</strong></p><p>検証目的: 区切確認の条件依存について、IBM Workload Automation の 依存関係で扱う条件依存は、単なる完了順序ではなく、戻りコードや条件の成立に基づいて後続操作を制御する仕組みです。異常終了に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、区切確認の条件依存の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄に条件依存を指定し、OSKB010010の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND 条件依存
CASE OSKB010010
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM 条件依存
CASE OSKB010010
SOURCE IBM Workload Automation
条件依存とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010010を同じ出力で読み、区切確認の条件依存の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010010
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010010
COMMAND ===&gt; OPSTAT
OPERATION OSKB010010 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の 条件依存 と OSKB010010 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 基本概念


<section class="kb-item" id="c15-i0191"><h3>Z Workload Scheduler</h3><p class="kb-meta">分類: 基本概念 ・ 難易度: 初級</p><p>IBM Workload Automation の 基本概念で扱うZ Workload Schedulerは、IBM Z Workload Scheduler は、z/OS 上のジョブ、開始タスク、依存関係、カレンダーを計画して実行管理するスケジューラです。手作業の投入順序を計画情報として管理し、実行状況を追跡します。運用では計画、トラッキング、JCL 準備の流れを分けて確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認の基本概念に関係する Z Workload Schedulerの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. OPSTAT の結果から対象行を抜き出し、構文確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. Z Workload Schedulerの名称と担当者名のみを残して構文確認の基本概念の表示本文を確認対象に含めない。</li><li>C. 作業スケジューラー以外の画面で構文確認の基本概念を確認し同じ証跡として扱ったことにする。</li><li>D. EQQZ045I の有無を見ず構文確認の基本概念の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Z Workload Scheduler は「Z Workload Schedulerの用途を作業スケジューラーの表示で確認する構文確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では IBM Workload Automationの Z Workload Schedulerと EQQZ045I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Z Workload Schedulerを IBM Workload Automationで扱う確認対象とし、用語名は構文確認用語です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Z Workload Scheduler</strong></p><p>検証目的: 構文確認の基本概念について、IBM Workload Automation の 基本概念で扱う Z Workload Schedulerは、IBM Z Workload Scheduler は、z/OSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、構文確認の基本概念の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にZ Workload Schedulを指定し、OSKB010001の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND Z Workload Schedul
CASE OSKB010001
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM Z Workload Schedul
CASE OSKB010001
SOURCE IBM Workload Automation
Z Workload SchedulとOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010001を同じ出力で読み、構文確認の基本概念の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010001
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010001
COMMAND ===&gt; OPSTAT
OPERATION OSKB010001 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の Z Workload Schedul と OSKB010001 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 定義


<section class="kb-item" id="c15-i0192"><h3>アプリケーション定義</h3><p class="kb-meta">分類: 定義 ・ 難易度: 中級</p><p>IBM Workload Automation の 定義で扱うアプリケーション定義は、関連する操作やジョブを業務単位にまとめる定義です。実行順序、カレンダー、依存関係、JCL の扱いが含まれます。変更時は業務名だけでなく、配下の操作と依存関係を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認のアプリケーション定義に関係するアプリケーション定義の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. OPSTAT で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. アプリケーション定義の名称と担当者名のみを残して終端確認のアプリケーション定義の表示本文を確認対象に含めない。</li><li>C. 作業スケジューラー以外の画面で終端確認のアプリケーション定義を確認し同じ証跡として扱ったことにする。</li><li>D. EQQZ045I の有無を見ず終端確認のアプリケーション定義の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠ではアプリケーション定義は「アプリケーション定義の用途を作業スケジューラーの表示で確認する終端確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では IBM Workload Automationのアプリケーション定義と EQQZ045I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語ではアプリケーション定義を IBM Workload Automationで扱う確認対象とし、用語名は終端確認用語です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アプリケーション定義</strong></p><p>検証目的: 終端確認のアプリケーション定義について、IBM Workload Automation の 定義で扱うアプリケーション定義は、関連する操作やジョブを業務単位にまとめる定義です。実行順序、カレンダー、依存関係、JCに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、終端確認のアプリケーション定義の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にアプリケーション定義を指定し、OSKB010005の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND アプリケーション定義
CASE OSKB010005
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM アプリケーション定義
CASE OSKB010005
SOURCE IBM Workload Automation
アプリケーション定義とOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010005を同じ出力で読み、終端確認のアプリケーション定義の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010005
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010005
COMMAND ===&gt; OPSTAT
OPERATION OSKB010005 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の アプリケーション定義 と OSKB010005 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0193"><h3>カレンダー</h3><p class="kb-meta">分類: 定義 ・ 難易度: 初級</p><p>IBM Workload Automation の 定義で扱うカレンダーは、営業日、休日、期間定義を管理して実行日判定に使う定義です。業務スケジュールが実行されない原因は、カレンダーや期間の定義にあることがあります。年次保守では翌年の休日反映を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認のカレンダーで作業スケジューラーの運用確認を行います。カレンダーの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IBM Workload Automationと無関係な一覧で上書確認のカレンダーを確認した扱いにする。</li><li>B. EQQZ045I の有無を確認せず上書確認のカレンダーを正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. カレンダーの属性行を読まず上書確認のカレンダーの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠ではカレンダーは「IBM Workload Automationでカレンダーの扱いを記録する上書確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡ではカレンダーの表示結果と EQQZ045I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料ではカレンダーの使い方を出典欄から追跡し、資料名は上書確認資料です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>カレンダー</strong></p><p>検証目的: 上書確認のカレンダーについて、IBM Workload Automation の 定義で扱うカレンダーは、営業日、休日、期間定義を管理して実行日判定に使う定義です。業務スケジュールが実行されない原因は、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、上書確認のカレンダーの確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にカレンダーを指定し、OSKB010007の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND カレンダー
CASE OSKB010007
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM カレンダー
CASE OSKB010007
SOURCE IBM Workload Automation
カレンダーとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010007を同じ出力で読み、上書確認のカレンダーの根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010007
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010007
COMMAND ===&gt; OPSTAT
OPERATION OSKB010007 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の カレンダー と OSKB010007 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0194"><h3>ジョブ記述</h3><p class="kb-meta">分類: 定義 ・ 難易度: 中級</p><p>IBM Workload Automation の 定義で扱うジョブ記述は、スケジューラが投入する z/OS ジョブや開始タスクの属性を定義する情報です。JCL、実行ワークステーション、依存関係、リカバリ動作と結び付きます。障害時は JES 上のジョブと scheduler 上の操作を対応させます</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認のジョブ記述でジョブ記述の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ジョブ記述の出力を取らず探索確認のジョブ記述の説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. OPSTAT を省略して探索確認のジョブ記述の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認のジョブ記述へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠ではジョブ記述は「探索確認のジョブ記述に関係する定義値と表示行を照合する探索確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡ではジョブ記述の属性行と EQQZ045I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出ではジョブ記述を IBM Workload Automationの運用手順で確認し、初出名は探索確認初出です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ジョブ記述</strong></p><p>検証目的: 探索確認のジョブ記述について、IBM Workload Automation の 定義で扱うジョブ記述は、スケジューラが投入する z/OS ジョブや開始タスクの属性を定義する情報です。JCL、実行ワークに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、探索確認のジョブ記述の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にジョブ記述を指定し、OSKB010006の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND ジョブ記述
CASE OSKB010006
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM ジョブ記述
CASE OSKB010006
SOURCE IBM Workload Automation
ジョブ記述とOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010006を同じ出力で読み、探索確認のジョブ記述の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010006
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010006
COMMAND ===&gt; OPSTAT
OPERATION OSKB010006 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の ジョブ記述 と OSKB010006 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0195"><h3>ワークステーション</h3><p class="kb-meta">分類: 定義 ・ 難易度: 中級</p><p>IBM Workload Automation の 定義で扱うワークステーションは、ジョブや操作を実行する論理的な処理場所を表す定義です。z/OS の実行先、手作業、プリンターなどを区別できます。ジョブが投入されない場合は、ワークステーションの可用性と宛先を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認のワークステーションに関するワークステーションの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. OPSTAT の結果を残さず置換確認のワークステーションの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認のワークステーションの証跡として保存して根拠にする。</li><li>C. ワークステーションの変更点を出力本文から切り離して置換確認のワークステーションの承認欄のみ残す。</li><li>D. 同じ画面で対象行と EQQZ045I を読み、置換確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠ではワークステーションは「ワークステーションの状態と出力メッセージを結び付ける置換確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存ではワークステーションの出力行と EQQZ045I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象ではワークステーションを IBM Workload Automationの確認記録に残し、対象名は置換確認対象です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ワークステーション</strong></p><p>検証目的: 置換確認のワークステーションについて、IBM Workload Automation の 定義で扱うワークステーションは、ジョブや操作を実行する論理的な処理場所を表す定義です。z/OS の実行先、手作業、プリンに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、置換確認のワークステーションの確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にワークステーションを指定し、OSKB010004の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND ワークステーション
CASE OSKB010004
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM ワークステーション
CASE OSKB010004
SOURCE IBM Workload Automation
ワークステーションとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010004を同じ出力で読み、置換確認のワークステーションの根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010004
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010004
COMMAND ===&gt; OPSTAT
OPERATION OSKB010004 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の ワークステーション と OSKB010004 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0196"><h3>特殊資源</h3><p class="kb-meta">分類: 定義 ・ 難易度: 中級</p><p>IBM Workload Automation の 定義で扱う特殊資源は、データセット、テープ装置、業務上の排他対象などを scheduler 上で資源として扱う定義です。競合するジョブの同時実行を防ぐために使います。滞留時は資源を保持している操作と待っている操作を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認の特殊資源に関する特殊資源の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. OPSTAT の結果を残さず出力確認の特殊資源の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の特殊資源の証跡として保存して根拠にする。</li><li>C. 特殊資源の変更点を出力本文から切り離して出力確認の特殊資源の承認欄のみ残す。</li><li>D. IBM Workload Automationの表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では特殊資源は「特殊資源の状態と出力メッセージを結び付ける出力確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では特殊資源の出力行と EQQZ045I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では特殊資源を IBM Workload Automationの確認記録に残し、対象名は出力確認対象です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源</strong></p><p>検証目的: 出力確認の特殊資源について、IBM Workload Automation の 定義で扱う特殊資源は、データセット、テープ装置、業務上の排他対象などを scheduler 上で資源として扱う定義です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、出力確認の特殊資源の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄に特殊資源を指定し、OSKB010008の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND 特殊資源
CASE OSKB010008
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM 特殊資源
CASE OSKB010008
SOURCE IBM Workload Automation
特殊資源とOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010008を同じ出力で読み、出力確認の特殊資源の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010008
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010008
COMMAND ===&gt; OPSTAT
OPERATION OSKB010008 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の 特殊資源 と OSKB010008 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 操作


<section class="kb-item" id="c15-i0197"><h3>Dynamic Workload Console</h3><p class="kb-meta">分類: 操作 ・ 難易度: 初級</p><p>IBM Workload Automation の 操作で扱うDynamic Workload Consoleは、計画確認、操作監視、問題調査を Web から行うためのインターフェースです。z/OS の ISPF パネルと役割が重なる部分もあります。運用手順ではどの画面で状態を確認するかを明確にします</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認の操作で作業スケジューラーの運用確認を行います。Dynamic Workload Consoleの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IBM Workload Automationと無関係な一覧で順序確認の操作を確認した扱いにする。</li><li>B. EQQZ045I の有無を確認せず順序確認の操作を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. Dynamic Workload Consoleの属性行を読まず順序確認の操作の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Dynamic Workload Console は「IBM Workload Automationで Dynamic Workload Consoleの扱いを記録する順序確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Dynamic Workload Consoleの表示結果と EQQZ045I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Dynamic Workload Consoleの使い方を出典欄から追跡し、資料名は順序確認資料です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Dynamic Workload Console</strong></p><p>検証目的: 順序確認の操作について、IBM Workload Automation の 操作で扱う Dynamic Workload Consoleは、計画確認、操作監視、問題調査を Web から行うためのインに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、順序確認の操作の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にDynamic Workload Cを指定し、OSKB010015の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND Dynamic Workload C
CASE OSKB010015
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM Dynamic Workload C
CASE OSKB010015
SOURCE IBM Workload Automation
Dynamic Workload CとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010015を同じ出力で読み、順序確認の操作の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010015
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010015
COMMAND ===&gt; OPSTAT
OPERATION OSKB010015 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の Dynamic Workload C と OSKB010015 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0198"><h3>ISPF パネルインターフェース</h3><p class="kb-meta">分類: 操作 ・ 難易度: 初級</p><p>IBM Workload Automation の 操作で扱うISPF パネルインターフェースは、z/OS 上で Z Workload Scheduler を操作するための対話画面です。計画、操作、依存関係、エラー状態をメインフレーム端末上で確認できます。障害時は画面上の操作番号と JES ジョブ名を対応させます</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認のパネルインターフェースに関する ISPF パネルインターフェースの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. OPSTAT の結果を残さず値域確認のパネルインターフェースの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認のパネルインターフェースの証跡として保存して根拠にする。</li><li>C. ISPF パネルインターフェースの変更点を出力本文から切り離して値域確認のパネルインターフェースの承認欄のみ残す。</li><li>D. 同じ画面で対象行と EQQZ045I を読み、値域確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では ISPF パネルインターフェース は「ISPF パネルインターフェースの状態と出力メッセージを結び付ける値域確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では ISPF パネルインターフェースの出力行と EQQZ045I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では ISPF パネルインターフェースを IBM Workload Automationの確認記録に残し、対象名は値域確認対象です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISPF パネルインターフェース</strong></p><p>検証目的: 値域確認のパネルインターフェースについて、IBM Workload Automation の 操作で扱う ISPF パネルインターフェースは、z/OS 上で Z Workload Scheduler を操作するためのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、値域確認のパネルインターフェースの確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にISPF パネルインターフェースを指定し、OSKB010016の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND ISPF パネルインターフェース
CASE OSKB010016
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM ISPF パネルインターフェース
CASE OSKB010016
SOURCE IBM Workload Automation
ISPF パネルインターフェースとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010016を同じ出力で読み、値域確認のパネルインターフェースの根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010016
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010016
COMMAND ===&gt; OPSTAT
OPERATION OSKB010016 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の ISPF パネルインターフェース と OSKB010016 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 特殊資源管理


<section class="kb-item" id="c15-i0199"><h3>conman submit sched 再実行判断 再計画083</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 上級</p><p>第八十三観点 特殊資源管理 の 再計画083 では conman submit sched を点検します。第八十三観点 対象は スケジュール済みのジョブストリームをオンデマンドで投入し、計画外作業を運用記録付きでです。第八十三観点 待ち状態がある時は ISPF パネルのワークステーション列 と IWAJOB103 の時刻差を確認します。第八十三観点 ジョブログは JES の purge 前に IWAログ103へ転記します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>conman submit sched 再実行判断 再計画083</strong></p><p>検証目的: 特殊資源管理における conman submit sched の再実行判断を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=IWAJOB103</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、conman submit sched の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
Dynamic Workload Console
IBM Z Workload Scheduler &gt; Workload &gt; Monitor &gt; Monitor Jobs
Filter job ===&gt; IWAJOB103
→ Enter を押す
［画面・出力］
Monitor Jobs
Engine ZWS1 Job IWAJOB103 Job Stream PAYROLL103 Status Successful Workstation CPU11
画面・出力には Monitor が含まれる。Monitor を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、ISPF パネルのワークステーション列 と IWAJOB103 の対応を確認する。
［操作（入力）］
Dynamic Workload Console
Selected job IWAJOB103
Action ===&gt; Job Log
→ Enter を押す
［画面・出力］
Job Log for IWAJOB103
JESMSGLG JOB IWAJOB103
IEF142I IWAJOB103 STEP010 - STEP WAS EXECUTED - COND CODE 0000
画面・出力には IWAJOB103 が含まれる。IWAJOB103 を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
Dynamic Workload Console
Selected job IWAJOB103
Action ===&gt; Properties
→ Enter を押す
［画面・出力］
Job Properties
Job IWAJOB103
Internal status Successful
Return code 0000
Operation 110
画面・出力には Properties が含まれる。Properties を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Monitor が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: IWAJOB103 が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Properties が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0200"><h3>conman submit sched 実行監視 資源確認053</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>第五十三観点 conman submit sched は IBM Workload Automation の 特殊資源管理 で扱う確認点です。第五十三観点 対象は スケジュール済みのジョブストリームをオンデマンドで投入し、計画外作業を運用記録付きでです。第五十三観点 採取値 IWAJOB073 を計画表とログの両方で読み、採取時刻をそろえます。第五十三観点 採取後は DWC 表示と ISPF 表示の差を IWA比較073に分けます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>conman submit sched 実行監視 資源確認053</strong></p><p>検証目的: 特殊資源管理における conman submit sched の実行監視を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=IWAJOB073</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、conman submit sched の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
Dynamic Workload Console
IBM Z Workload Scheduler &gt; Workload &gt; Monitor &gt; Monitor Jobs
Filter job ===&gt; IWAJOB073
→ Enter を押す
［画面・出力］
Monitor Jobs
Engine ZWS1 Job IWAJOB073 Job Stream PAYROLL073 Status Successful Workstation CPU05
画面・出力には Monitor が含まれる。Monitor を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、ISPF パネルのワークステーション列 と IWAJOB073 の対応を確認する。
［操作（入力）］
Dynamic Workload Console
Selected job IWAJOB073
Action ===&gt; Job Log
→ Enter を押す
［画面・出力］
Job Log for IWAJOB073
JESMSGLG JOB IWAJOB073
IEF142I IWAJOB073 STEP010 - STEP WAS EXECUTED - COND CODE 0000
画面・出力には IWAJOB073 が含まれる。IWAJOB073 を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
Dynamic Workload Console
Selected job IWAJOB073
Action ===&gt; Properties
→ Enter を押す
［画面・出力］
Job Properties
Job IWAJOB073
Internal status Successful
Return code 0000
Operation 050
画面・出力には Properties が含まれる。Properties を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Monitor が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: IWAJOB073 が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Properties が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0201"><h3>conman submit sched 計画反映 導入確認023</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>第二十三観点 特殊資源管理 の 導入確認023 では conman submit sched を点検します。第二十三観点 対象は スケジュール済みのジョブストリームをオンデマンドで投入し、計画外作業を運用記録付きでです。第二十三観点 待ち状態がある時は ISPF パネルのワークステーション列 と IWAJOB043 の時刻差を確認します。第二十三観点 ジョブログは JES の purge 前に IWAログ043へ転記します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>conman submit sched 計画反映 導入確認023</strong></p><p>検証目的: 特殊資源管理における conman submit sched の計画反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=IWAJOB043</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、conman submit sched の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
Dynamic Workload Console
IBM Z Workload Scheduler &gt; Workload &gt; Monitor &gt; Monitor Jobs
Filter job ===&gt; IWAJOB043
→ Enter を押す
［画面・出力］
Monitor Jobs
Engine ZWS1 Job IWAJOB043 Job Stream PAYROLL043 Status Successful Workstation CPU11
画面・出力には Monitor が含まれる。Monitor を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、ISPF パネルのワークステーション列 と IWAJOB043 の対応を確認する。
［操作（入力）］
Dynamic Workload Console
Selected job IWAJOB043
Action ===&gt; Job Log
→ Enter を押す
［画面・出力］
Job Log for IWAJOB043
JESMSGLG JOB IWAJOB043
IEF142I IWAJOB043 STEP010 - STEP WAS EXECUTED - COND CODE 0000
画面・出力には IWAJOB043 が含まれる。IWAJOB043 を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
Dynamic Workload Console
Selected job IWAJOB043
Action ===&gt; Properties
→ Enter を押す
［画面・出力］
Job Properties
Job IWAJOB043
Internal status Successful
Return code 0000
Operation 230
画面・出力には Properties が含まれる。Properties を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Monitor が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: IWAJOB043 が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Properties が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0202"><h3>job stream 変更反映 再実行038</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>第三十八観点 job stream の 再実行038 は IBM Workload Automation の 特殊資源管理 に属します。第三十八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第三十八観点 IWA058 の確認では tracker の通信完了メッセージ を起点に、RCY02 と対象 engine を照合します。第三十八観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡058として整理します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>job stream 変更反映 再実行038</strong></p><p>検証目的: 特殊資源管理における job stream の変更反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY02</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; S IWAJOB058
→ Enter を押す
［画面・出力］
EQQRCLSE RESTART AND CLEANUP
JOB IWAJOB058 OPERATION 140 STATUS ERROR
CLEANUP DATA SETS DISPLAYED
画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY02 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; VERIFY
→ Enter を押す
［画面・出力］
EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
JOB IWAJOB058 RESTART ACTION REQUIRES CONFIRMATION
画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; STEP
→ Enter を押す
［画面・出力］
RESTART SELECTION
JOB IWAJOB058 STEP STEP010 SELECTED
CLEANUP ACTION LIST AVAILABLE
画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0203"><h3>job stream 状態確認 照合098</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 上級</p><p>第九十八観点 job stream の 照合098 は IBM Workload Automation の 特殊資源管理 に属します。第九十八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第九十八観点 IWA118 の確認では tracker の通信完了メッセージ を起点に、RCY08 と対象 engine を照合します。第九十八観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡118として整理します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>job stream 状態確認 照合098</strong></p><p>検証目的: 特殊資源管理における job stream の状態確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY08</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; S IWAJOB118
→ Enter を押す
［画面・出力］
EQQRCLSE RESTART AND CLEANUP
JOB IWAJOB118 OPERATION 020 STATUS ERROR
CLEANUP DATA SETS DISPLAYED
画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY08 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; VERIFY
→ Enter を押す
［画面・出力］
EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
JOB IWAJOB118 RESTART ACTION REQUIRES CONFIRMATION
画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; STEP
→ Enter を押す
［画面・出力］
RESTART SELECTION
JOB IWAJOB118 STEP STEP010 SELECTED
CLEANUP ACTION LIST AVAILABLE
画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0204"><h3>job stream 資源制御 依存確認008</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 初級</p><p>第八観点 依存確認008 では 特殊資源管理 にある job stream を扱います。第八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第八観点 DWC と ISPF の結果を分け、RCY08 の記録先を明確にします。第八観点 資源待ちがあれば special resource 名を IWA資源028へ記録します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>job stream 資源制御 依存確認008</strong></p><p>検証目的: 特殊資源管理における job stream の資源制御を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY08</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; S IWAJOB028
→ Enter を押す
［画面・出力］
EQQRCLSE RESTART AND CLEANUP
JOB IWAJOB028 OPERATION 080 STATUS ERROR
CLEANUP DATA SETS DISPLAYED
画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY08 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; VERIFY
→ Enter を押す
［画面・出力］
EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
JOB IWAJOB028 RESTART ACTION REQUIRES CONFIRMATION
画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; STEP
→ Enter を押す
［画面・出力］
RESTART SELECTION
JOB IWAJOB028 STEP STEP010 SELECTED
CLEANUP ACTION LIST AVAILABLE
画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0205"><h3>job stream 障害切分け ログ採取068</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>第六十八観点 ログ採取068 では 特殊資源管理 にある job stream を扱います。第六十八観点 対象は 計画内でまとめて管理される一連のジョブや操作で、Dynamic Workload Cです。第六十八観点 DWC と ISPF の結果を分け、RCY05 の記録先を明確にします。第六十八観点 資源待ちがあれば special resource 名を IWA資源088へ記録します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>job stream 障害切分け ログ採取068</strong></p><p>検証目的: 特殊資源管理における job stream の障害切分けを机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=RCY05</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、job stream の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; S IWAJOB088
→ Enter を押す
［画面・出力］
EQQRCLSE RESTART AND CLEANUP
JOB IWAJOB088 OPERATION 200 STATUS ERROR
CLEANUP DATA SETS DISPLAYED
画面・出力には EQQRCLSE が含まれる。EQQRCLSE を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、tracker の通信完了メッセージ と RCY05 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; VERIFY
→ Enter を押す
［画面・出力］
EQQM037W OPERATION STATUS OR OPERATION JOB ID HAS CHANGED
JOB IWAJOB088 RESTART ACTION REQUIRES CONFIRMATION
画面・出力には EQQM037W が含まれる。EQQM037W を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQRCLSE -------- RESTART AND CLEANUP --------
Command ===&gt; STEP
→ Enter を押す
［画面・出力］
RESTART SELECTION
JOB IWAJOB088 STEP STEP010 SELECTED
CLEANUP ACTION LIST AVAILABLE
画面・出力には RESTART が含まれる。RESTART を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQRCLSE が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQM037W が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: RESTART が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0206"><h3>特殊資源管理 Special Resource ログとの照合 SR07</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>ログとの照合では 特殊資源管理 の 資源モニター を主操作として SR07 を判定します。時刻と対象識別子への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR07 に残します。ログとの照合を補助する 使用操作 では ALLOCATED を補助値として SR07 へ保存します。主判定のログとの照合では特殊資源管理の 資源モニター から QUANTITY を読み SR07 へ残します。証跡照合のログとの照合では特殊資源管理の QUANTITY と ALLOCATED を SR07 に保存します。記録対応のログとの照合では特殊資源管理の QuantityとAvailability の証跡へ SR07 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で 特殊資源管理 の 資源モニター と 使用操作 を用い 操作とログを対応 します。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。QUANTITY で対象 SR07 の QuantityとAvailability を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. QUANTITYを含む資源モニターの応答行を保存する。その応答を得るためISPF EQQMTOPP option 7 SPECRESを使用する。対象SR07のQuantityとAvailabilityとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. ISPF EQQMTOPP option 7 SPECRESが応答を返した時点で正常とする。応答中のQUANTITYの値は記録しない。EQQR011IをQUANTITYと同じ判定値とみなし対象SR07の主証跡にする。Special Resourceの時刻と対象識別子は確認済みとして扱う。さらにSDSF browse EQQMLOG FIND SR07のEQQR011IをQUANTITYと同種の値として併記する。</li><li>C. ISPF EQQMTOPP option 7 SPECRESのコマンド文字列だけを記録する。QUANTITYを含む応答行は保存しない。</li><li>D. Special Resourceの停止または再定義を実施する。その後にISPF EQQMTOPP option 7 SPECRESでQUANTITYを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として操作とログを対応しSR07に残します。
機能の仕組み: ログとの照合では使用操作を補助操作としSpecial Resourceの時刻と対象識別子をALLOCATEDと対象SR07で照合します。
各候補の評価: 資源モニターと使用操作の役割を分けるとA: QUANTITYの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではQuantityとAvailabilityを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではQuantityとAvailabilityを証明できない点でQuantityとAvailabilityを確認できません、D: 変更前のQuantityとAvailabilityを失う点で使用操作の範囲を越えます。結論としてログとの照合の特殊資源管理で判定する対象は SR07 です。
用語の定義: ログとの照合で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR07へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource ログとの照合 SR07</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて操作とログを対応し、SR07のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR07の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR07 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR07を指定し、SR07の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR07
→ Enter を押す
［画面・出力］
RESOURCE SR07 ADID APP07 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR07を指定し、SR07のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR07
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR07 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
② ステップ2 の ALLOCATED が画面・出力に表示されること
③ ステップ3 の EQQR011I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0207"><h3>特殊資源管理 Special Resource 代替経路の確認 SR10</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>代替経路の確認では 特殊資源管理 の 資源モニター を主操作として SR10 を判定します。主経路との役割差への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR10 に残します。代替経路の確認を補助する 使用操作 では ALLOCATED を補助値として SR10 へ保存します。主判定の代替経路の確認では特殊資源管理の 資源モニター から QUANTITY を読み SR10 へ残します。証跡照合の代替経路の確認では特殊資源管理の QUANTITY と ALLOCATED を SR10 に保存します。記録対応の代替経路の確認では特殊資源管理の QuantityとAvailability の証跡へ SR10 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で 特殊資源管理 の 資源モニター と 使用操作 の役割を分け 主経路との役割差 を調べます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。対象 SR10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 7 SPECRESのコマンド文字列だけを記録する。QUANTITYを含む応答行は保存しない。</li><li>B. Special Resourceの停止または再定義を実施する。その後にISPF EQQMTOPP option 7 SPECRESでQUANTITYを採取する。</li><li>C. ジョブストリーム運用のInput ArrivalとStatusを確認する。その値を特殊資源管理のSR10にも適用する。</li><li>D. ISPF EQQMTOPP option 7 SPECRESとISPF Special Resource Monitor USERS SR10の対象名をそろえる。前者のQUANTITYをQuantityとAvailabilityの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として代替手段の成立を確認しSR10に残します。
運用上の背景: 代替経路の確認では使用操作を補助操作としSpecial Resourceの主経路との役割差をALLOCATEDと対象SR10で照合します。
候補別の検討: 資源モニターと使用操作の役割を分けるとA: 入力記録だけではQuantityとAvailabilityを証明できない点で一次資料と一致しません、B: 変更前のQuantityとAvailabilityを失う点でQuantityとAvailabilityを確認できません、C: ジョブストリーム運用の値ではQUANTITYを確認できない点で使用操作の範囲を越えます、D: 同じ対象名のQUANTITYを採用する点で現在値を示します。結論として代替経路の確認の特殊資源管理で判定する対象は SR10 です。
重要用語の定義: 代替経路の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR10へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 代替経路の確認 SR10</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて代替手段の成立を確認し、SR10のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR10の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR10 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR10を指定し、SR10の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR10
→ Enter を押す
［画面・出力］
RESOURCE SR10 ADID APP10 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR10を指定し、SR10のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR10
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR10 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
② ステップ2 の ALLOCATED が画面・出力に表示されること
③ ステップ3 の EQQR011I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0208"><h3>特殊資源管理 Special Resource 変更前の確認 SR02</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>変更前の確認では 特殊資源管理 の 使用操作 を主操作として SR02 を判定します。変更対象と非対象の境界への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR02 に残します。変更前の確認を補助する イベントログ では EQQR011I を補助値として SR02 へ保存します。主判定の変更前の確認では特殊資源管理の 使用操作 から ALLOCATED を読み SR02 へ残します。証跡照合の変更前の確認では特殊資源管理の ALLOCATED と EQQR011I を SR02 に保存します。記録対応の変更前の確認では特殊資源管理の QuantityとAvailability の証跡へ SR02 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で 特殊資源管理 の 使用操作 と イベントログ を照合し 変更対象と非対象の境界 を確かめます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。ALLOCATED を読む前に対象 SR02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. ISPF Special Resource Monitor USERS SR02を対象名なしで実行する。一覧の先頭行をSR02の結果として記録する。</li><li>B. 前回保存したISPF Special Resource Monitor USERS SR02の結果を使う。今回のSDSF browse EQQMLOG FIND SR02の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのSR02の出力を再利用する。今回のISPF Special Resource Monitor USERS SR02とSDSF browse EQQMLOG FIND SR02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象SR02についてISPF Special Resource Monitor USERS SR02の応答からALLOCATEDを確認する。SDSF browse EQQMLOG FIND SR02は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは使用操作で ALLOCATED を読みQuantityとAvailabilityの主値として変更前の証跡を保存しSR02に残します。
動作の背景: 変更前の確認ではイベントログを補助操作としSpecial Resourceの変更対象と非対象の境界をEQQR011Iと対象SR02で照合します。
各選択肢の検討: 使用操作とイベントログの役割を分けるとA: 先頭行はSR02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で使用操作を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で特殊資源管理に使いません、D: ALLOCATEDと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の特殊資源管理で判定する対象は SR02 です。
初出用語の定義: 変更前の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR02へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 変更前の確認 SR02</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて変更前の証跡を保存し、SR02のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR02を指定し、SR02の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR02
→ Enter を押す
［画面・出力］
RESOURCE SR02 ADID APP02 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR02を指定し、SR02のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR02
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR02 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR02の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR02 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ALLOCATED が画面・出力に表示されること
② ステップ2 の EQQR011I が画面・出力に表示されること
③ ステップ3 の QUANTITY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0209"><h3>特殊資源管理 Special Resource 変更後の確認 SR03</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>変更後の確認では 特殊資源管理 の イベントログ を主操作として SR03 を判定します。反映値と残存値への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR03 に残します。変更後の確認を補助する 資源モニター では QUANTITY を補助値として SR03 へ保存します。主判定の変更後の確認では特殊資源管理の イベントログ から EQQR011I を読み SR03 へ残します。証跡照合の変更後の確認では特殊資源管理の EQQR011I と QUANTITY を SR03 に保存します。記録対応の変更後の確認では特殊資源管理の QuantityとAvailability の証跡へ SR03 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で 特殊資源管理 の イベントログ と 資源モニター を組み合わせる際は Special Resource がジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能という仕組みを前提にします。実在装置の状態と特殊資源の論理可用性を混同する危険があります。EQQR011I と QuantityとAvailability を対象 SR03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 7 SPECRESで周辺状態を押さえる。その後にSDSF browse EQQMLOG FIND SR03でEQQR011Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. Special Resourceの停止または再定義を実施する。その後にSDSF browse EQQMLOG FIND SR03でEQQR011Iを採取する。</li><li>C. 監査ログと EQQMLOGのMessage IDとADIDを確認する。その値を特殊資源管理のSR03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Special Resourceの反映値と残存値は確認済みとして扱う。さらにISPF Special Resource Monitor USERS SR03のALLOCATEDをEQQR011Iと同種の値として併記する。</li><li>D. ISPF EQQMTOPP option 7 SPECRESが成功したためSDSF browse EQQMLOG FIND SR03のEQQR011Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aはイベントログで EQQR011I を読みQuantityとAvailabilityの主値として変更結果を検証しSR03に残します。
内部の仕組み: 変更後の確認では資源モニターを補助操作としSpecial Resourceの反映値と残存値をQUANTITYと対象SR03で照合します。
誤答を含む比較: イベントログと資源モニターの役割を分けるとA: 周辺状態の後にEQQR011Iを確認する点でSR03を判定できます、B: 変更前のQuantityとAvailabilityを失う点で資源モニターの範囲を越えます、C: 監査ログと EQQMLOGの値ではEQQR011Iを確認できないうえに追加前提も不正な点でSR03の値を示しません、D: 補助操作の成功ではEQQR011Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の特殊資源管理で判定する対象は SR03 です。
用語定義: 変更後の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR03へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 変更後の確認 SR03</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて変更結果を検証し、SR03のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR03を指定し、SR03のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR03
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR03 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR03の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR03 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR03を指定し、SR03の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR03
→ Enter を押す
［画面・出力］
RESOURCE SR03 ADID APP03 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQR011I が画面・出力に表示されること
② ステップ2 の QUANTITY が画面・出力に表示されること
③ ステップ3 の ALLOCATED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0210"><h3>特殊資源管理 Special Resource 引継ぎ記録 SR09</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>引継ぎ記録では 特殊資源管理 の イベントログ を主操作として SR09 を判定します。次担当者が追跡できる証跡への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR09 に残します。引継ぎ記録を補助する 資源モニター では QUANTITY を補助値として SR09 へ保存します。主判定の引継ぎ記録では特殊資源管理の イベントログ から EQQR011I を読み SR09 へ残します。証跡照合の引継ぎ記録では特殊資源管理の EQQR011I と QUANTITY を SR09 に保存します。記録対応の引継ぎ記録では特殊資源管理の QuantityとAvailability の証跡へ SR09 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で 特殊資源管理 の イベントログ と 資源モニター を組み合わせる際は Special Resource がジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能という仕組みを前提にします。実在装置の状態と特殊資源の論理可用性を混同する危険があります。EQQR011I と QuantityとAvailability を対象 SR09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 7 SPECRESが成功したためSDSF browse EQQMLOG FIND SR09のEQQR011Iも正常だと推定する。主出力は保存しない。</li><li>B. SDSF browse EQQMLOG FIND SR09を対象名なしで実行する。一覧の先頭行をSR09の結果として記録する。</li><li>C. 対象名SR09を指定してSDSF browse EQQMLOG FIND SR09を実行する。応答中のEQQR011Iと時刻を保存する。ISPF EQQMTOPP option 7 SPECRESで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSDSF browse EQQMLOG FIND SR09の結果を使う。今回のISPF EQQMTOPP option 7 SPECRESの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cはイベントログで EQQR011I を読みQuantityとAvailabilityの主値として再現可能な記録を作成しSR09に残します。
製品内の仕組み: 引継ぎ記録では資源モニターを補助操作としSpecial Resourceの次担当者が追跡できる証跡をQUANTITYと対象SR09で照合します。
選択肢別の説明: イベントログと資源モニターの役割を分けるとA: 補助操作の成功ではEQQR011Iを確定できない点でSR09の値を示しません、B: 先頭行はSR09と確定できない点で引継ぎ記録に合いません、C: EQQR011Iと時刻を保存する点でイベントログに合います、D: 採取時刻が異なる点で特殊資源管理に使いません。結論として引継ぎ記録の特殊資源管理で判定する対象は SR09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR09へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 引継ぎ記録 SR09</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて再現可能な記録を作成し、SR09のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR09を指定し、SR09のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR09
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR09 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR09の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR09 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR09を指定し、SR09の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR09
→ Enter を押す
［画面・出力］
RESOURCE SR09 ADID APP09 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQR011I が画面・出力に表示されること
② ステップ2 の QUANTITY が画面・出力に表示されること
③ ステップ3 の ALLOCATED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0211"><h3>特殊資源管理 Special Resource 復旧後の確認 SR06</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>復旧後の確認では 特殊資源管理 の イベントログ を主操作として SR06 を判定します。再発していないことを示す値への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR06 に残します。復旧後の確認を補助する 資源モニター では QUANTITY を補助値として SR06 へ保存します。主判定の復旧後の確認では特殊資源管理の イベントログ から EQQR011I を読み SR06 へ残します。証跡照合の復旧後の確認では特殊資源管理の EQQR011I と QUANTITY を SR06 に保存します。記録対応の復旧後の確認では特殊資源管理の QuantityとAvailability の証跡へ SR06 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で 特殊資源管理 の イベントログ と 資源モニター を実施し Special Resource の役割を確認します。実在装置の状態と特殊資源の論理可用性を混同する危険があります。対象 SR06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 長期計画管理のRun DateとInput Arrivalを確認する。その値を特殊資源管理のSR06にも適用する。</li><li>B. ISPF EQQMTOPP option 7 SPECRESが成功したためSDSF browse EQQMLOG FIND SR06のEQQR011Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SR06へ引き継げるものとする。Special Resourceの再発していないことを示す値は確認済みとして扱う。さらにISPF Special Resource Monitor USERS SR06のALLOCATEDをEQQR011Iと同種の値として併記する。</li><li>C. SDSF browse EQQMLOG FIND SR06を対象名なしで実行する。一覧の先頭行をSR06の結果として記録する。</li><li>D. SDSF browse EQQMLOG FIND SR06でEQQR011Iを取得してからISPF Special Resource Monitor USERS SR06でALLOCATEDを照合する。SR06のQuantityとAvailabilityを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dはイベントログで EQQR011I を読みQuantityとAvailabilityの主値として復旧後の安定性を確認しSR06に残します。
構成上の背景: 復旧後の確認では資源モニターを補助操作としSpecial Resourceの再発していないことを示す値をQUANTITYと対象SR06で照合します。
候補ごとの理由: イベントログと資源モニターの役割を分けるとA: 長期計画管理の値ではEQQR011Iを確認できない点で資源モニターの範囲を越えます、B: 補助操作の成功ではEQQR011Iを確定できないうえに追加前提も不正な点でSR06の値を示しません、C: 先頭行はSR06と確定できない点で復旧後の確認に合いません、D: EQQR011IとALLOCATEDを順に照合する点でイベントログに合います。結論として復旧後の確認の特殊資源管理で判定する対象は SR06 です。
初出用語: 復旧後の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR06へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 復旧後の確認 SR06</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて復旧後の安定性を確認し、SR06のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR06を指定し、SR06のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR06
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR06 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR06の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR06 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR06を指定し、SR06の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR06
→ Enter を押す
［画面・出力］
RESOURCE SR06 ADID APP06 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQR011I が画面・出力に表示されること
② ステップ2 の QUANTITY が画面・出力に表示されること
③ ステップ3 の ALLOCATED が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0212"><h3>特殊資源管理 Special Resource 復旧準備 SR05</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>復旧準備では 特殊資源管理 の 使用操作 を主操作として SR05 を判定します。再開前に必要な整合性への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR05 に残します。復旧準備を補助する イベントログ では EQQR011I を補助値として SR05 へ保存します。主判定の復旧準備では特殊資源管理の 使用操作 から ALLOCATED を読み SR05 へ残します。証跡照合の復旧準備では特殊資源管理の ALLOCATED と EQQR011I を SR05 に保存します。記録対応の復旧準備では特殊資源管理の QuantityとAvailability の証跡へ SR05 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で 特殊資源管理 の 使用操作 と イベントログ を使い 復旧条件を確認 します。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。ALLOCATED を読み対象 SR05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したISPF Special Resource Monitor USERS SR05の結果を使う。今回のSDSF browse EQQMLOG FIND SR05の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのSR05の出力を再利用する。今回のISPF Special Resource Monitor USERS SR05とSDSF browse EQQMLOG FIND SR05は実行済みとして扱う。</li><li>C. 変更を加えずISPF Special Resource Monitor USERS SR05を実行する。ALLOCATEDを保存する。差分はSDSF browse EQQMLOG FIND SR05の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SDSF browse EQQMLOG FIND SR05のEQQR011IをQuantityとAvailabilityの主判定に採用する。ISPF Special Resource Monitor USERS SR05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは使用操作で ALLOCATED を読みQuantityとAvailabilityの主値として復旧条件を確認しSR05に残します。
処理の仕組み: 復旧準備ではイベントログを補助操作としSpecial Resourceの再開前に必要な整合性をEQQR011Iと対象SR05で照合します。
選択結果の内訳: 使用操作とイベントログの役割を分けるとA: 採取時刻が異なる点で使用操作を代替しません、B: 過去出力では今回の復旧準備を示せない点で特殊資源管理に使いません、C: 変更前のALLOCATEDを保存する点で正答です、D: EQQR011IはALLOCATEDを代替しないうえに追加前提も不正な点でSR05を採用できません。結論として復旧準備の特殊資源管理で判定する対象は SR05 です。
用語の説明: 復旧準備で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR05へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 復旧準備 SR05</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて復旧条件を確認し、SR05のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR05を指定し、SR05の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR05
→ Enter を押す
［画面・出力］
RESOURCE SR05 ADID APP05 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR05を指定し、SR05のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR05
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR05 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR05の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR05 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ALLOCATED が画面・出力に表示されること
② ステップ2 の EQQR011I が画面・出力に表示されること
③ ステップ3 の QUANTITY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0213"><h3>特殊資源管理 Special Resource 構成監査 SR08</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>構成監査では 特殊資源管理 の 使用操作 を主操作として SR08 を判定します。定義値と稼働値の一致への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR08 に残します。構成監査を補助する イベントログ では EQQR011I を補助値として SR08 へ保存します。主判定の構成監査では特殊資源管理の 使用操作 から ALLOCATED を読み SR08 へ残します。証跡照合の構成監査では特殊資源管理の ALLOCATED と EQQR011I を SR08 に保存します。記録対応の構成監査では特殊資源管理の QuantityとAvailability の証跡へ SR08 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で 特殊資源管理 の 使用操作 と イベントログ を照合し 定義値と稼働値の一致 を確かめます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。ALLOCATED を読む前に対象 SR08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのSR08の出力を再利用する。今回のISPF Special Resource Monitor USERS SR08とSDSF browse EQQMLOG FIND SR08は実行済みとして扱う。</li><li>B. SDSF browse EQQMLOG FIND SR08の結果だけでは確定しない。ISPF Special Resource Monitor USERS SR08のALLOCATEDを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SDSF browse EQQMLOG FIND SR08のEQQR011IをQuantityとAvailabilityの主判定に採用する。ISPF Special Resource Monitor USERS SR08の応答は採取対象から外す。</li><li>D. ISPF EQQMTOPP option 7 SPECRESのQUANTITYをALLOCATEDと同義の成功表示として扱う。ISPF Special Resource Monitor USERS SR08は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bは使用操作で ALLOCATED を読みQuantityとAvailabilityの主値として構成差分を監査しSR08に残します。
実行時の背景: 構成監査ではイベントログを補助操作としSpecial Resourceの定義値と稼働値の一致をEQQR011Iと対象SR08で照合します。
四つの候補の理由: 使用操作とイベントログの役割を分けるとA: 過去出力では今回の構成監査を示せない点で特殊資源管理に使いません、B: ALLOCATEDを主証跡として区別する点で正答です、C: EQQR011IはALLOCATEDを代替しない点でSR08を採用できません、D: QUANTITYとALLOCATEDは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の特殊資源管理で判定する対象は SR08 です。
初出語定義: 構成監査で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR08へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 構成監査 SR08</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて構成差分を監査し、SR08のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR08を指定し、SR08の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR08
→ Enter を押す
［画面・出力］
RESOURCE SR08 ADID APP08 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR08を指定し、SR08のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR08
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR08 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR08の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR08 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ALLOCATED が画面・出力に表示されること
② ステップ2 の EQQR011I が画面・出力に表示されること
③ ステップ3 の QUANTITY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0214"><h3>特殊資源管理 Special Resource 通常状態の確認 SR01</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>通常状態の確認では 特殊資源管理 の 資源モニター を主操作として SR01 を判定します。基準値と現在値の差への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR01 に残します。通常状態の確認を補助する 使用操作 では ALLOCATED を補助値として SR01 へ保存します。主判定の通常状態の確認では特殊資源管理の 資源モニター から QUANTITY を読み SR01 へ残します。証跡照合の通常状態の確認では特殊資源管理の QUANTITY と ALLOCATED を SR01 に保存します。記録対応の通常状態の確認では特殊資源管理の QuantityとAvailability の証跡へ SR01 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で 特殊資源管理 の 資源モニター と 使用操作 を用い 通常状態を確定 します。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。QUANTITY で対象 SR01 の QuantityとAvailability を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. ISPF Special Resource Monitor USERS SR01のALLOCATEDをQuantityとAvailabilityの主判定に採用する。ISPF EQQMTOPP option 7 SPECRESの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SDSF browse EQQMLOG FIND SR01のEQQR011IをQUANTITYと同義の成功表示として扱う。ISPF EQQMTOPP option 7 SPECRESは実行しない。</li><li>C. ISPF EQQMTOPP option 7 SPECRESを先に実行する。対象SR01のQUANTITYをQuantityとAvailabilityとして記録する。続いてISPF Special Resource Monitor USERS SR01で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. ISPF EQQMTOPP option 7 SPECRESが応答を返した時点で正常とする。応答中のQUANTITYの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として通常状態を確定しSR01に残します。
背景・仕組み: 通常状態の確認では使用操作を補助操作としSpecial Resourceの基準値と現在値の差をALLOCATEDと対象SR01で照合します。
選択肢の理由: 資源モニターと使用操作の役割を分けるとA: ALLOCATEDはQUANTITYを代替しないうえに追加前提も不正な点でSpecial Resourceに使えません、B: EQQR011IとQUANTITYは確認項目が異なる点でSR01を採用できません、C: QUANTITYを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではQuantityとAvailabilityを判定できない点で一次資料と一致しません。結論として通常状態の確認の特殊資源管理で判定する対象は SR01 です。
用語の初出定義: 通常状態の確認で使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR01へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 通常状態の確認 SR01</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて通常状態を確定し、SR01のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR01の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR01 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR01を指定し、SR01の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR01
→ Enter を押す
［画面・出力］
RESOURCE SR01 ADID APP01 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR01を指定し、SR01のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR01
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR01 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
② ステップ2 の ALLOCATED が画面・出力に表示されること
③ ステップ3 の EQQR011I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0215"><h3>特殊資源管理 Special Resource 障害切り分け SR04</h3><p class="kb-meta">分類: 特殊資源管理 ・ 難易度: 中級</p><p>障害切り分けでは 特殊資源管理 の 資源モニター を主操作として SR04 を判定します。最初に失敗した処理への注意として「実在装置の状態と特殊資源の論理可用性を混同する危険があります」を SR04 に残します。障害切り分けを補助する 使用操作 では ALLOCATED を補助値として SR04 へ保存します。主判定の障害切り分けでは特殊資源管理の 資源モニター から QUANTITY を読み SR04 へ残します。証跡照合の障害切り分けでは特殊資源管理の QUANTITY と ALLOCATED を SR04 に保存します。記録対応の障害切り分けでは特殊資源管理の QuantityとAvailability の証跡へ SR04 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで 特殊資源管理 の 資源モニター と 使用操作 の役割を分け 最初に失敗した処理 を調べます。Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能です。実在装置の状態と特殊資源の論理可用性を混同する危険があります。対象 SR04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse EQQMLOG FIND SR04のEQQR011IをQUANTITYと同義の成功表示として扱う。ISPF EQQMTOPP option 7 SPECRESは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. ISPF EQQMTOPP option 7 SPECRESの出力でSR04とQUANTITYが同じ応答にあることを確認する。QuantityとAvailabilityをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. ISPF EQQMTOPP option 7 SPECRESが応答を返した時点で正常とする。応答中のQUANTITYの値は記録しない。</li><li>D. ISPF EQQMTOPP option 7 SPECRESのコマンド文字列だけを記録する。QUANTITYを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bは資源モニターで QUANTITY を読みQuantityとAvailabilityの主値として障害範囲を限定しSR04に残します。
技術的背景: 障害切り分けでは使用操作を補助操作としSpecial Resourceの最初に失敗した処理をALLOCATEDと対象SR04で照合します。
四択の評価: 資源モニターと使用操作の役割を分けるとA: EQQR011IとQUANTITYは確認項目が異なるうえに追加前提も不正な点でSR04を採用できません、B: SR04とQUANTITYを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではQuantityとAvailabilityを判定できない点で一次資料と一致しません、D: 入力記録だけではQuantityとAvailabilityを証明できない点でQuantityとAvailabilityを確認できません。結論として障害切り分けの特殊資源管理で判定する対象は SR04 です。
初出語の意味: 障害切り分けで使う Special Resource はジョブ間で共有する論理資源の利用数、可用性、割当を計画の依存条件として管理する機能を表しQuantityとAvailabilityを判定する際にSR04へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特殊資源管理 Special Resource 障害切り分け SR04</strong></p><p>検証目的: 特殊資源管理のSpecial Resourceについて障害範囲を限定し、SR04のQuantityとAvailabilityを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象SR04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 7 SPECRESを指定し、SR04の資源モニターを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 7 SPECRES
→ Enter を押す
［画面・出力］
SPECIAL RESOURCE SR04 AVAILABLE YES QUANTITY 2 USED 1
画面・出力にあるQUANTITYを読み、QuantityとAvailabilityと対象SR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へISPF Special Resource Monitor USERS SR04を指定し、SR04の使用操作を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Special Resource Monitor USERS SR04
→ Enter を押す
［画面・出力］
RESOURCE SR04 ADID APP04 OPNO 020 QUANTITY 1 STATUS ALLOCATED
画面・出力にあるALLOCATEDを読み、QuantityとAvailabilityと対象SR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの特殊資源管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND SR04を指定し、SR04のイベントログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND SR04
→ Enter を押す
［画面・出力］
EQQR011I SPECIAL RESOURCE SR04 AVAILABILITY CHANGED TO YES
画面・出力にあるEQQR011Iを読み、QuantityとAvailabilityと対象SR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の QUANTITY が画面・出力に表示されること
② ステップ2 の ALLOCATED が画面・出力に表示されること
③ ステップ3 の EQQR011I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


## 現在計画管理


<section class="kb-item" id="c15-i0216"><h3>EQQMLOG ログ確認 依存確認016</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>第十六観点 依存確認016 では 現在計画管理 にある EQQMLOG を扱います。第十六観点 対象は controller、tracker、WAPL などのメッセージを確認するログで、Eです。第十六観点 特殊資源の使用量と待ち操作 を採る時点で CHK036 を明記し、変更反映の前提を守ります。第十六観点 後続作業では同じ engine と current plan を見たことを IWA監査036で残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EQQMLOG ログ確認 依存確認016</strong></p><p>検証目的: 現在計画管理における EQQMLOG のログ確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CHK036</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQMLOG の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
WAPL batch review
COMMAND ===&gt; BROWSE EQQYPARM
→ Enter を押す
［画面・出力］
EQQYPARM INIT SUBSYSTEM ZWS1
EQQMLIB SEQQMSG0
EQQMLOG IWA.WAPL.036.MLOG
画面・出力には EQQYPARM が含まれる。EQQYPARM を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、特殊資源の使用量と待ち操作 と CHK036 の対応を確認する。
［操作（入力）］
WAPL batch submit
COMMAND ===&gt; SUBMIT IWA.WAPL.CNTL(INIT036)
→ Enter を押す
［画面・出力］
EQQWAPL INIT COMPLETED
SUBSYSTEM ZWS1
MESSAGE LOG IWA.WAPL.036.MLOG
RETURN CODE 0000
画面・出力には EQQWAPL が含まれる。EQQWAPL を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
SDSF output browse
COMMAND ===&gt; FIND DYNLOG
→ Enter を押す
［画面・出力］
OPTIONS DYNLOG(IWA.WAPLLOG)
DYNAMIC LOG IWA.WAPLLOG.D260715.T0915A.IWAJOB036
ADVISORY MESSAGES WRITTEN
画面・出力には OPTIONS が含まれる。OPTIONS を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQYPARM が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQWAPL が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: OPTIONS が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0217"><h3>EQQMLOG 依存関係確認 再実行046</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 中級</p><p>第四十六観点 EQQMLOG の 再実行046 は IBM Workload Automation の 現在計画管理 に属します。第四十六観点 対象は controller、tracker、WAPL などのメッセージを確認するログで、Eです。第四十六観点 conman または WAPL の結果を使う時は、CHK066 の取得経路を残します。第四十六観点 WAPL を使う場合は subsystem 名を IWA言語066に残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EQQMLOG 依存関係確認 再実行046</strong></p><p>検証目的: 現在計画管理における EQQMLOG の依存関係確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CHK066</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQMLOG の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
WAPL batch review
COMMAND ===&gt; BROWSE EQQYPARM
→ Enter を押す
［画面・出力］
EQQYPARM INIT SUBSYSTEM ZWS1
EQQMLIB SEQQMSG0
EQQMLOG IWA.WAPL.066.MLOG
画面・出力には EQQYPARM が含まれる。EQQYPARM を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、特殊資源の使用量と待ち操作 と CHK066 の対応を確認する。
［操作（入力）］
WAPL batch submit
COMMAND ===&gt; SUBMIT IWA.WAPL.CNTL(INIT066)
→ Enter を押す
［画面・出力］
EQQWAPL INIT COMPLETED
SUBSYSTEM ZWS1
MESSAGE LOG IWA.WAPL.066.MLOG
RETURN CODE 0000
画面・出力には EQQWAPL が含まれる。EQQWAPL を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
SDSF output browse
COMMAND ===&gt; FIND DYNLOG
→ Enter を押す
［画面・出力］
OPTIONS DYNLOG(IWA.WAPLLOG)
DYNAMIC LOG IWA.WAPLLOG.D260715.T0915A.IWAJOB066
ADVISORY MESSAGES WRITTEN
画面・出力には OPTIONS が含まれる。OPTIONS を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQYPARM が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQWAPL が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: OPTIONS が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0218"><h3>EQQMLOG 資源制御 ログ採取076</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 中級</p><p>第七十六観点 ログ採取076 では 現在計画管理 にある EQQMLOG を扱います。第七十六観点 対象は controller、tracker、WAPL などのメッセージを確認するログで、Eです。第七十六観点 特殊資源の使用量と待ち操作 を採る時点で CHK096 を明記し、変更反映の前提を守ります。第七十六観点 後続作業では同じ engine と current plan を見たことを IWA監査096で残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EQQMLOG 資源制御 ログ採取076</strong></p><p>検証目的: 現在計画管理における EQQMLOG の資源制御を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CHK096</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQMLOG の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
WAPL batch review
COMMAND ===&gt; BROWSE EQQYPARM
→ Enter を押す
［画面・出力］
EQQYPARM INIT SUBSYSTEM ZWS1
EQQMLIB SEQQMSG0
EQQMLOG IWA.WAPL.096.MLOG
画面・出力には EQQYPARM が含まれる。EQQYPARM を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、特殊資源の使用量と待ち操作 と CHK096 の対応を確認する。
［操作（入力）］
WAPL batch submit
COMMAND ===&gt; SUBMIT IWA.WAPL.CNTL(INIT096)
→ Enter を押す
［画面・出力］
EQQWAPL INIT COMPLETED
SUBSYSTEM ZWS1
MESSAGE LOG IWA.WAPL.096.MLOG
RETURN CODE 0000
画面・出力には EQQWAPL が含まれる。EQQWAPL を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
SDSF output browse
COMMAND ===&gt; FIND DYNLOG
→ Enter を押す
［画面・出力］
OPTIONS DYNLOG(IWA.WAPLLOG)
DYNAMIC LOG IWA.WAPLLOG.D260715.T0915A.IWAJOB096
ADVISORY MESSAGES WRITTEN
画面・出力には OPTIONS が含まれる。OPTIONS を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQYPARM が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQWAPL が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: OPTIONS が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0219"><h3>current plan 定義照合 導入確認031</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 中級</p><p>第三十一観点 現在計画管理 の 導入確認031 では current plan を点検します。第三十一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第三十一観点 操作番号とジョブ名を PAYROLL051 に結び付け、再表示時の照合点にします。第三十一観点 計画反映後は long-term plan との差を IWA計画051で照合します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>current plan 定義照合 導入確認031</strong></p><p>検証目的: 現在計画管理における current plan の定義照合を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL051</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; LOCATE PAYROLL051
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN OPERATIONS
ADID PAYROLL051 IADATE 260715 WS CPU07 OPNO 070 JOBNAME IWAJOB051 STATUS READY
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL051 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
Command ===&gt; S 070
→ Enter を押す
［画面・出力］
EQQMOPJT JOB DETAIL
APPLICATION PAYROLL051
WORKSTATION CPU07
OPERATION 070
JOBNAME IWAJOB051
INPUT ARRIVAL 260715 0900
画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; REFRESH
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN REFRESHED
ADID PAYROLL051 OPNO 070 STATUS READY LAST UPDATE 260715 0915
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0220"><h3>current plan 実行監視 再計画091</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 上級</p><p>第九十一観点 現在計画管理 の 再計画091 では current plan を点検します。第九十一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第九十一観点 操作番号とジョブ名を PAYROLL111 に結び付け、再表示時の照合点にします。第九十一観点 計画反映後は long-term plan との差を IWA計画111で照合します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>current plan 実行監視 再計画091</strong></p><p>検証目的: 現在計画管理における current plan の実行監視を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL111</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; LOCATE PAYROLL111
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN OPERATIONS
ADID PAYROLL111 IADATE 260715 WS CPU07 OPNO 190 JOBNAME IWAJOB111 STATUS READY
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL111 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
Command ===&gt; S 190
→ Enter を押す
［画面・出力］
EQQMOPJT JOB DETAIL
APPLICATION PAYROLL111
WORKSTATION CPU07
OPERATION 190
JOBNAME IWAJOB111
INPUT ARRIVAL 260715 0900
画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; REFRESH
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN REFRESHED
ADID PAYROLL111 OPNO 190 STATUS READY LAST UPDATE 260715 0915
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0221"><h3>current plan 状態確認 監視001</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>第一観点 current plan は IBM Workload Automation の 現在計画管理 で扱う確認点です。第一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第一観点 EQQMLOG の EQQ メッセージ と PAYROLL021 を同じ記録に残し、再実行前の Ready 変更を記録せずに原因追跡できなくなることを管理します。第一観点 確認経路は DWC、ISPF、conman、WAPL の別を IWA記録021に残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>current plan 状態確認 監視001</strong></p><p>検証目的: 現在計画管理における current plan の状態確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL021</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; LOCATE PAYROLL021
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN OPERATIONS
ADID PAYROLL021 IADATE 260715 WS CPU01 OPNO 010 JOBNAME IWAJOB021 STATUS READY
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL021 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
Command ===&gt; S 010
→ Enter を押す
［画面・出力］
EQQMOPJT JOB DETAIL
APPLICATION PAYROLL021
WORKSTATION CPU01
OPERATION 010
JOBNAME IWAJOB021
INPUT ARRIVAL 260715 0900
画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; REFRESH
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN REFRESHED
ADID PAYROLL021 OPNO 010 STATUS READY LAST UPDATE 260715 0915
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0222"><h3>current plan 計画反映 資源確認061</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 中級</p><p>第六十一観点 current plan は IBM Workload Automation の 現在計画管理 で扱う確認点です。第六十一観点 対象は 1分から21日までの詳細な実行計画として、当日のジョブストリーム、操作、依存関係、ワです。第六十一観点 EQQMLOG の EQQ メッセージ と PAYROLL081 を同じ記録に残し、ジョブログが JES から purge された後に証跡を取り逃すことを管理します。第六十一観点 確認経路は DWC、ISPF、conman、WAPL の別を IWA記録081に残します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>current plan 計画反映 資源確認061</strong></p><p>検証目的: 現在計画管理における current plan の計画反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=PAYROLL081</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、current plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; LOCATE PAYROLL081
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN OPERATIONS
ADID PAYROLL081 IADATE 260715 WS CPU01 OPNO 130 JOBNAME IWAJOB081 STATUS READY
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、EQQMLOG の EQQ メッセージ と PAYROLL081 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPJT ---------------- OPERATION JOB DETAIL -------------------
Command ===&gt; S 130
→ Enter を押す
［画面・出力］
EQQMOPJT JOB DETAIL
APPLICATION PAYROLL081
WORKSTATION CPU01
OPERATION 130
JOBNAME IWAJOB081
INPUT ARRIVAL 260715 0900
画面・出力には EQQMOPJT が含まれる。EQQMOPJT を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMOPLT ------------- OPERATIONS IN THE CURRENT PLAN -------------
Command ===&gt; REFRESH
→ Enter を押す
［画面・出力］
EQQMOPLT CURRENT PLAN REFRESHED
ADID PAYROLL081 OPNO 130 STATUS READY LAST UPDATE 260715 0915
画面・出力には EQQMOPLT が含まれる。EQQMOPLT を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQMOPLT が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMOPJT が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQMOPLT が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0223"><h3>現在計画管理 Current Plan ログとの照合 CP07</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>ログとの照合では 現在計画管理 の 計画メニュー を主操作として CP07 を判定します。時刻と対象識別子への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP07 に残します。ログとの照合を補助する 操作一覧 では OPNO を補助値として CP07 へ保存します。主判定のログとの照合では現在計画管理の 計画メニュー から EQQMTOPP を読み CP07 へ残します。証跡照合のログとの照合では現在計画管理の EQQMTOPP と OPNO を CP07 に保存します。記録対応のログとの照合では現在計画管理の ADIDとOperation Status の証跡へ CP07 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で 現在計画管理 の 計画メニュー と 操作一覧 を組み合わせる際は Current Plan が実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータという仕組みを前提にします。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMTOPP と ADIDとOperation Status を対象 CP07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 2 LISTが応答を返した時点で正常とする。応答中のEQQMTOPPの値は記録しない。EQQMLOGをEQQMTOPPと同じ判定値とみなし対象CP07の主証跡にする。Current Planの時刻と対象識別子は確認済みとして扱う。さらにSDSF browse EQQMLOG FIND APP07のEQQMLOGをEQQMTOPPと同種の値として併記する。</li><li>B. ISPF EQQMTOPP option 2 LISTのコマンド文字列だけを記録する。EQQMTOPPを含む応答行は保存しない。</li><li>C. EQQMTOPPを含む計画メニューの応答行を保存する。その応答を得るためISPF EQQMTOPP option 2 LISTを使用する。対象CP07のADIDとOperation Statusとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. Current Planの停止または再定義を実施する。その後にISPF EQQMTOPP option 2 LISTでEQQMTOPPを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 適切な判定: Cは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として操作とログを対応しCP07に残します。
機能の仕組み: ログとの照合では操作一覧を補助操作としCurrent Planの時刻と対象識別子をOPNOと対象CP07で照合します。
各候補の評価: 計画メニューと操作一覧の役割を分けるとA: 応答の有無だけではADIDとOperation Statusを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではADIDとOperation Statusを証明できない点で一次資料と一致しません、C: EQQMTOPPの実値を対象別に残す点でCP07を判定できます、D: 変更前のADIDとOperation Statusを失う点で操作一覧の範囲を越えます。結論としてログとの照合の現在計画管理で判定する対象は CP07 です。
用語の定義: ログとの照合で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP07へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan ログとの照合 CP07</strong></p><p>検証目的: 現在計画管理のCurrent Planについて操作とログを対応し、CP07のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP07の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP07 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP07の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP07 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB07 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB07 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP07を指定し、CP07の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP07
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP07 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の EQQMLOG が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0224"><h3>現在計画管理 Current Plan 代替経路の確認 CP10</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>代替経路の確認では 現在計画管理 の 計画メニュー を主操作として CP10 を判定します。主経路との役割差への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP10 に残します。代替経路の確認を補助する 操作一覧 では OPNO を補助値として CP10 へ保存します。主判定の代替経路の確認では現在計画管理の 計画メニュー から EQQMTOPP を読み CP10 へ残します。証跡照合の代替経路の確認では現在計画管理の EQQMTOPP と OPNO を CP10 に保存します。記録対応の代替経路の確認では現在計画管理の ADIDとOperation Status の証跡へ CP10 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で 現在計画管理 の 計画メニュー と 操作一覧 を実施し Current Plan の役割を確認します。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 2 LISTのコマンド文字列だけを記録する。EQQMTOPPを含む応答行は保存しない。</li><li>B. ISPF EQQMTOPP option 2 LISTとISPF EQQMTOPP option 3 OPERATIONSの対象名をそろえる。前者のEQQMTOPPをADIDとOperation Statusの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. Current Planの停止または再定義を実施する。その後にISPF EQQMTOPP option 2 LISTでEQQMTOPPを採取する。</li><li>D. ISPF パネル運用のPanel IDとOptionを確認する。その値を現在計画管理のCP10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい判定結果: Bは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として代替手段の成立を確認しCP10に残します。
運用上の背景: 代替経路の確認では操作一覧を補助操作としCurrent Planの主経路との役割差をOPNOと対象CP10で照合します。
候補別の検討: 計画メニューと操作一覧の役割を分けるとA: 入力記録だけではADIDとOperation Statusを証明できない点で一次資料と一致しません、B: 同じ対象名のEQQMTOPPを採用する点でCP10を判定できます、C: 変更前のADIDとOperation Statusを失う点で操作一覧の範囲を越えます、D: ISPF パネル運用の値ではEQQMTOPPを確認できない点でCP10の値を示しません。結論として代替経路の確認の現在計画管理で判定する対象は CP10 です。
重要用語の定義: 代替経路の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP10へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 代替経路の確認 CP10</strong></p><p>検証目的: 現在計画管理のCurrent Planについて代替手段の成立を確認し、CP10のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP10の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP10 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP10の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP10 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB10 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB10 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP10を指定し、CP10の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP10
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP10 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の EQQMLOG が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0225"><h3>現在計画管理 Current Plan 変更前の確認 CP02</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>変更前の確認では 現在計画管理 の 操作一覧 を主操作として CP02 を判定します。変更対象と非対象の境界への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP02 に残します。変更前の確認を補助する 計画ログ では EQQMLOG を補助値として CP02 へ保存します。主判定の変更前の確認では現在計画管理の 操作一覧 から OPNO を読み CP02 へ残します。証跡照合の変更前の確認では現在計画管理の OPNO と EQQMLOG を CP02 に保存します。記録対応の変更前の確認では現在計画管理の ADIDとOperation Status の証跡へ CP02 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で 現在計画管理 の 操作一覧 と 計画ログ の役割を分け 変更対象と非対象の境界 を調べます。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 3 OPERATIONSを対象名なしで実行する。一覧の先頭行をCP02の結果として記録する。</li><li>B. 対象CP02についてISPF EQQMTOPP option 3 OPERATIONSの応答からOPNOを確認する。SDSF browse EQQMLOG FIND APP02は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したISPF EQQMTOPP option 3 OPERATIONSの結果を使う。今回のSDSF browse EQQMLOG FIND APP02の結果と同一時点の証跡として比較する。</li><li>D. 保存済みのCP02の出力を再利用する。今回のISPF EQQMTOPP option 3 OPERATIONSとSDSF browse EQQMLOG FIND APP02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: Bは操作一覧で OPNO を読みADIDとOperation Statusの主値として変更前の証跡を保存しCP02に残します。
動作の背景: 変更前の確認では計画ログを補助操作としCurrent Planの変更対象と非対象の境界をEQQMLOGと対象CP02で照合します。
各選択肢の検討: 操作一覧と計画ログの役割を分けるとA: 先頭行はCP02と確定できない点で変更前の確認に合いません、B: OPNOと補助証跡の時刻を合わせる点で操作一覧に合います、C: 採取時刻が異なる点で現在計画管理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でCurrent Planに使えません。結論として変更前の確認の現在計画管理で判定する対象は CP02 です。
初出用語の定義: 変更前の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP02へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 変更前の確認 CP02</strong></p><p>検証目的: 現在計画管理のCurrent Planについて変更前の証跡を保存し、CP02のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP02の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP02 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB02 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB02 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP02を指定し、CP02の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP02
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP02 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP02の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP02 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
② ステップ2 の EQQMLOG が画面・出力に表示されること
③ ステップ3 の EQQMTOPP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0226"><h3>現在計画管理 Current Plan 変更後の確認 CP03</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>変更後の確認では 現在計画管理 の 計画ログ を主操作として CP03 を判定します。反映値と残存値への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP03 に残します。変更後の確認を補助する 計画メニュー では EQQMTOPP を補助値として CP03 へ保存します。主判定の変更後の確認では現在計画管理の 計画ログ から EQQMLOG を読み CP03 へ残します。証跡照合の変更後の確認では現在計画管理の EQQMLOG と EQQMTOPP を CP03 に保存します。記録対応の変更後の確認では現在計画管理の ADIDとOperation Status の証跡へ CP03 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で 現在計画管理 の 計画ログ と 計画メニュー を使い 変更結果を検証 します。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMLOG を読み対象 CP03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. Current Planの停止または再定義を実施する。その後にSDSF browse EQQMLOG FIND APP03でEQQMLOGを採取する。</li><li>B. ワークステーション管理のWSIDとOpen Intervalを確認する。その値を現在計画管理のCP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Current Planの反映値と残存値は確認済みとして扱う。さらにISPF EQQMTOPP option 3 OPERATIONSのOPNOをEQQMLOGと同種の値として併記する。</li><li>C. ISPF EQQMTOPP option 2 LISTで周辺状態を押さえる。その後にSDSF browse EQQMLOG FIND APP03でEQQMLOGを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. ISPF EQQMTOPP option 2 LISTが成功したためSDSF browse EQQMLOG FIND APP03のEQQMLOGも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Cは計画ログで EQQMLOG を読みADIDとOperation Statusの主値として変更結果を検証しCP03に残します。
内部の仕組み: 変更後の確認では計画メニューを補助操作としCurrent Planの反映値と残存値をEQQMTOPPと対象CP03で照合します。
誤答を含む比較: 計画ログと計画メニューの役割を分けるとA: 変更前のADIDとOperation Statusを失う点でADIDとOperation Statusを確認できません、B: ワークステーション管理の値ではEQQMLOGを確認できないうえに追加前提も不正な点で計画メニューの範囲を越えます、C: 周辺状態の後にEQQMLOGを確認する点で現在値を示します、D: 補助操作の成功ではEQQMLOGを確定できない点で変更後の確認に合いません。結論として変更後の確認の現在計画管理で判定する対象は CP03 です。
用語定義: 変更後の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP03へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 変更後の確認 CP03</strong></p><p>検証目的: 現在計画管理のCurrent Planについて変更結果を検証し、CP03のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP03を指定し、CP03の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP03
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP03 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP03の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP03 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP03の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP03 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB03 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB03 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMLOG が画面・出力に表示されること
② ステップ2 の EQQMTOPP が画面・出力に表示されること
③ ステップ3 の OPNO が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0227"><h3>現在計画管理 Current Plan 引継ぎ記録 CP09</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>引継ぎ記録では 現在計画管理 の 計画ログ を主操作として CP09 を判定します。次担当者が追跡できる証跡への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP09 に残します。引継ぎ記録を補助する 計画メニュー では EQQMTOPP を補助値として CP09 へ保存します。主判定の引継ぎ記録では現在計画管理の 計画ログ から EQQMLOG を読み CP09 へ残します。証跡照合の引継ぎ記録では現在計画管理の EQQMLOG と EQQMTOPP を CP09 に保存します。記録対応の引継ぎ記録では現在計画管理の ADIDとOperation Status の証跡へ CP09 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で 現在計画管理 の 計画ログ と 計画メニュー を使い 再現可能な記録を作成 します。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMLOG を読み対象 CP09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 対象名CP09を指定してSDSF browse EQQMLOG FIND APP09を実行する。応答中のEQQMLOGと時刻を保存する。ISPF EQQMTOPP option 2 LISTで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. ISPF EQQMTOPP option 2 LISTが成功したためSDSF browse EQQMLOG FIND APP09のEQQMLOGも正常だと推定する。主出力は保存しない。</li><li>C. SDSF browse EQQMLOG FIND APP09を対象名なしで実行する。一覧の先頭行をCP09の結果として記録する。</li><li>D. 前回保存したSDSF browse EQQMLOG FIND APP09の結果を使う。今回のISPF EQQMTOPP option 2 LISTの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用操作の理由: Aは計画ログで EQQMLOG を読みADIDとOperation Statusの主値として再現可能な記録を作成しCP09に残します。
製品内の仕組み: 引継ぎ記録では計画メニューを補助操作としCurrent Planの次担当者が追跡できる証跡をEQQMTOPPと対象CP09で照合します。
選択肢別の説明: 計画ログと計画メニューの役割を分けるとA: EQQMLOGと時刻を保存する点で現在値を示します、B: 補助操作の成功ではEQQMLOGを確定できない点で引継ぎ記録に合いません、C: 先頭行はCP09と確定できない点で計画ログを代替しません、D: 採取時刻が異なる点で現在計画管理に使いません。結論として引継ぎ記録の現在計画管理で判定する対象は CP09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP09へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 引継ぎ記録 CP09</strong></p><p>検証目的: 現在計画管理のCurrent Planについて再現可能な記録を作成し、CP09のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP09を指定し、CP09の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP09
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP09 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP09の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP09 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP09の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP09 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB09 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB09 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMLOG が画面・出力に表示されること
② ステップ2 の EQQMTOPP が画面・出力に表示されること
③ ステップ3 の OPNO が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0228"><h3>現在計画管理 Current Plan 復旧後の確認 CP06</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>復旧後の確認では 現在計画管理 の 計画ログ を主操作として CP06 を判定します。再発していないことを示す値への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP06 に残します。復旧後の確認を補助する 計画メニュー では EQQMTOPP を補助値として CP06 へ保存します。主判定の復旧後の確認では現在計画管理の 計画ログ から EQQMLOG を読み CP06 へ残します。証跡照合の復旧後の確認では現在計画管理の EQQMLOG と EQQMTOPP を CP06 に保存します。記録対応の復旧後の確認では現在計画管理の ADIDとOperation Status の証跡へ CP06 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で 現在計画管理 の 計画ログ と 計画メニュー を照合し 再発していないことを示す値 を確かめます。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMLOG を読む前に対象 CP06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. ジョブ監視のStatusとJob IDを確認する。その値を現在計画管理のCP06にも適用する。</li><li>B. SDSF browse EQQMLOG FIND APP06でEQQMLOGを取得してからISPF EQQMTOPP option 3 OPERATIONSでOPNOを照合する。CP06のADIDとOperation Statusを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. ISPF EQQMTOPP option 2 LISTが成功したためSDSF browse EQQMLOG FIND APP06のEQQMLOGも正常だと推定する。主出力は保存しない。別資源で得た状態を対象CP06へ引き継げるものとする。Current Planの再発していないことを示す値は確認済みとして扱う。さらにISPF EQQMTOPP option 3 OPERATIONSのOPNOをEQQMLOGと同種の値として併記する。</li><li>D. SDSF browse EQQMLOG FIND APP06を対象名なしで実行する。一覧の先頭行をCP06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答内容: Bは計画ログで EQQMLOG を読みADIDとOperation Statusの主値として復旧後の安定性を確認しCP06に残します。
構成上の背景: 復旧後の確認では計画メニューを補助操作としCurrent Planの再発していないことを示す値をEQQMTOPPと対象CP06で照合します。
候補ごとの理由: 計画ログと計画メニューの役割を分けるとA: ジョブ監視の値ではEQQMLOGを確認できない点で計画メニューの範囲を越えます、B: EQQMLOGとOPNOを順に照合する点で現在値を示します、C: 補助操作の成功ではEQQMLOGを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はCP06と確定できない点で計画ログを代替しません。結論として復旧後の確認の現在計画管理で判定する対象は CP06 です。
初出用語: 復旧後の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP06へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 復旧後の確認 CP06</strong></p><p>検証目的: 現在計画管理のCurrent Planについて復旧後の安定性を確認し、CP06のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP06を指定し、CP06の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP06
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP06 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP06の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP06 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP06の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP06 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB06 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB06 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMLOG が画面・出力に表示されること
② ステップ2 の EQQMTOPP が画面・出力に表示されること
③ ステップ3 の OPNO が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0229"><h3>現在計画管理 Current Plan 復旧準備 CP05</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>復旧準備では 現在計画管理 の 操作一覧 を主操作として CP05 を判定します。再開前に必要な整合性への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP05 に残します。復旧準備を補助する 計画ログ では EQQMLOG を補助値として CP05 へ保存します。主判定の復旧準備では現在計画管理の 操作一覧 から OPNO を読み CP05 へ残します。証跡照合の復旧準備では現在計画管理の OPNO と EQQMLOG を CP05 に保存します。記録対応の復旧準備では現在計画管理の ADIDとOperation Status の証跡へ CP05 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で 現在計画管理 の 操作一覧 と 計画ログ を用い 復旧条件を確認 します。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。OPNO で対象 CP05 の ADIDとOperation Status を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずISPF EQQMTOPP option 3 OPERATIONSを実行する。OPNOを保存する。差分はSDSF browse EQQMLOG FIND APP05の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したISPF EQQMTOPP option 3 OPERATIONSの結果を使う。今回のSDSF browse EQQMLOG FIND APP05の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのCP05の出力を再利用する。今回のISPF EQQMTOPP option 3 OPERATIONSとSDSF browse EQQMLOG FIND APP05は実行済みとして扱う。</li><li>D. SDSF browse EQQMLOG FIND APP05のEQQMLOGをADIDとOperation Statusの主判定に採用する。ISPF EQQMTOPP option 3 OPERATIONSの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 選定理由: Aは操作一覧で OPNO を読みADIDとOperation Statusの主値として復旧条件を確認しCP05に残します。
処理の仕組み: 復旧準備では計画ログを補助操作としCurrent Planの再開前に必要な整合性をEQQMLOGと対象CP05で照合します。
選択結果の内訳: 操作一覧と計画ログの役割を分けるとA: 変更前のOPNOを保存する点で操作一覧に合います、B: 採取時刻が異なる点で現在計画管理に使いません、C: 過去出力では今回の復旧準備を示せない点でCurrent Planに使えません、D: EQQMLOGはOPNOを代替しないうえに追加前提も不正な点でCP05を採用できません。結論として復旧準備の現在計画管理で判定する対象は CP05 です。
用語の説明: 復旧準備で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP05へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 復旧準備 CP05</strong></p><p>検証目的: 現在計画管理のCurrent Planについて復旧条件を確認し、CP05のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP05の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP05 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB05 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB05 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP05を指定し、CP05の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP05
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP05 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP05の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP05 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
② ステップ2 の EQQMLOG が画面・出力に表示されること
③ ステップ3 の EQQMTOPP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0230"><h3>現在計画管理 Current Plan 構成監査 CP08</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>構成監査では 現在計画管理 の 操作一覧 を主操作として CP08 を判定します。定義値と稼働値の一致への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP08 に残します。構成監査を補助する 計画ログ では EQQMLOG を補助値として CP08 へ保存します。主判定の構成監査では現在計画管理の 操作一覧 から OPNO を読み CP08 へ残します。証跡照合の構成監査では現在計画管理の OPNO と EQQMLOG を CP08 に保存します。記録対応の構成監査では現在計画管理の ADIDとOperation Status の証跡へ CP08 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で 現在計画管理 の 操作一覧 と 計画ログ の役割を分け 定義値と稼働値の一致 を調べます。Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータです。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのCP08の出力を再利用する。今回のISPF EQQMTOPP option 3 OPERATIONSとSDSF browse EQQMLOG FIND APP08は実行済みとして扱う。</li><li>B. SDSF browse EQQMLOG FIND APP08のEQQMLOGをADIDとOperation Statusの主判定に採用する。ISPF EQQMTOPP option 3 OPERATIONSの応答は採取対象から外す。</li><li>C. ISPF EQQMTOPP option 2 LISTのEQQMTOPPをOPNOと同義の成功表示として扱う。ISPF EQQMTOPP option 3 OPERATIONSは実行しない。</li><li>D. SDSF browse EQQMLOG FIND APP08の結果だけでは確定しない。ISPF EQQMTOPP option 3 OPERATIONSのOPNOを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 技術上の正答: Dは操作一覧で OPNO を読みADIDとOperation Statusの主値として構成差分を監査しCP08に残します。
実行時の背景: 構成監査では計画ログを補助操作としCurrent Planの定義値と稼働値の一致をEQQMLOGと対象CP08で照合します。
四つの候補の理由: 操作一覧と計画ログの役割を分けるとA: 過去出力では今回の構成監査を示せない点で現在計画管理に使いません、B: EQQMLOGはOPNOを代替しない点でCurrent Planに使えません、C: EQQMTOPPとOPNOは確認項目が異なる点でCP08を採用できません、D: OPNOを主証跡として区別する点で主証跡になります。結論として構成監査の現在計画管理で判定する対象は CP08 です。
初出語定義: 構成監査で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP08へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 構成監査 CP08</strong></p><p>検証目的: 現在計画管理のCurrent Planについて構成差分を監査し、CP08のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP08の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP08 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB08 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB08 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP08を指定し、CP08の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP08
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP08 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP08の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP08 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
② ステップ2 の EQQMLOG が画面・出力に表示されること
③ ステップ3 の EQQMTOPP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0231"><h3>現在計画管理 Current Plan 通常状態の確認 CP01</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>通常状態の確認では 現在計画管理 の 計画メニュー を主操作として CP01 を判定します。基準値と現在値の差への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP01 に残します。通常状態の確認を補助する 操作一覧 では OPNO を補助値として CP01 へ保存します。主判定の通常状態の確認では現在計画管理の 計画メニュー から EQQMTOPP を読み CP01 へ残します。証跡照合の通常状態の確認では現在計画管理の EQQMTOPP と OPNO を CP01 に保存します。記録対応の通常状態の確認では現在計画管理の ADIDとOperation Status の証跡へ CP01 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で 現在計画管理 の 計画メニュー と 操作一覧 を組み合わせる際は Current Plan が実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータという仕組みを前提にします。長期計画の予定を現在計画の実行状態と誤認する危険があります。EQQMTOPP と ADIDとOperation Status を対象 CP01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF EQQMTOPP option 2 LISTを先に実行する。対象CP01のEQQMTOPPをADIDとOperation Statusとして記録する。続いてISPF EQQMTOPP option 3 OPERATIONSで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. ISPF EQQMTOPP option 3 OPERATIONSのOPNOをADIDとOperation Statusの主判定に採用する。ISPF EQQMTOPP option 2 LISTの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. SDSF browse EQQMLOG FIND APP01のEQQMLOGをEQQMTOPPと同義の成功表示として扱う。ISPF EQQMTOPP option 2 LISTは実行しない。</li><li>D. ISPF EQQMTOPP option 2 LISTが応答を返した時点で正常とする。応答中のEQQMTOPPの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: Aは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として通常状態を確定しCP01に残します。
背景・仕組み: 通常状態の確認では操作一覧を補助操作としCurrent Planの基準値と現在値の差をOPNOと対象CP01で照合します。
選択肢の理由: 計画メニューと操作一覧の役割を分けるとA: EQQMTOPPを主値として補助結果と照合する点で正答です、B: OPNOはEQQMTOPPを代替しないうえに追加前提も不正な点でCP01を採用できません、C: EQQMLOGとEQQMTOPPは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではADIDとOperation Statusを判定できない点で一次資料と一致しません。結論として通常状態の確認の現在計画管理で判定する対象は CP01 です。
用語の初出定義: 通常状態の確認で使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP01へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 通常状態の確認 CP01</strong></p><p>検証目的: 現在計画管理のCurrent Planについて通常状態を確定し、CP01のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP01の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP01 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP01の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP01 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB01 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB01 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP01を指定し、CP01の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP01
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP01 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の EQQMLOG が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0232"><h3>現在計画管理 Current Plan 障害切り分け CP04</h3><p class="kb-meta">分類: 現在計画管理 ・ 難易度: 初級</p><p>障害切り分けでは 現在計画管理 の 計画メニュー を主操作として CP04 を判定します。最初に失敗した処理への注意として「長期計画の予定を現在計画の実行状態と誤認する危険があります」を CP04 に残します。障害切り分けを補助する 操作一覧 では OPNO を補助値として CP04 へ保存します。主判定の障害切り分けでは現在計画管理の 計画メニュー から EQQMTOPP を読み CP04 へ残します。証跡照合の障害切り分けでは現在計画管理の EQQMTOPP と OPNO を CP04 に保存します。記録対応の障害切り分けでは現在計画管理の ADIDとOperation Status の証跡へ CP04 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで 現在計画管理 の 計画メニュー と 操作一覧 を実施し Current Plan の役割を確認します。長期計画の予定を現在計画の実行状態と誤認する危険があります。対象 CP04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse EQQMLOG FIND APP04のEQQMLOGをEQQMTOPPと同義の成功表示として扱う。ISPF EQQMTOPP option 2 LISTは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. ISPF EQQMTOPP option 2 LISTが応答を返した時点で正常とする。応答中のEQQMTOPPの値は記録しない。</li><li>C. ISPF EQQMTOPP option 2 LISTのコマンド文字列だけを記録する。EQQMTOPPを含む応答行は保存しない。</li><li>D. ISPF EQQMTOPP option 2 LISTの出力でCP04とEQQMTOPPが同じ応答にあることを確認する。ADIDとOperation Statusをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: Dは計画メニューで EQQMTOPP を読みADIDとOperation Statusの主値として障害範囲を限定しCP04に残します。
技術的背景: 障害切り分けでは操作一覧を補助操作としCurrent Planの最初に失敗した処理をOPNOと対象CP04で照合します。
四択の評価: 計画メニューと操作一覧の役割を分けるとA: EQQMLOGとEQQMTOPPは確認項目が異なるうえに追加前提も不正な点でCP04を採用できません、B: 応答の有無だけではADIDとOperation Statusを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではADIDとOperation Statusを証明できない点で一次資料と一致しません、D: CP04とEQQMTOPPを同じ応答で結ぶ点でCP04を判定できます。結論として障害切り分けの現在計画管理で判定する対象は CP04 です。
初出語の意味: 障害切り分けで使う Current Plan は実行対象のオカレンス、操作、依存関係、ワークステーション状態を直近の計画期間について保持するデータを表しADIDとOperation Statusを判定する際にCP04へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画管理 Current Plan 障害切り分け CP04</strong></p><p>検証目的: 現在計画管理のCurrent Planについて障害範囲を限定し、CP04のADIDとOperation Statusを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象CP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 2 LISTを指定し、CP04の計画メニューを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 2 LIST
→ Enter を押す
［画面・出力］
EQQMTOPP - MODIFYING THE CURRENT PLAN
2 LIST - List existing occurrences for further processing
Application ID APP04 Input Arrival 260715 1400 Status Started
画面・出力にあるEQQMTOPPを読み、ADIDとOperation Statusと対象CP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へISPF EQQMTOPP option 3 OPERATIONSを指定し、CP04の操作一覧を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF EQQMTOPP option 3 OPERATIONS
→ Enter を押す
［画面・出力］
ADID APP04 IA 260715 1400
OPNO 010 WS CPU1 JOBNAME JOB04 STATUS C
OPNO 020 WS CPU1 JOBNAME JOBB04 STATUS R
画面・出力にあるOPNOを読み、ADIDとOperation Statusと対象CP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの現在計画管理を確認する入力画面です。COMMAND入力口へSDSF browse EQQMLOG FIND APP04を指定し、CP04の計画ログを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQMLOG FIND APP04
→ Enter を押す
［画面・出力］
EQQMLOG CURRENT PLAN OCCURRENCE APP04 IA 260715 1400 UPDATED
画面・出力にあるEQQMLOGを読み、ADIDとOperation Statusと対象CP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQMTOPP が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の EQQMLOG が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


## 監査


<section class="kb-item" id="c15-i0233"><h3>AUDIT 初期化ステートメント</h3><p class="kb-meta">分類: 監査 ・ 難易度: 中級</p><p>IBM Workload Automation の 監査で扱うAUDIT 初期化ステートメントは、Z Workload Scheduler のファイル変更を監査ログに残すための設定です。どのファイルのどのアクセスを記録するかを指定できます。JCL やスケジュール定義の変更管理では監査対象を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認の初期化ステートメントで作業スケジューラーの運用確認を行います。AUDIT 初期化ステートメントの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IBM Workload Automationと無関係な一覧で監査確認の初期化ステートメントを確認した扱いにする。</li><li>B. EQQZ045I の有無を確認せず監査確認の初期化ステートメントを正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. AUDIT 初期化ステートメントの属性行を読まず監査確認の初期化ステートメントの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では AUDIT 初期化ステートメント は「IBM Workload Automationで AUDIT 初期化ステートメントの扱いを記録する監査確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では AUDIT 初期化ステートメントの表示結果と EQQZ045I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では AUDIT 初期化ステートメントの使い方を出典欄から追跡し、資料名は監査確認資料です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AUDIT 初期化ステートメント</strong></p><p>検証目的: 監査確認の初期化ステートメントについて、IBM Workload Automation の 監査で扱う AUDIT 初期化ステートメントは、Z Workload Scheduler のファイル変更を監査ログに残すたに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、監査確認の初期化ステートメントの確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にAUDIT 初期化ステートメントを指定し、OSKB010019の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND AUDIT 初期化ステートメント
CASE OSKB010019
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM AUDIT 初期化ステートメント
CASE OSKB010019
SOURCE IBM Workload Automation
AUDIT 初期化ステートメントとOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010019を同じ出力で読み、監査確認の初期化ステートメントの根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010019
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010019
COMMAND ===&gt; OPSTAT
OPERATION OSKB010019 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の AUDIT 初期化ステートメント と OSKB010019 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 監査ログと EQQMLOG


<section class="kb-item" id="c15-i0234"><h3>agent for z/OS system command 変更反映 資源確認029</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 中級</p><p>第二十九観点 z/OS agent command は IBM Workload Automation の 監査ログと EQQMLOG で扱う確認点です。第二十九観点 対象は z/OS system command で agent for z/OS の staです。第二十九観点 採取値 EQQ038 を計画表とログの両方で読み、採取時刻をそろえます。第二十九観点 採取後は DWC 表示と ISPF 表示の差を IWA比較049に分けます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>agent for z/OS system command 変更反映 資源確認029</strong></p><p>検証目的: 監査ログと EQQMLOGにおける agent for z/OS system command の変更反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ038</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、agent for z/OS system command の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /S EQQTRK
→ Enter を押す
［画面・出力］
EQQFSW1I WRITER TASK INITIALIZED FOR CPU05
EQQMLOG 049 TRACKER START CHECK
画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ038 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQFCC1I
→ Enter を押す
［画面・出力］
EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
TRACKER CPU05 CONNECTED TO CONTROLLER ZWS1
画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQTRK,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
TRACKER CPU05 EVENT QUEUE NORMAL
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0235"><h3>agent for z/OS system command 状態確認 監視089</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>第八十九観点 z/OS agent command は IBM Workload Automation の 監査ログと EQQMLOG で扱う確認点です。第八十九観点 対象は z/OS system command で agent for z/OS の staです。第八十九観点 採取値 EQQ018 を計画表とログの両方で読み、採取時刻をそろえます。第八十九観点 採取後は DWC 表示と ISPF 表示の差を IWA比較109に分けます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>agent for z/OS system command 状態確認 監視089</strong></p><p>検証目的: 監査ログと EQQMLOGにおける agent for z/OS system command の状態確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ018</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、agent for z/OS system command の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /S EQQTRK
→ Enter を押す
［画面・出力］
EQQFSW1I WRITER TASK INITIALIZED FOR CPU05
EQQMLOG 109 TRACKER START CHECK
画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ018 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQFCC1I
→ Enter を押す
［画面・出力］
EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
TRACKER CPU05 CONNECTED TO CONTROLLER ZWS1
画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQTRK,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
TRACKER CPU05 EVENT QUEUE NORMAL
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0236"><h3>agent for z/OS system command 障害切分け 再計画059</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 中級</p><p>第五十九観点 監査ログと EQQMLOG の 再計画059 では z/OS agent command を点検します。第五十九観点 対象は z/OS system command で agent for z/OS の staです。第五十九観点 待ち状態がある時は current plan の ADID/IADATE/OPNO と EQQ068 の時刻差を確認します。第五十九観点 ジョブログは JES の purge 前に IWAログ079へ転記します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>agent for z/OS system command 障害切分け 再計画059</strong></p><p>検証目的: 監査ログと EQQMLOGにおける agent for z/OS system command の障害切分けを机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=EQQ068</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、agent for z/OS system command の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /S EQQTRK
→ Enter を押す
［画面・出力］
EQQFSW1I WRITER TASK INITIALIZED FOR CPU11
EQQMLOG 079 TRACKER START CHECK
画面・出力には EQQFSW1I が含まれる。EQQFSW1I を読み取り、Dynamic Workload Console と ISPF の対象 engine を取り違えることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、current plan の ADID/IADATE/OPNO と EQQ068 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQFCC1I
→ Enter を押す
［画面・出力］
EQQFCC1I COMMUNICATION COMPLETED SUCCESSFULLY
TRACKER CPU11 CONNECTED TO CONTROLLER ZWS1
画面・出力には EQQFCC1I が含まれる。EQQFCC1I を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQTRK,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQTRK,STATUS
TRACKER CPU11 EVENT QUEUE NORMAL
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQFSW1I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQFCC1I が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0237"><h3>run cycle ログ確認 照合074</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 中級</p><p>第七十四観点 run cycle の 照合074 は IBM Workload Automation の 監査ログと EQQMLOG に属します。第七十四観点 対象は アプリケーションをいつ計画へ載せるかを決める周期条件で、カレンダーと入力到着時刻と合です。第七十四観点 IWA094 の確認では conman showjobs の Job Stream と Job 状態 を起点に、CPU02 と対象 engine を照合します。第七十四観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡094として整理します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>run cycle ログ確認 照合074</strong></p><p>検証目的: 監査ログと EQQMLOGにおける run cycle のログ確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU02</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、run cycle の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL094.IWAJOB094
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL094
Job: IWAJOB094
Workstation: CPU02
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU02 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL094
→ Enter を押す
［画面・出力］
Schedule PAYROLL094 submitted
Instance 2607150900 queued for workstation CPU02
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL094.IWAJOB094
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL094
Job: IWAJOB094
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0238"><h3>run cycle 再実行判断 ログ採取044</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 中級</p><p>第四十四観点 ログ採取044 では 監査ログと EQQMLOG にある run cycle を扱います。第四十四観点 対象は アプリケーションをいつ計画へ載せるかを決める周期条件で、カレンダーと入力到着時刻と合です。第四十四観点 DWC と ISPF の結果を分け、CPU08 の記録先を明確にします。第四十四観点 資源待ちがあれば special resource 名を IWA資源064へ記録します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>run cycle 再実行判断 ログ採取044</strong></p><p>検証目的: 監査ログと EQQMLOGにおける run cycle の再実行判断を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU08</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、run cycle の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL064.IWAJOB064
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL064
Job: IWAJOB064
Workstation: CPU08
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU08 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL064
→ Enter を押す
［画面・出力］
Schedule PAYROLL064 submitted
Instance 2607150900 queued for workstation CPU08
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL064.IWAJOB064
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL064
Job: IWAJOB064
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0239"><h3>run cycle 実行監視 再実行014</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 初級</p><p>第十四観点 run cycle の 再実行014 は IBM Workload Automation の 監査ログと EQQMLOG に属します。第十四観点 対象は アプリケーションをいつ計画へ載せるかを決める周期条件で、カレンダーと入力到着時刻と合です。第十四観点 IWA034 の確認では conman showjobs の Job Stream と Job 状態 を起点に、CPU02 と対象 engine を照合します。第十四観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡034として整理します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>run cycle 実行監視 再実行014</strong></p><p>検証目的: 監査ログと EQQMLOGにおける run cycle の実行監視を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CPU02</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、run cycle の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL034.IWAJOB034
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL034
Job: IWAJOB034
Workstation: CPU02
Status: SUCC
Return Code: 0
画面・出力には Stream が含まれる。Stream を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、conman showjobs の Job Stream と Job 状態 と CPU02 の対応を確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman submit sched PAYROLL034
→ Enter を押す
［画面・出力］
Schedule PAYROLL034 submitted
Instance 2607150900 queued for workstation CPU02
画面・出力には Schedule が含まれる。Schedule を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Workload Scheduler command line
Command ===&gt; conman showjobs PAYROLL034.IWAJOB034
→ Enter を押す
［画面・出力］
Job Stream: PAYROLL034
Job: IWAJOB034
Status: READY
Dependencies: satisfied
画面・出力には Stream が含まれる。Stream を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: Stream が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: Schedule が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: Stream が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0240"><h3>監査ログと EQQMLOG EQQMLOG ログとの照合 EQQ07</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>ログとの照合では 監査ログと EQQMLOG の ログ参照 を主操作として EQQ07 を判定します。時刻と対象識別子への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ07 に残します。ログとの照合を補助する ADID検索 では OPNO を補助値として EQQ07 へ保存します。主判定のログとの照合では監査ログの ログ参照 から EQQN013I を読み EQQ07 へ残します。証跡照合のログとの照合では監査ログの EQQN013I と OPNO を EQQ07 に保存します。記録対応のログとの照合では監査ログの Message IDとADID の証跡へ EQQ07 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で 監査ログと EQQMLOG の ログ参照 と ADID検索 を用い 操作とログを対応 します。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。EQQN013I で対象 EQQ07 の Message IDとADID を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. EQQN013Iを含むログ参照の応答行を保存する。その応答を得るためSDSF browse EQQCONT DD EQQMLOGを使用する。対象EQQ07のMessage IDとADIDとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. SDSF browse EQQCONT DD EQQMLOGが応答を返した時点で正常とする。応答中のEQQN013Iの値は記録しない。RETURNをEQQN013Iと同じ判定値とみなし対象EQQ07の主証跡にする。</li><li>C. SDSF browse EQQCONT DD EQQMLOGのコマンド文字列だけを記録する。EQQN013Iを含む応答行は保存しない。</li><li>D. EQQMLOGの停止または再定義を実施する。その後にSDSF browse EQQCONT DD EQQMLOGでEQQN013Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: Aはログ参照で EQQN013I を読みMessage IDとADIDの主値として操作とログを対応しEQQ07に残します。
機能の仕組み: ログとの照合ではADID検索を補助操作としEQQMLOGの時刻と対象識別子をOPNOと対象EQQ07で照合します。
各候補の評価: ログ参照とADID検索の役割を分けるとA: EQQN013Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではMessage IDとADIDを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではMessage IDとADIDを証明できない点でMessage IDとADIDを確認できません、D: 変更前のMessage IDとADIDを失う点でADID検索の範囲を越えます。結論としてログとの照合の監査ログで判定する対象は EQQ07 です。
用語の定義: ログとの照合で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ07へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG ログとの照合 EQQ07</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて操作とログを対応し、EQQ07のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ07のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP07を指定し、EQQ07のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP07
→ Enter を押す
［画面・出力］
EQQMLOG APP07 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ07の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の RETURN が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0241"><h3>監査ログと EQQMLOG EQQMLOG 代替経路の確認 EQQ10</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>代替経路の確認では 監査ログと EQQMLOG の ログ参照 を主操作として EQQ10 を判定します。主経路との役割差への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ10 に残します。代替経路の確認を補助する ADID検索 では OPNO を補助値として EQQ10 へ保存します。主判定の代替経路の確認では監査ログの ログ参照 から EQQN013I を読み EQQ10 へ残します。証跡照合の代替経路の確認では監査ログの EQQN013I と OPNO を EQQ10 に保存します。記録対応の代替経路の確認では監査ログの Message IDとADID の証跡へ EQQ10 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で 監査ログと EQQMLOG の ログ参照 と ADID検索 の役割を分け 主経路との役割差 を調べます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。対象 EQQ10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse EQQCONT DD EQQMLOGのコマンド文字列だけを記録する。EQQN013Iを含む応答行は保存しない。</li><li>B. EQQMLOGの停止または再定義を実施する。その後にSDSF browse EQQCONT DD EQQMLOGでEQQN013Iを採取する。</li><li>C. ジョブストリーム運用のInput ArrivalとStatusを確認する。その値を監査ログと EQQMLOGのEQQ10にも適用する。</li><li>D. SDSF browse EQQCONT DD EQQMLOGとSDSF EQQMLOG FIND APP10の対象名をそろえる。前者のEQQN013IをMessage IDとADIDの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: Dはログ参照で EQQN013I を読みMessage IDとADIDの主値として代替手段の成立を確認しEQQ10に残します。
運用上の背景: 代替経路の確認ではADID検索を補助操作としEQQMLOGの主経路との役割差をOPNOと対象EQQ10で照合します。
候補別の検討: ログ参照とADID検索の役割を分けるとA: 入力記録だけではMessage IDとADIDを証明できない点で一次資料と一致しません、B: 変更前のMessage IDとADIDを失う点でMessage IDとADIDを確認できません、C: ジョブストリーム運用の値ではEQQN013Iを確認できない点でADID検索の範囲を越えます、D: 同じ対象名のEQQN013Iを採用する点で現在値を示します。結論として代替経路の確認の監査ログで判定する対象は EQQ10 です。
重要用語の定義: 代替経路の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ10へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 代替経路の確認 EQQ10</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて代替手段の成立を確認し、EQQ10のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ10のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP10を指定し、EQQ10のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP10
→ Enter を押す
［画面・出力］
EQQMLOG APP10 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ10の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の RETURN が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0242"><h3>監査ログと EQQMLOG EQQMLOG 変更前の確認 EQQ02</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>変更前の確認では 監査ログと EQQMLOG の ADID検索 を主操作として EQQ02 を判定します。変更対象と非対象の境界への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ02 に残します。変更前の確認を補助する 日次計画結果 では RETURN を補助値として EQQ02 へ保存します。主判定の変更前の確認では監査ログの ADID検索 から OPNO を読み EQQ02 へ残します。証跡照合の変更前の確認では監査ログの OPNO と RETURN を EQQ02 に保存します。記録対応の変更前の確認では監査ログの Message IDとADID の証跡へ EQQ02 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で 監査ログと EQQMLOG の ADID検索 と 日次計画結果 を照合し 変更対象と非対象の境界 を確かめます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。OPNO を読む前に対象 EQQ02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. SDSF EQQMLOG FIND APP02を対象名なしで実行する。一覧の先頭行をEQQ02の結果として記録する。</li><li>B. 前回保存したSDSF EQQMLOG FIND APP02の結果を使う。今回のSDSF browse SYSPRINT FIND RETURN CODEの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのEQQ02の出力を再利用する。今回のSDSF EQQMLOG FIND APP02とSDSF browse SYSPRINT FIND RETURN CODEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象EQQ02についてSDSF EQQMLOG FIND APP02の応答からOPNOを確認する。SDSF browse SYSPRINT FIND RETURN CODEは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用理由: DはADID検索で OPNO を読みMessage IDとADIDの主値として変更前の証跡を保存しEQQ02に残します。
動作の背景: 変更前の確認では日次計画結果を補助操作としEQQMLOGの変更対象と非対象の境界をRETURNと対象EQQ02で照合します。
各選択肢の検討: ADID検索と日次計画結果の役割を分けるとA: 先頭行はEQQ02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でADID検索を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で監査ログと EQQMLOGに使いません、D: OPNOと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の監査ログで判定する対象は EQQ02 です。
初出用語の定義: 変更前の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ02へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 変更前の確認 EQQ02</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて変更前の証跡を保存し、EQQ02のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP02を指定し、EQQ02のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP02
→ Enter を押す
［画面・出力］
EQQMLOG APP02 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ02の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ02のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
② ステップ2 の RETURN が画面・出力に表示されること
③ ステップ3 の EQQN013I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0243"><h3>監査ログと EQQMLOG EQQMLOG 変更後の確認 EQQ03</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>変更後の確認では 監査ログと EQQMLOG の 日次計画結果 を主操作として EQQ03 を判定します。反映値と残存値への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ03 に残します。変更後の確認を補助する ログ参照 では EQQN013I を補助値として EQQ03 へ保存します。主判定の変更後の確認では監査ログの 日次計画結果 から RETURN を読み EQQ03 へ残します。証跡照合の変更後の確認では監査ログの RETURN と EQQN013I を EQQ03 に保存します。記録対応の変更後の確認では監査ログの Message IDとADID の証跡へ EQQ03 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で 監査ログと EQQMLOG の 日次計画結果 と ログ参照 を組み合わせる際は EQQMLOG がcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログという仕組みを前提にします。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。RETURN と Message IDとADID を対象 EQQ03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. SDSF browse EQQCONT DD EQQMLOGで周辺状態を押さえる。その後にSDSF browse SYSPRINT FIND RETURN CODEでRETURNを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. EQQMLOGの停止または再定義を実施する。その後にSDSF browse SYSPRINT FIND RETURN CODEでRETURNを採取する。</li><li>C. 監査ログと EQQMLOGのMessage IDとADIDを確認する。その値を監査ログと EQQMLOGのEQQ03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。EQQMLOGの反映値と残存値は確認済みとして扱う。さらにSDSF EQQMLOG FIND APP03のOPNOをRETURNと同種の値として併記する。</li><li>D. SDSF browse EQQCONT DD EQQMLOGが成功したためSDSF browse SYSPRINT FIND RETURN CODEのRETURNも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答の根拠: Aは日次計画結果で RETURN を読みMessage IDとADIDの主値として変更結果を検証しEQQ03に残します。
内部の仕組み: 変更後の確認ではログ参照を補助操作としEQQMLOGの反映値と残存値をEQQN013Iと対象EQQ03で照合します。
誤答を含む比較: 日次計画結果とログ参照の役割を分けるとA: 周辺状態の後にRETURNを確認する点でEQQ03を判定できます、B: 変更前のMessage IDとADIDを失う点でログ参照の範囲を越えます、C: 監査ログと EQQMLOGの値ではRETURNを確認できないうえに追加前提も不正な点でEQQ03の値を示しません、D: 補助操作の成功ではRETURNを確定できない点で変更後の確認に合いません。結論として変更後の確認の監査ログで判定する対象は EQQ03 です。
用語定義: 変更後の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ03へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 変更後の確認 EQQ03</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて変更結果を検証し、EQQ03のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ03の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ03のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP03を指定し、EQQ03のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP03
→ Enter を押す
［画面・出力］
EQQMLOG APP03 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RETURN が画面・出力に表示されること
② ステップ2 の EQQN013I が画面・出力に表示されること
③ ステップ3 の OPNO が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0244"><h3>監査ログと EQQMLOG EQQMLOG 引継ぎ記録 EQQ09</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>引継ぎ記録では 監査ログと EQQMLOG の 日次計画結果 を主操作として EQQ09 を判定します。次担当者が追跡できる証跡への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ09 に残します。引継ぎ記録を補助する ログ参照 では EQQN013I を補助値として EQQ09 へ保存します。主判定の引継ぎ記録では監査ログの 日次計画結果 から RETURN を読み EQQ09 へ残します。証跡照合の引継ぎ記録では監査ログの RETURN と EQQN013I を EQQ09 に保存します。記録対応の引継ぎ記録では監査ログの Message IDとADID の証跡へ EQQ09 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で 監査ログと EQQMLOG の 日次計画結果 と ログ参照 を組み合わせる際は EQQMLOG がcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログという仕組みを前提にします。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。RETURN と Message IDとADID を対象 EQQ09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. SDSF browse EQQCONT DD EQQMLOGが成功したためSDSF browse SYSPRINT FIND RETURN CODEのRETURNも正常だと推定する。主出力は保存しない。</li><li>B. SDSF browse SYSPRINT FIND RETURN CODEを対象名なしで実行する。一覧の先頭行をEQQ09の結果として記録する。</li><li>C. 対象名EQQ09を指定してSDSF browse SYSPRINT FIND RETURN CODEを実行する。応答中のRETURNと時刻を保存する。SDSF browse EQQCONT DD EQQMLOGで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSDSF browse SYSPRINT FIND RETURN CODEの結果を使う。今回のSDSF browse EQQCONT DD EQQMLOGの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: Cは日次計画結果で RETURN を読みMessage IDとADIDの主値として再現可能な記録を作成しEQQ09に残します。
製品内の仕組み: 引継ぎ記録ではログ参照を補助操作としEQQMLOGの次担当者が追跡できる証跡をEQQN013Iと対象EQQ09で照合します。
選択肢別の説明: 日次計画結果とログ参照の役割を分けるとA: 補助操作の成功ではRETURNを確定できない点でEQQ09の値を示しません、B: 先頭行はEQQ09と確定できない点で引継ぎ記録に合いません、C: RETURNと時刻を保存する点で日次計画結果に合います、D: 採取時刻が異なる点で監査ログと EQQMLOGに使いません。結論として引継ぎ記録の監査ログで判定する対象は EQQ09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ09へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 引継ぎ記録 EQQ09</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて再現可能な記録を作成し、EQQ09のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ09の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ09のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP09を指定し、EQQ09のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP09
→ Enter を押す
［画面・出力］
EQQMLOG APP09 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RETURN が画面・出力に表示されること
② ステップ2 の EQQN013I が画面・出力に表示されること
③ ステップ3 の OPNO が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0245"><h3>監査ログと EQQMLOG EQQMLOG 復旧後の確認 EQQ06</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>復旧後の確認では 監査ログと EQQMLOG の 日次計画結果 を主操作として EQQ06 を判定します。再発していないことを示す値への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ06 に残します。復旧後の確認を補助する ログ参照 では EQQN013I を補助値として EQQ06 へ保存します。主判定の復旧後の確認では監査ログの 日次計画結果 から RETURN を読み EQQ06 へ残します。証跡照合の復旧後の確認では監査ログの RETURN と EQQN013I を EQQ06 に保存します。記録対応の復旧後の確認では監査ログの Message IDとADID の証跡へ EQQ06 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で 監査ログと EQQMLOG の 日次計画結果 と ログ参照 を実施し EQQMLOG の役割を確認します。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。対象 EQQ06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 長期計画管理のRun DateとInput Arrivalを確認する。その値を監査ログと EQQMLOGのEQQ06にも適用する。</li><li>B. SDSF browse EQQCONT DD EQQMLOGが成功したためSDSF browse SYSPRINT FIND RETURN CODEのRETURNも正常だと推定する。主出力は保存しない。別資源で得た状態を対象EQQ06へ引き継げるものとする。</li><li>C. SDSF browse SYSPRINT FIND RETURN CODEを対象名なしで実行する。一覧の先頭行をEQQ06の結果として記録する。</li><li>D. SDSF browse SYSPRINT FIND RETURN CODEでRETURNを取得してからSDSF EQQMLOG FIND APP06でOPNOを照合する。EQQ06のMessage IDとADIDを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答内容: Dは日次計画結果で RETURN を読みMessage IDとADIDの主値として復旧後の安定性を確認しEQQ06に残します。
構成上の背景: 復旧後の確認ではログ参照を補助操作としEQQMLOGの再発していないことを示す値をEQQN013Iと対象EQQ06で照合します。
候補ごとの理由: 日次計画結果とログ参照の役割を分けるとA: 長期計画管理の値ではRETURNを確認できない点でログ参照の範囲を越えます、B: 補助操作の成功ではRETURNを確定できないうえに追加前提も不正な点でEQQ06の値を示しません、C: 先頭行はEQQ06と確定できない点で復旧後の確認に合いません、D: RETURNとOPNOを順に照合する点で日次計画結果に合います。結論として復旧後の確認の監査ログで判定する対象は EQQ06 です。
初出用語: 復旧後の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ06へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 復旧後の確認 EQQ06</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて復旧後の安定性を確認し、EQQ06のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ06の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ06のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP06を指定し、EQQ06のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP06
→ Enter を押す
［画面・出力］
EQQMLOG APP06 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RETURN が画面・出力に表示されること
② ステップ2 の EQQN013I が画面・出力に表示されること
③ ステップ3 の OPNO が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0246"><h3>監査ログと EQQMLOG EQQMLOG 復旧準備 EQQ05</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>復旧準備では 監査ログと EQQMLOG の ADID検索 を主操作として EQQ05 を判定します。再開前に必要な整合性への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ05 に残します。復旧準備を補助する 日次計画結果 では RETURN を補助値として EQQ05 へ保存します。主判定の復旧準備では監査ログの ADID検索 から OPNO を読み EQQ05 へ残します。証跡照合の復旧準備では監査ログの OPNO と RETURN を EQQ05 に保存します。記録対応の復旧準備では監査ログの Message IDとADID の証跡へ EQQ05 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で 監査ログと EQQMLOG の ADID検索 と 日次計画結果 を使い 復旧条件を確認 します。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。OPNO を読み対象 EQQ05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したSDSF EQQMLOG FIND APP05の結果を使う。今回のSDSF browse SYSPRINT FIND RETURN CODEの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのEQQ05の出力を再利用する。今回のSDSF EQQMLOG FIND APP05とSDSF browse SYSPRINT FIND RETURN CODEは実行済みとして扱う。</li><li>C. 変更を加えずSDSF EQQMLOG FIND APP05を実行する。OPNOを保存する。差分はSDSF browse SYSPRINT FIND RETURN CODEの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをMessage IDとADIDの主判定に採用する。SDSF EQQMLOG FIND APP05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 選定理由: CはADID検索で OPNO を読みMessage IDとADIDの主値として復旧条件を確認しEQQ05に残します。
処理の仕組み: 復旧準備では日次計画結果を補助操作としEQQMLOGの再開前に必要な整合性をRETURNと対象EQQ05で照合します。
選択結果の内訳: ADID検索と日次計画結果の役割を分けるとA: 採取時刻が異なる点でADID検索を代替しません、B: 過去出力では今回の復旧準備を示せない点で監査ログと EQQMLOGに使いません、C: 変更前のOPNOを保存する点で正答です、D: RETURNはOPNOを代替しないうえに追加前提も不正な点でEQQ05を採用できません。結論として復旧準備の監査ログで判定する対象は EQQ05 です。
用語の説明: 復旧準備で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ05へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 復旧準備 EQQ05</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて復旧条件を確認し、EQQ05のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP05を指定し、EQQ05のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP05
→ Enter を押す
［画面・出力］
EQQMLOG APP05 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ05の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ05のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
② ステップ2 の RETURN が画面・出力に表示されること
③ ステップ3 の EQQN013I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0247"><h3>監査ログと EQQMLOG EQQMLOG 構成監査 EQQ08</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>構成監査では 監査ログと EQQMLOG の ADID検索 を主操作として EQQ08 を判定します。定義値と稼働値の一致への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ08 に残します。構成監査を補助する 日次計画結果 では RETURN を補助値として EQQ08 へ保存します。主判定の構成監査では監査ログの ADID検索 から OPNO を読み EQQ08 へ残します。証跡照合の構成監査では監査ログの OPNO と RETURN を EQQ08 に保存します。記録対応の構成監査では監査ログの Message IDとADID の証跡へ EQQ08 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で 監査ログと EQQMLOG の ADID検索 と 日次計画結果 を照合し 定義値と稼働値の一致 を確かめます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。OPNO を読む前に対象 EQQ08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのEQQ08の出力を再利用する。今回のSDSF EQQMLOG FIND APP08とSDSF browse SYSPRINT FIND RETURN CODEは実行済みとして扱う。</li><li>B. SDSF browse SYSPRINT FIND RETURN CODEの結果だけでは確定しない。SDSF EQQMLOG FIND APP08のOPNOを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをMessage IDとADIDの主判定に採用する。SDSF EQQMLOG FIND APP08の応答は採取対象から外す。</li><li>D. SDSF browse EQQCONT DD EQQMLOGのEQQN013IをOPNOと同義の成功表示として扱う。SDSF EQQMLOG FIND APP08は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: BはADID検索で OPNO を読みMessage IDとADIDの主値として構成差分を監査しEQQ08に残します。
実行時の背景: 構成監査では日次計画結果を補助操作としEQQMLOGの定義値と稼働値の一致をRETURNと対象EQQ08で照合します。
四つの候補の理由: ADID検索と日次計画結果の役割を分けるとA: 過去出力では今回の構成監査を示せない点で監査ログと EQQMLOGに使いません、B: OPNOを主証跡として区別する点で正答です、C: RETURNはOPNOを代替しない点でEQQ08を採用できません、D: EQQN013IとOPNOは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の監査ログで判定する対象は EQQ08 です。
初出語定義: 構成監査で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ08へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 構成監査 EQQ08</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて構成差分を監査し、EQQ08のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP08を指定し、EQQ08のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP08
→ Enter を押す
［画面・出力］
EQQMLOG APP08 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ08の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ08のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の OPNO が画面・出力に表示されること
② ステップ2 の RETURN が画面・出力に表示されること
③ ステップ3 の EQQN013I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0248"><h3>監査ログと EQQMLOG EQQMLOG 通常状態の確認 EQQ01</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>通常状態の確認では 監査ログと EQQMLOG の ログ参照 を主操作として EQQ01 を判定します。基準値と現在値の差への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ01 に残します。通常状態の確認を補助する ADID検索 では OPNO を補助値として EQQ01 へ保存します。主判定の通常状態の確認では監査ログの ログ参照 から EQQN013I を読み EQQ01 へ残します。証跡照合の通常状態の確認では監査ログの EQQN013I と OPNO を EQQ01 に保存します。記録対応の通常状態の確認では監査ログの Message IDとADID の証跡へ EQQ01 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で 監査ログと EQQMLOG の ログ参照 と ADID検索 を用い 通常状態を確定 します。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。EQQN013I で対象 EQQ01 の Message IDとADID を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. SDSF EQQMLOG FIND APP01のOPNOをMessage IDとADIDの主判定に採用する。SDSF browse EQQCONT DD EQQMLOGの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをEQQN013Iと同義の成功表示として扱う。SDSF browse EQQCONT DD EQQMLOGは実行しない。</li><li>C. SDSF browse EQQCONT DD EQQMLOGを先に実行する。対象EQQ01のEQQN013IをMessage IDとADIDとして記録する。続いてSDSF EQQMLOG FIND APP01で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. SDSF browse EQQCONT DD EQQMLOGが応答を返した時点で正常とする。応答中のEQQN013Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解の説明: Cはログ参照で EQQN013I を読みMessage IDとADIDの主値として通常状態を確定しEQQ01に残します。
背景・仕組み: 通常状態の確認ではADID検索を補助操作としEQQMLOGの基準値と現在値の差をOPNOと対象EQQ01で照合します。
選択肢の理由: ログ参照とADID検索の役割を分けるとA: OPNOはEQQN013Iを代替しないうえに追加前提も不正な点でEQQMLOGに使えません、B: RETURNとEQQN013Iは確認項目が異なる点でEQQ01を採用できません、C: EQQN013Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではMessage IDとADIDを判定できない点で一次資料と一致しません。結論として通常状態の確認の監査ログで判定する対象は EQQ01 です。
用語の初出定義: 通常状態の確認で使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ01へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 通常状態の確認 EQQ01</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて通常状態を確定し、EQQ01のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ01のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP01を指定し、EQQ01のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP01
→ Enter を押す
［画面・出力］
EQQMLOG APP01 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ01の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の RETURN が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0249"><h3>監査ログと EQQMLOG EQQMLOG 障害切り分け EQQ04</h3><p class="kb-meta">分類: 監査ログと EQQMLOG ・ 難易度: 上級</p><p>障害切り分けでは 監査ログと EQQMLOG の ログ参照 を主操作として EQQ04 を判定します。最初に失敗した処理への注意として「別controllerや別計画期間のログを現在処理へ結び付ける危険があります」を EQQ04 に残します。障害切り分けを補助する ADID検索 では OPNO を補助値として EQQ04 へ保存します。主判定の障害切り分けでは監査ログの ログ参照 から EQQN013I を読み EQQ04 へ残します。証跡照合の障害切り分けでは監査ログの EQQN013I と OPNO を EQQ04 に保存します。記録対応の障害切り分けでは監査ログの Message IDとADID の証跡へ EQQ04 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで 監査ログと EQQMLOG の ログ参照 と ADID検索 の役割を分け 最初に失敗した処理 を調べます。EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログです。別controllerや別計画期間のログを現在処理へ結び付ける危険があります。対象 EQQ04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse SYSPRINT FIND RETURN CODEのRETURNをEQQN013Iと同義の成功表示として扱う。SDSF browse EQQCONT DD EQQMLOGは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. SDSF browse EQQCONT DD EQQMLOGの出力でEQQ04とEQQN013Iが同じ応答にあることを確認する。Message IDとADIDをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. SDSF browse EQQCONT DD EQQMLOGが応答を返した時点で正常とする。応答中のEQQN013Iの値は記録しない。</li><li>D. SDSF browse EQQCONT DD EQQMLOGのコマンド文字列だけを記録する。EQQN013Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい操作の説明: Bはログ参照で EQQN013I を読みMessage IDとADIDの主値として障害範囲を限定しEQQ04に残します。
技術的背景: 障害切り分けではADID検索を補助操作としEQQMLOGの最初に失敗した処理をOPNOと対象EQQ04で照合します。
四択の評価: ログ参照とADID検索の役割を分けるとA: RETURNとEQQN013Iは確認項目が異なるうえに追加前提も不正な点でEQQ04を採用できません、B: EQQ04とEQQN013Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではMessage IDとADIDを判定できない点で一次資料と一致しません、D: 入力記録だけではMessage IDとADIDを証明できない点でMessage IDとADIDを確認できません。結論として障害切り分けの監査ログで判定する対象は EQQ04 です。
初出語の意味: 障害切り分けで使う EQQMLOG はcontroller、tracker、日次計画、計画変更の主要メッセージを時系列で記録する診断ログを表しMessage IDとADIDを判定する際にEQQ04へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>監査ログと EQQMLOG EQQMLOG 障害切り分け EQQ04</strong></p><p>検証目的: 監査ログと EQQMLOGのEQQMLOGについて障害範囲を限定し、EQQ04のMessage IDとADIDを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象EQQ04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse EQQCONT DD EQQMLOGを指定し、EQQ04のログ参照を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse EQQCONT DD EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 2026-07-15 14:30 EQQN013I CURRENT PLAN DATA SET OPENED
画面・出力にあるEQQN013Iを読み、Message IDとADIDと対象EQQ04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF EQQMLOG FIND APP04を指定し、EQQ04のADID検索を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF EQQMLOG FIND APP04
→ Enter を押す
［画面・出力］
EQQMLOG APP04 IA 260715 1400 OPNO 010 STATUS COMPLETE
画面・出力にあるOPNOを読み、Message IDとADIDと対象EQQ04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの監査ログと EQQMLOGを確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND RETURN CODEを指定し、EQQ04の日次計画結果を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND RETURN CODE
→ Enter を押す
［画面・出力］
DAILY PLANNING REPORT PERIOD END 260716 2359 RETURN CODE 0000
画面・出力にあるRETURNを読み、Message IDとADIDと対象EQQ04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQN013I が画面・出力に表示されること
② ステップ2 の OPNO が画面・出力に表示されること
③ ステップ3 の RETURN が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


## 計画


<section class="kb-item" id="c15-i0250"><h3>現在計画 Current Plan</h3><p class="kb-meta">分類: 計画 ・ 難易度: 初級</p><p>IBM Workload Automation の 計画で扱う現在計画 Current Planは、現在計画は、実際に実行・追跡する対象ジョブや操作を保持する運用中の計画です。依存関係、ワークステーション、特殊資源、実行状態が含まれます。日々の運用では current plan の更新と拡張が中心になります</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認の現在計画で作業スケジューラーの運用確認を行います。現在計画 Current Planの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. IBM Workload Automationと無関係な一覧で呼出確認の現在計画を確認した扱いにする。</li><li>B. EQQZ045I の有無を確認せず呼出確認の現在計画を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. 現在計画 Current Planの属性行を読まず呼出確認の現在計画の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では現在計画 Current Plan は「IBM Workload Automationで現在計画 Current Planの扱いを記録する呼出確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では現在計画 Current Planの表示結果と EQQZ045I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では現在計画 Current Planの使い方を出典欄から追跡し、資料名は呼出確認資料です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>現在計画 Current Plan</strong></p><p>検証目的: 呼出確認の現在計画について、IBM Workload Automation の 計画で扱う現在計画 Current Planは、現在計画は、実際に実行・追跡する対象ジョブや操作を保持する運用中の計画でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、呼出確認の現在計画の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄に現在計画 Current Planを指定し、OSKB010003の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND 現在計画 Current Plan
CASE OSKB010003
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM 現在計画 Current Plan
CASE OSKB010003
SOURCE IBM Workload Automation
現在計画 Current PlanとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010003を同じ出力で読み、呼出確認の現在計画の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010003
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010003
COMMAND ===&gt; OPSTAT
OPERATION OSKB010003 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の 現在計画 Current Plan と OSKB010003 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0251"><h3>長期計画 LTP</h3><p class="kb-meta">分類: 計画 ・ 難易度: 初級</p><p>IBM Workload Automation の 計画で扱う長期計画 LTPは、長期計画は、将来の期間に実行するアプリケーションやジョブの高レベルな予定を作る計画です。数か月単位の予定や休日、サイクルを反映し、現在計画の元になります。計画変更では LTP の対象期間と反映先を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認の長期計画で長期計画 LTP の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. 長期計画 LTP の出力を取らず展開確認の長期計画の説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. OPSTAT を省略して展開確認の長期計画の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認の長期計画へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では長期計画 LTP は「展開確認の長期計画に関係する定義値と表示行を照合する展開確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では長期計画 LTP の属性行と EQQZ045I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では長期計画 LTP を IBM Workload Automationの運用手順で確認し、初出名は展開確認初出です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画 LTP</strong></p><p>検証目的: 展開確認の長期計画について、IBM Workload Automation の 計画で扱う長期計画 LTP は、長期計画は、将来の期間に実行するアプリケーションやジョブの高レベルな予定を作る計画です。数に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、展開確認の長期計画の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄に長期計画 LTPを指定し、OSKB010002の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND 長期計画 LTP
CASE OSKB010002
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM 長期計画 LTP
CASE OSKB010002
SOURCE IBM Workload Automation
長期計画 LTPとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010002を同じ出力で読み、展開確認の長期計画の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010002
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010002
COMMAND ===&gt; OPSTAT
OPERATION OSKB010002 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の 長期計画 LTP と OSKB010002 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 運用


<section class="kb-item" id="c15-i0252"><h3>Restart and cleanup</h3><p class="kb-meta">分類: 運用 ・ 難易度: 上級</p><p>IBM Workload Automation の 運用で扱うRestart and cleanupは、失敗したジョブの再実行や後片付けを支援する機能です。データセット削除、再投入条件、前回実行結果の扱いが関わります。自動化するときは安全に再実行できるジョブかどうかを確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認の運用で Restart and cleanupの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. Restart and cleanupの出力を取らず復旧確認の運用の説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. OPSTAT を省略して復旧確認の運用の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認の運用へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Restart and cleanup は「復旧確認の運用に関係する定義値と表示行を照合する復旧確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Restart and cleanupの属性行と EQQZ045I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Restart and cleanupを IBM Workload Automationの運用手順で確認し、初出名は復旧確認初出です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Restart and cleanup</strong></p><p>検証目的: 復旧確認の運用について、IBM Workload Automation の 運用で扱う Restart and cleanupは、失敗したジョブの再実行や後片付けを支援する機能です。データセット削除に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、復旧確認の運用の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にRestart and cleanuを指定し、OSKB010018の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND Restart and cleanu
CASE OSKB010018
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM Restart and cleanu
CASE OSKB010018
SOURCE IBM Workload Automation
Restart and cleanuとOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010018を同じ出力で読み、復旧確認の運用の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010018
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010018
COMMAND ===&gt; OPSTAT
OPERATION OSKB010018 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の Restart and cleanu と OSKB010018 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


<section class="kb-item" id="c15-i0253"><h3>計画の拡張</h3><p class="kb-meta">分類: 運用 ・ 難易度: 初級</p><p>IBM Workload Automation の 運用で扱う計画の拡張は、現在計画または長期計画の対象期間を先へ延ばす運用作業です。拡張を忘れると将来のジョブが計画に現れず、投入対象になりません。定期運用では拡張結果とカレンダー反映を確認します</p><p class="kb-src"><strong>出典:</strong> IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認の計画の拡張に関係する計画の拡張の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. OPSTAT で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. 計画の拡張の名称と担当者名のみを残して警告確認の計画の拡張の表示本文を確認対象に含めない。</li><li>C. 作業スケジューラー以外の画面で警告確認の計画の拡張を確認し同じ証跡として扱ったことにする。</li><li>D. EQQZ045I の有無を見ず警告確認の計画の拡張の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では計画の拡張は「計画の拡張の用途を作業スケジューラーの表示で確認する警告確認項目」と OPSTAT または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では IBM Workload Automationの計画の拡張と EQQZ045I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では計画の拡張を IBM Workload Automationで扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> 20_ZWS_Managing_Workload / 01_Overview</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>計画の拡張</strong></p><p>検証目的: 警告確認の計画の拡張について、IBM Workload Automation の 運用で扱う計画の拡張は、現在計画または長期計画の対象期間を先へ延ばす運用作業です。拡張を忘れると将来のジョブが計画に現れに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでOPSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に OPSTAT を入力し、警告確認の計画の拡張の確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; OPSTAT
COMMAND INPUTにOPSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄に計画の拡張を指定し、OSKB010017の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND 計画の拡張
CASE OSKB010017
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM 計画の拡張
CASE OSKB010017
SOURCE IBM Workload Automation
計画の拡張とOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010017を同じ出力で読み、警告確認の計画の拡張の根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; OPSTAT
CASE OSKB010017
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010017
COMMAND ===&gt; OPSTAT
OPERATION OSKB010017 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; OPSTAT が画面・出力に表示されること
② ステップ2 の 計画の拡張 と OSKB010017 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>


## 長期計画管理


<section class="kb-item" id="c15-i0254"><h3>EQQJOBSA 依存関係確認 監視017</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>第十七観点 EQQJOBSA は IBM Workload Automation の 長期計画管理 で扱う確認点です。第十七観点 対象は IBM Z Workload Scheduler の batch-job skeleです。第十七観点 採取値 CAL01 を計画表とログの両方で読み、採取時刻をそろえます。第十七観点 採取後は DWC 表示と ISPF 表示の差を IWA比較037に分けます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EQQJOBSA 依存関係確認 監視017</strong></p><p>検証目的: 長期計画管理における EQQJOBSA の依存関係確認を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CAL01</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQJOBSA の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMLTP ---------------- LONG TERM PLAN ----------------
Command ===&gt; LOCATE CAL01
→ Enter を押す
［画面・出力］
LONG TERM PLAN
CALENDAR CAL01 RUN CYCLE RCY08 APPLICATION PAYROLL037 INCLUDED
画面・出力には LONG が含まれる。LONG を読み取り、再実行前の Ready 変更を記録せずに原因追跡できなくなることを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Restart and cleanup の確認メッセージ と CAL01 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMAOCP -------- ADDING AN APPLICATION TO THE CURRENT PLAN --------
Command ===&gt; ADD PAYROLL037
→ Enter を押す
［画面・出力］
ADDING APPLICATION TO CURRENT PLAN
ADID PAYROLL037
INPUT ARRIVAL 260715 0900
OPERATIONS SELECTED
画面・出力には ADDING が含まれる。ADDING を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMMOPL -------- MODIFYING OPERATIONS IN THE CURRENT PLAN --------
Command ===&gt; OPER
→ Enter を押す
［画面・出力］
MODIFYING OPERATIONS
ADID PAYROLL037 OPNO 170 WORKSTATION CPU05 JOB IWAJOB037
画面・出力には MODIFYING が含まれる。MODIFYING を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: LONG が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: ADDING が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: MODIFYING が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0255"><h3>EQQJOBSA 変更反映 資源確認077</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 中級</p><p>第七十七観点 EQQJOBSA は IBM Workload Automation の 長期計画管理 で扱う確認点です。第七十七観点 対象は IBM Z Workload Scheduler の batch-job skeleです。第七十七観点 採取値 CAL05 を計画表とログの両方で読み、採取時刻をそろえます。第七十七観点 採取後は DWC 表示と ISPF 表示の差を IWA比較097に分けます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EQQJOBSA 変更反映 資源確認077</strong></p><p>検証目的: 長期計画管理における EQQJOBSA の変更反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CAL05</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQJOBSA の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMLTP ---------------- LONG TERM PLAN ----------------
Command ===&gt; LOCATE CAL05
→ Enter を押す
［画面・出力］
LONG TERM PLAN
CALENDAR CAL05 RUN CYCLE RCY05 APPLICATION PAYROLL097 INCLUDED
画面・出力には LONG が含まれる。LONG を読み取り、ジョブログが JES から purge された後に証跡を取り逃すことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Restart and cleanup の確認メッセージ と CAL05 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMAOCP -------- ADDING AN APPLICATION TO THE CURRENT PLAN --------
Command ===&gt; ADD PAYROLL097
→ Enter を押す
［画面・出力］
ADDING APPLICATION TO CURRENT PLAN
ADID PAYROLL097
INPUT ARRIVAL 260715 0900
OPERATIONS SELECTED
画面・出力には ADDING が含まれる。ADDING を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMMOPL -------- MODIFYING OPERATIONS IN THE CURRENT PLAN --------
Command ===&gt; OPER
→ Enter を押す
［画面・出力］
MODIFYING OPERATIONS
ADID PAYROLL097 OPNO 050 WORKSTATION CPU05 JOB IWAJOB097
画面・出力には MODIFYING が含まれる。MODIFYING を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: LONG が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: ADDING が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: MODIFYING が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0256"><h3>EQQJOBSA 資源制御 導入確認047</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 中級</p><p>第四十七観点 長期計画管理 の 導入確認047 では EQQJOBSA を点検します。第四十七観点 対象は IBM Z Workload Scheduler の batch-job skeleです。第四十七観点 待ち状態がある時は Restart and cleanup の確認メッセージ と CAL07 の時刻差を確認します。第四十七観点 ジョブログは JES の purge 前に IWAログ067へ転記します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EQQJOBSA 資源制御 導入確認047</strong></p><p>検証目的: 長期計画管理における EQQJOBSA の資源制御を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=CAL07</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、EQQJOBSA の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMLTP ---------------- LONG TERM PLAN ----------------
Command ===&gt; LOCATE CAL07
→ Enter を押す
［画面・出力］
LONG TERM PLAN
CALENDAR CAL07 RUN CYCLE RCY02 APPLICATION PAYROLL067 INCLUDED
画面・出力には LONG が含まれる。LONG を読み取り、tracker の通知遅延をジョブ障害と誤認することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Restart and cleanup の確認メッセージ と CAL07 の対応を確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMAOCP -------- ADDING AN APPLICATION TO THE CURRENT PLAN --------
Command ===&gt; ADD PAYROLL067
→ Enter を押す
［画面・出力］
ADDING APPLICATION TO CURRENT PLAN
ADID PAYROLL067
INPUT ARRIVAL 260715 0900
OPERATIONS SELECTED
画面・出力には ADDING が含まれる。ADDING を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
IBM Z Workload Scheduler ISPF
EQQMMOPL -------- MODIFYING OPERATIONS IN THE CURRENT PLAN --------
Command ===&gt; OPER
→ Enter を押す
［画面・出力］
MODIFYING OPERATIONS
ADID PAYROLL067 OPNO 230 WORKSTATION CPU11 JOB IWAJOB067
画面・出力には MODIFYING が含まれる。MODIFYING を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: LONG が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: ADDING が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: MODIFYING が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0257"><h3>long-term plan 再実行判断 ログ採取092</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 上級</p><p>第九十二観点 ログ採取092 では 長期計画管理 にある long-term plan を扱います。第九十二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第九十二観点 DWC と ISPF の結果を分け、200 の記録先を明確にします。第九十二観点 資源待ちがあれば special resource 名を IWA資源112へ記録します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>long-term plan 再実行判断 ログ採取092</strong></p><p>検証目的: 長期計画管理における long-term plan の再実行判断を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=200</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
EQQMLOG 112 CONTROLLER CHECK RECORDED
画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、WAPL のサブシステム初期化先を誤って別環境を更新することを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 200 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 112
CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
TRACKER CONNECTIONS LISTED FOR CPU08
画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,CPQRY,ADID=PAYROLL112
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
ADID PAYROLL112 OPNO 200 FOUND IN CURRENT PLAN
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0258"><h3>long-term plan 定義照合 照合002</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>第二観点 long-term plan の 照合002 は IBM Workload Automation の 長期計画管理 に属します。第二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第二観点 IWA022 の確認では Dynamic Workload Console の Monitor Jobs 表示 を起点に、020 と対象 engine を照合します。第二観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡022として整理します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>long-term plan 定義照合 照合002</strong></p><p>検証目的: 長期計画管理における long-term plan の定義照合を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=020</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
EQQMLOG 022 CONTROLLER CHECK RECORDED
画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、EQQMLOG の警告を確認せず critical path の影響を見落とすことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 020 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 022
CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
TRACKER CONNECTIONS LISTED FOR CPU02
画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,CPQRY,ADID=PAYROLL022
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
ADID PAYROLL022 OPNO 020 FOUND IN CURRENT PLAN
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0259"><h3>long-term plan 実行監視 再実行062</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 中級</p><p>第六十二観点 long-term plan の 再実行062 は IBM Workload Automation の 長期計画管理 に属します。第六十二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第六十二観点 IWA082 の確認では Dynamic Workload Console の Monitor Jobs 表示 を起点に、140 と対象 engine を照合します。第六十二観点 判断後は操作番号、ジョブ名、ログ時刻を IWA証跡082として整理します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>long-term plan 実行監視 再実行062</strong></p><p>検証目的: 長期計画管理における long-term plan の実行監視を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=140</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
EQQMLOG 082 CONTROLLER CHECK RECORDED
画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、計画に反映されていない定義変更を採用してしまうことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 140 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 082
CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
TRACKER CONNECTIONS LISTED FOR CPU02
画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,CPQRY,ADID=PAYROLL082
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
ADID PAYROLL082 OPNO 140 FOUND IN CURRENT PLAN
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0260"><h3>long-term plan 計画反映 依存確認032</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 中級</p><p>第三十二観点 依存確認032 では 長期計画管理 にある long-term plan を扱います。第三十二観点 対象は スケジューリング・データベースのアプリケーションやカレンダーをもとに期間計画を作り、です。第三十二観点 DWC と ISPF の結果を分け、080 の記録先を明確にします。第三十二観点 資源待ちがあれば special resource 名を IWA資源052へ記録します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>long-term plan 計画反映 依存確認032</strong></p><p>検証目的: 長期計画管理における long-term plan の計画反映を机上で確認する。</p><p>前提条件: IBM Workload Automation の対象 engine、サブシステム名、現在計画、EQQMLOG、権限を確認済み。対象=080</p><p>セッション環境: IBM Z Workload Scheduler ISPF / Dynamic Workload Console / z/OS console / SDSF / conman / WAPL review</p><pre class="kb-code">■ ステップ 1
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、long-term plan の対象状態を開き、計画、ジョブ、ワークステーション、ログのどれを確認しているかを固定する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,STATUS
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,STATUS
EQQMLOG 052 CONTROLLER CHECK RECORDED
画面・出力には EQQZ048I が含まれる。EQQZ048I を読み取り、特殊資源待ちをアプリケーション障害として扱うことを避けるため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、関連するログまたは詳細画面を開き、Dynamic Workload Console の Monitor Jobs 表示 と 080 の対応を確認する。
［操作（入力）］
SDSF log browse
COMMAND ===&gt; FIND EQQMLOG
→ Enter を押す
［画面・出力］
EQQMLOG 052
CONTROLLER EQQMAJOR CURRENT PLAN ACTIVE
TRACKER CONNECTIONS LISTED FOR CPU08
画面・出力には EQQMLOG が含まれる。EQQMLOG を読み取り、一次資料で示される画面またはメッセージ形式と照合する。
――――
■ ステップ 3
現在の画面は IBM Workload Automation の確認画面またはログ表示である。入力欄に対象値を指定し、再表示または後続画面で、記録した値が同じ対象に属することを確認する。
［操作（入力）］
z/OS console
COMMAND ===&gt; /F EQQMAJOR,CPQRY,ADID=PAYROLL052
→ Enter を押す
［画面・出力］
EQQZ048I A MODIFY COMMAND HAS BEEN PROCESSED. MODIFY EQQMAJOR,CPQRY
ADID PAYROLL052 OPNO 080 FOUND IN CURRENT PLAN
画面・出力には EQQZ048I が含まれる。EQQZ048I を残し、同じ手順を再実行した時の照合点にする。
――――</pre><p>合格条件: ステップ1: EQQZ048I が画面または出力に表示され、対象計画やログが取り違えられていないこと。
ステップ2: EQQMLOG が画面または出力に表示され、操作番号、ジョブ名、ログ時刻の対応が確認できること。
ステップ3: EQQZ048I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0261"><h3>長期計画管理 Long-Term Plan ログとの照合 LTP07</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>ログとの照合では 長期計画管理 の 長期計画表示 を主操作として LTP07 を判定します。時刻と対象識別子への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP07 に残します。ログとの照合を補助する 日次計画実行 では DAILY を補助値として LTP07 へ保存します。主判定のログとの照合では長期計画管理の 長期計画表示 から RUNDATE を読み LTP07 へ残します。証跡照合のログとの照合では長期計画管理の RUNDATE と DAILY を LTP07 に保存します。記録対応のログとの照合では長期計画管理の Run DateとInput Arrival の証跡へ LTP07 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で 長期計画管理 の 長期計画表示 と 日次計画実行 を用い 操作とログを対応 します。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。RUNDATE で対象 LTP07 の Run DateとInput Arrival を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. RUNDATEを含む長期計画表示の応答行を保存する。その応答を得るためISPF Long-Term Planning option DISPLAYを使用する。対象LTP07のRun DateとInput Arrivalとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. ISPF Long-Term Planning option DISPLAYが応答を返した時点で正常とする。応答中のRUNDATEの値は記録しない。EQQ0541EをRUNDATEと同じ判定値とみなし対象LTP07の主証跡にする。Long-Term Planの時刻と対象識別子は確認済みとして扱う。さらにSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRUNDATEと同種の値として併記する。</li><li>C. ISPF Long-Term Planning option DISPLAYのコマンド文字列だけを記録する。RUNDATEを含む応答行は保存しない。</li><li>D. Long-Term Planの停止または再定義を実施する。その後にISPF Long-Term Planning option DISPLAYでRUNDATEを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 適切な判定: Aは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として操作とログを対応しLTP07に残します。
機能の仕組み: ログとの照合では日次計画実行を補助操作としLong-Term Planの時刻と対象識別子をDAILYと対象LTP07で照合します。
各候補の評価: 長期計画表示と日次計画実行の役割を分けるとA: RUNDATEの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではRun DateとInput Arrivalを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではRun DateとInput Arrivalを証明できない点でRun DateとInput Arrivalを確認できません、D: 変更前のRun DateとInput Arrivalを失う点で日次計画実行の範囲を越えます。結論としてログとの照合の長期計画管理で判定する対象は LTP07 です。
用語の定義: ログとの照合で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP07へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan ログとの照合 LTP07</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて操作とログを対応し、LTP07のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP07の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP07
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP07)を指定し、LTP07の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP07)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP07の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
② ステップ2 の DAILY が画面・出力に表示されること
③ ステップ3 の EQQ0541E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0262"><h3>長期計画管理 Long-Term Plan 代替経路の確認 LTP10</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>代替経路の確認では 長期計画管理 の 長期計画表示 を主操作として LTP10 を判定します。主経路との役割差への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP10 に残します。代替経路の確認を補助する 日次計画実行 では DAILY を補助値として LTP10 へ保存します。主判定の代替経路の確認では長期計画管理の 長期計画表示 から RUNDATE を読み LTP10 へ残します。証跡照合の代替経路の確認では長期計画管理の RUNDATE と DAILY を LTP10 に保存します。記録対応の代替経路の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP10 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で 長期計画管理 の 長期計画表示 と 日次計画実行 の役割を分け 主経路との役割差 を調べます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。対象 LTP10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. ISPF Long-Term Planning option DISPLAYのコマンド文字列だけを記録する。RUNDATEを含む応答行は保存しない。</li><li>B. Long-Term Planの停止または再定義を実施する。その後にISPF Long-Term Planning option DISPLAYでRUNDATEを採取する。</li><li>C. ジョブストリーム運用のInput ArrivalとStatusを確認する。その値を長期計画管理のLTP10にも適用する。</li><li>D. ISPF Long-Term Planning option DISPLAYとSUBMIT IWA.DAILY.CNTL(DP10)の対象名をそろえる。前者のRUNDATEをRun DateとInput Arrivalの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい判定結果: Dは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として代替手段の成立を確認しLTP10に残します。
運用上の背景: 代替経路の確認では日次計画実行を補助操作としLong-Term Planの主経路との役割差をDAILYと対象LTP10で照合します。
候補別の検討: 長期計画表示と日次計画実行の役割を分けるとA: 入力記録だけではRun DateとInput Arrivalを証明できない点で一次資料と一致しません、B: 変更前のRun DateとInput Arrivalを失う点でRun DateとInput Arrivalを確認できません、C: ジョブストリーム運用の値ではRUNDATEを確認できない点で日次計画実行の範囲を越えます、D: 同じ対象名のRUNDATEを採用する点で現在値を示します。結論として代替経路の確認の長期計画管理で判定する対象は LTP10 です。
重要用語の定義: 代替経路の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP10へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 代替経路の確認 LTP10</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて代替手段の成立を確認し、LTP10のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP10の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP10
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP10)を指定し、LTP10の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP10)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP10の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
② ステップ2 の DAILY が画面・出力に表示されること
③ ステップ3 の EQQ0541E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0263"><h3>長期計画管理 Long-Term Plan 変更前の確認 LTP02</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>変更前の確認では 長期計画管理 の 日次計画実行 を主操作として LTP02 を判定します。変更対象と非対象の境界への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP02 に残します。変更前の確認を補助する 異常メッセージ では EQQ0541E を補助値として LTP02 へ保存します。主判定の変更前の確認では長期計画管理の 日次計画実行 から DAILY を読み LTP02 へ残します。証跡照合の変更前の確認では長期計画管理の DAILY と EQQ0541E を LTP02 に保存します。記録対応の変更前の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP02 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で 長期計画管理 の 日次計画実行 と 異常メッセージ を照合し 変更対象と非対象の境界 を確かめます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。DAILY を読む前に対象 LTP02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IWA.DAILY.CNTL(DP02)を対象名なしで実行する。一覧の先頭行をLTP02の結果として記録する。</li><li>B. 前回保存したSUBMIT IWA.DAILY.CNTL(DP02)の結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0541Eの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのLTP02の出力を再利用する。今回のSUBMIT IWA.DAILY.CNTL(DP02)とSDSF browse SYSPRINT FIND EQQ0541Eは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象LTP02についてSUBMIT IWA.DAILY.CNTL(DP02)の応答からDAILYを確認する。SDSF browse SYSPRINT FIND EQQ0541Eは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用理由: Dは日次計画実行で DAILY を読みRun DateとInput Arrivalの主値として変更前の証跡を保存しLTP02に残します。
動作の背景: 変更前の確認では異常メッセージを補助操作としLong-Term Planの変更対象と非対象の境界をEQQ0541Eと対象LTP02で照合します。
各選択肢の検討: 日次計画実行と異常メッセージの役割を分けるとA: 先頭行はLTP02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で日次計画実行を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点で長期計画管理に使いません、D: DAILYと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の長期計画管理で判定する対象は LTP02 です。
初出用語の定義: 変更前の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP02へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 変更前の確認 LTP02</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて変更前の証跡を保存し、LTP02のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP02)を指定し、LTP02の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP02)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP02の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP02の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP02
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DAILY が画面・出力に表示されること
② ステップ2 の EQQ0541E が画面・出力に表示されること
③ ステップ3 の APPLICATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0264"><h3>長期計画管理 Long-Term Plan 変更後の確認 LTP03</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>変更後の確認では 長期計画管理 の 異常メッセージ を主操作として LTP03 を判定します。反映値と残存値への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP03 に残します。変更後の確認を補助する 長期計画表示 では RUNDATE を補助値として LTP03 へ保存します。主判定の変更後の確認では長期計画管理の 異常メッセージ から EQQ0541E を読み LTP03 へ残します。証跡照合の変更後の確認では長期計画管理の EQQ0541E と RUNDATE を LTP03 に保存します。記録対応の変更後の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP03 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で 長期計画管理 の 異常メッセージ と 長期計画表示 を組み合わせる際は Long-Term Plan が将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データという仕組みを前提にします。空または未更新の長期計画から日次計画を作成する危険があります。EQQ0541E と Run DateとInput Arrival を対象 LTP03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF Long-Term Planning option DISPLAYで周辺状態を押さえる。その後にSDSF browse SYSPRINT FIND EQQ0541EでEQQ0541Eを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. Long-Term Planの停止または再定義を実施する。その後にSDSF browse SYSPRINT FIND EQQ0541EでEQQ0541Eを採取する。</li><li>C. 監査ログと EQQMLOGのMessage IDとADIDを確認する。その値を長期計画管理のLTP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。Long-Term Planの反映値と残存値は確認済みとして扱う。さらにSUBMIT IWA.DAILY.CNTL(DP03)のDAILYをEQQ0541Eと同種の値として併記する。</li><li>D. ISPF Long-Term Planning option DISPLAYが成功したためSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541Eも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答の根拠: Aは異常メッセージで EQQ0541E を読みRun DateとInput Arrivalの主値として変更結果を検証しLTP03に残します。
内部の仕組み: 変更後の確認では長期計画表示を補助操作としLong-Term Planの反映値と残存値をRUNDATEと対象LTP03で照合します。
誤答を含む比較: 異常メッセージと長期計画表示の役割を分けるとA: 周辺状態の後にEQQ0541Eを確認する点でLTP03を判定できます、B: 変更前のRun DateとInput Arrivalを失う点で長期計画表示の範囲を越えます、C: 監査ログと EQQMLOGの値ではEQQ0541Eを確認できないうえに追加前提も不正な点でLTP03の値を示しません、D: 補助操作の成功ではEQQ0541Eを確定できない点で変更後の確認に合いません。結論として変更後の確認の長期計画管理で判定する対象は LTP03 です。
用語定義: 変更後の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP03へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 変更後の確認 LTP03</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて変更結果を検証し、LTP03のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP03の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP03の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP03
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP03)を指定し、LTP03の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP03)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0541E が画面・出力に表示されること
② ステップ2 の APPLICATION が画面・出力に表示されること
③ ステップ3 の DAILY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0265"><h3>長期計画管理 Long-Term Plan 引継ぎ記録 LTP09</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>引継ぎ記録では 長期計画管理 の 異常メッセージ を主操作として LTP09 を判定します。次担当者が追跡できる証跡への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP09 に残します。引継ぎ記録を補助する 長期計画表示 では RUNDATE を補助値として LTP09 へ保存します。主判定の引継ぎ記録では長期計画管理の 異常メッセージ から EQQ0541E を読み LTP09 へ残します。証跡照合の引継ぎ記録では長期計画管理の EQQ0541E と RUNDATE を LTP09 に保存します。記録対応の引継ぎ記録では長期計画管理の Run DateとInput Arrival の証跡へ LTP09 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で 長期計画管理 の 異常メッセージ と 長期計画表示 を組み合わせる際は Long-Term Plan が将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データという仕組みを前提にします。空または未更新の長期計画から日次計画を作成する危険があります。EQQ0541E と Run DateとInput Arrival を対象 LTP09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. ISPF Long-Term Planning option DISPLAYが成功したためSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541Eも正常だと推定する。主出力は保存しない。</li><li>B. SDSF browse SYSPRINT FIND EQQ0541Eを対象名なしで実行する。一覧の先頭行をLTP09の結果として記録する。</li><li>C. 対象名LTP09を指定してSDSF browse SYSPRINT FIND EQQ0541Eを実行する。応答中のEQQ0541Eと時刻を保存する。ISPF Long-Term Planning option DISPLAYで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSDSF browse SYSPRINT FIND EQQ0541Eの結果を使う。今回のISPF Long-Term Planning option DISPLAYの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 採用操作の理由: Cは異常メッセージで EQQ0541E を読みRun DateとInput Arrivalの主値として再現可能な記録を作成しLTP09に残します。
製品内の仕組み: 引継ぎ記録では長期計画表示を補助操作としLong-Term Planの次担当者が追跡できる証跡をRUNDATEと対象LTP09で照合します。
選択肢別の説明: 異常メッセージと長期計画表示の役割を分けるとA: 補助操作の成功ではEQQ0541Eを確定できない点でLTP09の値を示しません、B: 先頭行はLTP09と確定できない点で引継ぎ記録に合いません、C: EQQ0541Eと時刻を保存する点で異常メッセージに合います、D: 採取時刻が異なる点で長期計画管理に使いません。結論として引継ぎ記録の長期計画管理で判定する対象は LTP09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP09へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 引継ぎ記録 LTP09</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて再現可能な記録を作成し、LTP09のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP09の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP09の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP09
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP09)を指定し、LTP09の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP09)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0541E が画面・出力に表示されること
② ステップ2 の APPLICATION が画面・出力に表示されること
③ ステップ3 の DAILY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0266"><h3>長期計画管理 Long-Term Plan 復旧後の確認 LTP06</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>復旧後の確認では 長期計画管理 の 異常メッセージ を主操作として LTP06 を判定します。再発していないことを示す値への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP06 に残します。復旧後の確認を補助する 長期計画表示 では RUNDATE を補助値として LTP06 へ保存します。主判定の復旧後の確認では長期計画管理の 異常メッセージ から EQQ0541E を読み LTP06 へ残します。証跡照合の復旧後の確認では長期計画管理の EQQ0541E と RUNDATE を LTP06 に保存します。記録対応の復旧後の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP06 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で 長期計画管理 の 異常メッセージ と 長期計画表示 を実施し Long-Term Plan の役割を確認します。空または未更新の長期計画から日次計画を作成する危険があります。対象 LTP06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 長期計画管理のRun DateとInput Arrivalを確認する。その値を長期計画管理のLTP06にも適用する。</li><li>B. ISPF Long-Term Planning option DISPLAYが成功したためSDSF browse SYSPRINT FIND EQQ0541EのEQQ0541Eも正常だと推定する。主出力は保存しない。別資源で得た状態を対象LTP06へ引き継げるものとする。</li><li>C. SDSF browse SYSPRINT FIND EQQ0541Eを対象名なしで実行する。一覧の先頭行をLTP06の結果として記録する。</li><li>D. SDSF browse SYSPRINT FIND EQQ0541EでEQQ0541Eを取得してからSUBMIT IWA.DAILY.CNTL(DP06)でDAILYを照合する。LTP06のRun DateとInput Arrivalを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正答内容: Dは異常メッセージで EQQ0541E を読みRun DateとInput Arrivalの主値として復旧後の安定性を確認しLTP06に残します。
構成上の背景: 復旧後の確認では長期計画表示を補助操作としLong-Term Planの再発していないことを示す値をRUNDATEと対象LTP06で照合します。
候補ごとの理由: 異常メッセージと長期計画表示の役割を分けるとA: 長期計画管理の値ではEQQ0541Eを確認できない点で長期計画表示の範囲を越えます、B: 補助操作の成功ではEQQ0541Eを確定できないうえに追加前提も不正な点でLTP06の値を示しません、C: 先頭行はLTP06と確定できない点で復旧後の確認に合いません、D: EQQ0541EとDAILYを順に照合する点で異常メッセージに合います。結論として復旧後の確認の長期計画管理で判定する対象は LTP06 です。
初出用語: 復旧後の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP06へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 復旧後の確認 LTP06</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて復旧後の安定性を確認し、LTP06のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP06の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP06の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP06
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP06)を指定し、LTP06の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP06)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の EQQ0541E が画面・出力に表示されること
② ステップ2 の APPLICATION が画面・出力に表示されること
③ ステップ3 の DAILY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0267"><h3>長期計画管理 Long-Term Plan 復旧準備 LTP05</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>復旧準備では 長期計画管理 の 日次計画実行 を主操作として LTP05 を判定します。再開前に必要な整合性への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP05 に残します。復旧準備を補助する 異常メッセージ では EQQ0541E を補助値として LTP05 へ保存します。主判定の復旧準備では長期計画管理の 日次計画実行 から DAILY を読み LTP05 へ残します。証跡照合の復旧準備では長期計画管理の DAILY と EQQ0541E を LTP05 に保存します。記録対応の復旧準備では長期計画管理の Run DateとInput Arrival の証跡へ LTP05 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で 長期計画管理 の 日次計画実行 と 異常メッセージ を使い 復旧条件を確認 します。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。DAILY を読み対象 LTP05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したSUBMIT IWA.DAILY.CNTL(DP05)の結果を使う。今回のSDSF browse SYSPRINT FIND EQQ0541Eの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのLTP05の出力を再利用する。今回のSUBMIT IWA.DAILY.CNTL(DP05)とSDSF browse SYSPRINT FIND EQQ0541Eは実行済みとして扱う。</li><li>C. 変更を加えずSUBMIT IWA.DAILY.CNTL(DP05)を実行する。DAILYを保存する。差分はSDSF browse SYSPRINT FIND EQQ0541Eの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRun DateとInput Arrivalの主判定に採用する。SUBMIT IWA.DAILY.CNTL(DP05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 選定理由: Cは日次計画実行で DAILY を読みRun DateとInput Arrivalの主値として復旧条件を確認しLTP05に残します。
処理の仕組み: 復旧準備では異常メッセージを補助操作としLong-Term Planの再開前に必要な整合性をEQQ0541Eと対象LTP05で照合します。
選択結果の内訳: 日次計画実行と異常メッセージの役割を分けるとA: 採取時刻が異なる点で日次計画実行を代替しません、B: 過去出力では今回の復旧準備を示せない点で長期計画管理に使いません、C: 変更前のDAILYを保存する点で正答です、D: EQQ0541EはDAILYを代替しないうえに追加前提も不正な点でLTP05を採用できません。結論として復旧準備の長期計画管理で判定する対象は LTP05 です。
用語の説明: 復旧準備で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP05へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 復旧準備 LTP05</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて復旧条件を確認し、LTP05のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP05)を指定し、LTP05の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP05)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP05の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP05の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP05
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DAILY が画面・出力に表示されること
② ステップ2 の EQQ0541E が画面・出力に表示されること
③ ステップ3 の APPLICATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0268"><h3>長期計画管理 Long-Term Plan 構成監査 LTP08</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>構成監査では 長期計画管理 の 日次計画実行 を主操作として LTP08 を判定します。定義値と稼働値の一致への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP08 に残します。構成監査を補助する 異常メッセージ では EQQ0541E を補助値として LTP08 へ保存します。主判定の構成監査では長期計画管理の 日次計画実行 から DAILY を読み LTP08 へ残します。証跡照合の構成監査では長期計画管理の DAILY と EQQ0541E を LTP08 に保存します。記録対応の構成監査では長期計画管理の Run DateとInput Arrival の証跡へ LTP08 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で 長期計画管理 の 日次計画実行 と 異常メッセージ を照合し 定義値と稼働値の一致 を確かめます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。DAILY を読む前に対象 LTP08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのLTP08の出力を再利用する。今回のSUBMIT IWA.DAILY.CNTL(DP08)とSDSF browse SYSPRINT FIND EQQ0541Eは実行済みとして扱う。</li><li>B. SDSF browse SYSPRINT FIND EQQ0541Eの結果だけでは確定しない。SUBMIT IWA.DAILY.CNTL(DP08)のDAILYを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRun DateとInput Arrivalの主判定に採用する。SUBMIT IWA.DAILY.CNTL(DP08)の応答は採取対象から外す。</li><li>D. ISPF Long-Term Planning option DISPLAYのRUNDATEをDAILYと同義の成功表示として扱う。SUBMIT IWA.DAILY.CNTL(DP08)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 技術上の正答: Bは日次計画実行で DAILY を読みRun DateとInput Arrivalの主値として構成差分を監査しLTP08に残します。
実行時の背景: 構成監査では異常メッセージを補助操作としLong-Term Planの定義値と稼働値の一致をEQQ0541Eと対象LTP08で照合します。
四つの候補の理由: 日次計画実行と異常メッセージの役割を分けるとA: 過去出力では今回の構成監査を示せない点で長期計画管理に使いません、B: DAILYを主証跡として区別する点で正答です、C: EQQ0541EはDAILYを代替しない点でLTP08を採用できません、D: RUNDATEとDAILYは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の長期計画管理で判定する対象は LTP08 です。
初出語定義: 構成監査で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP08へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 構成監査 LTP08</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて構成差分を監査し、LTP08のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP08)を指定し、LTP08の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP08)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP08の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP08の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP08
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DAILY が画面・出力に表示されること
② ステップ2 の EQQ0541E が画面・出力に表示されること
③ ステップ3 の APPLICATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0269"><h3>長期計画管理 Long-Term Plan 通常状態の確認 LTP01</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>通常状態の確認では 長期計画管理 の 長期計画表示 を主操作として LTP01 を判定します。基準値と現在値の差への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP01 に残します。通常状態の確認を補助する 日次計画実行 では DAILY を補助値として LTP01 へ保存します。主判定の通常状態の確認では長期計画管理の 長期計画表示 から RUNDATE を読み LTP01 へ残します。証跡照合の通常状態の確認では長期計画管理の RUNDATE と DAILY を LTP01 に保存します。記録対応の通常状態の確認では長期計画管理の Run DateとInput Arrival の証跡へ LTP01 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で 長期計画管理 の 長期計画表示 と 日次計画実行 を用い 通常状態を確定 します。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。RUNDATE で対象 LTP01 の Run DateとInput Arrival を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT IWA.DAILY.CNTL(DP01)のDAILYをRun DateとInput Arrivalの主判定に採用する。ISPF Long-Term Planning option DISPLAYの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRUNDATEと同義の成功表示として扱う。ISPF Long-Term Planning option DISPLAYは実行しない。</li><li>C. ISPF Long-Term Planning option DISPLAYを先に実行する。対象LTP01のRUNDATEをRun DateとInput Arrivalとして記録する。続いてSUBMIT IWA.DAILY.CNTL(DP01)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. ISPF Long-Term Planning option DISPLAYが応答を返した時点で正常とする。応答中のRUNDATEの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正解の説明: Cは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として通常状態を確定しLTP01に残します。
背景・仕組み: 通常状態の確認では日次計画実行を補助操作としLong-Term Planの基準値と現在値の差をDAILYと対象LTP01で照合します。
選択肢の理由: 長期計画表示と日次計画実行の役割を分けるとA: DAILYはRUNDATEを代替しないうえに追加前提も不正な点でLong-Term Planに使えません、B: EQQ0541EとRUNDATEは確認項目が異なる点でLTP01を採用できません、C: RUNDATEを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではRun DateとInput Arrivalを判定できない点で一次資料と一致しません。結論として通常状態の確認の長期計画管理で判定する対象は LTP01 です。
用語の初出定義: 通常状態の確認で使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP01へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 通常状態の確認 LTP01</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて通常状態を確定し、LTP01のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP01の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP01
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP01)を指定し、LTP01の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP01)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP01の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
② ステップ2 の DAILY が画面・出力に表示されること
③ ステップ3 の EQQ0541E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


<section class="kb-item" id="c15-i0270"><h3>長期計画管理 Long-Term Plan 障害切り分け LTP04</h3><p class="kb-meta">分類: 長期計画管理 ・ 難易度: 初級</p><p>障害切り分けでは 長期計画管理 の 長期計画表示 を主操作として LTP04 を判定します。最初に失敗した処理への注意として「空または未更新の長期計画から日次計画を作成する危険があります」を LTP04 に残します。障害切り分けを補助する 日次計画実行 では DAILY を補助値として LTP04 へ保存します。主判定の障害切り分けでは長期計画管理の 長期計画表示 から RUNDATE を読み LTP04 へ残します。証跡照合の障害切り分けでは長期計画管理の RUNDATE と DAILY を LTP04 に保存します。記録対応の障害切り分けでは長期計画管理の Run DateとInput Arrival の証跡へ LTP04 を結びます。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで 長期計画管理 の 長期計画表示 と 日次計画実行 の役割を分け 最初に失敗した処理 を調べます。Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データです。空または未更新の長期計画から日次計画を作成する危険があります。対象 LTP04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. SDSF browse SYSPRINT FIND EQQ0541EのEQQ0541EをRUNDATEと同義の成功表示として扱う。ISPF Long-Term Planning option DISPLAYは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. ISPF Long-Term Planning option DISPLAYの出力でLTP04とRUNDATEが同じ応答にあることを確認する。Run DateとInput Arrivalをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. ISPF Long-Term Planning option DISPLAYが応答を返した時点で正常とする。応答中のRUNDATEの値は記録しない。</li><li>D. ISPF Long-Term Planning option DISPLAYのコマンド文字列だけを記録する。RUNDATEを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 正しい操作の説明: Bは長期計画表示で RUNDATE を読みRun DateとInput Arrivalの主値として障害範囲を限定しLTP04に残します。
技術的背景: 障害切り分けでは日次計画実行を補助操作としLong-Term Planの最初に失敗した処理をDAILYと対象LTP04で照合します。
四択の評価: 長期計画表示と日次計画実行の役割を分けるとA: EQQ0541EとRUNDATEは確認項目が異なるうえに追加前提も不正な点でLTP04を採用できません、B: LTP04とRUNDATEを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではRun DateとInput Arrivalを判定できない点で一次資料と一致しません、D: 入力記録だけではRun DateとInput Arrivalを証明できない点でRun DateとInput Arrivalを確認できません。結論として障害切り分けの長期計画管理で判定する対象は LTP04 です。
初出語の意味: 障害切り分けで使う Long-Term Plan は将来の実行日、入力到着時刻、依存候補を保持し、日次計画処理が現在計画を作成する入力データを表しRun DateとInput Arrivalを判定する際にLTP04へ適用します。</p><p class="kb-src"><strong>出典:</strong> 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>長期計画管理 Long-Term Plan 障害切り分け LTP04</strong></p><p>検証目的: 長期計画管理のLong-Term Planについて障害範囲を限定し、LTP04のRun DateとInput Arrivalを実出力で確認する。</p><p>前提条件: IBM Workload Automationの参照権限を持ち、対象LTP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Workload Automationの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へISPF Long-Term Planning option DISPLAYを指定し、LTP04の長期計画表示を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; ISPF Long-Term Planning option DISPLAY
→ Enter を押す
［画面・出力］
APPLICATION APP04
RUN DATE 260716 INPUT ARRIVAL 0200
DEADLINE 260716 0600 PRIORITY 5
画面・出力にあるAPPLICATIONを読み、Run DateとInput Arrivalと対象LTP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSUBMIT IWA.DAILY.CNTL(DP04)を指定し、LTP04の日次計画実行を表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SUBMIT IWA.DAILY.CNTL(DP04)
→ Enter を押す
［画面・出力］
DAILY PLANNING STARTED
CURRENT PLAN EXTENDED THROUGH 260716 2359
RETURN CODE 0000
画面・出力にあるDAILYを読み、Run DateとInput Arrivalと対象LTP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Workload Automationの長期計画管理を確認する入力画面です。COMMAND入力口へSDSF browse SYSPRINT FIND EQQ0541Eを指定し、LTP04の異常メッセージを表示します。
［操作（入力）］
IBM Workload Automation 操作画面
COMMAND ===&gt; SDSF browse SYSPRINT FIND EQQ0541E
→ Enter を押す
［画面・出力］
EQQ0541E LONG TERM PLAN EMPTY - NO HEADER RECORD
画面・出力にあるEQQ0541Eを読み、Run DateとInput Arrivalと対象LTP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の APPLICATION が画面・出力に表示されること
② ステップ2 の DAILY が画面・出力に表示されること
③ ステップ3 の EQQ0541E が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: 01_Overview / 03_DWC_Users_Guide / 05_Scheduling_Job_Integrations / 07_Messages_and_Codes / 20_ZWS_Managing_Workload / 21_ZWS_Planning_Installation / 25_ZWS_WAPL_Users_Guide</p></div></details></section>


## その他


<section class="kb-item" id="c15-other"><h3>その他（特定項目に紐づかないQA・手順）</h3><p class="kb-meta">項目名が個別の技術項目に一致しなかったQA・手順です。</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Current plan special resource segm</strong></p><p>検証目的: 変更確認のレコードについて、IBM Workload Automation の レコードで扱う Current plan special resource segmentは、現在計画内で特殊資源の状態やに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IWA Dialogまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: IWA DialogでSRSTATを実行し、EQQZ045Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIWA Dialogのコマンド入力画面です。COMMAND INPUT ===&gt; に SRSTAT を入力し、変更確認のレコードの確認表示へ進みます。
［操作（入力）］
(IWA Dialog)
COMMAND INPUT ===&gt; SRSTAT
→ Enter を押す
［画面・出力］
(IWA Dialog)
COMMAND INPUT ===&gt; SRSTAT
COMMAND INPUTにSRSTATが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIWA Dialogの表示結果です。FIND欄にCurrent plan speciを指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(IWA Dialog Result)
COMMAND INPUT ===&gt; FIND Current plan speci
CASE OSKB010020
→ Enter を押す
［画面・出力］
(IWA Dialog Result)
ITEM Current plan speci
CASE OSKB010020
SOURCE IBM Workload Automation
Current plan speciとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIWA Dialogの詳細表示です。EQQZ045IとOSKB010020を同じ出力で読み、変更確認のレコードの根拠を記録します。
［操作（入力）］
(IWA Dialog Detail)
COMMAND INPUT ===&gt; SRSTAT
CASE OSKB010020
→ Enter を押す
［画面・出力］
IBM Z WORKLOAD SCHEDULER OSKB010020
COMMAND ===&gt; SRSTAT
OPERATION OSKB010020 STATUS C
EQQZ045I CURRENT PLAN ENTRY DISPLAYED
EQQZ045IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; SRSTAT が画面・出力に表示されること
② ステップ2 の Current plan speci と OSKB010020 が画面・出力に表示されること
③ ステップ3 の EQQZ045I と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: IBM Z Workload Scheduler Overview / Managing Workload / Planning and Installation / Driving IBM Z Workload Scheduler</p></div></details></section>
