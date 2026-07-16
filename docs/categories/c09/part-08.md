---
search:
  exclude: true
---

# GDPS 災害対策・サイトスイッチ — 詳細 (8/8)

[← GDPS 災害対策・サイトスイッチ の概要へ戻る](index.md)


## GDPS 災害対策・サイトスイッチ > z/OS Global Mirror ベストプラクティス

### Parameters that optimize reader performance {#c09-i1035}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Parameters that optimize reader performanceは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 優先検分の災害対策管理に関する Parameters that optimizeの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず優先検分の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検分の災害対策管理の証跡として保存して根拠にする。
    - C. Parameters that optimizeの変更点を出力本文から切り離して優先検分の災害対策管理の承認欄のみ残す。
    - D. 同じ画面で対象行と GEO267I を読み、優先検分の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では Parameters that optimize は「Parameters that optimizeの状態と出力メッセージを結び付ける優先検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では Parameters that optimizeの出力行と GEO267I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明のみに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では Parameters that optimizeを GDPS の確認記録に残し、対象名は優先検分対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### Parameters that optimize volume copy activity {#c09-i1036}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Parameters that optimize volume copy activityは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 記録検分の災害対策管理に関係する Parameters that optimizeの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK で得た表示本文を使い、記録検分の採否を説明欄に結び付ける。 ✅
    - B. Parameters that optimizeの名称と担当者名のみを残して記録検分の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で記録検分の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず記録検分の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では Parameters that optimize は「Parameters that optimizeの用途を災害対策管理の表示で確認する記録検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では GDPS の Parameters that optimizeと GEO267I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明のみに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では Parameters that optimizeを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は記録検分用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### Performance monitoring and analysis {#c09-i1037}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Performance monitoring and analysisは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116

??? question "確認問題（1問）"
    **問題.** 比較検分の災害対策管理で Performance monitoring aの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Performance monitoring aの出力を取らず比較検分の災害対策管理の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較検分として引き継ぐ。 ✅
    - C. GDPS PANEL CHECK を省略して比較検分の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検分の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では Performance monitoring a は「比較検分の災害対策管理に関係する定義値と表示行を照合する比較検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では Performance monitoring aの属性行と GEO267I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明のみに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では Performance monitoring aを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は比較検分初出です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116



### Performance troubleshooting {#c09-i1038}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Performance troubleshootingは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116

??? question "確認問題（1問）"
    **問題.** 順序検分の災害対策管理で災害対策管理の運用確認を行います。Performance troubleshootの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で順序検分の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず順序検分の災害対策管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序検分の確認にする。 ✅
    - D. Performance troubleshootの属性行を読まず順序検分の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では Performance troubleshoot は「GDPS で Performance troubleshootの扱いを記録する順序検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では Performance troubleshootの表示結果と GEO267I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明のみに寄り、判定名は順序検分不足です。順序検分資料では Performance troubleshootの使い方を出典欄から追跡し、資料名は順序検分資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116



### Planned outage support {#c09-i1039}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Planned outage supportは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116

??? question "確認問題（1問）"
    **問題.** 値域検分の災害対策管理に関する Planned outage supportの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず値域検分の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検分の災害対策管理の証跡として保存して根拠にする。
    - C. Planned outage supportの変更点を出力本文から切り離して値域検分の災害対策管理の承認欄のみ残す。
    - D. GDPS の表示形式に沿って根拠行を採り、値域検分の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では Planned outage support は「Planned outage supportの状態と出力メッセージを結び付ける値域検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では Planned outage supportの出力行と GEO267I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明のみに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では Planned outage supportを GDPS の確認記録に残し、対象名は値域検分対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116



