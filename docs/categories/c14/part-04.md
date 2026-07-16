---
search:
  exclude: true
---

# IBM Spectrum Protect 8.1 — 詳細 (4/4)

[← IBM Spectrum Protect 8.1 の概要へ戻る](index.md)


## ポリシー


<section class="kb-item" id="c14-i0491"><h3>ポリシーと管理クラス Policy Set 0212</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 中級</p><p>桃M登録0213ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M登録0213です。桃M登録0213はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M登録0213です。桃M登録0213ではディレクトリ管理クラスと取得時刻を採取票桃M登録0213へ残します。桃M登録0213では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M登録0213です。桃M登録0213の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M登録0213です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0212の役割を調べています。サーバー日次運用 Storage Pool 0295の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 障害切り分けに用いる役割はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。</li><li>C. 障害切り分けに用いる役割はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 登録対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・登録・ディレ・登録ドメ）です。登録時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・登録・ディレ・登録ドメです。Stora・抑止のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・抑止・ストレ・プール容）です。変更確認対象BackuのB:は「Backup andで変更前の確認ではコピーグループの」を述べ、対象は変更前の確認 CG02（Backu・変更確・確認で・バックア）です。棚卸時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・棚卸・開始時・日次処理）です。Poliを登録という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・登録・ディレ・登録ドメ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0212</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0212について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC02
確認コード SP81DD0212A
画面・出力には SP81DD0212A が表示され、ポリシーと管理クラス Policy Set 0212 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL01
Retain Extra Versions 30
確認コード SP81DD0212B
画面・出力には SP81DD0212B が表示され、ポリシーと管理クラス Policy Set 0212 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0212C
画面・出力には SP81DD0212C が表示され、ポリシーと管理クラス Policy Set 0212 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0212A が画面・出力に表示されること
② ステップ2 の SP81DD0212B が画面・出力に表示されること
③ ステップ3 の SP81DD0212C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0492"><h3>ポリシーと管理クラス Policy Set 0227</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 上級</p><p>茶H確認0228ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H確認0228です。茶H確認0228はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H確認0228です。茶H確認0228ではディレクトリ管理クラスと取得時刻を採取票茶H確認0228へ残します。茶H確認0228ではコピーグループ未定義を避けるため補助資料も照合する判断茶H確認0228です。茶H確認0228の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H確認0228です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「ポリシーと管理クラス Policy Set 0227」を「サーバー日次運用 Database Backup 0277」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 仕様上の役割はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。</li><li>D. 仕様上の役割はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 確認対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・確認・ディレ・コピーグ）です。確認時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・確認・ディレ・コピーグです。照合対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・照合・期限切・期限切れ）です。停止確認時のManagのC:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Manag・停止確・停止前・既定管理）です。ノード登録を棚卸のD:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・棚卸・ノード・ディレク）です。Poliを確認という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・確認・ディレ・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0227</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0227について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC08
確認コード SP81DD0227A
画面・出力には SP81DD0227A が表示され、ポリシーと管理クラス Policy Set 0227 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL02
Retain Extra Versions 30
確認コード SP81DD0227B
画面・出力には SP81DD0227B が表示され、ポリシーと管理クラス Policy Set 0227 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0227C
画面・出力には SP81DD0227C が表示され、ポリシーと管理クラス Policy Set 0227 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0227A が画面・出力に表示されること
② ステップ2 の SP81DD0227B が画面・出力に表示されること
③ ステップ3 の SP81DD0227C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0493"><h3>ポリシーと管理クラス Policy Set 0242</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 初級</p><p>緑C保護0243ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C保護0243です。緑C保護0243はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C保護0243です。緑C保護0243ではディレクトリ管理クラスと取得時刻を採取票緑C保護0243へ残します。緑C保護0243ではDIRMC誤設定を避けるため補助資料も照合する判断緑C保護0243です。緑C保護0243の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C保護0243です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0242を同一分類のサーバー日次運用 Storage Pool 0280と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. コマンドまたは機能の用途はDirectory-containeで停止前の確認ではストレージプールのである。</li><li>D. コマンドまたは機能の用途はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・保護・ディレ・ディレク）です。保護時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・保護・ディレ・ディレクです。抑止対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・抑止・ストレ・ノード状）です。停止確認時のDirecのC:は「Directory-containeで停止前の確認ではストレージプー」を述べ、対象は停止前の確認 POOL14（Direc・停止確・停止前・容量使用）です。ノード登録を監査のD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・監査・ノード・登録ドメ）です。Poliを保護という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・保護・ディレ・ディレク）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0242</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0242について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC02
確認コード SP81DD0242A
画面・出力には SP81DD0242A が表示され、ポリシーと管理クラス Policy Set 0242 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL02
Retain Extra Versions 30
確認コード SP81DD0242B
画面・出力には SP81DD0242B が表示され、ポリシーと管理クラス Policy Set 0242 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0242C
画面・出力には SP81DD0242C が表示され、ポリシーと管理クラス Policy Set 0242 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0242A が画面・出力に表示されること
② ステップ2 の SP81DD0242B が画面・出力に表示されること
③ ステップ3 の SP81DD0242C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0494"><h3>ポリシーと管理クラス Policy Set 0257</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 初級</p><p>藤R保護0258ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R保護0258です。藤R保護0258はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R保護0258です。藤R保護0258ではディレクトリ管理クラスと取得時刻を採取票藤R保護0258へ残します。藤R保護0258では管理クラス未割当を避けるため補助資料も照合する判断藤R保護0258です。藤R保護0258の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R保護0258です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0257の設定や表示を読む前に役割を確認します。サーバー日次運用 Storage Pool 0280ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>B. 一次資料が示す主目的はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。</li><li>C. 一次資料が示す主目的はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・保護・ディレ・管理クラ）です。保護時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・保護・ディレ・管理クラです。Stora・抑止のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・抑止・ストレ・ノード状）です。停止確認対象ManagのB:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Manag・停止確・停止前・既定管理）です。監査時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・監査・関連ノ・日次処理）です。Poliを保護という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・保護・ディレ・管理クラ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0257</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0257について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC08
確認コード SP81DD0257A
画面・出力には SP81DD0257A が表示され、ポリシーと管理クラス Policy Set 0257 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL03
Retain Extra Versions 30
確認コード SP81DD0257B
画面・出力には SP81DD0257B が表示され、ポリシーと管理クラス Policy Set 0257 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0257C
画面・出力には SP81DD0257C が表示され、ポリシーと管理クラス Policy Set 0257 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0257A が画面・出力に表示されること
② ステップ2 の SP81DD0257B が画面・出力に表示されること
③ ステップ3 の SP81DD0257C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0495"><h3>ポリシーと管理クラス Policy Set 0272</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 中級</p><p>桃M照合0273ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M照合0273です。桃M照合0273はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M照合0273です。桃M照合0273ではディレクトリ管理クラスと取得時刻を採取票桃M照合0273へ残します。桃M照合0273では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M照合0273です。桃M照合0273の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M照合0273です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0272に関する障害切り分けの前提を確認しています。クライアントスケジュール Action 0291の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割は抑止で開始時刻を証跡に残し・Actionの開始時刻と取得時刻を記録し。クライアントスケジュール Action 0291固有の属性も確認対象に含める。</li><li>B. 障害切り分けに用いる役割は停止確認で停止前の確認を証跡に残し・Client Nodeで停止前の確認ではノード管理の。</li><li>C. 障害切り分けに用いる役割は照合でディレクトリを証跡に残し・Policy Setのディレクトリ管理クラスと取得時刻を記録。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割は移行でストレージプを証跡に残し・Storage Poolのストレージプール使用量と取得時刻を。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 照合対象PolicでCの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・照合・ディレ・登録ドメ）です。照合時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・照合・ディレ・登録ドメです。Actio・抑止のA:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Actio・抑止・開始時・失敗イベ）です。停止確認対象ClienのB:は「Client Nodeで停止前の確認ではノード管理の」を述べ、対象は停止前の確認 NODE14（Clien・停止確・停止前・長期未接）です。Storを移行のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・移行・ストレ・プール容）です。Poliを照合という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・照合・ディレ・登録ドメ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0272</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0272について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC05
確認コード SP81DD0272A
画面・出力には SP81DD0272A が表示され、ポリシーと管理クラス Policy Set 0272 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL04
Retain Extra Versions 30
確認コード SP81DD0272B
画面・出力には SP81DD0272B が表示され、ポリシーと管理クラス Policy Set 0272 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0272C
画面・出力には SP81DD0272C が表示され、ポリシーと管理クラス Policy Set 0272 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0272A が画面・出力に表示されること
② ステップ2 の SP81DD0272B が画面・出力に表示されること
③ ステップ3 の SP81DD0272C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0496"><h3>ポリシーと管理クラス Policy Set 0287</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 中級</p><p>茶H抑止0288ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H抑止0288です。茶H抑止0288はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H抑止0288です。茶H抑止0288ではディレクトリ管理クラスと取得時刻を採取票茶H抑止0288へ残します。茶H抑止0288ではコピーグループ未定義を避けるため補助資料も照合する判断茶H抑止0288です。茶H抑止0288の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H抑止0288です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0287を保守記録に説明する必要があります。expiration 容量監視 詳細表示と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はコピーグループ未定義を避けるため・表示操作で対象欄を追跡するしてディレクトリを照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割は詳細表示の誤読を避けるため・詳細表示で詳細表示を確認するして詳細表示を照合する。</li><li>C. 仕様上の役割は長期未接続ノードを正常な保護対象を避けるため・通常状態確認で通常状態の確を確認するして通常状態の確を照合する。</li><li>D. 仕様上の役割はノード状態の誤読を避けるため・保守操作で監査欄を保存するして期限切れ処理を照合する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 抑止対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・抑止・ディレ・コピーグ）です。抑止時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・抑止・ディレ・コピーグです。詳細表示対象expirのB:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を容量監視として確」を述べ、対象は容量監視 詳細表示（expir・詳細表・詳細表・詳細表示）です。通常状態時のClienのC:は「Client Nodeで通常状態の確認ではノード管理の」を述べ、対象は通常状態の確認 NODE01（Clien・通常状・通常状・長期未接）です。Dataを切替のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・切替・期限切・ノード状）です。Poliを抑止という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・抑止・ディレ・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0287</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0287について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC02
確認コード SP81DD0287A
画面・出力には SP81DD0287A が表示され、ポリシーと管理クラス Policy Set 0287 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL05
Retain Extra Versions 30
確認コード SP81DD0287B
画面・出力には SP81DD0287B が表示され、ポリシーと管理クラス Policy Set 0287 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0287C
画面・出力には SP81DD0287C が表示され、ポリシーと管理クラス Policy Set 0287 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0287A が画面・出力に表示されること
② ステップ2 の SP81DD0287B が画面・出力に表示されること
③ ステップ3 の SP81DD0287C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0497"><h3>ポリシーと管理クラス Policy Set 0302</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 中級</p><p>緑C解析0303ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C解析0303です。緑C解析0303はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C解析0303です。緑C解析0303ではディレクトリ管理クラスと取得時刻を採取票緑C解析0303へ残します。緑C解析0303ではDIRMC誤設定を避けるため補助資料も照合する判断緑C解析0303です。緑C解析0303の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C解析0303です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0302の技術的な意味を資料で確認するとき、サーバー日次運用 Node Name 0328との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は点検操作で判定欄を記録することでディレクトリを確認し・ディレクトリー管理クラス指定を防ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途は保守操作で監査欄を保存することで運用状態を確認し・ノード状態の誤読を防ぐ。</li><li>C. コマンドまたは機能の用途は変更確認で変更後の確認を確認することで変更後の確認を確認し・置換条件や復元先を確認せず本を防ぐ。</li><li>D. コマンドまたは機能の用途は復旧操作で点検欄を確認することでノード登録値を確認し・管理クラス未割当を防ぐ。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・解析・ディレ・ディレク）です。解析時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・解析・ディレ・ディレクです。計画対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・計画・運用状・ノード状）です。変更確認時のClienのC:は「Client Restoreで変更後の確認ではリストア確認の」を述べ、対象は変更後の確認 RST03（Clien・変更確・変更後・置換条件）です。ディレクを移行のD:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・移行・ノード・管理クラ）です。Poliを解析という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・解析・ディレ・ディレク）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0302</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0302について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC08
確認コード SP81DD0302A
画面・出力には SP81DD0302A が表示され、ポリシーと管理クラス Policy Set 0302 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL06
Retain Extra Versions 30
確認コード SP81DD0302B
画面・出力には SP81DD0302B が表示され、ポリシーと管理クラス Policy Set 0302 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0302C
画面・出力には SP81DD0302C が表示され、ポリシーと管理クラス Policy Set 0302 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0302A が画面・出力に表示されること
② ステップ2 の SP81DD0302B が画面・出力に表示されること
③ ステップ3 の SP81DD0302C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0498"><h3>ポリシーと管理クラス Policy Set 0317</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 中級</p><p>藤R解析0318ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R解析0318です。藤R解析0318はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R解析0318です。藤R解析0318ではディレクトリ管理クラスと取得時刻を採取票藤R解析0318へ残します。藤R解析0318では管理クラス未割当を避けるため補助資料も照合する判断藤R解析0318です。藤R解析0318の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R解析0318です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0317について構成や状態を確認します。expiration 期限切れ確認 入力欄ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的は期限切れ確認で入力欄を証跡に残し・保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ。</li><li>B. 一次資料が示す主目的は再始動確認で確認ではアーを証跡に残し・Archive Operationで再始動後の確認ではアーカ。</li><li>C. 一次資料が示す主目的は収集でイベント結果を証跡に残し・Event Statusのイベント結果と取得時刻を記録し。</li><li>D. 一次資料が示す主目的は解析でディレクトリを証跡に残し・Policy Setのディレクトリ管理クラスと取得時刻を記録。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・解析・ディレ・管理クラ）です。解析時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・解析・ディレ・管理クラです。expir・期限切れ確のA:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」を述べ、対象は期限切れ確認 入力欄（expir・期限切・入力欄・入力欄の）です。再始動確対象ArchiのB:は「Archive Operationで再始動後の確認ではアーカイブ運用」を述べ、対象は再始動後の確認 ARC15（Archi・再始動・確認で・バックア）です。収集時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベン・日次処理）です。Poliを解析という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・解析・ディレ・管理クラ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0317</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0317について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC05
確認コード SP81DD0317A
画面・出力には SP81DD0317A が表示され、ポリシーと管理クラス Policy Set 0317 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL00
Retain Extra Versions 30
確認コード SP81DD0317B
画面・出力には SP81DD0317B が表示され、ポリシーと管理クラス Policy Set 0317 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0317C
画面・出力には SP81DD0317C が表示され、ポリシーと管理クラス Policy Set 0317 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0317A が画面・出力に表示されること
② ステップ2 の SP81DD0317B が画面・出力に表示されること
③ ステップ3 の SP81DD0317C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0499"><h3>ポリシーと管理クラス Policy Set 0332</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 中級</p><p>桃M計画0333ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M計画0333です。桃M計画0333はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M計画0333です。桃M計画0333ではディレクトリ管理クラスと取得時刻を採取票桃M計画0333へ残します。桃M計画0333では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M計画0333です。桃M計画0333の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M計画0333です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシーと管理クラス Policy Set 0332の役割を調べています。schedule 容量監視 履歴行の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はバックアップや管理コマンドを決めた時刻に実行する定義を容量監視として確認する。ノードで履歴行を確認するときは履歴行の誤読を防ぐ。</li><li>B. 障害切り分けに用いる役割はArchive Operationで依存関係の確認ではアーカイブ運用のである。依存関係確認で確認ではアーを確認するときはバックアップデータをアーカイを防ぐ。アーカイブ運用 Archive Operation 依存関係の確認固有の属性も確認対象に含める。</li><li>C. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。</li><li>D. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは登録ドメインの取り違えを防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 計画対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・計画・ディレ・登録ドメ）です。計画時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・計画・ディレ・登録ドメです。sched・ノードのA:は「バックアップや管理コマンドを決めた時刻に実行する定義を容量監視として」を述べ、対象は容量監視 履歴行（sched・ノード・履歴行・履歴行の）です。依存関係対象ArchiのB:は「Archive Operationで依存関係の確認ではアーカイブ運用」を述べ、対象は依存関係の確認 ARC13（Archi・依存関・確認で・バックア）です。保守時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・保守・管理ク・コピーグ）です。Poliを計画という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・計画・ディレ・登録ドメ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0332</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0332について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC02
確認コード SP81DD0332A
画面・出力には SP81DD0332A が表示され、ポリシーと管理クラス Policy Set 0332 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL01
Retain Extra Versions 30
確認コード SP81DD0332B
画面・出力には SP81DD0332B が表示され、ポリシーと管理クラス Policy Set 0332 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0332C
画面・出力には SP81DD0332C が表示され、ポリシーと管理クラス Policy Set 0332 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0332A が画面・出力に表示されること
② ステップ2 の SP81DD0332B が画面・出力に表示されること
③ ステップ3 の SP81DD0332C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0500"><h3>ポリシーと管理クラス Policy Set 0347</h3><p class="kb-meta">分類: ポリシー ・ 難易度: 上級</p><p>茶H解除0348ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H解除0348です。茶H解除0348はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H解除0348です。茶H解除0348ではディレクトリ管理クラスと取得時刻を採取票茶H解除0348へ残します。茶H解除0348ではコピーグループ未定義を避けるため補助資料も照合する判断茶H解除0348です。茶H解除0348の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H解除0348です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「ポリシーと管理クラス Policy Set 0347」を「backup copy group 状態確認 文字変換」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則である。状態確認で文字変換を確認するときは文字変換の誤読を防ぐ。</li><li>B. 仕様上の役割はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。主操作で出力欄を評価するときは関連付け漏れを防ぐ。</li><li>C. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。確認操作で状態欄を整理するときはデータベースバックアップ時刻を防ぐ。</li><li>D. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 解除対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・解除・ディレ・コピーグ）です。解除時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・解除・ディレ・コピーグです。backu・状態確認のA:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は状態確認 文字変換（backu・状態確・文字変・文字変換）です。巡回対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・巡回・スケジ・関連付け）です。登録時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・登録・ノード・データベ）です。Poliを解除という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・解除・ディレ・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシーと管理クラス Policy Set 0347</strong></p><p>検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0347について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY DOMAIN
→ Enter を押す
［画面・出力］
Policy Domain STANDARD
Policy Set ACTIVE
Management Class MC08
確認コード SP81DD0347A
画面・出力には SP81DD0347A が表示され、ポリシーと管理クラス Policy Set 0347 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmc QUERY MGMTCLASS -DETAIL
→ Enter を押す
［画面・出力］
Copy Group STANDARD
Destination DIRPOOL02
Retain Extra Versions 30
確認コード SP81DD0347B
画面・出力には SP81DD0347B が表示され、ポリシーと管理クラス Policy Set 0347 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY DOMAIN
→ Enter を押す
［画面・出力］
DIRMC MC_DIR02
Include Exclude rule reviewed
Client option file checked
確認コード SP81DD0347C
画面・出力には SP81DD0347C が表示され、ポリシーと管理クラス Policy Set 0347 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0347A が画面・出力に表示されること
② ステップ2 の SP81DD0347B が画面・出力に表示されること
③ ステップ3 の SP81DD0347C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## ポリシードメイン


