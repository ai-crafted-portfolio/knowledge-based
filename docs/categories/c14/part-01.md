---
search:
  exclude: true
---

# IBM Spectrum Protect 8.1 — 詳細 (1/4)

[← IBM Spectrum Protect 8.1 の概要へ戻る](index.md)


## アーカイブ運用


<section class="kb-item" id="c14-i0001"><h3>backup copy group 期限切れ確認 受信操作</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「backup copy group 期限切れ確認 受信操作」は、バックアップ版数と保存先を定めるコピー規則を期限切れ確認の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR063Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> backup copy group 期限切れ確認 受信操作の設定や表示を読む前に役割を確認します。management class 容量監視 分散定義ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視として確認する。</li><li>B. 対象資源に対する働きはStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 対象資源に対する働きはバックアップ版数と保存先を定めるコピー規則を期限切れ確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 期限切で期限切れ確でCの記述「バックアップ版数と保存先を定めるコピー規則を期限切れ確認する」に対応する項目は期限切れ確認 受信操作（backup・期限切れ）です。期限切・受信操に関するアーカイブ運用の仕様は「バックアップ版数と保存先を定めるコピー規則を期限切れ確認する」で、確認対象はbackup・期限切れ確です。manag・リストアのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視とし」を述べ、対象は容量監視 分散定義（managem・リストア）です。サーバで変更のB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・変更）です。Manaを照合のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・照合）です。backを期限切れ確という用語は「バックアップ版数と保存先を定めるコピー規則を期限切れ」を指し、期限切れ確認 受信操作（backup・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>backup copy group 期限切れ確認 受信操作</strong></p><p>検証目的: アーカイブ運用のbackup copy group 期限切れ確認 受信操作について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL063
画面・出力には ANR1550I が含まれ、backup copy group 期限切れ確認 受信操作の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL063 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL063
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0002"><h3>backup copy group 状態確認 文字変換</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「backup copy group 状態確認 文字変換」は、バックアップ版数と保存先を定めるコピー規則を状態確認の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR023Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> backup copy group 状態確認 文字変換の設定や表示を読む前に役割を確認します。ポリシードメイン Policy Domain 変更前の確認 DOM02ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはPolicy Domainで変更前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。</li><li>B. 状態を読み取るための働きはStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 状態を読み取るための働きはAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 状態を読み取るための働きはバックアップ版数と保存先を定めるコピー規則である。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 状態確認・backupでDの記述「バックアップ版数と保存先を定めるコピー規則である」に対応する項目は状態確認 文字変換（backup・状態確認）です。状態・文字変に関するアーカイブ運用の仕様は「バックアップ版数と保存先を定めるコピー規則」で、確認対象はbackup・状態確認です。変更確認・PolicyのA:は「Policy Domainで変更前の確認ではポリシードメインの」を述べ、対象は変更前の確認 DOM02（Policy・変更確認）です。復旧・StorageのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・復旧）です。確認・AssociatのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・確認）です。「backup copy group」は「バックアップ版数と保存先を定めるコピー規則」を指す用語で、状態確認 文字変換（backup・状態確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>backup copy group 状態確認 文字変換</strong></p><p>検証目的: アーカイブ運用のbackup copy group 状態確認 文字変換について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL023
画面・出力には ANR1550I が含まれ、backup copy group 状態確認 文字変換の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL023 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL023
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0003"><h3>expiration 宛先照合 ノード割当</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「expiration 宛先照合 ノード割当」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を宛先照合の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL047を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> expiration 宛先照合 ノード割当の設定や表示を読む前に役割を確認します。ポリシードメイン Policy Domain 権限境界の確認 DOM12ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きは保存期間を過ぎた版やアーカイブを期限切れにする処理である。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはPolicy Domainで権限境界の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>C. 状態を読み取るための働きはStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 状態を読み取るための働きはNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 宛先照合・expiratiでAの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理である」に対応する項目は宛先照合 ノード割当（expirat・宛先照合）です。宛先・ノードに関するアーカイブ運用の仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理」で、確認対象はexpirat・宛先照合です。権限境界確・PolicyのB:は「Policy Domainで権限境界の確認ではポリシードメインの」を述べ、対象は権限境界の確認 DOM12（Policy・権限境界）です。移行・StartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・移行）です。確認・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。「expiration」は「保存期間を過ぎた版やアーカイブを期限切れにする処理」を指す用語で、宛先照合 ノード割当（expirat・宛先照合）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>expiration 宛先照合 ノード割当</strong></p><p>検証目的: アーカイブ運用のexpiration 宛先照合 ノード割当について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL047
画面・出力には ANR1550I が含まれ、expiration 宛先照合 ノード割当の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL047 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL047
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0004"><h3>expiration 容量監視 詳細表示</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「expiration 容量監視 詳細表示」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を容量監視の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL007を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> expiration 容量監視 詳細表示の設定や表示を読む前に役割を確認します。policy domain 期限切れ確認 容量表示ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的は保存期間を過ぎた版やアーカイブを期限切れにする処理を容量監視として確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を期限切れ確認する。</li><li>C. 一次資料が示す主目的はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 詳細表示・expiratiでAの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理を容量監視として確」に対応する項目は容量監視 詳細表示（expirat・詳細表示）です。容量監・詳細に関するアーカイブ運用の仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理を容量監視として確」で、確認対象はexpirat・詳細表示です。容量表示・policyのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」を述べ、対象は期限切れ確認 容量表示（policy・容量表示）です。巡回・ActionのC:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・巡回）です。収集・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・収集）です。「expiration」は「保存期間を過ぎた版やアーカイブを期限切れにする処理を」を指す用語で、容量監視 詳細表示（expirat・詳細表示）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>expiration 容量監視 詳細表示</strong></p><p>検証目的: アーカイブ運用のexpiration 容量監視 詳細表示について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL007
画面・出力には ANR1550I が含まれ、expiration 容量監視 詳細表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL007 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL007
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0005"><h3>policy domain 保存期間確認 遅延表示</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「policy domain 保存期間確認 遅延表示」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位を保存期間確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE031を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> policy domain 保存期間確認 遅延表示の設定や表示を読む前に役割を確認します。管理クラス Management Class 権限境界の確認 MC12ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はクライアントに適用するバックアップとアーカイブの規則を束ねる単位である。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。</li><li>C. 一次資料が示す主目的はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 遅延表示・policyでAの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位であ」に対応する項目は保存期間確認 遅延表示（policy・遅延表示）です。保存期・遅延に関するアーカイブ運用の仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」で、確認対象はpolicy・遅延表示です。権限境界確・ManagemeのB:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。巡回・DIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・巡回）です。確認・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・確認）です。「policy domain」は「クライアントに適用するバックアップとアーカイブの規則」を指す用語で、保存期間確認 遅延表示（policy・遅延表示）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>policy domain 保存期間確認 遅延表示</strong></p><p>検証目的: アーカイブ運用のpolicy domain 保存期間確認 遅延表示について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL031
画面・出力には ANR1550I が含まれ、policy domain 保存期間確認 遅延表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL031 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL031
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0006"><h3>policy domain 復元前確認 統合管理</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「policy domain 復元前確認 統合管理」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE071を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> policy domain 復元前確認 統合管理の設定や表示を読む前に役割を確認します。コピーグループ Backup and Archive Copy Groupではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはBackup andで変更後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。</li><li>B. 状態を読み取るための働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 状態を読み取るための働きはCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 状態を読み取るための働きはクライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復元前で復元前確認でDの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」に対応する項目は復元前確認 統合管理（policy・復元前確）です。復元前・統合に関するアーカイブ運用の仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」で、確認対象はpolicy・復元前確認です。Backu・変更確認のA:は「Backup andで変更後の確認ではコピーグループの」を述べ、対象は変更後の確認 CG03（Backup・変更確認）です。ポリシで診断のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断）です。計画時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・計画）です。poliを復元前確認という用語は「クライアントに適用するバックアップとアーカイブの規則」を指し、復元前確認 統合管理（policy・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>policy domain 復元前確認 統合管理</strong></p><p>検証目的: アーカイブ運用のpolicy domain 復元前確認 統合管理について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL071
画面・出力には ANR1550I が含まれ、policy domain 復元前確認 統合管理の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL071 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL071
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0007"><h3>schedule 保存期間確認 レビュー結果</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「schedule 保存期間確認 レビュー結果」は、バックアップや管理コマンドを決めた時刻に実行する定義を保存期間確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 039を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> schedule 保存期間確認 レビュー結果の設定や表示を読む前に役割を確認します。コピーグループ Backup and Archive Copy Groupではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはBackup andで復旧準備ではコピーグループの アーカイブグループからRetainVersionを読みである。</li><li>B. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 対象資源に対する働きはバックアップや管理コマンドを決めた時刻に実行する定義である。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保存期間確・scheduleでCの記述「バックアップや管理コマンドを決めた時刻に実行する定義である」に対応する項目は保存期間確認 レビュー結果（schedul・保存期間）です。保存期・レビュに関するアーカイブ運用の仕様は「バックアップや管理コマンドを決めた時刻に実行する定義」で、確認対象はschedul・保存期間確です。復旧準備・BackupのA:は「Backup andで復旧準備ではコピーグループの」を述べ、対象は復旧準備 CG05（Backup・復旧準備）です。変更・StartのB:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・変更）です。照合・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・照合）です。「schedule」は「バックアップや管理コマンドを決めた時刻に実行する定義」を指す用語で、保存期間確認 レビュー結果（schedul・保存期間）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>schedule 保存期間確認 レビュー結果</strong></p><p>検証目的: アーカイブ運用のschedule 保存期間確認 レビュー結果について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL039
画面・出力には ANR1550I が含まれ、schedule 保存期間確認 レビュー結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL039 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL039
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0008"><h3>schedule 復元前確認 時刻合わせ</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「schedule 復元前確認 時刻合わせ」は、バックアップや管理コマンドを決めた時刻に実行する定義を復元前確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 079を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> schedule 復元前確認 時刻合わせの設定や表示を読む前に役割を確認します。ストレージプール Directory-container Storage Poolではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はバックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はDirectory-containeで変更前の確認ではストレージプールのである。</li><li>C. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復元前で復元前確認でAの記述「バックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する」に対応する項目は復元前確認 時刻合わせ（schedul・復元前確）です。復元前・時刻合に関するアーカイブ運用の仕様は「バックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する」で、確認対象はschedul・復元前確認です。ストレで変更確認のB:は「Directory-containeで変更前の確認ではストレージプー」を述べ、対象は変更前の確認 POOL02（Directo・変更確認）です。変更時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・変更）です。Manaを保護のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・保護）です。scheを復元前確認という用語は「バックアップや管理コマンドを決めた時刻に実行する定義」を指し、復元前確認 時刻合わせ（schedul・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>schedule 復元前確認 時刻合わせ</strong></p><p>検証目的: アーカイブ運用のschedule 復元前確認 時刻合わせについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL079
画面・出力には ANR1550I が含まれ、schedule 復元前確認 時刻合わせの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL079 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL079
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0009"><h3>storage pool コマンド証跡 接続状態</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「storage pool コマンド証跡 接続状態」は、バックアップやアーカイブのデータを格納するサーバー側領域をコマンド証跡の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 015を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> storage pool コマンド証跡 接続状態の設定や表示を読む前に役割を確認します。archive copy group 宛先照合 伝搬経路ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはアーカイブコピーの保存期間と宛先を定めるコピー規則である。</li><li>B. 対象資源に対する働きはEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>C. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>D. 対象資源に対する働きはバックアップやアーカイブのデータを格納するサーバー側領域をコマンド証跡として確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> アーカイブ・storageでDの記述「バックアップやアーカイブのデータを格納するサーバー側領域をコマンド証」に対応する項目はコマンド証跡 接続状態（storage・アーカイ）です。コマン・接続状に関するアーカイブ運用の仕様は「バックアップやアーカイブのデータを格納するサーバー側領域をコマンド証」で、確認対象はstorage・アーカイブです。宛先照合・archiveのA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は宛先照合 伝搬経路（archive・宛先照合）です。巡回・EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・巡回）です。確認・ServerのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・確認）です。「storage pool」は「バックアップやアーカイブのデータを格納するサーバー側」を指す用語で、コマンド証跡 接続状態（storage・アーカイ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>storage pool コマンド証跡 接続状態</strong></p><p>検証目的: アーカイブ運用のstorage pool コマンド証跡 接続状態について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL015
画面・出力には ANR1550I が含まれ、storage pool コマンド証跡 接続状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL015 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL015
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0010"><h3>storage pool ノード割当確認 接続認証</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の アーカイブ運用 で扱う「storage pool ノード割当確認 接続認証」は、バックアップやアーカイブのデータを格納するサーバー側領域をノード割当確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 055を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> storage pool ノード割当確認 接続認証の設定や表示を読む前に役割を確認します。管理クラス Management Class 性能影響の確認 MC11ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はManagement Classで性能影響の確認では管理クラスのである。</li><li>B. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 一次資料が示す主目的はバックアップやアーカイブのデータを格納するサーバー側領域をノード割当確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ノードでノード割当でCの記述「バックアップやアーカイブのデータを格納するサーバー側領域をノード割当」に対応する項目はノード割当確認 接続認証（storage・ノード割）です。ノード・接続認に関するアーカイブ運用の仕様は「バックアップやアーカイブのデータを格納するサーバー側領域をノード割当」で、確認対象はstorage・ノード割当です。Manag・性能影響確のA:は「Management Classで性能影響の確認では管理クラスの」を述べ、対象は性能影響の確認 MC11（Managem・性能影響）です。クライで棚卸のB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・棚卸）です。Nodeを保護のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・保護）です。storをノード割当という用語は「バックアップやアーカイブのデータを格納するサーバー側」を指し、ノード割当確認 接続認証（storage・ノード割）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>storage pool ノード割当確認 接続認証</strong></p><p>検証目的: アーカイブ運用のstorage pool ノード割当確認 接続認証について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、アーカイブ運用の対象へ進みます。
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
Destination Pool POOL055
画面・出力には ANR1550I が含まれ、storage pool ノード割当確認 接続認証の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL055 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL055
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0011"><h3>アーカイブ運用 Archive Operation ログとの照合 ARC07</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>ログとの照合では アーカイブ運用 の アーカイブ実行 を主操作として ARC07 を判定します。時刻と対象識別子への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC07 に残します。ログとの照合を補助する アーカイブ照会 では ArchiveDate を補助値として ARC07 へ保存します。主判定のログとの照合ではアーカイブ運用の アーカイブ実行 から MONTH_END を読み ARC07 へ残します。証跡照合のログとの照合ではアーカイブ運用の MONTH_END と ArchiveDate を ARC07 に保存します。記録対応のログとの照合ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「アーカイブ運用 Archive Operation ログとの照合 ARC07」を「複製・保護 Storage Pool Protection and Node」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はStorage Poolで復旧後の確認では複製・保護の 検証からANR3730Iを読み・復旧確認に使うである。</li><li>B. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 保守作業で参照する機能はArchive Operationでログとの照合ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ログとの対象ArchiでCの記述「Archive Operationでログとの照合ではアーカイブ運用の」に対応する項目はログとの照合 ARC07（Archive・ログとの）です。アーカ・ログとに関するアーカイブ運用の仕様は「Archive Operationでログとの照合ではアーカイブ運用の」で、確認対象はArchive・ログとの照です。Stora・復旧確認のA:は「Storage Poolで復旧後の確認では複製・保護の」を述べ、対象は復旧後の確認 REPL06（Storage・復旧確認）です。保守対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保守）です。Assoを解除のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・解除）です。Archをログとの照という用語は「Archive Operationでログとの照合では」を指し、ログとの照合 ARC07（Archive・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation ログとの照合 ARC07</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて操作とログを対応し、ARC07のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC07のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC07のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC07のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Archiving が画面・出力に表示されること
② ステップ2 の Size が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0012"><h3>アーカイブ運用 Archive Operation 代替経路の確認 ARC10</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>代替経路の確認では アーカイブ運用 の アーカイブ実行 を主操作として ARC10 を判定します。主経路との役割差への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC10 に残します。代替経路の確認を補助する アーカイブ照会 では ArchiveDate を補助値として ARC10 へ保存します。主判定の代替経路の確認ではアーカイブ運用の アーカイブ実行 から MONTH_END を読み ARC10 へ残します。証跡照合の代替経路の確認ではアーカイブ運用の MONTH_END と ArchiveDate を ARC10 に保存します。記録対応の代替経路の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 代替経路の確認 ARC10の技術的な意味を資料で確認するとき、複製・保護 Storage Pool Protection and Nodeとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はArchive Operationで代替経路の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はStorage Poolで性能影響の確認では複製・保護の 複製状態からTargetServerを読みである。</li><li>C. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>D. 管理対象との関係を表す説明はアーカイブコピーの保存期間と宛先を定めるコピー規則をコマンド証跡として確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 代替経路対象ArchiでAの記述「Archive Operationで代替経路の確認ではアーカイブ運用」に対応する項目は代替経路の確認 ARC10（Archive・代替経路）です。アーカ・代替経に関するアーカイブ運用の仕様は「Archive Operationで代替経路の確認ではアーカイブ運用」で、確認対象はArchive・代替経路確です。性能影響対象StoraのB:は「Storage Poolで性能影響の確認では複製・保護の」を述べ、対象は性能影響の確認 REPL11（Storage・性能影響）です。登録時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。archをストレージのD:は「アーカイブコピーの保存期間と宛先を定めるコピー規則をコマンド証跡とし」を述べ、対象はコマンド証跡 回収対象（archive・ストレー）です。Archを代替経路確という用語は「Archive Operationで代替経路の確認で」を指し、代替経路の確認 ARC10（Archive・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 代替経路の確認 ARC10</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて代替手段の成立を確認し、ARC10のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC10のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC10のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC10のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Archiving が画面・出力に表示されること
② ステップ2 の Size が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0013"><h3>アーカイブ運用 Archive Operation 依存関係の確認 ARC13</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>依存関係の確認では アーカイブ運用 の アーカイブ実行 を主操作として ARC13 を判定します。前提資源と後続処理の順序への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC13 に残します。依存関係の確認を補助する アーカイブ照会 では ArchiveDate を補助値として ARC13 へ保存します。主判定の依存関係の確認ではアーカイブ運用の アーカイブ実行 から MONTH_END を読み ARC13 へ残します。証跡照合の依存関係の確認ではアーカイブ運用の MONTH_END と ArchiveDate を ARC13 に保存します。記録対応の依存関係の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 依存関係の確認 ARC13の設定や表示を読む前に役割を確認します。サーバー日次運用 Storage Pool 0040ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>B. 対象資源に対する働きはArchive Operationで依存関係の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>D. 対象資源に対する働きはバックアップやアーカイブのデータを格納するサーバー側領域を復元前確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 依存関係対象ArchiでBの記述「Archive Operationで依存関係の確認ではアーカイブ運用」に対応する項目は依存関係の確認 ARC13（Archive・依存関係）です。アーカ・依存関に関するアーカイブ運用の仕様は「Archive Operationで依存関係の確認ではアーカイブ運用」で、確認対象はArchive・依存関係確です。Stora・復旧のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・復旧）です。登録時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。storを復元前確認のD:は「バックアップやアーカイブのデータを格納するサーバー側領域を復元前確認」を述べ、対象は復元前確認 取得間隔（storage・復元前確）です。Archを依存関係確という用語は「Archive Operationで依存関係の確認で」を指し、依存関係の確認 ARC13（Archive・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 依存関係の確認 ARC13</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて依存資源を点検し、ARC13のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC13のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC13のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC13のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Archiving が画面・出力に表示されること
② ステップ2 の Size が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0014"><h3>アーカイブ運用 Archive Operation 停止前の確認 ARC14</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>停止前の確認では アーカイブ運用 の アーカイブ照会 を主操作として ARC14 を判定します。処理中資源と未完了要求への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC14 に残します。停止前の確認を補助する コピーグループ では RetainVersion を補助値として ARC14 へ保存します。主判定の停止前の確認ではアーカイブ運用の アーカイブ照会 から ArchiveDate を読み ARC14 へ残します。証跡照合の停止前の確認ではアーカイブ運用の ArchiveDate と RetainVersion を ARC14 に保存します。記録対応の停止前の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 停止前の確認 ARC14を同一分類のサーバー日次運用 Node Name 0013と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. コマンドまたは機能の用途はCopy Groupのコピーグループと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. コマンドまたは機能の用途はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。</li><li>D. コマンドまたは機能の用途はArchive Operationで停止前の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 停止確認対象ArchiでDの記述「Archive Operationで停止前の確認ではアーカイブ運用の」に対応する項目は停止前の確認 ARC14（Archive・停止確認）です。アーカ・停止前に関するアーカイブ運用の仕様は「Archive Operationで停止前の確認ではアーカイブ運用の」で、確認対象はArchive・停止確認です。Node・巡回のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・巡回）です。確認対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・確認）です。ノード割時のpolicのC:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」を述べ、対象はノード割当確認 保持期間（policy・ノード割）です。Archを停止確認という用語は「Archive Operationで停止前の確認では」を指し、停止前の確認 ARC14（Archive・停止確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 停止前の確認 ARC14</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて安全な停止条件を確認し、ARC14のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC14のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC14のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC14のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Size が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Archiving が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0015"><h3>アーカイブ運用 Archive Operation 再始動後の確認 ARC15</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>再始動後の確認では アーカイブ運用 の コピーグループ を主操作として ARC15 を判定します。再開点と未処理データへの注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC15 に残します。再始動後の確認を補助する アーカイブ実行 では MONTH_END を補助値として ARC15 へ保存します。主判定の再始動後の確認ではアーカイブ運用の コピーグループ から RetainVersion を読み ARC15 へ残します。証跡照合の再始動後の確認ではアーカイブ運用の RetainVersion と MONTH_END を ARC15 に保存します。記録対応の再始動後の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「アーカイブ運用 Archive Operation 再始動後の確認 ARC15」を「リストア確認 Client Restore 性能影響の確認 RST11」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はClient Restoreで性能影響の確認ではリストア確認の 別名復元からrestoredを読みである。</li><li>B. 運用時に利用する技術的役割はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 運用時に利用する技術的役割はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 運用時に利用する技術的役割はArchive Operationで再始動後の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 再始動確対象ArchiでDの記述「Archive Operationで再始動後の確認ではアーカイブ運用」に対応する項目は再始動後の確認 ARC15（Archive・再始動確）です。アーカ・再始動に関するアーカイブ運用の仕様は「Archive Operationで再始動後の確認ではアーカイブ運用」で、確認対象はArchive・再始動確認です。Clien・性能影響確のA:は「Client Restoreで性能影響の確認ではリストア確認の」を述べ、対象は性能影響の確認 RST11（Client・性能影響）です。切替対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・切替）です。解除時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・解除）です。Archを再始動確認という用語は「Archive Operationで再始動後の確認で」を指し、再始動後の確認 ARC15（Archive・再始動確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 再始動後の確認 ARC15</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて再始動結果を検証し、ARC15のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC15のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC15のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC15のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Archiving が画面・出力に表示されること
③ ステップ3 の Size が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0016"><h3>アーカイブ運用 Archive Operation 変更前の確認 ARC02</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>変更前の確認では アーカイブ運用 の アーカイブ照会 を主操作として ARC02 を判定します。変更対象と非対象の境界への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC02 に残します。変更前の確認を補助する コピーグループ では RetainVersion を補助値として ARC02 へ保存します。主判定の変更前の確認ではアーカイブ運用の アーカイブ照会 から ArchiveDate を読み ARC02 へ残します。証跡照合の変更前の確認ではアーカイブ運用の ArchiveDate と RetainVersion を ARC02 に保存します。記録対応の変更前の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 変更前の確認 ARC02の技術的な意味を資料で確認するとき、アーカイブ運用 Archive Operation 性能影響の確認 ARC11との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はArchive Operationで性能影響の確認ではアーカイブ運用のである。</li><li>B. コマンドまたは機能の用途はArchive Operationで変更前の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認対象ArchiでBの記述「Archive Operationで変更前の確認ではアーカイブ運用の」に対応する項目は変更前の確認 ARC02（Archive・変更確認）です。アーカ・変更前に関するアーカイブ運用の仕様は「Archive Operationで変更前の確認ではアーカイブ運用の」で、確認対象はArchive・変更確認です。Archi・性能影響確のA:は「Archive Operationで性能影響の確認ではアーカイブ運用」を述べ、対象は性能影響の確認 ARC11（Archive・性能影響）です。収集時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・収集）です。Assoを承認のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・承認）です。Archを変更確認という用語は「Archive Operationで変更前の確認では」を指し、変更前の確認 ARC02（Archive・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 変更前の確認 ARC02</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて変更前の証跡を保存し、ARC02のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC02のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC02のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC02のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Size が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Archiving が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0017"><h3>アーカイブ運用 Archive Operation 変更後の確認 ARC03</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>変更後の確認では アーカイブ運用 の コピーグループ を主操作として ARC03 を判定します。反映値と残存値への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC03 に残します。変更後の確認を補助する アーカイブ実行 では MONTH_END を補助値として ARC03 へ保存します。主判定の変更後の確認ではアーカイブ運用の コピーグループ から RetainVersion を読み ARC03 へ残します。証跡照合の変更後の確認ではアーカイブ運用の RetainVersion と MONTH_END を ARC03 に保存します。記録対応の変更後の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 変更後の確認 ARC03を保守記録に説明する必要があります。ポリシーと管理クラス Management Class 0014と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はArchive Operationで変更後の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 運用時に利用する技術的役割はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>D. 運用時に利用する技術的役割はサーバーへ登録されたクライアントを表す管理単位を復元前確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認対象ArchiでAの記述「Archive Operationで変更後の確認ではアーカイブ運用の」に対応する項目は変更後の確認 ARC03（Archive・変更確認）です。アーカ・変更後に関するアーカイブ運用の仕様は「Archive Operationで変更後の確認ではアーカイブ運用の」で、確認対象はArchive・変更確認です。巡回対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・巡回）です。登録時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・登録）です。nodeを復元前確認のD:は「サーバーへ登録されたクライアントを表す管理単位を復元前確認する」を述べ、対象は復元前確認 応答行（node・復元前確）です。Archを変更確認という用語は「Archive Operationで変更後の確認では」を指し、変更後の確認 ARC03（Archive・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 変更後の確認 ARC03</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて変更結果を検証し、ARC03のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC03のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC03のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC03のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Archiving が画面・出力に表示されること
③ ステップ3 の Size が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0018"><h3>アーカイブ運用 Archive Operation 引継ぎ記録 ARC09</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>引継ぎ記録では アーカイブ運用 の コピーグループ を主操作として ARC09 を判定します。次担当者が追跡できる証跡への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC09 に残します。引継ぎ記録を補助する アーカイブ実行 では MONTH_END を補助値として ARC09 へ保存します。主判定の引継ぎ記録ではアーカイブ運用の コピーグループ から RetainVersion を読み ARC09 へ残します。証跡照合の引継ぎ記録ではアーカイブ運用の RetainVersion と MONTH_END を ARC09 に保存します。記録対応の引継ぎ記録ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 引継ぎ記録 ARC09について構成や状態を確認します。クライアントスケジュール Schedule Name 0024ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 状態を読み取るための働きはAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 状態を読み取るための働きはバックアップやアーカイブのデータを格納するサーバー側領域を復元前確認する。</li><li>D. 状態を読み取るための働きはArchive Operationで引継ぎ記録ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> アーカイ対象ArchiでDの記述「Archive Operationで引継ぎ記録ではアーカイブ運用ので」に対応する項目は引継ぎ記録 ARC09（Archive・アーカイ）です。アーカ・引継ぎに関するアーカイブ運用の仕様は「Archive Operationで引継ぎ記録ではアーカイブ運用の」で、確認対象はArchive・アーカイブです。Sched・棚卸のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・棚卸）です。登録対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・登録）です。復元前確時のstoraのC:は「バックアップやアーカイブのデータを格納するサーバー側領域を復元前確認」を述べ、対象は復元前確認 取得間隔（storage・復元前確）です。Archをアーカイブという用語は「Archive Operationで引継ぎ記録ではア」を指し、引継ぎ記録 ARC09（Archive・アーカイ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 引継ぎ記録 ARC09</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて再現可能な記録を作成し、ARC09のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC09のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC09のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC09のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Archiving が画面・出力に表示されること
③ ステップ3 の Size が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0019"><h3>アーカイブ運用 Archive Operation 復旧後の確認 ARC06</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>復旧後の確認では アーカイブ運用 の コピーグループ を主操作として ARC06 を判定します。再発していないことを示す値への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC06 に残します。復旧後の確認を補助する アーカイブ実行 では MONTH_END を補助値として ARC06 へ保存します。主判定の復旧後の確認ではアーカイブ運用の コピーグループ から RetainVersion を読み ARC06 へ残します。証跡照合の復旧後の確認ではアーカイブ運用の RetainVersion と MONTH_END を ARC06 に保存します。記録対応の復旧後の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 復旧後の確認 ARC06を同一分類のポリシーと管理クラス Copy Group 0011と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>B. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 構成を確認する際の意味はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を容量監視として確認する。</li><li>D. 構成を確認する際の意味はArchive Operationで復旧後の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧確認対象ArchiでDの記述「Archive Operationで復旧後の確認ではアーカイブ運用の」に対応する項目は復旧後の確認 ARC06（Archive・復旧確認）です。アーカ・復旧後に関するアーカイブ運用の仕様は「Archive Operationで復旧後の確認ではアーカイブ運用の」で、確認対象はArchive・復旧確認です。Copy・巡回のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・巡回）です。保守対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・保守）です。保護設定時のpolicのC:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を容」を述べ、対象は容量監視 保護設定（policy・保護設定）です。Archを復旧確認という用語は「Archive Operationで復旧後の確認では」を指し、復旧後の確認 ARC06（Archive・復旧確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 復旧後の確認 ARC06</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて復旧後の安定性を確認し、ARC06のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC06のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC06のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC06のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Archiving が画面・出力に表示されること
③ ステップ3 の Size が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0020"><h3>アーカイブ運用 Archive Operation 復旧準備 ARC05</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>復旧準備では アーカイブ運用 の アーカイブ照会 を主操作として ARC05 を判定します。再開前に必要な整合性への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC05 に残します。復旧準備を補助する コピーグループ では RetainVersion を補助値として ARC05 へ保存します。主判定の復旧準備ではアーカイブ運用の アーカイブ照会 から ArchiveDate を読み ARC05 へ残します。証跡照合の復旧準備ではアーカイブ運用の ArchiveDate と RetainVersion を ARC05 に保存します。記録対応の復旧準備ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 復旧準備 ARC05の設定や表示を読む前に役割を確認します。サーバーDB・DR Server Database Backup 停止前の確認ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。</li><li>B. 一次資料が示す主目的はArchive Operationで復旧準備ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>D. 一次資料が示す主目的はバックアップやアーカイブのデータを格納するサーバー側領域である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧準備対象ArchiでBの記述「Archive Operationで復旧準備ではアーカイブ運用のであ」に対応する項目は復旧準備 ARC05（Archive・復旧準備）です。アーカ・復旧準に関するアーカイブ運用の仕様は「Archive Operationで復旧準備ではアーカイブ運用の」で、確認対象はArchive・復旧準備です。停止確認対象停止前の確のA:は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」を述べ、対象は停止前の確認 DBBK14（DB・停止確認）です。収集時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・収集）です。storを状態確認のD:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は状態確認 スケジュール（storage・状態確認）です。Archを復旧準備という用語は「Archive Operationで復旧準備ではアー」を指し、復旧準備 ARC05（Archive・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 復旧準備 ARC05</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて復旧条件を確認し、ARC05のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC05のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC05のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC05のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Size が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Archiving が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0021"><h3>アーカイブ運用 Archive Operation 性能影響の確認 ARC11</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>性能影響の確認では アーカイブ運用 の アーカイブ照会 を主操作として ARC11 を判定します。処理時間と滞留箇所への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC11 に残します。性能影響の確認を補助する コピーグループ では RetainVersion を補助値として ARC11 へ保存します。主判定の性能影響の確認ではアーカイブ運用の アーカイブ照会 から ArchiveDate を読み ARC11 へ残します。証跡照合の性能影響の確認ではアーカイブ運用の ArchiveDate と RetainVersion を ARC11 に保存します。記録対応の性能影響の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 性能影響の確認 ARC11を保守記録に説明する必要があります。サーバー日次運用 Storage Pool 0010と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 仕様上の役割はArchive Operationで性能影響の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 性能影響対象ArchiでDの記述「Archive Operationで性能影響の確認ではアーカイブ運用」に対応する項目は性能影響の確認 ARC11（Archive・性能影響）です。アーカ・性能影に関するアーカイブ運用の仕様は「Archive Operationで性能影響の確認ではアーカイブ運用」で、確認対象はArchive・性能影響確です。Stora・巡回のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・巡回）です。確認対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・確認）です。解除時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・解除）です。Archを性能影響確という用語は「Archive Operationで性能影響の確認で」を指し、性能影響の確認 ARC11（Archive・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 性能影響の確認 ARC11</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて負荷と待ちを確認し、ARC11のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC11のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC11のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC11のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Size が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Archiving が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0022"><h3>アーカイブ運用 Archive Operation 構成監査 ARC08</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>構成監査では アーカイブ運用 の アーカイブ照会 を主操作として ARC08 を判定します。定義値と稼働値の一致への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC08 に残します。構成監査を補助する コピーグループ では RetainVersion を補助値として ARC08 へ保存します。主判定の構成監査ではアーカイブ運用の アーカイブ照会 から ArchiveDate を読み ARC08 へ残します。証跡照合の構成監査ではアーカイブ運用の ArchiveDate と RetainVersion を ARC08 に保存します。記録対応の構成監査ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 構成監査 ARC08の役割を調べています。サーバーDB・DR Server Database Backup 通常状態の確認の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はDBで通常状態の確認ではサーバーの DB状態からLastDatabaseを読み・通常状態確認に使うである。</li><li>B. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 障害切り分けに用いる役割はファイルのバックアップ先や保存期間を決めるポリシー要素である。</li><li>D. 障害切り分けに用いる役割はArchive Operationで構成監査ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構成監査対象ArchiでDの記述「Archive Operationで構成監査ではアーカイブ運用のであ」に対応する項目は構成監査 ARC08（Archive・構成監査）です。アーカ・構成監に関するアーカイブ運用の仕様は「Archive Operationで構成監査ではアーカイブ運用の」で、確認対象はArchive・構成監査です。通常状態対象通常状態ののA:は「DBで通常状態の確認ではサーバーの DB状態からLastDataba」を述べ、対象は通常状態の確認 DBBK01（DB・通常状態）です。確認対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。宛先照合時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は宛先照合 初期同期（managem・宛先照合）です。Archを構成監査という用語は「Archive Operationで構成監査ではアー」を指し、構成監査 ARC08（Archive・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 構成監査 ARC08</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて構成差分を監査し、ARC08のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC08のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC08のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC08のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Size が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Archiving が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0023"><h3>アーカイブ運用 Archive Operation 権限境界の確認 ARC12</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>権限境界の確認では アーカイブ運用 の コピーグループ を主操作として ARC12 を判定します。参照操作と変更操作の分離への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC12 に残します。権限境界の確認を補助する アーカイブ実行 では MONTH_END を補助値として ARC12 へ保存します。主判定の権限境界の確認ではアーカイブ運用の コピーグループ から RetainVersion を読み ARC12 へ残します。証跡照合の権限境界の確認ではアーカイブ運用の RetainVersion と MONTH_END を ARC12 に保存します。記録対応の権限境界の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 権限境界の確認 ARC12に関する障害切り分けの前提を確認しています。サーバー日次運用 Server Name 0001の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 機能の説明としてはAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 機能の説明としてはファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。</li><li>D. 機能の説明としてはArchive Operationで権限境界の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 権限境界対象ArchiでDの記述「Archive Operationで権限境界の確認ではアーカイブ運用」に対応する項目は権限境界の確認 ARC12（Archive・権限境界）です。アーカ・権限境に関するアーカイブ運用の仕様は「Archive Operationで権限境界の確認ではアーカイブ運用」で、確認対象はArchive・権限境界確です。Serve・巡回のA:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・巡回）です。切替対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・切替）です。復元前確時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」を述べ、対象は復元前確認 期限切れ（managem・復元前確）です。Archを権限境界確という用語は「Archive Operationで権限境界の確認で」を指し、権限境界の確認 ARC12（Archive・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 権限境界の確認 ARC12</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて実行権限を点検し、ARC12のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC12のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC12のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC12のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Archiving が画面・出力に表示されること
③ ステップ3 の Size が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0024"><h3>アーカイブ運用 Archive Operation 通常状態の確認 ARC01</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>通常状態の確認では アーカイブ運用 の アーカイブ実行 を主操作として ARC01 を判定します。基準値と現在値の差への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC01 に残します。通常状態の確認を補助する アーカイブ照会 では ArchiveDate を補助値として ARC01 へ保存します。主判定の通常状態の確認ではアーカイブ運用の アーカイブ実行 から MONTH_END を読み ARC01 へ残します。証跡照合の通常状態の確認ではアーカイブ運用の MONTH_END と ArchiveDate を ARC01 に保存します。記録対応の通常状態の確認ではアーカイブ運用の DescriptionとExpiration の証跡へ ARC01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 通常状態の確認 ARC01について構成や状態を確認します。アーカイブ運用 Archive Operation 権限境界の確認 ARC12ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはArchive Operationで通常状態の確認ではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはArchive Operationで権限境界の確認ではアーカイブ運用のである。</li><li>C. 対象資源に対する働きはPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 対象資源に対する働きはサーバーへ登録されたクライアントを表す管理単位を容量監視として確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 通常状態対象ArchiでAの記述「Archive Operationで通常状態の確認ではアーカイブ運用」に対応する項目は通常状態の確認 ARC01（Archive・通常状態）です。アーカ・通常状に関するアーカイブ運用の仕様は「Archive Operationで通常状態の確認ではアーカイブ運用」で、確認対象はArchive・通常状態確です。権限境界対象ArchiのB:は「Archive Operationで権限境界の確認ではアーカイブ運用」を述べ、対象は権限境界の確認 ARC12（Archive・権限境界）です。登録時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・登録）です。nodeをストレージのD:は「サーバーへ登録されたクライアントを表す管理単位を容量監視として確認す」を述べ、対象は容量監視 例外記録（node・ストレー）です。Archを通常状態確という用語は「Archive Operationで通常状態の確認で」を指し、通常状態の確認 ARC01（Archive・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 通常状態の確認 ARC01</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて通常状態を確定し、ARC01のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC01のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC01のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC01のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Archiving が画面・出力に表示されること
② ステップ2 の Size が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0025"><h3>アーカイブ運用 Archive Operation 障害切り分け ARC04</h3><p class="kb-meta">分類: アーカイブ運用 ・ 難易度: 中級</p><p>障害切り分けでは アーカイブ運用 の アーカイブ実行 を主操作として ARC04 を判定します。最初に失敗した処理への注意として「バックアップデータをアーカイブと誤認して保持期限を保証できない危険があります」を ARC04 に残します。障害切り分けを補助する アーカイブ照会 では ArchiveDate を補助値として ARC04 へ保存します。主判定の障害切り分けではアーカイブ運用の アーカイブ実行 から MONTH_END を読み ARC04 へ残します。証跡照合の障害切り分けではアーカイブ運用の MONTH_END と ArchiveDate を ARC04 に保存します。記録対応の障害切り分けではアーカイブ運用の DescriptionとExpiration の証跡へ ARC04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> アーカイブ運用 Archive Operation 障害切り分け ARC04に関する障害切り分けの前提を確認しています。アーカイブ運用 Archive Operation 停止前の確認 ARC14の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はArchive Operationで停止前の確認ではアーカイブ運用のである。</li><li>B. 表示や設定で扱う内容はArchive Operationで障害切り分けではアーカイブ運用のである。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 表示や設定で扱う内容はバックアップやアーカイブのデータを格納するサーバー側領域である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> アーカイ対象ArchiでBの記述「Archive Operationで障害切り分けではアーカイブ運用の」に対応する項目は障害切り分け ARC04（Archive・アーカイ）です。アーカ・障害切に関するアーカイブ運用の仕様は「Archive Operationで障害切り分けではアーカイブ運用の」で、確認対象はArchive・アーカイブです。Archi・停止確認のA:は「Archive Operationで停止前の確認ではアーカイブ運用の」を述べ、対象は停止前の確認 ARC14（Archive・停止確認）です。保守時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保守）です。storを状態確認のD:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は状態確認 スケジュール（storage・状態確認）です。Archをアーカイブという用語は「Archive Operationで障害切り分けでは」を指し、障害切り分け ARC04（Archive・アーカイ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アーカイブ運用 Archive Operation 障害切り分け ARC04</strong></p><p>検証目的: アーカイブ運用のArchive Operationについて障害範囲を限定し、ARC04のDescriptionとExpirationを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象ARC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc archive /app/report.dat -description=MONTH_ENDを指定し、ARC04のアーカイブ実行を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Archiving /app/report.dat
Archive description: MONTH_END
Successful archive: 1 file
画面・出力にあるArchivingを読み、DescriptionとExpirationと対象ARC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へdsmc query archive /app/report.dat -description=MONTH_ENDを指定し、ARC04のアーカイブ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; dsmc query archive /app/report.dat -description=MONTH_END
→ Enter を押す
［画面・出力］
Size Archive Date Time File -- 1048576 07/15/2026 13:40 /app/report.dat Description MONTH_END
画面・出力にあるSizeを読み、DescriptionとExpirationと対象ARC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のアーカイブ運用を確認する入力画面です。COMMAND入力口へQUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、ARC04のコピーグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP STANDARD ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive Retain Version: 365 Destination: ARCHPOOL
画面・出力にあるCopyを読み、DescriptionとExpirationと対象ARC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Archiving が画面・出力に表示されること
② ステップ2 の Size が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## コピーグループ


