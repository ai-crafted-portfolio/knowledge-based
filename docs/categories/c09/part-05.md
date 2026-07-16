---
search:
  exclude: true
---

# GDPS 災害対策・サイトスイッチ — 詳細 (5/5)

[← GDPS 災害対策・サイトスイッチ の概要へ戻る](index.md)


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

