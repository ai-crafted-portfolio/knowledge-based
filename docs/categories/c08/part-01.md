---
search:
  exclude: true
---

# ESS REC / REC NEAO — 詳細 (1/1)

[← ESS REC / REC NEAO の概要へ戻る](index.md)


## RPA監視


<section class="kb-item" id="c08-i0001"><h3>REC Webサイト 更新確認 監査020</h3><p class="kb-meta">分類: RPA監視 ・ 難易度: 中級</p><p>第二十観点 REC Webサイト は ESS REC 6 の RPA監視 で扱う管理項目です（区分第二十）（第二十観点）。第二十観点 管理上は ESS REC V6のライセンス登録やアクティベーションに関わる管理画面という値を追います（第二十観点）。第二十観点 RPA-JOB-020 を起点に設定値を戻し、特権操作の監査証跡化を点検します（第二十観点）。第二十観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録020に残します（第二十観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REC Webサイト 更新確認 監査020</strong></p><p>検証目的: RPA監視における REC Webサイト の更新確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=RPA-JOB-020</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により REC Webサイト の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=RPA-JOB-020
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 RPA-JOB-020
条件種別 正規表現
通知先 監査管理者
確認コード REC020A
画面・出力には REC020A が含まれる。REC020A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により REC Webサイト の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件20 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC020B
画面・出力には REC020B が含まれる。REC020B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により REC Webサイト の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=RPA-JOB-020
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 RPA-JOB-020
通知履歴 管理者へ送信済み
確認コード REC020C
画面・出力には REC020C が含まれる。REC020C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC020A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC020B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC020C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0002"><h3>アラート発報 レプリケーション確認 保護008</h3><p class="kb-meta">分類: RPA監視 ・ 難易度: 初級</p><p>第八観点 アラート発報 は ESS REC 6 の RPA監視 で扱う管理項目です（区分第八）（第八観点）。第八観点 管理上は 高リスク操作や異常を検知したときに管理者へ通知する機能という値を追います（第八観点）。第八観点 RPA-JOB-008、REC Webサイトのライセンス登録画面、管理ツールの表示を照合し、RPA異常検知の証跡化を確認します（第八観点）。第八観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録008に区別して残します（第八観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アラート発報 レプリケーション確認 保護008</strong></p><p>検証目的: RPA監視における アラート発報 のレプリケーション確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=RPA-JOB-008</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により アラート発報 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=RPA-JOB-008
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 RPA-JOB-008
条件種別 正規表現
通知先 監査管理者
確認コード REC008A
画面・出力には REC008A が含まれる。REC008A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により アラート発報 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件08 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC008B
画面・出力には REC008B が含まれる。REC008B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により アラート発報 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=RPA-JOB-008
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 RPA-JOB-008
通知履歴 管理者へ送信済み
確認コード REC008C
画面・出力には REC008C が含まれる。REC008C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC008A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC008B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC008C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0003"><h3>仮想アプライアンス方式 定義照合 保護032</h3><p class="kb-meta">分類: RPA監視 ・ 難易度: 中級</p><p>第三十二観点 仮想アプライアンス方式 は ESS REC 6 の RPA監視 で扱う管理項目です（区分第三十二）（第三十二観点）。第三十二観点 管理上は 提供方式によってUbuntu OSを使用する構成観点という値を追います（第三十二観点）。第三十二観点 PodmanとRHELバージョンの検証値 と RPA-JOB-032 を同じ証跡に置き、管理画面間の値合わせを管理します（第三十二観点）。第三十二観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録032から再現します（第三十二観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>仮想アプライアンス方式 定義照合 保護032</strong></p><p>検証目的: RPA監視における 仮想アプライアンス方式 の定義照合を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=RPA-JOB-032</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 仮想アプライアンス方式 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=RPA-JOB-032
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 RPA-JOB-032
条件種別 正規表現
通知先 監査管理者
確認コード REC032A
画面・出力には REC032A が含まれる。REC032A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 仮想アプライアンス方式 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件08 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC032B
画面・出力には REC032B が含まれる。REC032B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 仮想アプライアンス方式 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=RPA-JOB-032
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 RPA-JOB-032
通知履歴 管理者へ送信済み
確認コード REC032C
画面・出力には REC032C が含まれる。REC032C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC032A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC032B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC032C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## アラート通知


<section class="kb-item" id="c08-i0004"><h3>RHEL検証 レプリケーション確認 監査028</h3><p class="kb-meta">分類: アラート通知 ・ 難易度: 中級</p><p>第二十八観点 RHEL検証 は アラート通知 の障害調査で確認順序を決める対象です（第二十八観点）。第二十八観点 ESS REC 6サーバーのRed Hat Enterprise Linux上での動作確認結という説明を監査証跡と結びます（第二十八観点）。第二十八観点 ACTCODE-04028、REC Webサイトのライセンス登録画面、管理ツールの表示を照合し、操作録画とテキスト証跡の整合確認を確認します（第二十八観点）。第二十八観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録028に区別して残します（第二十八観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RHEL検証 レプリケーション確認 監査028</strong></p><p>検証目的: アラート通知における RHEL検証 のレプリケーション確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ACTCODE-04028</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により RHEL検証 の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.04 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC028A
画面・出力には REC028A が含まれる。REC028A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により RHEL検証 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC028B
画面・出力には REC028B が含まれる。REC028B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により RHEL検証 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC028C
画面・出力には REC028C が含まれる。REC028C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC028A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC028B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC028C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0005"><h3>キー打鍵情報 権限確認 監査004</h3><p class="kb-meta">分類: アラート通知 ・ 難易度: 初級</p><p>第四観点 キー打鍵情報 は アラート通知 の障害調査で確認順序を決める対象です（第四観点）。第四観点 キーボード入力を操作証跡の補助情報として扱う記録対象という説明を監査証跡と結びます（第四観点）。第四観点 画面表示文字列の検索結果 の値を ACTCODE-04004 と合わせ、特権操作の監査証跡化を記録します（第四観点）。第四観点 証跡には資料IDと確認値を併記し、REC記録004として保存します（第四観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>キー打鍵情報 権限確認 監査004</strong></p><p>検証目的: アラート通知における キー打鍵情報 の権限確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ACTCODE-04004</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により キー打鍵情報 の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.04 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC004A
画面・出力には REC004A が含まれる。REC004A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により キー打鍵情報 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC004B
画面・出力には REC004B が含まれる。REC004B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により キー打鍵情報 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC004C
画面・出力には REC004C が含まれる。REC004C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC004A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC004B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC004C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0006"><h3>休日業務検知 可用性確認 保護016</h3><p class="kb-meta">分類: アラート通知 ・ 難易度: 中級</p><p>第十六観点 休日業務検知 は アラート通知 の障害調査で確認順序を決める対象です（第十六観点）。第十六観点 休日作業を検知して働き方の実態を把握する監視観点という説明を監査証跡と結びます（第十六観点）。第十六観点 アラート通知履歴 と監査行を同じ確認票に置き、管理画面間の値合わせを説明可能にします（第十六観点）。第十六観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録016へ書きます（第十六観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>休日業務検知 可用性確認 保護016</strong></p><p>検証目的: アラート通知における 休日業務検知 の可用性確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ACTCODE-16016</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 休日業務検知 の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.16 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC016A
画面・出力には REC016A が含まれる。REC016A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 休日業務検知 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC016B
画面・出力には REC016B が含まれる。REC016B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 休日業務検知 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC016C
画面・出力には REC016C が含まれる。REC016C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC016A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC016B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC016C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0007"><h3>自社開発体制 更新確認 保護040</h3><p class="kb-meta">分類: アラート通知 ・ 難易度: 上級</p><p>第四十観点 自社開発体制 は アラート通知 の障害調査で確認順序を決める対象です（第四十観点）。第四十観点 ソースコードを自社で把握し問題切分けや修正へ対応する開発体制という説明を監査証跡と結びます（第四十観点）。第四十観点 ACTCODE-16040 を起点に設定値を戻し、ライセンス有効化情報の確認を点検します（第四十観点）。第四十観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録040に残します（第四十観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>自社開発体制 更新確認 保護040</strong></p><p>検証目的: アラート通知における 自社開発体制 の更新確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ACTCODE-16040</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 自社開発体制 の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.16 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC040A
画面・出力には REC040A が含まれる。REC040A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 自社開発体制 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC040B
画面・出力には REC040B が含まれる。REC040B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 自社開発体制 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC040C
画面・出力には REC040C が含まれる。REC040C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC040A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC040B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC040C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## クラウド対応