<section class="kb-item" id="c14-i0026"><h3>backup copy group 宛先照合 接続先</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「backup copy group 宛先照合 接続先」は、バックアップ版数と保存先を定めるコピー規則を宛先照合の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR003Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> backup copy group 宛先照合 接続先について構成や状態を確認します。reclamation 状態確認 承認待ちではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはストレージプール内の空き領域を回収する処理である。</li><li>B. 対象資源に対する働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 対象資源に対する働きはバックアップ版数と保存先を定めるコピー規則である。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 宛先照合・backupでCの記述「バックアップ版数と保存先を定めるコピー規則である」に対応する項目は宛先照合 接続先（backup・宛先照合）です。宛先・接続先に関するコピーグループの仕様は「バックアップ版数と保存先を定めるコピー規則」で、確認対象はbackup・宛先照合です。状態確認・reclamatのA:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は状態確認 承認待ち（reclama・状態確認）です。監査・PolicyのB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・監査）です。切替・ServerのD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・切替）です。「backup copy group」は「バックアップ版数と保存先を定めるコピー規則」を指す用語で、宛先照合 接続先（backup・宛先照合）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>backup copy group 宛先照合 接続先</strong></p><p>検証目的: コピーグループのbackup copy group 宛先照合 接続先について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL003
画面・出力には ANR1550I が含まれ、backup copy group 宛先照合 接続先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL003 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL003
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0027"><h3>backup copy group 容量監視 復元前提</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「backup copy group 容量監視 復元前提」は、バックアップ版数と保存先を定めるコピー規則を容量監視の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR043Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> backup copy group 容量監視 復元前提について構成や状態を確認します。ポリシードメイン Policy Domain 性能影響の確認 DOM11ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はPolicy Domainで性能影響の確認ではポリシードメインのである。</li><li>B. 一次資料が示す主目的はバックアップ版数と保存先を定めるコピー規則を容量監視として確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>D. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーグル・backupでBの記述「バックアップ版数と保存先を定めるコピー規則を容量監視として確認する」に対応する項目は容量監視 復元前提（backup・コピーグ）です。容量監・復元前に関するコピーグループの仕様は「バックアップ版数と保存先を定めるコピー規則を容量監視として確認する」で、確認対象はbackup・コピーグルです。性能影響確・PolicyのA:は「Policy Domainで性能影響の確認ではポリシードメインの」を述べ、対象は性能影響の確認 DOM11（Policy・性能影響）です。移行・NodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・移行）です。照合・EventのD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・照合）です。「backup copy group」は「バックアップ版数と保存先を定めるコピー規則を容量監視」を指す用語で、容量監視 復元前提（backup・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>backup copy group 容量監視 復元前提</strong></p><p>検証目的: コピーグループのbackup copy group 容量監視 復元前提について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL043
画面・出力には ANR1550I が含まれ、backup copy group 容量監視 復元前提の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL043 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL043
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0028"><h3>expiration 期限切れ確認 入力欄</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「expiration 期限切れ確認 入力欄」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL027を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> expiration 期限切れ確認 入力欄について構成や状態を確認します。storage pool 状態確認 スケジュールではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはバックアップやアーカイブのデータを格納するサーバー側領域である。</li><li>B. 対象資源に対する働きはDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 対象資源に対する働きは保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 期限切れ確・expiratiでCの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」に対応する項目は期限切れ確認 入力欄（expirat・期限切れ）です。期限切・入力欄に関するコピーグループの仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」で、確認対象はexpirat・期限切れ確です。状態確認・storageのA:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は状態確認 スケジュール（storage・状態確認）です。復旧・DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・復旧）です。照合・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・照合）です。「expiration」は「保存期間を過ぎた版やアーカイブを期限切れにする処理を」を指す用語で、期限切れ確認 入力欄（expirat・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>expiration 期限切れ確認 入力欄</strong></p><p>検証目的: コピーグループのexpiration 期限切れ確認 入力欄について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL027
画面・出力には ANR1550I が含まれ、expiration 期限切れ確認 入力欄の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL027 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL027
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0029"><h3>expiration 状態確認 外部連携</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「expiration 状態確認 外部連携」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を状態確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL067を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> expiration 状態確認 外部連携について構成や状態を確認します。管理クラス Management Class 変更後の確認 MC03ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はManagement Classで変更後の確認では管理クラスの オプション確認からDIRMCを読みである。</li><li>B. 一次資料が示す主目的はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 一次資料が示す主目的は保存期間を過ぎた版やアーカイブを期限切れにする処理である。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 状態で状態確認でCの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理である」に対応する項目は状態確認 外部連携（expirat・状態確認）です。状態・外部連に関するコピーグループの仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理」で、確認対象はexpirat・状態確認です。Manag・変更確認のA:は「Management Classで変更後の確認では管理クラスの」を述べ、対象は変更後の確認 MC03（Managem・変更確認）です。ポリシで移行のB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・移行）です。Evenを保護のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・保護）です。expiを状態確認という用語は「保存期間を過ぎた版やアーカイブを期限切れにする処理」を指し、状態確認 外部連携（expirat・状態確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>expiration 状態確認 外部連携</strong></p><p>検証目的: コピーグループのexpiration 状態確認 外部連携について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL067
画面・出力には ANR1550I が含まれ、expiration 状態確認 外部連携の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL067 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL067
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0030"><h3>policy domain コマンド証跡 重大度</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「policy domain コマンド証跡 重大度」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位をコマンド証跡の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE051を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> policy domain コマンド証跡 重大度について構成や状態を確認します。管理クラス Management Class 変更前の確認 MC02ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはManagement Classで変更前の確認では管理クラスの クライアント詳細からDefaultManagである。</li><li>B. 対象資源に対する働きはクライアントに適用するバックアップとアーカイブの規則を束ねる単位をコマンド証跡として確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 対象資源に対する働きはAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コマンでコピーグルでBの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をコ」に対応する項目はコマンド証跡 重大度（policy・コピーグ）です。コマン・重大度に関するコピーグループの仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をコ」で、確認対象はpolicy・コピーグルです。Manag・変更確認のA:は「Management Classで変更前の確認では管理クラスの」を述べ、対象は変更前の確認 MC02（Managem・変更確認）です。監査時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・監査）です。Assoを照合のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。poliをコピーグルという用語は「クライアントに適用するバックアップとアーカイブの規則」を指し、コマンド証跡 重大度（policy・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>policy domain コマンド証跡 重大度</strong></p><p>検証目的: コピーグループのpolicy domain コマンド証跡 重大度について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL051
画面・出力には ANR1550I が含まれ、policy domain コマンド証跡 重大度の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL051 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL051
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0031"><h3>policy domain ノード割当確認 保持期間</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 初級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「policy domain ノード割当確認 保持期間」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE011を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> policy domain ノード割当確認 保持期間について構成や状態を確認します。archive copy group 容量監視 実行結果ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはアーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確認する。</li><li>B. 状態を読み取るための働きはクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 状態を読み取るための働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> ノード割当・policyでBの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」に対応する項目はノード割当確認 保持期間（policy・ノード割）です。ノード・保持期に関するコピーグループの仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」で、確認対象はpolicy・ノード割当です。バックアッ・archiveのA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確」を述べ、対象は容量監視 実行結果（archive・バックア）です。復旧・ManagemeのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・復旧）です。確認・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・確認）です。「policy domain」は「クライアントに適用するバックアップとアーカイブの規則」を指す用語で、ノード割当確認 保持期間（policy・ノード割）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>policy domain ノード割当確認 保持期間</strong></p><p>検証目的: コピーグループのpolicy domain ノード割当確認 保持期間について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL011
画面・出力には ANR1550I が含まれ、policy domain ノード割当確認 保持期間の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL011 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL011
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0032"><h3>schedule コマンド証跡 詳細タブ</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「schedule コマンド証跡 詳細タブ」は、バックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 059を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> schedule コマンド証跡 詳細タブについて構成や状態を確認します。activity log ノード割当確認 セッション上限ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはサーバー操作とメッセージを追跡するログをノード割当確認する。</li><li>B. 状態を読み取るための働きはStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 状態を読み取るための働きはバックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡として確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コマンでコピーグルでCの記述「バックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡と」に対応する項目はコマンド証跡 詳細タブ（schedul・コピーグ）です。コマン・詳細タに関するコピーグループの仕様は「バックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡と」で、確認対象はschedul・コピーグルです。activ・ノード割当のA:は「サーバー操作とメッセージを追跡するログをノード割当確認する」を述べ、対象はノード割当確認 セッション上限（activit・ノード割）です。サーバで移行のB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・移行）です。Actiを解析のD:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・解析）です。scheをコピーグルという用語は「バックアップや管理コマンドを決めた時刻に実行する定義」を指し、コマンド証跡 詳細タブ（schedul・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>schedule コマンド証跡 詳細タブ</strong></p><p>検証目的: コピーグループのschedule コマンド証跡 詳細タブについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL059
画面・出力には ANR1550I が含まれ、schedule コマンド証跡 詳細タブの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL059 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL059
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0033"><h3>schedule ノード割当確認 変換規則</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「schedule ノード割当確認 変換規則」は、バックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 019を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> schedule ノード割当確認 変換規則について構成や状態を確認します。management class 宛先照合 初期同期ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はバックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はファイルのバックアップ先や保存期間を決めるポリシー要素である。</li><li>C. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>D. 一次資料が示す主目的はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> ノード割当・scheduleでAの記述「バックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認」に対応する項目はノード割当確認 変換規則（schedul・ノード割）です。ノード・変換規に関するコピーグループの仕様は「バックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認」で、確認対象はschedul・ノード割当です。宛先照合・managemeのB:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は宛先照合 初期同期（managem・宛先照合）です。復旧・NodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。登録・DatabaseのD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。「schedule」は「バックアップや管理コマンドを決めた時刻に実行する定義」を指す用語で、ノード割当確認 変換規則（schedul・ノード割）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>schedule ノード割当確認 変換規則</strong></p><p>検証目的: コピーグループのschedule ノード割当確認 変換規則について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL019
画面・出力には ANR1550I が含まれ、schedule ノード割当確認 変換規則の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL019 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL019
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0034"><h3>storage pool 保存期間確認 検査エンジン</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 上級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「storage pool 保存期間確認 検査エンジン」は、バックアップやアーカイブのデータを格納するサーバー側領域を保存期間確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 075を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> storage pool 保存期間確認 検査エンジンについて構成や状態を確認します。コピーグループ Backup and Archive Copy Groupではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはBackup andで再始動後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。</li><li>B. 対象資源に対する働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 対象資源に対する働きはバックアップやアーカイブのデータを格納するサーバー側領域である。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 保存期で保存期間確でCの記述「バックアップやアーカイブのデータを格納するサーバー側領域である」に対応する項目は保存期間確認 検査エンジン（storage・保存期間）です。保存期・検査エに関するコピーグループの仕様は「バックアップやアーカイブのデータを格納するサーバー側領域」で、確認対象はstorage・保存期間確です。Backu・再始動確認のA:は「Backup andで再始動後の確認ではコピーグループの」を述べ、対象は再始動後の確認 CG15（Backup・再始動確）です。ポリシで復旧のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・復旧）です。Nodeを確認のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。storを保存期間確という用語は「バックアップやアーカイブのデータを格納するサーバー側」を指し、保存期間確認 検査エンジン（storage・保存期間）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>storage pool 保存期間確認 検査エンジン</strong></p><p>検証目的: コピーグループのstorage pool 保存期間確認 検査エンジンについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL075
画面・出力には ANR1550I が含まれ、storage pool 保存期間確認 検査エンジンの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL075 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL075
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0035"><h3>storage pool 復元前確認 取得間隔</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>IBM Spectrum Protect 8.1 の コピーグループ で扱う「storage pool 復元前確認 取得間隔」は、バックアップやアーカイブのデータを格納するサーバー側領域を復元前確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 035を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> storage pool 復元前確認 取得間隔について構成や状態を確認します。backup copy group 保存期間確認 ルール読替ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはバックアップ版数と保存先を定めるコピー規則である。</li><li>B. 状態を読み取るための働きはDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 状態を読み取るための働きはバックアップやアーカイブのデータを格納するサーバー側領域を復元前確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復元前確認・storageでCの記述「バックアップやアーカイブのデータを格納するサーバー側領域を復元前確認」に対応する項目は復元前確認 取得間隔（storage・復元前確）です。復元前・取得間に関するコピーグループの仕様は「バックアップやアーカイブのデータを格納するサーバー側領域を復元前確認」で、確認対象はstorage・復元前確認です。保存期間確・backupのA:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は保存期間確認 ルール読替（backup・保存期間）です。棚卸・DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・棚卸）です。確認・AssociatのD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・確認）です。「storage pool」は「バックアップやアーカイブのデータを格納するサーバー側」を指す用語で、復元前確認 取得間隔（storage・復元前確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>storage pool 復元前確認 取得間隔</strong></p><p>検証目的: コピーグループのstorage pool 復元前確認 取得間隔について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、コピーグループの対象へ進みます。
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
Destination Pool POOL035
画面・出力には ANR1550I が含まれ、storage pool 復元前確認 取得間隔の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY STGPOOL POOL035 FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Storage Pool Name POOL035
Device Class DISK
Estimated Capacity 100 G
Pct Util 42.0
画面・出力には Storage が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
② ステップ2 の ANR1550I が画面・出力に表示されること
③ ステップ3 の Storage が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands</p></div></details></section>


<section class="kb-item" id="c14-i0036"><h3>コピーグループ Backup and Archive Copy Group ログとの照合 CG07</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>ログとの照合では コピーグループ の コピーグループ照会 を主操作として CG07 を判定します。時刻と対象識別子への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG07 に残します。ログとの照合を補助する アーカイブグループ では RetainVersion を補助値として CG07 へ保存します。主判定のログとの照合ではコピーグループの コピーグループ照会 から VersionsData を読み CG07 へ残します。証跡照合のログとの照合ではコピーグループの VersionsData と RetainVersion を CG07 に保存します。記録対応のログとの照合ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group ログとの照合 CG07を保守記録に説明する必要があります。ストレージプール Directory-container Storage Poolと取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDirectory-containeで引継ぎ記録ではストレージプールのである。</li><li>B. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。ポリシーと管理クラス Management Class 0089固有の属性も確認対象に含める。</li><li>C. 保守作業で参照する機能はBackup andでログとの照合ではコピーグループの コピーグループ照会からVersionsDataを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーでログとの照でCの記述「Backup andでログとの照合ではコピーグループの」に対応する項目はログとの照合 CG07（Backup・ログとの）です。コピー・ログとに関するコピーグループの仕様は「Backup andでログとの照合ではコピーグループの」で、確認対象はBackup・ログとの照です。Direc・ストレージのA:は「Directory-containeで引継ぎ記録ではストレージプール」を述べ、対象は引継ぎ記録 POOL09（Directo・ストレー）です。ポリシで変更のB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・変更）です。Starを解析のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・解析）です。Backをログとの照という用語は「Backup andでログとの照合ではコピーグループ」を指し、ログとの照合 CG07（Backup・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group ログとの照合 CG07</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて操作とログを対応し、CG07のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG07 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG07のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG07 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG07 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG07のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG07 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG07 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG07の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG07 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Management が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0037"><h3>コピーグループ Backup and Archive Copy Group 代替経路の確認 CG10</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>代替経路の確認では コピーグループ の コピーグループ照会 を主操作として CG10 を判定します。主経路との役割差への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG10 に残します。代替経路の確認を補助する アーカイブグループ では RetainVersion を補助値として CG10 へ保存します。主判定の代替経路の確認ではコピーグループの コピーグループ照会 から VersionsData を読み CG10 へ残します。証跡照合の代替経路の確認ではコピーグループの VersionsData と RetainVersion を CG10 に保存します。記録対応の代替経路の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 代替経路の確認 CG10を同一分類のアーカイブ運用 Archive Operation 再始動後の確認 ARC15と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はBackup andで代替経路の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はArchive Operationで再始動後の確認ではアーカイブ運用のである。</li><li>C. 管理対象との関係を表す説明はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。クライアントスケジュール Action 0141固有の属性も確認対象に含める。</li><li>D. 管理対象との関係を表す説明はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで代替経路確でAの記述「Backup andで代替経路の確認ではコピーグループの」に対応する項目は代替経路の確認 CG10（Backup・代替経路）です。コピー・代替経に関するコピーグループの仕様は「Backup andで代替経路の確認ではコピーグループの」で、確認対象はBackup・代替経路確です。アーカで再始動確認のB:は「Archive Operationで再始動後の確認ではアーカイブ運用」を述べ、対象は再始動後の確認 ARC15（Archive・再始動確）です。保守時のActioのC:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・保守）です。Scheを解析のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・解析）です。Backを代替経路確という用語は「Backup andで代替経路の確認ではコピーグルー」を指し、代替経路の確認 CG10（Backup・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 代替経路の確認 CG10</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて代替手段の成立を確認し、CG10のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG10 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG10のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG10 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG10 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG10のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG10 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG10 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG10の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG10 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Management が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0038"><h3>コピーグループ Backup and Archive Copy Group 依存関係の確認 CG13</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>依存関係の確認では コピーグループ の コピーグループ照会 を主操作として CG13 を判定します。前提資源と後続処理の順序への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG13 に残します。依存関係の確認を補助する アーカイブグループ では RetainVersion を補助値として CG13 へ保存します。主判定の依存関係の確認ではコピーグループの コピーグループ照会 から VersionsData を読み CG13 へ残します。証跡照合の依存関係の確認ではコピーグループの VersionsData と RetainVersion を CG13 に保存します。記録対応の依存関係の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 依存関係の確認 CG13について構成や状態を確認します。コピーグループ Backup and Archive Copy Groupではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはBackup andで再始動後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。</li><li>B. 対象資源に対する働きはManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス Management Class 0134固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きはサーバーへ登録されたクライアントを表す管理単位である。</li><li>D. 対象資源に対する働きはBackup andで依存関係の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで依存関係確でDの記述「Backup andで依存関係の確認ではコピーグループの」に対応する項目は依存関係の確認 CG13（Backup・依存関係）です。コピー・依存関に関するコピーグループの仕様は「Backup andで依存関係の確認ではコピーグループの」で、確認対象はBackup・依存関係確です。Backu・再始動確認のA:は「Backup andで再始動後の確認ではコピーグループの」を述べ、対象は再始動後の確認 CG15（Backup・再始動確）です。ポリシで診断のB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・診断）です。状態確認時のnodeのC:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は状態確認 構成配布（node・状態確認）です。Backを依存関係確という用語は「Backup andで依存関係の確認ではコピーグルー」を指し、依存関係の確認 CG13（Backup・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 依存関係の確認 CG13</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて依存資源を点検し、CG13のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG13 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG13のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG13 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG13 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG13のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG13 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG13 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG13の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG13 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Management が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0039"><h3>コピーグループ Backup and Archive Copy Group 停止前の確認 CG14</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>停止前の確認では コピーグループ の アーカイブグループ を主操作として CG14 を判定します。処理中資源と未完了要求への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG14 に残します。停止前の確認を補助する 管理クラス対応 では BackupCopy を補助値として CG14 へ保存します。主判定の停止前の確認ではコピーグループの アーカイブグループ から RetainVersion を読み CG14 へ残します。証跡照合の停止前の確認ではコピーグループの RetainVersion と BackupCopy を CG14 に保存します。記録対応の停止前の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 停止前の確認 CG14の技術的な意味を資料で確認するとき、複製・保護 Storage Pool Protection and Nodeとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はBackup andで停止前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はStorage Poolで障害切り分けでは複製・保護の プール保護からANR0984Iを読み・複製である。</li><li>C. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. コマンドまたは機能の用途はバックアップ版数と保存先を定めるコピー規則である。backup copy group 状態確認 文字変換固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで停止確認でAの記述「Backup andで停止前の確認ではコピーグループの」に対応する項目は停止前の確認 CG14（Backup・停止確認）です。コピー・停止前に関するコピーグループの仕様は「Backup andで停止前の確認ではコピーグループの」で、確認対象はBackup・停止確認です。保護で複製・保護のB:は「Storage Poolで障害切り分けでは複製・保護の」を述べ、対象は障害切り分け REPL04（Storage・複製）です。保守時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・保守）です。backを状態確認のD:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は状態確認 文字変換（backup・状態確認）です。Backを停止確認という用語は「Backup andで停止前の確認ではコピーグループ」を指し、停止前の確認 CG14（Backup・停止確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 停止前の確認 CG14</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて安全な停止条件を確認し、CG14のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG14 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG14のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG14 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG14 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG14の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG14 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG14 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG14のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG14 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Management が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0040"><h3>コピーグループ Backup and Archive Copy Group 再始動後の確認 CG15</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>再始動後の確認では コピーグループ の 管理クラス対応 を主操作として CG15 を判定します。再開点と未処理データへの注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG15 に残します。再始動後の確認を補助する コピーグループ照会 では VersionsData を補助値として CG15 へ保存します。主判定の再始動後の確認ではコピーグループの 管理クラス対応 から BackupCopy を読み CG15 へ残します。証跡照合の再始動後の確認ではコピーグループの BackupCopy と VersionsData を CG15 に保存します。記録対応の再始動後の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 再始動後の確認 CG15を保守記録に説明する必要があります。リストア確認 Client Restore 変更後の確認 RST03と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はClient Restoreで変更後の確認ではリストア確認の 活動ログからRestoreを読みである。リストア確認 Client Restore 変更後の確認 RST03固有の属性も確認対象に含める。</li><li>B. 運用時に利用する技術的役割はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 運用時に利用する技術的役割はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 運用時に利用する技術的役割はBackup andで再始動後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで再始動確認でDの記述「Backup andで再始動後の確認ではコピーグループの」に対応する項目は再始動後の確認 CG15（Backup・再始動確）です。コピー・再始動に関するコピーグループの仕様は「Backup andで再始動後の確認ではコピーグループの」で、確認対象はBackup・再始動確認です。Clien・変更確認のA:は「Client Restoreで変更後の確認ではリストア確認の」を述べ、対象は変更後の確認 RST03（Client・変更確認）です。クライで切替のB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・切替）です。解除時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・解除）です。Backを再始動確認という用語は「Backup andで再始動後の確認ではコピーグルー」を指し、再始動後の確認 CG15（Backup・再始動確）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 再始動後の確認 CG15</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて再始動結果を検証し、CG15のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG15 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG15の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG15 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG15 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG15のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG15 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG15 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG15のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG15 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Management が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0041"><h3>コピーグループ Backup and Archive Copy Group 変更前の確認 CG02</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>変更前の確認では コピーグループ の アーカイブグループ を主操作として CG02 を判定します。変更対象と非対象の境界への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG02 に残します。変更前の確認を補助する 管理クラス対応 では BackupCopy を補助値として CG02 へ保存します。主判定の変更前の確認ではコピーグループの アーカイブグループ から RetainVersion を読み CG02 へ残します。証跡照合の変更前の確認ではコピーグループの RetainVersion と BackupCopy を CG02 に保存します。記録対応の変更前の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 変更前の確認 CG02を同一分類のストレージプール Directory-container Storage Poolと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はDirectory-containeで権限境界の確認ではストレージプールのである。ストレージプール Directory-container固有の属性も確認対象に含める。</li><li>B. コマンドまたは機能の用途はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. コマンドまたは機能の用途はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで変更確認でBの記述「Backup andで変更前の確認ではコピーグループの」に対応する項目は変更前の確認 CG02（Backup・変更確認）です。コピー・変更前に関するコピーグループの仕様は「Backup andで変更前の確認ではコピーグループの」で、確認対象はBackup・変更確認です。Direc・権限境界確のA:は「Directory-containeで権限境界の確認ではストレージプ」を述べ、対象は権限境界の確認 POOL12（Directo・権限境界）です。保守時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・保守）です。Evenを解除のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・解除）です。Backを変更確認という用語は「Backup andで変更前の確認ではコピーグループ」を指し、変更前の確認 CG02（Backup・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 変更前の確認 CG02</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて変更前の証跡を保存し、CG02のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG02 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG02のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG02 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG02 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG02の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG02 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG02 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG02のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG02 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Management が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0042"><h3>コピーグループ Backup and Archive Copy Group 変更後の確認 CG03</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>変更後の確認では コピーグループ の 管理クラス対応 を主操作として CG03 を判定します。反映値と残存値への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG03 に残します。変更後の確認を補助する コピーグループ照会 では VersionsData を補助値として CG03 へ保存します。主判定の変更後の確認ではコピーグループの 管理クラス対応 から BackupCopy を読み CG03 へ残します。証跡照合の変更後の確認ではコピーグループの BackupCopy と VersionsData を CG03 に保存します。記録対応の変更後の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「コピーグループ Backup and Archive Copy Group 変更後の確認 CG03」を「リストア確認 Client Restore 代替経路の確認 RST10」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はBackup andで変更後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はClient Restoreで代替経路の確認ではリストア確認の 候補照会からMgmtClassを読みである。</li><li>C. 運用時に利用する技術的役割はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 運用時に利用する技術的役割はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Start Time 0348固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで変更確認でAの記述「Backup andで変更後の確認ではコピーグループの」に対応する項目は変更後の確認 CG03（Backup・変更確認）です。コピー・変更後に関するコピーグループの仕様は「Backup andで変更後の確認ではコピーグループの」で、確認対象はBackup・変更確認です。リストで代替経路確のB:は「Client Restoreで代替経路の確認ではリストア確認の」を述べ、対象は代替経路の確認 RST10（Client・代替経路）です。保守時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・保守）です。Starを解除のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・解除）です。Backを変更確認という用語は「Backup andで変更後の確認ではコピーグループ」を指し、変更後の確認 CG03（Backup・変更確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 変更後の確認 CG03</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて変更結果を検証し、CG03のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG03 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG03の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG03 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG03 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG03のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG03 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG03 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG03のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG03 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Management が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0043"><h3>コピーグループ Backup and Archive Copy Group 引継ぎ記録 CG09</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>引継ぎ記録では コピーグループ の 管理クラス対応 を主操作として CG09 を判定します。次担当者が追跡できる証跡への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG09 に残します。引継ぎ記録を補助する コピーグループ照会 では VersionsData を補助値として CG09 へ保存します。主判定の引継ぎ記録ではコピーグループの 管理クラス対応 から BackupCopy を読み CG09 へ残します。証跡照合の引継ぎ記録ではコピーグループの BackupCopy と VersionsData を CG09 に保存します。記録対応の引継ぎ記録ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 引継ぎ記録 CG09の設定や表示を読む前に役割を確認します。バックアップ運用 Incremental Backup 構成監査 BKP08ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはIncremental Backupで構成監査ではバックアップ運用のである。</li><li>B. 状態を読み取るための働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 状態を読み取るための働きはBackup andで引継ぎ記録ではコピーグループの 管理クラス対応からBackupCopyを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。クライアントスケジュール Action 0306固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーでコピーグルでCの記述「Backup andで引継ぎ記録ではコピーグループの」に対応する項目は引継ぎ記録 CG09（Backup・コピーグ）です。コピー・引継ぎに関するコピーグループの仕様は「Backup andで引継ぎ記録ではコピーグループの」で、確認対象はBackup・コピーグルです。Incre・構成監査のA:は「Incremental Backupで構成監査ではバックアップ運用の」を述べ、対象は構成監査 BKP08（Increme・構成監査）です。サーバで診断のB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・診断）です。Actiを解析のD:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・解析）です。Backをコピーグルという用語は「Backup andで引継ぎ記録ではコピーグループの」を指し、引継ぎ記録 CG09（Backup・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 引継ぎ記録 CG09</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて再現可能な記録を作成し、CG09のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG09 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG09の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG09 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG09 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG09のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG09 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG09 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG09のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG09 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Management が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0044"><h3>コピーグループ Backup and Archive Copy Group 復旧後の確認 CG06</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>復旧後の確認では コピーグループ の 管理クラス対応 を主操作として CG06 を判定します。再発していないことを示す値への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG06 に残します。復旧後の確認を補助する コピーグループ照会 では VersionsData を補助値として CG06 へ保存します。主判定の復旧後の確認ではコピーグループの 管理クラス対応 から BackupCopy を読み CG06 へ残します。証跡照合の復旧後の確認ではコピーグループの BackupCopy と VersionsData を CG06 に保存します。記録対応の復旧後の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 復旧後の確認 CG06の技術的な意味を資料で確認するとき、コピーグループ Backup and Archive Copy Groupとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はBackup andで引継ぎ記録ではコピーグループの 管理クラス対応からBackupCopyを読みである。コピーグループ Backup and Archive Copy固有の属性も確認対象に含める。</li><li>B. 構成を確認する際の意味はBackup andで復旧後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 構成を確認する際の意味はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで復旧確認でBの記述「Backup andで復旧後の確認ではコピーグループの」に対応する項目は復旧後の確認 CG06（Backup・復旧確認）です。コピー・復旧後に関するコピーグループの仕様は「Backup andで復旧後の確認ではコピーグループの」で、確認対象はBackup・復旧確認です。Backu・コピーグルのA:は「Backup andで引継ぎ記録ではコピーグループの」を述べ、対象は引継ぎ記録 CG09（Backup・コピーグ）です。保守時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保守）です。Scheを計画のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・計画）です。Backを復旧確認という用語は「Backup andで復旧後の確認ではコピーグループ」を指し、復旧後の確認 CG06（Backup・復旧確認）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 復旧後の確認 CG06</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて復旧後の安定性を確認し、CG06のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG06 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG06の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG06 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG06 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG06のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG06 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG06 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG06のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG06 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Management が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0045"><h3>コピーグループ Backup and Archive Copy Group 復旧準備 CG05</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>復旧準備では コピーグループ の アーカイブグループ を主操作として CG05 を判定します。再開前に必要な整合性への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG05 に残します。復旧準備を補助する 管理クラス対応 では BackupCopy を補助値として CG05 へ保存します。主判定の復旧準備ではコピーグループの アーカイブグループ から RetainVersion を読み CG05 へ残します。証跡照合の復旧準備ではコピーグループの RetainVersion と BackupCopy を CG05 に保存します。記録対応の復旧準備ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 復旧準備 CG05について構成や状態を確認します。コピーグループ Backup and Archive Copy Groupではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はBackup andで依存関係の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。</li><li>B. 一次資料が示す主目的はBackup andで復旧準備ではコピーグループの アーカイブグループからRetainVersionを読みである。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 一次資料が示す主目的はバックアップ版数と保存先を定めるコピー規則である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで復旧準備でBの記述「Backup andで復旧準備ではコピーグループの」に対応する項目は復旧準備 CG05（Backup・復旧準備）です。コピー・復旧準に関するコピーグループの仕様は「Backup andで復旧準備ではコピーグループの」で、確認対象はBackup・復旧準備です。Backu・依存関係確のA:は「Backup andで依存関係の確認ではコピーグループの」を述べ、対象は依存関係の確認 CG13（Backup・依存関係）です。移行時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・移行）です。backを宛先照合のD:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は宛先照合 接続先（backup・宛先照合）です。Backを復旧準備という用語は「Backup andで復旧準備ではコピーグループの」を指し、復旧準備 CG05（Backup・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 復旧準備 CG05</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて復旧条件を確認し、CG05のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG05 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG05のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG05 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG05 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG05の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG05 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG05 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG05のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG05 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Management が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0046"><h3>コピーグループ Backup and Archive Copy Group 性能影響の確認 CG11</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>性能影響の確認では コピーグループ の アーカイブグループ を主操作として CG11 を判定します。処理時間と滞留箇所への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG11 に残します。性能影響の確認を補助する 管理クラス対応 では BackupCopy を補助値として CG11 へ保存します。主判定の性能影響の確認ではコピーグループの アーカイブグループ から RetainVersion を読み CG11 へ残します。証跡照合の性能影響の確認ではコピーグループの RetainVersion と BackupCopy を CG11 に保存します。記録対応の性能影響の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「コピーグループ Backup and Archive Copy Group 性能影響の確認 CG11」を「リストア確認 Client Restore 変更後の確認 RST03」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はClient Restoreで変更後の確認ではリストア確認の 活動ログからRestoreを読みである。リストア確認 Client Restore 変更後の確認 RST03固有の属性も確認対象に含める。</li><li>B. 仕様上の役割はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>C. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 仕様上の役割はBackup andで性能影響の確認ではコピーグループの アーカイブグループからRetainVersionをである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで性能影響確でDの記述「Backup andで性能影響の確認ではコピーグループの」に対応する項目は性能影響の確認 CG11（Backup・性能影響）です。コピー・性能影に関するコピーグループの仕様は「Backup andで性能影響の確認ではコピーグループの」で、確認対象はBackup・性能影響確です。Clien・変更確認のA:は「Client Restoreで変更後の確認ではリストア確認の」を述べ、対象は変更後の確認 RST03（Client・変更確認）です。クライで診断のB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・診断）です。解除時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・解除）です。Backを性能影響確という用語は「Backup andで性能影響の確認ではコピーグルー」を指し、性能影響の確認 CG11（Backup・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 性能影響の確認 CG11</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて負荷と待ちを確認し、CG11のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG11 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG11のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG11 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG11 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG11の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG11 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG11 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG11のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG11 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Management が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0047"><h3>コピーグループ Backup and Archive Copy Group 構成監査 CG08</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>構成監査では コピーグループ の アーカイブグループ を主操作として CG08 を判定します。定義値と稼働値の一致への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG08 に残します。構成監査を補助する 管理クラス対応 では BackupCopy を補助値として CG08 へ保存します。主判定の構成監査ではコピーグループの アーカイブグループ から RetainVersion を読み CG08 へ残します。証跡照合の構成監査ではコピーグループの RetainVersion と BackupCopy を CG08 に保存します。記録対応の構成監査ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 構成監査 CG08に関する障害切り分けの前提を確認しています。リストア確認 Client Restore 変更後の確認 RST03の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はClient Restoreで変更後の確認ではリストア確認の 活動ログからRestoreを読みである。</li><li>C. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。ポリシーと管理クラス Policy Set 0167固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで構成監査でAの記述「Backup andで構成監査ではコピーグループの」に対応する項目は構成監査 CG08（Backup・構成監査）です。コピー・構成監に関するコピーグループの仕様は「Backup andで構成監査ではコピーグループの」で、確認対象はBackup・構成監査です。リストで変更確認のB:は「Client Restoreで変更後の確認ではリストア確認の」を述べ、対象は変更後の確認 RST03（Client・変更確認）です。切替時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・切替）です。Evenを計画のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・計画）です。Backを構成監査という用語は「Backup andで構成監査ではコピーグループの」を指し、構成監査 CG08（Backup・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 構成監査 CG08</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて構成差分を監査し、CG08のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG08 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG08のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG08 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG08 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG08の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG08 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG08 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG08のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG08 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Management が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0048"><h3>コピーグループ Backup and Archive Copy Group 権限境界の確認 CG12</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>権限境界の確認では コピーグループ の 管理クラス対応 を主操作として CG12 を判定します。参照操作と変更操作の分離への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG12 に残します。権限境界の確認を補助する コピーグループ照会 では VersionsData を補助値として CG12 へ保存します。主判定の権限境界の確認ではコピーグループの 管理クラス対応 から BackupCopy を読み CG12 へ残します。証跡照合の権限境界の確認ではコピーグループの BackupCopy と VersionsData を CG12 に保存します。記録対応の権限境界の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 権限境界の確認 CG12の役割を調べています。バックアップ運用 Incremental Backup 権限境界の確認 BKP12の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはIncremental Backupで権限境界の確認ではバックアップ運用のである。バックアップ運用 Incremental Backup 権限境界の確認固有の属性も確認対象に含める。</li><li>B. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 機能の説明としてはBackup andで権限境界の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはアーカイブコピーの保存期間と宛先を定めるコピー規則をノード割当確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで権限境界確でCの記述「Backup andで権限境界の確認ではコピーグループの」に対応する項目は権限境界の確認 CG12（Backup・権限境界）です。コピー・権限境に関するコピーグループの仕様は「Backup andで権限境界の確認ではコピーグループの」で、確認対象はBackup・権限境界確です。Incre・権限境界確のA:は「Incremental Backupで権限境界の確認ではバックアップ」を述べ、対象は権限境界の確認 BKP12（Increme・権限境界）です。サーバで切替のB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・切替）です。archをノード割当のD:は「アーカイブコピーの保存期間と宛先を定めるコピー規則をノード割当確認す」を述べ、対象はノード割当確認 対象表（archive・ノード割）です。Backを権限境界確という用語は「Backup andで権限境界の確認ではコピーグルー」を指し、権限境界の確認 CG12（Backup・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 権限境界の確認 CG12</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて実行権限を点検し、CG12のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG12 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG12の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG12 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG12 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG12のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG12 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG12 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG12のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG12 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Management が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Copy が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0049"><h3>コピーグループ Backup and Archive Copy Group 通常状態の確認 CG01</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>通常状態の確認では コピーグループ の コピーグループ照会 を主操作として CG01 を判定します。基準値と現在値の差への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG01 に残します。通常状態の確認を補助する アーカイブグループ では RetainVersion を補助値として CG01 へ保存します。主判定の通常状態の確認ではコピーグループの コピーグループ照会 から VersionsData を読み CG01 へ残します。証跡照合の通常状態の確認ではコピーグループの VersionsData と RetainVersion を CG01 に保存します。記録対応の通常状態の確認ではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 通常状態の確認 CG01の設定や表示を読む前に役割を確認します。コピーグループ Backup and Archive Copy Groupではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはBackup andで通常状態の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。</li><li>C. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 対象資源に対する働きはSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。クライアントスケジュール Schedule Name 0279固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーで通常状態確でAの記述「Backup andで通常状態の確認ではコピーグループの」に対応する項目は通常状態の確認 CG01（Backup・通常状態）です。コピー・通常状に関するコピーグループの仕様は「Backup andで通常状態の確認ではコピーグループの」で、確認対象はBackup・通常状態確です。コピーで構成監査のB:は「Backup andで構成監査ではコピーグループの」を述べ、対象は構成監査 CG08（Backup・構成監査）です。変更時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・変更）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。Backを通常状態確という用語は「Backup andで通常状態の確認ではコピーグルー」を指し、通常状態の確認 CG01（Backup・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 通常状態の確認 CG01</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて通常状態を確定し、CG01のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG01 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG01のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG01 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG01 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG01のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG01 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG01 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG01の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG01 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Management が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0050"><h3>コピーグループ Backup and Archive Copy Group 障害切り分け CG04</h3><p class="kb-meta">分類: コピーグループ ・ 難易度: 中級</p><p>障害切り分けでは コピーグループ の コピーグループ照会 を主操作として CG04 を判定します。最初に失敗した処理への注意として「バックアップ保持値をアーカイブ保持へ適用する危険があります」を CG04 に残します。障害切り分けを補助する アーカイブグループ では RetainVersion を補助値として CG04 へ保存します。主判定の障害切り分けではコピーグループの コピーグループ照会 から VersionsData を読み CG04 へ残します。証跡照合の障害切り分けではコピーグループの VersionsData と RetainVersion を CG04 に保存します。記録対応の障害切り分けではコピーグループの VEREXISTSとRETEXTRA の証跡へ CG04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> コピーグループ Backup and Archive Copy Group 障害切り分け CG04の役割を調べています。バックアップ運用 Incremental Backup 引継ぎ記録 BKP09の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はBackup andで障害切り分けではコピーグループの コピーグループ照会からVersionsDataを読みである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はIncremental Backupで引継ぎ記録ではバックアップ運用の 活動ログからANR2507Iを読みである。</li><li>C. 表示や設定で扱う内容はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。ポリシーと管理クラス Copy Group 0131固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> コピーでコピーグルでAの記述「Backup andで障害切り分けではコピーグループの」に対応する項目は障害切り分け CG04（Backup・コピーグ）です。コピー・障害切に関するコピーグループの仕様は「Backup andで障害切り分けではコピーグループの」で、確認対象はBackup・コピーグルです。バックでバックアッのB:は「Incremental Backupで引継ぎ記録ではバックアップ運用」を述べ、対象は引継ぎ記録 BKP09（Increme・バックア）です。診断時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・診断）です。Manaを計画のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・計画）です。Backをコピーグルという用語は「Backup andで障害切り分けではコピーグループ」を指し、障害切り分け CG04（Backup・コピーグ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コピーグループ Backup and Archive Copy Group 障害切り分け CG04</strong></p><p>検証目的: コピーグループのBackup and Archive Copy Groupについて障害範囲を限定し、CG04のVEREXISTSとRETEXTRAを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象CG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG04 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILEDを指定し、CG04のコピーグループ照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG04 ACTIVE STANDARD TYPE=BACKUP FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Backup
Versions Data Exists: 5
Retain Extra Versions: 30
Destination: DIRPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY COPYGROUP CG04 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILEDを指定し、CG04のアーカイブグループを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY COPYGROUP CG04 ACTIVE STANDARD TYPE=ARCHIVE FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Copy Group Type: Archive
Retain Version: 365
Destination: ARCHPOOL
画面・出力にあるCopyを読み、VEREXISTSとRETEXTRAと対象CG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のコピーグループを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS CG04 ACTIVE STANDARD FORMAT=DETAILEDを指定し、CG04の管理クラス対応を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY MGMTCLASS CG04 ACTIVE STANDARD FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Management Class Name: STANDARD Backup Copy Group: STANDARD Archive Copy Group: STANDARD
画面・出力にあるManagementを読み、VEREXISTSとRETEXTRAと対象CG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Copy が画面・出力に表示されること
② ステップ2 の Copy が画面・出力に表示されること
③ ステップ3 の Management が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## サーバーDB・DR