### Planning for configuration and workload changes {#c09-i1040}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Planning for configuration and workload changesは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 警告検分の災害対策管理に関係する Planning for configuratiの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告検分で再確認できる形にする。 ✅
    - B. Planning for configuratiの名称と担当者名のみを残して警告検分の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で警告検分の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず警告検分の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では Planning for configurati は「Planning for configuratiの用途を災害対策管理の表示で確認する警告検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では GDPS の Planning for configuratiと GEO267I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明のみに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では Planning for configuratiを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は警告検分用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Planning to protect critical data and applications {#c09-i1041}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Planning to protect critical data and applicationsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 復旧検分の災害対策管理で Planning to protect critの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Planning to protect critの出力を取らず復旧検分の災害対策管理の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧検分の確認値として扱う。 ✅
    - C. GDPS PANEL CHECK を省略して復旧検分の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検分の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では Planning to protect crit は「復旧検分の災害対策管理に関係する定義値と表示行を照合する復旧検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では Planning to protect critの属性行と GEO267I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明のみに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では Planning to protect critを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は復旧検分初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Preparing for initial deployment {#c09-i1042}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Preparing for initial deploymentは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.58 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.58

??? question "確認問題（1問）"
    **問題.** 監査検分の災害対策管理で災害対策管理の運用確認を行います。Preparing for initial deの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で監査検分の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず監査検分の災害対策管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査検分の根拠を固定する。 ✅
    - D. Preparing for initial deの属性行を読まず監査検分の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では Preparing for initial de は「GDPS で Preparing for initial deの扱いを記録する監査検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では Preparing for initial deの表示結果と GEO267I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明のみに寄り、判定名は監査検分不足です。監査検分資料では Preparing for initial deの使い方を出典欄から追跡し、資料名は監査検分資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.58



### Primary disk systems {#c09-i1043}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Primary disk systemsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111

??? question "確認問題（1問）"
    **問題.** 変更検分の災害対策管理に関する Primary disk systemsの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず変更検分の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検分の災害対策管理の証跡として保存して根拠にする。
    - C. Primary disk systemsの変更点を出力本文から切り離して変更検分の災害対策管理の承認欄のみ残す。
    - D. GEO267I を含む表示を保存し、説明欄との差分を変更検分で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では Primary disk systems は「Primary disk systemsの状態と出力メッセージを結び付ける変更検分項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では Primary disk systemsの出力行と GEO267I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明のみに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では Primary disk systemsを GDPS の確認記録に残し、対象名は変更検分対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111



### Primary site definitions {#c09-i1044}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Primary site definitionsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40

??? question "確認問題（1問）"
    **問題.** 構文確認の災害対策管理に関係する Primary site definitionsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果から対象行を抜き出し、構文確認の証跡として残す。 ✅
    - B. Primary site definitionsの名称と担当者名のみを残して構文確認の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で構文確認の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず構文確認の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では Primary site definitions は「Primary site definitionsの用途を災害対策管理の表示で確認する構文確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では GDPS の Primary site definitionsと GEO267I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明のみに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では Primary site definitionsを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は構文確認用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40



### Primary systems {#c09-i1045}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Primary systemsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111

??? question "確認問題（1問）"
    **問題.** 展開確認の災害対策管理で Primary systemsの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Primary systemsの出力を取らず展開確認の災害対策管理の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開確認の確認記録にまとめる。 ✅
    - C. GDPS PANEL CHECK を省略して展開確認の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開確認の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では Primary systems は「展開確認の災害対策管理に関係する定義値と表示行を照合する展開確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では Primary systemsの属性行と GEO267I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明のみに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では Primary systemsを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は展開確認初出です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111



### Primary systems performance monitoring {#c09-i1046}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Primary systems performance monitoringは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111

??? question "確認問題（1問）"
    **問題.** 呼出確認の災害対策管理で災害対策管理の運用確認を行います。Primary systems performaの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で呼出確認の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず呼出確認の災害対策管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認の根拠にする。 ✅
    - D. Primary systems performaの属性行を読まず呼出確認の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では Primary systems performa は「GDPS で Primary systems performaの扱いを記録する呼出確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では Primary systems performaの表示結果と GEO267I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明のみに寄り、判定名は呼出確認不足です。呼出確認資料では Primary systems performaの使い方を出典欄から追跡し、資料名は呼出確認資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111



### Processor requirement considerations for SDM {#c09-i1047}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Processor requirement considerations for SDMは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 置換確認の災害対策管理に関する Processor requirement coの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず置換確認の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換確認の災害対策管理の証跡として保存して根拠にする。
    - C. Processor requirement coの変更点を出力本文から切り離して置換確認の災害対策管理の承認欄のみ残す。
    - D. 同じ画面で対象行と GEO267I を読み、置換確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では Processor requirement co は「Processor requirement coの状態と出力メッセージを結び付ける置換確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では Processor requirement coの出力行と GEO267I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明のみに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では Processor requirement coを GDPS の確認記録に残し、対象名は置換確認対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Recovery site definitions {#c09-i1048}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Recovery site definitionsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 終端確認の災害対策管理に関係する Recovery site definitionの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK で得た表示本文を使い、終端確認の採否を説明欄に結び付ける。 ✅
    - B. Recovery site definitionの名称と担当者名のみを残して終端確認の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で終端確認の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず終端確認の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では Recovery site definition は「Recovery site definitionの用途を災害対策管理の表示で確認する終端確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では GDPS の Recovery site definitionと GEO267I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明のみに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では Recovery site definitionを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は終端確認用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Recovery site in a production sysplex {#c09-i1049}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Recovery site in a production sysplexは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 探索確認の災害対策管理で Recovery site in a produの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Recovery site in a produの出力を取らず探索確認の災害対策管理の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索確認として引き継ぐ。 ✅
    - C. GDPS PANEL CHECK を省略して探索確認の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索確認の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では Recovery site in a produ は「探索確認の災害対策管理に関係する定義値と表示行を照合する探索確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では Recovery site in a produの属性行と GEO267I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明のみに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では Recovery site in a produを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は探索確認初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Requirements for z/OS Global Mirror {#c09-i1050}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Requirements for z/OS Global Mirrorは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 上書確認のRequirements for z/OS Global Mirrorで災害対策管理の運用確認を行います。Requirements for z 属性の根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で上書確認のRequirements for z/OS Global Mirrorを確認した扱いにする。
    - B. GEO267I の有無を確認せず上書確認のRequirements for z/OS Global Mirrorを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 ✅
    - D. Requirements for z 属性の属性行を読まず上書確認のRequirements for z/OS Global Mirrorの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では Requirements for z 属性 は「GDPS で Requirements for z 属性の扱いを記録する上書確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では Requirements for z 属性の表示結果と GEO267I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明のみに寄り、判定名は上書確認不足です。上書確認資料では Requirements for z 属性の使い方を出典欄から追跡し、資料名は上書確認資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Resource contention {#c09-i1051}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Resource contentionは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 出力確認の災害対策管理に関する Resource contentionの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず出力確認の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の災害対策管理の証跡として保存して根拠にする。
    - C. Resource contentionの変更点を出力本文から切り離して出力確認の災害対策管理の承認欄のみ残す。
    - D. GDPS の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では Resource contention は「Resource contentionの状態と出力メッセージを結び付ける出力確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では Resource contentionの出力行と GEO267I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では Resource contentionを GDPS の確認記録に残し、対象名は出力確認対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### SAN monitoring {#c09-i1052}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

SAN monitoringは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116

??? question "確認問題（1問）"
    **問題.** 条件確認の災害対策管理に関係する SAN monitoringの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 ✅
    - B. SAN monitoringの名称と担当者名のみを残して条件確認の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で条件確認の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず条件確認の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では SAN monitoring は「SAN monitoringの用途を災害対策管理の表示で確認する条件確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では GDPS の SAN monitoringと GEO267I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では SAN monitoringを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は条件確認用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.116



### SDM location {#c09-i1053}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

SDM locationは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40

??? question "確認問題（1問）"
    **問題.** 優先確認の災害対策管理に関する SDM locationの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず優先確認の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先確認の災害対策管理の証跡として保存して根拠にする。
    - C. SDM locationの変更点を出力本文から切り離して優先確認の災害対策管理の承認欄のみ残す。
    - D. GEO267I を含む表示を保存し、説明欄との差分を優先確認で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では SDM location は「SDM locationの状態と出力メッセージを結び付ける優先確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では SDM locationの出力行と GEO267I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明のみに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では SDM locationを GDPS の確認記録に残し、対象名は優先確認対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40



### SDM resources {#c09-i1054}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

SDM resourcesは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40

??? question "確認問題（1問）"
    **問題.** 記録確認の災害対策管理に関係する SDM resourcesの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果から対象行を抜き出し、記録確認の証跡として残す。 ✅
    - B. SDM resourcesの名称と担当者名のみを残して記録確認の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で記録確認の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず記録確認の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では SDM resources は「SDM resourcesの用途を災害対策管理の表示で確認する記録確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では GDPS の SDM resourcesと GEO267I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明のみに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では SDM resourcesを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は記録確認用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40



### SDM session considerations {#c09-i1055}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

SDM session considerationsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40

??? question "確認問題（1問）"
    **問題.** 比較確認の災害対策管理で SDM session consideratioの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. SDM session consideratioの出力を取らず比較確認の災害対策管理の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較確認の確認記録にまとめる。 ✅
    - C. GDPS PANEL CHECK を省略して比較確認の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較確認の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では SDM session consideratio は「比較確認の災害対策管理に関係する定義値と表示行を照合する比較確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では SDM session consideratioの属性行と GEO267I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明のみに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では SDM session consideratioを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は比較確認初出です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40



### Scenarios for installation deployment and upgrade {#c09-i1056}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Scenarios for installation deployment and upgradeは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 区切確認の災害対策管理で Scenarios for installatiの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Scenarios for installatiの出力を取らず区切確認の災害対策管理の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 ✅
    - C. GDPS PANEL CHECK を省略して区切確認の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では Scenarios for installati は「区切確認の災害対策管理に関係する定義値と表示行を照合する区切確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では Scenarios for installatiの属性行と GEO267I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では Scenarios for installatiを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は区切確認初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Scenarios for ongoing operations {#c09-i1057}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Scenarios for ongoing operationsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 範囲確認の災害対策管理で災害対策管理の運用確認を行います。Scenarios for ongoing opの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で範囲確認の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず範囲確認の災害対策管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 ✅
    - D. Scenarios for ongoing opの属性行を読まず範囲確認の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では Scenarios for ongoing op は「GDPS で Scenarios for ongoing opの扱いを記録する範囲確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では Scenarios for ongoing opの表示結果と GEO267I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では Scenarios for ongoing opの使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Software requirements {#c09-i1058}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Software requirementsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40

??? question "確認問題（1問）"
    **問題.** 順序確認の災害対策管理で災害対策管理の運用確認を行います。Software requirementsの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で順序確認の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず順序確認の災害対策管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 ✅
    - D. Software requirementsの属性行を読まず順序確認の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では Software requirements は「GDPS で Software requirementsの扱いを記録する順序確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では Software requirementsの表示結果と GEO267I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明のみに寄り、判定名は順序確認不足です。順序確認資料では Software requirementsの使い方を出典欄から追跡し、資料名は順序確認資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40



### Storage management subsystem {#c09-i1059}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Storage management subsystemは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.58 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.58

??? question "確認問題（1問）"
    **問題.** 値域確認の災害対策管理に関する Storage management subsyの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず値域確認の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域確認の災害対策管理の証跡として保存して根拠にする。
    - C. Storage management subsyの変更点を出力本文から切り離して値域確認の災害対策管理の承認欄のみ残す。
    - D. 同じ画面で対象行と GEO267I を読み、値域確認の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では Storage management subsy は「Storage management subsyの状態と出力メッセージを結び付ける値域確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では Storage management subsyの出力行と GEO267I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明のみに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では Storage management subsyを GDPS の確認記録に残し、対象名は値域確認対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.58



### Storage requirements {#c09-i1060}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Storage requirementsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40

??? question "確認問題（1問）"
    **問題.** 警告確認の災害対策管理に関係する Storage requirementsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 ✅
    - B. Storage requirementsの名称と担当者名のみを残して警告確認の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で警告確認の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず警告確認の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では Storage requirements は「Storage requirementsの用途を災害対策管理の表示で確認する警告確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では GDPS の Storage requirementsと GEO267I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明のみに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では Storage requirementsを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は警告確認用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.40



### Suspending a zGM session {#c09-i1061}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Suspending a zGM sessionは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 復旧確認の災害対策管理で Suspending a zGM sessionの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Suspending a zGM sessionの出力を取らず復旧確認の災害対策管理の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 ✅
    - C. GDPS PANEL CHECK を省略して復旧確認の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Suspending a zGM session は「復旧確認の災害対策管理に関係する定義値と表示行を照合する復旧確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Suspending a zGM sessionの属性行と GEO267I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Suspending a zGM sessionを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は復旧確認初出です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### Suspending volumes {#c09-i1062}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Suspending volumesは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111

??? question "確認問題（1問）"
    **問題.** 監査確認の災害対策管理で災害対策管理の運用確認を行います。Suspending volumesの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で監査確認の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず監査確認の災害対策管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 ✅
    - D. Suspending volumesの属性行を読まず監査確認の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では Suspending volumes は「GDPS で Suspending volumesの扱いを記録する監査確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では Suspending volumesの表示結果と GEO267I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明のみに寄り、判定名は監査確認不足です。監査確認資料では Suspending volumesの使い方を出典欄から追跡し、資料名は監査確認資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111



### System Data Mover {#c09-i1063}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

System Data Moverは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 変更確認の災害対策管理に関する System Data Moverの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず変更確認の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更確認の災害対策管理の証跡として保存して根拠にする。
    - C. System Data Moverの変更点を出力本文から切り離して変更確認の災害対策管理の承認欄のみ残す。
    - D. GDPS の表示形式に沿って根拠行を採り、変更確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では System Data Mover は「System Data Moverの状態と出力メッセージを結び付ける変更確認項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では System Data Moverの出力行と GEO267I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明のみに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では System Data Moverを GDPS の確認記録に残し、対象名は変更確認対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### System Data Mover considerations {#c09-i1064}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

System Data Mover considerationsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67

??? question "確認問題（1問）"
    **問題.** 構文照合の災害対策管理に関係する System Data Mover considの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文照合で再確認できる形にする。 ✅
    - B. System Data Mover considの名称と担当者名のみを残して構文照合の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で構文照合の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず構文照合の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では System Data Mover consid は「System Data Mover considの用途を災害対策管理の表示で確認する構文照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では GDPS の System Data Mover considと GEO267I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明のみに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では System Data Mover considを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は構文照合用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67



### Terms and process definitions for z/OS Global Mirror {#c09-i1065}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Terms and process definitions for z/OS Global Mirrorは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 展開照合の災害対策管理で Terms and process definiの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Terms and process definiの出力を取らず展開照合の災害対策管理の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開照合の確認値として扱う。 ✅
    - C. GDPS PANEL CHECK を省略して展開照合の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開照合の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では Terms and process defini は「展開照合の災害対策管理に関係する定義値と表示行を照合する展開照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では Terms and process definiの属性行と GEO267I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明のみに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では Terms and process definiを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は展開照合初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Testing z/OS Global Mirror {#c09-i1066}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Testing z/OS Global Mirrorは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67

??? question "確認問題（1問）"
    **問題.** 呼出照合のTesting z/OS Global Mirrorで災害対策管理の運用確認を行います。Testing z 属性の根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で呼出照合のTesting z/OS Global Mirrorを確認した扱いにする。
    - B. GEO267I の有無を確認せず呼出照合のTesting z/OS Global Mirrorを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出照合の根拠を固定する。 ✅
    - D. Testing z 属性の属性行を読まず呼出照合のTesting z/OS Global Mirrorの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では Testing z 属性 は「GDPS で Testing z 属性の扱いを記録する呼出照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では Testing z 属性の表示結果と GEO267I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明のみに寄り、判定名は呼出照合不足です。呼出照合資料では Testing z 属性の使い方を出典欄から追跡し、資料名は呼出照合資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67



### The MzGM Incremental Resync function {#c09-i1067}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

The MzGM Incremental Resync functionは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 終端照合の災害対策管理に関係する The MzGM Incremental Resの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果から対象行を抜き出し、終端照合の証跡として残す。 ✅
    - B. The MzGM Incremental Resの名称と担当者名のみを残して終端照合の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で終端照合の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず終端照合の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では The MzGM Incremental Res は「The MzGM Incremental Resの用途を災害対策管理の表示で確認する終端照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では GDPS の The MzGM Incremental Resと GEO267I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では The MzGM Incremental Resを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は終端照合用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### The data set for zGM {#c09-i1068}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

The data set for zGMは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 置換照合の災害対策管理に関する The data set for zGM の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず置換照合の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換照合の災害対策管理の証跡として保存して根拠にする。
    - C. The data set for zGM の変更点を出力本文から切り離して置換照合の災害対策管理の承認欄のみ残す。
    - D. GEO267I を含む表示を保存し、説明欄との差分を置換照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では The data set for zGM は「The data set for zGM の状態と出力メッセージを結び付ける置換照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では The data set for zGM の出力行と GEO267I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明のみに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では The data set for zGM を GDPS の確認記録に残し、対象名は置換照合対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### The zGM enhanced multiple reader (enhanced reader) function {#c09-i1069}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

The zGM enhanced multiple reader (enhanced reader) functionは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 探索照合の災害対策管理で The zGM enhanced multiplの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. The zGM enhanced multiplの出力を取らず探索照合の災害対策管理の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索照合の確認記録にまとめる。 ✅
    - C. GDPS PANEL CHECK を省略して探索照合の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では The zGM enhanced multipl は「探索照合の災害対策管理に関係する定義値と表示行を照合する探索照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では The zGM enhanced multiplの属性行と GEO267I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では The zGM enhanced multiplを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は探索照合初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Time-consistent recovery {#c09-i1070}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Time-consistent recoveryは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.26 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.26

??? question "確認問題（1問）"
    **問題.** 上書照合の災害対策管理で災害対策管理の運用確認を行います。Time-consistent recoveryの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で上書照合の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず上書照合の災害対策管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書照合の根拠にする。 ✅
    - D. Time-consistent recoveryの属性行を読まず上書照合の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では Time-consistent recovery は「GDPS で Time-consistent recoveryの扱いを記録する上書照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では Time-consistent recoveryの表示結果と GEO267I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では Time-consistent recoveryの使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.26



### Tuning parameters for zGM {#c09-i1071}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Tuning parameters for zGMは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 出力照合の災害対策管理に関する Tuning parameters for zG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず出力照合の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力照合の災害対策管理の証跡として保存して根拠にする。
    - C. Tuning parameters for zG の変更点を出力本文から切り離して出力照合の災害対策管理の承認欄のみ残す。
    - D. 同じ画面で対象行と GEO267I を読み、出力照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では Tuning parameters for zG は「Tuning parameters for zG の状態と出力メッセージを結び付ける出力照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では Tuning parameters for zG の出力行と GEO267I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明のみに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では Tuning parameters for zG を GDPS の確認記録に残し、対象名は出力照合対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### Tuning z/OS Global Mirror {#c09-i1072}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Tuning z/OS Global Mirrorは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79

??? question "確認問題（1問）"
    **問題.** 条件照合のTuning z/OS Global Mirrorに関係する Tuning z 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK で得た表示本文を使い、条件照合の採否を説明欄に結び付ける。 ✅
    - B. Tuning z 属性の名称と担当者名のみを残して条件照合のTuning z/OS Global Mirrorの表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で条件照合のTuning z/OS Global Mirrorを確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず条件照合のTuning z/OS Global Mirrorの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では Tuning z 属性 は「Tuning z 属性の用途を災害対策管理の表示で確認する条件照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では GDPS の Tuning z 属性と GEO267I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では Tuning z 属性を GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は条件照合用語です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.79



### Unplanned outage support {#c09-i1073}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Unplanned outage supportは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111

??? question "確認問題（1問）"
    **問題.** 区切照合の災害対策管理で Unplanned outage supportの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Unplanned outage supportの出力を取らず区切照合の災害対策管理の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切照合として引き継ぐ。 ✅
    - C. GDPS PANEL CHECK を省略して区切照合の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では Unplanned outage support は「区切照合の災害対策管理に関係する定義値と表示行を照合する区切照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では Unplanned outage supportの属性行と GEO267I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では Unplanned outage supportを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は区切照合初出です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111



### Upgrading the server {#c09-i1074}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Upgrading the serverは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67

??? question "確認問題（1問）"
    **問題.** 範囲照合の災害対策管理で災害対策管理の運用確認を行います。Upgrading the serverの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で範囲照合の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず範囲照合の災害対策管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲照合の確認にする。 ✅
    - D. Upgrading the serverの属性行を読まず範囲照合の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では Upgrading the server は「GDPS で Upgrading the serverの扱いを記録する範囲照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では Upgrading the serverの表示結果と GEO267I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では Upgrading the serverの使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67



### Upgrading the storage system {#c09-i1075}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Upgrading the storage systemは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67

??? question "確認問題（1問）"
    **問題.** 優先照合の災害対策管理に関する Upgrading the storage syの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず優先照合の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の災害対策管理の証跡として保存して根拠にする。
    - C. Upgrading the storage syの変更点を出力本文から切り離して優先照合の災害対策管理の承認欄のみ残す。
    - D. GDPS の表示形式に沿って根拠行を採り、優先照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では Upgrading the storage sy は「Upgrading the storage syの状態と出力メッセージを結び付ける優先照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では Upgrading the storage syの出力行と GEO267I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では Upgrading the storage syを GDPS の確認記録に残し、対象名は優先照合対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.67



### Using XQuery to verify SDM parameter settings {#c09-i1076}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Using XQuery to verify SDM parameter settingsは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 記録照合の災害対策管理に関係する Using XQuery to verify S の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録照合で再確認できる形にする。 ✅
    - B. Using XQuery to verify S の名称と担当者名のみを残して記録照合の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で記録照合の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず記録照合の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では Using XQuery to verify S は「Using XQuery to verify S の用途を災害対策管理の表示で確認する記録照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では GDPS の Using XQuery to verify S と GEO267I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明のみに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では Using XQuery to verify S を GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は記録照合用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### What to expect from z/OS Global Mirror {#c09-i1077}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

What to expect from z/OS Global Mirrorは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 変更照合更新の変更照合として What to expect from z/OS Glo を確認するとき、後続担当者へ残すべき証跡はどれですか。

    - A. 戻り値と時刻を主な根拠にして表示行を読まない。
    - B. 変更照合の定義行と出力行を同じ証跡として保存する。 ✅
    - C. 承認欄の記入を優先して出力メッセージを保存しない。
    - D. 名称と担当者名を保存して表示本文を確認しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正解はBです。変更照合更新で扱う What to expect from z/OS Glo は GDPS 災害対策・サイトスイッチ の確認対象です（変更照合更新用語）。変更照合更新の担当者は変更照合として、表示本文とメッセージを照合します（変更照合更新照合）。変更照合更新の対応を残すと、後続担当者は同じ出典に戻って確認できます（変更照合更新出典）。A: 変更照合更新で表示とメッセージを結ぶ場合に根拠になります（変更照合更新A）。B: 変更照合更新で定義と出力の関係がない場合は追跡できません（変更照合更新B）。C: 変更照合更新で出典名のみでは実際の表示を説明できません（変更照合更新C）。D: 変更照合更新で操作記録のみでは値や状態の確認が不足します（変更照合更新D）。変更照合更新の初出用語として What to expect from z/OS Glo を扱い、分類内の確認名として保存します（変更照合更新終点）。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### Write pacing and device blocking {#c09-i1078}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

Write pacing and device blockingは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS 災害対策・サイトスイッチ の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 順序照合の災害対策管理で災害対策管理の運用確認を行います。Write pacing and deviceの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で順序照合の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず順序照合の災害対策管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序照合の根拠を固定する。 ✅
    - D. Write pacing and deviceの属性行を読まず順序照合の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では Write pacing and device は「GDPS で Write pacing and deviceの扱いを記録する順序照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では Write pacing and deviceの表示結果と GEO267I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では Write pacing and deviceの使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



### XRC testing {#c09-i1079}
*分類: z/OS Global Mirror ベストプラクティス*  ・  難易度: 上級

XRC testingは、GDPS 災害対策・サイトスイッチのz/OS Global Mirror ベストプラクティスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111 を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111

??? question "確認問題（1問）"
    **問題.** 値域照合の災害対策管理に関する XRC testingの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず値域照合の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の災害対策管理の証跡として保存して根拠にする。
    - C. XRC testingの変更点を出力本文から切り離して値域照合の災害対策管理の承認欄のみ残す。
    - D. GEO267I を含む表示を保存し、説明欄との差分を値域照合で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では XRC testing は「XRC testingの状態と出力メッセージを結び付ける値域照合項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では XRC testingの出力行と GEO267I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では XRC testingを GDPS の確認記録に残し、対象名は値域照合対象です。

    **出典:** GDPS_REDP4878_zOS_Global_Mirror_Planning_Operations_Best_Practices.pdf p.111




## GDPS 災害対策・サイトスイッチ > スクリプト > Control script

### Control script {#c09-i1080}
*分類: スクリプト > Control script*  ・  難易度: 中級

Control scriptは、一つ以上の機能にまたがる複雑な多段の操作を、計画アクションのパネルからまとめて実行する処理です。予定した保守や切り替えに用います

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 優先追跡の災害対策管理に関する Control scriptの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず優先追跡の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の災害対策管理の証跡として保存して根拠にする。
    - C. Control scriptの変更点を出力本文から切り離して優先追跡の災害対策管理の承認欄のみ残す。
    - D. 同じ画面で対象行と GEO267I を読み、優先追跡の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では Control script は「Control scriptの状態と出力メッセージを結び付ける優先追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では Control scriptの出力行と GEO267I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では Control scriptを GDPS の確認記録に残し、対象名は優先追跡対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > スクリプト > Planned Actions

### Planned Actions {#c09-i1081}
*分類: スクリプト > Planned Actions*  ・  難易度: 中級

Planned Actionsは、計画作業のスクリプトを一覧し、選んで実行するパネルです。選んだControl scriptの内容が表示欄に示されます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 記録追跡の災害対策管理に関係する Planned Actionsの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS PANEL CHECK で得た表示本文を使い、記録追跡の採否を説明欄に結び付ける。 ✅
    - B. Planned Actionsの名称と担当者名のみを残して記録追跡の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で記録追跡の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず記録追跡の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では Planned Actions は「Planned Actionsの用途を災害対策管理の表示で確認する記録追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では GDPS の Planned Actionsと GEO267I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では Planned Actionsを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > スクリプト > Takeover script

### Takeover script {#c09-i1082}
*分類: スクリプト > Takeover script*  ・  難易度: 中級

Takeover scriptは、特定の非計画事象が起きたあとに自動で実行される一連の処理です。切り替え後の後処理を行う型とCPCの障害に対応する型があります

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 範囲追跡の災害対策管理で災害対策管理の運用確認を行います。Takeover scriptの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で範囲追跡の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず範囲追跡の災害対策管理を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲追跡の根拠にする。 ✅
    - D. Takeover scriptの属性行を読まず範囲追跡の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では Takeover script は「GDPS で Takeover scriptの扱いを記録する範囲追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では Takeover scriptの表示結果と GEO267I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では Takeover scriptの使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > スクリプト > post-swap script

### post-swap script {#c09-i1083}
*分類: スクリプト > post-swap script*  ・  難易度: 上級

post-swap scriptは、非計画のHyperSwapのあとにGDPSが実行する引継ぎの処理です。切り替え後の状態を正常な運用へ整えます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 比較追跡の災害対策管理でpost-swap scriptの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. post-swap scriptの出力を取らず比較追跡の災害対策管理の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較追跡として引き継ぐ。 ✅
    - C. GDPS HyperSwap status panelを省略して比較追跡の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠ではpost-swap script は「比較追跡の災害対策管理に関係する定義値と表示行を照合する比較追跡項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡ではpost-swap scriptの属性行と GEO267I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出ではpost-swap scriptを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は比較追跡初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 凍結方針 > PPRCFAILURE=STOP

### PPRCFAILURE=STOP {#c09-i1084}
*分類: 凍結方針 > PPRCFAILURE=STOP*  ・  難易度: 上級

PPRCFAILURE=STOPは、入出力が止められている間に本番システムをリセットする凍結方針です。二次ボリュームの一貫性を最優先します

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 呼出追跡の災害対策管理で災害対策管理の運用確認を行います。PPRCFAILURE 属性の根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で呼出追跡の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず呼出追跡の災害対策管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 ✅
    - D. PPRCFAILURE 属性の属性行を読まず呼出追跡の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では PPRCFAILURE 属性 は「GDPS で PPRCFAILURE 属性の扱いを記録する呼出追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では PPRCFAILURE 属性の表示結果と GEO267I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では PPRCFAILURE 属性の使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 凍結方針 > PPRCFAILURE=STOPLAST

### PPRCFAILURE=STOPLAST {#c09-i1085}
*分類: 凍結方針 > PPRCFAILURE=STOPLAST*  ・  難易度: 上級

PPRCFAILURE=STOPLASTは、複数の複製脚を持つ構成でのみ意味を持つ凍結方針です。最後の脚が失われるときに初めて本番を止めます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 置換追跡の災害対策管理に関する PPRCFAILURE 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず置換追跡の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の災害対策管理の証跡として保存して根拠にする。
    - C. PPRCFAILURE 属性の変更点を出力本文から切り離して置換追跡の災害対策管理の承認欄のみ残す。
    - D. GDPS の表示形式に沿って根拠行を採り、置換追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では PPRCFAILURE 属性 は「PPRCFAILURE 属性の状態と出力メッセージを結び付ける置換追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では PPRCFAILURE 属性の出力行と GEO267I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では PPRCFAILURE 属性を GDPS の確認記録に残し、対象名は置換追跡対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 凍結方針 > freeze policy

### freeze policy {#c09-i1086}
*分類: 凍結方針 > freeze policy*  ・  難易度: 中級

freeze policyは、ミラー障害を検知してFreezeを行ったあとの動作を決める方針です。PPRCFAILUREの選択肢で継続か停止かを選びます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 条件検査の災害対策管理に関係するfreeze policyの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件検査で再確認できる形にする。 ✅
    - B. freeze policyの名称と担当者名のみを残して条件検査の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で条件検査の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず条件検査の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠ではfreeze policy は「freeze policyの用途を災害対策管理の表示で確認する条件検査項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では GDPS のfreeze policyと GEO267I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語ではfreeze policyを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は条件検査用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 構成定義 > GEOGROUP

### GEOGROUP {#c09-i1087}
*分類: 構成定義 > GEOGROUP*  ・  難易度: 中級

GEOGROUPは、資源のまとまりを表す構成の定義です。GEOPARMとあわせて維持し、地域切り替えの際に活動側と非活動側で一致させます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 区切追跡の災害対策管理で GEOGROUP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. GEOGROUP の出力を取らず区切追跡の災害対策管理の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切追跡の確認記録にまとめる。 ✅
    - C. GDPS configuration panelを省略して区切追跡の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では GEOGROUP は「区切追跡の災害対策管理に関係する定義値と表示行を照合する区切追跡項目」と GDPS configuration panelまたは該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では GEOGROUP の属性行と GEO251I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では GEOGROUP を GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は区切追跡初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 構成定義 > GEOPARM

### GEOPARM {#c09-i1088}
*分類: 構成定義 > GEOPARM*  ・  難易度: 中級

GEOPARMは、GDPSで管理するディスク構成や複製の対、PPRCリンクを定義する構成ファイルです。更新時は非活動側の構成にも同じ変更を反映します

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 条件追跡の災害対策管理に関係する GEOPARM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS configuration panelの結果から対象行を抜き出し、条件追跡の証跡として残す。 ✅
    - B. GEOPARM の名称と担当者名のみを残して条件追跡の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で条件追跡の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO251I の有無を見ず条件追跡の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では GEOPARM は「GEOPARM の用途を災害対策管理の表示で確認する条件追跡項目」と GDPS configuration panelまたは該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では GDPS の GEOPARM と GEO251I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では GEOPARM を GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 継続可用性 > HyperSwap

### HyperSwap {#c09-i1089}
*分類: 継続可用性 > HyperSwap*  ・  難易度: 初級

HyperSwapは、ミラーの一次ディスクから二次ディスクへの切り替えを本番システムに透過的に行う機能です。すべての一次ボリュームをまとめて切り替えます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 警告照合の災害対策管理に関係する HyperSwapの設問です。一次資料に沿って採るべき確認はどれですか。

    - A. GDPS HyperSwap status panelの結果から対象行を抜き出し、警告照合の証跡として残す。 ✅
    - B. HyperSwapの名称と担当者名のみを残して警告照合の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で警告照合の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず警告照合の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 初級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では HyperSwap は「HyperSwapの用途を災害対策管理の表示で確認する警告照合項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では GDPS の HyperSwapと GEO267I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では HyperSwapを GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は警告照合用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 継続可用性 > 計画HyperSwap

### 計画HyperSwap {#c09-i1090}
*分類: 継続可用性 > 計画HyperSwap*  ・  難易度: 中級

計画HyperSwapは、操作者があらかじめ意図して行うディスクの切り替えです。保守などの計画作業で一次と二次を入れ替えます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 復旧照合の計画で計画 HyperSwapの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. 計画 HyperSwapの出力を取らず復旧照合の計画の説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧照合の確認記録にまとめる。 ✅
    - C. GDPS HyperSwap status panelを省略して復旧照合の計画の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の計画へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では計画 HyperSwap は「復旧照合の計画に関係する定義値と表示行を照合する復旧照合項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では計画 HyperSwapの属性行と GEO267I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では計画 HyperSwapを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は復旧照合初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 継続可用性 > 非計画HyperSwap

### 非計画HyperSwap {#c09-i1091}
*分類: 継続可用性 > 非計画HyperSwap*  ・  難易度: 中級

非計画HyperSwapは、一次ディスクの問題を検知したときに自動でディスクを切り替える動きです。急性と分類される問題も引き金として扱われます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 監査照合の非計画で災害対策管理の運用確認を行います。非計画 HyperSwapの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で監査照合の非計画を確認した扱いにする。
    - B. GEO267I の有無を確認せず監査照合の非計画を正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査照合の根拠にする。 ✅
    - D. 非計画 HyperSwapの属性行を読まず監査照合の非計画の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では非計画 HyperSwap は「GDPS で非計画 HyperSwapの扱いを記録する監査照合項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では非計画 HyperSwapの表示結果と GEO267I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では非計画 HyperSwapの使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 複製技術 > Global Mirror

### Global Mirror {#c09-i1092}
*分類: 複製技術 > Global Mirror*  ・  難易度: 中級

Global Mirrorは、GDPS GMが用いる非同期の遠隔複製です。ファイバー・チャネル・プロトコル上で動き、ほぼ無制限の距離で災害対策を実現します

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



## GDPS 災害対策・サイトスイッチ > 複製技術 > Metro Mirror

### Metro Mirror {#c09-i1093}
*分類: 複製技術 > Metro Mirror*  ・  難易度: 中級

Metro Mirrorは、GDPS Metroが土台とする同期の遠隔複製です。書き込みを二次へ同期で反映し、目標復旧点であるRPOをゼロにできます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



## GDPS 災害対策・サイトスイッチ > 複製技術 > PPRC link

### PPRC link {#c09-i1094}
*分類: 複製技術 > PPRC link*  ・  難易度: 中級

PPRC linkは、一次と二次のディスク・サブシステムを結ぶ複製の経路です。GEOPARMに定義し、Metro Mirrorの同期複製に用います

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 上書検査の災害対策管理で災害対策管理の運用確認を行います。PPRC linkの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で上書検査の災害対策管理を確認した扱いにする。
    - B. GEO251I の有無を確認せず上書検査の災害対策管理を正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書検査の確認にする。 ✅
    - D. PPRC linkの属性行を読まず上書検査の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では PPRC link は「GDPS で PPRC linkの扱いを記録する上書検査項目」と GDPS configuration panelまたは該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では PPRC linkの表示結果と GEO251I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では PPRC linkの使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 障害対応 > ELB

### ELB {#c09-i1095}
*分類: 障害対応 > ELB*  ・  難易度: 上級

ELBは、Freezeの結果として一次ディスクが置かれる延長ロング・ビジーの状態です。一次への更新を一時的に保留し、不整合の拡大を防ぎます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 探索追跡の災害対策管理で ELB の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. ELB の出力を取らず探索追跡の災害対策管理の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索追跡の確認値として扱う。 ✅
    - C. GDPS HyperSwap status panelを省略して探索追跡の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では ELB は「探索追跡の災害対策管理に関係する定義値と表示行を照合する探索追跡項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では ELB の属性行と GEO267I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では ELB を GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は探索追跡初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 障害対応 > Freeze

### Freeze {#c09-i1096}
*分類: 障害対応 > Freeze*  ・  難易度: 中級

Freezeは、ミラーの障害を検知したときに、その複製脚に対し自動かつ無条件に行う動きです。二次ボリュームの整合した一組を確保します

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



## GDPS 災害対策・サイトスイッチ > 障害対応 > Incremental Resynchronization

### Incremental Resynchronization {#c09-i1097}
*分類: 障害対応 > Incremental Resynchronization*  ・  難易度: 上級

Incremental Resynchronizationは、複数脚の構成でディスクの切り替えや回復の後、差分だけを再同期する仕組みです。全面の再コピーを避けます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 出力追跡の災害対策管理に関する Incremental Resynchronizの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず出力追跡の災害対策管理の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の災害対策管理の証跡として保存して根拠にする。
    - C. Incremental Resynchronizの変更点を出力本文から切り離して出力追跡の災害対策管理の承認欄のみ残す。
    - D. GEO267I を含む表示を保存し、説明欄との差分を出力追跡で確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では Incremental Resynchroniz は「Incremental Resynchronizの状態と出力メッセージを結び付ける出力追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では Incremental Resynchronizの出力行と GEO267I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では Incremental Resynchronizを GDPS の確認記録に残し、対象名は出力追跡対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 障害対応 > PRIMARYFAILURE

### PRIMARYFAILURE {#c09-i1098}
*分類: 障害対応 > PRIMARYFAILURE*  ・  難易度: 上級

PRIMARYFAILUREは、一次ディスクの問題を検知してFreezeを行ったあとに取る動作を選ぶ方針です。切り替えを行う選択肢と伴わない選択肢があります

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 終端追跡の災害対策管理に関係する PRIMARYFAILURE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端追跡で再確認できる形にする。 ✅
    - B. PRIMARYFAILURE の名称と担当者名のみを残して終端追跡の災害対策管理の表示本文を確認対象に含めない。
    - C. 災害対策管理以外の画面で終端追跡の災害対策管理を確認し同じ証跡として扱ったことにする。
    - D. GEO267I の有無を見ず終端追跡の災害対策管理の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では PRIMARYFAILURE は「PRIMARYFAILURE の用途を災害対策管理の表示で確認する終端追跡項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では GDPS の PRIMARYFAILURE と GEO267I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では PRIMARYFAILURE を GDPS 災害対策・サイトスイッチで扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 障害対応 > Preferred Swap Leg

### Preferred Swap Leg {#c09-i1099}
*分類: 障害対応 > Preferred Swap Leg*  ・  難易度: 上級

Preferred Swap Legは、複数脚の構成で非計画のHyperSwapの際にどの複製脚で切り替えるかを選ぶ方針です。指定した脚を優先して選びます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 上書追跡の災害対策管理で災害対策管理の運用確認を行います。Preferred Swap Legの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で上書追跡の災害対策管理を確認した扱いにする。
    - B. GEO267I の有無を確認せず上書追跡の災害対策管理を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書追跡の根拠を固定する。 ✅
    - D. Preferred Swap Legの属性行を読まず上書追跡の災害対策管理の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では Preferred Swap Leg は「GDPS で Preferred Swap Legの扱いを記録する上書追跡項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では Preferred Swap Legの表示結果と GEO267I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では Preferred Swap Legの使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## GDPS 災害対策・サイトスイッチ > 障害対応 > dual-leg configuration

### dual-leg configuration {#c09-i1100}
*分類: 障害対応 > dual-leg configuration*  ・  難易度: 上級

dual-leg configurationは、二つの複製脚を持つGDPS Metroの構成です。三つのコピーを保ち、一つが使えなくても残る二つで保護を続けます

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services



## GDPS 災害対策・サイトスイッチ > 障害対応 > site failure

### site failure {#c09-i1101}
*分類: 障害対応 > site failure*  ・  難易度: 中級

site failureは、サイト全体が失われる障害です。Freezeは、ミラーの障害がサイト障害の最初の兆候である場合に備えて二次の整合を確保します

**出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

??? question "確認問題（1問）"
    **問題.** 探索検査の災害対策管理でsite failureの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. site failureの出力を取らず探索検査の災害対策管理の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索検査として引き継ぐ。 ✅
    - C. GDPS HyperSwap status panelを省略して探索検査の災害対策管理の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の災害対策管理へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠ではsite failure は「探索検査の災害対策管理に関係する定義値と表示行を照合する探索検査項目」と GDPS HyperSwap status panelまたは該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡ではsite failureの属性行と GEO267I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出ではsite failureを GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は探索検査初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services




## その他

### その他（特定項目に紐づかないQA・手順） {#c09-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（4問）"
    **問題.** 比較追跡の概要・計で Minimizing latency 属性の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Minimizing latency 属性の出力を取らず比較追跡の概要・計の説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較追跡として引き継ぐ。 ✅
    - C. GDPS PANEL CHECK を省略して比較追跡の概要・計の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の概要・計へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では Minimizing latency 属性 は「比較追跡の概要・計に関係する定義値と表示行を照合する比較追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では Minimizing latency 属性の属性行と GEO267I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では Minimizing latency 属性を GDPS 災害対策・サイトスイッチの運用手順で確認し、初出名は比較追跡初出です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **問題.** 置換整理の概要 機に関する Combining local and metrの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず置換整理の概要 機の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理の概要 機の証跡として保存して根拠にする。
    - C. Combining local and metrの変更点を出力本文から切り離して置換整理の概要 機の承認欄のみ残す。
    - D. 参照資料名、表示行、メッセージをそろえて置換整理の根拠を固定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では Combining local and metr は「Combining local and metrの状態と出力メッセージを結び付ける置換整理項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では Combining local and metrの出力行と GEO267I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では Combining local and metrを GDPS の確認記録に残し、対象名は置換整理対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **問題.** 優先記録の概要 機に関する DR and continuous availaの引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. GDPS PANEL CHECK の結果を残さず優先記録の概要 機の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の概要 機の証跡として保存して根拠にする。
    - C. DR and continuous availaの変更点を出力本文から切り離して優先記録の概要 機の承認欄のみ残す。
    - D. 属性行、戻り表示、メッセージ見出しを合わせて優先記録の根拠にする。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では DR and continuous availa は「DR and continuous availaの状態と出力メッセージを結び付ける優先記録項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では DR and continuous availaの出力行と GEO267I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では DR and continuous availaを GDPS の確認記録に残し、対象名は優先記録対象です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **問題.** 呼出追跡の概要 機で災害対策管理の運用確認を行います。Local continuous availabの根拠にできる作業はどれですか。

    - A. GDPS と無関係な一覧で呼出追跡の概要 機を確認した扱いにする。
    - B. GEO267I の有無を確認せず呼出追跡の概要 機を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出追跡の根拠を固定する。 ✅
    - D. Local continuous availabの属性行を読まず呼出追跡の概要 機の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では Local continuous availab は「GDPS で Local continuous availabの扱いを記録する呼出追跡項目」と GDPS PANEL CHECK または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では Local continuous availabの表示結果と GEO267I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では Local continuous availabの使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services


??? note "検証手順（33件）"
    **HyperSwap 確認手順**

    - 検証目的: GDPS 主パネルで HyperSwap が有効で、Metro Mirror が全二重化されていることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。GDPS Metro の構成要約と HyperSwap 状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> GDPS
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - Main Panel
    Configuration     METRO1             Overall status  OK
    Production site   SITE1              Recovery site   SITE2
    Metro Mirror      FULL DUPLEX         Direction       SITE1 -> SITE2
    HyperSwap         ENABLED             Preferred leg   LEG1
    Selection ===>
    ```

    METRO1 の HyperSwap ENABLED と Metro Mirror FULL DUPLEX は、スワップ前提となる保護状態を示します。

    - 合格条件: ① ステップ1の HyperSwap ENABLED が表示されること
    ② ステップ1の Metro Mirror FULL DUPLEX が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **計画HyperSwap 確認手順**

    - 検証目的: 計画 HyperSwap 用の control script が実行可能で、対象サイトと複製前提が確認済みであることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。Planned Actions から PLNHYPER の内容を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 6
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Planned Action - Script Detail
    Script PLNHYPER      Type CONTROL      Status READY
    Action HYPERSWAP     Target SITE2      Replication leg LEG1
    Precheck Mirror FULL DUPLEX
    Run ===> NO
    ```

    PLNHYPER の Target SITE2、Replication leg LEG1、Precheck Mirror FULL DUPLEX により計画切替の入力を照合できます。

    - 合格条件: ① ステップ1の Script PLNHYPER と Type CONTROL が表示されること
    ② ステップ1の Target SITE2 と Mirror FULL DUPLEX が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **非計画HyperSwap 確認手順**

    - 検証目的: 非計画 HyperSwap が一次ディスク障害時の方針として有効で、失敗時の後続動作まで定義されていることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。HyperSwap と Freeze の方針パネルを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - HyperSwap and Freeze Policy
    Configuration METRO1
    HyperSwap status        ENABLED
    PPRCFAILURE             STOP
    PRIMARYFAILURE          SWAP,STOP
    Preferred Swap Leg     LEG1
    Action ===>
    ```

    PRIMARYFAILURE SWAP,STOP と HyperSwap status ENABLED は、一次障害でスワップし不能時に停止する方針です。

    - 合格条件: ① ステップ1の PRIMARYFAILURE SWAP,STOP が表示されること
    ② ステップ1の HyperSwap status ENABLED が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Metro Mirror 確認手順**

    - 検証目的: DASD Remote Copy パネルで同期 Metro Mirror の LSS ペアが全二重状態であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。DASD Remote Copy の LSS ペア一覧を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS DASD Remote Copy - LSS Pairs
    Configuration METRO1    Consistency Group CG01
    Leg   Primary        Secondary      Copy mode      Pair status
    LEG1  SITE1 LSS 01   SITE2 LSS 11   METRO MIRROR  FULL DUPLEX
    Volume pairs 256     Duplex 256     Suspended 0    Error 0
    Action ===>
    ```

    LEG1 の Copy mode METRO MIRROR と Pair status FULL DUPLEX、Duplex 256 により同期複製を確認できます。

    - 合格条件: ① ステップ1の METRO MIRROR と FULL DUPLEX が表示されること
    ② ステップ1の Volume pairs 256 と Duplex 256 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Global Mirror 確認手順**

    - 検証目的: GDPS GM 主パネルで Global Mirror セッションの複製方向、稼働状態、整合点、RPO を確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。GDPS Global - GM の主パネルを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> GDPS
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Global - GM Main Panel
    Configuration GM2SITE            Overall status OK
    K-sys KSYSA     R-sys RSYSB      Session GM01
    Global Mirror SITE1 -> SITE2     Session status RUNNING
    Consistency point CURRENT        Current RPO 00:00:07
    Selection ===>
    ```

    GM01 の SITE1 -> SITE2、RUNNING、Consistency point CURRENT、Current RPO 00:00:07 でセッション状態を確認できます。

    - 合格条件: ① ステップ1の Global Mirror SITE1 -> SITE2 が表示されること
    ② ステップ1の Session status RUNNING と Current RPO 00:00:07 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Freeze 確認手順**

    - 検証目的: Freeze 方針と HyperSwap 方針を同じ構成画面で確認し、複製障害時のデータ整合性保護動作を判断します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。Metro Mirror 障害時の Freeze 方針を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - HyperSwap and Freeze Policy
    Configuration METRO1
    HyperSwap status        ENABLED
    PPRCFAILURE             STOP
    PRIMARYFAILURE          SWAP,STOP
    Preferred Swap Leg     LEG1
    Action ===>
    ```

    PPRCFAILURE STOP は Freeze 後に入出力停止中の本番システムをリセットする方針です。

    - 合格条件: ① ステップ1の PPRCFAILURE STOP が表示されること
    ② ステップ1の PRIMARYFAILURE SWAP,STOP が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **PPRCFAILURE=STOP 確認手順**

    - 検証目的: PPRCFAILURE=STOP が Freeze 後に本番システムを停止して RPO 0 を保護する設定であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。Freeze and Stop の方針とデータ損失目標を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - HyperSwap and Freeze Policy
    Configuration METRO1
    HyperSwap status        ENABLED
    PPRCFAILURE             STOP
    PRIMARYFAILURE          SWAP,STOP
    Preferred Swap Leg     LEG1
    Action ===>
    Data loss objective    RPO 0
    ```

    PPRCFAILURE STOP と Data loss objective RPO 0 は、停止により更新差分を増やさない設計を示します。

    - 合格条件: ① ステップ1の PPRCFAILURE STOP が表示されること
    ② ステップ1の Data loss objective RPO 0 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **PPRCFAILURE=STOPLAST 確認手順**

    - 検証目的: dual-leg 構成で STOPLAST が他レッグを確認し、最後の有効レッグを Freeze した場合だけ停止する設定を確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。dual-leg 用 Freeze 方針と他レッグの複製状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - Dual-leg Freeze Policy
    Configuration METRO2LEG
    PPRCFAILURE STOPLAST
    Frozen leg LEG2
    Other leg LEG1 FULL DUPLEX
    Decision GO - viable leg remains
    ```

    PPRCFAILURE STOPLAST と Other leg LEG1 FULL DUPLEX により、使用可能なレッグが残るため GO 判定になります。

    - 合格条件: ① ステップ1の PPRCFAILURE STOPLAST が表示されること
    ② ステップ1の Other leg LEG1 FULL DUPLEX が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **PRIMARYFAILURE 確認手順**

    - 検証目的: PRIMARYFAILURE 方針が一次ディスク障害後に SWAP を試み、スワップ不能時は STOP する設定であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。一次ディスク障害時の HyperSwap 方針を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - HyperSwap and Freeze Policy
    Configuration METRO1
    HyperSwap status        ENABLED
    PPRCFAILURE             STOP
    PRIMARYFAILURE          SWAP,STOP
    Preferred Swap Leg     LEG1
    Action ===>
    ```

    PRIMARYFAILURE SWAP,STOP と Preferred Swap Leg LEG1 は、LEG1 でスワップし不能なら停止する設定です。

    - 合格条件: ① ステップ1の PRIMARYFAILURE SWAP,STOP が表示されること
    ② ステップ1の Preferred Swap Leg LEG1 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **ELB 確認手順**

    - 検証目的: Freeze 中に PPRC ペアが Extended Long Busy となり、本番システムの入出力が方針決定までロックされることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。Freeze 対象の LSS ペア詳細で装置待機状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS DASD Remote Copy - Freeze Detail
    Consistency Group CG01
    Device state ELB
    Host I/O WAITING
    Metro Mirror SUSPEND IN PROGRESS
    Policy PPRCFAILURE=STOP
    ```

    Device state ELB と Host I/O WAITING は、Freeze 方針決定まで入出力が待機していることを示します。

    - 合格条件: ① ステップ1の Consistency Group CG01 と Device state ELB が表示されること
    ② ステップ1の Host I/O WAITING が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Preferred Swap Leg 確認手順**

    - 検証目的: dual-leg の非計画 HyperSwap で優先レッグが選択候補として評価され、全二重状態であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。dual-leg の優先レッグと各レッグの適格状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - HyperSwap Leg Selection
    Configuration METRO2LEG
    Preferred Swap Leg LEG1
    LEG1 FULL DUPLEX ELIGIBLE
    LEG2 FULL DUPLEX ELIGIBLE
    Selected first LEG1
    ```

    Preferred Swap Leg LEG1 と両レッグの FULL DUPLEX ELIGIBLE により、LEG1 が最初に選択されます。

    - 合格条件: ① ステップ1の Preferred Swap Leg LEG1 が表示されること
    ② ステップ1の LEG1 FULL DUPLEX と LEG2 FULL DUPLEX が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Incremental Resynchronization 確認手順**

    - 検証目的: dual-leg 間の増分再同期用レッグが追跡情報を保持し、スワップ後の全量コピーを避ける準備状態にあることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。dual-leg 構成の MTIR レッグと変更記録状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - Incremental Resynchronization
    Configuration METRO2LEG
    Leg LEG3     Role MTIR
    Change recording ACTIVE
    Resync state READY
    Source SITE2     Target SITE3
    ```

    LEG3 の Role MTIR、Change recording ACTIVE、Resync state READY が増分再同期の準備状態を示します。

    - 合格条件: ① ステップ1の LEG3 と Role MTIR が表示されること
    ② ステップ1の Change recording ACTIVE と Resync state READY が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **GEOPARM 確認手順**

    - 検証目的: GEOPARM に一次・二次 LSS、装置ペア、PPRC リンク、複製レッグが定義されていることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。GDPS の DASD リモート・コピー構成定義を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE GDPS.V4R7M0.PARMLIB(GEOPARM)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- GDPS.V4R7M0.PARMLIB(GEOPARM) -- Line 00000000 Col 001 080
    Command ===>
    000001 CONFIGURATION METRO1
    000002 LEG LEG1 MODE METRO_MIRROR
    000003 PRIMARY_LSS SITE1.01
    000004 SECONDARY_LSS SITE2.11
    000005 PPRC_LINK LINK12
    ```

    GEOPARM の LEG1、PRIMARY_LSS SITE1.01、SECONDARY_LSS SITE2.11、PPRC_LINK LINK12 で複製構成を確認できます。

    - 合格条件: ① ステップ1の GEOPARM と LEG1 が表示されること
    ② ステップ1の SITE1.01 と SITE2.11 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **GEOGROUP 確認手順**

    - 検証目的: GEOGROUP に同じ管理単位の K-sys、R-sys、サイト、シスプレックスが関連付けられていることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。GDPS 管理グループの K-sys と R-sys の対応を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> BROWSE GDPS.V4R7M0.PARMLIB(GEOGROUP)
    → Enter を押す
    ```

    画面・出力:
    ```text
    BROWSE -- GDPS.V4R7M0.PARMLIB(GEOGROUP) -- Line 00000000 Col 001 080
    Command ===>
    000001 GEOGROUP GM2SITE
    000002 SITE SITE1 K_SYS KSYSA
    000003 SITE SITE2 R_SYS RSYSB
    000004 GM_SESSION GM01
    000005 END_GROUP
    ```

    GEOGROUP GM2SITE の SITE1 K_SYS KSYSA と SITE2 R_SYS RSYSB で管理対象を確認できます。

    - 合格条件: ① ステップ1の GEOGROUP GM2SITE が表示されること
    ② ステップ1の KSYSA と RSYSB が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Takeover script 確認手順**

    - 検証目的: unplanned event に対応する予約名の takeover script が定義され、自動選択可能であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。SWAPSite13 の予約名、トリガー、対象サイトを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 6
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Planned Action - Script Detail
    Script SWAPSite13     Type TAKEOVER     Status DEFINED
    Trigger UNPLANNED HYPERSWAP
    From SITE1     To SITE3
    First statement RESYNC MTIR LEG3
    ```

    SWAPSite13 の Type TAKEOVER と Trigger UNPLANNED HYPERSWAP により自動実行対象を識別できます。

    - 合格条件: ① ステップ1の Script SWAPSite13 と Type TAKEOVER が表示されること
    ② ステップ1の Trigger UNPLANNED HYPERSWAP が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Control script 確認手順**

    - 検証目的: control script が複数の GDPS 機能を順番に実行し、前の文の成功後だけ次へ進む構成であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。DRTEST control script の処理順と再開位置を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 6
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Planned Action - Script Detail
    Script DRTEST     Type CONTROL     Status READY
    Step 1 PREPARE GM01
    Step 2 ACTIVATE SITE2
    Step 3 START RECOVERY SYSTEMS
    Restart point Step 1
    ```

    DRTEST の Step 1 PREPARE GM01 から Step 3 までの順序と Restart point により多段処理を確認できます。

    - 合格条件: ① ステップ1の Script DRTEST と Type CONTROL が表示されること
    ② ステップ1の Step 1 PREPARE GM01 と Step 2 ACTIVATE SITE2 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Planned Actions 確認手順**

    - 検証目的: Planned Actions パネルに実行可能な control script と定義済み takeover script が別種別で一覧されることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。実行可能なスクリプトと種別、状態を一覧表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 6
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Planned Actions
    Configuration METRO1
    Sel  Script       Type       Status   Last result
     _   PLNHYPER     CONTROL    READY    SUCCESS
     _   DRTEST       CONTROL    READY    SUCCESS
     _   SWAPSite13   TAKEOVER   DEFINED  NOT RUN
    Selection ===>
    ```

    DRTEST CONTROL READY と SWAPSite13 TAKEOVER DEFINED により計画用と自動引継ぎ用を区別できます。

    - 合格条件: ① ステップ1の DRTEST CONTROL READY が表示されること
    ② ステップ1の SWAPSite13 TAKEOVER DEFINED が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **post-swap script 確認手順**

    - 検証目的: 非計画 HyperSwap 後に実行する post-swap script が、増分再同期とサイト役割変更を含むことを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。SWAPSite13 のスワップ後処理文を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 6
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Takeover Script Detail
    Script SWAPSite13     Trigger POST-SWAP
    Step 1 RESYNC LEG3
    Step 2 SET PRIMARY SITE3
    Step 3 VERIFY METRO MIRROR
    Status DEFINED
    ```

    POST-SWAP の RESYNC LEG3 と SET PRIMARY SITE3 は増分再同期と新本番サイト設定の後処理です。

    - 合格条件: ① ステップ1の Script SWAPSite13 と Trigger POST-SWAP が表示されること
    ② ステップ1の RESYNC LEG3 と SET PRIMARY SITE3 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **K-sys 確認手順**

    - 検証目的: GDPS GM の K-sys が Global Mirror の制御と復旧処理を担当し、セッションへ接続されていることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。GDPS GM の制御システム一覧を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Global - Controlling Systems
    System KSYSA     Role K-SYS     Site SITE1
    Status AVAILABLE
    Controls GM01
    NetView ACTIVE     System Automation AVAILABLE
    ```

    System KSYSA の Role K-SYS、Controls GM01、Status AVAILABLE により本番側制御役割を確認できます。

    - 合格条件: ① ステップ1の System KSYSA と Role K-SYS が表示されること
    ② ステップ1の Controls GM01 と Status AVAILABLE が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **R-sys 確認手順**

    - 検証目的: GDPS GM の R-sys が復旧サイト側で Global Mirror の回復操作を担当し、待機可能であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。GDPS GM の復旧制御システムを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Global - Controlling Systems
    System RSYSB     Role R-SYS     Site SITE2
    Status AVAILABLE
    Recovery for GM01
    NetView ACTIVE     System Automation AVAILABLE
    ```

    System RSYSB の Role R-SYS、Recovery for GM01、Status AVAILABLE により復旧側制御役割を確認できます。

    - 合格条件: ① ステップ1の System RSYSB と Role R-SYS が表示されること
    ② ステップ1の Recovery for GM01 と Status AVAILABLE が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **RPO 確認手順**

    - 検証目的: Global Mirror の現在の遅延と最終整合点時刻を表示し、定義した RPO 目標内であることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。GM01 の整合点遅延と RPO 目標を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Global - GM Session Detail
    Session GM01     Status RUNNING
    Last consistency point 2026-07-16 10:52:14
    Current RPO 00:00:07
    RPO target 00:00:30
    Within target YES
    ```

    Current RPO 00:00:07 が RPO target 00:00:30 より短く、Within target YES と評価されています。

    - 合格条件: ① ステップ1の Session GM01 と Current RPO 00:00:07 が表示されること
    ② ステップ1の RPO target 00:00:30 と Within target YES が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **RTO 確認手順**

    - 検証目的: 直近の復旧訓練でサイト切替から業務再開までの測定時間が RTO 目標内であったことを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。直近の復旧訓練結果と RTO 比較を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 7
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Recovery Exercise History
    Drill DRTEST-20260701
    Start 2026-07-01 09:00:00
    Service available 2026-07-01 09:22:15
    Measured RTO 00:22:15
    RTO target 01:00:00     Within target YES
    ```

    Measured RTO 00:22:15 と RTO target 01:00:00 の比較が Within target YES になっています。

    - 合格条件: ① ステップ1の Drill DRTEST-20260701 と Measured RTO 00:22:15 が表示されること
    ② ステップ1の RTO target 01:00:00 と Within target YES が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **GDPS Metro 確認手順**

    - 検証目的: GDPS Metro 構成が二つのサイト、Metro Mirror、HyperSwap、シスプレックス管理を一体で提供していることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。METRO1 のサイト、複製、HyperSwap 状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> GDPS
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - Main Panel
    Configuration     METRO1             Overall status  OK
    Production site   SITE1              Recovery site   SITE2
    Metro Mirror      FULL DUPLEX         Direction       SITE1 -> SITE2
    HyperSwap         ENABLED             Preferred leg   LEG1
    Selection ===>
    ```

    GDPS Metro の METRO1 に SITE1 と SITE2、Metro Mirror FULL DUPLEX、HyperSwap ENABLED が表示されます。

    - 合格条件: ① ステップ1の GDPS Metro と METRO1 が表示されること
    ② ステップ1の Metro Mirror FULL DUPLEX と HyperSwap ENABLED が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **GDPS GM 確認手順**

    - 検証目的: GDPS GM 構成が K-sys と R-sys から遠隔 Global Mirror セッションを監視・制御していることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。GM2SITE の制御システムと Global Mirror 状態を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> GDPS
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Global - GM Main Panel
    Configuration GM2SITE            Overall status OK
    K-sys KSYSA     R-sys RSYSB      Session GM01
    Global Mirror SITE1 -> SITE2     Session status RUNNING
    Consistency point CURRENT        Current RPO 00:00:07
    Selection ===>
    ```

    GDPS Global - GM の GM2SITE に KSYSA、RSYSB、Session GM01、RUNNING が表示されます。

    - 合格条件: ① ステップ1の GDPS Global - GM と GM2SITE が表示されること
    ② ステップ1の KSYSA と RSYSB と GM01 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **GDPS MGM 確認手順**

    - 検証目的: GDPS MGM のメトロ域同期レッグと遠隔非同期レッグが同時に正常で、三サイト保護を構成することを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。MGM3SITE のメトロ域と地域外の複製レッグを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> GDPS
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro Global - GM Main Panel
    Configuration MGM3SITE     Overall status OK
    MM01 METRO MIRROR SITE1 -> SITE2 FULL DUPLEX
    GM01 GLOBAL MIRROR SITE1 -> SITE3 RUNNING
    HyperSwap ENABLED     Current RPO 00:00:09
    Selection ===>
    ```

    MM01 METRO MIRROR FULL DUPLEX と GM01 GLOBAL MIRROR RUNNING により三サイト複製を確認できます。

    - 合格条件: ① ステップ1の MM01 METRO MIRROR FULL DUPLEX が表示されること
    ② ステップ1の GM01 GLOBAL MIRROR RUNNING が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **dual-leg configuration 確認手順**

    - 検証目的: dual-leg 構成に共通一次コピーから二つの二次コピーへ伸びる活動レッグと、二次間 MTIR レッグがあることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。二つの活動レッグと二次間 MTIR レッグを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - Dual-leg Topology
    Configuration METRO2LEG
    LEG1 SITE1 -> SITE2 ACTIVE FULL DUPLEX
    LEG2 SITE1 -> SITE3 ACTIVE FULL DUPLEX
    LEG3 SITE2 <-> SITE3 MTIR READY
    Primary copy SITE1
    ```

    LEG1 ACTIVE、LEG2 ACTIVE、LEG3 MTIR READY により dual-leg と増分再同期経路を確認できます。

    - 合格条件: ① ステップ1の LEG1 ACTIVE と LEG2 ACTIVE が表示されること
    ② ステップ1の LEG3 MTIR READY が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Metro Mirror suspend 確認手順**

    - 検証目的: Freeze 後に Metro Mirror が中断され、二次コピーの整合性が保存されて再同期待ちになることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。Freeze 対象レッグの中断状態と二次整合性を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS DASD Remote Copy - LSS Pairs
    Configuration METRO1     Consistency Group CG01
    Leg LEG1     Copy mode METRO MIRROR
    Pair status SUSPENDED
    Secondary consistency PRESERVED
    Resynchronization REQUIRED
    ```

    Pair status SUSPENDED と Secondary consistency PRESERVED は Freeze 後の整合コピー保存を示します。

    - 合格条件: ① ステップ1の LEG1 と Pair status SUSPENDED が表示されること
    ② ステップ1の Secondary consistency PRESERVED が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **symmetrical configuration 確認手順**

    - 検証目的: symmetrical 4-site 構成で両地域に Metro Mirror があり、どちらが本番でも地域外 Global Mirror を維持できることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は NetView の入力画面です。MGM4SITE の地域内レッグと地域間レッグを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    NetView ===> GDPS
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS MGM - Symmetrical 4-site Topology
    Configuration MGM4SITE
    REGION1 SITE1-SITE2 METRO MIRROR FULL DUPLEX
    REGION2 SITE3-SITE4 METRO MIRROR FULL DUPLEX
    Cross-region GLOBAL MIRROR READY
    Active region REGION1
    ```

    REGION1 と REGION2 の METRO MIRROR、Cross-region GLOBAL MIRROR READY により対称構成を確認できます。

    - 合格条件: ① ステップ1の REGION1 SITE1-SITE2 METRO MIRROR が表示されること
    ② ステップ1の REGION2 SITE3-SITE4 METRO MIRROR が表示されること
    ③ ステップ1の Cross-region GLOBAL MIRROR READY が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **controlling system 確認手順**

    - 検証目的: GDPS controlling system が NetView と System Automation を使用し、複製と自動化の制御役割を担うことを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。GDPS 制御システムの役割と基盤タスクを表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS - Controlling System Detail
    System KSYSA     Role CONTROLLING
    Site SITE1
    NetView CNM01 ACTIVE
    System Automation AVAILABLE
    Controls GM01
    ```

    KSYSA の Role CONTROLLING、NetView CNM01 ACTIVE、Controls GM01 により制御役割を確認できます。

    - 合格条件: ① ステップ1の System KSYSA と Role CONTROLLING が表示されること
    ② ステップ1の NetView CNM01 ACTIVE と Controls GM01 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **site failure 確認手順**

    - 検証目的: サイト障害アラートが影響資源と復旧候補サイトを示し、対応 takeover script が提示されることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。SDF から SITE1 の重大アラート詳細を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> A
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS SDF - Alert Detail
    Site SITE1     Status FAILED     Severity CRITICAL
    Sysplex resources UNAVAILABLE
    Recovery site SITE2     Status AVAILABLE
    Takeover script SITEFAIL12     Status DEFINED
    Operator decision REQUIRED
    ```

    SITE1 の Status FAILED と SITE2 AVAILABLE、Takeover script SITEFAIL12 により復旧候補と処理を確認できます。

    - 合格条件: ① ステップ1の Site SITE1 と Status FAILED が表示されること
    ② ステップ1の Recovery site SITE2 と Takeover script SITEFAIL12 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **PPRC link 確認手順**

    - 検証目的: PPRC link の一次・二次ストレージ接続が稼働し、Metro Mirror ペアの複数経路が確保されていることを確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。DASD Remote Copy の PPRC link 詳細を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS DASD Remote Copy - PPRC Links
    Link LINK12     Status OPERATIONAL
    Primary SITE1.2107-01
    Secondary SITE2.2107-02
    Active paths 8     Failed paths 0
    Last monitor 2026-07-16 10:55:00
    ```

    LINK12 の Status OPERATIONAL、Active paths 8、Failed paths 0 により複製経路の稼働を確認できます。

    - 合格条件: ① ステップ1の Link LINK12 と Status OPERATIONAL が表示されること
    ② ステップ1の Active paths 8 と Failed paths 0 が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **Region Switch 確認手順**

    - 検証目的: Region Switch の事前確認で現行・切替先地域、共通 GEOPARM/GEOGROUP、Global Mirror 方向変更を確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。Region Switch 用 procedure の現行地域と切替先を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> 6
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Region Switch - Procedure Confirmation
    Configuration GM2SITE
    Current region REGION1
    Target region REGION2
    GEOPARM COMMON     GEOGROUP COMMON
    GM01 reverse direction REQUIRED
    Run ===> NO
    ```

    REGION1 から REGION2、共通 GEOPARM/GEOGROUP、GM01 reverse direction REQUIRED が切替内容です。

    - 合格条件: ① ステップ1の Current region REGION1 と Target region REGION2 が表示されること
    ② ステップ1の GEOPARM COMMON と GEOGROUP COMMON が表示されること
    ③ ステップ1の GM01 reverse direction REQUIRED が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

    ---

    **freeze policy 確認手順**

    - 検証目的: freeze policy の値と、各値が Freeze 後に選ぶ停止・継続・条件判定のうち現在の設定を確認します。
    - 前提条件: 検証用の IBM GDPS 4.7 環境へ参照権限で接続し、NetView 3270 パネルと構成データを表示できること。切替や停止は実行せず、Run は NO のまま確認します。
    - セッション環境: IBM GDPS 4.7 を実行する NetView 3270 コマンド・ファシリティと GDPS パネル。

    **ステップ 1**
    現在の画面は Selection の入力画面です。現在の PPRCFAILURE 値と Freeze 後の動作説明を表示するため、表示された入力口へ選択値または実在コマンドを指定して実行します。
    操作（入力）:
    ```text
    Selection ===> P
    → Enter を押す
    ```

    画面・出力:
    ```text
    GDPS Metro - Freeze Policy
    Configuration METRO1
    PPRCFAILURE STOP
    Freeze action RESET PRODUCTION SYSTEMS
    Secondary consistency PRESERVED
    Data loss objective RPO 0
    ```

    PPRCFAILURE STOP の Freeze action RESET PRODUCTION SYSTEMS と RPO 0 が停止方針の実動作を示します。

    - 合格条件: ① ステップ1の PPRCFAILURE STOP が表示されること
    ② ステップ1の Freeze action RESET PRODUCTION SYSTEMS が表示されること
    - 検証状態: 机上
    - 出典: GDPS_SG24-6374_Family_Introduction_to_Concepts_and_Capabilities / GDPS_SG24-8367_DS8000_Copy_Services