<section class="kb-item" id="c08-i0008"><h3>VDI操作監視 状態確認 確認011</h3><p class="kb-meta">分類: クラウド対応 ・ 難易度: 中級</p><p>第十一観点 クラウド対応 の変更作業では VDI操作監視 の現在値を先に固定します（第十一観点）。第十一観点 役割は 仮想デスクトップ利用時の操作実態を可視化する監視対象という範囲です（第十一観点）。第十一観点 Docker-CEとdocker-composeの検証値 と監査行を同じ確認票に置き、操作録画とテキスト証跡の整合確認を説明可能にします（第十一観点）。第十一観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録011へ書きます（第十一観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VDI操作監視 状態確認 確認011</strong></p><p>検証目的: クラウド対応における VDI操作監視 の状態確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REPORT-011</p><p>セッション環境: REC NEAO 管理画面 / 働き方モニタリング</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により VDI操作監視 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; モニタリング &gt; テレワーク対象=REPORT-011
→ ENTER を押す
［画面・出力］
モニタリング対象
対象 REPORT-011
VDI 操作監視 有効
DaaS 操作監視 有効
確認コード REC011A
画面・出力には REC011A が含まれる。REC011A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により VDI操作監視 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; レポート &gt; 働き方モニタリング
→ ENTER を押す
［画面・出力］
働き方モニタリングレポート
深夜残業 検知あり
休日業務 確認対象
確認コード REC011B
画面・出力には REC011B が含まれる。REC011B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により VDI操作監視 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; アラート &gt; 勤務時間外
→ ENTER を押す
［画面・出力］
勤務時間外アラート
対象 REPORT-011
通知履歴 管理者確認済み
確認コード REC011C
画面・出力には REC011C が含まれる。REC011C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC011A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC011B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC011C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0009"><h3>アクティベーションコード ログ確認 接続023</h3><p class="kb-meta">分類: クラウド対応 ・ 難易度: 中級</p><p>第二十三観点 クラウド対応 の変更作業では アクティベーションコード の現在値を先に固定します（第二十三観点）。第二十三観点 役割は ESS REC V6を有効化するために発行される4桁-4桁形式のコードという範囲です（第二十三観点）。第二十三観点 REPORT-023、操作証跡の録画一覧、管理ツールの表示を照合し、ライセンス有効化情報の確認を確認します（第二十三観点）。第二十三観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録023に区別して残します（第二十三観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アクティベーションコード ログ確認 接続023</strong></p><p>検証目的: クラウド対応における アクティベーションコード のログ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REPORT-023</p><p>セッション環境: REC NEAO 管理画面 / 働き方モニタリング</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により アクティベーションコード の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; モニタリング &gt; テレワーク対象=REPORT-023
→ ENTER を押す
［画面・出力］
モニタリング対象
対象 REPORT-023
VDI 操作監視 有効
DaaS 操作監視 有効
確認コード REC023A
画面・出力には REC023A が含まれる。REC023A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により アクティベーションコード の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; レポート &gt; 働き方モニタリング
→ ENTER を押す
［画面・出力］
働き方モニタリングレポート
深夜残業 検知あり
休日業務 確認対象
確認コード REC023B
画面・出力には REC023B が含まれる。REC023B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により アクティベーションコード の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; アラート &gt; 勤務時間外
→ ENTER を押す
［画面・出力］
勤務時間外アラート
対象 REPORT-023
通知履歴 管理者確認済み
確認コード REC023C
画面・出力には REC023C が含まれる。REC023C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC023A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC023B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC023C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0010"><h3>操作ログ管理 構成確認 確認035</h3><p class="kb-meta">分類: クラウド対応 ・ 難易度: 上級</p><p>第三十五観点 クラウド対応 の変更作業では 操作ログ管理 の現在値を先に固定します（第三十五観点）。第三十五観点 役割は 操作内容を監査手順に組み込み妥当性を点検する管理観点という範囲です（第三十五観点）。第三十五観点 REPORT-035 を起点に設定値を戻し、RPA異常検知の証跡化を点検します（第三十五観点）。第三十五観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録035に残します（第三十五観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>操作ログ管理 構成確認 確認035</strong></p><p>検証目的: クラウド対応における 操作ログ管理 の構成確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REPORT-035</p><p>セッション環境: REC NEAO 管理画面 / 働き方モニタリング</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 操作ログ管理 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; モニタリング &gt; テレワーク対象=REPORT-035
→ ENTER を押す
［画面・出力］
モニタリング対象
対象 REPORT-035
VDI 操作監視 有効
DaaS 操作監視 有効
確認コード REC035A
画面・出力には REC035A が含まれる。REC035A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 操作ログ管理 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; レポート &gt; 働き方モニタリング
→ ENTER を押す
［画面・出力］
働き方モニタリングレポート
深夜残業 検知あり
休日業務 確認対象
確認コード REC035B
画面・出力には REC035B が含まれる。REC035B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 操作ログ管理 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; アラート &gt; 勤務時間外
→ ENTER を押す
［画面・出力］
勤務時間外アラート
対象 REPORT-035
通知履歴 管理者確認済み
確認コード REC035C
画面・出力には REC035C が含まれる。REC035C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC035A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC035B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC035C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## テレワーク監視