<section class="kb-item" id="c14-i0051"><h3>サーバーDB・DR Server Database Backup ログとの照合 DBBK07</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>ログとの照合では サーバーDB・DR の DB状態 を主操作として DBBK07 を判定します。時刻と対象識別子への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK07 に残します。ログとの照合を補助する DBバックアップ では ANR4550I を補助値として DBBK07 へ保存します。主判定のログとの照合ではサーバーの DB状態 から LastDatabase を読み DBBK07 へ残します。証跡照合のログとの照合ではサーバーの LastDatabase と ANR4550I を DBBK07 に保存します。記録対応のログとの照合ではサーバーの Backup SeriesとVolume History の証跡へ DBBK07 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup ログとの照合 DBBK07に関する障害切り分けの前提を確認しています。サーバー日次運用 Server Name 0076の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はDBでログとの照合ではサーバーの DB状態からLastDatabaseを読み・ログとの照合に使うである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 表示や設定で扱う内容はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Association 0240固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はクライアントに適用するバックアップとアーカイブの規則を束ねる単位である。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> ログとの対象DBでAの記述「DBでログとの照合ではサーバーの DB状態からLastDatabas」に対応する項目はログとの照合 DBBK07（DB・ログと・ログとの）です。サーバ・ログとに関するサーバーDB・DRの仕様は「DBでログとの照合ではサーバーの DB状態からLastDatabas」で、確認対象はDB・ログと・ログとのです。監査対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査・DBバッ）です。保護時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・保護・関連ノー）です。poliを宛先照合のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」を述べ、対象は宛先照合 プロファイル（policy・宛先照・プロファ）です。ログとの照をログとのという用語は「DBでログとの照合ではサーバーの」を指し、ログとの照合 DBBK07（DB・ログと・ログとの）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup ログとの照合 DBBK07</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて操作とログを対応し、DBBK07のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK07のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK07のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK07の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Available が画面・出力に表示されること
② ステップ2 の ANR4550I が画面・出力に表示されること
③ ステップ3 の BACKUPFULL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0052"><h3>サーバーDB・DR Server Database Backup 代替経路の確認 DBBK10</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>代替経路の確認では サーバーDB・DR の DB状態 を主操作として DBBK10 を判定します。主経路との役割差への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK10 に残します。代替経路の確認を補助する DBバックアップ では ANR4550I を補助値として DBBK10 へ保存します。主判定の代替経路の確認ではサーバーの DB状態 から LastDatabase を読み DBBK10 へ残します。証跡照合の代替経路の確認ではサーバーの LastDatabase と ANR4550I を DBBK10 に保存します。記録対応の代替経路の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK10 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバーDB・DR Server Database Backup 代替経路の確認 DBBK10」を「ポリシーと管理クラス Copy Group 0086」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 保守作業で参照する機能はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 保守作業で参照する機能はPolicy Domainで再始動後の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>D. 保守作業で参照する機能はDBで代替経路の確認ではサーバーの DB状態からLastDatabaseを読み・代替経路確認に使うである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 代替経路対象DBでDの記述「DBで代替経路の確認ではサーバーの DB状態からLastDataba」に対応する項目は代替経路の確認 DBBK10（DB・代替経・代替経路）です。サーバ・代替経に関するサーバーDB・DRの仕様は「DBで代替経路の確認ではサーバーの DB状態からLastDataba」で、確認対象はDB・代替経・代替経路です。Copy・変更のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・変更・コピーグ）です。照合対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・照合・関連ノー）です。再始動確時のPolicのC:は「Policy Domainで再始動後の確認ではポリシードメインの」を述べ、対象は再始動後の確認 DOM15（Policy・再始動・再始動後）です。代替経路のを代替経路という用語は「DBで代替経路の確認ではサーバーの」を指し、代替経路の確認 DBBK10（DB・代替経・代替経路）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 代替経路の確認 DBBK10</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて代替手段の成立を確認し、DBBK10のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK10のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK10のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK10の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Available が画面・出力に表示されること
② ステップ2 の ANR4550I が画面・出力に表示されること
③ ステップ3 の BACKUPFULL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0053"><h3>サーバーDB・DR Server Database Backup 依存関係の確認 DBBK13</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>依存関係の確認では サーバーDB・DR の DB状態 を主操作として DBBK13 を判定します。前提資源と後続処理の順序への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK13 に残します。依存関係の確認を補助する DBバックアップ では ANR4550I を補助値として DBBK13 へ保存します。主判定の依存関係の確認ではサーバーの DB状態 から LastDatabase を読み DBBK13 へ残します。証跡照合の依存関係の確認ではサーバーの LastDatabase と ANR4550I を DBBK13 に保存します。記録対応の依存関係の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK13 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 依存関係の確認 DBBK13の技術的な意味を資料で確認するとき、ポリシーと管理クラス DIRMC 0008との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>B. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 管理対象との関係を表す説明はBackup andで障害切り分けではコピーグループの コピーグループ照会からVersionsDataを読みである。</li><li>D. 管理対象との関係を表す説明はDBで依存関係の確認ではサーバーの DB状態からLastDatabaseを読み・依存関係確認に使うである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 依存関係対象DBでDの記述「DBで依存関係の確認ではサーバーの DB状態からLastDataba」に対応する項目は依存関係の確認 DBBK13（DB・依存関・依存関係）です。サーバ・依存関に関するサーバーDB・DRの仕様は「DBで依存関係の確認ではサーバーの DB状態からLastDataba」で、確認対象はDB・依存関・依存関係です。巡回対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・巡回・ノード登）です。照合対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・照合・期限切れ）です。コピーグ時のBackuのC:は「Backup andで障害切り分けではコピーグループの」を述べ、対象は障害切り分け CG04（Backup・コピー・コピーグ）です。依存関係のを依存関係という用語は「DBで依存関係の確認ではサーバーの」を指し、依存関係の確認 DBBK13（DB・依存関・依存関係）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 依存関係の確認 DBBK13</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて依存資源を点検し、DBBK13のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK13と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK13のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK13のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK13の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Available が画面・出力に表示されること
② ステップ2 の ANR4550I が画面・出力に表示されること
③ ステップ3 の BACKUPFULL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0054"><h3>サーバーDB・DR Server Database Backup 停止前の確認 DBBK14</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>停止前の確認では サーバーDB・DR の DBバックアップ を主操作として DBBK14 を判定します。処理中資源と未完了要求への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK14 に残します。停止前の確認を補助する 履歴照会 では BACKUPFULL を補助値として DBBK14 へ保存します。主判定の停止前の確認ではサーバーの DBバックアップ から ANR4550I を読み DBBK14 へ残します。証跡照合の停止前の確認ではサーバーの ANR4550I と BACKUPFULL を DBBK14 に保存します。記録対応の停止前の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK14 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 停止前の確認 DBBK14を保守記録に説明する必要があります。ポリシーと管理クラス Policy Domain 0065と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。ポリシーと管理クラス Policy Domain 0065固有の属性も確認対象に含める。</li><li>C. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>D. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則である。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 停止確認対象DBでAの記述「DBで停止前の確認ではサーバーの DBバックアップからANR4550」に対応する項目は停止前の確認 DBBK14（DB・停止確・停止前の）です。サーバ・停止前に関するサーバーDB・DRの仕様は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」で、確認対象はDB・停止確・停止前のです。監査対象PolicのB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・監査・管理クラ）です。抑止時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・抑止・イベント）です。backを保存期間確のD:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は保存期間確認 ルール読替（backup・保存期・ルール読）です。停止前の確を停止確認という用語は「DBで停止前の確認ではサーバーの」を指し、停止前の確認 DBBK14（DB・停止確・停止前の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 停止前の確認 DBBK14</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて安全な停止条件を確認し、DBBK14のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK14と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK14のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK14の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK14のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR4550I が画面・出力に表示されること
② ステップ2 の BACKUPFULL が画面・出力に表示されること
③ ステップ3 の Available が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0055"><h3>サーバーDB・DR Server Database Backup 再始動後の確認 DBBK15</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>再始動後の確認では サーバーDB・DR の 履歴照会 を主操作として DBBK15 を判定します。再開点と未処理データへの注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK15 に残します。再始動後の確認を補助する DB状態 では LastDatabase を補助値として DBBK15 へ保存します。主判定の再始動後の確認ではサーバーの 履歴照会 から BACKUPFULL を読み DBBK15 へ残します。証跡照合の再始動後の確認ではサーバーの BACKUPFULL と LastDatabase を DBBK15 に保存します。記録対応の再始動後の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK15 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 再始動後の確認 DBBK15に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Policy Set 0017の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>B. 機能の説明としてはDBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・再始動確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>D. 機能の説明としてはバックアップやアーカイブのデータを格納するサーバー側領域である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 再始動確対象DBでBの記述「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」に対応する項目は再始動後の確認 DBBK15（DB・再始動・再始動後）です。サーバ・再始動に関するサーバーDB・DRの仕様は「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」で、確認対象はDB・再始動・再始動後です。Polic・巡回のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・巡回・ディレク）です。照合時のServeのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・照合・DBバッ）です。storを保存期間確のD:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は保存期間確認 検査エンジン（storag・保存期・検査エン）です。再始動後のを再始動確という用語は「DBで再始動後の確認ではサーバーの」を指し、再始動後の確認 DBBK15（DB・再始動・再始動後）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 再始動後の確認 DBBK15</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて再始動結果を検証し、DBBK15のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK15と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK15の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK15のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK15のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の BACKUPFULL が画面・出力に表示されること
② ステップ2 の Available が画面・出力に表示されること
③ ステップ3 の ANR4550I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0056"><h3>サーバーDB・DR Server Database Backup 変更前の確認 DBBK02</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>変更前の確認では サーバーDB・DR の DBバックアップ を主操作として DBBK02 を判定します。変更対象と非対象の境界への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK02 に残します。変更前の確認を補助する 履歴照会 では BACKUPFULL を補助値として DBBK02 へ保存します。主判定の変更前の確認ではサーバーの DBバックアップ から ANR4550I を読み DBBK02 へ残します。証跡照合の変更前の確認ではサーバーの ANR4550I と BACKUPFULL を DBBK02 に保存します。記録対応の変更前の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK02 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバーDB・DR Server Database Backup 変更前の確認 DBBK02」を「クライアントスケジュール Start Time 0063」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。クライアントスケジュール Start Time 0063固有の属性も確認対象に含める。</li><li>B. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 仕様上の役割は保存期間を過ぎた版やアーカイブを期限切れにする処理をノード割当確認する。</li><li>D. 仕様上の役割はDBで変更前の確認ではサーバーの DBバックアップからANR4550Iを読み・変更確認に使うである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認対象DBでDの記述「DBで変更前の確認ではサーバーの DBバックアップからANR4550」に対応する項目は変更前の確認 DBBK02（DB・変更確・変更前の）です。サーバ・変更前に関するサーバーDB・DRの仕様は「DBで変更前の確認ではサーバーの DBバックアップからANR4550」で、確認対象はDB・変更確・変更前のです。Start・監査のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査・失敗理由）です。確認対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・確認・イベント）です。ノード割時のexpirのC:は「保存期間を過ぎた版やアーカイブを期限切れにする処理をノード割当確認す」を述べ、対象はノード割当確認 管理レポート（expira・ノード・管理レポ）です。変更前の確を変更確認という用語は「DBで変更前の確認ではサーバーの」を指し、変更前の確認 DBBK02（DB・変更確・変更前の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 変更前の確認 DBBK02</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて変更前の証跡を保存し、DBBK02のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK02のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK02の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK02のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR4550I が画面・出力に表示されること
② ステップ2 の BACKUPFULL が画面・出力に表示されること
③ ステップ3 の Available が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0057"><h3>サーバーDB・DR Server Database Backup 変更後の確認 DBBK03</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>変更後の確認では サーバーDB・DR の 履歴照会 を主操作として DBBK03 を判定します。反映値と残存値への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK03 に残します。変更後の確認を補助する DB状態 では LastDatabase を補助値として DBBK03 へ保存します。主判定の変更後の確認ではサーバーの 履歴照会 から BACKUPFULL を読み DBBK03 へ残します。証跡照合の変更後の確認ではサーバーの BACKUPFULL と LastDatabase を DBBK03 に保存します。記録対応の変更後の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK03 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 変更後の確認 DBBK03の役割を調べています。サーバー日次運用 Node Name 0058の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 機能の説明としてはDBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・変更確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>D. 機能の説明としてはバックアップやアーカイブのデータを格納するサーバー側領域をノード割当確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認対象DBでBの記述「DBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを」に対応する項目は変更後の確認 DBBK03（DB・変更確・変更後の）です。サーバ・変更後に関するサーバーDB・DRの仕様は「DBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを」で、確認対象はDB・変更確・変更後のです。Node・復旧のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧・運用状態）です。登録時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・登録・スケジュ）です。storをノード割当のD:は「バックアップやアーカイブのデータを格納するサーバー側領域をノード割当」を述べ、対象はノード割当確認 接続認証（storag・ノード・接続認証）です。変更後の確を変更確認という用語は「DBで変更後の確認ではサーバーの」を指し、変更後の確認 DBBK03（DB・変更確・変更後の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 変更後の確認 DBBK03</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて変更結果を検証し、DBBK03のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK03の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK03のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK03のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の BACKUPFULL が画面・出力に表示されること
② ステップ2 の Available が画面・出力に表示されること
③ ステップ3 の ANR4550I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0058"><h3>サーバーDB・DR Server Database Backup 引継ぎ記録 DBBK09</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>引継ぎ記録では サーバーDB・DR の 履歴照会 を主操作として DBBK09 を判定します。次担当者が追跡できる証跡への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK09 に残します。引継ぎ記録を補助する DB状態 では LastDatabase を補助値として DBBK09 へ保存します。主判定の引継ぎ記録ではサーバーの 履歴照会 から BACKUPFULL を読み DBBK09 へ残します。証跡照合の引継ぎ記録ではサーバーの BACKUPFULL と LastDatabase を DBBK09 に保存します。記録対応の引継ぎ記録ではサーバーの Backup SeriesとVolume History の証跡へ DBBK09 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 引継ぎ記録 DBBK09を同一分類のクライアントスケジュール Action 0066と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。クライアントスケジュール Action 0066固有の属性も確認対象に含める。</li><li>B. 構成を確認する際の意味はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 構成を確認する際の意味はDBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読み・サーバーDBに使うである。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はManagement Classで代替経路の確認では管理クラスのである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> サーバー対象DBでCの記述「DBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読」に対応する項目は引継ぎ記録 DBBK09（DB・サーバ・引継ぎ記）です。サーバ・引継ぎに関するサーバーDB・DRの仕様は「DBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読」で、確認対象はDB・サーバ・引継ぎ記です。Actio・監査のA:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・監査・開始時刻）です。照合対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合・ノード登）です。Manaを代替経路確のD:は「Management Classで代替経路の確認では管理クラスの」を述べ、対象は代替経路の確認 MC10（Manage・代替経・代替経路）です。引継ぎ記録をサーバーという用語は「DBで引継ぎ記録ではサーバーの」を指し、引継ぎ記録 DBBK09（DB・サーバ・引継ぎ記）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 引継ぎ記録 DBBK09</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて再現可能な記録を作成し、DBBK09のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK09の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK09のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK09のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の BACKUPFULL が画面・出力に表示されること
② ステップ2 の Available が画面・出力に表示されること
③ ステップ3 の ANR4550I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0059"><h3>サーバーDB・DR Server Database Backup 復旧後の確認 DBBK06</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>復旧後の確認では サーバーDB・DR の 履歴照会 を主操作として DBBK06 を判定します。再発していないことを示す値への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK06 に残します。復旧後の確認を補助する DB状態 では LastDatabase を補助値として DBBK06 へ保存します。主判定の復旧後の確認ではサーバーの 履歴照会 から BACKUPFULL を読み DBBK06 へ残します。証跡照合の復旧後の確認ではサーバーの BACKUPFULL と LastDatabase を DBBK06 に保存します。記録対応の復旧後の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK06 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 復旧後の確認 DBBK06を保守記録に説明する必要があります。サーバー日次運用 Database Backup 0007と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 運用時に利用する技術的役割はAssociationの関連ノードと取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 運用時に利用する技術的役割はサーバー操作とメッセージを追跡するログをコマンド証跡として確認する。</li><li>D. 運用時に利用する技術的役割はDBで復旧後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・復旧確認に使うである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認対象DBでDの記述「DBで復旧後の確認ではサーバーの 履歴照会からBACKUPFULLを」に対応する項目は復旧後の確認 DBBK06（DB・復旧確・復旧後の）です。サーバ・復旧後に関するサーバーDB・DRの仕様は「DBで復旧後の確認ではサーバーの 履歴照会からBACKUPFULLを」で、確認対象はDB・復旧確・復旧後のです。Datab・巡回のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・巡回・期限切れ）です。保護対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・保護・関連ノー）です。バックア時のactivのC:は「サーバー操作とメッセージを追跡するログをコマンド証跡として確認する」を述べ、対象はコマンド証跡 統計値（activi・バック・統計値）です。復旧後の確を復旧確認という用語は「DBで復旧後の確認ではサーバーの」を指し、復旧後の確認 DBBK06（DB・復旧確・復旧後の）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 復旧後の確認 DBBK06</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて復旧後の安定性を確認し、DBBK06のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK06の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK06のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK06のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の BACKUPFULL が画面・出力に表示されること
② ステップ2 の Available が画面・出力に表示されること
③ ステップ3 の ANR4550I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0060"><h3>サーバーDB・DR Server Database Backup 復旧準備 DBBK05</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>復旧準備では サーバーDB・DR の DBバックアップ を主操作として DBBK05 を判定します。再開前に必要な整合性への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK05 に残します。復旧準備を補助する 履歴照会 では BACKUPFULL を補助値として DBBK05 へ保存します。主判定の復旧準備ではサーバーの DBバックアップ から ANR4550I を読み DBBK05 へ残します。証跡照合の復旧準備ではサーバーの ANR4550I と BACKUPFULL を DBBK05 に保存します。記録対応の復旧準備ではサーバーの Backup SeriesとVolume History の証跡へ DBBK05 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 復旧準備 DBBK05の技術的な意味を資料で確認するとき、サーバー日次運用 Database Backup 0022との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. コマンドまたは機能の用途はDBで復旧準備ではサーバーの DBバックアップからANR4550Iを読み・復旧準備に使うである。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途は保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧準備対象DBでCの記述「DBで復旧準備ではサーバーの DBバックアップからANR4550Iを」に対応する項目は復旧準備 DBBK05（DB・復旧準・復旧準備）です。サーバ・復旧準に関するサーバーDB・DRの仕様は「DBで復旧準備ではサーバーの DBバックアップからANR4550Iを」で、確認対象はDB・復旧準・復旧準備です。Datab・棚卸のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・棚卸・期限切れ）です。照合対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・照合・ストレー）です。expiを復元前確認のD:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」を述べ、対象は復元前確認 自動処理（expira・復元前・自動処理）です。復旧準備でを復旧準備という用語は「DBで復旧準備ではサーバーの DBバックアップからA」を指し、復旧準備 DBBK05（DB・復旧準・復旧準備）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 復旧準備 DBBK05</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて復旧条件を確認し、DBBK05のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK05のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK05の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK05のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR4550I が画面・出力に表示されること
② ステップ2 の BACKUPFULL が画面・出力に表示されること
③ ステップ3 の Available が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0061"><h3>サーバーDB・DR Server Database Backup 性能影響の確認 DBBK11</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>性能影響の確認では サーバーDB・DR の DBバックアップ を主操作として DBBK11 を判定します。処理時間と滞留箇所への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK11 に残します。性能影響の確認を補助する 履歴照会 では BACKUPFULL を補助値として DBBK11 へ保存します。主判定の性能影響の確認ではサーバーの DBバックアップ から ANR4550I を読み DBBK11 へ残します。証跡照合の性能影響の確認ではサーバーの ANR4550I と BACKUPFULL を DBBK11 に保存します。記録対応の性能影響の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK11 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 性能影響の確認 DBBK11の役割を調べています。サーバー日次運用 Node Name 0028の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はDBで性能影響の確認ではサーバーの DBバックアップからANR4550Iを読み・性能影響確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。ポリシーと管理クラス Policy Set 0272固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はManagement Classで引継ぎ記録では管理クラスの オプション確認からDIRMCを読みである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 性能影響対象DBでAの記述「DBで性能影響の確認ではサーバーの DBバックアップからANR455」に対応する項目は性能影響の確認 DBBK11（DB・性能影・性能影響）です。サーバ・性能影に関するサーバーDB・DRの仕様は「DBで性能影響の確認ではサーバーの DBバックアップからANR455」で、確認対象はDB・性能影・性能影響です。棚卸対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・棚卸・運用状態）です。照合時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・照合・ディレク）です。Manaを管理クラスのD:は「Management Classで引継ぎ記録では管理クラスの」を述べ、対象は引継ぎ記録 MC09（Manage・管理ク・引継ぎ記）です。性能影響のを性能影響という用語は「DBで性能影響の確認ではサーバーの」を指し、性能影響の確認 DBBK11（DB・性能影・性能影響）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 性能影響の確認 DBBK11</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて負荷と待ちを確認し、DBBK11のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK11と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK11のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK11の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK11のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR4550I が画面・出力に表示されること
② ステップ2 の BACKUPFULL が画面・出力に表示されること
③ ステップ3 の Available が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0062"><h3>サーバーDB・DR Server Database Backup 構成監査 DBBK08</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>構成監査では サーバーDB・DR の DBバックアップ を主操作として DBBK08 を判定します。定義値と稼働値の一致への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK08 に残します。構成監査を補助する 履歴照会 では BACKUPFULL を補助値として DBBK08 へ保存します。主判定の構成監査ではサーバーの DBバックアップ から ANR4550I を読み DBBK08 へ残します。証跡照合の構成監査ではサーバーの ANR4550I と BACKUPFULL を DBBK08 に保存します。記録対応の構成監査ではサーバーの Backup SeriesとVolume History の証跡へ DBBK08 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 構成監査 DBBK08の設定や表示を読む前に役割を確認します。サーバー日次運用 Expiration Status 0079ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はDBで構成監査ではサーバーの DBバックアップからANR4550Iを読み・構成監査に使うである。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 一次資料が示す主目的はストレージプール内の空き領域を回収する処理である。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構成監査対象DBでAの記述「DBで構成監査ではサーバーの DBバックアップからANR4550Iを」に対応する項目は構成監査 DBBK08（DB・構成監・構成監査）です。サーバ・構成監に関するサーバーDB・DRの仕様は「DBで構成監査ではサーバーの DBバックアップからANR4550Iを」で、確認対象はDB・構成監・構成監査です。監査対象ExpirのB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expira・監査・ノード登）です。収集時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・収集・スケジュ）です。reclを保存期間確のD:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は保存期間確認 画面タグ（reclam・保存期・画面タグ）です。構成監査でを構成監査という用語は「DBで構成監査ではサーバーの DBバックアップからA」を指し、構成監査 DBBK08（DB・構成監・構成監査）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 構成監査 DBBK08</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて構成差分を監査し、DBBK08のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK08のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK08の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK08のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ANR4550I が画面・出力に表示されること
② ステップ2 の BACKUPFULL が画面・出力に表示されること
③ ステップ3 の Available が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0063"><h3>サーバーDB・DR Server Database Backup 権限境界の確認 DBBK12</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>権限境界の確認では サーバーDB・DR の 履歴照会 を主操作として DBBK12 を判定します。参照操作と変更操作の分離への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK12 に残します。権限境界の確認を補助する DB状態 では LastDatabase を補助値として DBBK12 へ保存します。主判定の権限境界の確認ではサーバーの 履歴照会 から BACKUPFULL を読み DBBK12 へ残します。証跡照合の権限境界の確認ではサーバーの BACKUPFULL と LastDatabase を DBBK12 に保存します。記録対応の権限境界の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK12 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 権限境界の確認 DBBK12について構成や状態を確認します。ポリシーと管理クラス Policy Set 0047ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはDBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULLを読み・権限境界確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。ポリシーと管理クラス Policy Set 0047固有の属性も確認対象に含める。</li><li>C. 状態を読み取るための働きはManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 状態を読み取るための働きはDirectory-containeで通常状態の確認ではストレージプールのである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 権限境界対象DBでAの記述「DBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULL」に対応する項目は権限境界の確認 DBBK12（DB・権限境・権限境界）です。サーバ・権限境に関するサーバーDB・DRの仕様は「DBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULL」で、確認対象はDB・権限境・権限境界です。復旧対象PolicのB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・復旧・ディレク）です。保護時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・保護・ドメイン）です。Direを通常状態確のD:は「Directory-containeで通常状態の確認ではストレージプ」を述べ、対象は通常状態の確認 POOL01（Direct・通常状・通常状態）です。権限境界のを権限境界という用語は「DBで権限境界の確認ではサーバーの」を指し、権限境界の確認 DBBK12（DB・権限境・権限境界）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 権限境界の確認 DBBK12</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて実行権限を点検し、DBBK12のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK12と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK12の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK12のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK12のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の BACKUPFULL が画面・出力に表示されること
② ステップ2 の Available が画面・出力に表示されること
③ ステップ3 の ANR4550I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0064"><h3>サーバーDB・DR Server Database Backup 通常状態の確認 DBBK01</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>通常状態の確認では サーバーDB・DR の DB状態 を主操作として DBBK01 を判定します。基準値と現在値の差への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK01 に残します。通常状態の確認を補助する DBバックアップ では ANR4550I を補助値として DBBK01 へ保存します。主判定の通常状態の確認ではサーバーの DB状態 から LastDatabase を読み DBBK01 へ残します。証跡照合の通常状態の確認ではサーバーの LastDatabase と ANR4550I を DBBK01 に保存します。記録対応の通常状態の確認ではサーバーの Backup SeriesとVolume History の証跡へ DBBK01 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 通常状態の確認 DBBK01を同一分類のサーバーDB・DR Server Database Backup 変更後の確認と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はDBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・変更確認に使うである。</li><li>B. 管理対象との関係を表す説明はDBで通常状態の確認ではサーバーの DB状態からLastDatabaseを読み・通常状態確認に使うである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 管理対象との関係を表す説明はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 通常状態対象DBでBの記述「DBで通常状態の確認ではサーバーの DB状態からLastDataba」に対応する項目は通常状態の確認 DBBK01（DB・通常状・通常状態）です。サーバ・通常状に関するサーバーDB・DRの仕様は「DBで通常状態の確認ではサーバーの DB状態からLastDataba」で、確認対象はDB・通常状・通常状態です。変更確認対象変更後の確のA:は「DBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを」を述べ、対象は変更後の確認 DBBK03（DB・変更確・変更後の）です。保護時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・保護・ディレク）です。Backを変更確認のD:は「Backup andで変更前の確認ではコピーグループの」を述べ、対象は変更前の確認 CG02（Backup・変更確・確認では）です。通常状態のを通常状態という用語は「DBで通常状態の確認ではサーバーの」を指し、通常状態の確認 DBBK01（DB・通常状・通常状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 通常状態の確認 DBBK01</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて通常状態を確定し、DBBK01のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK01のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK01のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK01の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Available が画面・出力に表示されること
② ステップ2 の ANR4550I が画面・出力に表示されること
③ ステップ3 の BACKUPFULL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0065"><h3>サーバーDB・DR Server Database Backup 障害切り分け DBBK04</h3><p class="kb-meta">分類: サーバーDB・DR ・ 難易度: 上級</p><p>障害切り分けでは サーバーDB・DR の DB状態 を主操作として DBBK04 を判定します。最初に失敗した処理への注意として「DBバックアップ媒体とボリューム履歴を別世代で保管する危険があります」を DBBK04 に残します。障害切り分けを補助する DBバックアップ では ANR4550I を補助値として DBBK04 へ保存します。主判定の障害切り分けではサーバーの DB状態 から LastDatabase を読み DBBK04 へ残します。証跡照合の障害切り分けではサーバーの LastDatabase と ANR4550I を DBBK04 に保存します。記録対応の障害切り分けではサーバーの Backup SeriesとVolume History の証跡へ DBBK04 を結びます。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバーDB・DR Server Database Backup 障害切り分け DBBK04について構成や状態を確認します。ポリシーと管理クラス Policy Set 0077ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>B. 対象資源に対する働きはEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 対象資源に対する働きはDBで障害切り分けではサーバーの DB状態からLastDatabaseを読み・サーバーDBに使うである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはサーバー操作とメッセージを追跡するログをコマンド証跡として確認する。activity log コマンド証跡 統計値固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> サーバー対象DBでCの記述「DBで障害切り分けではサーバーの DB状態からLastDatabas」に対応する項目は障害切り分け DBBK04（DB・サーバ・障害切り）です。サーバ・障害切に関するサーバーDB・DRの仕様は「DBで障害切り分けではサーバーの DB状態からLastDatabas」で、確認対象はDB・サーバ・障害切りです。Polic・監査のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・監査・ディレク）です。登録対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・登録・イベント）です。actiをバックアッのD:は「サーバー操作とメッセージを追跡するログをコマンド証跡として確認する」を述べ、対象はコマンド証跡 統計値（activi・バック・統計値）です。障害切り分をサーバーという用語は「DBで障害切り分けではサーバーの」を指し、障害切り分け DBBK04（DB・サーバ・障害切り）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバーDB・DR Server Database Backup 障害切り分け DBBK04</strong></p><p>検証目的: サーバーDB・DRのServer Database Backupについて障害範囲を限定し、DBBK04のBackup SeriesとVolume Historyを実出力で確認する。</p><p>前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DBBK04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY DB FORMAT=DETAILEDを指定し、DBBK04のDB状態を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY DB FORMAT=DETAILED
→ Enter を押す
［画面・出力］
Available Space (MB): 524288
Assigned Capacity (MB): 262144
Pct Util: 48.1
Last Database Backup Date/Time: 07/15/2026 02:00
画面・出力にあるAvailableを読み、Backup SeriesとVolume Historyと対象DBBK04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へBACKUP DB TYPE=FULL DEVCLASS=LTOを指定し、DBBK04のDBバックアップを表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; BACKUP DB TYPE=FULL DEVCLASS=LTO
→ Enter を押す
［画面・出力］
ANR1360I Full database backup started. ANR4550I Full database backup completed successfully.
画面・出力にあるANR4550Iを読み、Backup SeriesとVolume Historyと対象DBBK04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1のサーバーDB・DRを確認する入力画面です。COMMAND入力口へQUERY VOLHISTORY TYPE=DBBACKUPを指定し、DBBK04の履歴照会を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面
COMMAND ===&gt; QUERY VOLHISTORY TYPE=DBBACKUP
→ Enter を押す
［画面・出力］
Date/Time: 07/15/2026 02:00 Volume Type: BACKUPFULL Volume Name: DBBK001
画面・出力にあるBACKUPFULLを読み、Backup SeriesとVolume Historyと対象DBBK04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の Available が画面・出力に表示されること
② ステップ2 の ANR4550I が画面・出力に表示されること
③ ステップ3 の BACKUPFULL が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