<section class="kb-item" id="c14-i0501"><h3>backup copy group コマンド証跡 収集装置</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「backup copy group コマンド証跡 収集装置」は、バックアップ版数と保存先を定めるコピー規則をコマンド証跡の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR073Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「backup copy group コマンド証跡 収集装置」を「バックアップ運用 Incremental Backup 停止前の確認 BKP14」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はIncremental Backupで停止前の確認ではバックアップ運用のである。</li><li>B. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 仕様上の役割はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> コマンでポリシードでDの記述「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」に対応する項目はコマンド証跡 収集装置（backup・ポリシー）です。コマン・収集装に関するポリシードメインの仕様は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」で、確認対象はbackup・ポリシードです。Incre・停止確認のA:は「Incremental Backupで停止前の確認ではバックアップ運」を述べ、対象は停止前の確認 BKP14（Increme・停止確認）です。サーバで監査のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・監査）です。解析時のServeのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・解析）です。backをポリシードという用語は「バックアップ版数と保存先を定めるコピー規則をコマンド」を指し、コマンド証跡 収集装置（backup・ポリシー）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>backup copy group コマンド証跡 収集装置</strong></p><p>検証目的: ポリシードメインのbackup copy group コマンド証跡 収集装置について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL073
画面・出力には ANR1550I が含まれ、backup copy group コマンド証跡 収集装置の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL073 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL073
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0502"><h3>backup copy group ノード割当確認 再同期判断</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「backup copy group ノード割当確認 再同期判断」は、バックアップ版数と保存先を定めるコピー規則をノード割当確認の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR033Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「backup copy group ノード割当確認 再同期判断」を「backup copy group 保存期間確認 ルール読替」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はバックアップ版数と保存先を定めるコピー規則である。</li><li>B. 保守作業で参照する機能はバックアップ版数と保存先を定めるコピー規則をノード割当確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 保守作業で参照する機能はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ノード割当・backupでBの記述「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」に対応する項目はノード割当確認 再同期判断（backup・ノード割）です。ノード・再同期に関するポリシードメインの仕様は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」で、確認対象はbackup・ノード割当です。保存期間確・backupのA:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は保存期間確認 ルール読替（backup・保存期間）です。巡回・PolicyのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・巡回）です。確認・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。「backup copy group」は「バックアップ版数と保存先を定めるコピー規則をノード割」を指す用語で、ノード割当確認 再同期判断（backup・ノード割）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>backup copy group ノード割当確認 再同期判断</strong></p><p>検証目的: ポリシードメインのbackup copy group ノード割当確認 再同期判断について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL033
画面・出力には ANR1550I が含まれ、backup copy group ノード割当確認 再同期判断の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL033 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL033
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0503"><h3>expiration 保存期間確認 同期範囲</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「expiration 保存期間確認 同期範囲」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を保存期間確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL017を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「expiration 保存期間確認 同期範囲」を「management class 状態確認 イベント識別」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はファイルのバックアップ先や保存期間を決めるポリシー要素である。</li><li>B. 運用時に利用する技術的役割は保存期間を過ぎた版やアーカイブを期限切れにする処理である。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はDBで障害切り分けではサーバーの DB状態からLastDatabaseを読み・サーバーDBに使うである。</li><li>D. 運用時に利用する技術的役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保存期間確・expiratiでBの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理である」に対応する項目は保存期間確認 同期範囲（expirat・保存期間）です。保存期・同期範に関するポリシードメインの仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理」で、確認対象はexpirat・保存期間確です。状態確認・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は状態確認 イベント識別（managem・状態確認）です。サーバーD・DBのC:は「DBで障害切り分けではサーバーの DB状態からLastDatabas」を述べ、対象は障害切り分け DBBK04（DB・サーバー）です。登録・EventのD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・登録）です。「expiration」は「保存期間を過ぎた版やアーカイブを期限切れにする処理」を指す用語で、保存期間確認 同期範囲（expirat・保存期間）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>expiration 保存期間確認 同期範囲</strong></p><p>検証目的: ポリシードメインのexpiration 保存期間確認 同期範囲について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL017
画面・出力には ANR1550I が含まれ、expiration 保存期間確認 同期範囲の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL017 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL017
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0504"><h3>expiration 復元前確認 自動処理</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「expiration 復元前確認 自動処理」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL057を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「expiration 復元前確認 自動処理」を「backup copy group コマンド証跡 収集装置」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。</li><li>C. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復元前で復元前確認でAの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」に対応する項目は復元前確認 自動処理（expirat・復元前確）です。復元前・自動処に関するポリシードメインの仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」で、確認対象はexpirat・復元前確認です。コマンでポリシードのB:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backup・ポリシー）です。復旧時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・復旧）です。Manaを保護のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・保護）です。expiを復元前確認という用語は「保存期間を過ぎた版やアーカイブを期限切れにする処理を」を指し、復元前確認 自動処理（expirat・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>expiration 復元前確認 自動処理</strong></p><p>検証目的: ポリシードメインのexpiration 復元前確認 自動処理について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL057
画面・出力には ANR1550I が含まれ、expiration 復元前確認 自動処理の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL057 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL057
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0505"><h3>policy domain 期限切れ確認 容量表示</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「policy domain 期限切れ確認 容量表示」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期限切れ確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE041を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「policy domain 期限切れ確認 容量表示」を「管理クラス Management Class 権限境界の確認 MC12」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。</li><li>B. 運用時に利用する技術的役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 運用時に利用する技術的役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を期限切れ確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 容量表示・policyでCの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」に対応する項目は期限切れ確認 容量表示（policy・容量表示）です。期限切・容量に関するポリシードメインの仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」で、確認対象はpolicy・容量表示です。権限境界確・ManagemeのA:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。復旧・NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。確認・StorageのD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・確認）です。「policy domain」は「クライアントに適用するバックアップとアーカイブの規則」を指す用語で、期限切れ確認 容量表示（policy・容量表示）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>policy domain 期限切れ確認 容量表示</strong></p><p>検証目的: ポリシードメインのpolicy domain 期限切れ確認 容量表示について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL041
画面・出力には ANR1550I が含まれ、policy domain 期限切れ確認 容量表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL041 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL041
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0506"><h3>policy domain 状態確認 開始時刻</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「policy domain 状態確認 開始時刻」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位を状態確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE001を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「policy domain 状態確認 開始時刻」を「ポリシードメイン Policy Domain 性能影響の確認 DOM11」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はPolicy Domainで性能影響の確認ではポリシードメインのである。</li><li>B. 仕様上の役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位である。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 仕様上の役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 状態確認・policyでBの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位であ」に対応する項目は状態確認 開始時刻（policy・状態確認）です。状態・開始時に関するポリシードメインの仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」で、確認対象はpolicy・状態確認です。性能影響確・PolicyのA:は「Policy Domainで性能影響の確認ではポリシードメインの」を述べ、対象は性能影響の確認 DOM11（Policy・性能影響）です。棚卸・CopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・棚卸）です。確認・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。「policy domain」は「クライアントに適用するバックアップとアーカイブの規則」を指す用語で、状態確認 開始時刻（policy・状態確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>policy domain 状態確認 開始時刻</strong></p><p>検証目的: ポリシードメインのpolicy domain 状態確認 開始時刻について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL001
画面・出力には ANR1550I が含まれ、policy domain 状態確認 開始時刻の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL001 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL001
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0507"><h3>schedule 期限切れ確認 ドメイン値</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「schedule 期限切れ確認 ドメイン値」は、バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 049を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「schedule 期限切れ確認 ドメイン値」を「コピーグループ Backup and Archive Copy Group」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はBackup andで変更後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。</li><li>B. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 仕様上の役割はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 仕様上の役割はバックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 期限切れ確・scheduleでDの記述「バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認す」に対応する項目は期限切れ確認 ドメイン値（schedul・期限切れ）です。期限切・ドメイに関するポリシードメインの仕様は「バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認す」で、確認対象はschedul・期限切れ確です。変更確認・BackupのA:は「Backup andで変更後の確認ではコピーグループの」を述べ、対象は変更後の確認 CG03（Backup・変更確認）です。復旧・ExpiratiのB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・復旧）です。登録・ActionのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・登録）です。「schedule」は「バックアップや管理コマンドを決めた時刻に実行する定義」を指す用語で、期限切れ確認 ドメイン値（schedul・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>schedule 期限切れ確認 ドメイン値</strong></p><p>検証目的: ポリシードメインのschedule 期限切れ確認 ドメイン値について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL049
画面・出力には ANR1550I が含まれ、schedule 期限切れ確認 ドメイン値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL049 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL049
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0508"><h3>schedule 状態確認 復旧手掛かり</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「schedule 状態確認 復旧手掛かり」は、バックアップや管理コマンドを決めた時刻に実行する定義を状態確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 009を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「schedule 状態確認 復旧手掛かり」を「node 宛先照合 データソース」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はサーバーへ登録されたクライアントを表す管理単位である。</li><li>B. 保守作業で参照する機能はバックアップや管理コマンドを決めた時刻に実行する定義である。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>D. 保守作業で参照する機能はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 復旧手掛か・scheduleでBの記述「バックアップや管理コマンドを決めた時刻に実行する定義である」に対応する項目は状態確認 復旧手掛かり（schedul・復旧手掛）です。状態・復旧手に関するポリシードメインの仕様は「バックアップや管理コマンドを決めた時刻に実行する定義」で、確認対象はschedul・復旧手掛かです。宛先照合・nodeのA:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は宛先照合 データソース（node・宛先照合）です。監査・ServerのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査）です。保護・AssociatのD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保護）です。「schedule」は「バックアップや管理コマンドを決めた時刻に実行する定義」を指す用語で、状態確認 復旧手掛かり（schedul・復旧手掛）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>schedule 状態確認 復旧手掛かり</strong></p><p>検証目的: ポリシードメインのschedule 状態確認 復旧手掛かりについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL009
画面・出力には ANR1550I が含まれ、schedule 状態確認 復旧手掛かりの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL009 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL009
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0509"><h3>storage pool 宛先照合 キーマップ</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「storage pool 宛先照合 キーマップ」は、バックアップやアーカイブのデータを格納するサーバー側領域を宛先照合の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 025を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「storage pool 宛先照合 キーマップ」を「management class 復元前確認 期限切れ」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。</li><li>B. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 仕様上の役割はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. 仕様上の役割はバックアップやアーカイブのデータを格納するサーバー側領域である。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 宛先照合・storageでDの記述「バックアップやアーカイブのデータを格納するサーバー側領域である」に対応する項目は宛先照合 キーマップ（storage・宛先照合）です。宛先・キーマに関するポリシードメインの仕様は「バックアップやアーカイブのデータを格納するサーバー側領域」で、確認対象はstorage・宛先照合です。復元前確認・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」を述べ、対象は復元前確認 期限切れ（managem・復元前確）です。監査・StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査）です。照合・ScheduleのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。「storage pool」は「バックアップやアーカイブのデータを格納するサーバー側」を指す用語で、宛先照合 キーマップ（storage・宛先照合）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>storage pool 宛先照合 キーマップ</strong></p><p>検証目的: ポリシードメインのstorage pool 宛先照合 キーマップについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL025
画面・出力には ANR1550I が含まれ、storage pool 宛先照合 キーマップの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL025 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL025
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0510"><h3>storage pool 容量監視 翻訳表</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「storage pool 容量監視 翻訳表」は、バックアップやアーカイブのデータを格納するサーバー側領域を容量監視の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 065を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「storage pool 容量監視 翻訳表」を「reclamation 期限切れ確認 診断採取」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はストレージプール内の空き領域を回収する処理を期限切れ確認する。</li><li>B. 運用時に利用する技術的役割はバックアップやアーカイブのデータを格納するサーバー側領域を容量監視として確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 運用時に利用する技術的役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 容量監でポリシードでBの記述「バックアップやアーカイブのデータを格納するサーバー側領域を容量監視と」に対応する項目は容量監視 翻訳表（storage・ポリシー）です。容量監・翻訳表に関するポリシードメインの仕様は「バックアップやアーカイブのデータを格納するサーバー側領域を容量監視と」で、確認対象はstorage・ポリシードです。recla・診断採取のA:は「ストレージプール内の空き領域を回収する処理を期限切れ確認する」を述べ、対象は期限切れ確認 診断採取（reclama・診断採取）です。変更時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・変更）です。Poliを確認のD:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・確認）です。storをポリシードという用語は「バックアップやアーカイブのデータを格納するサーバー側」を指し、容量監視 翻訳表（storage・ポリシー）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>storage pool 容量監視 翻訳表</strong></p><p>検証目的: ポリシードメインのstorage pool 容量監視 翻訳表について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL065
画面・出力には ANR1550I が含まれ、storage pool 容量監視 翻訳表の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL065 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL065
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0511"><h3>ポリシードメイン Policy Domain ログとの照合 DOM07</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>ログとの照合では ポリシードメイン の ドメイン照会 を主操作として DOM07 を判定します。時刻と対象識別子への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM07 に残します。ログとの照合を補助する ポリシーセット では PolicySet を補助値として DOM07 へ保存します。主判定のログとの照合ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM07 へ残します。証跡照合のログとの照合ではポリシードメインの PolicyDomain と PolicySet を DOM07 に保存します。記録対応のログとの照合ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain ログとの照合 DOM07の設定や表示を読む前に役割を確認します。アーカイブ運用 Archive Operation 構成監査 ARC08ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはArchive Operationで構成監査ではアーカイブ運用のである。アーカイブ運用 Archive Operation 構成監査 ARC08固有の属性も確認対象に含める。</li><li>B. 対象資源に対する働きはSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 対象資源に対する働きはPolicy Domainでログとの照合ではポリシードメインの ドメイン照会からPolicyDomainを読である。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシでログとの照でCの記述「Policy Domainでログとの照合ではポリシードメインの」に対応する項目はログとの照合 DOM07（Policy・ログとの）です。ポリシ・ログとに関するポリシードメインの仕様は「Policy Domainでログとの照合ではポリシードメインの」で、確認対象はPolicy・ログとの照です。Archi・構成監査のA:は「Archive Operationで構成監査ではアーカイブ運用の」を述べ、対象は構成監査 ARC08（Archive・構成監査）です。クライで移行のB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・移行）です。Dataを抑止のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・抑止）です。Poliをログとの照という用語は「Policy Domainでログとの照合ではポリシー」を指し、ログとの照合 DOM07（Policy・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain ログとの照合 DOM07</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて操作とログを対応し、DOM07のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM07 FORMAT=DETAILEDを指定し、DOM07のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM07 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM07
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM07 ACTIVEを指定し、DOM07のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM07 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM07 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE07 FORMAT=DETAILEDを指定し、DOM07のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE07 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE07 Policy Domain Name: DOM07 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0512"><h3>ポリシードメイン Policy Domain 代替経路の確認 DOM10</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>代替経路の確認では ポリシードメイン の ドメイン照会 を主操作として DOM10 を判定します。主経路との役割差への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM10 に残します。代替経路の確認を補助する ポリシーセット では PolicySet を補助値として DOM10 へ保存します。主判定の代替経路の確認ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM10 へ残します。証跡照合の代替経路の確認ではポリシードメインの PolicyDomain と PolicySet を DOM10 に保存します。記録対応の代替経路の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 代替経路の確認 DOM10の役割を調べています。ストレージプール Directory-container Storage Poolの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はDirectory-containeで代替経路の確認ではストレージプールのである。</li><li>B. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>D. 表示や設定で扱う内容はPolicy Domainで代替経路の確認ではポリシードメインのである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで代替経路確でDの記述「Policy Domainで代替経路の確認ではポリシードメインのであ」に対応する項目は代替経路の確認 DOM10（Policy・代替経路）です。ポリシ・代替経に関するポリシードメインの仕様は「Policy Domainで代替経路の確認ではポリシードメインの」で、確認対象はPolicy・代替経路確です。Direc・代替経路確のA:は「Directory-containeで代替経路の確認ではストレージプ」を述べ、対象は代替経路の確認 POOL10（Directo・代替経路）です。サーバで移行のB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・移行）です。照合時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。Poliを代替経路確という用語は「Policy Domainで代替経路の確認ではポリシ」を指し、代替経路の確認 DOM10（Policy・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 代替経路の確認 DOM10</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて代替手段の成立を確認し、DOM10のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM10 FORMAT=DETAILEDを指定し、DOM10のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM10 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM10
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM10 ACTIVEを指定し、DOM10のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM10 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM10 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE10 FORMAT=DETAILEDを指定し、DOM10のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE10 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE10 Policy Domain Name: DOM10 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0513"><h3>ポリシードメイン Policy Domain 依存関係の確認 DOM13</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>依存関係の確認では ポリシードメイン の ドメイン照会 を主操作として DOM13 を判定します。前提資源と後続処理の順序への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM13 に残します。依存関係の確認を補助する ポリシーセット では PolicySet を補助値として DOM13 へ保存します。主判定の依存関係の確認ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM13 へ残します。証跡照合の依存関係の確認ではポリシードメインの PolicyDomain と PolicySet を DOM13 に保存します。記録対応の依存関係の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 依存関係の確認 DOM13を保守記録に説明する必要があります。管理クラス Management Class 性能影響の確認 MC11と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はManagement Classで性能影響の確認では管理クラスのである。</li><li>B. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 保守作業で参照する機能はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 保守作業で参照する機能はPolicy Domainで依存関係の確認ではポリシードメインのである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで依存関係確でDの記述「Policy Domainで依存関係の確認ではポリシードメインのであ」に対応する項目は依存関係の確認 DOM13（Policy・依存関係）です。ポリシ・依存関に関するポリシードメインの仕様は「Policy Domainで依存関係の確認ではポリシードメインの」で、確認対象はPolicy・依存関係確です。Manag・性能影響確のA:は「Management Classで性能影響の確認では管理クラスの」を述べ、対象は性能影響の確認 MC11（Managem・性能影響）です。クライで保守のB:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・保守）です。計画時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・計画）です。Poliを依存関係確という用語は「Policy Domainで依存関係の確認ではポリシ」を指し、依存関係の確認 DOM13（Policy・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 依存関係の確認 DOM13</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて依存資源を点検し、DOM13のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM13 FORMAT=DETAILEDを指定し、DOM13のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM13 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM13
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM13 ACTIVEを指定し、DOM13のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM13 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM13 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE13 FORMAT=DETAILEDを指定し、DOM13のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE13 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE13 Policy Domain Name: DOM13 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0514"><h3>ポリシードメイン Policy Domain 停止前の確認 DOM14</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>停止前の確認では ポリシードメイン の ポリシーセット を主操作として DOM14 を判定します。処理中資源と未完了要求への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM14 に残します。停止前の確認を補助する ノード所属 では NodeName を補助値として DOM14 へ保存します。主判定の停止前の確認ではポリシードメインの ポリシーセット から PolicySet を読み DOM14 へ残します。証跡照合の停止前の確認ではポリシードメインの PolicySet と NodeName を DOM14 に保存します。記録対応の停止前の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 停止前の確認 DOM14に関する障害切り分けの前提を確認しています。コピーグループ Backup and Archive Copy Groupの機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。</li><li>B. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 障害切り分けに用いる役割はPolicy Domainで停止前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで停止確認でCの記述「Policy Domainで停止前の確認ではポリシードメインの」に対応する項目は停止前の確認 DOM14（Policy・停止確認）です。ポリシ・停止前に関するポリシードメインの仕様は「Policy Domainで停止前の確認ではポリシードメインの」で、確認対象はPolicy・停止確認です。Backu・構成監査のA:は「Backup andで構成監査ではコピーグループの」を述べ、対象は構成監査 CG08（Backup・構成監査）です。ポリシで移行のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・移行）です。Expiを解析のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・解析）です。Poliを停止確認という用語は「Policy Domainで停止前の確認ではポリシー」を指し、停止前の確認 DOM14（Policy・停止確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 停止前の確認 DOM14</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて安全な停止条件を確認し、DOM14のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM14 ACTIVEを指定し、DOM14のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM14 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM14 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE14 FORMAT=DETAILEDを指定し、DOM14のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE14 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE14 Policy Domain Name: DOM14 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM14 FORMAT=DETAILEDを指定し、DOM14のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM14 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM14
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0515"><h3>ポリシードメイン Policy Domain 再始動後の確認 DOM15</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>再始動後の確認では ポリシードメイン の ノード所属 を主操作として DOM15 を判定します。再開点と未処理データへの注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM15 に残します。再始動後の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM15 へ保存します。主判定の再始動後の確認ではポリシードメインの ノード所属 から NodeName を読み DOM15 へ残します。証跡照合の再始動後の確認ではポリシードメインの NodeName と PolicyDomain を DOM15 に保存します。記録対応の再始動後の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 再始動後の確認 DOM15の設定や表示を読む前に役割を確認します。アーカイブ運用 Archive Operation 通常状態の確認 ARC01ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはArchive Operationで通常状態の確認ではアーカイブ運用のである。アーカイブ運用 Archive Operation 通常状態の確認固有の属性も確認対象に含める。</li><li>B. 状態を読み取るための働きはManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 状態を読み取るための働きはSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. 状態を読み取るための働きはPolicy Domainで再始動後の確認ではポリシードメインの ノード所属からNodeNameを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで再始動確認でDの記述「Policy Domainで再始動後の確認ではポリシードメインの」に対応する項目は再始動後の確認 DOM15（Policy・再始動確）です。ポリシ・再始動に関するポリシードメインの仕様は「Policy Domainで再始動後の確認ではポリシードメインの」で、確認対象はPolicy・再始動確認です。Archi・通常状態確のA:は「Archive Operationで通常状態の確認ではアーカイブ運用」を述べ、対象は通常状態の確認 ARC01（Archive・通常状態）です。ポリシで監査のB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・監査）です。照合時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。Poliを再始動確認という用語は「Policy Domainで再始動後の確認ではポリシ」を指し、再始動後の確認 DOM15（Policy・再始動確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 再始動後の確認 DOM15</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて再始動結果を検証し、DOM15のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE15 FORMAT=DETAILEDを指定し、DOM15のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE15 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE15 Policy Domain Name: DOM15 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM15 FORMAT=DETAILEDを指定し、DOM15のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM15 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM15
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM15 ACTIVEを指定し、DOM15のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM15 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM15 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0516"><h3>ポリシードメイン Policy Domain 変更前の確認 DOM02</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>変更前の確認では ポリシードメイン の ポリシーセット を主操作として DOM02 を判定します。変更対象と非対象の境界への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM02 に残します。変更前の確認を補助する ノード所属 では NodeName を補助値として DOM02 へ保存します。主判定の変更前の確認ではポリシードメインの ポリシーセット から PolicySet を読み DOM02 へ残します。証跡照合の変更前の確認ではポリシードメインの PolicySet と NodeName を DOM02 に保存します。記録対応の変更前の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 変更前の確認 DOM02の役割を調べています。ストレージプール Directory-container Storage Poolの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はPolicy Domainで変更前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はDirectory-containeで障害切り分けではストレージプールのである。</li><li>C. 障害切り分けに用いる役割はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。サーバー日次運用 Node Name 0283固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで変更確認でAの記述「Policy Domainで変更前の確認ではポリシードメインの」に対応する項目は変更前の確認 DOM02（Policy・変更確認）です。ポリシ・変更前に関するポリシードメインの仕様は「Policy Domainで変更前の確認ではポリシードメインの」で、確認対象はPolicy・変更確認です。ストレでストレージのB:は「Directory-containeで障害切り分けではストレージプー」を述べ、対象は障害切り分け POOL04（Directo・ストレー）です。移行時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・移行）です。Nodeを抑止のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・抑止）です。Poliを変更確認という用語は「Policy Domainで変更前の確認ではポリシー」を指し、変更前の確認 DOM02（Policy・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 変更前の確認 DOM02</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて変更前の証跡を保存し、DOM02のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM02 ACTIVEを指定し、DOM02のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM02 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM02 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE02 FORMAT=DETAILEDを指定し、DOM02のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE02 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE02 Policy Domain Name: DOM02 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM02 FORMAT=DETAILEDを指定し、DOM02のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM02 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM02
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0517"><h3>ポリシードメイン Policy Domain 変更後の確認 DOM03</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>変更後の確認では ポリシードメイン の ノード所属 を主操作として DOM03 を判定します。反映値と残存値への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM03 に残します。変更後の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM03 へ保存します。主判定の変更後の確認ではポリシードメインの ノード所属 から NodeName を読み DOM03 へ残します。証跡照合の変更後の確認ではポリシードメインの NodeName と PolicyDomain を DOM03 に保存します。記録対応の変更後の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 変更後の確認 DOM03について構成や状態を確認します。ポリシードメイン Policy Domain 再始動後の確認 DOM15ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはPolicy Domainで再始動後の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>B. 状態を読み取るための働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 状態を読み取るための働きはManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 状態を読み取るための働きはPolicy Domainで変更後の確認ではポリシードメインの ノード所属からNodeNameを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで変更確認でDの記述「Policy Domainで変更後の確認ではポリシードメインの」に対応する項目は変更後の確認 DOM03（Policy・変更確認）です。ポリシ・変更後に関するポリシードメインの仕様は「Policy Domainで変更後の確認ではポリシードメインの」で、確認対象はPolicy・変更確認です。Polic・再始動確認のA:は「Policy Domainで再始動後の確認ではポリシードメインの」を述べ、対象は再始動後の確認 DOM15（Policy・再始動確）です。サーバで監査のB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査）です。照合時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・照合）です。Poliを変更確認という用語は「Policy Domainで変更後の確認ではポリシー」を指し、変更後の確認 DOM03（Policy・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 変更後の確認 DOM03</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて変更結果を検証し、DOM03のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE03 FORMAT=DETAILEDを指定し、DOM03のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE03 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE03 Policy Domain Name: DOM03 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM03 FORMAT=DETAILEDを指定し、DOM03のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM03 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM03
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM03 ACTIVEを指定し、DOM03のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM03 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM03 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0518"><h3>ポリシードメイン Policy Domain 引継ぎ記録 DOM09</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>引継ぎ記録では ポリシードメイン の ノード所属 を主操作として DOM09 を判定します。次担当者が追跡できる証跡への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM09 に残します。引継ぎ記録を補助する ドメイン照会 では PolicyDomain を補助値として DOM09 へ保存します。主判定の引継ぎ記録ではポリシードメインの ノード所属 から NodeName を読み DOM09 へ残します。証跡照合の引継ぎ記録ではポリシードメインの NodeName と PolicyDomain を DOM09 に保存します。記録対応の引継ぎ記録ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「ポリシードメイン Policy Domain 引継ぎ記録 DOM09」を「ストレージプール Directory-container Storage Pool」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はDirectory-containeで構成監査ではストレージプールのである。</li><li>B. 運用時に利用する技術的役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス Policy Set 0062固有の属性も確認対象に含める。</li><li>C. 運用時に利用する技術的役割はCopy Groupのコピーグループと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 運用時に利用する技術的役割はPolicy Domainで引継ぎ記録ではポリシードメインの ノード所属からNodeNameを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシでポリシードでDの記述「Policy Domainで引継ぎ記録ではポリシードメインの」に対応する項目は引継ぎ記録 DOM09（Policy・ポリシー）です。ポリシ・引継ぎに関するポリシードメインの仕様は「Policy Domainで引継ぎ記録ではポリシードメインの」で、確認対象はPolicy・ポリシードです。Direc・構成監査のA:は「Directory-containeで構成監査ではストレージプールの」を述べ、対象は構成監査 POOL08（Directo・構成監査）です。ポリシで監査のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・監査）です。解除時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解除）です。Poliをポリシードという用語は「Policy Domainで引継ぎ記録ではポリシード」を指し、引継ぎ記録 DOM09（Policy・ポリシー）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 引継ぎ記録 DOM09</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて再現可能な記録を作成し、DOM09のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE09 FORMAT=DETAILEDを指定し、DOM09のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE09 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE09 Policy Domain Name: DOM09 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM09 FORMAT=DETAILEDを指定し、DOM09のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM09 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM09
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM09 ACTIVEを指定し、DOM09のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM09 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM09 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0519"><h3>ポリシードメイン Policy Domain 復旧後の確認 DOM06</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>復旧後の確認では ポリシードメイン の ノード所属 を主操作として DOM06 を判定します。再発していないことを示す値への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM06 に残します。復旧後の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM06 へ保存します。主判定の復旧後の確認ではポリシードメインの ノード所属 から NodeName を読み DOM06 へ残します。証跡照合の復旧後の確認ではポリシードメインの NodeName と PolicyDomain を DOM06 に保存します。記録対応の復旧後の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 復旧後の確認 DOM06に関する障害切り分けの前提を確認しています。バックアップ運用 Incremental Backup 変更後の確認 BKP03の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはIncremental Backupで変更後の確認ではバックアップ運用のである。</li><li>B. 機能の説明としてはPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス Policy Set 0122固有の属性も確認対象に含める。</li><li>D. 機能の説明としてはAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで復旧確認でBの記述「Policy Domainで復旧後の確認ではポリシードメインの」に対応する項目は復旧後の確認 DOM06（Policy・復旧確認）です。ポリシ・復旧後に関するポリシードメインの仕様は「Policy Domainで復旧後の確認ではポリシードメインの」で、確認対象はPolicy・復旧確認です。Incre・変更確認のA:は「Incremental Backupで変更後の確認ではバックアップ運」を述べ、対象は変更後の確認 BKP03（Increme・変更確認）です。診断時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断）です。Assoを照合のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。Poliを復旧確認という用語は「Policy Domainで復旧後の確認ではポリシー」を指し、復旧後の確認 DOM06（Policy・復旧確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 復旧後の確認 DOM06</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて復旧後の安定性を確認し、DOM06のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE06 FORMAT=DETAILEDを指定し、DOM06のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE06 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE06 Policy Domain Name: DOM06 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM06 FORMAT=DETAILEDを指定し、DOM06のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM06 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM06
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM06 ACTIVEを指定し、DOM06のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM06 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM06 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0520"><h3>ポリシードメイン Policy Domain 復旧準備 DOM05</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>復旧準備では ポリシードメイン の ポリシーセット を主操作として DOM05 を判定します。再開前に必要な整合性への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM05 に残します。復旧準備を補助する ノード所属 では NodeName を補助値として DOM05 へ保存します。主判定の復旧準備ではポリシードメインの ポリシーセット から PolicySet を読み DOM05 へ残します。証跡照合の復旧準備ではポリシードメインの PolicySet と NodeName を DOM05 に保存します。記録対応の復旧準備ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 復旧準備 DOM05を保守記録に説明する必要があります。管理クラス Management Class 性能影響の確認 MC11と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はManagement Classで性能影響の確認では管理クラスのである。管理クラス Management Class 性能影響の確認 MC11固有の属性も確認対象に含める。</li><li>B. 仕様上の役割はPolicy Domainで復旧準備ではポリシードメインの ポリシーセットからPolicySetを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 仕様上の役割はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで復旧準備でBの記述「Policy Domainで復旧準備ではポリシードメインの」に対応する項目は復旧準備 DOM05（Policy・復旧準備）です。ポリシ・復旧準に関するポリシードメインの仕様は「Policy Domainで復旧準備ではポリシードメインの」で、確認対象はPolicy・復旧準備です。Manag・性能影響確のA:は「Management Classで性能影響の確認では管理クラスの」を述べ、対象は性能影響の確認 MC11（Managem・性能影響）です。監査時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・監査）です。Assoを照合のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。Poliを復旧準備という用語は「Policy Domainで復旧準備ではポリシードメ」を指し、復旧準備 DOM05（Policy・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 復旧準備 DOM05</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて復旧条件を確認し、DOM05のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM05 ACTIVEを指定し、DOM05のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM05 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM05 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE05 FORMAT=DETAILEDを指定し、DOM05のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE05 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE05 Policy Domain Name: DOM05 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM05 FORMAT=DETAILEDを指定し、DOM05のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM05 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM05
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0521"><h3>ポリシードメイン Policy Domain 性能影響の確認 DOM11</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>性能影響の確認では ポリシードメイン の ポリシーセット を主操作として DOM11 を判定します。処理時間と滞留箇所への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM11 に残します。性能影響の確認を補助する ノード所属 では NodeName を補助値として DOM11 へ保存します。主判定の性能影響の確認ではポリシードメインの ポリシーセット から PolicySet を読み DOM11 へ残します。証跡照合の性能影響の確認ではポリシードメインの PolicySet と NodeName を DOM11 に保存します。記録対応の性能影響の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 性能影響の確認 DOM11について構成や状態を確認します。アーカイブ運用 Archive Operation ログとの照合 ARC07ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はArchive Operationでログとの照合ではアーカイブ運用のである。</li><li>B. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 一次資料が示す主目的はPolicy Domainで性能影響の確認ではポリシードメインのである。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで性能影響確でCの記述「Policy Domainで性能影響の確認ではポリシードメインのであ」に対応する項目は性能影響の確認 DOM11（Policy・性能影響）です。ポリシ・性能影に関するポリシードメインの仕様は「Policy Domainで性能影響の確認ではポリシードメインの」で、確認対象はPolicy・性能影響確です。Archi・ログとの照のA:は「Archive Operationでログとの照合ではアーカイブ運用の」を述べ、対象はログとの照合 ARC07（Archive・ログとの）です。サーバで診断のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・診断）です。Starを抑止のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・抑止）です。Poliを性能影響確という用語は「Policy Domainで性能影響の確認ではポリシ」を指し、性能影響の確認 DOM11（Policy・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 性能影響の確認 DOM11</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて負荷と待ちを確認し、DOM11のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM11 ACTIVEを指定し、DOM11のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM11 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM11 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE11 FORMAT=DETAILEDを指定し、DOM11のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE11 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE11 Policy Domain Name: DOM11 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM11 FORMAT=DETAILEDを指定し、DOM11のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM11 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM11
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0522"><h3>ポリシードメイン Policy Domain 構成監査 DOM08</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>構成監査では ポリシードメイン の ポリシーセット を主操作として DOM08 を判定します。定義値と稼働値の一致への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM08 に残します。構成監査を補助する ノード所属 では NodeName を補助値として DOM08 へ保存します。主判定の構成監査ではポリシードメインの ポリシーセット から PolicySet を読み DOM08 へ残します。証跡照合の構成監査ではポリシードメインの PolicySet と NodeName を DOM08 に保存します。記録対応の構成監査ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 構成監査 DOM08を同一分類の管理クラス Management Class 構成監査 MC08と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はPolicy Domainで構成監査ではポリシードメインの ポリシーセットからPolicySetを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はManagement Classで構成監査では管理クラスの クライアント詳細からDefaultManagemである。</li><li>C. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>D. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで構成監査でAの記述「Policy Domainで構成監査ではポリシードメインの」に対応する項目は構成監査 DOM08（Policy・構成監査）です。ポリシ・構成監に関するポリシードメインの仕様は「Policy Domainで構成監査ではポリシードメインの」で、確認対象はPolicy・構成監査です。管理クで構成監査のB:は「Management Classで構成監査では管理クラスの」を述べ、対象は構成監査 MC08（Managem・構成監査）です。監査時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・監査）です。Assoを解析のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・解析）です。Poliを構成監査という用語は「Policy Domainで構成監査ではポリシードメ」を指し、構成監査 DOM08（Policy・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 構成監査 DOM08</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて構成差分を監査し、DOM08のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM08 ACTIVEを指定し、DOM08のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM08 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM08 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE08 FORMAT=DETAILEDを指定し、DOM08のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE08 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE08 Policy Domain Name: DOM08 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM08 FORMAT=DETAILEDを指定し、DOM08のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM08 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM08
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0523"><h3>ポリシードメイン Policy Domain 権限境界の確認 DOM12</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>権限境界の確認では ポリシードメイン の ノード所属 を主操作として DOM12 を判定します。参照操作と変更操作の分離への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM12 に残します。権限境界の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM12 へ保存します。主判定の権限境界の確認ではポリシードメインの ノード所属 から NodeName を読み DOM12 へ残します。証跡照合の権限境界の確認ではポリシードメインの NodeName と PolicyDomain を DOM12 に保存します。記録対応の権限境界の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 権限境界の確認 DOM12の技術的な意味を資料で確認するとき、コピーグループ Backup and Archive Copy Groupとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はBackup andで権限境界の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。</li><li>B. 構成を確認する際の意味はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>D. 構成を確認する際の意味はPolicy Domainで権限境界の確認ではポリシードメインの ノード所属からNodeNameを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで権限境界確でDの記述「Policy Domainで権限境界の確認ではポリシードメインの」に対応する項目は権限境界の確認 DOM12（Policy・権限境界）です。ポリシ・権限境に関するポリシードメインの仕様は「Policy Domainで権限境界の確認ではポリシードメインの」で、確認対象はPolicy・権限境界確です。Backu・権限境界確のA:は「Backup andで権限境界の確認ではコピーグループの」を述べ、対象は権限境界の確認 CG12（Backup・権限境界）です。サーバで診断のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・診断）です。照合時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。Poliを権限境界確という用語は「Policy Domainで権限境界の確認ではポリシ」を指し、権限境界の確認 DOM12（Policy・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 権限境界の確認 DOM12</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて実行権限を点検し、DOM12のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE12 FORMAT=DETAILEDを指定し、DOM12のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE12 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE12 Policy Domain Name: DOM12 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM12 FORMAT=DETAILEDを指定し、DOM12のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM12 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM12
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM12 ACTIVEを指定し、DOM12のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM12 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM12 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0524"><h3>ポリシードメイン Policy Domain 通常状態の確認 DOM01</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>通常状態の確認では ポリシードメイン の ドメイン照会 を主操作として DOM01 を判定します。基準値と現在値の差への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM01 に残します。通常状態の確認を補助する ポリシーセット では PolicySet を補助値として DOM01 へ保存します。主判定の通常状態の確認ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM01 へ残します。証跡照合の通常状態の確認ではポリシードメインの PolicyDomain と PolicySet を DOM01 に保存します。記録対応の通常状態の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「ポリシードメイン Policy Domain 通常状態の確認 DOM01」を「コピーグループ Backup and Archive Copy Group」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はBackup andで通常状態の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。</li><li>B. 保守作業で参照する機能はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 保守作業で参照する機能はPolicy Domainで通常状態の確認ではポリシードメインのである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシで通常状態確でCの記述「Policy Domainで通常状態の確認ではポリシードメインのであ」に対応する項目は通常状態の確認 DOM01（Policy・通常状態）です。ポリシ・通常状に関するポリシードメインの仕様は「Policy Domainで通常状態の確認ではポリシードメインの」で、確認対象はPolicy・通常状態確です。Backu・通常状態確のA:は「Backup andで通常状態の確認ではコピーグループの」を述べ、対象は通常状態の確認 CG01（Backup・通常状態）です。ポリシで復旧のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・復旧）です。Starを計画のD:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・計画）です。Poliを通常状態確という用語は「Policy Domainで通常状態の確認ではポリシ」を指し、通常状態の確認 DOM01（Policy・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 通常状態の確認 DOM01</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて通常状態を確定し、DOM01のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM01 FORMAT=DETAILEDを指定し、DOM01のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM01 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM01
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM01 ACTIVEを指定し、DOM01のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM01 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM01 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE01 FORMAT=DETAILEDを指定し、DOM01のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE01 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE01 Policy Domain Name: DOM01 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0525"><h3>ポリシードメイン Policy Domain 障害切り分け DOM04</h3><p class="kb-meta">分類: ポリシードメイン ・ 難易度: 初級</p><p>障害切り分けでは ポリシードメイン の ドメイン照会 を主操作として DOM04 を判定します。最初に失敗した処理への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM04 に残します。障害切り分けを補助する ポリシーセット では PolicySet を補助値として DOM04 へ保存します。主判定の障害切り分けではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM04 へ残します。証跡照合の障害切り分けではポリシードメインの PolicyDomain と PolicySet を DOM04 に保存します。記録対応の障害切り分けではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ポリシードメイン Policy Domain 障害切り分け DOM04の技術的な意味を資料で確認するとき、ストレージプール Directory-container Storage Poolとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はDirectory-containeで再始動後の確認ではストレージプールのである。</li><li>B. 管理対象との関係を表す説明はPolicy Domainで障害切り分けではポリシードメインの ドメイン照会からPolicyDomainを読である。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。サーバー日次運用 Storage Pool 0325固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ポリシでポリシードでBの記述「Policy Domainで障害切り分けではポリシードメインの」に対応する項目は障害切り分け DOM04（Policy・ポリシー）です。ポリシ・障害切に関するポリシードメインの仕様は「Policy Domainで障害切り分けではポリシードメインの」で、確認対象はPolicy・ポリシードです。Direc・再始動確認のA:は「Directory-containeで再始動後の確認ではストレージプ」を述べ、対象は再始動後の確認 POOL15（Directo・再始動確）です。診断時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断）です。Storを計画のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・計画）です。Poliをポリシードという用語は「Policy Domainで障害切り分けではポリシー」を指し、障害切り分け DOM04（Policy・ポリシー）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ポリシードメイン Policy Domain 障害切り分け DOM04</strong></p><p>検証目的: ポリシードメインのPolicy Domainについて障害範囲を限定し、DOM04のDomain NameとActivated Policy Setを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM04 FORMAT=DETAILEDを指定し、DOM04のドメイン照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN DOM04 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM04
Activated Policy Set: ACTIVE
Number of Nodes: 12
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM04 ACTIVEを指定し、DOM04のポリシーセットを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY POLICYSET DOM04 ACTIVE
→ Enter を押す
［画面・出力］
Policy Domain Name: DOM04 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE04 FORMAT=DETAILEDを指定し、DOM04のノード所属を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY NODE NODE04 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Node Name: NODE04 Policy Domain Name: DOM04 Locked: No
画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## リストア確認