<section class="kb-item" id="c08-i0011"><h3>Podman検証 状態確認 接続031</h3><p class="kb-meta">分類: テレワーク監視 ・ 難易度: 中級</p><p>第三十一観点 テレワーク監視 で Podman検証 は 状態確認 を点検します（運用第三十一）（第三十一観点）。第三十一観点 確認時には RHEL環境で確認されたPodmanバージョンの観点という性質を前提にします（資料第三十一）（第三十一観点）。第三十一観点 Docker-CEとdocker-composeの検証値 と監査行を同じ確認票に置き、特権操作の監査証跡化を説明可能にします（第三十一観点）。第三十一観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録031へ書きます（第三十一観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Podman検証 状態確認 接続031</strong></p><p>検証目的: テレワーク監視における Podman検証 の状態確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=Podman-07</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により Podman検証 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=Podman-07
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID Podman-07
記録種別 画面遷移
録画状態 記録済み
確認コード REC031A
画面・出力には REC031A が含まれる。REC031A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により Podman検証 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC031B
画面・出力には REC031B が含まれる。REC031B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により Podman検証 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 Podman-07
確認結果 録画と文字列情報を照合済み
確認コード REC031C
画面・出力には REC031C が含まれる。REC031C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC031A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC031B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC031C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0012"><h3>サブスクリプション契約 接続確認 確認019</h3><p class="kb-meta">分類: テレワーク監視 ・ 難易度: 中級</p><p>第十九観点 テレワーク監視 で サブスクリプション契約 は 接続確認 を点検します（運用第十九）（第十九観点）。第十九観点 確認時には 利用形態に応じてサブスクリプション型料金へ対応する管理観点という性質を前提にします（資料第十九）（第十九観点）。第十九観点 アクティベーションコード発行サイトの入力欄 の値を Podman-19 と合わせ、RPA異常検知の証跡化を記録します（第十九観点）。第十九観点 証跡には資料IDと確認値を併記し、REC記録019として保存します（第十九観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サブスクリプション契約 接続確認 確認019</strong></p><p>検証目的: テレワーク監視における サブスクリプション契約 の接続確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=Podman-19</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により サブスクリプション契約 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=Podman-19
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID Podman-19
記録種別 画面遷移
録画状態 記録済み
確認コード REC019A
画面・出力には REC019A が含まれる。REC019A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により サブスクリプション契約 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC019B
画面・出力には REC019B が含まれる。REC019B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により サブスクリプション契約 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 Podman-19
確認結果 録画と文字列情報を照合済み
確認コード REC019C
画面・出力には REC019C が含まれる。REC019C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC019A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC019B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC019C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0013"><h3>複数条件の組み合わせ セキュリティ確認 接続007</h3><p class="kb-meta">分類: テレワーク監視 ・ 難易度: 初級</p><p>第七観点 テレワーク監視 で 複数条件の組み合わせ は セキュリティ確認 を点検します（運用第七）（第七観点）。第七観点 確認時には 複数の検知条件を合わせて操作リスクを判定する設定方式という性質を前提にします（資料第七）（第七観点）。第七観点 働き方モニタリングレポート と Podman-07 を同じ証跡に置き、ライセンス有効化情報の確認を管理します（第七観点）。第七観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録007から再現します（第七観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複数条件の組み合わせ セキュリティ確認 接続007</strong></p><p>検証目的: テレワーク監視における 複数条件の組み合わせ のセキュリティ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=Podman-07</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 複数条件の組み合わせ の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=Podman-07
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID Podman-07
記録種別 画面遷移
録画状態 記録済み
確認コード REC007A
画面・出力には REC007A が含まれる。REC007A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 複数条件の組み合わせ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC007B
画面・出力には REC007B が含まれる。REC007B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 複数条件の組み合わせ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 Podman-07
確認結果 録画と文字列情報を照合済み
確認コード REC007C
画面・出力には REC007C が含まれる。REC007C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC007A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC007B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC007C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## ライセンス管理


<section class="kb-item" id="c08-i0014"><h3>インスタンスID 状態確認 構成021</h3><p class="kb-meta">分類: ライセンス管理 ・ 難易度: 中級</p><p>第二十一観点 ライセンス管理 の運用では インスタンスID を定義、ログ、画面の値と結びます（第二十一観点）。第二十一観点 アクティベーションコード発行時に入力する8桁英数字の識別情報という内容を操作結果と照合します（第二十一観点）。第二十一観点 Docker-CEとdocker-composeの検証値 と監査行を同じ確認票に置き、管理画面間の値合わせを説明可能にします（第二十一観点）。第二十一観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録021へ書きます（第二十一観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>インスタンスID 状態確認 構成021</strong></p><p>検証目的: ライセンス管理における インスタンスID の状態確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=VDI-SESSION-021</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により インスタンスID の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC21021
アクティベーション申請コード PIM-21021-A1B2-C3D4
確認コード REC021A
画面・出力には REC021A が含まれる。REC021A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により インスタンスID の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 21A21-B21
確認コード REC021B
画面・出力には REC021B が含まれる。REC021B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により インスタンスID の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC021C
画面・出力には REC021C が含まれる。REC021C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC021A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC021B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC021C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0015"><h3>特権ID操作証跡 接続確認 照合009</h3><p class="kb-meta">分類: ライセンス管理 ・ 難易度: 中級</p><p>第九観点 ライセンス管理 の運用では 特権ID操作証跡 を定義、ログ、画面の値と結びます（第九観点）。第九観点 特権IDを使った管理作業の内容を後から点検できる形で残す証跡という内容を操作結果と照合します（第九観点）。第九観点 アクティベーションコード発行サイトの入力欄 の値を VDI-SESSION-009 と合わせ、特権操作の監査証跡化を記録します（第九観点）。第九観点 証跡には資料IDと確認値を併記し、REC記録009として保存します（第九観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>特権ID操作証跡 接続確認 照合009</strong></p><p>検証目的: ライセンス管理における 特権ID操作証跡 の接続確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=VDI-SESSION-009</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 特権ID操作証跡 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC09009
アクティベーション申請コード PIM-09009-A1B2-C3D4
確認コード REC009A
画面・出力には REC009A が含まれる。REC009A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 特権ID操作証跡 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 09A09-B09
確認コード REC009B
画面・出力には REC009B が含まれる。REC009B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 特権ID操作証跡 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC009C
画面・出力には REC009C が含まれる。REC009C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC009A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC009B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC009C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0016"><h3>集積パッチ001版以降 ログ確認 照合033</h3><p class="kb-meta">分類: ライセンス管理 ・ 難易度: 中級</p><p>第三十三観点 ライセンス管理 の運用では 集積パッチ001版以降 を定義、ログ、画面の値と結びます（第三十三観点）。第三十三観点 稼働OS拡張後のESS REC 6サーバー版を区別する更新観点という内容を操作結果と照合します（第三十三観点）。第三十三観点 VDI-SESSION-033、操作証跡の録画一覧、管理ツールの表示を照合し、操作録画とテキスト証跡の整合確認を確認します（第三十三観点）。第三十三観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録033に区別して残します（第三十三観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>集積パッチ001版以降 ログ確認 照合033</strong></p><p>検証目的: ライセンス管理における 集積パッチ001版以降 のログ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=VDI-SESSION-033</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 集積パッチ001版以降 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC09033
アクティベーション申請コード PIM-09033-A1B2-C3D4
確認コード REC033A
画面・出力には REC033A が含まれる。REC033A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 集積パッチ001版以降 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 09A09-B33
確認コード REC033B
画面・出力には REC033B が含まれる。REC033B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 集積パッチ001版以降 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC033C
画面・出力には REC033C が含まれる。REC033C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC033A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC033B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC033C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## リモート保守監査