## サーバー運用


<section class="kb-item" id="c14-i0066"><h3>サーバー日次運用 Database Backup 0007</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>茶H巡回0008ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票茶H巡回0008です。茶H巡回0008はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録茶H巡回0008です。茶H巡回0008では期限切れ処理と取得時刻を採取票茶H巡回0008へ残します。茶H巡回0008ではプール容量不足の見落としを避けるため補助資料も照合する判断茶H巡回0008です。茶H巡回0008の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録茶H巡回0008です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0007を保守記録に説明する必要があります。クライアントスケジュール Event Status 0012と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 保守作業で参照する機能はDirectory-containeで変更後の確認ではストレージプールのである。ストレージプール Directory-container固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 巡回対象DatabでBの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・巡回・期限切れ）です。サーバに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・巡回・期限切れです。Event・巡回のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・巡回・イベント）です。照合時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・照合・管理クラ）です。Direを変更確認のD:は「Directory-containeで変更後の確認ではストレージプー」を述べ、対象は変更後の確認 POOL03（Direct・変更確・変更後の）です。Dataを巡回という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・巡回・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0007</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0007について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2207
確認コード SP81DD0007A
画面・出力には SP81DD0007A が表示され、サーバー日次運用 Database Backup 0007 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE007
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0007B
画面・出力には SP81DD0007B が表示され、サーバー日次運用 Database Backup 0007 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 507 GB
確認コード SP81DD0007C
画面・出力には SP81DD0007C が表示され、サーバー日次運用 Database Backup 0007 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0007A が画面・出力に表示されること
② ステップ2 の SP81DD0007B が画面・出力に表示されること
③ ステップ3 の SP81DD0007C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0067"><h3>サーバー日次運用 Database Backup 0022</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>緑C棚卸0023ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票緑C棚卸0023です。緑C棚卸0023はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録緑C棚卸0023です。緑C棚卸0023では期限切れ処理と取得時刻を採取票緑C棚卸0023へ残します。緑C棚卸0023ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断緑C棚卸0023です。緑C棚卸0023の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録緑C棚卸0023です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0022の技術的な意味を資料で確認するとき、サーバー日次運用 Storage Pool 0040との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Storage Pool 0040固有の属性も確認対象に含める。</li><li>C. 管理対象との関係を表す説明はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 管理対象との関係を表す説明はClient Nodeで復旧後の確認ではノード管理の 関連付けからAssociatedNodeを読みである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 棚卸対象DatabでAの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・棚卸・期限切れ）です。棚卸時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・棚卸・期限切れです。復旧対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・復旧・ストレー）です。抑止時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・抑止・コピーグ）です。Clieを復旧確認のD:は「Client Nodeで復旧後の確認ではノード管理の」を述べ、対象は復旧後の確認 NODE06（Client・復旧確・復旧後の）です。Dataを棚卸という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・棚卸・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0022</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0022について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2222
確認コード SP81DD0022A
画面・出力には SP81DD0022A が表示され、サーバー日次運用 Database Backup 0022 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE022
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0022B
画面・出力には SP81DD0022B が表示され、サーバー日次運用 Database Backup 0022 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 522 GB
確認コード SP81DD0022C
画面・出力には SP81DD0022C が表示され、サーバー日次運用 Database Backup 0022 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0022A が画面・出力に表示されること
② ステップ2 の SP81DD0022B が画面・出力に表示されること
③ ステップ3 の SP81DD0022C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0068"><h3>サーバー日次運用 Database Backup 0037</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藤R棚卸0038ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藤R棚卸0038です。藤R棚卸0038はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録藤R棚卸0038です。藤R棚卸0038では期限切れ処理と取得時刻を採取票藤R棚卸0038へ残します。藤R棚卸0038では期限切れ処理の未実行を避けるため補助資料も照合する判断藤R棚卸0038です。藤R棚卸0038の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録藤R棚卸0038です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0037について構成や状態を確認します。サーバー日次運用 Storage Pool 0115ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>D. 対象資源に対する働きはバックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 棚卸対象DatabでBの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・棚卸・期限切れ）です。棚卸時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・棚卸・期限切れです。Stora・移行のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・移行・ストレー）です。確認時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・確認・ドメイン）です。scheを復元前確認のD:は「バックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する」を述べ、対象は復元前確認 時刻合わせ（schedu・復元前・時刻合わ）です。Dataを棚卸という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・棚卸・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0037</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0037について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2237
確認コード SP81DD0037A
画面・出力には SP81DD0037A が表示され、サーバー日次運用 Database Backup 0037 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE037
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0037B
画面・出力には SP81DD0037B が表示され、サーバー日次運用 Database Backup 0037 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 537 GB
確認コード SP81DD0037C
画面・出力には SP81DD0037C が表示され、サーバー日次運用 Database Backup 0037 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0037A が画面・出力に表示されること
② ステップ2 の SP81DD0037B が画面・出力に表示されること
③ ステップ3 の SP81DD0037C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0069"><h3>サーバー日次運用 Database Backup 0052</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>桃M復旧0053ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票桃M復旧0053です。桃M復旧0053はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録桃M復旧0053です。桃M復旧0053では期限切れ処理と取得時刻を採取票桃M復旧0053へ残します。桃M復旧0053ではノード状態の誤読を避けるため補助資料も照合する判断桃M復旧0053です。桃M復旧0053の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録桃M復旧0053です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0052の役割を調べています。サーバー日次運用 Server Name 0091の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 表示や設定で扱う内容はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>C. 表示や設定で扱う内容はDirectory-containeで性能影響の確認ではストレージプールのである。</li><li>D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・復旧・期限切れ）です。復旧時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・復旧・期限切れです。Serve・変更のA:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・変更・データベ）です。計画対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・計画・ストレー）です。性能影響時のDirecのC:は「Directory-containeで性能影響の確認ではストレージプ」を述べ、対象は性能影響の確認 POOL11（Direct・性能影・性能影響）です。Dataを復旧という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・復旧・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0052</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0052について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2252
確認コード SP81DD0052A
画面・出力には SP81DD0052A が表示され、サーバー日次運用 Database Backup 0052 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE052
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0052B
画面・出力には SP81DD0052B が表示され、サーバー日次運用 Database Backup 0052 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 552 GB
確認コード SP81DD0052C
画面・出力には SP81DD0052C が表示され、サーバー日次運用 Database Backup 0052 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0052A が画面・出力に表示されること
② ステップ2 の SP81DD0052B が画面・出力に表示されること
③ ステップ3 の SP81DD0052C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0070"><h3>サーバー日次運用 Database Backup 0067</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>茶H監査0068ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票茶H監査0068です。茶H監査0068はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録茶H監査0068です。茶H監査0068では期限切れ処理と取得時刻を採取票茶H監査0068へ残します。茶H監査0068ではプール容量不足の見落としを避けるため補助資料も照合する判断茶H監査0068です。茶H監査0068の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録茶H監査0068です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Database Backup 0067」を「クライアントスケジュール Action 0156」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>C. 保守作業で参照する機能はClient Restoreで変更前の確認ではリストア確認の 別名復元からrestoredを読みである。</li><li>D. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・監査・期限切れ）です。監査時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・監査・期限切れです。Actio・保守のA:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・保守・開始時刻）です。抑止対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・抑止・失敗理由）です。変更確認時のClienのC:は「Client Restoreで変更前の確認ではリストア確認の」を述べ、対象は変更前の確認 RST02（Client・変更確・変更前の）です。Dataを監査という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・監査・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0067</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0067について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2207
確認コード SP81DD0067A
画面・出力には SP81DD0067A が表示され、サーバー日次運用 Database Backup 0067 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE067
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0067B
画面・出力には SP81DD0067B が表示され、サーバー日次運用 Database Backup 0067 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 567 GB
確認コード SP81DD0067C
画面・出力には SP81DD0067C が表示され、サーバー日次運用 Database Backup 0067 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0067A が画面・出力に表示されること
② ステップ2 の SP81DD0067B が画面・出力に表示されること
③ ステップ3 の SP81DD0067C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0071"><h3>サーバー日次運用 Database Backup 0082</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>緑C変更0083ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票緑C変更0083です。緑C変更0083はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録緑C変更0083です。緑C変更0083では期限切れ処理と取得時刻を採取票緑C変更0083へ残します。緑C変更0083ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断緑C変更0083です。緑C変更0083の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録緑C変更0083です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0082を同一分類のクライアントスケジュール Association 0150と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>B. 管理対象との関係を表す説明はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。クライアントスケジュール Action 0321固有の属性も確認対象に含める。</li><li>C. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はDirectory-containeで代替経路の確認ではストレージプールのである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更対象DatabでCの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・変更・期限切れ）です。変更時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・変更・期限切れです。Assoc・保守のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・保守・関連ノー）です。計画対象ActioのB:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・計画・開始時刻）です。Direを代替経路確のD:は「Directory-containeで代替経路の確認ではストレージプ」を述べ、対象は代替経路の確認 POOL10（Direct・代替経・代替経路）です。Dataを変更という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・変更・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0082</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0082について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2222
確認コード SP81DD0082A
画面・出力には SP81DD0082A が表示され、サーバー日次運用 Database Backup 0082 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE082
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0082B
画面・出力には SP81DD0082B が表示され、サーバー日次運用 Database Backup 0082 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 582 GB
確認コード SP81DD0082C
画面・出力には SP81DD0082C が表示され、サーバー日次運用 Database Backup 0082 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0082A が画面・出力に表示されること
② ステップ2 の SP81DD0082B が画面・出力に表示されること
③ ステップ3 の SP81DD0082C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0072"><h3>サーバー日次運用 Database Backup 0097</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藤R変更0098ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藤R変更0098です。藤R変更0098はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録藤R変更0098です。藤R変更0098では期限切れ処理と取得時刻を採取票藤R変更0098へ残します。藤R変更0098では期限切れ処理の未実行を避けるため補助資料も照合する判断藤R変更0098です。藤R変更0098の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録藤R変更0098です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0097の設定や表示を読む前に役割を確認します。クライアントスケジュール Event Status 0192ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 対象資源に対する働きはバックアップ版数と保存先を定めるコピー規則である。backup copy group 状態確認 文字変換固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きはDirectory-containeで引継ぎ記録ではストレージプールのである。</li><li>D. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・変更・期限切れ）です。変更時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・変更・期限切れです。Event・収集のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベント）です。状態確認対象backuのB:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は状態確認 文字変換（backup・状態確・文字変換）です。ストレー時のDirecのC:は「Directory-containeで引継ぎ記録ではストレージプール」を述べ、対象は引継ぎ記録 POOL09（Direct・ストレ・引継ぎ記）です。Dataを変更という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・変更・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0097</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0097について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2237
確認コード SP81DD0097A
画面・出力には SP81DD0097A が表示され、サーバー日次運用 Database Backup 0097 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE097
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0097B
画面・出力には SP81DD0097B が表示され、サーバー日次運用 Database Backup 0097 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 597 GB
確認コード SP81DD0097C
画面・出力には SP81DD0097C が表示され、サーバー日次運用 Database Backup 0097 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0097A が画面・出力に表示されること
② ステップ2 の SP81DD0097B が画面・出力に表示されること
③ ステップ3 の SP81DD0097C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0073"><h3>サーバー日次運用 Database Backup 0112</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>桃M移行0113ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票桃M移行0113です。桃M移行0113はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録桃M移行0113です。桃M移行0113では期限切れ処理と取得時刻を採取票桃M移行0113へ残します。桃M移行0113ではノード状態の誤読を避けるため補助資料も照合する判断桃M移行0113です。桃M移行0113の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録桃M移行0113です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0112に関する障害切り分けの前提を確認しています。クライアントスケジュール Action 0171の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>B. 表示や設定で扱う内容はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はDBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読み・サーバーDBに使うである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 移行対象DatabでCの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Databa・移行・期限切れ）です。移行時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はDatab・移行・期限切れです。Actio・切替のA:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・切替・開始時刻）です。計画対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・計画・コピーグ）です。引継ぎ記録をサーバーのD:は「DBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読」を述べ、対象は引継ぎ記録 DBBK09（DB・サーバ・引継ぎ記）です。Dataを移行という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Databa・移行・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0112</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0112について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2252
確認コード SP81DD0112A
画面・出力には SP81DD0112A が表示され、サーバー日次運用 Database Backup 0112 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE112
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0112B
画面・出力には SP81DD0112B が表示され、サーバー日次運用 Database Backup 0112 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 612 GB
確認コード SP81DD0112C
画面・出力には SP81DD0112C が表示され、サーバー日次運用 Database Backup 0112 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0112A が画面・出力に表示されること
② ステップ2 の SP81DD0112B が画面・出力に表示されること
③ ステップ3 の SP81DD0112C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0074"><h3>サーバー日次運用 Database Backup 0127</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>茶H診断0128ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票茶H診断0128です。茶H診断0128はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録茶H診断0128です。茶H診断0128では期限切れ処理と取得時刻を採取票茶H診断0128へ残します。茶H診断0128ではプール容量不足の見落としを避けるため補助資料も照合する判断茶H診断0128です。茶H診断0128の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録茶H診断0128です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0127を保守記録に説明する必要があります。サーバー日次運用 Storage Pool 0160と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 保守作業で参照する機能はArchive Operationで復旧準備ではアーカイブ運用のである。アーカイブ運用 Archive Operation 復旧準備 ARC05固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 診断対象DatabでAの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・診断・期限切・プール容）です。診断時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・診断・期限切・プール容です。切替対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・切替・ストレ・ノード状）です。解除時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・解除・ノード・管理クラ）です。Archを復旧準備のD:は「Archive Operationで復旧準備ではアーカイブ運用の」を述べ、対象は復旧準備 ARC05（Archi・復旧準・復旧準・バックア）です。Dataを診断という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・診断・期限切・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0127</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0127について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2207
確認コード SP81DD0127A
画面・出力には SP81DD0127A が表示され、サーバー日次運用 Database Backup 0127 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE007
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0127B
画面・出力には SP81DD0127B が表示され、サーバー日次運用 Database Backup 0127 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 507 GB
確認コード SP81DD0127C
画面・出力には SP81DD0127C が表示され、サーバー日次運用 Database Backup 0127 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0127A が画面・出力に表示されること
② ステップ2 の SP81DD0127B が画面・出力に表示されること
③ ステップ3 の SP81DD0127C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0075"><h3>サーバー日次運用 Database Backup 0142</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>緑C保守0143ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票緑C保守0143です。緑C保守0143はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録緑C保守0143です。緑C保守0143では期限切れ処理と取得時刻を採取票緑C保守0143へ残します。緑C保守0143ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断緑C保守0143です。緑C保守0143の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録緑C保守0143です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0142の技術的な意味を資料で確認するとき、ポリシーと管理クラス Copy Group 0146との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>C. 管理対象との関係を表す説明はStorage Poolで復旧後の確認では複製・保護の 検証からANR3730Iを読み・復旧確認に使うである。</li><li>D. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保守対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・保守・期限切・データベ）です。保守時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・保守・期限切・データベです。Copy・保守のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・保守・コピー・ディレク）です。解除対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・解除・ストレ・プール容）です。復旧確認時のStoraのC:は「Storage Poolで復旧後の確認では複製・保護の」を述べ、対象は復旧後の確認 REPL06（Stora・復旧確・復旧後・PROT）です。Dataを保守という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・保守・期限切・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0142</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0142について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2222
確認コード SP81DD0142A
画面・出力には SP81DD0142A が表示され、サーバー日次運用 Database Backup 0142 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE022
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0142B
画面・出力には SP81DD0142B が表示され、サーバー日次運用 Database Backup 0142 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 522 GB
確認コード SP81DD0142C
画面・出力には SP81DD0142C が表示され、サーバー日次運用 Database Backup 0142 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0142A が画面・出力に表示されること
② ステップ2 の SP81DD0142B が画面・出力に表示されること
③ ステップ3 の SP81DD0142C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0076"><h3>サーバー日次運用 Database Backup 0157</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藤R保守0158ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藤R保守0158です。藤R保守0158はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録藤R保守0158です。藤R保守0158では期限切れ処理と取得時刻を採取票藤R保守0158へ残します。藤R保守0158では期限切れ処理の未実行を避けるため補助資料も照合する判断藤R保守0158です。藤R保守0158の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録藤R保守0158です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0157について構成や状態を確認します。サーバー日次運用 Node Name 0253ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 対象資源に対する働きはバックアップやアーカイブのデータを格納するサーバー側領域をノード割当確認する。</li><li>C. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはStorage Poolで再始動後の確認では複製・保護の 検証からANR3730Iを読み・再始動確認に使うである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保守対象DatabでCの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・保守・期限切・期限切れ）です。保守時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・保守・期限切・期限切れです。Node・保護のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・保護・運用状・期限切れ）です。ノード割対象storaのB:は「バックアップやアーカイブのデータを格納するサーバー側領域をノード割当」を述べ、対象はノード割当確認 接続認証（stora・ノード・接続認・接続認証）です。Storを再始動確認のD:は「Storage Poolで再始動後の確認では複製・保護の」を述べ、対象は再始動後の確認 REPL15（Stora・再始動・再始動・PROT）です。Dataを保守という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・保守・期限切・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0157</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0157について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2237
確認コード SP81DD0157A
画面・出力には SP81DD0157A が表示され、サーバー日次運用 Database Backup 0157 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE037
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0157B
画面・出力には SP81DD0157B が表示され、サーバー日次運用 Database Backup 0157 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 537 GB
確認コード SP81DD0157C
画面・出力には SP81DD0157C が表示され、サーバー日次運用 Database Backup 0157 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0157A が画面・出力に表示されること
② ステップ2 の SP81DD0157B が画面・出力に表示されること
③ ステップ3 の SP81DD0157C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0077"><h3>サーバー日次運用 Database Backup 0172</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>桃M切替0173ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票桃M切替0173です。桃M切替0173はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録桃M切替0173です。桃M切替0173では期限切れ処理と取得時刻を採取票桃M切替0173へ残します。桃M切替0173ではノード状態の誤読を避けるため補助資料も照合する判断桃M切替0173です。桃M切替0173の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録桃M切替0173です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0172の役割を調べています。サーバー日次運用 Node Name 0268の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>B. 表示や設定で扱う内容はサーバー操作とメッセージを追跡するログである。</li><li>C. 表示や設定で扱う内容はStorage Poolで性能影響の確認では複製・保護の 複製状態からTargetServerを読みである。</li><li>D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 切替対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・切替・期限切・ノード状）です。切替時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・切替・期限切・ノード状です。Node・照合のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・照合・運用状・ノード状）です。状態確認対象activのB:は「サーバー操作とメッセージを追跡するログ」を述べ、対象は状態確認 高速伝搬（activ・状態確・高速伝・高速伝搬）です。性能影響時のStoraのC:は「Storage Poolで性能影響の確認では複製・保護の」を述べ、対象は性能影響の確認 REPL11（Stora・性能影・性能影・PROT）です。Dataを切替という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・切替・期限切・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0172</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0172について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2252
確認コード SP81DD0172A
画面・出力には SP81DD0172A が表示され、サーバー日次運用 Database Backup 0172 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE052
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0172B
画面・出力には SP81DD0172B が表示され、サーバー日次運用 Database Backup 0172 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 552 GB
確認コード SP81DD0172C
画面・出力には SP81DD0172C が表示され、サーバー日次運用 Database Backup 0172 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0172A が画面・出力に表示されること
② ステップ2 の SP81DD0172B が画面・出力に表示されること
③ ステップ3 の SP81DD0172C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0078"><h3>サーバー日次運用 Database Backup 0187</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>茶H収集0188ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票茶H収集0188です。茶H収集0188はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録茶H収集0188です。茶H収集0188では期限切れ処理と取得時刻を採取票茶H収集0188へ残します。茶H収集0188ではプール容量不足の見落としを避けるため補助資料も照合する判断茶H収集0188です。茶H収集0188の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録茶H収集0188です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Database Backup 0187」を「サーバー日次運用 Expiration Status 0229」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 保守作業で参照する機能はサーバー操作とメッセージを追跡するログである。</li><li>C. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。サーバー日次運用 Storage Pool 0085固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集対象DatabでCの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・収集・期限切・プール容）です。収集時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・収集・期限切・プール容です。Expir・確認のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・確認・ノード・期限切れ）です。宛先照合対象activのB:は「サーバー操作とメッセージを追跡するログ」を述べ、対象は宛先照合 キュー状態（activ・宛先照・キュー・キュー状）です。Storを変更のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・変更・ストレ・期限切れ）です。Dataを収集という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・収集・期限切・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0187</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0187について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2207
確認コード SP81DD0187A
画面・出力には SP81DD0187A が表示され、サーバー日次運用 Database Backup 0187 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE067
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0187B
画面・出力には SP81DD0187B が表示され、サーバー日次運用 Database Backup 0187 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 567 GB
確認コード SP81DD0187C
画面・出力には SP81DD0187C が表示され、サーバー日次運用 Database Backup 0187 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0187A が画面・出力に表示されること
② ステップ2 の SP81DD0187B が画面・出力に表示されること
③ ステップ3 の SP81DD0187C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0079"><h3>サーバー日次運用 Database Backup 0202</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>緑C登録0203ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票緑C登録0203です。緑C登録0203はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録緑C登録0203です。緑C登録0203では期限切れ処理と取得時刻を採取票緑C登録0203へ残します。緑C登録0203ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断緑C登録0203です。緑C登録0203の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録緑C登録0203です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0202を同一分類のポリシーと管理クラス Policy Domain 0290と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 管理対象との関係を表す説明はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。</li><li>C. 管理対象との関係を表す説明はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 登録対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・登録・期限切・データベ）です。登録時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・登録・期限切・データベです。Polic・抑止のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・抑止・管理ク・ディレク）です。変更確認対象BackuのB:は「Backup andで変更前の確認ではコピーグループの」を述べ、対象は変更前の確認 CG02（Backu・変更確・確認で・バックア）です。巡回時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・巡回・イベン・日次処理）です。Dataを登録という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・登録・期限切・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0202</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0202について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2222
確認コード SP81DD0202A
画面・出力には SP81DD0202A が表示され、サーバー日次運用 Database Backup 0202 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE082
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0202B
画面・出力には SP81DD0202B が表示され、サーバー日次運用 Database Backup 0202 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 582 GB
確認コード SP81DD0202C
画面・出力には SP81DD0202C が表示され、サーバー日次運用 Database Backup 0202 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0202A が画面・出力に表示されること
② ステップ2 の SP81DD0202B が画面・出力に表示されること
③ ステップ3 の SP81DD0202C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0080"><h3>サーバー日次運用 Database Backup 0217</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藤R登録0218ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藤R登録0218です。藤R登録0218はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録藤R登録0218です。藤R登録0218では期限切れ処理と取得時刻を採取票藤R登録0218へ残します。藤R登録0218では期限切れ処理の未実行を避けるため補助資料も照合する判断藤R登録0218です。藤R登録0218の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録藤R登録0218です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0217の設定や表示を読む前に役割を確認します。クライアントスケジュール Action 0276ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>D. 対象資源に対する働きはStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 登録対象DatabでBの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・登録・期限切・期限切れ）です。登録時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・登録・期限切・期限切れです。Actio・照合のA:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・照合・開始時・日次処理）です。復旧確認時のPolicのC:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Polic・復旧確・復旧後・ノードを）です。Storを棚卸のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・棚卸・ストレ・期限切れ）です。Dataを登録という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・登録・期限切・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0217</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0217について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2237
確認コード SP81DD0217A
画面・出力には SP81DD0217A が表示され、サーバー日次運用 Database Backup 0217 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE097
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0217B
画面・出力には SP81DD0217B が表示され、サーバー日次運用 Database Backup 0217 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 597 GB
確認コード SP81DD0217C
画面・出力には SP81DD0217C が表示され、サーバー日次運用 Database Backup 0217 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0217A が画面・出力に表示されること
② ステップ2 の SP81DD0217B が画面・出力に表示されること
③ ステップ3 の SP81DD0217C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0081"><h3>サーバー日次運用 Database Backup 0232</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>桃M確認0233ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票桃M確認0233です。桃M確認0233はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録桃M確認0233です。桃M確認0233では期限切れ処理と取得時刻を採取票桃M確認0233へ残します。桃M確認0233ではノード状態の誤読を避けるため補助資料も照合する判断桃M確認0233です。桃M確認0233の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録桃M確認0233です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0232に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Policy Set 0302の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はPolicy Domainで引継ぎ記録ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>D. 表示や設定で扱う内容はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 確認対象DatabでBの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・確認・期限切・ノード状）です。確認時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・確認・期限切・ノード状です。Polic・解析のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・解析・ディレ・ディレク）です。ポリシー時のPolicのC:は「Policy Domainで引継ぎ記録ではポリシードメインの」を述べ、対象は引継ぎ記録 DOM09（Polic・ポリシ・引継ぎ・ノードを）です。Manaを復旧のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・復旧・ドメイ・登録ドメ）です。Dataを確認という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・確認・期限切・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0232</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0232について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2252
確認コード SP81DD0232A
画面・出力には SP81DD0232A が表示され、サーバー日次運用 Database Backup 0232 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE112
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0232B
画面・出力には SP81DD0232B が表示され、サーバー日次運用 Database Backup 0232 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 612 GB
確認コード SP81DD0232C
画面・出力には SP81DD0232C が表示され、サーバー日次運用 Database Backup 0232 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0232A が画面・出力に表示されること
② ステップ2 の SP81DD0232B が画面・出力に表示されること
③ ステップ3 の SP81DD0232C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0082"><h3>サーバー日次運用 Database Backup 0247</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>茶H保護0248ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票茶H保護0248です。茶H保護0248はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録茶H保護0248です。茶H保護0248では期限切れ処理と取得時刻を採取票茶H保護0248へ残します。茶H保護0248ではプール容量不足の見落としを避けるため補助資料も照合する判断茶H保護0248です。茶H保護0248の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録茶H保護0248です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0247を保守記録に説明する必要があります。ポリシーと管理クラス Copy Group 0281と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はCopy Groupのコピーグループと取得時刻を記録し・管理クラス未割当を防ぐである。ポリシーと管理クラス Copy Group 0281固有の属性も確認対象に含める。</li><li>C. 保守作業で参照する機能はManagement Classで通常状態の確認では管理クラスのである。</li><li>D. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象DatabでAの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・保護・期限切・プール容）です。保護時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・保護・期限切・プール容です。抑止対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・抑止・コピー・管理クラ）です。通常状態時のManagのC:は「Management Classで通常状態の確認では管理クラスの」を述べ、対象は通常状態の確認 MC01（Manag・通常状・通常状・既定管理）です。ノード登録を保守のD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・保守・ノード・コピーグ）です。Dataを保護という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・保護・期限切・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0247</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0247について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2207
確認コード SP81DD0247A
画面・出力には SP81DD0247A が表示され、サーバー日次運用 Database Backup 0247 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE007
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0247B
画面・出力には SP81DD0247B が表示され、サーバー日次運用 Database Backup 0247 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 507 GB
確認コード SP81DD0247C
画面・出力には SP81DD0247C が表示され、サーバー日次運用 Database Backup 0247 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0247A が画面・出力に表示されること
② ステップ2 の SP81DD0247B が画面・出力に表示されること
③ ステップ3 の SP81DD0247C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0083"><h3>サーバー日次運用 Database Backup 0262</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>緑C照合0263ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票緑C照合0263です。緑C照合0263はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録緑C照合0263です。緑C照合0263では期限切れ処理と取得時刻を採取票緑C照合0263へ残します。緑C照合0263ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断緑C照合0263です。緑C照合0263の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録緑C照合0263です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0262の技術的な意味を資料で確認するとき、ポリシーと管理クラス Policy Domain 0320との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>B. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はBackup andでログとの照合ではコピーグループの コピーグループ照会からVersionsDataを読みである。</li><li>D. 管理対象との関係を表す説明はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 照合対象DatabでBの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・照合・期限切・データベ）です。照合時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・照合・期限切・データベです。Polic・計画のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・計画・管理ク・登録ドメ）です。ログとの時のBackuのC:は「Backup andでログとの照合ではコピーグループの」を述べ、対象はログとの照合 CG07（Backu・ログと・照合で・バックア）です。ノード登録を監査のD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・監査・ノード・登録ドメ）です。Dataを照合という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・照合・期限切・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0262</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0262について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2222
確認コード SP81DD0262A
画面・出力には SP81DD0262A が表示され、サーバー日次運用 Database Backup 0262 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE022
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0262B
画面・出力には SP81DD0262B が表示され、サーバー日次運用 Database Backup 0262 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 522 GB
確認コード SP81DD0262C
画面・出力には SP81DD0262C が表示され、サーバー日次運用 Database Backup 0262 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0262A が画面・出力に表示されること
② ステップ2 の SP81DD0262B が画面・出力に表示されること
③ ステップ3 の SP81DD0262C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0084"><h3>サーバー日次運用 Database Backup 0277</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藤R照合0278ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藤R照合0278です。藤R照合0278はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録藤R照合0278です。藤R照合0278では期限切れ処理と取得時刻を採取票藤R照合0278へ残します。藤R照合0278では期限切れ処理の未実行を避けるため補助資料も照合する判断藤R照合0278です。藤R照合0278の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録藤R照合0278です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0277について構成や状態を確認します。ポリシーと管理クラス Copy Group 0341ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは管理クラス未割当を避けるため・復旧操作で点検欄を確認するしてコピーグルーを照合する。</li><li>B. 対象資源に対する働きは期限切れ処理の未実行を避けるため・記録操作で証跡欄を照合するして期限切れ処理を照合する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはバックアップ保持値をアーカイブ保を避けるため・コピーグルーで引継ぎ記録でを確認するして引継ぎ記録でを照合する。</li><li>D. 対象資源に対する働きは管理クラス未割当を避けるため・復旧操作で点検欄を確認するしてノード登録値を照合する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 照合対象DatabでBの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・照合・期限切・期限切れ）です。照合時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・照合・期限切・期限切れです。Copy・解除のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解除・コピー・管理クラ）です。コピーグ時のBackuのC:は「Backup andで引継ぎ記録ではコピーグループの」を述べ、対象は引継ぎ記録 CG09（Backu・コピー・引継ぎ・バックア）です。ディレクを移行のD:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・移行・ノード・管理クラ）です。Dataを照合という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・照合・期限切・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0277</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0277について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2237
確認コード SP81DD0277A
画面・出力には SP81DD0277A が表示され、サーバー日次運用 Database Backup 0277 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE037
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0277B
画面・出力には SP81DD0277B が表示され、サーバー日次運用 Database Backup 0277 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 537 GB
確認コード SP81DD0277C
画面・出力には SP81DD0277C が表示され、サーバー日次運用 Database Backup 0277 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0277A が画面・出力に表示されること
② ステップ2 の SP81DD0277B が画面・出力に表示されること
③ ステップ3 の SP81DD0277C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0085"><h3>サーバー日次運用 Database Backup 0292</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>桃M抑止0293ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票桃M抑止0293です。桃M抑止0293はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録桃M抑止0293です。桃M抑止0293では期限切れ処理と取得時刻を採取票桃M抑止0293へ残します。桃M抑止0293ではノード状態の誤読を避けるため補助資料も照合する判断桃M抑止0293です。桃M抑止0293の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録桃M抑止0293です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0292の役割を調べています。サーバー日次運用 Storage Pool 0310の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は保守操作で監査欄を保存することで期限切れ処理を確認し・ノード状態の誤読を防ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容は確認操作で状態欄を整理することでストレージプを確認し・データベースバックアップ時刻を防ぐ。</li><li>C. 表示や設定で扱う内容は構成監査で構成監査ではを確認することで構成監査ではを確認し・PROTECT STGPOOを防ぐ。</li><li>D. 表示や設定で扱う内容は変更確認操作で採取欄を棚卸することでイベント結果を確認し・開始時刻誤設定を防ぐ。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 抑止対象DatabでAの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・抑止・期限切・ノード状）です。抑止時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・抑止・期限切・ノード状です。解析対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・解析・ストレ・データベ）です。構成監査時のStoraのC:は「Storage Poolで構成監査では複製・保護の」を述べ、対象は構成監査 REPL08（Stora・構成監・構成監・PROT）です。Evenを移行のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・移行・イベン・開始時刻）です。Dataを抑止という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・抑止・期限切・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0292</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0292について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2252
確認コード SP81DD0292A
画面・出力には SP81DD0292A が表示され、サーバー日次運用 Database Backup 0292 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE052
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0292B
画面・出力には SP81DD0292B が表示され、サーバー日次運用 Database Backup 0292 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 552 GB
確認コード SP81DD0292C
画面・出力には SP81DD0292C が表示され、サーバー日次運用 Database Backup 0292 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0292A が画面・出力に表示されること
② ステップ2 の SP81DD0292B が画面・出力に表示されること
③ ステップ3 の SP81DD0292C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0086"><h3>サーバー日次運用 Database Backup 0307</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>茶H解析0308ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票茶H解析0308です。茶H解析0308はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録茶H解析0308です。茶H解析0308では期限切れ処理と取得時刻を採取票茶H解析0308へ残します。茶H解析0308ではプール容量不足の見落としを避けるため補助資料も照合する判断茶H解析0308です。茶H解析0308の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録茶H解析0308です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Database Backup 0307」を「activity log 保存期間確認 監査証跡」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はプール容量不足の見落としを避けるため・採取操作で照合欄を点検するして期限切れ処理を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能は監査証跡の誤読を避けるため・監査証跡で監査証跡を確認するして監査証跡を照合する。</li><li>C. 保守作業で参照する機能は置換条件や復元先を確認せず本番フを避けるため・依存関係確認で依存関係の確を確認するして依存関係の確を照合する。</li><li>D. 保守作業で参照する機能は関連付け漏れを避けるため・主操作で出力欄を評価するしてスケジュールを照合する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象DatabでAの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・解析・期限切・プール容）です。解析時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・解析・期限切・プール容です。監査証跡対象activのB:は「サーバー操作とメッセージを追跡するログ」を述べ、対象は保存期間確認 監査証跡（activ・監査証・監査証・監査証跡）です。依存関係時のClienのC:は「Client Restoreで依存関係の確認ではリストア確認の」を述べ、対象は依存関係の確認 RST13（Clien・依存関・依存関・置換条件）です。Scheを収集のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・収集・スケジ・関連付け）です。Dataを解析という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・解析・期限切・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0307</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0307について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2207
確認コード SP81DD0307A
画面・出力には SP81DD0307A が表示され、サーバー日次運用 Database Backup 0307 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE067
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0307B
画面・出力には SP81DD0307B が表示され、サーバー日次運用 Database Backup 0307 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 567 GB
確認コード SP81DD0307C
画面・出力には SP81DD0307C が表示され、サーバー日次運用 Database Backup 0307 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0307A が画面・出力に表示されること
② ステップ2 の SP81DD0307B が画面・出力に表示されること
③ ステップ3 の SP81DD0307C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0087"><h3>サーバー日次運用 Database Backup 0322</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>緑C計画0323ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票緑C計画0323です。緑C計画0323はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録緑C計画0323です。緑C計画0323では期限切れ処理と取得時刻を採取票緑C計画0323へ残します。緑C計画0323ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断緑C計画0323です。緑C計画0323の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録緑C計画0323です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0322を同一分類のarchive copy group 容量監視 実行結果と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は実行結果の誤読を避けるため・バックアップで実行結果を確認するして実行結果を照合する。</li><li>B. 管理対象との関係を表す説明はコピーグループ未定義を避けるため・表示操作で対象欄を追跡するしてコピーグルーを照合する。</li><li>C. 管理対象との関係を表す説明は期限切れ処理の未実行を避けるため・記録操作で証跡欄を照合するしてデータベースを照合する。サーバー日次運用 Server Name 0181固有の属性も確認対象に含める。</li><li>D. 管理対象との関係を表す説明はデータベースバックアップ時刻の記を避けるため・確認操作で状態欄を整理するして期限切れ処理を照合する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 計画対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・計画・期限切・データベ）です。計画時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・計画・期限切・データベです。archi・バックアッのA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確」を述べ、対象は容量監視 実行結果（archi・バック・実行結・実行結果）です。巡回対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・巡回・コピー・コピーグ）です。収集時のServeのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Serve・収集・データ・期限切れ）です。Dataを計画という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・計画・期限切・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0322</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0322について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2222
確認コード SP81DD0322A
画面・出力には SP81DD0322A が表示され、サーバー日次運用 Database Backup 0322 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE082
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0322B
画面・出力には SP81DD0322B が表示され、サーバー日次運用 Database Backup 0322 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 582 GB
確認コード SP81DD0322C
画面・出力には SP81DD0322C が表示され、サーバー日次運用 Database Backup 0322 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0322A が画面・出力に表示されること
② ステップ2 の SP81DD0322B が画面・出力に表示されること
③ ステップ3 の SP81DD0322C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0088"><h3>サーバー日次運用 Database Backup 0337</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藤R計画0338ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藤R計画0338です。藤R計画0338はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録藤R計画0338です。藤R計画0338では期限切れ処理と取得時刻を採取票藤R計画0338へ残します。藤R計画0338では期限切れ処理の未実行を避けるため補助資料も照合する判断藤R計画0338です。藤R計画0338の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録藤R計画0338です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0337の設定や表示を読む前に役割を確認します。expiration 復元前確認 自動処理ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは自動処理の誤読を避けるため・復元前確認で自動処理を確認するして自動処理を照合する。</li><li>B. 対象資源に対する働きは失敗イベントの見落としを避けるため・監査操作で記録欄を比較するして失敗理由を照合する。クライアントスケジュール Start Time 0003固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きは開始時刻誤設定を避けるため・変更確認操作で採取欄を棚卸するしてスケジュールを照合する。</li><li>D. 対象資源に対する働きは期限切れ処理の未実行を避けるため・記録操作で証跡欄を照合するして期限切れ処理を照合する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 計画対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・計画・期限切・期限切れ）です。計画時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・計画・期限切・期限切れです。expir・復元前確認のA:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」を述べ、対象は復元前確認 自動処理（expir・復元前・自動処・自動処理）です。巡回対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・巡回・失敗理・失敗イベ）です。確認時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・確認・スケジ・開始時刻）です。Dataを計画という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・計画・期限切・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0337</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0337について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2237
確認コード SP81DD0337A
画面・出力には SP81DD0337A が表示され、サーバー日次運用 Database Backup 0337 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE097
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0337B
画面・出力には SP81DD0337B が表示され、サーバー日次運用 Database Backup 0337 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 597 GB
確認コード SP81DD0337C
画面・出力には SP81DD0337C が表示され、サーバー日次運用 Database Backup 0337 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0337A が画面・出力に表示されること
② ステップ2 の SP81DD0337B が画面・出力に表示されること
③ ステップ3 の SP81DD0337C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0089"><h3>サーバー日次運用 Database Backup 0352</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>桃M解除0353ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票桃M解除0353です。桃M解除0353はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録桃M解除0353です。桃M解除0353では期限切れ処理と取得時刻を採取票桃M解除0353へ残します。桃M解除0353ではノード状態の誤読を避けるため補助資料も照合する判断桃M解除0353です。桃M解除0353の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録桃M解除0353です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Database Backup 0352に関する障害切り分けの前提を確認しています。management class 保存期間確認 停止時刻の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は保存期間確認で停止時刻を証跡に残し・ファイルのバックアップ先や保存期間を決めるポリシー要素。</li><li>B. 表示や設定で扱う内容は巡回で関連ノードを証跡に残し・Associationの関連ノードと取得時刻を記録し。</li><li>C. 表示や設定で扱う内容は登録でドメイン割当を証跡に残し・Management Classのドメイン割当と取得時刻を記。</li><li>D. 表示や設定で扱う内容は解除で期限切れ処理を証跡に残し・Database Backupの期限切れ処理と取得時刻を記録。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 解除対象DatabでDの記述「Database Backupの期限切れ処理と取得時刻を記録し」に対応する項目はDatabase Backup（Datab・解除・期限切・ノード状）です。解除時のDatabに関するサーバー運用の仕様は「Database Backupの期限切れ処理と取得時刻を記録し」で、確認対象はData・解除・期限切・ノード状です。manag・保存期間確のA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は保存期間確認 停止時刻（manag・保存期・停止時・停止時刻）です。巡回対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・巡回・関連ノ・失敗イベ）です。登録時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・登録・ドメイ・管理クラ）です。Dataを解除という用語は「Database Backupの期限切れ処理と取得時」を指し、Database Backup（Datab・解除・期限切・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Database Backup 0352</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Database Backup 0352について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Database Backup と 期限切れ処理</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STGPOOL
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2252
確認コード SP81DD0352A
画面・出力には SP81DD0352A が表示され、サーバー日次運用 Database Backup 0352 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE112
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0352B
画面・出力には SP81DD0352B が表示され、サーバー日次運用 Database Backup 0352 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Database Backup を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 612 GB
確認コード SP81DD0352C
画面・出力には SP81DD0352C が表示され、サーバー日次運用 Database Backup 0352 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0352A が画面・出力に表示されること
② ステップ2 の SP81DD0352B が画面・出力に表示されること
③ ステップ3 の SP81DD0352C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0090"><h3>サーバー日次運用 Expiration Status 0004</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>紅E巡回0005ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紅E巡回0005です。紅E巡回0005はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録紅E巡回0005です。紅E巡回0005ではノード登録と取得時刻を採取票紅E巡回0005へ残します。紅E巡回0005ではノード状態の誤読を避けるため補助資料も照合する判断紅E巡回0005です。紅E巡回0005の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録紅E巡回0005です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0004の役割を調べています。クライアントスケジュール Event Status 0057の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>B. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>D. 表示や設定で扱う内容はManagement Classで再始動後の確認では管理クラスの オプション確認からDIRMCを読みである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 巡回対象ExpirでBの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・巡回・ノード登）です。サーバに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・巡回・ノード登です。Event・復旧のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・復旧・イベント）です。照合時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・照合・運用状態）です。Manaを再始動確認のD:は「Management Classで再始動後の確認では管理クラスの」を述べ、対象は再始動後の確認 MC15（Manage・再始動・再始動後）です。Expiを巡回という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・巡回・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0004</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0004について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2204
確認コード SP81DD0004A
画面・出力には SP81DD0004A が表示され、サーバー日次運用 Expiration Status 0004 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE004
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0004B
画面・出力には SP81DD0004B が表示され、サーバー日次運用 Expiration Status 0004 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 504 GB
確認コード SP81DD0004C
画面・出力には SP81DD0004C が表示され、サーバー日次運用 Expiration Status 0004 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0004A が画面・出力に表示されること
② ステップ2 の SP81DD0004B が画面・出力に表示されること
③ ステップ3 の SP81DD0004C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0091"><h3>サーバー日次運用 Expiration Status 0019</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>空T巡回0020ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票空T巡回0020です。空T巡回0020はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録空T巡回0020です。空T巡回0020ではノード登録と取得時刻を採取票空T巡回0020へ残します。空T巡回0020ではプール容量不足の見落としを避けるため補助資料も照合する判断空T巡回0020です。空T巡回0020の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録空T巡回0020です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Expiration Status 0019」を「ポリシーと管理クラス Policy Domain 0110」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はCopy Groupのコピーグループと取得時刻を記録し・管理クラス未割当を防ぐである。ポリシーと管理クラス Copy Group 0281固有の属性も確認対象に含める。</li><li>D. 保守作業で参照する機能はDirectory-containeで停止前の確認ではストレージプールのである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 巡回対象ExpirでBの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・巡回・ノード登）です。サーバに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・巡回・ノード登です。Polic・移行のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・移行・管理クラ）です。抑止時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・抑止・コピーグ）です。Direを停止確認のD:は「Directory-containeで停止前の確認ではストレージプー」を述べ、対象は停止前の確認 POOL14（Direct・停止確・停止前の）です。Expiを巡回という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・巡回・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0019</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0019について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2219
確認コード SP81DD0019A
画面・出力には SP81DD0019A が表示され、サーバー日次運用 Expiration Status 0019 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE019
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0019B
画面・出力には SP81DD0019B が表示され、サーバー日次運用 Expiration Status 0019 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 519 GB
確認コード SP81DD0019C
画面・出力には SP81DD0019C が表示され、サーバー日次運用 Expiration Status 0019 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0019A が画面・出力に表示されること
② ステップ2 の SP81DD0019B が画面・出力に表示されること
③ ステップ3 の SP81DD0019C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0092"><h3>サーバー日次運用 Expiration Status 0034</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>翠O棚卸0035ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票翠O棚卸0035です。翠O棚卸0035はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録翠O棚卸0035です。翠O棚卸0035ではノード登録と取得時刻を採取票翠O棚卸0035へ残します。翠O棚卸0035ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断翠O棚卸0035です。翠O棚卸0035の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録翠O棚卸0035です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0034を同一分類のサーバー日次運用 Storage Pool 0130と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>C. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 管理対象との関係を表す説明はManagement Classで代替経路の確認では管理クラスのである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 棚卸対象ExpirでAの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・棚卸・ノード登）です。棚卸時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・棚卸・ノード登です。診断対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・診断・ストレー）です。解析時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・解析・関連ノー）です。Manaを代替経路確のD:は「Management Classで代替経路の確認では管理クラスの」を述べ、対象は代替経路の確認 MC10（Manage・代替経・代替経路）です。Expiを棚卸という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・棚卸・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0034</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0034について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2234
確認コード SP81DD0034A
画面・出力には SP81DD0034A が表示され、サーバー日次運用 Expiration Status 0034 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE034
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0034B
画面・出力には SP81DD0034B が表示され、サーバー日次運用 Expiration Status 0034 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 534 GB
確認コード SP81DD0034C
画面・出力には SP81DD0034C が表示され、サーバー日次運用 Expiration Status 0034 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0034A が画面・出力に表示されること
② ステップ2 の SP81DD0034B が画面・出力に表示されること
③ ステップ3 の SP81DD0034C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0093"><h3>サーバー日次運用 Expiration Status 0049</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>朱J復旧0050ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票朱J復旧0050です。朱J復旧0050はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録朱J復旧0050です。朱J復旧0050ではノード登録と取得時刻を採取票朱J復旧0050へ残します。朱J復旧0050では期限切れ処理の未実行を避けるため補助資料も照合する判断朱J復旧0050です。朱J復旧0050の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録朱J復旧0050です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0049の設定や表示を読む前に役割を確認します。サーバー日次運用 Node Name 0073ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはDirectory-containeで代替経路の確認ではストレージプールのである。ストレージプール Directory-container固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧対象ExpirでCの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・復旧・ノード登）です。復旧時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・復旧・ノード登です。Node・監査のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・監査・運用状態）です。保護対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護・失敗理由）です。Direを代替経路確のD:は「Directory-containeで代替経路の確認ではストレージプ」を述べ、対象は代替経路の確認 POOL10（Direct・代替経・代替経路）です。Expiを復旧という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・復旧・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0049</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0049について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2249
確認コード SP81DD0049A
画面・出力には SP81DD0049A が表示され、サーバー日次運用 Expiration Status 0049 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE049
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0049B
画面・出力には SP81DD0049B が表示され、サーバー日次運用 Expiration Status 0049 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 549 GB
確認コード SP81DD0049C
画面・出力には SP81DD0049C が表示され、サーバー日次運用 Expiration Status 0049 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0049A が画面・出力に表示されること
② ステップ2 の SP81DD0049B が画面・出力に表示されること
③ ステップ3 の SP81DD0049C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0094"><h3>サーバー日次運用 Expiration Status 0064</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>紅E監査0065ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紅E監査0065です。紅E監査0065はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録紅E監査0065です。紅E監査0065ではノード登録と取得時刻を採取票紅E監査0065へ残します。紅E監査0065ではノード状態の誤読を避けるため補助資料も照合する判断紅E監査0065です。紅E監査0065の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録紅E監査0065です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0064に関する障害切り分けの前提を確認しています。クライアントスケジュール Event Status 0072の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 表示や設定で扱う内容はCopy Groupのコピーグループと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 表示や設定で扱う内容はBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。</li><li>D. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・監査・ノード登）です。監査時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・監査・ノード登です。Event・監査のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・監査・イベント）です。抑止対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・抑止・コピーグ）です。構成監査時のBackuのC:は「Backup andで構成監査ではコピーグループの」を述べ、対象は構成監査 CG08（Backup・構成監・構成監査）です。Expiを監査という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・監査・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0064</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0064について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2204
確認コード SP81DD0064A
画面・出力には SP81DD0064A が表示され、サーバー日次運用 Expiration Status 0064 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE064
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0064B
画面・出力には SP81DD0064B が表示され、サーバー日次運用 Expiration Status 0064 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 564 GB
確認コード SP81DD0064C
画面・出力には SP81DD0064C が表示され、サーバー日次運用 Expiration Status 0064 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0064A が画面・出力に表示されること
② ステップ2 の SP81DD0064B が画面・出力に表示されること
③ ステップ3 の SP81DD0064C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0095"><h3>サーバー日次運用 Expiration Status 0079</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>空T監査0080ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票空T監査0080です。空T監査0080はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録空T監査0080です。空T監査0080ではノード登録と取得時刻を採取票空T監査0080へ残します。空T監査0080ではプール容量不足の見落としを避けるため補助資料も照合する判断空T監査0080です。空T監査0080の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録空T監査0080です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0079を保守記録に説明する必要があります。ポリシーと管理クラス Policy Domain 0125と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>B. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はバックアップや管理コマンドを決めた時刻に実行する定義である。</li><li>D. 保守作業で参照する機能はIncremental Backupで変更前の確認ではバックアップ運用のである。バックアップ運用 Incremental Backup 変更前の確認固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査対象ExpirでBの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・監査・ノード登）です。監査時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・監査・ノード登です。Polic・診断のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・診断・管理クラ）です。復旧手掛時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義」を述べ、対象は状態確認 復旧手掛かり（schedu・復旧手・復旧手掛）です。Incrを変更確認のD:は「Incremental Backupで変更前の確認ではバックアップ運」を述べ、対象は変更前の確認 BKP02（Increm・変更確・変更前の）です。Expiを監査という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・監査・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0079</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0079について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2219
確認コード SP81DD0079A
画面・出力には SP81DD0079A が表示され、サーバー日次運用 Expiration Status 0079 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE079
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0079B
画面・出力には SP81DD0079B が表示され、サーバー日次運用 Expiration Status 0079 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 579 GB
確認コード SP81DD0079C
画面・出力には SP81DD0079C が表示され、サーバー日次運用 Expiration Status 0079 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0079A が画面・出力に表示されること
② ステップ2 の SP81DD0079B が画面・出力に表示されること
③ ステップ3 の SP81DD0079C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0096"><h3>サーバー日次運用 Expiration Status 0094</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>翠O変更0095ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票翠O変更0095です。翠O変更0095はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録翠O変更0095です。翠O変更0095ではノード登録と取得時刻を採取票翠O変更0095へ残します。翠O変更0095ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断翠O変更0095です。翠O変更0095の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録翠O変更0095です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0094の技術的な意味を資料で確認するとき、ポリシーと管理クラス DIRMC 0113との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。ポリシーと管理クラス DIRMC 0113固有の属性も確認対象に含める。</li><li>B. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はサーバーへ登録されたクライアントを表す管理単位を復元前確認する。</li><li>D. 管理対象との関係を表す説明はClient Nodeで停止前の確認ではノード管理の 占有量照会からLogicalFilesを読みである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更対象ExpirでBの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・変更・ノード登）です。変更時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・変更・ノード登です。移行対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・移行・ノード登）です。復元前確時のnodeのC:は「サーバーへ登録されたクライアントを表す管理単位を復元前確認する」を述べ、対象は復元前確認 応答行（node・復元前・応答行）です。Clieを停止確認のD:は「Client Nodeで停止前の確認ではノード管理の」を述べ、対象は停止前の確認 NODE14（Client・停止確・停止前の）です。Expiを変更という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・変更・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0094</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0094について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2234
確認コード SP81DD0094A
画面・出力には SP81DD0094A が表示され、サーバー日次運用 Expiration Status 0094 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE094
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0094B
画面・出力には SP81DD0094B が表示され、サーバー日次運用 Expiration Status 0094 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 594 GB
確認コード SP81DD0094C
画面・出力には SP81DD0094C が表示され、サーバー日次運用 Expiration Status 0094 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0094A が画面・出力に表示されること
② ステップ2 の SP81DD0094B が画面・出力に表示されること
③ ステップ3 の SP81DD0094C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0097"><h3>サーバー日次運用 Expiration Status 0109</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>朱J移行0110ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票朱J移行0110です。朱J移行0110はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録朱J移行0110です。朱J移行0110ではノード登録と取得時刻を採取票朱J移行0110へ残します。朱J移行0110では期限切れ処理の未実行を避けるため補助資料も照合する判断朱J移行0110です。朱J移行0110の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録朱J移行0110です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0109について構成や状態を確認します。ポリシーと管理クラス Management Class 0194ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 対象資源に対する働きはCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 対象資源に対する働きはStorage Poolで通常状態の確認では複製・保護の プール保護からANR0984Iを読みである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 移行対象ExpirでAの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expira・移行・ノード登）です。移行時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpir・移行・ノード登です。収集対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・収集・ドメイン）です。計画時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・計画・コピーグ）です。Storを通常状態確のD:は「Storage Poolで通常状態の確認では複製・保護の」を述べ、対象は通常状態の確認 REPL01（Storag・通常状・通常状態）です。Expiを移行という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expira・移行・ノード登）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0109</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0109について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2249
確認コード SP81DD0109A
画面・出力には SP81DD0109A が表示され、サーバー日次運用 Expiration Status 0109 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE109
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0109B
画面・出力には SP81DD0109B が表示され、サーバー日次運用 Expiration Status 0109 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 609 GB
確認コード SP81DD0109C
画面・出力には SP81DD0109C が表示され、サーバー日次運用 Expiration Status 0109 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0109A が画面・出力に表示されること
② ステップ2 の SP81DD0109B が画面・出力に表示されること
③ ステップ3 の SP81DD0109C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0098"><h3>サーバー日次運用 Expiration Status 0124</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>紅E診断0125ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紅E診断0125です。紅E診断0125はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録紅E診断0125です。紅E診断0125ではノード登録と取得時刻を採取票紅E診断0125へ残します。紅E診断0125ではノード状態の誤読を避けるため補助資料も照合する判断紅E診断0125です。紅E診断0125の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録紅E診断0125です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0124の役割を調べています。クライアントスケジュール Event Status 0132の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 表示や設定で扱う内容はバックアップや管理コマンドを決めた時刻に実行する定義を容量監視として確認する。schedule 容量監視 履歴行固有の属性も確認対象に含める。</li><li>C. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はArchive Operationで通常状態の確認ではアーカイブ運用のである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 診断対象ExpirでCの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・診断・ノード・ノード状）です。診断時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・診断・ノード・ノード状です。Event・診断のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・診断・イベン・日次処理）です。ノード対象schedのB:は「バックアップや管理コマンドを決めた時刻に実行する定義を容量監視として」を述べ、対象は容量監視 履歴行（sched・ノード・履歴行・履歴行の）です。Archを通常状態確のD:は「Archive Operationで通常状態の確認ではアーカイブ運用」を述べ、対象は通常状態の確認 ARC01（Archi・通常状・確認で・バックア）です。Expiを診断という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・診断・ノード・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0124</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0124について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2204
確認コード SP81DD0124A
画面・出力には SP81DD0124A が表示され、サーバー日次運用 Expiration Status 0124 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE004
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0124B
画面・出力には SP81DD0124B が表示され、サーバー日次運用 Expiration Status 0124 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 504 GB
確認コード SP81DD0124C
画面・出力には SP81DD0124C が表示され、サーバー日次運用 Expiration Status 0124 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0124A が画面・出力に表示されること
② ステップ2 の SP81DD0124B が画面・出力に表示されること
③ ステップ3 の SP81DD0124C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0099"><h3>サーバー日次運用 Expiration Status 0139</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>空T診断0140ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票空T診断0140です。空T診断0140はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録空T診断0140です。空T診断0140ではノード登録と取得時刻を採取票空T診断0140へ残します。空T診断0140ではプール容量不足の見落としを避けるため補助資料も照合する判断空T診断0140です。空T診断0140の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録空T診断0140です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Expiration Status 0139」を「ポリシーと管理クラス Copy Group 0176」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。ポリシーと管理クラス Copy Group 0176固有の属性も確認対象に含める。</li><li>B. 保守作業で参照する機能はEvent Statusのイベント結果と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 保守作業で参照する機能はArchive Operationで停止前の確認ではアーカイブ運用のである。</li><li>D. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 診断対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・診断・ノード・プール容）です。診断時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・診断・ノード・プール容です。Copy・切替のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・切替・コピー・登録ドメ）です。解除対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・解除・イベン・開始時刻）です。停止確認時のArchiのC:は「Archive Operationで停止前の確認ではアーカイブ運用の」を述べ、対象は停止前の確認 ARC14（Archi・停止確・停止前・バックア）です。Expiを診断という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・診断・ノード・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0139</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0139について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2219
確認コード SP81DD0139A
画面・出力には SP81DD0139A が表示され、サーバー日次運用 Expiration Status 0139 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE019
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0139B
画面・出力には SP81DD0139B が表示され、サーバー日次運用 Expiration Status 0139 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 519 GB
確認コード SP81DD0139C
画面・出力には SP81DD0139C が表示され、サーバー日次運用 Expiration Status 0139 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0139A が画面・出力に表示されること
② ステップ2 の SP81DD0139B が画面・出力に表示されること
③ ステップ3 の SP81DD0139C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0100"><h3>サーバー日次運用 Expiration Status 0154</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>翠O保守0155ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票翠O保守0155です。翠O保守0155はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録翠O保守0155です。翠O保守0155ではノード登録と取得時刻を採取票翠O保守0155へ残します。翠O保守0155ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断翠O保守0155です。翠O保守0155の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録翠O保守0155です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0154を同一分類のクライアントスケジュール Action 0156と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Action 0156固有の属性も確認対象に含める。</li><li>C. 管理対象との関係を表す説明はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保守対象ExpirでAの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・保守・ノード・データベ）です。保守時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・保守・ノード・データベです。保守対象ActioのB:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・保守・開始時・日次処理）です。解除時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解除・コピー・登録ドメ）です。Assoを復旧のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・復旧・関連ノ・関連付け）です。Expiを保守という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・保守・ノード・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0154</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0154について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2234
確認コード SP81DD0154A
画面・出力には SP81DD0154A が表示され、サーバー日次運用 Expiration Status 0154 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE034
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0154B
画面・出力には SP81DD0154B が表示され、サーバー日次運用 Expiration Status 0154 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 534 GB
確認コード SP81DD0154C
画面・出力には SP81DD0154C が表示され、サーバー日次運用 Expiration Status 0154 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0154A が画面・出力に表示されること
② ステップ2 の SP81DD0154B が画面・出力に表示されること
③ ステップ3 の SP81DD0154C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0101"><h3>サーバー日次運用 Expiration Status 0169</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>朱J切替0170ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票朱J切替0170です。朱J切替0170はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録朱J切替0170です。朱J切替0170ではノード登録と取得時刻を採取票朱J切替0170へ残します。朱J切替0170では期限切れ処理の未実行を避けるため補助資料も照合する判断朱J切替0170です。朱J切替0170の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録朱J切替0170です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0169の設定や表示を読む前に役割を確認します。サーバー日次運用 Node Name 0208ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>C. 対象資源に対する働きはPolicy Domainで停止前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。</li><li>D. 対象資源に対する働きはStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 切替対象ExpirでAの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・切替・ノード・期限切れ）です。切替時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・切替・ノード・期限切れです。登録対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・登録・運用状・ノード状）です。停止確認時のPolicのC:は「Policy Domainで停止前の確認ではポリシードメインの」を述べ、対象は停止前の確認 DOM14（Polic・停止確・確認で・ノードを）です。Storを巡回のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・巡回・ストレ・データベ）です。Expiを切替という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・切替・ノード・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0169</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0169について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2249
確認コード SP81DD0169A
画面・出力には SP81DD0169A が表示され、サーバー日次運用 Expiration Status 0169 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE049
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0169B
画面・出力には SP81DD0169B が表示され、サーバー日次運用 Expiration Status 0169 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 549 GB
確認コード SP81DD0169C
画面・出力には SP81DD0169C が表示され、サーバー日次運用 Expiration Status 0169 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0169A が画面・出力に表示されること
② ステップ2 の SP81DD0169B が画面・出力に表示されること
③ ステップ3 の SP81DD0169C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0102"><h3>サーバー日次運用 Expiration Status 0184</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>紅E収集0185ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紅E収集0185です。紅E収集0185はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録紅E収集0185です。紅E収集0185ではノード登録と取得時刻を採取票紅E収集0185へ残します。紅E収集0185ではノード状態の誤読を避けるため補助資料も照合する判断紅E収集0185です。紅E収集0185の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録紅E収集0185です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0184に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Management Class 0194の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 表示や設定で扱う内容はPolicy Domainで復旧準備ではポリシードメインの ポリシーセットからPolicySetを読みである。</li><li>C. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集対象ExpirでCの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・収集・ノード・ノード状）です。収集時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・収集・ノード・ノード状です。Manag・収集のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・収集・ドメイ・ディレク）です。復旧準備対象PolicのB:は「Policy Domainで復旧準備ではポリシードメインの」を述べ、対象は復旧準備 DOM05（Polic・復旧準・復旧準・ノードを）です。Dataを変更のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・変更・期限切・データベ）です。Expiを収集という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・収集・ノード・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0184</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0184について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2204
確認コード SP81DD0184A
画面・出力には SP81DD0184A が表示され、サーバー日次運用 Expiration Status 0184 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE064
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0184B
画面・出力には SP81DD0184B が表示され、サーバー日次運用 Expiration Status 0184 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 564 GB
確認コード SP81DD0184C
画面・出力には SP81DD0184C が表示され、サーバー日次運用 Expiration Status 0184 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0184A が画面・出力に表示されること
② ステップ2 の SP81DD0184B が画面・出力に表示されること
③ ステップ3 の SP81DD0184C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0103"><h3>サーバー日次運用 Expiration Status 0199</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>空T収集0200ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票空T収集0200です。空T収集0200はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録空T収集0200です。空T収集0200ではノード登録と取得時刻を採取票空T収集0200へ残します。空T収集0200ではプール容量不足の見落としを避けるため補助資料も照合する判断空T収集0200です。空T収集0200の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録空T収集0200です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0199を保守記録に説明する必要があります。ポリシーと管理クラス Management Class 0239と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>B. 保守作業で参照する機能はアーカイブコピーの保存期間と宛先を定めるコピー規則である。archive copy group 状態確認 集約装置固有の属性も確認対象に含める。</li><li>C. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集対象ExpirでCの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・収集・ノード・プール容）です。収集時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・収集・ノード・プール容です。Manag・確認のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・確認・ドメイ・コピーグ）です。状態確認対象archiのB:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は状態確認 集約装置（archi・状態確・集約装・集約装置）です。Assoを棚卸のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・棚卸・関連ノ・開始時刻）です。Expiを収集という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・収集・ノード・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0199</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0199について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2219
確認コード SP81DD0199A
画面・出力には SP81DD0199A が表示され、サーバー日次運用 Expiration Status 0199 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE079
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0199B
画面・出力には SP81DD0199B が表示され、サーバー日次運用 Expiration Status 0199 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 579 GB
確認コード SP81DD0199C
画面・出力には SP81DD0199C が表示され、サーバー日次運用 Expiration Status 0199 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0199A が画面・出力に表示されること
② ステップ2 の SP81DD0199B が画面・出力に表示されること
③ ステップ3 の SP81DD0199C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0104"><h3>サーバー日次運用 Expiration Status 0214</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>翠O登録0215ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票翠O登録0215です。翠O登録0215はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録翠O登録0215です。翠O登録0215ではノード登録と取得時刻を採取票翠O登録0215へ残します。翠O登録0215ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断翠O登録0215です。翠O登録0215の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録翠O登録0215です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0214の技術的な意味を資料で確認するとき、ポリシーと管理クラス Management Class 0254との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>C. 管理対象との関係を表す説明はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。backup copy group コマンド証跡 収集装置固有の属性も確認対象に含める。</li><li>D. 管理対象との関係を表す説明はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 登録対象ExpirでAの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・登録・ノード・データベ）です。登録時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・登録・ノード・データベです。保護対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・保護・ドメイ・ディレク）です。ポリシー時のbackuのC:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backu・ポリシ・収集装・収集装置）です。Poliを変更のD:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・変更・管理ク・登録ドメ）です。Expiを登録という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・登録・ノード・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0214</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0214について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2234
確認コード SP81DD0214A
画面・出力には SP81DD0214A が表示され、サーバー日次運用 Expiration Status 0214 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE094
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0214B
画面・出力には SP81DD0214B が表示され、サーバー日次運用 Expiration Status 0214 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 594 GB
確認コード SP81DD0214C
画面・出力には SP81DD0214C が表示され、サーバー日次運用 Expiration Status 0214 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0214A が画面・出力に表示されること
② ステップ2 の SP81DD0214B が画面・出力に表示されること
③ ステップ3 の SP81DD0214C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0105"><h3>サーバー日次運用 Expiration Status 0229</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>朱J確認0230ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票朱J確認0230です。朱J確認0230はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録朱J確認0230です。朱J確認0230ではノード登録と取得時刻を採取票朱J確認0230へ残します。朱J確認0230では期限切れ処理の未実行を避けるため補助資料も照合する判断朱J確認0230です。朱J確認0230の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録朱J確認0230です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0229について構成や状態を確認します。クライアントスケジュール Event Status 0312ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 対象資源に対する働きはClient Nodeで復旧準備ではノード管理の 占有量照会からLogicalFilesを読みである。</li><li>C. 対象資源に対する働きはStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>D. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 確認対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・確認・ノード・期限切れ）です。確認時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・確認・ノード・期限切れです。Event・解析のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・解析・イベン・日次処理）です。復旧準備対象ClienのB:は「Client Nodeで復旧準備ではノード管理の」を述べ、対象は復旧準備 NODE05（Clien・復旧準・復旧準・長期未接）です。変更時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・変更・ストレ・期限切れ）です。Expiを確認という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・確認・ノード・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0229</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0229について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2249
確認コード SP81DD0229A
画面・出力には SP81DD0229A が表示され、サーバー日次運用 Expiration Status 0229 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE109
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0229B
画面・出力には SP81DD0229B が表示され、サーバー日次運用 Expiration Status 0229 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 609 GB
確認コード SP81DD0229C
画面・出力には SP81DD0229C が表示され、サーバー日次運用 Expiration Status 0229 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0229A が画面・出力に表示されること
② ステップ2 の SP81DD0229B が画面・出力に表示されること
③ ステップ3 の SP81DD0229C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0106"><h3>サーバー日次運用 Expiration Status 0244</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>紅E保護0245ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紅E保護0245です。紅E保護0245はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録紅E保護0245です。紅E保護0245ではノード登録と取得時刻を採取票紅E保護0245へ残します。紅E保護0245ではノード状態の誤読を避けるため補助資料も照合する判断紅E保護0245です。紅E保護0245の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録紅E保護0245です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0244の役割を調べています。クライアントスケジュール Event Status 0267の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>B. 表示や設定で扱う内容はDirectory-containeで通常状態の確認ではストレージプールのである。</li><li>C. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象ExpirでCの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・保護・ノード・ノード状）です。保護時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・保護・ノード・ノード状です。Event・照合のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・照合・イベン・失敗イベ）です。通常状態対象DirecのB:は「Directory-containeで通常状態の確認ではストレージプ」を述べ、対象は通常状態の確認 POOL01（Direc・通常状・通常状・容量使用）です。Poliを変更のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・変更・ディレ・登録ドメ）です。Expiを保護という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・保護・ノード・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0244</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0244について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2204
確認コード SP81DD0244A
画面・出力には SP81DD0244A が表示され、サーバー日次運用 Expiration Status 0244 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE004
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0244B
画面・出力には SP81DD0244B が表示され、サーバー日次運用 Expiration Status 0244 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 504 GB
確認コード SP81DD0244C
画面・出力には SP81DD0244C が表示され、サーバー日次運用 Expiration Status 0244 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0244A が画面・出力に表示されること
② ステップ2 の SP81DD0244B が画面・出力に表示されること
③ ステップ3 の SP81DD0244C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0107"><h3>サーバー日次運用 Expiration Status 0259</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>空T保護0260ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票空T保護0260です。空T保護0260はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録空T保護0260です。空T保護0260ではノード登録と取得時刻を採取票空T保護0260へ残します。空T保護0260ではプール容量不足の見落としを避けるため補助資料も照合する判断空T保護0260です。空T保護0260の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録空T保護0260です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Expiration Status 0259」を「ポリシーと管理クラス DIRMC 0338」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 保守作業で参照する機能はClient Nodeで再始動後の確認ではノード管理の 関連付けからAssociatedNodeを読みである。</li><li>C. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象ExpirでCの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・保護・ノード・プール容）です。保護時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・保護・ノード・プール容です。計画対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・計画・ノード・ディレク）です。再始動確対象ClienのB:は「Client Nodeで再始動後の確認ではノード管理の」を述べ、対象は再始動後の確認 NODE15（Clien・再始動・再始動・長期未接）です。Actiを診断のD:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Actio・診断・開始時・開始時刻）です。Expiを保護という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・保護・ノード・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0259</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0259について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2219
確認コード SP81DD0259A
画面・出力には SP81DD0259A が表示され、サーバー日次運用 Expiration Status 0259 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE019
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0259B
画面・出力には SP81DD0259B が表示され、サーバー日次運用 Expiration Status 0259 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 519 GB
確認コード SP81DD0259C
画面・出力には SP81DD0259C が表示され、サーバー日次運用 Expiration Status 0259 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0259A が画面・出力に表示されること
② ステップ2 の SP81DD0259B が画面・出力に表示されること
③ ステップ3 の SP81DD0259C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0108"><h3>サーバー日次運用 Expiration Status 0274</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>翠O照合0275ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票翠O照合0275です。翠O照合0275はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録翠O照合0275です。翠O照合0275ではノード登録と取得時刻を採取票翠O照合0275へ残します。翠O照合0275ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断翠O照合0275です。翠O照合0275の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録翠O照合0275です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0274を同一分類のクライアントスケジュール Action 0336と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。照合操作で確認欄を採取するときは日次処理順序の誤読を防ぐ。</li><li>B. 管理対象との関係を表す説明はStorage Poolで障害切り分けでは複製・保護の プール保護からANR0984Iを読み・複製である。複製・保護で障害切り分けを確認するときはPROTECT STGPOOを防ぐ。</li><li>C. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。復旧操作で点検欄を確認するときは管理クラス未割当を防ぐ。</li><li>D. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。確認操作で状態欄を整理するときはデータベースバックアップ時刻を防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 照合対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・照合・ノード・データベ）です。照合時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・照合・ノード・データベです。Actio・計画のA:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・計画・開始時・日次処理）です。複製対象StoraのB:は「Storage Poolで障害切り分けでは複製・保護の」を述べ、対象は障害切り分け REPL04（Stora・複製・障害切・PROT）です。保守時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・保守・ドメイ・管理クラ）です。Expiを照合という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・照合・ノード・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0274</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0274について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2234
確認コード SP81DD0274A
画面・出力には SP81DD0274A が表示され、サーバー日次運用 Expiration Status 0274 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE034
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0274B
画面・出力には SP81DD0274B が表示され、サーバー日次運用 Expiration Status 0274 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 534 GB
確認コード SP81DD0274C
画面・出力には SP81DD0274C が表示され、サーバー日次運用 Expiration Status 0274 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0274A が画面・出力に表示されること
② ステップ2 の SP81DD0274B が画面・出力に表示されること
③ ステップ3 の SP81DD0274C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0109"><h3>サーバー日次運用 Expiration Status 0289</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>朱J抑止0290ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票朱J抑止0290です。朱J抑止0290はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録朱J抑止0290です。朱J抑止0290ではノード登録と取得時刻を採取票朱J抑止0290へ残します。朱J抑止0290では期限切れ処理の未実行を避けるため補助資料も照合する判断朱J抑止0290です。朱J抑止0290の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録朱J抑止0290です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0289の設定や表示を読む前に役割を確認します。ポリシーと管理クラス Copy Group 0356ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは登録ドメインの取り違えを防ぐ。</li><li>B. 対象資源に対する働きはDirectory-containeで停止前の確認ではストレージプールのである。停止確認で停止前の確認を確認するときは容量使用率と損傷データ件数をを防ぐ。ストレージプール Directory-container固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きはDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。復旧操作で点検欄を確認するときは管理クラス未割当を防ぐ。</li><li>D. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。記録操作で証跡欄を照合するときは期限切れ処理の未実行を防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 抑止対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・抑止・ノード・期限切れ）です。抑止時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・抑止・ノード・期限切れです。Copy・解除のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解除・コピー・登録ドメ）です。停止確認対象DirecのB:は「Directory-containeで停止前の確認ではストレージプー」を述べ、対象は停止前の確認 POOL14（Direc・停止確・停止前・容量使用）です。移行時のディレクトのC:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・移行・ノード・管理クラ）です。Expiを抑止という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・抑止・ノード・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0289</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0289について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2249
確認コード SP81DD0289A
画面・出力には SP81DD0289A が表示され、サーバー日次運用 Expiration Status 0289 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE049
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0289B
画面・出力には SP81DD0289B が表示され、サーバー日次運用 Expiration Status 0289 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 549 GB
確認コード SP81DD0289C
画面・出力には SP81DD0289C が表示され、サーバー日次運用 Expiration Status 0289 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0289A が画面・出力に表示されること
② ステップ2 の SP81DD0289B が画面・出力に表示されること
③ ステップ3 の SP81DD0289C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0110"><h3>サーバー日次運用 Expiration Status 0304</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>紅E解析0305ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紅E解析0305です。紅E解析0305はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録紅E解析0305です。紅E解析0305ではノード登録と取得時刻を採取票紅E解析0305へ残します。紅E解析0305ではノード状態の誤読を避けるため補助資料も照合する判断紅E解析0305です。紅E解析0305の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録紅E解析0305です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0304に関する障害切り分けの前提を確認しています。policy domain 期限切れ確認 容量表示の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は容量表示で容量表示を証跡に残し・クライアントに適用するバックアップとアーカイブの規則を束ねる。</li><li>B. 表示や設定で扱う内容は変更確認で変更後の確認を証跡に残し・DBで変更後の確認ではサーバーの 履歴照会からBACKUPF。</li><li>C. 表示や設定で扱う内容は保守で期限切れ処理を証跡に残し・Database Backupの期限切れ処理と取得時刻を記録。</li><li>D. 表示や設定で扱う内容は解析でノード登録を証跡に残し・Expiration Statusのノード登録と取得時刻を記。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・解析・ノード・ノード状）です。解析時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・解析・ノード・ノード状です。polic・容量表示のA:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」を述べ、対象は期限切れ確認 容量表示（polic・容量表・容量表・容量表示）です。変更確認対象データベーのB:は「DBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを」を述べ、対象は変更後の確認 DBBK03（データベー・変更確・変更後・データベ）です。保守時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・保守・期限切・データベ）です。Expiを解析という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・解析・ノード・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0304</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0304について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2204
確認コード SP81DD0304A
画面・出力には SP81DD0304A が表示され、サーバー日次運用 Expiration Status 0304 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE064
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0304B
画面・出力には SP81DD0304B が表示され、サーバー日次運用 Expiration Status 0304 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 564 GB
確認コード SP81DD0304C
画面・出力には SP81DD0304C が表示され、サーバー日次運用 Expiration Status 0304 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0304A が画面・出力に表示されること
② ステップ2 の SP81DD0304B が画面・出力に表示されること
③ ステップ3 の SP81DD0304C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0111"><h3>サーバー日次運用 Expiration Status 0319</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>空T解析0320ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票空T解析0320です。空T解析0320はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録空T解析0320です。空T解析0320ではノード登録と取得時刻を採取票空T解析0320へ残します。空T解析0320ではプール容量不足の見落としを避けるため補助資料も照合する判断空T解析0320です。空T解析0320の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録空T解析0320です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0319を保守記録に説明する必要があります。クライアントスケジュール Event Status 0327と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は失敗イベントの見落としを避けるため・監査操作で記録欄を比較するしてイベント結果を照合する。</li><li>B. 保守作業で参照する機能はプール容量不足の見落としを避けるため・採取操作で照合欄を点検するしてノード登録を照合する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はデータベースバックアップ媒体とボを避けるため・依存関係確認で依存関係の確を確認するして依存関係の確を照合する。</li><li>D. 保守作業で参照する機能は期限切れ処理の未実行を避けるため・記録操作で証跡欄を照合するして運用状態を照合する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象ExpirでBの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・解析・ノード・プール容）です。解析時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・解析・ノード・プール容です。Event・計画のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・計画・イベン・失敗イベ）です。依存関係時のデータベーのC:は「DBで依存関係の確認ではサーバーの DB状態からLastDataba」を述べ、対象は依存関係の確認 DBBK13（データベー・依存関・依存関・データベ）です。Nodeを収集のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・収集・運用状・期限切れ）です。Expiを解析という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・解析・ノード・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0319</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0319について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2219
確認コード SP81DD0319A
画面・出力には SP81DD0319A が表示され、サーバー日次運用 Expiration Status 0319 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE079
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0319B
画面・出力には SP81DD0319B が表示され、サーバー日次運用 Expiration Status 0319 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 579 GB
確認コード SP81DD0319C
画面・出力には SP81DD0319C が表示され、サーバー日次運用 Expiration Status 0319 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0319A が画面・出力に表示されること
② ステップ2 の SP81DD0319B が画面・出力に表示されること
③ ステップ3 の SP81DD0319C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0112"><h3>サーバー日次運用 Expiration Status 0334</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>翠O計画0335ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票翠O計画0335です。翠O計画0335はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録翠O計画0335です。翠O計画0335ではノード登録と取得時刻を採取票翠O計画0335へ残します。翠O計画0335ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断翠O計画0335です。翠O計画0335の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録翠O計画0335です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0334の技術的な意味を資料で確認するとき、node コマンド証跡 マクロ実行との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はマクロ実行の誤読を避けるため・管理クラスでマクロ実行を確認するしてマクロ実行を照合する。</li><li>B. 管理対象との関係を表す説明は置換条件や復元先を確認せず本番フを避けるため・構成監査で構成監査ではを確認するして構成監査ではを照合する。</li><li>C. 管理対象との関係を表す説明は失敗イベントの見落としを避けるため・監査操作で記録欄を比較するしてイベント結果を照合する。</li><li>D. 管理対象との関係を表す説明はデータベースバックアップ時刻の記を避けるため・確認操作で状態欄を整理するしてノード登録を照合する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 計画対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・計画・ノード・データベ）です。計画時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・計画・ノード・データベです。node・管理クラスのA:は「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」を述べ、対象はコマンド証跡 マクロ実行（node・管理ク・マクロ・マクロ実）です。構成監査対象ClienのB:は「Client Restoreで構成監査ではリストア確認の」を述べ、対象は構成監査 RST08（Clien・構成監・構成監・置換条件）です。登録時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・登録・イベン・失敗イベ）です。Expiを計画という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・計画・ノード・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0334</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0334について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2234
確認コード SP81DD0334A
画面・出力には SP81DD0334A が表示され、サーバー日次運用 Expiration Status 0334 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE094
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0334B
画面・出力には SP81DD0334B が表示され、サーバー日次運用 Expiration Status 0334 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 594 GB
確認コード SP81DD0334C
画面・出力には SP81DD0334C が表示され、サーバー日次運用 Expiration Status 0334 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0334A が画面・出力に表示されること
② ステップ2 の SP81DD0334B が画面・出力に表示されること
③ ステップ3 の SP81DD0334C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0113"><h3>サーバー日次運用 Expiration Status 0349</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>朱J解除0350ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票朱J解除0350です。朱J解除0350はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録朱J解除0350です。朱J解除0350ではノード登録と取得時刻を採取票朱J解除0350へ残します。朱J解除0350では期限切れ処理の未実行を避けるため補助資料も照合する判断朱J解除0350です。朱J解除0350の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録朱J解除0350です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Expiration Status 0349について構成や状態を確認します。management class 状態確認 イベント識別ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは状態確認でイベント識別を確認することでイベント識別を確認し・イベント識別の誤読を防ぐ。</li><li>B. 対象資源に対する働きは照合操作で確認欄を採取することでイベント結果を確認し・日次処理順序の誤読を防ぐ。</li><li>C. 対象資源に対する働きは保守操作で監査欄を保存することで運用状態を確認し・ノード状態の誤読を防ぐ。</li><li>D. 対象資源に対する働きは記録操作で証跡欄を照合することでノード登録を確認し・期限切れ処理の未実行を防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 解除対象ExpirでDの記述「Expiration Statusのノード登録と取得時刻を記録し」に対応する項目はExpiration Status（Expir・解除・ノード・期限切れ）です。解除時のExpirに関するサーバー運用の仕様は「Expiration Statusのノード登録と取得時刻を記録し」で、確認対象はExpi・解除・ノード・期限切れです。manag・状態確認のA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は状態確認 イベント識別（manag・状態確・イベン・イベント）です。巡回対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・巡回・イベン・日次処理）です。登録時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・登録・運用状・ノード状）です。Expiを解除という用語は「Expiration Statusのノード登録と取得」を指し、Expiration Status（Expir・解除・ノード・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Expiration Status 0349</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Expiration Status 0349について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Expiration Status と ノード登録</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY NODE
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2249
確認コード SP81DD0349A
画面・出力には SP81DD0349A が表示され、サーバー日次運用 Expiration Status 0349 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE109
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0349B
画面・出力には SP81DD0349B が表示され、サーバー日次運用 Expiration Status 0349 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Expiration Status を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 609 GB
確認コード SP81DD0349C
画面・出力には SP81DD0349C が表示され、サーバー日次運用 Expiration Status 0349 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0349A が画面・出力に表示されること
② ステップ2 の SP81DD0349B が画面・出力に表示されること
③ ステップ3 の SP81DD0349C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0114"><h3>サーバー日次運用 Node Name 0013</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>灰N巡回0014ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票灰N巡回0014です。灰N巡回0014はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録灰N巡回0014です。灰N巡回0014では運用状態と取得時刻を採取票灰N巡回0014へ残します。灰N巡回0014では期限切れ処理の未実行を避けるため補助資料も照合する判断灰N巡回0014です。灰N巡回0014の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録灰N巡回0014です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0013について構成や状態を確認します。サーバー日次運用 Expiration Status 0049ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはサーバー操作とメッセージを追跡するログを容量監視として確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 巡回対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・巡回・運用状態）です。サーバに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・巡回・運用状態です。Expir・復旧のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expira・復旧・ノード登）です。照合対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・照合・失敗理由）です。actiをリストアのD:は「サーバー操作とメッセージを追跡するログを容量監視として確認する」を述べ、対象は容量監視 アーカイブ（activi・リスト・アーカイ）です。Nodeを巡回という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・巡回・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0013</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0013について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2213
確認コード SP81DD0013A
画面・出力には SP81DD0013A が表示され、サーバー日次運用 Node Name 0013 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE013
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0013B
画面・出力には SP81DD0013B が表示され、サーバー日次運用 Node Name 0013 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 513 GB
確認コード SP81DD0013C
画面・出力には SP81DD0013C が表示され、サーバー日次運用 Node Name 0013 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0013A が画面・出力に表示されること
② ステップ2 の SP81DD0013B が画面・出力に表示されること
③ ステップ3 の SP81DD0013C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0115"><h3>サーバー日次運用 Node Name 0028</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黄I棚卸0029ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黄I棚卸0029です。黄I棚卸0029はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録黄I棚卸0029です。黄I棚卸0029では運用状態と取得時刻を採取票黄I棚卸0029へ残します。黄I棚卸0029ではノード状態の誤読を避けるため補助資料も照合する判断黄I棚卸0029です。黄I棚卸0029の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録黄I棚卸0029です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0028の役割を調べています。サーバー日次運用 Expiration Status 0049の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。</li><li>B. 表示や設定で扱う内容はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はClient Nodeで通常状態の確認ではノード管理の ノード照会からLastAccessを読みである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 棚卸対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・棚卸・運用状態）です。棚卸時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・棚卸・運用状態です。Expir・復旧のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expira・復旧・ノード登）です。確認対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・確認・スケジュ）です。Clieを通常状態確のD:は「Client Nodeで通常状態の確認ではノード管理の」を述べ、対象は通常状態の確認 NODE01（Client・通常状・通常状態）です。Nodeを棚卸という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・棚卸・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0028</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0028について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2228
確認コード SP81DD0028A
画面・出力には SP81DD0028A が表示され、サーバー日次運用 Node Name 0028 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE028
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0028B
画面・出力には SP81DD0028B が表示され、サーバー日次運用 Node Name 0028 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 528 GB
確認コード SP81DD0028C
画面・出力には SP81DD0028C が表示され、サーバー日次運用 Node Name 0028 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0028A が画面・出力に表示されること
② ステップ2 の SP81DD0028B が画面・出力に表示されること
③ ステップ3 の SP81DD0028C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0116"><h3>サーバー日次運用 Node Name 0043</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藍D復旧0044ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藍D復旧0044です。藍D復旧0044はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録藍D復旧0044です。藍D復旧0044では運用状態と取得時刻を採取票藍D復旧0044へ残します。藍D復旧0044ではプール容量不足の見落としを避けるため補助資料も照合する判断藍D復旧0044です。藍D復旧0044の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録藍D復旧0044です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Node Name 0043」を「ポリシーと管理クラス DIRMC 0113」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 保守作業で参照する機能はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 保守作業で参照する機能はBackup andで引継ぎ記録ではコピーグループの 管理クラス対応からBackupCopyを読みである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧対象NodeでAの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・復旧・運用状態）です。復旧時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・復旧・運用状態です。移行対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・移行・ノード登）です。照合時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・照合・ディレク）です。BackをコピーグルのD:は「Backup andで引継ぎ記録ではコピーグループの」を述べ、対象は引継ぎ記録 CG09（Backup・コピー・引継ぎ記）です。Nodeを復旧という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・復旧・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0043</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0043について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2243
確認コード SP81DD0043A
画面・出力には SP81DD0043A が表示され、サーバー日次運用 Node Name 0043 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE043
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0043B
画面・出力には SP81DD0043B が表示され、サーバー日次運用 Node Name 0043 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 543 GB
確認コード SP81DD0043C
画面・出力には SP81DD0043C が表示され、サーバー日次運用 Node Name 0043 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0043A が画面・出力に表示されること
② ステップ2 の SP81DD0043B が画面・出力に表示されること
③ ステップ3 の SP81DD0043C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0117"><h3>サーバー日次運用 Node Name 0058</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黒S復旧0059ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黒S復旧0059です。黒S復旧0059はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録黒S復旧0059です。黒S復旧0059では運用状態と取得時刻を採取票黒S復旧0059へ残します。黒S復旧0059ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断黒S復旧0059です。黒S復旧0059の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録黒S復旧0059です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0058を同一分類のクライアントスケジュール Start Time 0153と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>B. 管理対象との関係を表す説明はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 管理対象との関係を表す説明はBackup andで通常状態の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧対象NodeでBの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・復旧・運用状態）です。復旧時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・復旧・運用状態です。Start・保守のA:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・保守・失敗理由）です。解除時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・解除・関連ノー）です。Backを通常状態確のD:は「Backup andで通常状態の確認ではコピーグループの」を述べ、対象は通常状態の確認 CG01（Backup・通常状・確認では）です。Nodeを復旧という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・復旧・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0058</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0058について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2258
確認コード SP81DD0058A
画面・出力には SP81DD0058A が表示され、サーバー日次運用 Node Name 0058 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE058
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0058B
画面・出力には SP81DD0058B が表示され、サーバー日次運用 Node Name 0058 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 558 GB
確認コード SP81DD0058C
画面・出力には SP81DD0058C が表示され、サーバー日次運用 Node Name 0058 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0058A が画面・出力に表示されること
② ステップ2 の SP81DD0058B が画面・出力に表示されること
③ ステップ3 の SP81DD0058C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0118"><h3>サーバー日次運用 Node Name 0073</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>灰N監査0074ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票灰N監査0074です。灰N監査0074はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録灰N監査0074です。灰N監査0074では運用状態と取得時刻を採取票灰N監査0074へ残します。灰N監査0074では期限切れ処理の未実行を避けるため補助資料も照合する判断灰N監査0074です。灰N監査0074の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録灰N監査0074です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0073の設定や表示を読む前に役割を確認します。クライアントスケジュール Start Time 0123ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>B. 対象資源に対する働きはActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはArchive Operationで復旧準備ではアーカイブ運用のである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・監査・運用状態）です。監査時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・監査・運用状態です。Start・診断のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・診断・失敗理由）です。計画対象ActioのB:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・計画・開始時刻）です。Archを復旧準備のD:は「Archive Operationで復旧準備ではアーカイブ運用の」を述べ、対象は復旧準備 ARC05（Archiv・復旧準・復旧準備）です。Nodeを監査という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・監査・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0073</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0073について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2213
確認コード SP81DD0073A
画面・出力には SP81DD0073A が表示され、サーバー日次運用 Node Name 0073 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE073
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0073B
画面・出力には SP81DD0073B が表示され、サーバー日次運用 Node Name 0073 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 573 GB
確認コード SP81DD0073C
画面・出力には SP81DD0073C が表示され、サーバー日次運用 Node Name 0073 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0073A が画面・出力に表示されること
② ステップ2 の SP81DD0073B が画面・出力に表示されること
③ ステップ3 の SP81DD0073C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0119"><h3>サーバー日次運用 Node Name 0088</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黄I変更0089ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黄I変更0089です。黄I変更0089はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録黄I変更0089です。黄I変更0089では運用状態と取得時刻を採取票黄I変更0089へ残します。黄I変更0089ではノード状態の誤読を避けるため補助資料も照合する判断黄I変更0089です。黄I変更0089の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録黄I変更0089です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0088に関する障害切り分けの前提を確認しています。サーバー日次運用 Storage Pool 0100の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>B. 表示や設定で扱う内容はEvent Statusのイベント結果と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>C. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はStorage Poolで再始動後の確認では複製・保護の 検証からANR3730Iを読み・再始動確認に使うである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・変更・運用状態）です。変更時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・変更・運用状態です。Stora・移行のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・移行・ストレー）です。解除対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・解除・イベント）です。Storを再始動確認のD:は「Storage Poolで再始動後の確認では複製・保護の」を述べ、対象は再始動後の確認 REPL15（Storag・再始動・再始動後）です。Nodeを変更という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・変更・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0088</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0088について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2228
確認コード SP81DD0088A
画面・出力には SP81DD0088A が表示され、サーバー日次運用 Node Name 0088 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE088
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0088B
画面・出力には SP81DD0088B が表示され、サーバー日次運用 Node Name 0088 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 588 GB
確認コード SP81DD0088C
画面・出力には SP81DD0088C が表示され、サーバー日次運用 Node Name 0088 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0088A が画面・出力に表示されること
② ステップ2 の SP81DD0088B が画面・出力に表示されること
③ ステップ3 の SP81DD0088C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0120"><h3>サーバー日次運用 Node Name 0103</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>藍D移行0104ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藍D移行0104です。藍D移行0104はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録藍D移行0104です。藍D移行0104では運用状態と取得時刻を採取票藍D移行0104へ残します。藍D移行0104ではプール容量不足の見落としを避けるため補助資料も照合する判断藍D移行0104です。藍D移行0104の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録藍D移行0104です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0103を保守記録に説明する必要があります。サーバー日次運用 Database Backup 0172と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>B. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 保守作業で参照する機能はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はArchive Operationで性能影響の確認ではアーカイブ運用のである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 移行対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・移行・運用状態）です。移行時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・移行・運用状態です。Datab・切替のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・切替・期限切れ）です。解除対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・解除・ドメイン）です。Archを性能影響確のD:は「Archive Operationで性能影響の確認ではアーカイブ運用」を述べ、対象は性能影響の確認 ARC11（Archiv・性能影・確認では）です。Nodeを移行という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・移行・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0103</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0103について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2243
確認コード SP81DD0103A
画面・出力には SP81DD0103A が表示され、サーバー日次運用 Node Name 0103 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE103
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0103B
画面・出力には SP81DD0103B が表示され、サーバー日次運用 Node Name 0103 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 603 GB
確認コード SP81DD0103C
画面・出力には SP81DD0103C が表示され、サーバー日次運用 Node Name 0103 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0103A が画面・出力に表示されること
② ステップ2 の SP81DD0103B が画面・出力に表示されること
③ ステップ3 の SP81DD0103C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0121"><h3>サーバー日次運用 Node Name 0118</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>黒S移行0119ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黒S移行0119です。黒S移行0119はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録黒S移行0119です。黒S移行0119では運用状態と取得時刻を採取票黒S移行0119へ残します。黒S移行0119ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断黒S移行0119です。黒S移行0119の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録黒S移行0119です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0118の技術的な意味を資料で確認するとき、サーバー日次運用 Expiration Status 0214との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 管理対象との関係を表す説明はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はファイルのバックアップ先や保存期間を決めるポリシー要素である。</li><li>D. 管理対象との関係を表す説明はIncremental Backupで復旧後の確認ではバックアップ運用のである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 移行対象NodeでBの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・移行・運用状態）です。移行時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・移行・運用状態です。Expir・登録のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expira・登録・ノード登）です。宛先照合時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は宛先照合 初期同期（manage・宛先照・初期同期）です。Incrを復旧確認のD:は「Incremental Backupで復旧後の確認ではバックアップ運」を述べ、対象は復旧後の確認 BKP06（Increm・復旧確・復旧後の）です。Nodeを移行という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・移行・運用状態）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0118</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0118について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2258
確認コード SP81DD0118A
画面・出力には SP81DD0118A が表示され、サーバー日次運用 Node Name 0118 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE118
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0118B
画面・出力には SP81DD0118B が表示され、サーバー日次運用 Node Name 0118 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 618 GB
確認コード SP81DD0118C
画面・出力には SP81DD0118C が表示され、サーバー日次運用 Node Name 0118 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0118A が画面・出力に表示されること
② ステップ2 の SP81DD0118B が画面・出力に表示されること
③ ステップ3 の SP81DD0118C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0122"><h3>サーバー日次運用 Node Name 0133</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>灰N診断0134ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票灰N診断0134です。灰N診断0134はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録灰N診断0134です。灰N診断0134では運用状態と取得時刻を採取票灰N診断0134へ残します。灰N診断0134では期限切れ処理の未実行を避けるため補助資料も照合する判断灰N診断0134です。灰N診断0134の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録灰N診断0134です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0133について構成や状態を確認します。クライアントスケジュール Start Time 0153ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>B. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはアーカイブコピーの保存期間と宛先を定めるコピー規則をノード割当確認する。archive copy group ノード割当確認 対象表固有の属性も確認対象に含める。</li><li>D. 対象資源に対する働きはArchive Operationで権限境界の確認ではアーカイブ運用のである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 診断対象NodeでBの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・診断・運用状・期限切れ）です。診断時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・診断・運用状・期限切れです。Start・保守のA:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・保守・失敗理・関連付け）です。ノード割時のarchiのC:は「アーカイブコピーの保存期間と宛先を定めるコピー規則をノード割当確認す」を述べ、対象はノード割当確認 対象表（archi・ノード・対象表・対象表の）です。Archを権限境界確のD:は「Archive Operationで権限境界の確認ではアーカイブ運用」を述べ、対象は権限境界の確認 ARC12（Archi・権限境・確認で・バックア）です。Nodeを診断という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・診断・運用状・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0133</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0133について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2213
確認コード SP81DD0133A
画面・出力には SP81DD0133A が表示され、サーバー日次運用 Node Name 0133 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE013
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0133B
画面・出力には SP81DD0133B が表示され、サーバー日次運用 Node Name 0133 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 513 GB
確認コード SP81DD0133C
画面・出力には SP81DD0133C が表示され、サーバー日次運用 Node Name 0133 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0133A が画面・出力に表示されること
② ステップ2 の SP81DD0133B が画面・出力に表示されること
③ ステップ3 の SP81DD0133C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0123"><h3>サーバー日次運用 Node Name 0148</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黄I保守0149ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黄I保守0149です。黄I保守0149はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録黄I保守0149です。黄I保守0149では運用状態と取得時刻を採取票黄I保守0149へ残します。黄I保守0149ではノード状態の誤読を避けるため補助資料も照合する判断黄I保守0149です。黄I保守0149の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録黄I保守0149です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0148の役割を調べています。ポリシーと管理クラス Policy Domain 0200の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>B. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はファイルのバックアップ先や保存期間を決めるポリシー要素である。</li><li>D. 表示や設定で扱う内容はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保守対象NodeでBの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・保守・運用状・ノード状）です。保守時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・保守・運用状・ノード状です。Polic・登録のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・登録・管理ク・登録ドメ）です。状態確認時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は状態確認 イベント識別（manag・状態確・イベン・イベント）です。Scheを棚卸のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・棚卸・スケジ・日次処理）です。Nodeを保守という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・保守・運用状・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0148</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0148について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2228
確認コード SP81DD0148A
画面・出力には SP81DD0148A が表示され、サーバー日次運用 Node Name 0148 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE028
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0148B
画面・出力には SP81DD0148B が表示され、サーバー日次運用 Node Name 0148 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 528 GB
確認コード SP81DD0148C
画面・出力には SP81DD0148C が表示され、サーバー日次運用 Node Name 0148 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0148A が画面・出力に表示されること
② ステップ2 の SP81DD0148B が画面・出力に表示されること
③ ステップ3 の SP81DD0148C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0124"><h3>サーバー日次運用 Node Name 0163</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藍D切替0164ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藍D切替0164です。藍D切替0164はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録藍D切替0164です。藍D切替0164では運用状態と取得時刻を採取票藍D切替0164へ残します。藍D切替0164ではプール容量不足の見落としを避けるため補助資料も照合する判断藍D切替0164です。藍D切替0164の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録藍D切替0164です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Node Name 0163」を「ポリシーと管理クラス Management Class 0209」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>B. 保守作業で参照する機能はファイルのバックアップ先や保存期間を決めるポリシー要素を期限切れ確認する。</li><li>C. 保守作業で参照する機能はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 切替対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・切替・運用状・プール容）です。切替時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・切替・運用状・プール容です。Manag・登録のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・登録・ドメイ・管理クラ）です。期限切れ対象managのB:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を期限切れ確認」を述べ、対象は期限切れ確認 宛先定義（manag・期限切・宛先定・宛先定義）です。Evenを棚卸のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・棚卸・イベン・失敗イベ）です。Nodeを切替という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・切替・運用状・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0163</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0163について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2243
確認コード SP81DD0163A
画面・出力には SP81DD0163A が表示され、サーバー日次運用 Node Name 0163 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE043
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0163B
画面・出力には SP81DD0163B が表示され、サーバー日次運用 Node Name 0163 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 543 GB
確認コード SP81DD0163C
画面・出力には SP81DD0163C が表示され、サーバー日次運用 Node Name 0163 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0163A が画面・出力に表示されること
② ステップ2 の SP81DD0163B が画面・出力に表示されること
③ ステップ3 の SP81DD0163C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0125"><h3>サーバー日次運用 Node Name 0178</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黒S切替0179ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黒S切替0179です。黒S切替0179はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録黒S切替0179です。黒S切替0179では運用状態と取得時刻を採取票黒S切替0179へ残します。黒S切替0179ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断黒S切替0179です。黒S切替0179の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録黒S切替0179です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0178を同一分類のポリシーと管理クラス Management Class 0209と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>B. 管理対象との関係を表す説明はバックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する。</li><li>C. 管理対象との関係を表す説明はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 切替対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・切替・運用状・データベ）です。切替時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・切替・運用状・データベです。Manag・登録のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・登録・ドメイ・管理クラ）です。復元前確対象schedのB:は「バックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する」を述べ、対象は復元前確認 時刻合わせ（sched・復元前・時刻合・時刻合わ）です。ノード登録を監査のD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・監査・ノード・登録ドメ）です。Nodeを切替という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・切替・運用状・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0178</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0178について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2258
確認コード SP81DD0178A
画面・出力には SP81DD0178A が表示され、サーバー日次運用 Node Name 0178 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE058
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0178B
画面・出力には SP81DD0178B が表示され、サーバー日次運用 Node Name 0178 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 558 GB
確認コード SP81DD0178C
画面・出力には SP81DD0178C が表示され、サーバー日次運用 Node Name 0178 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0178A が画面・出力に表示されること
② ステップ2 の SP81DD0178B が画面・出力に表示されること
③ ステップ3 の SP81DD0178C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0126"><h3>サーバー日次運用 Node Name 0193</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>灰N収集0194ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票灰N収集0194です。灰N収集0194はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録灰N収集0194です。灰N収集0194では運用状態と取得時刻を採取票灰N収集0194へ残します。灰N収集0194では期限切れ処理の未実行を避けるため補助資料も照合する判断灰N収集0194です。灰N収集0194の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録灰N収集0194です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0193の設定や表示を読む前に役割を確認します。ポリシーと管理クラス Policy Domain 0215ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>B. 対象資源に対する働きはPolicy Domainで依存関係の確認ではポリシードメインのである。</li><li>C. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・収集・運用状・期限切れ）です。収集時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・収集・運用状・期限切れです。Polic・登録のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・登録・管理ク・コピーグ）です。依存関係対象PolicのB:は「Policy Domainで依存関係の確認ではポリシードメインの」を述べ、対象は依存関係の確認 DOM13（Polic・依存関・確認で・ノードを）です。Starを巡回のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・巡回・失敗理・失敗イベ）です。Nodeを収集という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・収集・運用状・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0193</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0193について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2213
確認コード SP81DD0193A
画面・出力には SP81DD0193A が表示され、サーバー日次運用 Node Name 0193 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE073
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0193B
画面・出力には SP81DD0193B が表示され、サーバー日次運用 Node Name 0193 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 573 GB
確認コード SP81DD0193C
画面・出力には SP81DD0193C が表示され、サーバー日次運用 Node Name 0193 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0193A が画面・出力に表示されること
② ステップ2 の SP81DD0193B が画面・出力に表示されること
③ ステップ3 の SP81DD0193C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0127"><h3>サーバー日次運用 Node Name 0208</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黄I登録0209ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黄I登録0209です。黄I登録0209はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録黄I登録0209です。黄I登録0209では運用状態と取得時刻を採取票黄I登録0209へ残します。黄I登録0209ではノード状態の誤読を避けるため補助資料も照合する判断黄I登録0209です。黄I登録0209の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録黄I登録0209です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0208に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Policy Set 0212の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 表示や設定で扱う内容はバックアップや管理コマンドを決めた時刻に実行する定義である。</li><li>D. 表示や設定で扱う内容はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 登録対象NodeでAの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・登録・運用状・ノード状）です。登録時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・登録・運用状・ノード状です。登録対象PolicのB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・登録・ディレ・登録ドメ）です。宛先照合時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義」を述べ、対象は宛先照合 ホスト検査（sched・宛先照・ホスト・ホスト検）です。Starを復旧のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・復旧・失敗理・日次処理）です。Nodeを登録という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・登録・運用状・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0208</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0208について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2228
確認コード SP81DD0208A
画面・出力には SP81DD0208A が表示され、サーバー日次運用 Node Name 0208 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE088
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0208B
画面・出力には SP81DD0208B が表示され、サーバー日次運用 Node Name 0208 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 588 GB
確認コード SP81DD0208C
画面・出力には SP81DD0208C が表示され、サーバー日次運用 Node Name 0208 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0208A が画面・出力に表示されること
② ステップ2 の SP81DD0208B が画面・出力に表示されること
③ ステップ3 の SP81DD0208C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0128"><h3>サーバー日次運用 Node Name 0223</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>藍D確認0224ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藍D確認0224です。藍D確認0224はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録藍D確認0224です。藍D確認0224では運用状態と取得時刻を採取票藍D確認0224へ残します。藍D確認0224ではプール容量不足の見落としを避けるため補助資料も照合する判断藍D確認0224です。藍D確認0224の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録藍D確認0224です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0223を保守記録に説明する必要があります。ポリシーと管理クラス Management Class 0299と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>B. 保守作業で参照する機能はPolicy Domainで性能影響の確認ではポリシードメインのである。</li><li>C. 保守作業で参照する機能はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>D. 保守作業で参照する機能はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 確認対象NodeでDの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・確認・運用状・プール容）です。確認時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・確認・運用状・プール容です。Manag・抑止のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・抑止・ドメイ・コピーグ）です。性能影響対象PolicのB:は「Policy Domainで性能影響の確認ではポリシードメインの」を述べ、対象は性能影響の確認 DOM11（Polic・性能影・確認で・ノードを）です。移行時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・移行・ストレ・プール容）です。Nodeを確認という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・確認・運用状・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0223</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0223について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2243
確認コード SP81DD0223A
画面・出力には SP81DD0223A が表示され、サーバー日次運用 Node Name 0223 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE103
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0223B
画面・出力には SP81DD0223B が表示され、サーバー日次運用 Node Name 0223 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 603 GB
確認コード SP81DD0223C
画面・出力には SP81DD0223C が表示され、サーバー日次運用 Node Name 0223 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0223A が画面・出力に表示されること
② ステップ2 の SP81DD0223B が画面・出力に表示されること
③ ステップ3 の SP81DD0223C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0129"><h3>サーバー日次運用 Node Name 0238</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>黒S確認0239ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黒S確認0239です。黒S確認0239はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録黒S確認0239です。黒S確認0239では運用状態と取得時刻を採取票黒S確認0239へ残します。黒S確認0239ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断黒S確認0239です。黒S確認0239の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録黒S確認0239です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0238の技術的な意味を資料で確認するとき、ポリシーと管理クラス Copy Group 0326との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 管理対象との関係を表す説明は保存期間を過ぎた版やアーカイブを期限切れにする処理をノード割当確認する。</li><li>C. 管理対象との関係を表す説明はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 確認対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・確認・運用状・データベ）です。確認時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・確認・運用状・データベです。Copy・計画のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・計画・コピー・ディレク）です。ノード割対象expirのB:は「保存期間を過ぎた版やアーカイブを期限切れにする処理をノード割当確認す」を述べ、対象はノード割当確認 管理レポート（expir・ノード・管理レ・管理レポ）です。Evenを変更のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更・イベン・失敗イベ）です。Nodeを確認という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・確認・運用状・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0238</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0238について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2258
確認コード SP81DD0238A
画面・出力には SP81DD0238A が表示され、サーバー日次運用 Node Name 0238 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE118
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0238B
画面・出力には SP81DD0238B が表示され、サーバー日次運用 Node Name 0238 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 618 GB
確認コード SP81DD0238C
画面・出力には SP81DD0238C が表示され、サーバー日次運用 Node Name 0238 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0238A が画面・出力に表示されること
② ステップ2 の SP81DD0238B が画面・出力に表示されること
③ ステップ3 の SP81DD0238C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0130"><h3>サーバー日次運用 Node Name 0253</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>灰N保護0254ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票灰N保護0254です。灰N保護0254はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録灰N保護0254です。灰N保護0254では運用状態と取得時刻を採取票灰N保護0254へ残します。灰N保護0254では期限切れ処理の未実行を避けるため補助資料も照合する判断灰N保護0254です。灰N保護0254の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録灰N保護0254です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0253について構成や状態を確認します。クライアントスケジュール Start Time 0288ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>B. 対象資源に対する働きはDirectory-containeで権限境界の確認ではストレージプールのである。</li><li>C. 対象資源に対する働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・保護・運用状・期限切れ）です。保護時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・保護・運用状・期限切れです。Start・抑止のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・抑止・失敗理・日次処理）です。権限境界対象DirecのB:は「Directory-containeで権限境界の確認ではストレージプ」を述べ、対象は権限境界の確認 POOL12（Direc・権限境・権限境・容量使用）です。Evenを復旧のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・復旧・イベン・関連付け）です。Nodeを保護という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・保護・運用状・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0253</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0253について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2213
確認コード SP81DD0253A
画面・出力には SP81DD0253A が表示され、サーバー日次運用 Node Name 0253 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE013
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0253B
画面・出力には SP81DD0253B が表示され、サーバー日次運用 Node Name 0253 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 513 GB
確認コード SP81DD0253C
画面・出力には SP81DD0253C が表示され、サーバー日次運用 Node Name 0253 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0253A が画面・出力に表示されること
② ステップ2 の SP81DD0253B が画面・出力に表示されること
③ ステップ3 の SP81DD0253C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0131"><h3>サーバー日次運用 Node Name 0268</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黄I照合0269ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黄I照合0269です。黄I照合0269はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録黄I照合0269です。黄I照合0269では運用状態と取得時刻を採取票黄I照合0269へ残します。黄I照合0269ではノード状態の誤読を避けるため補助資料も照合する判断黄I照合0269です。黄I照合0269の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録黄I照合0269です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0268の役割を調べています。サーバー日次運用 Expiration Status 0319の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 表示や設定で扱う内容はClient Nodeで代替経路の確認ではノード管理の ノード照会からLastAccessを読みである。</li><li>C. 表示や設定で扱う内容はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>D. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 照合対象NodeでDの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・照合・運用状・ノード状）です。照合時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・照合・運用状・ノード状です。Expir・解析のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・解析・ノード・プール容）です。代替経路対象ClienのB:は「Client Nodeで代替経路の確認ではノード管理の」を述べ、対象は代替経路の確認 NODE10（Clien・代替経・代替経・長期未接）です。変更時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・変更・管理ク・登録ドメ）です。Nodeを照合という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・照合・運用状・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0268</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0268について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2228
確認コード SP81DD0268A
画面・出力には SP81DD0268A が表示され、サーバー日次運用 Node Name 0268 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE028
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0268B
画面・出力には SP81DD0268B が表示され、サーバー日次運用 Node Name 0268 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 528 GB
確認コード SP81DD0268C
画面・出力には SP81DD0268C が表示され、サーバー日次運用 Node Name 0268 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0268A が画面・出力に表示されること
② ステップ2 の SP81DD0268B が画面・出力に表示されること
③ ステップ3 の SP81DD0268C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0132"><h3>サーバー日次運用 Node Name 0283</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>藍D抑止0284ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藍D抑止0284です。藍D抑止0284はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録藍D抑止0284です。藍D抑止0284では運用状態と取得時刻を採取票藍D抑止0284へ残します。藍D抑止0284ではプール容量不足の見落としを避けるため補助資料も照合する判断藍D抑止0284です。藍D抑止0284の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録藍D抑止0284です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Node Name 0283」を「ポリシーと管理クラス Management Class 0284」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は調査操作で保守欄を引き継ぎすることでドメイン割当を確認し・登録ドメインの取り違えを防ぐ。</li><li>B. 保守作業で参照する機能は復旧準備で復旧準備ではを確認することで復旧準備ではを確認し・置換条件や復元先を確認せず本を防ぐ。</li><li>C. 保守作業で参照する機能は保守操作で監査欄を保存することで期限切れ処理を確認し・ノード状態の誤読を防ぐ。</li><li>D. 保守作業で参照する機能は採取操作で照合欄を点検することで運用状態を確認し・プール容量不足の見落としを防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 抑止対象NodeでDの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・抑止・運用状・プール容）です。抑止時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・抑止・運用状・プール容です。Manag・抑止のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・抑止・ドメイ・登録ドメ）です。復旧準備対象ClienのB:は「Client Restoreで復旧準備ではリストア確認の」を述べ、対象は復旧準備 RST05（Clien・復旧準・復旧準・置換条件）です。移行時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・移行・期限切・ノード状）です。Nodeを抑止という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・抑止・運用状・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0283</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0283について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2243
確認コード SP81DD0283A
画面・出力には SP81DD0283A が表示され、サーバー日次運用 Node Name 0283 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE043
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0283B
画面・出力には SP81DD0283B が表示され、サーバー日次運用 Node Name 0283 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 543 GB
確認コード SP81DD0283C
画面・出力には SP81DD0283C が表示され、サーバー日次運用 Node Name 0283 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0283A が画面・出力に表示されること
② ステップ2 の SP81DD0283B が画面・出力に表示されること
③ ステップ3 の SP81DD0283C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0133"><h3>サーバー日次運用 Node Name 0298</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黒S抑止0299ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黒S抑止0299です。黒S抑止0299はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録黒S抑止0299です。黒S抑止0299では運用状態と取得時刻を採取票黒S抑止0299へ残します。黒S抑止0299ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断黒S抑止0299です。黒S抑止0299の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録黒S抑止0299です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0298を同一分類のmanagement class 宛先照合 初期同期と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は初期同期の誤読を避けるため・宛先照合で初期同期を確認するして初期同期を照合する。</li><li>B. 管理対象との関係を表す説明はデータベースバックアップ時刻の記を避けるため・確認操作で状態欄を整理するして運用状態を照合する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はバックアップデータをアーカイブとを避けるため・アーカイブ運で障害切り分けを確認するして障害切り分けを照合する。</li><li>D. 管理対象との関係を表す説明は登録ドメインの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてドメイン割当を照合する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 抑止対象NodeでBの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・抑止・運用状・データベ）です。抑止時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・抑止・運用状・データベです。manag・宛先照合のA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は宛先照合 初期同期（manag・宛先照・初期同・初期同期）です。アーカイ時のArchiのC:は「Archive Operationで障害切り分けではアーカイブ運用の」を述べ、対象は障害切り分け ARC04（Archi・アーカ・障害切・バックア）です。Manaを移行のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・移行・ドメイ・登録ドメ）です。Nodeを抑止という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・抑止・運用状・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0298</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0298について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2258
確認コード SP81DD0298A
画面・出力には SP81DD0298A が表示され、サーバー日次運用 Node Name 0298 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE058
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0298B
画面・出力には SP81DD0298B が表示され、サーバー日次運用 Node Name 0298 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 558 GB
確認コード SP81DD0298C
画面・出力には SP81DD0298C が表示され、サーバー日次運用 Node Name 0298 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0298A が画面・出力に表示されること
② ステップ2 の SP81DD0298B が画面・出力に表示されること
③ ステップ3 の SP81DD0298C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0134"><h3>サーバー日次運用 Node Name 0313</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>灰N解析0314ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票灰N解析0314です。灰N解析0314はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録灰N解析0314です。灰N解析0314では運用状態と取得時刻を採取票灰N解析0314へ残します。灰N解析0314では期限切れ処理の未実行を避けるため補助資料も照合する判断灰N解析0314です。灰N解析0314の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録灰N解析0314です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0313の設定や表示を読む前に役割を確認します。policy domain 期限切れ確認 容量表示ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは容量表示で容量表示を証跡に残し・クライアントに適用するバックアップとアーカイブの規則を束ねる。</li><li>B. 対象資源に対する働きは代替経路確認で代替経路の確を証跡に残し・Client Restoreで代替経路の確認ではリストア確認。</li><li>C. 対象資源に対する働きは保守でノード登録値を証跡に残し・DIRMCのノード登録値と取得時刻を記録し。</li><li>D. 対象資源に対する働きは解析で運用状態を証跡に残し・Node Nameの運用状態と取得時刻を記録し。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象NodeでDの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・解析・運用状・期限切れ）です。解析時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・解析・運用状・期限切れです。polic・容量表示のA:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」を述べ、対象は期限切れ確認 容量表示（polic・容量表・容量表・容量表示）です。代替経路対象ClienのB:は「Client Restoreで代替経路の確認ではリストア確認の」を述べ、対象は代替経路の確認 RST10（Clien・代替経・代替経・置換条件）です。保守時のディレクトのC:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・保守・ノード・ディレク）です。Nodeを解析という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・解析・運用状・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0313</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0313について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2213
確認コード SP81DD0313A
画面・出力には SP81DD0313A が表示され、サーバー日次運用 Node Name 0313 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE073
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0313B
画面・出力には SP81DD0313B が表示され、サーバー日次運用 Node Name 0313 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 573 GB
確認コード SP81DD0313C
画面・出力には SP81DD0313C が表示され、サーバー日次運用 Node Name 0313 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0313A が画面・出力に表示されること
② ステップ2 の SP81DD0313B が画面・出力に表示されること
③ ステップ3 の SP81DD0313C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0135"><h3>サーバー日次運用 Node Name 0328</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>黄I計画0329ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黄I計画0329です。黄I計画0329はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録黄I計画0329です。黄I計画0329では運用状態と取得時刻を採取票黄I計画0329へ残します。黄I計画0329ではノード状態の誤読を避けるため補助資料も照合する判断黄I計画0329です。黄I計画0329の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録黄I計画0329です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0328に関する障害切り分けの前提を確認しています。node 保存期間確認 活動ログの機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はサーバーへ登録されたクライアントを表す管理単位である。保存期間確認で活動ログを確認するときは活動ログの誤読を防ぐ。</li><li>B. 表示や設定で扱う内容はClient Restoreで性能影響の確認ではリストア確認の 別名復元からrestoredを読みである。性能影響確認で性能影響の確を確認するときは置換条件や復元先を確認せず本を防ぐ。</li><li>C. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。保守操作で監査欄を保存するときはノード状態の誤読を防ぐ。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。採取操作で照合欄を点検するときはプール容量不足の見落としを防ぐ。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 計画対象NodeでCの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・計画・運用状・ノード状）です。計画時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・計画・運用状・ノード状です。node・保存期間確のA:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は保存期間確認 活動ログ（node・保存期・活動ロ・活動ログ）です。性能影響対象ClienのB:は「Client Restoreで性能影響の確認ではリストア確認の」を述べ、対象は性能影響の確認 RST11（Clien・性能影・性能影・置換条件）です。Dataを収集のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・収集・期限切・プール容）です。Nodeを計画という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・計画・運用状・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0328</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0328について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2228
確認コード SP81DD0328A
画面・出力には SP81DD0328A が表示され、サーバー日次運用 Node Name 0328 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE088
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0328B
画面・出力には SP81DD0328B が表示され、サーバー日次運用 Node Name 0328 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 588 GB
確認コード SP81DD0328C
画面・出力には SP81DD0328C が表示され、サーバー日次運用 Node Name 0328 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0328A が画面・出力に表示されること
② ステップ2 の SP81DD0328B が画面・出力に表示されること
③ ステップ3 の SP81DD0328C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0136"><h3>サーバー日次運用 Node Name 0343</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>藍D解除0344ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票藍D解除0344です。藍D解除0344はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録藍D解除0344です。藍D解除0344では運用状態と取得時刻を採取票藍D解除0344へ残します。藍D解除0344ではプール容量不足の見落としを避けるため補助資料も照合する判断藍D解除0344です。藍D解除0344の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録藍D解除0344です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0343を保守記録に説明する必要があります。storage pool 宛先照合 キーマップと取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は宛先照合でキーマップを確認することでキーマップを確認し・キーマップの誤読を防ぐ。</li><li>B. 保守作業で参照する機能は停止確認で停止前の確認を確認することで停止前の確認を確認し・置換条件や復元先を確認せず本を防ぐ。</li><li>C. 保守作業で参照する機能は表示操作で対象欄を追跡することでディレクトリを確認し・コピーグループ未定義を防ぐ。</li><li>D. 保守作業で参照する機能は採取操作で照合欄を点検することで運用状態を確認し・プール容量不足の見落としを防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 解除対象NodeでDの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・解除・運用状・プール容）です。解除時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・解除・運用状・プール容です。stora・宛先照合のA:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は宛先照合 キーマップ（stora・宛先照・キーマ・キーマッ）です。停止確認対象ClienのB:は「Client Restoreで停止前の確認ではリストア確認の」を述べ、対象は停止前の確認 RST14（Clien・停止確・停止前・置換条件）です。切替時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・切替・ディレ・コピーグ）です。Nodeを解除という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・解除・運用状・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0343</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0343について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2243
確認コード SP81DD0343A
画面・出力には SP81DD0343A が表示され、サーバー日次運用 Node Name 0343 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE103
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0343B
画面・出力には SP81DD0343B が表示され、サーバー日次運用 Node Name 0343 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 603 GB
確認コード SP81DD0343C
画面・出力には SP81DD0343C が表示され、サーバー日次運用 Node Name 0343 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0343A が画面・出力に表示されること
② ステップ2 の SP81DD0343B が画面・出力に表示されること
③ ステップ3 の SP81DD0343C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0137"><h3>サーバー日次運用 Node Name 0358</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>黒S解除0359ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票黒S解除0359です。黒S解除0359はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録黒S解除0359です。黒S解除0359では運用状態と取得時刻を採取票黒S解除0359へ残します。黒S解除0359ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断黒S解除0359です。黒S解除0359の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録黒S解除0359です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Node Name 0358の技術的な意味を資料で確認するとき、archive copy group コマンド証跡 回収対象との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はアーカイブコピーの保存期間と宛先を定めるコピー規則をコマンド証跡として確認する。ストレージプで回収対象を確認するときは回収対象の誤読を防ぐ。</li><li>B. 管理対象との関係を表す説明はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。確認操作で状態欄を整理するときはデータベースバックアップ時刻を防ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。</li><li>D. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは登録ドメインの取り違えを防ぐ。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 解除対象NodeでBの記述「Node Nameの運用状態と取得時刻を記録し」に対応する項目はNode Name（Node・解除・運用状・データベ）です。解除時のNodeに関するサーバー運用の仕様は「Node Nameの運用状態と取得時刻を記録し」で、確認対象はNode・解除・運用状・データベです。archi・ストレージのA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則をコマンド証跡とし」を述べ、対象はコマンド証跡 回収対象（archi・ストレ・回収対・回収対象）です。巡回時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・巡回・コピー・コピーグ）です。Manaを確認のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・確認・ドメイ・登録ドメ）です。Nodeを解除という用語は「Node Nameの運用状態と取得時刻を記録し」を指し、Node Name（Node・解除・運用状・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Node Name 0358</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Node Name 0358について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Node Name と 運用状態</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; EXPIRE INVENTORY
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2258
確認コード SP81DD0358A
画面・出力には SP81DD0358A が表示され、サーバー日次運用 Node Name 0358 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE118
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0358B
画面・出力には SP81DD0358B が表示され、サーバー日次運用 Node Name 0358 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Node Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 618 GB
確認コード SP81DD0358C
画面・出力には SP81DD0358C が表示され、サーバー日次運用 Node Name 0358 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0358A が画面・出力に表示されること
② ステップ2 の SP81DD0358B が画面・出力に表示されること
③ ステップ3 の SP81DD0358C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0138"><h3>サーバー日次運用 Server Name 0001</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>橙B巡回0002ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票橙B巡回0002です。橙B巡回0002はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録橙B巡回0002です。橙B巡回0002ではDBバックアップ履歴と取得時刻を採取票橙B巡回0002へ残します。橙B巡回0002では期限切れ処理の未実行を避けるため補助資料も照合する判断橙B巡回0002です。橙B巡回0002の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録橙B巡回0002です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0001の設定や表示を読む前に役割を確認します。サーバー日次運用 Database Backup 0082ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 対象資源に対する働きはバックアップや管理コマンドを決めた時刻に実行する定義である。</li><li>D. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 巡回対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・巡回・DBバッ）です。サーバに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・巡回・DBバッです。Datab・変更のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・変更・期限切れ）です。保護対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護・失敗理由）です。保存期間時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義」を述べ、対象は保存期間確認 レビュー結果（schedu・保存期・レビュー）です。Servを巡回という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・巡回・DBバッ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0001</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0001について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2201
確認コード SP81DD0001A
画面・出力には SP81DD0001A が表示され、サーバー日次運用 Server Name 0001 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE001
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0001B
画面・出力には SP81DD0001B が表示され、サーバー日次運用 Server Name 0001 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 501 GB
確認コード SP81DD0001C
画面・出力には SP81DD0001C が表示され、サーバー日次運用 Server Name 0001 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0001A が画面・出力に表示されること
② ステップ2 の SP81DD0001B が画面・出力に表示されること
③ ステップ3 の SP81DD0001C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0139"><h3>サーバー日次運用 Server Name 0016</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>青Q巡回0017ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票青Q巡回0017です。青Q巡回0017はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録青Q巡回0017です。青Q巡回0017ではDBバックアップ履歴と取得時刻を採取票青Q巡回0017へ残します。青Q巡回0017ではノード状態の誤読を避けるため補助資料も照合する判断青Q巡回0017です。青Q巡回0017の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録青Q巡回0017です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0016に関する障害切り分けの前提を確認しています。クライアントスケジュール Action 0051の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>B. 表示や設定で扱う内容はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 表示や設定で扱う内容はサーバーへ登録されたクライアントを表す管理単位を期限切れ確認する。node 期限切れ確認 更新配布固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 巡回対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・巡回・DBバッ）です。サーバに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・巡回・DBバッです。Actio・復旧のA:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・復旧・開始時刻）です。確認対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・確認・コピーグ）です。期限切れ時のnodeのC:は「サーバーへ登録されたクライアントを表す管理単位を期限切れ確認する」を述べ、対象は期限切れ確認 更新配布（node・期限切・更新配布）です。Servを巡回という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・巡回・DBバッ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0016</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0016について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2216
確認コード SP81DD0016A
画面・出力には SP81DD0016A が表示され、サーバー日次運用 Server Name 0016 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE016
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0016B
画面・出力には SP81DD0016B が表示され、サーバー日次運用 Server Name 0016 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 516 GB
確認コード SP81DD0016C
画面・出力には SP81DD0016C が表示され、サーバー日次運用 Server Name 0016 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0016A が画面・出力に表示されること
② ステップ2 の SP81DD0016B が画面・出力に表示されること
③ ステップ3 の SP81DD0016C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0140"><h3>サーバー日次運用 Server Name 0031</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>白L棚卸0032ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票白L棚卸0032です。白L棚卸0032はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録白L棚卸0032です。白L棚卸0032ではDBバックアップ履歴と取得時刻を採取票白L棚卸0032へ残します。白L棚卸0032ではプール容量不足の見落としを避けるため補助資料も照合する判断白L棚卸0032です。白L棚卸0032の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録白L棚卸0032です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0031を保守記録に説明する必要があります。クライアントスケジュール Start Time 0063と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 保守作業で参照する機能はBackup andで依存関係の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 棚卸対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・棚卸・データベ）です。棚卸時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・棚卸・データベです。監査対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査・失敗理由）です。抑止時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・抑止・ノード登）です。Backを依存関係確のD:は「Backup andで依存関係の確認ではコピーグループの」を述べ、対象は依存関係の確認 CG13（Backup・依存関・確認では）です。Servを棚卸という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・棚卸・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0031</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0031について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2231
確認コード SP81DD0031A
画面・出力には SP81DD0031A が表示され、サーバー日次運用 Server Name 0031 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE031
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0031B
画面・出力には SP81DD0031B が表示され、サーバー日次運用 Server Name 0031 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 531 GB
確認コード SP81DD0031C
画面・出力には SP81DD0031C が表示され、サーバー日次運用 Server Name 0031 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0031A が画面・出力に表示されること
② ステップ2 の SP81DD0031B が画面・出力に表示されること
③ ステップ3 の SP81DD0031C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0141"><h3>サーバー日次運用 Server Name 0046</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>紫G復旧0047ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紫G復旧0047です。紫G復旧0047はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録紫G復旧0047です。紫G復旧0047ではDBバックアップ履歴と取得時刻を採取票紫G復旧0047へ残します。紫G復旧0047ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断紫G復旧0047です。紫G復旧0047の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録紫G復旧0047です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0046の技術的な意味を資料で確認するとき、ポリシーと管理クラス Policy Set 0122との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>B. 管理対象との関係を表す説明はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 管理対象との関係を表す説明はPolicy Domainで停止前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。</li><li>D. 管理対象との関係を表す説明はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・復旧・データベ）です。復旧時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・復旧・データベです。Polic・診断のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断・ディレク）です。計画対象StartのB:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・計画・失敗理由）です。停止確認時のPolicのC:は「Policy Domainで停止前の確認ではポリシードメインの」を述べ、対象は停止前の確認 DOM14（Policy・停止確・確認では）です。Servを復旧という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・復旧・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0046</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0046について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2246
確認コード SP81DD0046A
画面・出力には SP81DD0046A が表示され、サーバー日次運用 Server Name 0046 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE046
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0046B
画面・出力には SP81DD0046B が表示され、サーバー日次運用 Server Name 0046 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 546 GB
確認コード SP81DD0046C
画面・出力には SP81DD0046C が表示され、サーバー日次運用 Server Name 0046 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0046A が画面・出力に表示されること
② ステップ2 の SP81DD0046B が画面・出力に表示されること
③ ステップ3 の SP81DD0046C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0142"><h3>サーバー日次運用 Server Name 0061</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>橙B監査0062ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票橙B監査0062です。橙B監査0062はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録橙B監査0062です。橙B監査0062ではDBバックアップ履歴と取得時刻を採取票橙B監査0062へ残します。橙B監査0062では期限切れ処理の未実行を避けるため補助資料も照合する判断橙B監査0062です。橙B監査0062の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録橙B監査0062です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0061について構成や状態を確認します。ポリシーと管理クラス Policy Set 0137ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 対象資源に対する働きはDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。ポリシーと管理クラス DIRMC 0308固有の属性も確認対象に含める。</li><li>D. 対象資源に対する働きはIncremental Backupで構成監査ではバックアップ運用のである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・監査・データベ）です。監査時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・監査・データベです。診断対象PolicのB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断・ディレク）です。解析時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・解析・ノード登）です。Incrを構成監査のD:は「Incremental Backupで構成監査ではバックアップ運用の」を述べ、対象は構成監査 BKP08（Increm・構成監・構成監査）です。Servを監査という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・監査・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0061</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0061について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2201
確認コード SP81DD0061A
画面・出力には SP81DD0061A が表示され、サーバー日次運用 Server Name 0061 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE061
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0061B
画面・出力には SP81DD0061B が表示され、サーバー日次運用 Server Name 0061 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 561 GB
確認コード SP81DD0061C
画面・出力には SP81DD0061C が表示され、サーバー日次運用 Server Name 0061 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0061A が画面・出力に表示されること
② ステップ2 の SP81DD0061B が画面・出力に表示されること
③ ステップ3 の SP81DD0061C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0143"><h3>サーバー日次運用 Server Name 0076</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>青Q監査0077ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票青Q監査0077です。青Q監査0077はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録青Q監査0077です。青Q監査0077ではDBバックアップ履歴と取得時刻を採取票青Q監査0077へ残します。青Q監査0077ではノード状態の誤読を避けるため補助資料も照合する判断青Q監査0077です。青Q監査0077の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録青Q監査0077です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0076の役割を調べています。ポリシーと管理クラス Management Class 0164の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 表示や設定で扱う内容はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。</li><li>D. 表示や設定で扱う内容はManagement Classで再始動後の確認では管理クラスの オプション確認からDIRMCを読みである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・監査・データベ）です。監査時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・監査・データベです。切替対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・切替・ドメイン）です。抑止時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・抑止・関連ノー）です。Manaを再始動確認のD:は「Management Classで再始動後の確認では管理クラスの」を述べ、対象は再始動後の確認 MC15（Manage・再始動・再始動後）です。Servを監査という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・監査・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0076</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0076について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2216
確認コード SP81DD0076A
画面・出力には SP81DD0076A が表示され、サーバー日次運用 Server Name 0076 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE076
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0076B
画面・出力には SP81DD0076B が表示され、サーバー日次運用 Server Name 0076 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 576 GB
確認コード SP81DD0076C
画面・出力には SP81DD0076C が表示され、サーバー日次運用 Server Name 0076 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0076A が画面・出力に表示されること
② ステップ2 の SP81DD0076B が画面・出力に表示されること
③ ステップ3 の SP81DD0076C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0144"><h3>サーバー日次運用 Server Name 0091</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>白L変更0092ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票白L変更0092です。白L変更0092はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録白L変更0092です。白L変更0092ではDBバックアップ履歴と取得時刻を採取票白L変更0092へ残します。白L変更0092ではプール容量不足の見落としを避けるため補助資料も照合する判断白L変更0092です。白L変更0092の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録白L変更0092です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Server Name 0091」を「ポリシーと管理クラス Policy Set 0152」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。</li><li>C. 保守作業で参照する機能はバックアップや管理コマンドを決めた時刻に実行する定義である。</li><li>D. 保守作業で参照する機能はClient Nodeで障害切り分けではノード管理の ノード照会からLastAccessを読み・ノードに使うである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・変更・データベ）です。変更時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・変更・データベです。保守対象PolicのB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・保守・ディレク）です。復旧手掛時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義」を述べ、対象は状態確認 復旧手掛かり（schedu・復旧手・復旧手掛）です。ClieをノードのD:は「Client Nodeで障害切り分けではノード管理の」を述べ、対象は障害切り分け NODE04（Client・ノード・障害切り）です。Servを変更という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・変更・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0091</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0091について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2231
確認コード SP81DD0091A
画面・出力には SP81DD0091A が表示され、サーバー日次運用 Server Name 0091 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE091
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0091B
画面・出力には SP81DD0091B が表示され、サーバー日次運用 Server Name 0091 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 591 GB
確認コード SP81DD0091C
画面・出力には SP81DD0091C が表示され、サーバー日次運用 Server Name 0091 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0091A が画面・出力に表示されること
② ステップ2 の SP81DD0091B が画面・出力に表示されること
③ ステップ3 の SP81DD0091C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0145"><h3>サーバー日次運用 Server Name 0106</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>紫G移行0107ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紫G移行0107です。紫G移行0107はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録紫G移行0107です。紫G移行0107ではDBバックアップ履歴と取得時刻を採取票紫G移行0107へ残します。紫G移行0107ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断紫G移行0107です。紫G移行0107の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録紫G移行0107です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0106を同一分類のクライアントスケジュール Association 0150と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。クライアントスケジュール Association 0150固有の属性も確認対象に含める。</li><li>C. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>D. 管理対象との関係を表す説明はArchive Operationで代替経路の確認ではアーカイブ運用のである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 移行対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Server・移行・データベ）です。移行時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServe・移行・データベです。保守対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・保守・関連ノー）です。計画時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・計画・ドメイン）です。Archを代替経路確のD:は「Archive Operationで代替経路の確認ではアーカイブ運用」を述べ、対象は代替経路の確認 ARC10（Archiv・代替経・確認では）です。Servを移行という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Server・移行・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0106</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0106について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2246
確認コード SP81DD0106A
画面・出力には SP81DD0106A が表示され、サーバー日次運用 Server Name 0106 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE106
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0106B
画面・出力には SP81DD0106B が表示され、サーバー日次運用 Server Name 0106 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 606 GB
確認コード SP81DD0106C
画面・出力には SP81DD0106C が表示され、サーバー日次運用 Server Name 0106 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0106A が画面・出力に表示されること
② ステップ2 の SP81DD0106B が画面・出力に表示されること
③ ステップ3 の SP81DD0106C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0146"><h3>サーバー日次運用 Server Name 0121</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>橙B診断0122ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票橙B診断0122です。橙B診断0122はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録橙B診断0122です。橙B診断0122ではDBバックアップ履歴と取得時刻を採取票橙B診断0122へ残します。橙B診断0122では期限切れ処理の未実行を避けるため補助資料も照合する判断橙B診断0122です。橙B診断0122の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録橙B診断0122です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0121の設定や表示を読む前に役割を確認します。サーバー日次運用 Expiration Status 0184ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。</li><li>B. 対象資源に対する働きはファイルのバックアップ先や保存期間を決めるポリシー要素を期限切れ確認する。management class 期限切れ確認 宛先定義固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きはDBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・変更確認に使うである。</li><li>D. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 診断対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・診断・データ・期限切れ）です。診断時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・診断・データ・期限切れです。Expir・収集のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・収集・ノード・ノード状）です。期限切れ対象managのB:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を期限切れ確認」を述べ、対象は期限切れ確認 宛先定義（manag・期限切・宛先定・宛先定義）です。変更確認時のDBのC:は「DBで変更後の確認ではサーバーの 履歴照会からBACKUPFULLを」を述べ、対象は変更後の確認 DBBK03（DB・変更確・変更後・データベ）です。Servを診断という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・診断・データ・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0121</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0121について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2201
確認コード SP81DD0121A
画面・出力には SP81DD0121A が表示され、サーバー日次運用 Server Name 0121 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE001
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0121B
画面・出力には SP81DD0121B が表示され、サーバー日次運用 Server Name 0121 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 501 GB
確認コード SP81DD0121C
画面・出力には SP81DD0121C が表示され、サーバー日次運用 Server Name 0121 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0121A が画面・出力に表示されること
② ステップ2 の SP81DD0121B が画面・出力に表示されること
③ ステップ3 の SP81DD0121C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0147"><h3>サーバー日次運用 Server Name 0136</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>青Q診断0137ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票青Q診断0137です。青Q診断0137はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録青Q診断0137です。青Q診断0137ではDBバックアップ履歴と取得時刻を採取票青Q診断0137へ残します。青Q診断0137ではノード状態の誤読を避けるため補助資料も照合する判断青Q診断0137です。青Q診断0137の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録青Q診断0137です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0136に関する障害切り分けの前提を確認しています。クライアントスケジュール Action 0231の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。</li><li>C. 表示や設定で扱う内容は保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する。</li><li>D. 表示や設定で扱う内容はClient Restoreで復旧準備ではリストア確認の 別名復元からrestoredを読み・復旧準備に使うである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 診断対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・診断・データ・ノード状）です。診断時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・診断・データ・ノード状です。確認対象ActioのB:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Actio・確認・開始時・失敗イベ）です。期限切れ時のexpirのC:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」を述べ、対象は期限切れ確認 入力欄（expir・期限切・入力欄・入力欄の）です。Clieを復旧準備のD:は「Client Restoreで復旧準備ではリストア確認の」を述べ、対象は復旧準備 RST05（Clien・復旧準・復旧準・置換条件）です。Servを診断という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・診断・データ・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0136</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0136について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2216
確認コード SP81DD0136A
画面・出力には SP81DD0136A が表示され、サーバー日次運用 Server Name 0136 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE016
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0136B
画面・出力には SP81DD0136B が表示され、サーバー日次運用 Server Name 0136 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 516 GB
確認コード SP81DD0136C
画面・出力には SP81DD0136C が表示され、サーバー日次運用 Server Name 0136 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0136A が画面・出力に表示されること
② ステップ2 の SP81DD0136B が画面・出力に表示されること
③ ステップ3 の SP81DD0136C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0148"><h3>サーバー日次運用 Server Name 0151</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>白L保守0152ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票白L保守0152です。白L保守0152はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録白L保守0152です。白L保守0152ではDBバックアップ履歴と取得時刻を採取票白L保守0152へ残します。白L保守0152ではプール容量不足の見落としを避けるため補助資料も照合する判断白L保守0152です。白L保守0152の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録白L保守0152です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0151を保守記録に説明する必要があります。サーバー日次運用 Storage Pool 0235と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li><li>B. 保守作業で参照する機能はサーバー操作とメッセージを追跡するログを復元前確認する。</li><li>C. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はDBで復旧準備ではサーバーの DBバックアップからANR4550Iを読み・復旧準備に使うである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 保守対象ServeでCの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・保守・データ・プール容）です。保守時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・保守・データ・プール容です。Stora・確認のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・確認・ストレ・プール容）です。復元前確対象activのB:は「サーバー操作とメッセージを追跡するログを復元前確認する」を述べ、対象は復元前確認 管理クラス（activ・復元前・管理ク・管理クラ）です。復旧準備でを復旧準備のD:は「DBで復旧準備ではサーバーの DBバックアップからANR4550Iを」を述べ、対象は復旧準備 DBBK05（DB・復旧準・復旧準・データベ）です。Servを保守という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・保守・データ・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0151</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0151について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2231
確認コード SP81DD0151A
画面・出力には SP81DD0151A が表示され、サーバー日次運用 Server Name 0151 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE031
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0151B
画面・出力には SP81DD0151B が表示され、サーバー日次運用 Server Name 0151 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 531 GB
確認コード SP81DD0151C
画面・出力には SP81DD0151C が表示され、サーバー日次運用 Server Name 0151 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0151A が画面・出力に表示されること
② ステップ2 の SP81DD0151B が画面・出力に表示されること
③ ステップ3 の SP81DD0151C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0149"><h3>サーバー日次運用 Server Name 0166</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>紫G切替0167ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紫G切替0167です。紫G切替0167はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録紫G切替0167です。紫G切替0167ではDBバックアップ履歴と取得時刻を採取票紫G切替0167へ残します。紫G切替0167ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断紫G切替0167です。紫G切替0167の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録紫G切替0167です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0166の技術的な意味を資料で確認するとき、サーバー日次運用 Node Name 0238との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 管理対象との関係を表す説明はPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。</li><li>C. 管理対象との関係を表す説明はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。</li><li>D. 管理対象との関係を表す説明はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 切替対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・切替・データ・データベ）です。切替時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・切替・データ・データベです。Node・確認のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認・運用状・データベ）です。復旧確認対象PolicのB:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Polic・復旧確・復旧後・ノードを）です。巡回時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・巡回・ディレ・ディレク）です。Servを切替という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・切替・データ・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0166</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0166について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2246
確認コード SP81DD0166A
画面・出力には SP81DD0166A が表示され、サーバー日次運用 Server Name 0166 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE046
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0166B
画面・出力には SP81DD0166B が表示され、サーバー日次運用 Server Name 0166 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 546 GB
確認コード SP81DD0166C
画面・出力には SP81DD0166C が表示され、サーバー日次運用 Server Name 0166 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0166A が画面・出力に表示されること
② ステップ2 の SP81DD0166B が画面・出力に表示されること
③ ステップ3 の SP81DD0166C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0150"><h3>サーバー日次運用 Server Name 0181</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>橙B収集0182ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票橙B収集0182です。橙B収集0182はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録橙B収集0182です。橙B収集0182ではDBバックアップ履歴と取得時刻を採取票橙B収集0182へ残します。橙B収集0182では期限切れ処理の未実行を避けるため補助資料も照合する判断橙B収集0182です。橙B収集0182の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録橙B収集0182です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0181について構成や状態を確認します。クライアントスケジュール Schedule Name 0249ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。</li><li>C. 対象資源に対する働きはクライアントに適用するバックアップとアーカイブの規則を束ねる単位を期限切れ確認する。</li><li>D. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・収集・データ・期限切れ）です。収集時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・収集・データ・期限切れです。保護対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・保護・スケジ・関連付け）です。容量表示時のpolicのC:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」を述べ、対象は期限切れ確認 容量表示（polic・容量表・容量表・容量表示）です。Dataを監査のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・監査・期限切・プール容）です。Servを収集という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・収集・データ・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0181</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0181について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2201
確認コード SP81DD0181A
画面・出力には SP81DD0181A が表示され、サーバー日次運用 Server Name 0181 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE061
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0181B
画面・出力には SP81DD0181B が表示され、サーバー日次運用 Server Name 0181 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 561 GB
確認コード SP81DD0181C
画面・出力には SP81DD0181C が表示され、サーバー日次運用 Server Name 0181 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0181A が画面・出力に表示されること
② ステップ2 の SP81DD0181B が画面・出力に表示されること
③ ステップ3 の SP81DD0181C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0151"><h3>サーバー日次運用 Server Name 0196</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>青Q収集0197ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票青Q収集0197です。青Q収集0197はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録青Q収集0197です。青Q収集0197ではDBバックアップ履歴と取得時刻を採取票青Q収集0197へ残します。青Q収集0197ではノード状態の誤読を避けるため補助資料も照合する判断青Q収集0197です。青Q収集0197の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録青Q収集0197です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0196の役割を調べています。クライアントスケジュール Association 0270の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>B. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はファイルのバックアップ先や保存期間を決めるポリシー要素である。</li><li>D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 収集対象ServeでBの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・収集・データ・ノード状）です。収集時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・収集・データ・ノード状です。Assoc・照合のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・照合・関連ノ・開始時刻）です。状態確認時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は状態確認 イベント識別（manag・状態確・イベン・イベント）です。Dataを棚卸のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・棚卸・期限切・データベ）です。Servを収集という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・収集・データ・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0196</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0196について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2216
確認コード SP81DD0196A
画面・出力には SP81DD0196A が表示され、サーバー日次運用 Server Name 0196 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE076
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0196B
画面・出力には SP81DD0196B が表示され、サーバー日次運用 Server Name 0196 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 576 GB
確認コード SP81DD0196C
画面・出力には SP81DD0196C が表示され、サーバー日次運用 Server Name 0196 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0196A が画面・出力に表示されること
② ステップ2 の SP81DD0196B が画面・出力に表示されること
③ ステップ3 の SP81DD0196C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0152"><h3>サーバー日次運用 Server Name 0211</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>白L登録0212ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票白L登録0212です。白L登録0212はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録白L登録0212です。白L登録0212ではDBバックアップ履歴と取得時刻を採取票白L登録0212へ残します。白L登録0212ではプール容量不足の見落としを避けるため補助資料も照合する判断白L登録0212です。白L登録0212の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録白L登録0212です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Server Name 0211」を「サーバー日次運用 Expiration Status 0274」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li><li>B. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はPolicy Domainで依存関係の確認ではポリシードメインのである。</li><li>D. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 登録対象ServeでBの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・登録・データ・プール容）です。登録時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・登録・データ・プール容です。Expir・照合のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・照合・ノード・データベ）です。依存関係時のPolicのC:は「Policy Domainで依存関係の確認ではポリシードメインの」を述べ、対象は依存関係の確認 DOM13（Polic・依存関・確認で・ノードを）です。ノード登録を棚卸のD:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・棚卸・ノード・ディレク）です。Servを登録という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・登録・データ・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0211</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0211について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2231
確認コード SP81DD0211A
画面・出力には SP81DD0211A が表示され、サーバー日次運用 Server Name 0211 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE091
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0211B
画面・出力には SP81DD0211B が表示され、サーバー日次運用 Server Name 0211 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 591 GB
確認コード SP81DD0211C
画面・出力には SP81DD0211C が表示され、サーバー日次運用 Server Name 0211 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0211A が画面・出力に表示されること
② ステップ2 の SP81DD0211B が画面・出力に表示されること
③ ステップ3 の SP81DD0211C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0153"><h3>サーバー日次運用 Server Name 0226</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 上級</p><p>紫G確認0227ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紫G確認0227です。紫G確認0227はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録紫G確認0227です。紫G確認0227ではDBバックアップ履歴と取得時刻を採取票紫G確認0227へ残します。紫G確認0227ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断紫G確認0227です。紫G確認0227の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録紫G確認0227です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0226を同一分類のポリシーと管理クラス Policy Domain 0275と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。</li><li>C. 管理対象との関係を表す説明はClient Nodeで停止前の確認ではノード管理の 占有量照会からLogicalFilesを読みである。</li><li>D. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 確認対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・確認・データ・データベ）です。確認時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・確認・データ・データベです。照合対象PolicのB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・照合・管理ク・コピーグ）です。停止確認時のClienのC:は「Client Nodeで停止前の確認ではノード管理の」を述べ、対象は停止前の確認 NODE14（Clien・停止確・停止前・長期未接）です。Storを監査のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・監査・ストレ・データベ）です。Servを確認という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・確認・データ・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0226</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0226について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2246
確認コード SP81DD0226A
画面・出力には SP81DD0226A が表示され、サーバー日次運用 Server Name 0226 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE106
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0226B
画面・出力には SP81DD0226B が表示され、サーバー日次運用 Server Name 0226 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 606 GB
確認コード SP81DD0226C
画面・出力には SP81DD0226C が表示され、サーバー日次運用 Server Name 0226 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0226A が画面・出力に表示されること
② ステップ2 の SP81DD0226B が画面・出力に表示されること
③ ステップ3 の SP81DD0226C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0154"><h3>サーバー日次運用 Server Name 0241</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>橙B保護0242ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票橙B保護0242です。橙B保護0242はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録橙B保護0242です。橙B保護0242ではDBバックアップ履歴と取得時刻を採取票橙B保護0242へ残します。橙B保護0242では期限切れ処理の未実行を避けるため補助資料も照合する判断橙B保護0242です。橙B保護0242の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録橙B保護0242です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0241の設定や表示を読む前に役割を確認します。クライアントスケジュール Start Time 0258ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。</li><li>B. 対象資源に対する働きはDirectory-containeで復旧後の確認ではストレージプールのである。ストレージプール Directory-container固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きはEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。</li><li>D. 対象資源に対する働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・保護・データ・期限切れ）です。保護時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・保護・データ・期限切れです。Start・保護のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護・失敗理・開始時刻）です。復旧確認対象DirecのB:は「Directory-containeで復旧後の確認ではストレージプー」を述べ、対象は復旧後の確認 POOL06（Direc・復旧確・復旧後・容量使用）です。診断時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・診断・イベン・日次処理）です。Servを保護という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・保護・データ・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0241</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0241について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2201
確認コード SP81DD0241A
画面・出力には SP81DD0241A が表示され、サーバー日次運用 Server Name 0241 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE001
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0241B
画面・出力には SP81DD0241B が表示され、サーバー日次運用 Server Name 0241 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL01
Pool Type DIRECTORY
Estimated Capacity 501 GB
確認コード SP81DD0241C
画面・出力には SP81DD0241C が表示され、サーバー日次運用 Server Name 0241 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0241A が画面・出力に表示されること
② ステップ2 の SP81DD0241B が画面・出力に表示されること
③ ステップ3 の SP81DD0241C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0155"><h3>サーバー日次運用 Server Name 0256</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 初級</p><p>青Q保護0257ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票青Q保護0257です。青Q保護0257はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録青Q保護0257です。青Q保護0257ではDBバックアップ履歴と取得時刻を採取票青Q保護0257へ残します。青Q保護0257ではノード状態の誤読を避けるため補助資料も照合する判断青Q保護0257です。青Q保護0257の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録青Q保護0257です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0256に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Management Class 0329の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。</li><li>C. 表示や設定で扱う内容はArchive Operationで性能影響の確認ではアーカイブ運用のである。</li><li>D. 表示や設定で扱う内容はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 保護対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・保護・データ・ノード状）です。保護時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・保護・データ・ノード状です。計画対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・計画・ドメイ・管理クラ）です。性能影響時のArchiのC:は「Archive Operationで性能影響の確認ではアーカイブ運用」を述べ、対象は性能影響の確認 ARC11（Archi・性能影・確認で・バックア）です。Expiを診断のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・診断・ノード・ノード状）です。Servを保護という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・保護・データ・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0256</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0256について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2216
確認コード SP81DD0256A
画面・出力には SP81DD0256A が表示され、サーバー日次運用 Server Name 0256 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE016
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0256B
画面・出力には SP81DD0256B が表示され、サーバー日次運用 Server Name 0256 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL02
Pool Type DIRECTORY
Estimated Capacity 516 GB
確認コード SP81DD0256C
画面・出力には SP81DD0256C が表示され、サーバー日次運用 Server Name 0256 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0256A が画面・出力に表示されること
② ステップ2 の SP81DD0256B が画面・出力に表示されること
③ ステップ3 の SP81DD0256C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0156"><h3>サーバー日次運用 Server Name 0271</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>白L照合0272ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票白L照合0272です。白L照合0272はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録白L照合0272です。白L照合0272ではDBバックアップ履歴と取得時刻を採取票白L照合0272へ残します。白L照合0272ではプール容量不足の見落としを避けるため補助資料も照合する判断白L照合0272です。白L照合0272の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録白L照合0272です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0271を保守記録に説明する必要があります。ポリシーと管理クラス Management Class 0299と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は抑止でドメイン割当を証跡に残し・Management Classのドメイン割当と取得時刻を記。</li><li>B. 保守作業で参照する機能は照合でデータベースを証跡に残し・Server NameのDBバックアップ履歴と取得時刻を記録。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能は変更確認で変更前の確認を証跡に残し・Client Restoreで変更前の確認ではリストア確認の。</li><li>D. 保守作業で参照する機能は保守でノード登録値を証跡に残し・DIRMCのノード登録値と取得時刻を記録し。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 照合対象ServeでBの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・照合・データ・プール容）です。照合時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・照合・データ・プール容です。Manag・抑止のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・抑止・ドメイ・コピーグ）です。変更確認時のClienのC:は「Client Restoreで変更前の確認ではリストア確認の」を述べ、対象は変更前の確認 RST02（Clien・変更確・変更前・置換条件）です。ディレクを保守のD:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・保守・ノード・ディレク）です。Servを照合という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・照合・データ・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0271</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0271について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2231
確認コード SP81DD0271A
画面・出力には SP81DD0271A が表示され、サーバー日次運用 Server Name 0271 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE031
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0271B
画面・出力には SP81DD0271B が表示され、サーバー日次運用 Server Name 0271 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL03
Pool Type DIRECTORY
Estimated Capacity 531 GB
確認コード SP81DD0271C
画面・出力には SP81DD0271C が表示され、サーバー日次運用 Server Name 0271 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0271A が画面・出力に表示されること
② ステップ2 の SP81DD0271B が画面・出力に表示されること
③ ステップ3 の SP81DD0271C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0157"><h3>サーバー日次運用 Server Name 0286</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>紫G抑止0287ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票紫G抑止0287です。紫G抑止0287はサーバー日次運用の確認操作でサーバー日次運用の状態欄を整理する記録紫G抑止0287です。紫G抑止0287ではDBバックアップ履歴と取得時刻を採取票紫G抑止0287へ残します。紫G抑止0287ではDBバックアップ時刻の記録漏れを避けるため補助資料も照合する判断紫G抑止0287です。紫G抑止0287の用語整理ではサーバー日次運用の対象値を実在出力で読み分けする記録紫G抑止0287です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0286の技術的な意味を資料で確認するとき、ポリシーと管理クラス Management Class 0299との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。</li><li>B. 管理対象との関係を表す説明はIncremental Backupで障害切り分けではバックアップ運用の 増分実行からobjectsを読みである。バックアップで障害切り分けを確認するときは除外規則や失敗ファイルを見ずを防ぐ。</li><li>C. 管理対象との関係を表す説明はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。確認操作で状態欄を整理するときはデータベースバックアップ時刻を防ぐ。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは登録ドメインの取り違えを防ぐ。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 抑止対象ServeでCの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・抑止・データ・データベ）です。抑止時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・抑止・データ・データベです。Manag・抑止のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・抑止・ドメイ・コピーグ）です。バックア対象IncreのB:は「Incremental Backupで障害切り分けではバックアップ運」を述べ、対象は障害切り分け BKP04（Incre・バック・障害切・除外規則）です。Poliを変更のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・変更・ディレ・登録ドメ）です。Servを抑止という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・抑止・データ・データベ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0286</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0286について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2246
確認コード SP81DD0286A
画面・出力には SP81DD0286A が表示され、サーバー日次運用 Server Name 0286 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE046
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0286B
画面・出力には SP81DD0286B が表示され、サーバー日次運用 Server Name 0286 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL04
Pool Type DIRECTORY
Estimated Capacity 546 GB
確認コード SP81DD0286C
画面・出力には SP81DD0286C が表示され、サーバー日次運用 Server Name 0286 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0286A が画面・出力に表示されること
② ステップ2 の SP81DD0286B が画面・出力に表示されること
③ ステップ3 の SP81DD0286C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0158"><h3>サーバー日次運用 Server Name 0301</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>橙B解析0302ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票橙B解析0302です。橙B解析0302はサーバー日次運用の記録操作でサーバー日次運用の証跡欄を照合する記録橙B解析0302です。橙B解析0302ではDBバックアップ履歴と取得時刻を採取票橙B解析0302へ残します。橙B解析0302では期限切れ処理の未実行を避けるため補助資料も照合する判断橙B解析0302です。橙B解析0302の用語整理ではサーバー日次運用の対象値を実在出力で比較する記録橙B解析0302です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0301について構成や状態を確認します。ポリシーと管理クラス Management Class 0314ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは解析でデータベースを証跡に残し・Server NameのDBバックアップ履歴と取得時刻を記録。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きは解析でドメイン割当を証跡に残し・Management Classのドメイン割当と取得時刻を記。</li><li>C. 対象資源に対する働きは変更確認で変更後の確認を証跡に残し・Archive Operationで変更後の確認ではアーカイ。</li><li>D. 対象資源に対する働きは収集でディレクトリを証跡に残し・Policy Setのディレクトリ管理クラスと取得時刻を記録。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象ServeでAの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・解析・データ・期限切れ）です。解析時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・解析・データ・期限切れです。解析対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・解析・ドメイ・ディレク）です。変更確認時のArchiのC:は「Archive Operationで変更後の確認ではアーカイブ運用の」を述べ、対象は変更後の確認 ARC03（Archi・変更確・変更後・バックア）です。Poliを収集のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・収集・ディレ・管理クラ）です。Servを解析という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・解析・データ・期限切れ）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0301</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0301について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2201
確認コード SP81DD0301A
画面・出力には SP81DD0301A が表示され、サーバー日次運用 Server Name 0301 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE061
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0301B
画面・出力には SP81DD0301B が表示され、サーバー日次運用 Server Name 0301 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL05
Pool Type DIRECTORY
Estimated Capacity 561 GB
確認コード SP81DD0301C
画面・出力には SP81DD0301C が表示され、サーバー日次運用 Server Name 0301 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0301A が画面・出力に表示されること
② ステップ2 の SP81DD0301B が画面・出力に表示されること
③ ステップ3 の SP81DD0301C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0159"><h3>サーバー日次運用 Server Name 0316</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>青Q解析0317ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票青Q解析0317です。青Q解析0317はサーバー日次運用の保守操作でサーバー日次運用の監査欄を保存する記録青Q解析0317です。青Q解析0317ではDBバックアップ履歴と取得時刻を採取票青Q解析0317へ残します。青Q解析0317ではノード状態の誤読を避けるため補助資料も照合する判断青Q解析0317です。青Q解析0317の用語整理ではサーバー日次運用の対象値を実在出力で区別する記録青Q解析0317です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> サーバー日次運用 Server Name 0316の役割を調べています。クライアントスケジュール Action 0321の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。主操作で出力欄を評価するときは関連付け漏れを防ぐ。</li><li>B. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。保守操作で監査欄を保存するときはノード状態の誤読を防ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はIncremental Backupで依存関係の確認ではバックアップ運用のである。依存関係確認で依存関係の確を確認するときは除外規則や失敗ファイルを見ずを防ぐ。</li><li>D. 表示や設定で扱う内容はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 解析対象ServeでBの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・解析・データ・ノード状）です。解析時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・解析・データ・ノード状です。Actio・計画のA:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Actio・計画・開始時・関連付け）です。依存関係時のIncreのC:は「Incremental Backupで依存関係の確認ではバックアップ」を述べ、対象は依存関係の確認 BKP13（Incre・依存関・依存関・除外規則）です。Poliを保守のD:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・保守・管理ク・コピーグ）です。Servを解析という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・解析・データ・ノード状）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0316</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0316について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2216
確認コード SP81DD0316A
画面・出力には SP81DD0316A が表示され、サーバー日次運用 Server Name 0316 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE076
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0316B
画面・出力には SP81DD0316B が表示され、サーバー日次運用 Server Name 0316 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL06
Pool Type DIRECTORY
Estimated Capacity 576 GB
確認コード SP81DD0316C
画面・出力には SP81DD0316C が表示され、サーバー日次運用 Server Name 0316 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0316A が画面・出力に表示されること
② ステップ2 の SP81DD0316B が画面・出力に表示されること
③ ステップ3 の SP81DD0316C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>