<section class="kb-item" id="c14-i0526"><h3>activity log 宛先照合 キュー状態</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「activity log 宛先照合 キュー状態」は、サーバー操作とメッセージを追跡するログを宛先照合の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 040を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> activity log 宛先照合 キュー状態を同一分類のmanagement class 復元前確認 期限切れと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。</li><li>B. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. コマンドまたは機能の用途はサーバー操作とメッセージを追跡するログである。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 宛先照合・activityでCの記述「サーバー操作とメッセージを追跡するログである」に対応する項目は宛先照合 キュー状態（activit・宛先照合）です。宛先・キューに関するリストア確認の仕様は「サーバー操作とメッセージを追跡するログ」で、確認対象はactivit・宛先照合です。復元前確認・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」を述べ、対象は復元前確認 期限切れ（managem・復元前確）です。変更・NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・変更）です。照合・AssociatのD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。「activity log」は「サーバー操作とメッセージを追跡するログ」を指す用語で、宛先照合 キュー状態（activit・宛先照合）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>activity log 宛先照合 キュー状態</strong></p><p>検証目的: リストア確認のactivity log 宛先照合 キュー状態について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL040
画面・出力には ANR1550I が含まれ、activity log 宛先照合 キュー状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL040 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL040
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0527"><h3>activity log 容量監視 アーカイブ</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「activity log 容量監視 アーカイブ」は、サーバー操作とメッセージを追跡するログを容量監視の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 080を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> activity log 容量監視 アーカイブを同一分類の管理クラス Management Class 停止前の確認 MC14と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。</li><li>B. 構成を確認する際の意味はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 構成を確認する際の意味はサーバー操作とメッセージを追跡するログを容量監視として確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 容量監でリストアでCの記述「サーバー操作とメッセージを追跡するログを容量監視として確認する」に対応する項目は容量監視 アーカイブ（activit・リストア）です。容量監・アーカに関するリストア確認の仕様は「サーバー操作とメッセージを追跡するログを容量監視として確認する」で、確認対象はactivit・リストアです。Manag・停止確認のA:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Managem・停止確認）です。サーバで監査のB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査）です。Actiを解析のD:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・解析）です。actiをリストアという用語は「サーバー操作とメッセージを追跡するログを容量監視とし」を指し、容量監視 アーカイブ（activit・リストア）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>activity log 容量監視 アーカイブ</strong></p><p>検証目的: リストア確認のactivity log 容量監視 アーカイブについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL080
画面・出力には ANR1550I が含まれ、activity log 容量監視 アーカイブの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL080 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL080
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0528"><h3>archive copy group 保存期間確認 証明書検査</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「archive copy group 保存期間確認 証明書検査」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を保存期間確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 024を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> archive copy group 保存期間確認 証明書検査を同一分類のポリシードメイン Policy Domain 通常状態の確認 DOM01と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はPolicy Domainで通常状態の確認ではポリシードメインのである。</li><li>B. 管理対象との関係を表す説明はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>C. 管理対象との関係を表す説明はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 管理対象との関係を表す説明はアーカイブコピーの保存期間と宛先を定めるコピー規則である。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保存期間確・archiveでDの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則である」に対応する項目は保存期間確認 証明書検査（archive・保存期間）です。保存期・証明書に関するリストア確認の仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則」で、確認対象はarchive・保存期間確です。通常状態確・PolicyのA:は「Policy Domainで通常状態の確認ではポリシードメインの」を述べ、対象は通常状態の確認 DOM01（Policy・通常状態）です。監査・EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・監査）です。照合・StartのC:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・照合）です。「archive copy group」は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を指す用語で、保存期間確認 証明書検査（archive・保存期間）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>archive copy group 保存期間確認 証明書検査</strong></p><p>検証目的: リストア確認のarchive copy group 保存期間確認 証明書検査について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL024
画面・出力には ANR1550I が含まれ、archive copy group 保存期間確認 証明書検査の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL024 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL024
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0529"><h3>archive copy group 復元前確認 送信操作</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「archive copy group 復元前確認 送信操作」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 064を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> archive copy group 復元前確認 送信操作を同一分類のbackup copy group コマンド証跡 収集装置と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はアーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。</li><li>C. コマンドまたは機能の用途はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. コマンドまたは機能の用途はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復元前で復元前確認でAの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認する」に対応する項目は復元前確認 送信操作（archive・復元前確）です。復元前・送信操に関するリストア確認の仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認する」で、確認対象はarchive・復元前確認です。コマンでポリシードのB:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backup・ポリシー）です。変更時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・変更）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。archを復元前確認という用語は「アーカイブコピーの保存期間と宛先を定めるコピー規則を」を指し、復元前確認 送信操作（archive・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>archive copy group 復元前確認 送信操作</strong></p><p>検証目的: リストア確認のarchive copy group 復元前確認 送信操作について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL064
画面・出力には ANR1550I が含まれ、archive copy group 復元前確認 送信操作の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL064 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL064
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0530"><h3>management class 宛先照合 初期同期</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「management class 宛先照合 初期同期」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を宛先照合の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL032を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> management class 宛先照合 初期同期を同一分類のコピーグループ Backup and Archive Copy Groupと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。</li><li>B. 構成を確認する際の意味はファイルのバックアップ先や保存期間を決めるポリシー要素である。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はDBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・再始動確認に使うである。</li><li>D. 構成を確認する際の意味はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 宛先照合・managemeでBの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素である」に対応する項目は宛先照合 初期同期（managem・宛先照合）です。宛先・初期同に関するリストア確認の仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素」で、確認対象はmanagem・宛先照合です。変更確認・BackupのA:は「Backup andで変更前の確認ではコピーグループの」を述べ、対象は変更前の確認 CG02（Backup・変更確認）です。再始動確認・DBのC:は「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は再始動後の確認 DBBK15（DB・再始動確）です。照合・DIRMCのD:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合）です。「management class」は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指す用語で、宛先照合 初期同期（managem・宛先照合）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>management class 宛先照合 初期同期</strong></p><p>検証目的: リストア確認のmanagement class 宛先照合 初期同期について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL032
画面・出力には ANR1550I が含まれ、management class 宛先照合 初期同期の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL032 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL032
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0531"><h3>management class 容量監視 分散定義</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「management class 容量監視 分散定義」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL072を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> management class 容量監視 分散定義を同一分類のコピーグループ Backup and Archive Copy Groupと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はBackup andで復旧準備ではコピーグループの アーカイブグループからRetainVersionを読みである。</li><li>B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>D. 管理対象との関係を表す説明はファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視として確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 容量監でリストアでDの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視とし」に対応する項目は容量監視 分散定義（managem・リストア）です。容量監・分散定に関するリストア確認の仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視とし」で、確認対象はmanagem・リストアです。Backu・復旧準備のA:は「Backup andで復旧準備ではコピーグループの」を述べ、対象は復旧準備 CG05（Backup・復旧準備）です。サーバで変更のB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・変更）です。解析時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・解析）です。manaをリストアという用語は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指し、容量監視 分散定義（managem・リストア）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>management class 容量監視 分散定義</strong></p><p>検証目的: リストア確認のmanagement class 容量監視 分散定義について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL072
画面・出力には ANR1550I が含まれ、management class 容量監視 分散定義の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL072 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL072
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0532"><h3>node 期限切れ確認 更新配布</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「node 期限切れ確認 更新配布」は、サーバーへ登録されたクライアントを表す管理単位を期限切れ確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE056を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> node 期限切れ確認 更新配布を同一分類のポリシードメイン Policy Domain 復旧後の確認 DOM06と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>B. 構成を確認する際の意味はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 構成を確認する際の意味はサーバーへ登録されたクライアントを表す管理単位を期限切れ確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 期限切で期限切れ確でCの記述「サーバーへ登録されたクライアントを表す管理単位を期限切れ確認する」に対応する項目は期限切れ確認 更新配布（node・期限切れ）です。期限切・更新配に関するリストア確認の仕様は「サーバーへ登録されたクライアントを表す管理単位を期限切れ確認する」で、確認対象はnode・期限切れ確です。Polic・復旧確認のA:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Policy・復旧確認）です。ポリシで移行のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・移行）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。nodeを期限切れ確という用語は「サーバーへ登録されたクライアントを表す管理単位を期限」を指し、期限切れ確認 更新配布（node・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>node 期限切れ確認 更新配布</strong></p><p>検証目的: リストア確認のnode 期限切れ確認 更新配布について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL056
画面・出力には ANR1550I が含まれ、node 期限切れ確認 更新配布の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL056 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL056
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0533"><h3>node 状態確認 構成配布</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「node 状態確認 構成配布」は、サーバーへ登録されたクライアントを表す管理単位を状態確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE016を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> node 状態確認 構成配布を同一分類のreclamation 状態確認 承認待ちと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はサーバーへ登録されたクライアントを表す管理単位である。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はストレージプール内の空き領域を回収する処理である。</li><li>C. コマンドまたは機能の用途はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. コマンドまたは機能の用途はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 状態確認・nodeでAの記述「サーバーへ登録されたクライアントを表す管理単位である」に対応する項目は状態確認 構成配布（node・状態確認）です。状態・構成配に関するリストア確認の仕様は「サーバーへ登録されたクライアントを表す管理単位」で、確認対象はnode・状態確認です。状態確認・reclamatのB:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は状態確認 承認待ち（reclama・状態確認）です。巡回・StartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・巡回）です。保護・ServerのD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保護）です。「node」は「サーバーへ登録されたクライアントを表す管理単位」を指す用語で、状態確認 構成配布（node・状態確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>node 状態確認 構成配布</strong></p><p>検証目的: リストア確認のnode 状態確認 構成配布について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL016
画面・出力には ANR1550I が含まれ、node 状態確認 構成配布の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL016 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL016
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0534"><h3>reclamation コマンド証跡 差分確認</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「reclamation コマンド証跡 差分確認」は、ストレージプール内の空き領域を回収する処理をコマンド証跡の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR008Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> reclamation コマンド証跡 差分確認を同一分類のmanagement class ノード割当確認 オンライン表示と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確認する。</li><li>B. 構成を確認する際の意味はストレージプール内の空き領域を回収する処理をコマンド証跡として確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 構成を確認する際の意味はStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 差分確認・reclamatでBの記述「ストレージプール内の空き領域を回収する処理をコマンド証跡として確認す」に対応する項目はコマンド証跡 差分確認（reclama・差分確認）です。コマン・差分に関するリストア確認の仕様は「ストレージプール内の空き領域を回収する処理をコマンド証跡として確認す」で、確認対象はreclama・差分確認です。オンライン・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確」を述べ、対象はノード割当確認 オンライン表示（managem・オンライ）です。棚卸・ScheduleのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・棚卸）です。保護・StartのD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護）です。「reclamation」は「ストレージプール内の空き領域を回収する処理をコマンド」を指す用語で、コマンド証跡 差分確認（reclama・差分確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>reclamation コマンド証跡 差分確認</strong></p><p>検証目的: リストア確認のreclamation コマンド証跡 差分確認について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL008
画面・出力には ANR1550I が含まれ、reclamation コマンド証跡 差分確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL008 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL008
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0535"><h3>reclamation ノード割当確認 プール宛先</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の リストア確認 で扱う「reclamation ノード割当確認 プール宛先」は、ストレージプール内の空き領域を回収する処理をノード割当確認の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR048Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> reclamation ノード割当確認 プール宛先を同一分類の管理クラス Management Class 権限境界の確認 MC12と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。</li><li>B. 管理対象との関係を表す説明はストレージプール内の空き領域を回収する処理をノード割当確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ノード割当・reclamatでBの記述「ストレージプール内の空き領域を回収する処理をノード割当確認する」に対応する項目はノード割当確認 プール宛先（reclama・ノード割）です。ノード・プールに関するリストア確認の仕様は「ストレージプール内の空き領域を回収する処理をノード割当確認する」で、確認対象はreclama・ノード割当です。権限境界確・ManagemeのA:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。復旧・DatabaseのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・復旧）です。保護・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・保護）です。「reclamation」は「ストレージプール内の空き領域を回収する処理をノード割」を指す用語で、ノード割当確認 プール宛先（reclama・ノード割）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>reclamation ノード割当確認 プール宛先</strong></p><p>検証目的: リストア確認のreclamation ノード割当確認 プール宛先について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL048
画面・出力には ANR1550I が含まれ、reclamation ノード割当確認 プール宛先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL048 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL048
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0536"><h3>リストア確認 Client Restore ログとの照合 RST07</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>ログとの照合では リストア確認 の 候補照会 を主操作として RST07 を判定します。時刻と対象識別子への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST07 に残します。ログとの照合を補助する 別名復元 では restored を補助値として RST07 へ保存します。主判定のログとの照合ではリストア確認の 候補照会 から MgmtClass を読み RST07 へ残します。証跡照合のログとの照合ではリストア確認の MgmtClass と restored を RST07 に保存します。記録対応のログとの照合ではリストア確認の Restore CountとFailed Count の証跡へ RST07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore ログとの照合 RST07を同一分類のリストア確認 Client Restore 引継ぎ記録 RST09と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はClient Restoreで引継ぎ記録ではリストア確認の 活動ログからRestoreを読みである。</li><li>B. 管理対象との関係を表す説明はClient Restoreでログとの照合ではリストア確認の 候補照会からMgmtClassを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 管理対象との関係を表す説明はファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確認する。management class ノード割当確認 オンライン表示固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ログとの対象ClienでBの記述「Client Restoreでログとの照合ではリストア確認の」に対応する項目はログとの照合 RST07（Client・ログとの）です。リスト・ログとに関するリストア確認の仕様は「Client Restoreでログとの照合ではリストア確認の」で、確認対象はClient・ログとの照です。Clien・リストア確のA:は「Client Restoreで引継ぎ記録ではリストア確認の」を述べ、対象は引継ぎ記録 RST09（Client・リストア）です。保護時のActioのC:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・保護）です。manaをオンラインのD:は「ファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確」を述べ、対象はノード割当確認 オンライン表示（managem・オンライ）です。Clieをログとの照という用語は「Client Restoreでログとの照合ではリスト」を指し、ログとの照合 RST07（Client・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore ログとの照合 RST07</strong></p><p>検証目的: リストア確認のClient Restoreについて操作とログを対応し、RST07のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST07の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST07の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST07の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE07 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
② ステップ2 の restored が画面・出力に表示されること
③ ステップ3 の Restore が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0537"><h3>リストア確認 Client Restore 代替経路の確認 RST10</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>代替経路の確認では リストア確認 の 候補照会 を主操作として RST10 を判定します。主経路との役割差への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST10 に残します。代替経路の確認を補助する 別名復元 では restored を補助値として RST10 へ保存します。主判定の代替経路の確認ではリストア確認の 候補照会 から MgmtClass を読み RST10 へ残します。証跡照合の代替経路の確認ではリストア確認の MgmtClass と restored を RST10 に保存します。記録対応の代替経路の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 代替経路の確認 RST10について構成や状態を確認します。サーバーDB・DR Server Database Backup 性能影響の確認ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはDBで性能影響の確認ではサーバーの DBバックアップからANR4550Iを読み・性能影響確認に使うである。</li><li>B. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Expiration Status 0244固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きはClient Restoreで代替経路の確認ではリストア確認の 候補照会からMgmtClassを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはストレージプール内の空き領域を回収する処理をノード割当確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 代替経路対象ClienでCの記述「Client Restoreで代替経路の確認ではリストア確認の」に対応する項目は代替経路の確認 RST10（Client・代替経路）です。リスト・代替経に関するリストア確認の仕様は「Client Restoreで代替経路の確認ではリストア確認の」で、確認対象はClient・代替経路確です。性能影響対象性能影響ののA:は「DBで性能影響の確認ではサーバーの DBバックアップからANR455」を述べ、対象は性能影響の確認 DBBK11（DB・性能影響）です。保護対象ExpirのB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・保護）です。reclをノード割当のD:は「ストレージプール内の空き領域を回収する処理をノード割当確認する」を述べ、対象はノード割当確認 プール宛先（reclama・ノード割）です。Clieを代替経路確という用語は「Client Restoreで代替経路の確認ではリス」を指し、代替経路の確認 RST10（Client・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 代替経路の確認 RST10</strong></p><p>検証目的: リストア確認のClient Restoreについて代替手段の成立を確認し、RST10のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST10の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST10の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST10の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE10 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
② ステップ2 の restored が画面・出力に表示されること
③ ステップ3 の Restore が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0538"><h3>リストア確認 Client Restore 依存関係の確認 RST13</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>依存関係の確認では リストア確認 の 候補照会 を主操作として RST13 を判定します。前提資源と後続処理の順序への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST13 に残します。依存関係の確認を補助する 別名復元 では restored を補助値として RST13 へ保存します。主判定の依存関係の確認ではリストア確認の 候補照会 から MgmtClass を読み RST13 へ残します。証跡照合の依存関係の確認ではリストア確認の MgmtClass と restored を RST13 に保存します。記録対応の依存関係の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 依存関係の確認 RST13に関する障害切り分けの前提を確認しています。サーバーDB・DR Server Database Backup 再始動後の確認の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はClient Restoreで依存関係の確認ではリストア確認の 候補照会からMgmtClassを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はDBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・再始動確認に使うである。</li><li>C. 表示や設定で扱う内容はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Schedule Name 0204固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はバックアップ版数と保存先を定めるコピー規則である。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 依存関係対象ClienでAの記述「Client Restoreで依存関係の確認ではリストア確認の」に対応する項目は依存関係の確認 RST13（Client・依存関係）です。リスト・依存関に関するリストア確認の仕様は「Client Restoreで依存関係の確認ではリストア確認の」で、確認対象はClient・依存関係確です。再始動確対象DBのB:は「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は再始動後の確認 DBBK15（DB・再始動確）です。登録時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・登録）です。backを保存期間確のD:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は保存期間確認 ルール読替（backup・保存期間）です。Clieを依存関係確という用語は「Client Restoreで依存関係の確認ではリス」を指し、依存関係の確認 RST13（Client・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 依存関係の確認 RST13</strong></p><p>検証目的: リストア確認のClient Restoreについて依存資源を点検し、RST13のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST13の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST13の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST13の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE13 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
② ステップ2 の restored が画面・出力に表示されること
③ ステップ3 の Restore が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0539"><h3>リストア確認 Client Restore 停止前の確認 RST14</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>停止前の確認では リストア確認 の 別名復元 を主操作として RST14 を判定します。処理中資源と未完了要求への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST14 に残します。停止前の確認を補助する 活動ログ では Restore を補助値として RST14 へ保存します。主判定の停止前の確認ではリストア確認の 別名復元 から restored を読み RST14 へ残します。証跡照合の停止前の確認ではリストア確認の restored と Restore を RST14 に保存します。記録対応の停止前の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 停止前の確認 RST14の設定や表示を読む前に役割を確認します。サーバーDB・DR Server Database Backup 停止前の確認ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。</li><li>B. 一次資料が示す主目的はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 一次資料が示す主目的はClient Restoreで停止前の確認ではリストア確認の 別名復元からrestoredを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はPolicy Domainで停止前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 停止確認対象ClienでCの記述「Client Restoreで停止前の確認ではリストア確認の」に対応する項目は停止前の確認 RST14（Client・停止確認）です。リスト・停止前に関するリストア確認の仕様は「Client Restoreで停止前の確認ではリストア確認の」で、確認対象はClient・停止確認です。停止確認対象停止前の確のA:は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」を述べ、対象は停止前の確認 DBBK14（DB・停止確認）です。収集対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・収集）です。Poliを停止確認のD:は「Policy Domainで停止前の確認ではポリシードメインの」を述べ、対象は停止前の確認 DOM14（Policy・停止確認）です。Clieを停止確認という用語は「Client Restoreで停止前の確認ではリスト」を指し、停止前の確認 RST14（Client・停止確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 停止前の確認 RST14</strong></p><p>検証目的: リストア確認のClient Restoreについて安全な停止条件を確認し、RST14のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST14の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST14の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE14 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST14の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の restored が画面・出力に表示されること
② ステップ2 の Restore が画面・出力に表示されること
③ ステップ3 の MgmtClass が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0540"><h3>リストア確認 Client Restore 再始動後の確認 RST15</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>再始動後の確認では リストア確認 の 活動ログ を主操作として RST15 を判定します。再開点と未処理データへの注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST15 に残します。再始動後の確認を補助する 候補照会 では MgmtClass を補助値として RST15 へ保存します。主判定の再始動後の確認ではリストア確認の 活動ログ から Restore を読み RST15 へ残します。証跡照合の再始動後の確認ではリストア確認の Restore と MgmtClass を RST15 に保存します。記録対応の再始動後の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 再始動後の確認 RST15を同一分類のサーバーDB・DR Server Database Backup 停止前の確認と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。</li><li>B. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。サーバー日次運用 Database Backup 0247固有の属性も確認対象に含める。</li><li>C. 構成を確認する際の意味はバックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認する。</li><li>D. 構成を確認する際の意味はClient Restoreで再始動後の確認ではリストア確認の 活動ログからRestoreを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 再始動確対象ClienでDの記述「Client Restoreで再始動後の確認ではリストア確認の」に対応する項目は再始動後の確認 RST15（Client・再始動確）です。リスト・再始動に関するリストア確認の仕様は「Client Restoreで再始動後の確認ではリストア確認の」で、確認対象はClient・再始動確認です。停止確認対象停止前の確のA:は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」を述べ、対象は停止前の確認 DBBK14（DB・停止確認）です。保護対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・保護）です。期限切れ時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認す」を述べ、対象は期限切れ確認 ドメイン値（schedul・期限切れ）です。Clieを再始動確認という用語は「Client Restoreで再始動後の確認ではリス」を指し、再始動後の確認 RST15（Client・再始動確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 再始動後の確認 RST15</strong></p><p>検証目的: リストア確認のClient Restoreについて再始動結果を検証し、RST15のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST15の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE15 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST15の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST15の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Restore が画面・出力に表示されること
② ステップ2 の MgmtClass が画面・出力に表示されること
③ ステップ3 の restored が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0541"><h3>リストア確認 Client Restore 変更前の確認 RST02</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>変更前の確認では リストア確認 の 別名復元 を主操作として RST02 を判定します。変更対象と非対象の境界への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST02 に残します。変更前の確認を補助する 活動ログ では Restore を補助値として RST02 へ保存します。主判定の変更前の確認ではリストア確認の 別名復元 から restored を読み RST02 へ残します。証跡照合の変更前の確認ではリストア確認の restored と Restore を RST02 に保存します。記録対応の変更前の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 変更前の確認 RST02について構成や状態を確認します。サーバー日次運用 Server Name 0031ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はClient Restoreで変更前の確認ではリストア確認の 別名復元からrestoredを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 一次資料が示す主目的はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。クライアントスケジュール Start Time 0243固有の属性も確認対象に含める。</li><li>D. 一次資料が示す主目的はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認対象ClienでAの記述「Client Restoreで変更前の確認ではリストア確認の」に対応する項目は変更前の確認 RST02（Client・変更確認）です。リスト・変更前に関するリストア確認の仕様は「Client Restoreで変更前の確認ではリストア確認の」で、確認対象はClient・変更確認です。棚卸対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・棚卸）です。保護時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護）です。backをポリシードのD:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backup・ポリシー）です。Clieを変更確認という用語は「Client Restoreで変更前の確認ではリスト」を指し、変更前の確認 RST02（Client・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 変更前の確認 RST02</strong></p><p>検証目的: リストア確認のClient Restoreについて変更前の証跡を保存し、RST02のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST02の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST02の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE02 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST02の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の restored が画面・出力に表示されること
② ステップ2 の Restore が画面・出力に表示されること
③ ステップ3 の MgmtClass が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0542"><h3>リストア確認 Client Restore 変更後の確認 RST03</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>変更後の確認では リストア確認 の 活動ログ を主操作として RST03 を判定します。反映値と残存値への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST03 に残します。変更後の確認を補助する 候補照会 では MgmtClass を補助値として RST03 へ保存します。主判定の変更後の確認ではリストア確認の 活動ログ から Restore を読み RST03 へ残します。証跡照合の変更後の確認ではリストア確認の Restore と MgmtClass を RST03 に保存します。記録対応の変更後の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 変更後の確認 RST03の技術的な意味を資料で確認するとき、クライアントスケジュール Event Status 0027との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>B. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 構成を確認する際の意味はバックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡として確認する。</li><li>D. 構成を確認する際の意味はClient Restoreで変更後の確認ではリストア確認の 活動ログからRestoreを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認対象ClienでDの記述「Client Restoreで変更後の確認ではリストア確認の」に対応する項目は変更後の確認 RST03（Client・変更確認）です。リスト・変更後に関するリストア確認の仕様は「Client Restoreで変更後の確認ではリストア確認の」で、確認対象はClient・変更確認です。Event・棚卸のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・棚卸）です。登録対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。コピーグ時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡と」を述べ、対象はコマンド証跡 詳細タブ（schedul・コピーグ）です。Clieを変更確認という用語は「Client Restoreで変更後の確認ではリスト」を指し、変更後の確認 RST03（Client・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 変更後の確認 RST03</strong></p><p>検証目的: リストア確認のClient Restoreについて変更結果を検証し、RST03のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST03の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE03 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST03の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST03の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Restore が画面・出力に表示されること
② ステップ2 の MgmtClass が画面・出力に表示されること
③ ステップ3 の restored が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0543"><h3>リストア確認 Client Restore 引継ぎ記録 RST09</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>引継ぎ記録では リストア確認 の 活動ログ を主操作として RST09 を判定します。次担当者が追跡できる証跡への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST09 に残します。引継ぎ記録を補助する 候補照会 では MgmtClass を補助値として RST09 へ保存します。主判定の引継ぎ記録ではリストア確認の 活動ログ から Restore を読み RST09 へ残します。証跡照合の引継ぎ記録ではリストア確認の Restore と MgmtClass を RST09 に保存します。記録対応の引継ぎ記録ではリストア確認の Restore CountとFailed Count の証跡へ RST09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 引継ぎ記録 RST09の役割を調べています。サーバー日次運用 Database Backup 0007の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 機能の説明としてはDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 機能の説明としてはアーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確認する。</li><li>D. 機能の説明としてはClient Restoreで引継ぎ記録ではリストア確認の 活動ログからRestoreを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> リストア対象ClienでDの記述「Client Restoreで引継ぎ記録ではリストア確認の」に対応する項目は引継ぎ記録 RST09（Client・リストア）です。リスト・引継ぎに関するリストア確認の仕様は「Client Restoreで引継ぎ記録ではリストア確認の」で、確認対象はClient・リストア確です。Datab・巡回のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・巡回）です。収集対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・収集）です。バックア時のarchiのC:は「アーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確」を述べ、対象は容量監視 実行結果（archive・バックア）です。Clieをリストア確という用語は「Client Restoreで引継ぎ記録ではリストア」を指し、引継ぎ記録 RST09（Client・リストア）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 引継ぎ記録 RST09</strong></p><p>検証目的: リストア確認のClient Restoreについて再現可能な記録を作成し、RST09のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST09の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE09 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST09の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST09の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Restore が画面・出力に表示されること
② ステップ2 の MgmtClass が画面・出力に表示されること
③ ステップ3 の restored が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0544"><h3>リストア確認 Client Restore 復旧後の確認 RST06</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>復旧後の確認では リストア確認 の 活動ログ を主操作として RST06 を判定します。再発していないことを示す値への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST06 に残します。復旧後の確認を補助する 候補照会 では MgmtClass を補助値として RST06 へ保存します。主判定の復旧後の確認ではリストア確認の 活動ログ から Restore を読み RST06 へ残します。証跡照合の復旧後の確認ではリストア確認の Restore と MgmtClass を RST06 に保存します。記録対応の復旧後の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 復旧後の確認 RST06の設定や表示を読む前に役割を確認します。サーバー日次運用 Expiration Status 0034ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 状態を読み取るための働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 状態を読み取るための働きはClient Restoreで復旧後の確認ではリストア確認の 活動ログからRestoreを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはストレージプール内の空き領域を回収する処理である。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧確認対象ClienでCの記述「Client Restoreで復旧後の確認ではリストア確認の」に対応する項目は復旧後の確認 RST06（Client・復旧確認）です。リスト・復旧後に関するリストア確認の仕様は「Client Restoreで復旧後の確認ではリストア確認の」で、確認対象はClient・復旧確認です。Expir・棚卸のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・棚卸）です。保護対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・保護）です。reclを宛先照合のD:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は宛先照合 集約結果（reclama・宛先照合）です。Clieを復旧確認という用語は「Client Restoreで復旧後の確認ではリスト」を指し、復旧後の確認 RST06（Client・復旧確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 復旧後の確認 RST06</strong></p><p>検証目的: リストア確認のClient Restoreについて復旧後の安定性を確認し、RST06のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST06の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE06 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST06の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST06の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Restore が画面・出力に表示されること
② ステップ2 の MgmtClass が画面・出力に表示されること
③ ステップ3 の restored が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0545"><h3>リストア確認 Client Restore 復旧準備 RST05</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>復旧準備では リストア確認 の 別名復元 を主操作として RST05 を判定します。再開前に必要な整合性への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST05 に残します。復旧準備を補助する 活動ログ では Restore を補助値として RST05 へ保存します。主判定の復旧準備ではリストア確認の 別名復元 から restored を読み RST05 へ残します。証跡照合の復旧準備ではリストア確認の restored と Restore を RST05 に保存します。記録対応の復旧準備ではリストア確認の Restore CountとFailed Count の証跡へ RST05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 復旧準備 RST05に関する障害切り分けの前提を確認しています。サーバー日次運用 Node Name 0013の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 障害切り分けに用いる役割はClient Restoreで復旧準備ではリストア確認の 別名復元からrestoredを読み・復旧準備に使うである。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。サーバー日次運用 Storage Pool 0250固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はアーカイブコピーの保存期間と宛先を定めるコピー規則である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧準備対象ClienでBの記述「Client Restoreで復旧準備ではリストア確認の」に対応する項目は復旧準備 RST05（Client・復旧準備）です。リスト・復旧準に関するリストア確認の仕様は「Client Restoreで復旧準備ではリストア確認の」で、確認対象はClient・復旧準備です。Node・巡回のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・巡回）です。保護時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・保護）です。archを保存期間確のD:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は保存期間確認 証明書検査（archive・保存期間）です。Clieを復旧準備という用語は「Client Restoreで復旧準備ではリストア確」を指し、復旧準備 RST05（Client・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 復旧準備 RST05</strong></p><p>検証目的: リストア確認のClient Restoreについて復旧条件を確認し、RST05のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST05の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST05の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE05 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST05の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の restored が画面・出力に表示されること
② ステップ2 の Restore が画面・出力に表示されること
③ ステップ3 の MgmtClass が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0546"><h3>リストア確認 Client Restore 性能影響の確認 RST11</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>性能影響の確認では リストア確認 の 別名復元 を主操作として RST11 を判定します。処理時間と滞留箇所への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST11 に残します。性能影響の確認を補助する 活動ログ では Restore を補助値として RST11 へ保存します。主判定の性能影響の確認ではリストア確認の 別名復元 から restored を読み RST11 へ残します。証跡照合の性能影響の確認ではリストア確認の restored と Restore を RST11 に保存します。記録対応の性能影響の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 性能影響の確認 RST11の技術的な意味を資料で確認するとき、サーバー日次運用 Node Name 0058との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。サーバー日次運用 Node Name 0058固有の属性も確認対象に含める。</li><li>B. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. コマンドまたは機能の用途はClient Restoreで性能影響の確認ではリストア確認の 別名復元からrestoredを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 性能影響対象ClienでDの記述「Client Restoreで性能影響の確認ではリストア確認の」に対応する項目は性能影響の確認 RST11（Client・性能影響）です。リスト・性能影に関するリストア確認の仕様は「Client Restoreで性能影響の確認ではリストア確認の」で、確認対象はClient・性能影響確です。Node・復旧のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。切替対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・切替）です。承認時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・承認）です。Clieを性能影響確という用語は「Client Restoreで性能影響の確認ではリス」を指し、性能影響の確認 RST11（Client・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 性能影響の確認 RST11</strong></p><p>検証目的: リストア確認のClient Restoreについて負荷と待ちを確認し、RST11のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST11の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST11の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE11 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST11の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の restored が画面・出力に表示されること
② ステップ2 の Restore が画面・出力に表示されること
③ ステップ3 の MgmtClass が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0547"><h3>リストア確認 Client Restore 構成監査 RST08</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>構成監査では リストア確認 の 別名復元 を主操作として RST08 を判定します。定義値と稼働値の一致への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST08 に残します。構成監査を補助する 活動ログ では Restore を補助値として RST08 へ保存します。主判定の構成監査ではリストア確認の 別名復元 から restored を読み RST08 へ残します。証跡照合の構成監査ではリストア確認の restored と Restore を RST08 に保存します。記録対応の構成監査ではリストア確認の Restore CountとFailed Count の証跡へ RST08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「リストア確認 Client Restore 構成監査 RST08」を「サーバー日次運用 Node Name 0058」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はClient Restoreで構成監査ではリストア確認の 別名復元からrestoredを読み・構成監査に使うである。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 仕様上の役割はバックアップやアーカイブのデータを格納するサーバー側領域である。storage pool 保存期間確認 検査エンジン固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構成監査対象ClienでAの記述「Client Restoreで構成監査ではリストア確認の」に対応する項目は構成監査 RST08（Client・構成監査）です。リスト・構成監に関するリストア確認の仕様は「Client Restoreで構成監査ではリストア確認の」で、確認対象はClient・構成監査です。復旧対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。収集時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集）です。storを保存期間確のD:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は保存期間確認 検査エンジン（storage・保存期間）です。Clieを構成監査という用語は「Client Restoreで構成監査ではリストア確」を指し、構成監査 RST08（Client・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 構成監査 RST08</strong></p><p>検証目的: リストア確認のClient Restoreについて構成差分を監査し、RST08のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST08の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST08の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE08 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST08の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の restored が画面・出力に表示されること
② ステップ2 の Restore が画面・出力に表示されること
③ ステップ3 の MgmtClass が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0548"><h3>リストア確認 Client Restore 権限境界の確認 RST12</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>権限境界の確認では リストア確認 の 活動ログ を主操作として RST12 を判定します。参照操作と変更操作の分離への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST12 に残します。権限境界の確認を補助する 候補照会 では MgmtClass を補助値として RST12 へ保存します。主判定の権限境界の確認ではリストア確認の 活動ログ から Restore を読み RST12 へ残します。証跡照合の権限境界の確認ではリストア確認の Restore と MgmtClass を RST12 に保存します。記録対応の権限境界の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 権限境界の確認 RST12を保守記録に説明する必要があります。複製・保護 Storage Pool Protection and Nodeと取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はClient Restoreで権限境界の確認ではリストア確認の 活動ログからRestoreを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はStorage Poolで変更後の確認では複製・保護の 検証からANR3730Iを読み・変更確認に使うである。</li><li>C. 運用時に利用する技術的役割はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>D. 運用時に利用する技術的役割はPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 権限境界対象ClienでAの記述「Client Restoreで権限境界の確認ではリストア確認の」に対応する項目は権限境界の確認 RST12（Client・権限境界）です。リスト・権限境に関するリストア確認の仕様は「Client Restoreで権限境界の確認ではリストア確認の」で、確認対象はClient・権限境界確です。変更確認対象StoraのB:は「Storage Poolで変更後の確認では複製・保護の」を述べ、対象は変更後の確認 REPL03（Storage・変更確認）です。確認時のServeのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・確認）です。Poliを復旧確認のD:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Policy・復旧確認）です。Clieを権限境界確という用語は「Client Restoreで権限境界の確認ではリス」を指し、権限境界の確認 RST12（Client・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 権限境界の確認 RST12</strong></p><p>検証目的: リストア確認のClient Restoreについて実行権限を点検し、RST12のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST12の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE12 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST12の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST12の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Restore が画面・出力に表示されること
② ステップ2 の MgmtClass が画面・出力に表示されること
③ ステップ3 の restored が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0549"><h3>リストア確認 Client Restore 通常状態の確認 RST01</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>通常状態の確認では リストア確認 の 候補照会 を主操作として RST01 を判定します。基準値と現在値の差への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST01 に残します。通常状態の確認を補助する 別名復元 では restored を補助値として RST01 へ保存します。主判定の通常状態の確認ではリストア確認の 候補照会 から MgmtClass を読み RST01 へ残します。証跡照合の通常状態の確認ではリストア確認の MgmtClass と restored を RST01 に保存します。記録対応の通常状態の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 通常状態の確認 RST01の役割を調べています。サーバーDB・DR Server Database Backup 代替経路の確認の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はClient Restoreで通常状態の確認ではリストア確認の 候補照会からMgmtClassを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はDBで代替経路の確認ではサーバーの DB状態からLastDatabaseを読み・代替経路確認に使うである。サーバーDB・DR Server Database Backup固有の属性も確認対象に含める。</li><li>C. 表示や設定で扱う内容はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 表示や設定で扱う内容はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 通常状態対象ClienでAの記述「Client Restoreで通常状態の確認ではリストア確認の」に対応する項目は通常状態の確認 RST01（Client・通常状態）です。リスト・通常状に関するリストア確認の仕様は「Client Restoreで通常状態の確認ではリストア確認の」で、確認対象はClient・通常状態確です。代替経路対象DBのB:は「DBで代替経路の確認ではサーバーの DB状態からLastDataba」を述べ、対象は代替経路の確認 DBBK10（DB・代替経路）です。切替時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・切替）です。ノード登録を解除のD:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・解除）です。Clieを通常状態確という用語は「Client Restoreで通常状態の確認ではリス」を指し、通常状態の確認 RST01（Client・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 通常状態の確認 RST01</strong></p><p>検証目的: リストア確認のClient Restoreについて通常状態を確定し、RST01のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST01の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST01の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST01の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE01 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
② ステップ2 の restored が画面・出力に表示されること
③ ステップ3 の Restore が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0550"><h3>リストア確認 Client Restore 障害切り分け RST04</h3><p class="kb-meta">分類: リストア確認 ・ 難易度: 中級</p><p>障害切り分けでは リストア確認 の 候補照会 を主操作として RST04 を判定します。最初に失敗した処理への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST04 に残します。障害切り分けを補助する 別名復元 では restored を補助値として RST04 へ保存します。主判定の障害切り分けではリストア確認の 候補照会 から MgmtClass を読み RST04 へ残します。証跡照合の障害切り分けではリストア確認の MgmtClass と restored を RST04 に保存します。記録対応の障害切り分けではリストア確認の Restore CountとFailed Count の証跡へ RST04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> リストア確認 Client Restore 障害切り分け RST04を保守記録に説明する必要があります。サーバーDB・DR Server Database Backup 代替経路の確認と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDBで代替経路の確認ではサーバーの DB状態からLastDatabaseを読み・代替経路確認に使うである。</li><li>B. 保守作業で参照する機能はClient Restoreで障害切り分けではリストア確認の 候補照会からMgmtClassを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 保守作業で参照する機能はアーカイブコピーの保存期間と宛先を定めるコピー規則である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> リストア対象ClienでBの記述「Client Restoreで障害切り分けではリストア確認の」に対応する項目は障害切り分け RST04（Client・リストア）です。リスト・障害切に関するリストア確認の仕様は「Client Restoreで障害切り分けではリストア確認の」で、確認対象はClient・リストア確です。代替経路対象代替経路ののA:は「DBで代替経路の確認ではサーバーの DB状態からLastDataba」を述べ、対象は代替経路の確認 DBBK10（DB・代替経路）です。確認時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・確認）です。archを宛先照合のD:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は宛先照合 伝搬経路（archive・宛先照合）です。Clieをリストア確という用語は「Client Restoreで障害切り分けではリスト」を指し、障害切り分け RST04（Client・リストア）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>リストア確認 Client Restore 障害切り分け RST04</strong></p><p>検証目的: リストア確認のClient Restoreについて障害範囲を限定し、RST04のRestore CountとFailed Countを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST04の候補照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query backup /app/report.dat -inactive
→ Enter を押す
［画面・出力］
Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST04の別名復元を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc restore /app/report.dat /restore/report.dat
→ Enter を押す
［画面・出力］
Restoring /app/report.dat to /restore/report.dat
Total number of objects restored: 1
Total number of objects failed: 0
画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST04の活動ログを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
→ Enter を押す
［画面・出力］
ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE04 completed.
画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
② ステップ2 の restored が画面・出力に表示されること
③ ステップ3 の Restore が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## 管理クラス