<section class="kb-item" id="c08-i0017"><h3>docker-compose検証 更新確認 復旧030</h3><p class="kb-meta">分類: リモート保守監査 ・ 難易度: 中級</p><p>第三十観点 docker-compose検証 は ESS REC 6 の リモート保守監査 を説明するための項目です（第三十観点）。第三十観点 資料上は ESS REC 6サーバー構成で確認されたdocker-composeバージョンの観点として扱います（第三十観点）。第三十観点 DockerCE-06 を起点に設定値を戻し、RPA異常検知の証跡化を点検します（第三十観点）。第三十観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録030に残します（第三十観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>docker-compose検証 更新確認 復旧030</strong></p><p>検証目的: リモート保守監査における docker-compose検証 の更新確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=DockerCE-06</p><p>セッション環境: REC NEAO 管理画面 / RPA監視</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により docker-compose検証 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; ジョブ=DockerCE-06
→ ENTER を押す
［画面・出力］
RPA監視
ジョブ DockerCE-06
画面遷移録画 記録済み
確認コード REC030A
画面・出力には REC030A が含まれる。REC030A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により docker-compose検証 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; エラー検知
→ ENTER を押す
［画面・出力］
RPA検知条件
エラーメッセージ 検知対象
動作異常 アラート対象
確認コード REC030B
画面・出力には REC030B が含まれる。REC030B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により docker-compose検証 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; 実行結果
→ ENTER を押す
［画面・出力］
RPA実行結果
ジョブ DockerCE-06
実行結果と問題発生時の事象を確認可能
確認コード REC030C
画面・出力には REC030C が含まれる。REC030C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC030A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC030B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC030C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0018"><h3>クラウド環境対応 レプリケーション確認 点検018</h3><p class="kb-meta">分類: リモート保守監査 ・ 難易度: 中級</p><p>第十八観点 クラウド環境対応 は ESS REC 6 の リモート保守監査 を説明するための項目です（第十八観点）。第十八観点 資料上は オンプレミス以外にDaaSなどのクラウド環境へ適用する運用観点として扱います（第十八観点）。第十八観点 DockerCE-18、REC Webサイトのライセンス登録画面、管理ツールの表示を照合し、ライセンス有効化情報の確認を確認します（第十八観点）。第十八観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録018に区別して残します（第十八観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>クラウド環境対応 レプリケーション確認 点検018</strong></p><p>検証目的: リモート保守監査における クラウド環境対応 のレプリケーション確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=DockerCE-18</p><p>セッション環境: REC NEAO 管理画面 / RPA監視</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により クラウド環境対応 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; ジョブ=DockerCE-18
→ ENTER を押す
［画面・出力］
RPA監視
ジョブ DockerCE-18
画面遷移録画 記録済み
確認コード REC018A
画面・出力には REC018A が含まれる。REC018A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により クラウド環境対応 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; エラー検知
→ ENTER を押す
［画面・出力］
RPA検知条件
エラーメッセージ 検知対象
動作異常 アラート対象
確認コード REC018B
画面・出力には REC018B が含まれる。REC018B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により クラウド環境対応 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; 実行結果
→ ENTER を押す
［画面・出力］
RPA実行結果
ジョブ DockerCE-18
実行結果と問題発生時の事象を確認可能
確認コード REC018C
画面・出力には REC018C が含まれる。REC018C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC018A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC018B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC018C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0019"><h3>正規表現条件 可用性確認 復旧006</h3><p class="kb-meta">分類: リモート保守監査 ・ 難易度: 初級</p><p>第六観点 正規表現条件 は ESS REC 6 の リモート保守監査 を説明するための項目です（第六観点）。第六観点 資料上は 監視ログの文字列に対して柔軟な一致条件を設定する検知ルール要素として扱います（第六観点）。第六観点 アラート通知履歴 と監査行を同じ確認票に置き、操作録画とテキスト証跡の整合確認を説明可能にします（第六観点）。第六観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録006へ書きます（第六観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>正規表現条件 可用性確認 復旧006</strong></p><p>検証目的: リモート保守監査における 正規表現条件 の可用性確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=DockerCE-06</p><p>セッション環境: REC NEAO 管理画面 / RPA監視</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 正規表現条件 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; ジョブ=DockerCE-06
→ ENTER を押す
［画面・出力］
RPA監視
ジョブ DockerCE-06
画面遷移録画 記録済み
確認コード REC006A
画面・出力には REC006A が含まれる。REC006A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 正規表現条件 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; エラー検知
→ ENTER を押す
［画面・出力］
RPA検知条件
エラーメッセージ 検知対象
動作異常 アラート対象
確認コード REC006B
画面・出力には REC006B が含まれる。REC006B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 正規表現条件 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; 実行結果
→ ENTER を押す
［画面・出力］
RPA実行結果
ジョブ DockerCE-06
実行結果と問題発生時の事象を確認可能
確認コード REC006C
画面・出力には REC006C が含まれる。REC006C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC006A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC006B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC006C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## 動作検証


<section class="kb-item" id="c08-i0020"><h3>アクティベーション申請コード 定義照合 復旧022</h3><p class="kb-meta">分類: 動作検証 ・ 難易度: 中級</p><p>第二十二観点 アクティベーション申請コード は 動作検証 の障害調査で確認順序を決める対象です（第二十二観点）。第二十二観点 アクティベーションコード発行に使う申請コードという説明を監査証跡と結びます（第二十二観点）。第二十二観点 PodmanとRHELバージョンの検証値 と ALERT-RULE-022 を同じ証跡に置き、操作録画とテキスト証跡の整合確認を管理します（第二十二観点）。第二十二観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録022から再現します（第二十二観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アクティベーション申請コード 定義照合 復旧022</strong></p><p>検証目的: 動作検証における アクティベーション申請コード の定義照合を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ALERT-RULE-022</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により アクティベーション申請コード の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.22 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC022A
画面・出力には REC022A が含まれる。REC022A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により アクティベーション申請コード の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC022B
画面・出力には REC022B が含まれる。REC022B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により アクティベーション申請コード の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC022C
画面・出力には REC022C が含まれる。REC022C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC022A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC022B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC022C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0021"><h3>リモート保守記録 更新確認 点検010</h3><p class="kb-meta">分類: 動作検証 ・ 難易度: 中級</p><p>第十観点 リモート保守記録 は 動作検証 の障害調査で確認順序を決める対象です（第十観点）。第十観点 委託先や保守担当者によるリモート作業を監査対象として残す記録という説明を監査証跡と結びます（第十観点）。第十観点 ALERT-RULE-010 を起点に設定値を戻し、管理画面間の値合わせを点検します（第十観点）。第十観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録010に残します（第十観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リモート保守記録 更新確認 点検010</strong></p><p>検証目的: 動作検証における リモート保守記録 の更新確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ALERT-RULE-010</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により リモート保守記録 の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.10 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC010A
画面・出力には REC010A が含まれる。REC010A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により リモート保守記録 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC010B
画面・出力には REC010B が含まれる。REC010B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により リモート保守記録 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC010C
画面・出力には REC010C が含まれる。REC010C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC010A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC010B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC010C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0022"><h3>集積パッチ004版 権限確認 点検034</h3><p class="kb-meta">分類: 動作検証 ・ 難易度: 上級</p><p>第三十四観点 集積パッチ004版 は 動作検証 の障害調査で確認順序を決める対象です（第三十四観点）。第三十四観点 RHEL9.5以上とPodman5の組み合わせで必要になる適用条件という説明を監査証跡と結びます（第三十四観点）。第三十四観点 画面表示文字列の検索結果 の値を ALERT-RULE-034 と合わせ、ライセンス有効化情報の確認を記録します（第三十四観点）。第三十四観点 証跡には資料IDと確認値を併記し、REC記録034として保存します（第三十四観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>集積パッチ004版 権限確認 点検034</strong></p><p>検証目的: 動作検証における 集積パッチ004版 の権限確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=ALERT-RULE-034</p><p>セッション環境: 製品動作検証表 / サーバー要件確認</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 集積パッチ004版 の値を確認し、対象の現在値を固定する。
［操作（入力）］
動作検証表
COMMAND ===&gt; ESS REC 6 サーバー V6.1.0＋集積パッチ001版以降
→ ENTER を押す
［画面・出力］
動作検証表
Ubuntu Server 24.04.10 LTS
Docker-CE V29.3.1
docker-compose V2.40.3
確認コード REC034A
画面・出力には REC034A が含まれる。REC034A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 集積パッチ004版 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
動作検証表
COMMAND ===&gt; Red Hat Enterprise Linux
→ ENTER を押す
［画面・出力］
動作検証表
RHEL 9.6
Podman V5.4.0
docker-compose V2.40.3
確認コード REC034B
画面・出力には REC034B が含まれる。REC034B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 集積パッチ004版 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
動作検証表
COMMAND ===&gt; 注意事項
→ ENTER を押す
［画面・出力］
注意事項
RHEL9.5以上とPodman5の組み合わせでは集積パッチ004版の適用が必要
確認コード REC034C
画面・出力には REC034C が含まれる。REC034C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC034A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC034B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC034C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## 操作証跡管理