<section class="kb-item" id="c14-i0160"><h3>サーバー日次運用 Server Name 0331</h3><p class="kb-meta">分類: サーバー運用 ・ 難易度: 中級</p><p>白L計画0332ではIBM Spectrum Protect 8.1 の サーバー運用を扱う採取票白L計画0332です。白L計画0332はサーバー日次運用の採取操作でサーバー日次運用の照合欄を点検する記録白L計画0332です。白L計画0332ではDBバックアップ履歴と取得時刻を採取票白L計画0332へ残します。白L計画0332ではプール容量不足の見落としを避けるため補助資料も照合する判断白L計画0332です。白L計画0332の用語整理ではサーバー日次運用の対象値を実在出力で評価する記録白L計画0332です。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「サーバー日次運用 Server Name 0331」を「reclamation 保存期間確認 画面タグ」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は保存期間確認で画面タグを確認することで画面タグを確認し・画面タグの誤読を防ぐ。</li><li>B. 保守作業で参照する機能は確認操作で状態欄を整理することで期限切れ処理を確認し・データベースバックアップ時刻を防ぐ。</li><li>C. 保守作業で参照する機能は確認操作で状態欄を整理することで運用状態を確認し・データベースバックアップ時刻を防ぐ。</li><li>D. 保守作業で参照する機能は採取操作で照合欄を点検することでデータベースを確認し・プール容量不足の見落としを防ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 計画対象ServeでDの記述「Server NameのDBバックアップ履歴と取得時刻を記録し」に対応する項目はServer Name（Serve・計画・データ・プール容）です。計画時のServeに関するサーバー運用の仕様は「Server NameのDBバックアップ履歴と取得時刻を記録し」で、確認対象はServ・計画・データ・プール容です。recla・保存期間確のA:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は保存期間確認 画面タグ（recla・保存期・画面タ・画面タグ）です。棚卸対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・棚卸・期限切・データベ）です。切替時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・切替・運用状・データベ）です。Servを計画という用語は「Server NameのDBバックアップ履歴と取得時」を指し、Server Name（Serve・計画・データ・プール容）に該当します。</p><p class="kb-src"><strong>出典:</strong> SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>サーバー日次運用 Server Name 0331</strong></p><p>検証目的: サーバー日次運用のサーバー日次運用 Server Name 0331について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。</p><p>前提条件: 対象資料を確認済み。対象=Server Name と DBバックアップ履歴</p><p>セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; QUERY STATUS
→ Enter を押す
［画面・出力］
Server Name TSM01
Availability enabled
Database Backup completed at 2231
確認コード SP81DD0331A
画面・出力には SP81DD0331A が表示され、サーバー日次運用 Server Name 0331 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY NODE
→ Enter を押す
［画面・出力］
Node Name NODE091
Platform AIX
Policy Domain STANDARD
Contact admin@example.invalid
確認コード SP81DD0331B
画面・出力には SP81DD0331B が表示され、サーバー日次運用 Server Name 0331 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Server Name を読むため、サーバー日次運用 の対象値を表示します。
［操作（入力）］
IBM Spectrum Protect 8.1 操作画面またはコマンド環境
COMMAND ===&gt; dsmadmc QUERY STATUS
→ Enter を押す
［画面・出力］
Storage Pool DIRPOOL00
Pool Type DIRECTORY
Estimated Capacity 591 GB
確認コード SP81DD0331C
画面・出力には SP81DD0331C が表示され、サーバー日次運用 Server Name 0331 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の SP81DD0331A が画面・出力に表示されること
② ステップ2 の SP81DD0331B が画面・出力に表示されること
③ ステップ3 の SP81DD0331C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en</p></div></details></section>