<section class="kb-item" id="c14-i0551"><h3>activity log 保存期間確認 監査証跡</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「activity log 保存期間確認 監査証跡」は、サーバー操作とメッセージを追跡するログを保存期間確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 010を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> activity log 保存期間確認 監査証跡の役割を調べています。activity log 容量監視 アーカイブの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はサーバー操作とメッセージを追跡するログを容量監視として確認する。</li><li>B. 障害切り分けに用いる役割はサーバー操作とメッセージを追跡するログである。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 監査証跡・activityでBの記述「サーバー操作とメッセージを追跡するログである」に対応する項目は保存期間確認 監査証跡（activit・監査証跡）です。保存期・監査証に関する管理クラスの仕様は「サーバー操作とメッセージを追跡するログ」で、確認対象はactivit・監査証跡です。リストア・activityのA:は「サーバー操作とメッセージを追跡するログを容量監視として確認する」を述べ、対象は容量監視 アーカイブ（activit・リストア）です。棚卸・ManagemeのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・棚卸）です。切替・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・切替）です。「activity log」は「サーバー操作とメッセージを追跡するログ」を指す用語で、保存期間確認 監査証跡（activit・監査証跡）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>activity log 保存期間確認 監査証跡</strong></p><p>検証目的: 管理クラスのactivity log 保存期間確認 監査証跡について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL010
画面・出力には ANR1550I が含まれ、activity log 保存期間確認 監査証跡の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL010 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL010
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0552"><h3>activity log 復元前確認 管理クラス</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「activity log 復元前確認 管理クラス」は、サーバー操作とメッセージを追跡するログを復元前確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 050を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> activity log 復元前確認 管理クラスの役割を調べています。policy domain 復元前確認 統合管理の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはサーバー操作とメッセージを追跡するログを復元前確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはクライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認する。</li><li>C. 機能の説明としてはEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. 機能の説明としてはExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復元前確認・activityでAの記述「サーバー操作とメッセージを追跡するログを復元前確認する」に対応する項目は復元前確認 管理クラス（activit・復元前確）です。復元前・管理クに関する管理クラスの仕様は「サーバー操作とメッセージを追跡するログを復元前確認する」で、確認対象はactivit・復元前確認です。復元前確認・policyのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」を述べ、対象は復元前確認 統合管理（policy・復元前確）です。変更・EventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更）です。保護・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・保護）です。「activity log」は「サーバー操作とメッセージを追跡するログを復元前確認す」を指す用語で、復元前確認 管理クラス（activit・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>activity log 復元前確認 管理クラス</strong></p><p>検証目的: 管理クラスのactivity log 復元前確認 管理クラスについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL050
画面・出力には ANR1550I が含まれ、activity log 復元前確認 管理クラスの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL050 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL050
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0553"><h3>archive copy group 期限切れ確認 適用位置</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「archive copy group 期限切れ確認 適用位置」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 034を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> archive copy group 期限切れ確認 適用位置の役割を調べています。archive copy group 宛先照合 伝搬経路の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はアーカイブコピーの保存期間と宛先を定めるコピー規則である。</li><li>B. 障害切り分けに用いる役割はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 障害切り分けに用いる役割はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 障害切り分けに用いる役割はアーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 期限切れ確・archiveでDの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認する」に対応する項目は期限切れ確認 適用位置（archive・期限切れ）です。期限切・適用位に関する管理クラスの仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認する」で、確認対象はarchive・期限切れ確です。宛先照合・archiveのA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は宛先照合 伝搬経路（archive・宛先照合）です。復旧・ScheduleのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・復旧）です。確認・EventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・確認）です。「archive copy group」は「アーカイブコピーの保存期間と宛先を定めるコピー規則を」を指す用語で、期限切れ確認 適用位置（archive・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>archive copy group 期限切れ確認 適用位置</strong></p><p>検証目的: 管理クラスのarchive copy group 期限切れ確認 適用位置について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL034
画面・出力には ANR1550I が含まれ、archive copy group 期限切れ確認 適用位置の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL034 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL034
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0554"><h3>archive copy group 状態確認 集約装置</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「archive copy group 状態確認 集約装置」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を状態確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 074を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> archive copy group 状態確認 集約装置の役割を調べています。ポリシードメイン Policy Domain 引継ぎ記録 DOM09の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはPolicy Domainで引継ぎ記録ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>B. 機能の説明としてはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 機能の説明としてはDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 機能の説明としてはアーカイブコピーの保存期間と宛先を定めるコピー規則である。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 状態で状態確認でDの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則である」に対応する項目は状態確認 集約装置（archive・状態確認）です。状態・集約装に関する管理クラスの仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則」で、確認対象はarchive・状態確認です。Polic・ポリシードのA:は「Policy Domainで引継ぎ記録ではポリシードメインの」を述べ、対象は引継ぎ記録 DOM09（Policy・ポリシー）です。サーバで復旧のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・復旧）です。照合時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合）です。archを状態確認という用語は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を指し、状態確認 集約装置（archive・状態確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>archive copy group 状態確認 集約装置</strong></p><p>検証目的: 管理クラスのarchive copy group 状態確認 集約装置について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL074
画面・出力には ANR1550I が含まれ、archive copy group 状態確認 集約装置の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL074 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL074
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0555"><h3>management class 保存期間確認 停止時刻</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「management class 保存期間確認 停止時刻」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を保存期間確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL002を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> management class 保存期間確認 停止時刻の役割を調べています。expiration 期限切れ確認 入力欄の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはファイルのバックアップ先や保存期間を決めるポリシー要素である。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としては保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する。</li><li>C. 機能の説明としてはStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保存期間確・managemeでAの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素である」に対応する項目は保存期間確認 停止時刻（managem・保存期間）です。保存期・停止時に関する管理クラスの仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素」で、確認対象はmanagem・保存期間確です。期限切れ確・expiratiのB:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」を述べ、対象は期限切れ確認 入力欄（expirat・期限切れ）です。復旧・StartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・復旧）です。登録・DatabaseのD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。「management class」は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指す用語で、保存期間確認 停止時刻（managem・保存期間）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>management class 保存期間確認 停止時刻</strong></p><p>検証目的: 管理クラスのmanagement class 保存期間確認 停止時刻について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL002
画面・出力には ANR1550I が含まれ、management class 保存期間確認 停止時刻の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL002 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL002
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0556"><h3>management class 復元前確認 期限切れ</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「management class 復元前確認 期限切れ」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL042を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> management class 復元前確認 期限切れの役割を調べています。policy domain コマンド証跡 重大度の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をコマンド証跡として確認する。</li><li>B. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 表示や設定で扱う内容はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復元前確認・managemeでCの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」に対応する項目は復元前確認 期限切れ（managem・復元前確）です。復元前・期限切に関する管理クラスの仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」で、確認対象はmanagem・復元前確認です。コピーグル・policyのA:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をコ」を述べ、対象はコマンド証跡 重大度（policy・コピーグ）です。変更・ActionのB:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・変更）です。照合・DatabaseのD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。「management class」は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指す用語で、復元前確認 期限切れ（managem・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>management class 復元前確認 期限切れ</strong></p><p>検証目的: 管理クラスのmanagement class 復元前確認 期限切れについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL042
画面・出力には ANR1550I が含まれ、management class 復元前確認 期限切れの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL042 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL042
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0557"><h3>node コマンド証跡 マクロ実行</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「node コマンド証跡 マクロ実行」は、サーバーへ登録されたクライアントを表す管理単位をコマンド証跡の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE066を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> node コマンド証跡 マクロ実行の役割を調べています。管理クラス Management Class 権限境界の確認 MC12の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はサーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。</li><li>C. 表示や設定で扱う内容はAssociationの関連ノードと取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コマンで管理クラスでAの記述「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」に対応する項目はコマンド証跡 マクロ実行（node・管理クラ）です。コマン・マクロに関する管理クラスの仕様は「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」で、確認対象はnode・管理クラスです。管理クで権限境界確のB:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。監査時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・監査）です。Servを保護のD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保護）です。nodeを管理クラスという用語は「サーバーへ登録されたクライアントを表す管理単位をコマ」を指し、コマンド証跡 マクロ実行（node・管理クラ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>node コマンド証跡 マクロ実行</strong></p><p>検証目的: 管理クラスのnode コマンド証跡 マクロ実行について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL066
画面・出力には ANR1550I が含まれ、node コマンド証跡 マクロ実行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL066 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL066
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0558"><h3>node ノード割当確認 保存場所</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「node ノード割当確認 保存場所」は、サーバーへ登録されたクライアントを表す管理単位をノード割当確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE026を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> node ノード割当確認 保存場所の役割を調べています。コピーグループ Backup and Archive Copy Groupの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはサーバーへ登録されたクライアントを表す管理単位をノード割当確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。</li><li>C. 機能の説明としてはAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 機能の説明としてはServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ノード割当・nodeでAの記述「サーバーへ登録されたクライアントを表す管理単位をノード割当確認する」に対応する項目はノード割当確認 保存場所（node・ノード割）です。ノード・保存場に関する管理クラスの仕様は「サーバーへ登録されたクライアントを表す管理単位をノード割当確認する」で、確認対象はnode・ノード割当です。構成監査・BackupのB:は「Backup andで構成監査ではコピーグループの」を述べ、対象は構成監査 CG08（Backup・構成監査）です。棚卸・AssociatのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・棚卸）です。収集・ServerのD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・収集）です。「node」は「サーバーへ登録されたクライアントを表す管理単位をノー」を指す用語で、ノード割当確認 保存場所（node・ノード割）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>node ノード割当確認 保存場所</strong></p><p>検証目的: 管理クラスのnode ノード割当確認 保存場所について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL026
画面・出力には ANR1550I が含まれ、node ノード割当確認 保存場所の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL026 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL026
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0559"><h3>reclamation 宛先照合 集約結果</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「reclamation 宛先照合 集約結果」は、ストレージプール内の空き領域を回収する処理を宛先照合の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR018Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> reclamation 宛先照合 集約結果の役割を調べています。ポリシードメイン Policy Domain 代替経路の確認 DOM10の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はストレージプール内の空き領域を回収する処理である。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はPolicy Domainで代替経路の確認ではポリシードメインのである。</li><li>C. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 表示や設定で扱う内容はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 宛先照合・reclamatでAの記述「ストレージプール内の空き領域を回収する処理である」に対応する項目は宛先照合 集約結果（reclama・宛先照合）です。宛先・集約結に関する管理クラスの仕様は「ストレージプール内の空き領域を回収する処理」で、確認対象はreclama・宛先照合です。代替経路確・PolicyのB:は「Policy Domainで代替経路の確認ではポリシードメインの」を述べ、対象は代替経路の確認 DOM10（Policy・代替経路）です。棚卸・ActionのC:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・棚卸）です。照合・PolicyのD:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・照合）です。「reclamation」は「ストレージプール内の空き領域を回収する処理」を指す用語で、宛先照合 集約結果（reclama・宛先照合）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>reclamation 宛先照合 集約結果</strong></p><p>検証目的: 管理クラスのreclamation 宛先照合 集約結果について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL018
画面・出力には ANR1550I が含まれ、reclamation 宛先照合 集約結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL018 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL018
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0560"><h3>reclamation 容量監視 一覧画面</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の 管理クラス で扱う「reclamation 容量監視 一覧画面」は、ストレージプール内の空き領域を回収する処理を容量監視の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR058Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> reclamation 容量監視 一覧画面の役割を調べています。reclamation 保存期間確認 画面タグの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はストレージプール内の空き領域を回収する処理である。</li><li>B. 障害切り分けに用いる役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 障害切り分けに用いる役割はストレージプール内の空き領域を回収する処理を容量監視として確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 容量監で管理クラスでDの記述「ストレージプール内の空き領域を回収する処理を容量監視として確認する」に対応する項目は容量監視 一覧画面（reclama・管理クラ）です。容量監・一覧画に関する管理クラスの仕様は「ストレージプール内の空き領域を回収する処理を容量監視として確認する」で、確認対象はreclama・管理クラスです。recla・保存期間確のA:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は保存期間確認 画面タグ（reclama・保存期間）です。クライで変更のB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更）です。確認時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・確認）です。reclを管理クラスという用語は「ストレージプール内の空き領域を回収する処理を容量監視」を指し、容量監視 一覧画面（reclama・管理クラ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>reclamation 容量監視 一覧画面</strong></p><p>検証目的: 管理クラスのreclamation 容量監視 一覧画面について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DOMAIN STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
Policy Domain Name STANDARD
Backup Retention 30
Archive Retention 365
画面・出力には ANR2017I が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE POLICYSET STANDARD ACTIVE
→ Enter を押す
［画面・出力］
ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
Management Class STANDARD
Destination Pool POOL058
画面・出力には ANR1550I が含まれ、reclamation 容量監視 一覧画面の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL058 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL058
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0561"><h3>管理クラス Management Class ログとの照合 MC07</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>ログとの照合では 管理クラス の 管理クラス照会 を主操作として MC07 を判定します。時刻と対象識別子への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC07 に残します。ログとの照合を補助する クライアント詳細 では DefaultManagement を補助値として MC07 へ保存します。主判定のログとの照合では管理クラスの 管理クラス照会 から ManagementClass を読み MC07 へ残します。証跡照合のログとの照合では管理クラスの ManagementClass と DefaultManagement を MC07 に保存します。記録対応のログとの照合では管理クラスの Management ClassとDefault の証跡へ MC07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class ログとの照合 MC07に関する障害切り分けの前提を確認しています。ノード管理 Client Node 代替経路の確認 NODE10の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はClient Nodeで代替経路の確認ではノード管理の ノード照会からLastAccessを読みである。ノード管理 Client Node 代替経路の確認 NODE10固有の属性も確認対象に含める。</li><li>B. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 表示や設定で扱う内容はManagement Classでログとの照合では管理クラスの 管理クラス照会からManagementClaである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クでログとの照でCの記述「Management Classでログとの照合では管理クラスの」に対応する項目はログとの照合 MC07（Managem・ログとの）です。管理ク・ログとに関する管理クラスの仕様は「Management Classでログとの照合では管理クラスの」で、確認対象はManagem・ログとの照です。Clien・代替経路確のA:は「Client Nodeで代替経路の確認ではノード管理の」を述べ、対象は代替経路の確認 NODE10（Client・代替経路）です。サーバで保守のB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・保守）です。計画でDIRMCのD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・計画）です。Manaをログとの照という用語は「Management Classでログとの照合では管」を指し、ログとの照合 MC07（Managem・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class ログとの照合 MC07</strong></p><p>検証目的: 管理クラスのManagement Classについて操作とログを対応し、MC07のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC07 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC07の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC07 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC07
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC07のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC07 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC07のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Domain が画面・出力に表示されること
③ ステップ3 の DIRMC が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0562"><h3>管理クラス Management Class 代替経路の確認 MC10</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>代替経路の確認では 管理クラス の 管理クラス照会 を主操作として MC10 を判定します。主経路との役割差への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC10 に残します。代替経路の確認を補助する クライアント詳細 では DefaultManagement を補助値として MC10 へ保存します。主判定の代替経路の確認では管理クラスの 管理クラス照会 から ManagementClass を読み MC10 へ残します。証跡照合の代替経路の確認では管理クラスの ManagementClass と DefaultManagement を MC10 に保存します。記録対応の代替経路の確認では管理クラスの Management ClassとDefault の証跡へ MC10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「管理クラス Management Class 代替経路の確認 MC10」を「ノード管理 Client Node 権限境界の確認 NODE12」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はClient Nodeで権限境界の確認ではノード管理の 関連付けからAssociatedNodeを読みである。</li><li>B. 保守作業で参照する機能はManagement Classで代替経路の確認では管理クラスのである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで代替経路確でBの記述「Management Classで代替経路の確認では管理クラスのであ」に対応する項目は代替経路の確認 MC10（Managem・代替経路）です。管理ク・代替経に関する管理クラスの仕様は「Management Classで代替経路の確認では管理クラスの」で、確認対象はManagem・代替経路確です。Clien・権限境界確のA:は「Client Nodeで権限境界の確認ではノード管理の」を述べ、対象は権限境界の確認 NODE12（Client・権限境界）です。移行時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・移行）です。Dataを照合のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。Manaを代替経路確という用語は「Management Classで代替経路の確認では」を指し、代替経路の確認 MC10（Managem・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 代替経路の確認 MC10</strong></p><p>検証目的: 管理クラスのManagement Classについて代替手段の成立を確認し、MC10のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC10 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC10の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC10 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC10
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC10のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC10 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC10のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Domain が画面・出力に表示されること
③ ステップ3 の DIRMC が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0563"><h3>管理クラス Management Class 依存関係の確認 MC13</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>依存関係の確認では 管理クラス の 管理クラス照会 を主操作として MC13 を判定します。前提資源と後続処理の順序への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC13 に残します。依存関係の確認を補助する クライアント詳細 では DefaultManagement を補助値として MC13 へ保存します。主判定の依存関係の確認では管理クラスの 管理クラス照会 から ManagementClass を読み MC13 へ残します。証跡照合の依存関係の確認では管理クラスの ManagementClass と DefaultManagement を MC13 に保存します。記録対応の依存関係の確認では管理クラスの Management ClassとDefault の証跡へ MC13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 依存関係の確認 MC13の技術的な意味を資料で確認するとき、アーカイブ運用 Archive Operation 障害切り分け ARC04との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はArchive Operationで障害切り分けではアーカイブ運用のである。</li><li>B. 管理対象との関係を表す説明はManagement Classで依存関係の確認では管理クラスのである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで依存関係確でBの記述「Management Classで依存関係の確認では管理クラスのであ」に対応する項目は依存関係の確認 MC13（Managem・依存関係）です。管理ク・依存関に関する管理クラスの仕様は「Management Classで依存関係の確認では管理クラスの」で、確認対象はManagem・依存関係確です。Archi・アーカイブのA:は「Archive Operationで障害切り分けではアーカイブ運用の」を述べ、対象は障害切り分け ARC04（Archive・アーカイ）です。診断時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・診断）です。Assoを抑止のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・抑止）です。Manaを依存関係確という用語は「Management Classで依存関係の確認では」を指し、依存関係の確認 MC13（Managem・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 依存関係の確認 MC13</strong></p><p>検証目的: 管理クラスのManagement Classについて依存資源を点検し、MC13のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC13 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC13の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC13 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC13
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC13のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC13 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC13のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Domain が画面・出力に表示されること
③ ステップ3 の DIRMC が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0564"><h3>管理クラス Management Class 停止前の確認 MC14</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>停止前の確認では 管理クラス の クライアント詳細 を主操作として MC14 を判定します。処理中資源と未完了要求への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC14 に残します。停止前の確認を補助する オプション確認 では DIRMC を補助値として MC14 へ保存します。主判定の停止前の確認では管理クラスの クライアント詳細 から DefaultManagement を読み MC14 へ残します。証跡照合の停止前の確認では管理クラスの DefaultManagement と DIRMC を MC14 に保存します。記録対応の停止前の確認では管理クラスの Management ClassとDefault の証跡へ MC14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 停止前の確認 MC14を保守記録に説明する必要があります。ノード管理 Client Node 性能影響の確認 NODE11と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はClient Nodeで性能影響の確認ではノード管理の 占有量照会からLogicalFilesを読みである。</li><li>B. 仕様上の役割はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 仕様上の役割はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Node Name 0328固有の属性も確認対象に含める。</li><li>D. 仕様上の役割はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで停止確認でDの記述「Management Classで停止前の確認では管理クラスの」に対応する項目は停止前の確認 MC14（Managem・停止確認）です。管理ク・停止前に関する管理クラスの仕様は「Management Classで停止前の確認では管理クラスの」で、確認対象はManagem・停止確認です。Clien・性能影響確のA:は「Client Nodeで性能影響の確認ではノード管理の」を述べ、対象は性能影響の確認 NODE11（Client・性能影響）です。クライで保守のB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保守）です。計画時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・計画）です。Manaを停止確認という用語は「Management Classで停止前の確認では管」を指し、停止前の確認 MC14（Managem・停止確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 停止前の確認 MC14</strong></p><p>検証目的: 管理クラスのManagement Classについて安全な停止条件を確認し、MC14のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC14のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC14 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC14のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC14 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC14の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC14 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC14
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Domain が画面・出力に表示されること
② ステップ2 の DIRMC が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0565"><h3>管理クラス Management Class 再始動後の確認 MC15</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>再始動後の確認では 管理クラス の オプション確認 を主操作として MC15 を判定します。再開点と未処理データへの注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC15 に残します。再始動後の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC15 へ保存します。主判定の再始動後の確認では管理クラスの オプション確認 から DIRMC を読み MC15 へ残します。証跡照合の再始動後の確認では管理クラスの DIRMC と ManagementClass を MC15 に保存します。記録対応の再始動後の確認では管理クラスの Management ClassとDefault の証跡へ MC15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 再始動後の確認 MC15に関する障害切り分けの前提を確認しています。複製・保護 Storage Pool Protection and Nodeの機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはStorage Poolで変更後の確認では複製・保護の 検証からANR3730Iを読み・変更確認に使うである。</li><li>B. 機能の説明としてはActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 機能の説明としてはManagement Classで再始動後の確認では管理クラスの オプション確認からDIRMCを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで再始動確認でCの記述「Management Classで再始動後の確認では管理クラスの」に対応する項目は再始動後の確認 MC15（Managem・再始動確）です。管理ク・再始動に関する管理クラスの仕様は「Management Classで再始動後の確認では管理クラスの」で、確認対象はManagem・再始動確認です。Stora・変更確認のA:は「Storage Poolで変更後の確認では複製・保護の」を述べ、対象は変更後の確認 REPL03（Storage・変更確認）です。クライで移行のB:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・移行）です。Dataを計画のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・計画）です。Manaを再始動確認という用語は「Management Classで再始動後の確認では」を指し、再始動後の確認 MC15（Managem・再始動確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 再始動後の確認 MC15</strong></p><p>検証目的: 管理クラスのManagement Classについて再始動結果を検証し、MC15のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC15のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC15 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC15の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC15 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC15
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC15のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC15 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Domain が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0566"><h3>管理クラス Management Class 変更前の確認 MC02</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>変更前の確認では 管理クラス の クライアント詳細 を主操作として MC02 を判定します。変更対象と非対象の境界への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC02 に残します。変更前の確認を補助する オプション確認 では DIRMC を補助値として MC02 へ保存します。主判定の変更前の確認では管理クラスの クライアント詳細 から DefaultManagement を読み MC02 へ残します。証跡照合の変更前の確認では管理クラスの DefaultManagement と DIRMC を MC02 に保存します。記録対応の変更前の確認では管理クラスの Management ClassとDefault の証跡へ MC02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「管理クラス Management Class 変更前の確認 MC02」を「ノード管理 Client Node 通常状態の確認 NODE01」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はClient Nodeで通常状態の確認ではノード管理の ノード照会からLastAccessを読みである。ノード管理 Client Node 通常状態の確認 NODE01固有の属性も確認対象に含める。</li><li>B. 仕様上の役割はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 仕様上の役割はManagement Classで変更前の確認では管理クラスの クライアント詳細からDefaultManagである。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで変更確認でCの記述「Management Classで変更前の確認では管理クラスの」に対応する項目は変更前の確認 MC02（Managem・変更確認）です。管理ク・変更前に関する管理クラスの仕様は「Management Classで変更前の確認では管理クラスの」で、確認対象はManagem・変更確認です。Clien・通常状態確のA:は「Client Nodeで通常状態の確認ではノード管理の」を述べ、対象は通常状態の確認 NODE01（Client・通常状態）です。ポリシで保守のB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・保守）です。Actiを解除のD:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・解除）です。Manaを変更確認という用語は「Management Classで変更前の確認では管」を指し、変更前の確認 MC02（Managem・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 変更前の確認 MC02</strong></p><p>検証目的: 管理クラスのManagement Classについて変更前の証跡を保存し、MC02のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC02のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC02 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC02のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC02 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC02の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC02 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC02
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Domain が画面・出力に表示されること
② ステップ2 の DIRMC が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0567"><h3>管理クラス Management Class 変更後の確認 MC03</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>変更後の確認では 管理クラス の オプション確認 を主操作として MC03 を判定します。反映値と残存値への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC03 に残します。変更後の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC03 へ保存します。主判定の変更後の確認では管理クラスの オプション確認 から DIRMC を読み MC03 へ残します。証跡照合の変更後の確認では管理クラスの DIRMC と ManagementClass を MC03 に保存します。記録対応の変更後の確認では管理クラスの Management ClassとDefault の証跡へ MC03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 変更後の確認 MC03の役割を調べています。ノード管理 Client Node 変更後の確認 NODE03の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはClient Nodeで変更後の確認ではノード管理の 関連付けからAssociatedNodeを読みである。</li><li>B. 機能の説明としてはStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 機能の説明としてはManagement Classで変更後の確認では管理クラスの オプション確認からDIRMCを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで変更確認でCの記述「Management Classで変更後の確認では管理クラスの」に対応する項目は変更後の確認 MC03（Managem・変更確認）です。管理ク・変更後に関する管理クラスの仕様は「Management Classで変更後の確認では管理クラスの」で、確認対象はManagem・変更確認です。Clien・変更確認のA:は「Client Nodeで変更後の確認ではノード管理の」を述べ、対象は変更後の確認 NODE03（Client・変更確認）です。サーバで変更のB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・変更）です。Poliを抑止のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・抑止）です。Manaを変更確認という用語は「Management Classで変更後の確認では管」を指し、変更後の確認 MC03（Managem・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 変更後の確認 MC03</strong></p><p>検証目的: 管理クラスのManagement Classについて変更結果を検証し、MC03のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC03のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC03 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC03の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC03 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC03
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC03のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC03 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Domain が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0568"><h3>管理クラス Management Class 引継ぎ記録 MC09</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>引継ぎ記録では 管理クラス の オプション確認 を主操作として MC09 を判定します。次担当者が追跡できる証跡への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC09 に残します。引継ぎ記録を補助する 管理クラス照会 では ManagementClass を補助値として MC09 へ保存します。主判定の引継ぎ記録では管理クラスの オプション確認 から DIRMC を読み MC09 へ残します。証跡照合の引継ぎ記録では管理クラスの DIRMC と ManagementClass を MC09 に保存します。記録対応の引継ぎ記録では管理クラスの Management ClassとDefault の証跡へ MC09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 引継ぎ記録 MC09を同一分類のリストア確認 Client Restore 性能影響の確認 RST11と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はClient Restoreで性能影響の確認ではリストア確認の 別名復元からrestoredを読みである。</li><li>B. 構成を確認する際の意味はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 構成を確認する際の意味はManagement Classで引継ぎ記録では管理クラスの オプション確認からDIRMCを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで管理クラスでCの記述「Management Classで引継ぎ記録では管理クラスの」に対応する項目は引継ぎ記録 MC09（Managem・管理クラ）です。管理ク・引継ぎに関する管理クラスの仕様は「Management Classで引継ぎ記録では管理クラスの」で、確認対象はManagem・管理クラスです。Clien・性能影響確のA:は「Client Restoreで性能影響の確認ではリストア確認の」を述べ、対象は性能影響の確認 RST11（Client・性能影響）です。ポリシで移行のB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・移行）です。Evenを計画のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・計画）です。Manaを管理クラスという用語は「Management Classで引継ぎ記録では管理」を指し、引継ぎ記録 MC09（Managem・管理クラ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 引継ぎ記録 MC09</strong></p><p>検証目的: 管理クラスのManagement Classについて再現可能な記録を作成し、MC09のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC09のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC09 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC09の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC09 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC09
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC09のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC09 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Domain が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0569"><h3>管理クラス Management Class 復旧後の確認 MC06</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>復旧後の確認では 管理クラス の オプション確認 を主操作として MC06 を判定します。再発していないことを示す値への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC06 に残します。復旧後の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC06 へ保存します。主判定の復旧後の確認では管理クラスの オプション確認 から DIRMC を読み MC06 へ残します。証跡照合の復旧後の確認では管理クラスの DIRMC と ManagementClass を MC06 に保存します。記録対応の復旧後の確認では管理クラスの Management ClassとDefault の証跡へ MC06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 復旧後の確認 MC06を保守記録に説明する必要があります。管理クラス Management Class 停止前の確認 MC14と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。</li><li>B. 運用時に利用する技術的役割はManagement Classで復旧後の確認では管理クラスの オプション確認からDIRMCを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 運用時に利用する技術的役割はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで復旧確認でBの記述「Management Classで復旧後の確認では管理クラスの」に対応する項目は復旧後の確認 MC06（Managem・復旧確認）です。管理ク・復旧後に関する管理クラスの仕様は「Management Classで復旧後の確認では管理クラスの」で、確認対象はManagem・復旧確認です。Manag・停止確認のA:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Managem・停止確認）です。移行時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・移行）です。Actiを計画のD:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・計画）です。Manaを復旧確認という用語は「Management Classで復旧後の確認では管」を指し、復旧後の確認 MC06（Managem・復旧確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 復旧後の確認 MC06</strong></p><p>検証目的: 管理クラスのManagement Classについて復旧後の安定性を確認し、MC06のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC06のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC06 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC06の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC06 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC06
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC06のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC06 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Domain が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0570"><h3>管理クラス Management Class 復旧準備 MC05</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>復旧準備では 管理クラス の クライアント詳細 を主操作として MC05 を判定します。再開前に必要な整合性への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC05 に残します。復旧準備を補助する オプション確認 では DIRMC を補助値として MC05 へ保存します。主判定の復旧準備では管理クラスの クライアント詳細 から DefaultManagement を読み MC05 へ残します。証跡照合の復旧準備では管理クラスの DefaultManagement と DIRMC を MC05 に保存します。記録対応の復旧準備では管理クラスの Management ClassとDefault の証跡へ MC05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 復旧準備 MC05の技術的な意味を資料で確認するとき、ノード管理 Client Node 障害切り分け NODE04との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はClient Nodeで障害切り分けではノード管理の ノード照会からLastAccessを読み・ノードに使うである。</li><li>B. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>D. コマンドまたは機能の用途はManagement Classで復旧準備では管理クラスの クライアント詳細からDefaultManagemである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで復旧準備でDの記述「Management Classで復旧準備では管理クラスの」に対応する項目は復旧準備 MC05（Managem・復旧準備）です。管理ク・復旧準に関する管理クラスの仕様は「Management Classで復旧準備では管理クラスの」で、確認対象はManagem・復旧準備です。Clien・ノードのA:は「Client Nodeで障害切り分けではノード管理の」を述べ、対象は障害切り分け NODE04（Client・ノード）です。ポリシで変更のB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・変更）です。解析時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・解析）です。Manaを復旧準備という用語は「Management Classで復旧準備では管理ク」を指し、復旧準備 MC05（Managem・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 復旧準備 MC05</strong></p><p>検証目的: 管理クラスのManagement Classについて復旧条件を確認し、MC05のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC05のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC05 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC05のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC05 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC05の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC05 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC05
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Domain が画面・出力に表示されること
② ステップ2 の DIRMC が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0571"><h3>管理クラス Management Class 性能影響の確認 MC11</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>性能影響の確認では 管理クラス の クライアント詳細 を主操作として MC11 を判定します。処理時間と滞留箇所への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC11 に残します。性能影響の確認を補助する オプション確認 では DIRMC を補助値として MC11 へ保存します。主判定の性能影響の確認では管理クラスの クライアント詳細 から DefaultManagement を読み MC11 へ残します。証跡照合の性能影響の確認では管理クラスの DefaultManagement と DIRMC を MC11 に保存します。記録対応の性能影響の確認では管理クラスの Management ClassとDefault の証跡へ MC11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 性能影響の確認 MC11の役割を調べています。ノード管理 Client Node 性能影響の確認 NODE11の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はClient Nodeで性能影響の確認ではノード管理の 占有量照会からLogicalFilesを読みである。</li><li>B. 障害切り分けに用いる役割はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 障害切り分けに用いる役割はManagement Classで性能影響の確認では管理クラスのである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで性能影響確でDの記述「Management Classで性能影響の確認では管理クラスのであ」に対応する項目は性能影響の確認 MC11（Managem・性能影響）です。管理ク・性能影に関する管理クラスの仕様は「Management Classで性能影響の確認では管理クラスの」で、確認対象はManagem・性能影響確です。Clien・性能影響確のA:は「Client Nodeで性能影響の確認ではノード管理の」を述べ、対象は性能影響の確認 NODE11（Client・性能影響）です。クライで移行のB:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・移行）です。解析時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解析）です。Manaを性能影響確という用語は「Management Classで性能影響の確認では」を指し、性能影響の確認 MC11（Managem・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 性能影響の確認 MC11</strong></p><p>検証目的: 管理クラスのManagement Classについて負荷と待ちを確認し、MC11のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC11のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC11 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC11のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC11 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC11の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC11 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC11
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Domain が画面・出力に表示されること
② ステップ2 の DIRMC が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0572"><h3>管理クラス Management Class 構成監査 MC08</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>構成監査では 管理クラス の クライアント詳細 を主操作として MC08 を判定します。定義値と稼働値の一致への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC08 に残します。構成監査を補助する オプション確認 では DIRMC を補助値として MC08 へ保存します。主判定の構成監査では管理クラスの クライアント詳細 から DefaultManagement を読み MC08 へ残します。証跡照合の構成監査では管理クラスの DefaultManagement と DIRMC を MC08 に保存します。記録対応の構成監査では管理クラスの Management ClassとDefault の証跡へ MC08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 構成監査 MC08の設定や表示を読む前に役割を確認します。コピーグループ Backup and Archive Copy Groupではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はBackup andで代替経路の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。</li><li>B. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 一次資料が示す主目的はManagement Classで構成監査では管理クラスの クライアント詳細からDefaultManagemである。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで構成監査でCの記述「Management Classで構成監査では管理クラスの」に対応する項目は構成監査 MC08（Managem・構成監査）です。管理ク・構成監に関する管理クラスの仕様は「Management Classで構成監査では管理クラスの」で、確認対象はManagem・構成監査です。Backu・代替経路確のA:は「Backup andで代替経路の確認ではコピーグループの」を述べ、対象は代替経路の確認 CG10（Backup・代替経路）です。ポリシで診断のB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・診断）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。Manaを構成監査という用語は「Management Classで構成監査では管理ク」を指し、構成監査 MC08（Managem・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 構成監査 MC08</strong></p><p>検証目的: 管理クラスのManagement Classについて構成差分を監査し、MC08のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC08のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC08 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC08のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC08 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC08の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC08 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC08
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Domain が画面・出力に表示されること
② ステップ2 の DIRMC が画面・出力に表示されること
③ ステップ3 の Policy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0573"><h3>管理クラス Management Class 権限境界の確認 MC12</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>権限境界の確認では 管理クラス の オプション確認 を主操作として MC12 を判定します。参照操作と変更操作の分離への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC12 に残します。権限境界の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC12 へ保存します。主判定の権限境界の確認では管理クラスの オプション確認 から DIRMC を読み MC12 へ残します。証跡照合の権限境界の確認では管理クラスの DIRMC と ManagementClass を MC12 に保存します。記録対応の権限境界の確認では管理クラスの Management ClassとDefault の証跡へ MC12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 権限境界の確認 MC12について構成や状態を確認します。管理クラス Management Class 依存関係の確認 MC13ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはManagement Classで依存関係の確認では管理クラスのである。</li><li>B. 状態を読み取るための働きはManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>D. 状態を読み取るための働きはEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで権限境界確でBの記述「Management Classで権限境界の確認では管理クラスの」に対応する項目は権限境界の確認 MC12（Managem・権限境界）です。管理ク・権限境に関する管理クラスの仕様は「Management Classで権限境界の確認では管理クラスの」で、確認対象はManagem・権限境界確です。Manag・依存関係確のA:は「Management Classで依存関係の確認では管理クラスの」を述べ、対象は依存関係の確認 MC13（Managem・依存関係）です。診断時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・診断）です。Evenを抑止のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・抑止）です。Manaを権限境界確という用語は「Management Classで権限境界の確認では」を指し、権限境界の確認 MC12（Managem・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 権限境界の確認 MC12</strong></p><p>検証目的: 管理クラスのManagement Classについて実行権限を点検し、MC12のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC12のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC12 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC12の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC12 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC12
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC12のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC12 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
② ステップ2 の Policy が画面・出力に表示されること
③ ステップ3 の Domain が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0574"><h3>管理クラス Management Class 通常状態の確認 MC01</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>通常状態の確認では 管理クラス の 管理クラス照会 を主操作として MC01 を判定します。基準値と現在値の差への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC01 に残します。通常状態の確認を補助する クライアント詳細 では DefaultManagement を補助値として MC01 へ保存します。主判定の通常状態の確認では管理クラスの 管理クラス照会 から ManagementClass を読み MC01 へ残します。証跡照合の通常状態の確認では管理クラスの ManagementClass と DefaultManagement を MC01 に保存します。記録対応の通常状態の確認では管理クラスの Management ClassとDefault の証跡へ MC01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 通常状態の確認 MC01を同一分類のバックアップ運用 Incremental Backup ログとの照合 BKP07と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はIncremental Backupでログとの照合ではバックアップ運用の 増分実行からobjectsを読みである。</li><li>B. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 管理対象との関係を表す説明はManagement Classで通常状態の確認では管理クラスのである。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで通常状態確でCの記述「Management Classで通常状態の確認では管理クラスのであ」に対応する項目は通常状態の確認 MC01（Managem・通常状態）です。管理ク・通常状に関する管理クラスの仕様は「Management Classで通常状態の確認では管理クラスの」で、確認対象はManagem・通常状態確です。Incre・ログとの照のA:は「Incremental Backupでログとの照合ではバックアップ運」を述べ、対象はログとの照合 BKP07（Increme・ログとの）です。クライで保守のB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保守）です。Scheを解除のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・解除）です。Manaを通常状態確という用語は「Management Classで通常状態の確認では」を指し、通常状態の確認 MC01（Managem・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 通常状態の確認 MC01</strong></p><p>検証目的: 管理クラスのManagement Classについて通常状態を確定し、MC01のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC01 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC01の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC01 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC01
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC01のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC01 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC01のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Domain が画面・出力に表示されること
③ ステップ3 の DIRMC が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0575"><h3>管理クラス Management Class 障害切り分け MC04</h3><p class="kb-meta">分類: 管理クラス ・ 難易度: 初級</p><p>障害切り分けでは 管理クラス の 管理クラス照会 を主操作として MC04 を判定します。最初に失敗した処理への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC04 に残します。障害切り分けを補助する クライアント詳細 では DefaultManagement を補助値として MC04 へ保存します。主判定の障害切り分けでは管理クラスの 管理クラス照会 から ManagementClass を読み MC04 へ残します。証跡照合の障害切り分けでは管理クラスの ManagementClass と DefaultManagement を MC04 に保存します。記録対応の障害切り分けでは管理クラスの Management ClassとDefault の証跡へ MC04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 管理クラス Management Class 障害切り分け MC04について構成や状態を確認します。コピーグループ Backup and Archive Copy Groupではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはBackup andで復旧後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。コピーグループ Backup and Archive Copy固有の属性も確認対象に含める。</li><li>B. 対象資源に対する働きはManagement Classで障害切り分けでは管理クラスの 管理クラス照会からManagementClaである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 管理クで管理クラスでBの記述「Management Classで障害切り分けでは管理クラスの」に対応する項目は障害切り分け MC04（Managem・管理クラ）です。管理ク・障害切に関する管理クラスの仕様は「Management Classで障害切り分けでは管理クラスの」で、確認対象はManagem・管理クラスです。Backu・復旧確認のA:は「Backup andで復旧後の確認ではコピーグループの」を述べ、対象は復旧後の確認 CG06（Backup・復旧確認）です。監査時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査）です。Expiを計画のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・計画）です。Manaを管理クラスという用語は「Management Classで障害切り分けでは管」を指し、障害切り分け MC04（Managem・管理クラ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>管理クラス Management Class 障害切り分け MC04</strong></p><p>検証目的: 管理クラスのManagement Classについて障害範囲を限定し、MC04のManagement ClassとDefaultを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC04 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC04の管理クラス照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS MC04 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Policy Domain Name: MC04
Policy Set Name: ACTIVE
Management Class Name: STANDARD
Default Management Class: Yes
画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC04のクライアント詳細を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query mgmtclass -detail
→ Enter を押す
［画面・出力］
Domain Name: MC04 Active Policy Set: ACTIVE Default Management Class: STANDARD
画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC04のオプション確認を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query option
→ Enter を押す
［画面・出力］
DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Policy が画面・出力に表示されること
② ステップ2 の Domain が画面・出力に表示されること
③ ステップ3 の DIRMC が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## 複製・保護