<section class="kb-item" id="c08-i0023"><h3>RPA画面遷移録画 ログ確認 構成013</h3><p class="kb-meta">分類: 操作証跡管理 ・ 難易度: 中級</p><p>第十三観点 操作証跡管理 で RPA画面遷移録画 は ログ確認 を点検します（運用第十三）（第十三観点）。第十三観点 確認時には RPA実行時の画面変化を録画し、実行結果や問題発生時の把握に使う記録という性質を前提にします（資料第十三）（第十三観点）。第十三観点 REC-AUDIT-013、操作証跡の録画一覧、管理ツールの表示を照合し、ライセンス有効化情報の確認を確認します（第十三観点）。第十三観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録013に区別して残します（第十三観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RPA画面遷移録画 ログ確認 構成013</strong></p><p>検証目的: 操作証跡管理における RPA画面遷移録画 のログ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REC-AUDIT-013</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により RPA画面遷移録画 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=REC-AUDIT-013
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID REC-AUDIT-013
記録種別 画面遷移
録画状態 記録済み
確認コード REC013A
画面・出力には REC013A が含まれる。REC013A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により RPA画面遷移録画 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC013B
画面・出力には REC013B が含まれる。REC013B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により RPA画面遷移録画 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 REC-AUDIT-013
確認結果 録画と文字列情報を照合済み
確認コード REC013C
画面・出力には REC013C が含まれる。REC013C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC013A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC013B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC013C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0024"><h3>メール発行手順 構成確認 照合025</h3><p class="kb-meta">分類: 操作証跡管理 ・ 難易度: 中級</p><p>第二十五観点 操作証跡管理 で メール発行手順 は 構成確認 を点検します（運用第二十五）（第二十五観点）。第二十五観点 確認時には Web発行が使えない場合に必要情報を送ってコードを受け取る手順という性質を前提にします（資料第二十五）（第二十五観点）。第二十五観点 REC-AUDIT-025 を起点に設定値を戻し、RPA異常検知の証跡化を点検します（第二十五観点）。第二十五観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録025に残します（第二十五観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メール発行手順 構成確認 照合025</strong></p><p>検証目的: 操作証跡管理における メール発行手順 の構成確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REC-AUDIT-025</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により メール発行手順 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=REC-AUDIT-025
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID REC-AUDIT-025
記録種別 画面遷移
録画状態 記録済み
確認コード REC025A
画面・出力には REC025A が含まれる。REC025A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により メール発行手順 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC025B
画面・出力には REC025B が含まれる。REC025B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により メール発行手順 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 REC-AUDIT-025
確認結果 録画と文字列情報を照合済み
確認コード REC025C
画面・出力には REC025C が含まれる。REC025C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC025A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC025B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC025C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0025"><h3>内部統制監査 セキュリティ確認 構成037</h3><p class="kb-meta">分類: 操作証跡管理 ・ 難易度: 上級</p><p>第三十七観点 操作証跡管理 で 内部統制監査 は セキュリティ確認 を点検します（運用第三十七）（第三十七観点）。第三十七観点 確認時には 操作証跡を用いてシステム操作の統制状況を確認する監査観点という性質を前提にします（資料第三十七）（第三十七観点）。第三十七観点 働き方モニタリングレポート と REC-AUDIT-037 を同じ証跡に置き、特権操作の監査証跡化を管理します（第三十七観点）。第三十七観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録037から再現します（第三十七観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>内部統制監査 セキュリティ確認 構成037</strong></p><p>検証目的: 操作証跡管理における 内部統制監査 のセキュリティ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REC-AUDIT-037</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 内部統制監査 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=REC-AUDIT-037
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID REC-AUDIT-037
記録種別 画面遷移
録画状態 記録済み
確認コード REC037A
画面・出力には REC037A が含まれる。REC037A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 内部統制監査 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC037B
画面・出力には REC037B が含まれる。REC037B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 内部統制監査 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 REC-AUDIT-037
確認結果 録画と文字列情報を照合済み
確認コード REC037C
画面・出力には REC037C が含まれる。REC037C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC037A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC037B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC037C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0026"><h3>画面遷移記録 状態確認 照合001</h3><p class="kb-meta">分類: 操作証跡管理 ・ 難易度: 初級</p><p>第一観点 操作証跡管理 で 画面遷移記録 は 状態確認 を点検します（運用第一）（第一観点）。第一観点 確認時には 利用者や管理者のデスクトップ操作の画面遷移を証跡として残す記録対象という性質を前提にします（資料第一）（第一観点）。第一観点 Docker-CEとdocker-composeの検証値 と監査行を同じ確認票に置き、操作録画とテキスト証跡の整合確認を説明可能にします（第一観点）。第一観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録001へ書きます（第一観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>画面遷移記録 状態確認 照合001</strong></p><p>検証目的: 操作証跡管理における 画面遷移記録 の状態確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=REC-AUDIT-001</p><p>セッション環境: ESS REC 管理画面 / 証跡検索</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 画面遷移記録 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡検索 &gt; 対象ID=REC-AUDIT-001
→ ENTER を押す
［画面・出力］
証跡検索結果
対象ID REC-AUDIT-001
記録種別 画面遷移
録画状態 記録済み
確認コード REC001A
画面・出力には REC001A が含まれる。REC001A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 画面遷移記録 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 表示文字列
→ ENTER を押す
［画面・出力］
証跡詳細
画面表示文字列 取得済み
キー打鍵情報 取得済み
プロセス記録 取得済み
確認コード REC001B
画面・出力には REC001B が含まれる。REC001B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 画面遷移記録 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 証跡詳細 &gt; 監査メモ
→ ENTER を押す
［画面・出力］
監査メモ
対象 REC-AUDIT-001
確認結果 録画と文字列情報を照合済み
確認コード REC001C
画面・出力には REC001C が含まれる。REC001C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC001A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC001B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC001C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## 検知ルール


<section class="kb-item" id="c08-i0027"><h3>Ubuntu Server検証 セキュリティ確認 確認027</h3><p class="kb-meta">分類: 検知ルール ・ 難易度: 中級</p><p>第二十七観点 検知ルール の運用では Ubuntu Server検証 を定義、ログ、画面の値と結びます（第二十七観点）。第二十七観点 ESS REC 6サーバーのUbuntu Server上での動作確認結果という内容を操作結果と照合します（第二十七観点）。第二十七観点 働き方モニタリングレポート と LICENSE-027 を同じ証跡に置き、管理画面間の値合わせを管理します（第二十七観点）。第二十七観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録027から再現します（第二十七観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Ubuntu Server検証 セキュリティ確認 確認027</strong></p><p>検証目的: 検知ルールにおける Ubuntu Server検証 のセキュリティ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=LICENSE-027</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により Ubuntu Server検証 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC03027
アクティベーション申請コード PIM-03027-A1B2-C3D4
確認コード REC027A
画面・出力には REC027A が含まれる。REC027A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により Ubuntu Server検証 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 03A03-B27
確認コード REC027B
画面・出力には REC027B が含まれる。REC027B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により Ubuntu Server検証 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC027C
画面・出力には REC027C が含まれる。REC027C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC027A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC027B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC027C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0028"><h3>永久サポート 接続確認 接続039</h3><p class="kb-meta">分類: 検知ルール ・ 難易度: 上級</p><p>第三十九観点 検知ルール の運用では 永久サポート を定義、ログ、画面の値と結びます（第三十九観点）。第三十九観点 利用継続中の旧バージョンへ保守を提供するサポート方針という内容を操作結果と照合します（第三十九観点）。第三十九観点 アクティベーションコード発行サイトの入力欄 の値を LICENSE-039 と合わせ、操作録画とテキスト証跡の整合確認を記録します（第三十九観点）。第三十九観点 証跡には資料IDと確認値を併記し、REC記録039として保存します（第三十九観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>永久サポート 接続確認 接続039</strong></p><p>検証目的: 検知ルールにおける 永久サポート の接続確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=LICENSE-039</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 永久サポート の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC15039
アクティベーション申請コード PIM-15039-A1B2-C3D4
確認コード REC039A
画面・出力には REC039A が含まれる。REC039A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 永久サポート の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 15A15-B39
確認コード REC039B
画面・出力には REC039B が含まれる。REC039B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 永久サポート の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC039C
画面・出力には REC039C が含まれる。REC039C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC039A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC039B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC039C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0029"><h3>深夜残業検知 構成確認 接続015</h3><p class="kb-meta">分類: 検知ルール ・ 難易度: 中級</p><p>第十五観点 検知ルール の運用では 深夜残業検知 を定義、ログ、画面の値と結びます（第十五観点）。第十五観点 テレワークやモバイルワークで深夜作業を検知する監視観点という内容を操作結果と照合します（第十五観点）。第十五観点 LICENSE-015 を起点に設定値を戻し、特権操作の監査証跡化を点検します（第十五観点）。第十五観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録015に残します（第十五観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>深夜残業検知 構成確認 接続015</strong></p><p>検証目的: 検知ルールにおける 深夜残業検知 の構成確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=LICENSE-015</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 深夜残業検知 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC15015
アクティベーション申請コード PIM-15015-A1B2-C3D4
確認コード REC015A
画面・出力には REC015A が含まれる。REC015A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 深夜残業検知 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 15A15-B15
確認コード REC015B
画面・出力には REC015B が含まれる。REC015B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 深夜残業検知 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC015C
画面・出力には REC015C が含まれる。REC015C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC015A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC015B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC015C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0030"><h3>画面表示文字列 ログ確認 確認003</h3><p class="kb-meta">分類: 検知ルール ・ 難易度: 初級</p><p>第三観点 検知ルール の運用では 画面表示文字列 を定義、ログ、画面の値と結びます（第三観点）。第三観点 画面上に現れる文字列を取得し、操作内容の検索や点検へ使う情報という内容を操作結果と照合します（第三観点）。第三観点 LICENSE-003、操作証跡の録画一覧、管理ツールの表示を照合し、RPA異常検知の証跡化を確認します（第三観点）。第三観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録003に区別して残します（第三観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>画面表示文字列 ログ確認 確認003</strong></p><p>検証目的: 検知ルールにおける 画面表示文字列 のログ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=LICENSE-003</p><p>セッション環境: REC Webサイト / アクティベーション</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 画面表示文字列 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; ライセンス登録
→ ENTER を押す
［画面・出力］
ライセンス登録
インスタンスID REC03003
アクティベーション申請コード PIM-03003-A1B2-C3D4
確認コード REC003A
画面・出力には REC003A が含まれる。REC003A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 画面表示文字列 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
アクティベーションコード発行サイト
COMMAND ===&gt; インスタンスIDと申請コードを入力
→ ENTER を押す
［画面・出力］
アクティベーションコード発行
入力確認 完了
アクティベーションコード 03A03-B03
確認コード REC003B
画面・出力には REC003B が含まれる。REC003B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 画面表示文字列 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC Webサイト
COMMAND ===&gt; ライセンス管理 &gt; アクティベーション
→ ENTER を押す
［画面・出力］
ライセンス状態
製品 ESS REC V6
アクティベーション 登録完了
確認コード REC003C
画面・出力には REC003C が含まれる。REC003C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC003A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC003B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC003C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## 特権アクセス監査


<section class="kb-item" id="c08-i0031"><h3>Docker-CE検証 接続確認 構成029</h3><p class="kb-meta">分類: 特権アクセス監査 ・ 難易度: 中級</p><p>第二十九観点 特権アクセス監査 の変更作業では Docker-CE検証 の現在値を先に固定します（第二十九観点）。第二十九観点 役割は Ubuntu Server環境で利用するDocker-CEバージョンの確認観点という範囲です（第二十九観点）。第二十九観点 アクティベーションコード発行サイトの入力欄 の値を Ubuntu24-REC05 と合わせ、ライセンス有効化情報の確認を記録します（第二十九観点）。第二十九観点 証跡には資料IDと確認値を併記し、REC記録029として保存します（第二十九観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Docker-CE検証 接続確認 構成029</strong></p><p>検証目的: 特権アクセス監査における Docker-CE検証 の接続確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=Ubuntu24-REC05</p><p>セッション環境: REC NEAO 管理画面 / 働き方モニタリング</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により Docker-CE検証 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; モニタリング &gt; テレワーク対象=Ubuntu24-REC05
→ ENTER を押す
［画面・出力］
モニタリング対象
対象 Ubuntu24-REC05
VDI 操作監視 有効
DaaS 操作監視 有効
確認コード REC029A
画面・出力には REC029A が含まれる。REC029A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により Docker-CE検証 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; レポート &gt; 働き方モニタリング
→ ENTER を押す
［画面・出力］
働き方モニタリングレポート
深夜残業 検知あり
休日業務 確認対象
確認コード REC029B
画面・出力には REC029B が含まれる。REC029B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により Docker-CE検証 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; アラート &gt; 勤務時間外
→ ENTER を押す
［画面・出力］
勤務時間外アラート
対象 Ubuntu24-REC05
通知履歴 管理者確認済み
確認コード REC029C
画面・出力には REC029C が含まれる。REC029C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC029A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC029B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC029C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0032"><h3>働き方モニタリングレポート セキュリティ確認 照合017</h3><p class="kb-meta">分類: 特権アクセス監査 ・ 難易度: 中級</p><p>第十七観点 特権アクセス監査 の変更作業では 働き方モニタリングレポート の現在値を先に固定します（第十七観点）。第十七観点 役割は テレワークやRPAの実態を俯瞰して把握するためのレポートという範囲です（第十七観点）。第十七観点 働き方モニタリングレポート と Ubuntu24-REC17 を同じ証跡に置き、操作録画とテキスト証跡の整合確認を管理します（第十七観点）。第十七観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録017から再現します（第十七観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>働き方モニタリングレポート セキュリティ確認 照合017</strong></p><p>検証目的: 特権アクセス監査における 働き方モニタリングレポート のセキュリティ確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=Ubuntu24-REC17</p><p>セッション環境: REC NEAO 管理画面 / 働き方モニタリング</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 働き方モニタリングレポート の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; モニタリング &gt; テレワーク対象=Ubuntu24-REC17
→ ENTER を押す
［画面・出力］
モニタリング対象
対象 Ubuntu24-REC17
VDI 操作監視 有効
DaaS 操作監視 有効
確認コード REC017A
画面・出力には REC017A が含まれる。REC017A を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 働き方モニタリングレポート の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; レポート &gt; 働き方モニタリング
→ ENTER を押す
［画面・出力］
働き方モニタリングレポート
深夜残業 検知あり
休日業務 確認対象
確認コード REC017B
画面・出力には REC017B が含まれる。REC017B を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 働き方モニタリングレポート の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; アラート &gt; 勤務時間外
→ ENTER を押す
［画面・出力］
勤務時間外アラート
対象 Ubuntu24-REC17
通知履歴 管理者確認済み
確認コード REC017C
画面・出力には REC017C が含まれる。REC017C を読み取り、操作録画とテキスト証跡の整合確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC017A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC017B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC017C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0033"><h3>検知ルール 構成確認 構成005</h3><p class="kb-meta">分類: 特権アクセス監査 ・ 難易度: 初級</p><p>第五観点 特権アクセス監査 の変更作業では 検知ルール の現在値を先に固定します（第五観点）。第五観点 役割は 監視対象ログを条件化し、高リスク操作を発見するための定義という範囲です（第五観点）。第五観点 Ubuntu24-REC05 を起点に設定値を戻し、管理画面間の値合わせを点検します（第五観点）。第五観点 確認経路は管理画面、証跡一覧、検知ルール、動作検証表の別を REC記録005に残します（第五観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>検知ルール 構成確認 構成005</strong></p><p>検証目的: 特権アクセス監査における 検知ルール の構成確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=Ubuntu24-REC05</p><p>セッション環境: REC NEAO 管理画面 / 働き方モニタリング</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 検知ルール の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; モニタリング &gt; テレワーク対象=Ubuntu24-REC05
→ ENTER を押す
［画面・出力］
モニタリング対象
対象 Ubuntu24-REC05
VDI 操作監視 有効
DaaS 操作監視 有効
確認コード REC005A
画面・出力には REC005A が含まれる。REC005A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 検知ルール の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; レポート &gt; 働き方モニタリング
→ ENTER を押す
［画面・出力］
働き方モニタリングレポート
深夜残業 検知あり
休日業務 確認対象
確認コード REC005B
画面・出力には REC005B が含まれる。REC005B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 検知ルール の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; アラート &gt; 勤務時間外
→ ENTER を押す
［画面・出力］
勤務時間外アラート
対象 Ubuntu24-REC05
通知履歴 管理者確認済み
確認コード REC005C
画面・出力には REC005C が含まれる。REC005C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC005A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC005B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC005C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## 監査レポート