<section class="kb-item" id="c14-i0576"><h3>複製・保護 Storage Pool Protection and Node Replication ログとの照合 REPL07</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>ログとの照合では 複製・保護 の プール保護 を主操作として REPL07 を判定します。時刻と対象識別子への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL07 に残します。ログとの照合を補助する 複製状態 では TargetServer を補助値として REPL07 へ保存します。主判定のログとの照合では複製・保護の プール保護 から ANR0984I を読み REPL07 へ残します。証跡照合のログとの照合では複製・保護の ANR0984I と TargetServer を REPL07 に保存します。記録対応のログとの照合では複製・保護の Replication StatusとTarget Server の証跡へ REPL07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationの設定や表示を読む前に役割を確認します。ポリシーと管理クラス Policy Domain 0005ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>B. 対象資源に対する働きはStorage Poolでログとの照合では複製・保護の プール保護からANR0984Iを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 対象資源に対する働きはクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。policy domain ノード割当確認 保持期間固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> ログとの対象StoraでBの記述「Storage Poolでログとの照合では複製・保護の」に対応する項目はログとの照合 REPL07（Storag・ログと・ログとの）です。保護・ログとに関する複製・保護の仕様は「Storage Poolでログとの照合では複製・保護の」で、確認対象はStora・ログと・ログとのです。Polic・巡回のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・巡回・管理クラ）です。登録時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・登録・開始時刻）です。poliをノード割当のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」を述べ、対象はノード割当確認 保持期間（policy・ノード・保持期間）です。Storをログとの照という用語は「Storage Poolでログとの照合では複製」を指し、ログとの照合 REPL07（Storag・ログと・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication ログとの照合 REPL07</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて操作とログを対応し、REPL07のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL07を指定し、REPL07のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL07
→ Enter を押す
［画面・出力］
ANR0984I Process 07 for PROTECT STORAGE POOL started. ANR0985I Process 07 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE07を指定し、REPL07の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE07
→ Enter を押す
［画面・出力］
Node Name: NODE07 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE07を指定し、REPL07の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE07
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE07 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の ANR3730I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0577"><h3>複製・保護 Storage Pool Protection and Node Replication 代替経路の確認 REPL10</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>代替経路の確認では 複製・保護 の プール保護 を主操作として REPL10 を判定します。主経路との役割差への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL10 に残します。代替経路の確認を補助する 複製状態 では TargetServer を補助値として REPL10 へ保存します。主判定の代替経路の確認では複製・保護の プール保護 から ANR0984I を読み REPL10 へ残します。証跡照合の代替経路の確認では複製・保護の ANR0984I と TargetServer を REPL10 に保存します。記録対応の代替経路の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationの役割を調べています。クライアントスケジュール Action 0006の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>B. 表示や設定で扱う内容はStorage Poolで代替経路の確認では複製・保護の プール保護からANR0984Iを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 表示や設定で扱う内容はストレージプール内の空き領域を回収する処理を容量監視として確認する。reclamation 容量監視 一覧画面固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 代替経路対象StoraでBの記述「Storage Poolで代替経路の確認では複製・保護の」に対応する項目は代替経路の確認 REPL10（Storag・代替経・代替経路）です。保護・代替経に関する複製・保護の仕様は「Storage Poolで代替経路の確認では複製・保護の」で、確認対象はStora・代替経・代替経路です。Actio・巡回のA:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・巡回・開始時刻）です。保護時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・保護・スケジュ）です。reclを管理クラスのD:は「ストレージプール内の空き領域を回収する処理を容量監視として確認する」を述べ、対象は容量監視 一覧画面（reclam・管理ク・一覧画面）です。Storを代替経路確という用語は「Storage Poolで代替経路の確認では複製」を指し、代替経路の確認 REPL10（Storag・代替経・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 代替経路の確認 REPL10</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて代替手段の成立を確認し、REPL10のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL10を指定し、REPL10のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL10
→ Enter を押す
［画面・出力］
ANR0984I Process 10 for PROTECT STORAGE POOL started. ANR0985I Process 10 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE10を指定し、REPL10の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE10
→ Enter を押す
［画面・出力］
Node Name: NODE10 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE10を指定し、REPL10の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE10
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE10 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の ANR3730I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0578"><h3>複製・保護 Storage Pool Protection and Node Replication 依存関係の確認 REPL13</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>依存関係の確認では 複製・保護 の プール保護 を主操作として REPL13 を判定します。前提資源と後続処理の順序への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL13 に残します。依存関係の確認を補助する 複製状態 では TargetServer を補助値として REPL13 へ保存します。主判定の依存関係の確認では複製・保護の プール保護 から ANR0984I を読み REPL13 へ残します。証跡照合の依存関係の確認では複製・保護の ANR0984I と TargetServer を REPL13 に保存します。記録対応の依存関係の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationを保守記録に説明する必要があります。サーバー日次運用 Server Name 0001と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はStorage Poolで依存関係の確認では複製・保護の プール保護からANR0984Iを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 保守作業で参照する機能はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。サーバー日次運用 Storage Pool 0265固有の属性も確認対象に含める。</li><li>D. 保守作業で参照する機能はサーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 依存関係対象StoraでAの記述「Storage Poolで依存関係の確認では複製・保護の」に対応する項目は依存関係の確認 REPL13（Storag・依存関・依存関係）です。保護・依存関に関する複製・保護の仕様は「Storage Poolで依存関係の確認では複製・保護の」で、確認対象はStora・依存関・依存関係です。巡回対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・巡回・DBバッ）です。照合時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・照合・ストレー）です。nodeを管理クラスのD:は「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」を述べ、対象はコマンド証跡 マクロ実行（node・管理ク・マクロ実）です。Storを依存関係確という用語は「Storage Poolで依存関係の確認では複製」を指し、依存関係の確認 REPL13（Storag・依存関・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 依存関係の確認 REPL13</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて依存資源を点検し、REPL13のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL13を指定し、REPL13のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL13
→ Enter を押す
［画面・出力］
ANR0984I Process 13 for PROTECT STORAGE POOL started. ANR0985I Process 13 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE13を指定し、REPL13の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE13
→ Enter を押す
［画面・出力］
Node Name: NODE13 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE13を指定し、REPL13の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE13
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE13 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の ANR3730I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0579"><h3>複製・保護 Storage Pool Protection and Node Replication 停止前の確認 REPL14</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>停止前の確認では 複製・保護 の 複製状態 を主操作として REPL14 を判定します。処理中資源と未完了要求への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL14 に残します。停止前の確認を補助する 検証 では ANR3730I を補助値として REPL14 へ保存します。主判定の停止前の確認では複製・保護の 複製状態 から TargetServer を読み REPL14 へ残します。証跡照合の停止前の確認では複製・保護の TargetServer と ANR3730I を REPL14 に保存します。記録対応の停止前の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationに関する障害切り分けの前提を確認しています。ポリシーと管理クラス Policy Domain 0020の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>B. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 障害切り分けに用いる役割はバックアップ版数と保存先を定めるコピー規則をノード割当確認する。backup copy group ノード割当確認 再同期判断固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はStorage Poolで停止前の確認では複製・保護の 複製状態からTargetServerを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 停止確認対象StoraでDの記述「Storage Poolで停止前の確認では複製・保護の」に対応する項目は停止前の確認 REPL14（Storag・停止確・停止前の）です。保護・停止前に関する複製・保護の仕様は「Storage Poolで停止前の確認では複製・保護の」で、確認対象はStora・停止確・停止前のです。Polic・棚卸のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・棚卸・管理クラ）です。照合対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合・ノード登）です。ノード割時のbackuのC:は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」を述べ、対象はノード割当確認 再同期判断（backup・ノード・再同期判）です。Storを停止確認という用語は「Storage Poolで停止前の確認では複製」を指し、停止前の確認 REPL14（Storag・停止確・停止前の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 停止前の確認 REPL14</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて安全な停止条件を確認し、REPL14のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE14を指定し、REPL14の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE14
→ Enter を押す
［画面・出力］
Node Name: NODE14 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE14を指定し、REPL14の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE14
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE14 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL14を指定し、REPL14のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL14
→ Enter を押す
［画面・出力］
ANR0984I Process 14 for PROTECT STORAGE POOL started. ANR0985I Process 14 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の ANR3730I が画面・出力に表示されること
③ ステップ3 の ANR0984I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0580"><h3>複製・保護 Storage Pool Protection and Node Replication 再始動後の確認 REPL15</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>再始動後の確認では 複製・保護 の 検証 を主操作として REPL15 を判定します。再開点と未処理データへの注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL15 に残します。再始動後の確認を補助する プール保護 では ANR0984I を補助値として REPL15 へ保存します。主判定の再始動後の確認では複製・保護の 検証 から ANR3730I を読み REPL15 へ残します。証跡照合の再始動後の確認では複製・保護の ANR3730I と ANR0984I を REPL15 に保存します。記録対応の再始動後の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationの設定や表示を読む前に役割を確認します。ポリシーと管理クラス Policy Set 0047ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>B. 状態を読み取るための働きはDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 状態を読み取るための働きはStorage Poolで再始動後の確認では複製・保護の 検証からANR3730Iを読み・再始動確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはバックアップ版数と保存先を定めるコピー規則をノード割当確認する。backup copy group ノード割当確認 再同期判断固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 再始動確対象StoraでCの記述「Storage Poolで再始動後の確認では複製・保護の」に対応する項目は再始動後の確認 REPL15（Storag・再始動・再始動後）です。保護・再始動に関する複製・保護の仕様は「Storage Poolで再始動後の確認では複製・保護の」で、確認対象はStora・再始動・再始動後です。Polic・復旧のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・復旧・ディレク）です。保護対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・保護・期限切れ）です。backをノード割当のD:は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」を述べ、対象はノード割当確認 再同期判断（backup・ノード・再同期判）です。Storを再始動確認という用語は「Storage Poolで再始動後の確認では複製」を指し、再始動後の確認 REPL15（Storag・再始動・再始動後）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 再始動後の確認 REPL15</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて再始動結果を検証し、REPL15のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE15を指定し、REPL15の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE15
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE15 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL15を指定し、REPL15のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL15
→ Enter を押す
［画面・出力］
ANR0984I Process 15 for PROTECT STORAGE POOL started. ANR0985I Process 15 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE15を指定し、REPL15の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE15
→ Enter を押す
［画面・出力］
Node Name: NODE15 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
② ステップ2 の ANR0984I が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0581"><h3>複製・保護 Storage Pool Protection and Node Replication 変更前の確認 REPL02</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>変更前の確認では 複製・保護 の 複製状態 を主操作として REPL02 を判定します。変更対象と非対象の境界への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL02 に残します。変更前の確認を補助する 検証 では ANR3730I を補助値として REPL02 へ保存します。主判定の変更前の確認では複製・保護の 複製状態 から TargetServer を読み REPL02 へ残します。証跡照合の変更前の確認では複製・保護の TargetServer と ANR3730I を REPL02 に保存します。記録対応の変更前の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationの役割を調べています。クライアントスケジュール Association 0060の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Association 0060固有の属性も確認対象に含める。</li><li>B. 障害切り分けに用いる役割はStorage Poolで変更前の確認では複製・保護の 複製状態からTargetServerを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 障害切り分けに用いる役割はバックアップ版数と保存先を定めるコピー規則を容量監視として確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認対象StoraでBの記述「Storage Poolで変更前の確認では複製・保護の」に対応する項目は変更前の確認 REPL02（Storag・変更確・変更前の）です。保護・変更前に関する複製・保護の仕様は「Storage Poolで変更前の確認では複製・保護の」で、確認対象はStora・変更確・変更前のです。Assoc・監査のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・監査・関連ノー）です。切替時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・切替・管理クラ）です。backをコピーグルのD:は「バックアップ版数と保存先を定めるコピー規則を容量監視として確認する」を述べ、対象は容量監視 復元前提（backup・コピー・復元前提）です。Storを変更確認という用語は「Storage Poolで変更前の確認では複製」を指し、変更前の確認 REPL02（Storag・変更確・変更前の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 変更前の確認 REPL02</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて変更前の証跡を保存し、REPL02のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE02を指定し、REPL02の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE02
→ Enter を押す
［画面・出力］
Node Name: NODE02 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE02を指定し、REPL02の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE02
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE02 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL02を指定し、REPL02のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL02
→ Enter を押す
［画面・出力］
ANR0984I Process 02 for PROTECT STORAGE POOL started. ANR0985I Process 02 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の ANR3730I が画面・出力に表示されること
③ ステップ3 の ANR0984I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0582"><h3>複製・保護 Storage Pool Protection and Node Replication 変更後の確認 REPL03</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>変更後の確認では 複製・保護 の 検証 を主操作として REPL03 を判定します。反映値と残存値への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL03 に残します。変更後の確認を補助する プール保護 では ANR0984I を補助値として REPL03 へ保存します。主判定の変更後の確認では複製・保護の 検証 から ANR3730I を読み REPL03 へ残します。証跡照合の変更後の確認では複製・保護の ANR3730I と ANR0984I を REPL03 に保存します。記録対応の変更後の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationについて構成や状態を確認します。クライアントスケジュール Start Time 0048ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 状態を読み取るための働きはAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 状態を読み取るための働きはサーバー操作とメッセージを追跡するログを復元前確認する。activity log 復元前確認 管理クラス固有の属性も確認対象に含める。</li><li>D. 状態を読み取るための働きはStorage Poolで変更後の確認では複製・保護の 検証からANR3730Iを読み・変更確認に使うである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認対象StoraでDの記述「Storage Poolで変更後の確認では複製・保護の」に対応する項目は変更後の確認 REPL03（Storag・変更確・変更後の）です。保護・変更後に関する複製・保護の仕様は「Storage Poolで変更後の確認では複製・保護の」で、確認対象はStora・変更確・変更後のです。Start・復旧のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・復旧・失敗理由）です。確認対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・確認・関連ノー）です。復元前確時のactivのC:は「サーバー操作とメッセージを追跡するログを復元前確認する」を述べ、対象は復元前確認 管理クラス（activi・復元前・管理クラ）です。Storを変更確認という用語は「Storage Poolで変更後の確認では複製」を指し、変更後の確認 REPL03（Storag・変更確・変更後の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 変更後の確認 REPL03</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて変更結果を検証し、REPL03のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE03を指定し、REPL03の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE03
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE03 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL03を指定し、REPL03のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL03
→ Enter を押す
［画面・出力］
ANR0984I Process 03 for PROTECT STORAGE POOL started. ANR0985I Process 03 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE03を指定し、REPL03の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE03
→ Enter を押す
［画面・出力］
Node Name: NODE03 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
② ステップ2 の ANR0984I が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0583"><h3>複製・保護 Storage Pool Protection and Node Replication 引継ぎ記録 REPL09</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>引継ぎ記録では 複製・保護 の 検証 を主操作として REPL09 を判定します。次担当者が追跡できる証跡への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL09 に残します。引継ぎ記録を補助する プール保護 では ANR0984I を補助値として REPL09 へ保存します。主判定の引継ぎ記録では複製・保護の 検証 から ANR3730I を読み REPL09 へ残します。証跡照合の引継ぎ記録では複製・保護の ANR3730I と ANR0984I を REPL09 に保存します。記録対応の引継ぎ記録では複製・保護の Replication StatusとTarget Server の証跡へ REPL09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「複製・保護 Storage Pool Protection and Node Replication」を「サーバーDB・DR Server Database Backup 構成監査」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はDBで構成監査ではサーバーの DBバックアップからANR4550Iを読み・構成監査に使うである。</li><li>B. 運用時に利用する技術的役割はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Node Name 0208固有の属性も確認対象に含める。</li><li>C. 運用時に利用する技術的役割はStorage Poolで引継ぎ記録では複製・保護の 検証からANR3730Iを読み・複製・保護に使うである。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はストレージプール内の空き領域を回収する処理である。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 複製対象StoraでCの記述「Storage Poolで引継ぎ記録では複製・保護の」に対応する項目は引継ぎ記録 REPL09（Storag・複製・引継ぎ記）です。保護・引継ぎに関する複製・保護の仕様は「Storage Poolで引継ぎ記録では複製・保護の」で、確認対象はStora・複製・引継ぎ記です。構成監査対象構成監査でのA:は「DBで構成監査ではサーバーの DBバックアップからANR4550Iを」を述べ、対象は構成監査 DBBK08（DB・構成監・構成監査）です。登録対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・登録・運用状態）です。reclを保存期間確のD:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は保存期間確認 画面タグ（reclam・保存期・画面タグ）です。Storを複製・保護という用語は「Storage Poolで引継ぎ記録では複製」を指し、引継ぎ記録 REPL09（Storag・複製・引継ぎ記）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 引継ぎ記録 REPL09</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて再現可能な記録を作成し、REPL09のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE09を指定し、REPL09の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE09
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE09 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL09を指定し、REPL09のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL09
→ Enter を押す
［画面・出力］
ANR0984I Process 09 for PROTECT STORAGE POOL started. ANR0985I Process 09 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE09を指定し、REPL09の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE09
→ Enter を押す
［画面・出力］
Node Name: NODE09 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
② ステップ2 の ANR0984I が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0584"><h3>複製・保護 Storage Pool Protection and Node Replication 復旧後の確認 REPL06</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>復旧後の確認では 複製・保護 の 検証 を主操作として REPL06 を判定します。再発していないことを示す値への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL06 に残します。復旧後の確認を補助する プール保護 では ANR0984I を補助値として REPL06 へ保存します。主判定の復旧後の確認では複製・保護の 検証 から ANR3730I を読み REPL06 へ残します。証跡照合の復旧後の確認では複製・保護の ANR3730I と ANR0984I を REPL06 に保存します。記録対応の復旧後の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationに関する障害切り分けの前提を確認しています。クライアントスケジュール Schedule Name 0069の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>B. 機能の説明としてはStorage Poolで復旧後の確認では複製・保護の 検証からANR3730Iを読み・復旧確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 機能の説明としてはクライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認する。policy domain 復元前確認 統合管理固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認対象StoraでBの記述「Storage Poolで復旧後の確認では複製・保護の」に対応する項目は復旧後の確認 REPL06（Storag・復旧確・復旧後の）です。保護・復旧後に関する複製・保護の仕様は「Storage Poolで復旧後の確認では複製・保護の」で、確認対象はStora・復旧確・復旧後のです。Sched・監査のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・監査・スケジュ）です。登録時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・登録・管理クラ）です。poliを復元前確認のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」を述べ、対象は復元前確認 統合管理（policy・復元前・統合管理）です。Storを復旧確認という用語は「Storage Poolで復旧後の確認では複製」を指し、復旧後の確認 REPL06（Storag・復旧確・復旧後の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 復旧後の確認 REPL06</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて復旧後の安定性を確認し、REPL06のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE06を指定し、REPL06の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE06
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE06 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL06を指定し、REPL06のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL06
→ Enter を押す
［画面・出力］
ANR0984I Process 06 for PROTECT STORAGE POOL started. ANR0985I Process 06 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE06を指定し、REPL06の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE06
→ Enter を押す
［画面・出力］
Node Name: NODE06 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
② ステップ2 の ANR0984I が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0585"><h3>複製・保護 Storage Pool Protection and Node Replication 復旧準備 REPL05</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>復旧準備では 複製・保護 の 複製状態 を主操作として REPL05 を判定します。再開前に必要な整合性への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL05 に残します。復旧準備を補助する 検証 では ANR3730I を補助値として REPL05 へ保存します。主判定の復旧準備では複製・保護の 複製状態 から TargetServer を読み REPL05 へ残します。証跡照合の復旧準備では複製・保護の TargetServer と ANR3730I を REPL05 に保存します。記録対応の復旧準備では複製・保護の Replication StatusとTarget Server の証跡へ REPL05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationを保守記録に説明する必要があります。ポリシーと管理クラス Policy Set 0032と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>B. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 仕様上の役割はPolicy Domainで障害切り分けではポリシードメインの ドメイン照会からPolicyDomainを読である。</li><li>D. 仕様上の役割はStorage Poolで復旧準備では複製・保護の 複製状態からTargetServerを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧準備対象StoraでDの記述「Storage Poolで復旧準備では複製・保護の」に対応する項目は復旧準備 REPL05（Storag・復旧準・復旧準備）です。保護・復旧準に関する複製・保護の仕様は「Storage Poolで復旧準備では複製・保護の」で、確認対象はStora・復旧準・復旧準備です。Polic・棚卸のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・棚卸・ディレク）です。保護対象PolicのB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・保護・管理クラ）です。ポリシー時のPolicのC:は「Policy Domainで障害切り分けではポリシードメインの」を述べ、対象は障害切り分け DOM04（Policy・ポリシ・障害切り）です。Storを復旧準備という用語は「Storage Poolで復旧準備では複製・保護の」を指し、復旧準備 REPL05（Storag・復旧準・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 復旧準備 REPL05</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて復旧条件を確認し、REPL05のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE05を指定し、REPL05の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE05
→ Enter を押す
［画面・出力］
Node Name: NODE05 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE05を指定し、REPL05の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE05
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE05 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL05を指定し、REPL05のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL05
→ Enter を押す
［画面・出力］
ANR0984I Process 05 for PROTECT STORAGE POOL started. ANR0985I Process 05 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の ANR3730I が画面・出力に表示されること
③ ステップ3 の ANR0984I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0586"><h3>複製・保護 Storage Pool Protection and Node Replication 性能影響の確認 REPL11</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>性能影響の確認では 複製・保護 の 複製状態 を主操作として REPL11 を判定します。処理時間と滞留箇所への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL11 に残します。性能影響の確認を補助する 検証 では ANR3730I を補助値として REPL11 へ保存します。主判定の性能影響の確認では複製・保護の 複製状態 から TargetServer を読み REPL11 へ残します。証跡照合の性能影響の確認では複製・保護の TargetServer と ANR3730I を REPL11 に保存します。記録対応の性能影響の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationについて構成や状態を確認します。クライアントスケジュール Event Status 0012ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Event Status 0012固有の属性も確認対象に含める。</li><li>B. 一次資料が示す主目的はStorage Poolで性能影響の確認では複製・保護の 複製状態からTargetServerを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 一次資料が示す主目的はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を容量監視として確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 性能影響対象StoraでBの記述「Storage Poolで性能影響の確認では複製・保護の」に対応する項目は性能影響の確認 REPL11（Storag・性能影・性能影響）です。保護・性能影に関する複製・保護の仕様は「Storage Poolで性能影響の確認では複製・保護の」で、確認対象はStora・性能影・性能影響です。Event・巡回のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・巡回・イベント）です。保護時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・保護・スケジュ）です。poliを保護設定のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を容」を述べ、対象は容量監視 保護設定（policy・保護設・保護設定）です。Storを性能影響確という用語は「Storage Poolで性能影響の確認では複製」を指し、性能影響の確認 REPL11（Storag・性能影・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 性能影響の確認 REPL11</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて負荷と待ちを確認し、REPL11のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE11を指定し、REPL11の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE11
→ Enter を押す
［画面・出力］
Node Name: NODE11 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE11を指定し、REPL11の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE11
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE11 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL11を指定し、REPL11のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL11
→ Enter を押す
［画面・出力］
ANR0984I Process 11 for PROTECT STORAGE POOL started. ANR0985I Process 11 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の ANR3730I が画面・出力に表示されること
③ ステップ3 の ANR0984I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0587"><h3>複製・保護 Storage Pool Protection and Node Replication 構成監査 REPL08</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>構成監査では 複製・保護 の 複製状態 を主操作として REPL08 を判定します。定義値と稼働値の一致への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL08 に残します。構成監査を補助する 検証 では ANR3730I を補助値として REPL08 へ保存します。主判定の構成監査では複製・保護の 複製状態 から TargetServer を読み REPL08 へ残します。証跡照合の構成監査では複製・保護の TargetServer と ANR3730I を REPL08 に保存します。記録対応の構成監査では複製・保護の Replication StatusとTarget Server の証跡へ REPL08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationを同一分類のクライアントスケジュール Schedule Name 0039と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>B. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. コマンドまたは機能の用途はPolicy Domainでログとの照合ではポリシードメインの ドメイン照会からPolicyDomainを読である。</li><li>D. コマンドまたは機能の用途はStorage Poolで構成監査では複製・保護の 複製状態からTargetServerを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構成監査対象StoraでDの記述「Storage Poolで構成監査では複製・保護の」に対応する項目は構成監査 REPL08（Storag・構成監・構成監査）です。保護・構成監に関する複製・保護の仕様は「Storage Poolで構成監査では複製・保護の」で、確認対象はStora・構成監・構成監査です。Sched・棚卸のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・棚卸・スケジュ）です。収集対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・収集・ドメイン）です。ログとの時のPolicのC:は「Policy Domainでログとの照合ではポリシードメインの」を述べ、対象はログとの照合 DOM07（Policy・ログと・ログとの）です。Storを構成監査という用語は「Storage Poolで構成監査では複製・保護の」を指し、構成監査 REPL08（Storag・構成監・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 構成監査 REPL08</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて構成差分を監査し、REPL08のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE08を指定し、REPL08の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE08
→ Enter を押す
［画面・出力］
Node Name: NODE08 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE08を指定し、REPL08の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE08
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE08 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL08を指定し、REPL08のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL08
→ Enter を押す
［画面・出力］
ANR0984I Process 08 for PROTECT STORAGE POOL started. ANR0985I Process 08 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Node が画面・出力に表示されること
② ステップ2 の ANR3730I が画面・出力に表示されること
③ ステップ3 の ANR0984I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0588"><h3>複製・保護 Storage Pool Protection and Node Replication 権限境界の確認 REPL12</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>権限境界の確認では 複製・保護 の 検証 を主操作として REPL12 を判定します。参照操作と変更操作の分離への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL12 に残します。権限境界の確認を補助する プール保護 では ANR0984I を補助値として REPL12 へ保存します。主判定の権限境界の確認では複製・保護の 検証 から ANR3730I を読み REPL12 へ残します。証跡照合の権限境界の確認では複製・保護の ANR3730I と ANR0984I を REPL12 に保存します。記録対応の権限境界の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationの技術的な意味を資料で確認するとき、クライアントスケジュール Action 0021との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。クライアントスケジュール Action 0021固有の属性も確認対象に含める。</li><li>B. 構成を確認する際の意味はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 構成を確認する際の意味はStorage Poolで権限境界の確認では複製・保護の 検証からANR3730Iを読み・権限境界確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味は保存期間を過ぎた版やアーカイブを期限切れにする処理である。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 権限境界対象StoraでCの記述「Storage Poolで権限境界の確認では複製・保護の」に対応する項目は権限境界の確認 REPL12（Storag・権限境・権限境界）です。保護・権限境に関する複製・保護の仕様は「Storage Poolで権限境界の確認では複製・保護の」で、確認対象はStora・権限境・権限境界です。Actio・棚卸のA:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・棚卸・開始時刻）です。保護対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保護・DBバッ）です。expiを保存期間確のD:は「保存期間を過ぎた版やアーカイブを期限切れにする処理」を述べ、対象は保存期間確認 同期範囲（expira・保存期・同期範囲）です。Storを権限境界確という用語は「Storage Poolで権限境界の確認では複製」を指し、権限境界の確認 REPL12（Storag・権限境・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 権限境界の確認 REPL12</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて実行権限を点検し、REPL12のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE12を指定し、REPL12の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE12
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE12 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL12を指定し、REPL12のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL12
→ Enter を押す
［画面・出力］
ANR0984I Process 12 for PROTECT STORAGE POOL started. ANR0985I Process 12 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE12を指定し、REPL12の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE12
→ Enter を押す
［画面・出力］
Node Name: NODE12 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
② ステップ2 の ANR0984I が画面・出力に表示されること
③ ステップ3 の Node が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0589"><h3>複製・保護 Storage Pool Protection and Node Replication 通常状態の確認 REPL01</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>通常状態の確認では 複製・保護 の プール保護 を主操作として REPL01 を判定します。基準値と現在値の差への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL01 に残します。通常状態の確認を補助する 複製状態 では TargetServer を補助値として REPL01 へ保存します。主判定の通常状態の確認では複製・保護の プール保護 から ANR0984I を読み REPL01 へ残します。証跡照合の通常状態の確認では複製・保護の ANR0984I と TargetServer を REPL01 に保存します。記録対応の通常状態の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「複製・保護 Storage Pool Protection and Node Replication」を「サーバーDB・DR Server Database Backup 権限境界の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULLを読み・権限境界確認に使うである。</li><li>B. 保守作業で参照する機能はStorage Poolで通常状態の確認では複製・保護の プール保護からANR0984Iを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 保守作業で参照する機能はサーバー操作とメッセージを追跡するログをノード割当確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 通常状態対象StoraでBの記述「Storage Poolで通常状態の確認では複製・保護の」に対応する項目は通常状態の確認 REPL01（Storag・通常状・通常状態）です。保護・通常状に関する複製・保護の仕様は「Storage Poolで通常状態の確認では複製・保護の」で、確認対象はStora・通常状・通常状態です。権限境界対象権限境界ののA:は「DBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は権限境界の確認 DBBK12（DB・権限境・権限境界）です。収集時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベント）です。actiをノード割当のD:は「サーバー操作とメッセージを追跡するログをノード割当確認する」を述べ、対象はノード割当確認 セッション上限（activi・ノード・セッショ）です。Storを通常状態確という用語は「Storage Poolで通常状態の確認では複製」を指し、通常状態の確認 REPL01（Storag・通常状・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 通常状態の確認 REPL01</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて通常状態を確定し、REPL01のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL01を指定し、REPL01のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL01
→ Enter を押す
［画面・出力］
ANR0984I Process 01 for PROTECT STORAGE POOL started. ANR0985I Process 01 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE01を指定し、REPL01の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE01
→ Enter を押す
［画面・出力］
Node Name: NODE01 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE01を指定し、REPL01の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE01
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE01 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の ANR3730I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0590"><h3>複製・保護 Storage Pool Protection and Node Replication 障害切り分け REPL04</h3><p class="kb-meta">分類: 複製・保護 ・ 難易度: 上級</p><p>障害切り分けでは 複製・保護 の プール保護 を主操作として REPL04 を判定します。最初に失敗した処理への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL04 に残します。障害切り分けを補助する 複製状態 では TargetServer を補助値として REPL04 へ保存します。主判定の障害切り分けでは複製・保護の プール保護 から ANR0984I を読み REPL04 へ残します。証跡照合の障害切り分けでは複製・保護の ANR0984I と TargetServer を REPL04 に保存します。記録対応の障害切り分けでは複製・保護の Replication StatusとTarget Server の証跡へ REPL04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 複製・保護 Storage Pool Protection and Node Replicationの技術的な意味を資料で確認するとき、クライアントスケジュール Schedule Name 0054との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 管理対象との関係を表す説明はバックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認する。</li><li>D. 管理対象との関係を表す説明はStorage Poolで障害切り分けでは複製・保護の プール保護からANR0984Iを読み・複製である。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 複製対象StoraでDの記述「Storage Poolで障害切り分けでは複製・保護の」に対応する項目は障害切り分け REPL04（Storag・複製・障害切り）です。保護・障害切に関する複製・保護の仕様は「Storage Poolで障害切り分けでは複製・保護の」で、確認対象はStora・複製・障害切りです。Sched・復旧のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・復旧・スケジュ）です。切替対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・切替・ストレー）です。ノード割時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認」を述べ、対象はノード割当確認 変換規則（schedu・ノード・変換規則）です。Storを複製・保護という用語は「Storage Poolで障害切り分けでは複製」を指し、障害切り分け REPL04（Storag・複製・障害切り）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>複製・保護 Storage Pool Protection and Node Replication 障害切り分け REPL04</strong></p><p>検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて障害範囲を限定し、REPL04のReplication StatusとTarget Serverを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL04を指定し、REPL04のプール保護を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; PROTECT STGPOOL REPL04
→ Enter を押す
［画面・出力］
ANR0984I Process 04 for PROTECT STORAGE POOL started. ANR0985I Process 04 completed with completion state SUCCESS.
画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE04を指定し、REPL04の複製状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY REPLICATION NODE04
→ Enter を押す
［画面・出力］
Node Name: NODE04 Target Server: DR1 Status: Complete Files Replicated: 1240
画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE04を指定し、REPL04の検証を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; VALIDATE REPLICATION NODE04
→ Enter を押す
［画面・出力］
ANR3730I Replication validation for node NODE04 completed. Differences: 0
画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
② ステップ2 の Node が画面・出力に表示されること
③ ステップ3 の ANR3730I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>