<section class="kb-item" id="c08-i0034"><h3>DaaS環境監視 定義照合 監査012</h3><p class="kb-meta">分類: 監査レポート ・ 難易度: 中級</p><p>第十二観点 DaaS環境監視 は ESS REC 6 の 監査レポート を説明するための項目です（第十二観点）。第十二観点 資料上は クラウド型デスクトップ環境の利用状況をモニタリングする対象として扱います（第十二観点）。第十二観点 PodmanとRHELバージョンの検証値 と AUDIT-TRACE-012 を同じ証跡に置き、ライセンス有効化情報の確認を管理します（第十二観点）。第十二観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録012から再現します（第十二観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DaaS環境監視 定義照合 監査012</strong></p><p>検証目的: 監査レポートにおける DaaS環境監視 の定義照合を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=AUDIT-TRACE-012</p><p>セッション環境: REC NEAO 管理画面 / RPA監視</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により DaaS環境監視 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; ジョブ=AUDIT-TRACE-012
→ ENTER を押す
［画面・出力］
RPA監視
ジョブ AUDIT-TRACE-012
画面遷移録画 記録済み
確認コード REC012A
画面・出力には REC012A が含まれる。REC012A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により DaaS環境監視 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; エラー検知
→ ENTER を押す
［画面・出力］
RPA検知条件
エラーメッセージ 検知対象
動作異常 アラート対象
確認コード REC012B
画面・出力には REC012B が含まれる。REC012B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により DaaS環境監視 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; 実行結果
→ ENTER を押す
［画面・出力］
RPA実行結果
ジョブ AUDIT-TRACE-012
実行結果と問題発生時の事象を確認可能
確認コード REC012C
画面・出力には REC012C が含まれる。REC012C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC012A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC012B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC012C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0035"><h3>情報漏洩対策 可用性確認 監査036</h3><p class="kb-meta">分類: 監査レポート ・ 難易度: 上級</p><p>第三十六観点 情報漏洩対策 は ESS REC 6 の 監査レポート を説明するための項目です（第三十六観点）。第三十六観点 資料上は 操作証跡により内部不正や情報持ち出しリスクを抑える観点として扱います（第三十六観点）。第三十六観点 アラート通知履歴 と監査行を同じ確認票に置き、特権操作の監査証跡化を説明可能にします（第三十六観点）。第三十六観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録036へ書きます（第三十六観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>情報漏洩対策 可用性確認 監査036</strong></p><p>検証目的: 監査レポートにおける 情報漏洩対策 の可用性確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=AUDIT-TRACE-036</p><p>セッション環境: REC NEAO 管理画面 / RPA監視</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 情報漏洩対策 の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; ジョブ=AUDIT-TRACE-036
→ ENTER を押す
［画面・出力］
RPA監視
ジョブ AUDIT-TRACE-036
画面遷移録画 記録済み
確認コード REC036A
画面・出力には REC036A が含まれる。REC036A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 情報漏洩対策 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; エラー検知
→ ENTER を押す
［画面・出力］
RPA検知条件
エラーメッセージ 検知対象
動作異常 アラート対象
確認コード REC036B
画面・出力には REC036B が含まれる。REC036B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 情報漏洩対策 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; 実行結果
→ ENTER を押す
［画面・出力］
RPA実行結果
ジョブ AUDIT-TRACE-036
実行結果と問題発生時の事象を確認可能
確認コード REC036C
画面・出力には REC036C が含まれる。REC036C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC036A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC036B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC036C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0036"><h3>発行サイト 権限確認 保護024</h3><p class="kb-meta">分類: 監査レポート ・ 難易度: 中級</p><p>第二十四観点 発行サイト は ESS REC 6 の 監査レポート を説明するための項目です（第二十四観点）。第二十四観点 資料上は インスタンスIDと申請コードを入力してコードを発行するWebサイトとして扱います（第二十四観点）。第二十四観点 画面表示文字列の検索結果 の値を AUDIT-TRACE-024 と合わせ、RPA異常検知の証跡化を記録します（第二十四観点）。第二十四観点 証跡には資料IDと確認値を併記し、REC記録024として保存します（第二十四観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>発行サイト 権限確認 保護024</strong></p><p>検証目的: 監査レポートにおける 発行サイト の権限確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=AUDIT-TRACE-024</p><p>セッション環境: REC NEAO 管理画面 / RPA監視</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 発行サイト の値を確認し、対象の現在値を固定する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; ジョブ=AUDIT-TRACE-024
→ ENTER を押す
［画面・出力］
RPA監視
ジョブ AUDIT-TRACE-024
画面遷移録画 記録済み
確認コード REC024A
画面・出力には REC024A が含まれる。REC024A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 発行サイト の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; エラー検知
→ ENTER を押す
［画面・出力］
RPA検知条件
エラーメッセージ 検知対象
動作異常 アラート対象
確認コード REC024B
画面・出力には REC024B が含まれる。REC024B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 発行サイト の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
REC NEAO Console
COMMAND ===&gt; RPA監視 &gt; 実行結果
→ ENTER を押す
［画面・出力］
RPA実行結果
ジョブ AUDIT-TRACE-024
実行結果と問題発生時の事象を確認可能
確認コード REC024C
画面・出力には REC024C が含まれる。REC024C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC024A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC024B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC024C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


## 録画・記録


<section class="kb-item" id="c08-i0037"><h3>RPA動作異常検知 権限確認 復旧014</h3><p class="kb-meta">分類: 録画・記録 ・ 難易度: 中級</p><p>第十四観点 RPA動作異常検知 は ESS REC 6 の 録画・記録 で扱う管理項目です（区分第十四）（第十四観点）。第十四観点 管理上は RPAのエラーや異常動作を検知し、管理者通知へつなげる機能という値を追います（第十四観点）。第十四観点 画面表示文字列の検索結果 の値を NEAO-MON-014 と合わせ、RPA異常検知の証跡化を記録します（第十四観点）。第十四観点 証跡には資料IDと確認値を併記し、REC記録014として保存します（第十四観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RPA動作異常検知 権限確認 復旧014</strong></p><p>検証目的: 録画・記録における RPA動作異常検知 の権限確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=NEAO-MON-014</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により RPA動作異常検知 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=NEAO-MON-014
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 NEAO-MON-014
条件種別 正規表現
通知先 監査管理者
確認コード REC014A
画面・出力には REC014A が含まれる。REC014A を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により RPA動作異常検知 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件14 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC014B
画面・出力には REC014B が含まれる。REC014B を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により RPA動作異常検知 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=NEAO-MON-014
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 NEAO-MON-014
通知履歴 管理者へ送信済み
確認コード REC014C
画面・出力には REC014C が含まれる。REC014C を読み取り、RPA異常検知の証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC014A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC014B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC014C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0038"><h3>市場シェア根拠 レプリケーション確認 復旧038</h3><p class="kb-meta">分類: 録画・記録 ・ 難易度: 上級</p><p>第三十八観点 市場シェア根拠 は ESS REC 6 の 録画・記録 で扱う管理項目です（区分第三十八）（第三十八観点）。第三十八観点 管理上は 証跡管理ツールの市場実績を説明する参考情報という値を追います（第三十八観点）。第三十八観点 NEAO-MON-038、REC Webサイトのライセンス登録画面、管理ツールの表示を照合し、管理画面間の値合わせを確認します（第三十八観点）。第三十八観点 調査票では録画、文字列、打鍵、アラートの入口を REC記録038に区別して残します（第三十八観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>市場シェア根拠 レプリケーション確認 復旧038</strong></p><p>検証目的: 録画・記録における 市場シェア根拠 のレプリケーション確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=NEAO-MON-038</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 市場シェア根拠 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=NEAO-MON-038
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 NEAO-MON-038
条件種別 正規表現
通知先 監査管理者
確認コード REC038A
画面・出力には REC038A が含まれる。REC038A を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 市場シェア根拠 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件14 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC038B
画面・出力には REC038B が含まれる。REC038B を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 市場シェア根拠 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=NEAO-MON-038
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 NEAO-MON-038
通知履歴 管理者へ送信済み
確認コード REC038C
画面・出力には REC038C が含まれる。REC038C を読み取り、管理画面間の値合わせのため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC038A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC038B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC038C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0039"><h3>起動プロセス記録 定義照合 点検002</h3><p class="kb-meta">分類: 録画・記録 ・ 難易度: 初級</p><p>第二観点 起動プロセス記録 は ESS REC 6 の 録画・記録 で扱う管理項目です（区分第二）（第二観点）。第二観点 管理上は 操作対象環境で起動したプロセスを証跡として追跡する記録対象という値を追います（第二観点）。第二観点 PodmanとRHELバージョンの検証値 と NEAO-MON-002 を同じ証跡に置き、ライセンス有効化情報の確認を管理します（第二観点）。第二観点 後続確認では画面値、録画証跡、通知履歴の対応を REC記録002から再現します（第二観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>起動プロセス記録 定義照合 点検002</strong></p><p>検証目的: 録画・記録における 起動プロセス記録 の定義照合を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=NEAO-MON-002</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 起動プロセス記録 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=NEAO-MON-002
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 NEAO-MON-002
条件種別 正規表現
通知先 監査管理者
確認コード REC002A
画面・出力には REC002A が含まれる。REC002A を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 起動プロセス記録 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件02 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC002B
画面・出力には REC002B が含まれる。REC002B を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 起動プロセス記録 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=NEAO-MON-002
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 NEAO-MON-002
通知履歴 管理者へ送信済み
確認コード REC002C
画面・出力には REC002C が含まれる。REC002C を読み取り、ライセンス有効化情報の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC002A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC002B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC002C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>


<section class="kb-item" id="c08-i0040"><h3>電話発行手順 可用性確認 点検026</h3><p class="kb-meta">分類: 録画・記録 ・ 難易度: 中級</p><p>第二十六観点 電話発行手順 は ESS REC 6 の 録画・記録 で扱う管理項目です（区分第二十六）（第二十六観点）。第二十六観点 管理上は メール利用ができない場合に必要情報を伝えてコードを受け取る手順という値を追います（第二十六観点）。第二十六観点 アラート通知履歴 と監査行を同じ確認票に置き、特権操作の監査証跡化を説明可能にします（第二十六観点）。第二十六観点 記録では対象名、証跡時刻、ルール名、確認値を REC記録026へ書きます（第二十六観点）。</p><p class="kb-src"><strong>出典:</strong> ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>電話発行手順 可用性確認 点検026</strong></p><p>検証目的: 録画・記録における 電話発行手順 の可用性確認を机上で確認する。</p><p>前提条件: ESS REC 6 または REC NEAO の管理画面、証跡一覧、検知ルール、動作検証表を確認済み。対象=NEAO-MON-026</p><p>セッション環境: ESS REC 管理画面 / 検知ルール</p><pre class="kb-code">■ ステップ 1
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。状態表示により 電話発行手順 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; ルール名=NEAO-MON-026
→ ENTER を押す
［画面・出力］
検知ルール詳細
ルール名 NEAO-MON-026
条件種別 正規表現
通知先 監査管理者
確認コード REC026A
画面・出力には REC026A が含まれる。REC026A を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。定義照合により 電話発行手順 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; 検知ルール &gt; 条件一覧
→ ENTER を押す
［画面・出力］
条件一覧
条件02 画面表示文字列に一致
複数条件 組み合わせあり
確認コード REC026B
画面・出力には REC026B が含まれる。REC026B を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は ESS REC 6 または REC NEAO の確認画面、証跡表示、動作検証表のいずれかである。ログ確認により 電話発行手順 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
ESS REC Console
COMMAND ===&gt; アラート履歴 &gt; ルール名=NEAO-MON-026
→ ENTER を押す
［画面・出力］
アラート履歴
ルール名 NEAO-MON-026
通知履歴 管理者へ送信済み
確認コード REC026C
画面・出力には REC026C が含まれる。REC026C を読み取り、特権操作の監査証跡化のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: REC026A が画面または出力に表示され、対象証跡や設定が取り違えられていないこと。
ステップ2: REC026B が画面または出力に表示され、管理画面、証跡、動作検証表の対応が確認できること。
ステップ3: REC026C が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ESS_REC_6_User_Guide / ESS_REC_6_Installation_Guide / ESS_REC_NEAO_Product_Guide / customer.et-x.jp aid-1700 Activation Guide / customer.et-x.jp aid-2178 Product Validation Guide</p></div></details></section>
