---
search:
  exclude: true
---

# TSO / ISPF / SDSF — 詳細 (6/6)

[← TSO / ISPF / SDSF の概要へ戻る](index.md)


## その他

### その他（特定項目に紐づかないQA・手順） {#c30-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（120問）"
    **問題.** 保存面のREADYプロンプト確認を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってREADY表示と入力待ち状態を確認する場合、どの項目を選ぶべきですか。

    - A. READY prompt ✅
    - B. SDSF ? JDS
    - C. SDSF ULOG
    - D. LISTALC STATUS

    正解: **A** ／ 難易度: 初級

    **解説:** 編集面観点で読むREADYプロンプト確認証跡は正答位置Aで、記録する焦点はREADY prompt読取です。監査面観点のREADYプロンプト確認状態は、TSO/Eコマンド入力可能な状態を識別することを満たす入力、画面、応答を同じ証跡で確認するREADYプロンプト確認状態です。通信面観点のREADYプロンプト確認定義は、READY表示と入力待ち状態を入力記録と合わせて処理対象を見分けるREADYプロンプト確認定義です。保存面観点のREADYプロンプト確認根拠は、TSO/Eセッションの入力要求と戻った表示を結び、運用状態を説明するREADYプロンプト確認根拠です。A: 応答面観点のREADYプロンプト確認読取は、入力名と画面内のREADY表示と入力待ち状態を結ぶREADYプロンプト確認復旧です。B: 検索面観点の参照先はJob Data Set表示状態で、作業記録で追跡する対象はREADYプロンプト確認引継ぎです。C: 端末面観点の比較先はユーザーセッションログ定義で、要求対象はREADYプロンプト確認応答です。D: 出力面観点の照合先は割り当て一覧根拠で、中心はREADYプロンプト確認保守です。照合面観点の用語定義として、READYプロンプト確認とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むREADYプロンプト確認棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide READY

    ---

    **問題.** 照合面のセッション終了を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってREADY配下のログオフ入力を確認する場合、最も適切な確認対象はどれですか。

    - A. OUTDES
    - B. LOGOFF command ✅
    - C. ISPF option 3.2 Data Set Utility
    - D. PF3 END

    正解: **B** ／ 難易度: 初級

    **解説:** 投入面観点の資料照合としてセッション終了読取を選び、答えはBで、記録焦点はセッション終了状態です。保存面観点のセッション終了定義は、TSO/E利用後にログオフして端末セッションを閉じることを満たす入力、画面、応答を同じ証跡で確認するセッション終了定義です。確認面観点から見るセッション終了根拠は、READY配下のログオフ入力を応答画面と対応させるセッション終了根拠です。照合面観点のセッション終了応答は、TSO/Eセッションの入力要求と戻った表示を結び、運用状態を説明するセッション終了応答です。A: 検索面観点の参照先は出力記述子作成状態で、作業記録で追跡する対象はセッション終了棚卸です。B: 端末面観点のセッション終了定義は、入力名と画面内のREADY配下のログオフ入力を結ぶセッション終了照合です。C: 出力面観点の照合先はData Set Utility根拠で、中心はセッション終了監査です。D: 通信面観点の処理段階は終了キー終了応答で、入力と表示を結ぶ対象はセッション終了引継ぎです。選択面観点の用語定義として、セッション終了とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むセッション終了復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide LOGOFF

    ---

    **問題.** 管理面のメッセージID表示を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってプロファイル メッセージID表示を確認する場合、証跡として中心に置く項目はどれですか。

    - A. SEND USER
    - B. ISPF Primary Option Menu
    - C. ISPF EDIT CANCEL
    - D. PROFILE MSGID ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 投入面観点のメッセージID表示定義は正答Dで、表記上の手掛かりはプロファイル メッセージID根拠です。選択面観点のメッセージID表示応答は、TSO/E応答にメッセージIDを表示する設定を確認することを満たす入力、画面、応答を同じ証跡で確認するメッセージID表示応答です。確認面観点で読むメッセージID表示保守は、プロファイル メッセージID表示を資料のコマンド形式やパネル形式と照合するメッセージID表示保守です。管理面観点のメッセージID表示監査は、TSO/Eプロファイルの入力要求と戻った表示を結び、運用状態を説明するメッセージID表示監査です。A: 出力面観点の照合先は短文メッセージ送信根拠で、中心はメッセージID表示棚卸です。B: 通信面観点の処理段階は基本選択メニュー表示応答で、入力と表示を結ぶ対象はメッセージID表示復旧です。C: 監査面観点の参照先は編集取消保守で、作業記録で追跡する対象はメッセージID表示照合です。D: 投入面観点のメッセージID表示監査は、入力名と画面内のプロファイル メッセージID表示を結ぶメッセージID表示選択です。一覧面観点の用語定義として、メッセージID表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むメッセージID表示報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PROFILE MSGID

    ---

    **問題.** 一覧面のコマンドヘルプ表示を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってヘルプ member textとprompt modeを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. HELP command ✅
    - B. LOG and LIST disposition
    - C. SDSF S output data set
    - D. SDSF P purge

    正解: **A** ／ 難易度: 初級

    **解説:** 通信面観点で読むコマンドヘルプ表示根拠は正答位置Aで、記録する焦点はヘルプ command応答です。管理面観点のコマンドヘルプ表示保守は、コマンドの構文やオペランド説明をヘルプデータから確認することを満たす入力、画面、応答を同じ証跡で確認するコマンドヘルプ表示保守です。保存面観点のコマンドヘルプ表示監査は、ヘルプ member textとprompt modeを入力記録と合わせて処理対象を見分けるコマンドヘルプ表示監査です。一覧面観点のコマンドヘルプ表示引継ぎは、TSO/Eヘルプの入力要求と戻った表示を結び、運用状態を説明するコマンドヘルプ表示引継ぎです。A: 編集面観点のコマンドヘルプ表示応答は、入力名と画面内のヘルプ member textとprompt modeを結ぶコマンドヘルプ表示反映です。B: 監査面観点の参照先はログリスト処理保守で、作業記録で追跡する対象はコマンドヘルプ表示報告です。C: 投入面観点の比較先は出力データセット表示監査で、要求対象はコマンドヘルプ表示棚卸です。D: 操作面観点の照合先はジョブ取消と出力削除引継ぎで、中心はコマンドヘルプ表示復旧です。応答面観点の用語定義として、コマンドヘルプ表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むコマンドヘルプ表示選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference HELP

    ---

    **問題.** 応答面の割り当て一覧を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってDD名と実行中表示TA SET NAMEを確認する場合、どの項目を選ぶべきですか。

    - A. RENAME DATASET
    - B. LISTALC STATUS ✅
    - C. PRINTDS
    - D. ISPF option 6 Command

    正解: **B** ／ 難易度: 中級

    **解説:** 確認面観点の資料照合として割り当て一覧応答を選び、答えはBで、記録焦点は割り当て一覧保守です。一覧面観点の割り当て一覧監査は、セッション中に割り当て済みのDD名とデータセットを確認することを満たす入力、画面、応答を同じ証跡で確認する割り当て一覧監査です。選択面観点から見る割り当て一覧引継ぎは、DD名と実行中表示TA SET NAMEを応答画面と対応させる割り当て一覧引継ぎです。応答面観点の割り当て一覧棚卸は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明する割り当て一覧棚卸です。A: 監査面観点の参照先はデータセット改名保守で、作業記録で追跡する対象は割り当て一覧選択です。B: 投入面観点の割り当て一覧監査は、入力名と画面内のDD名と実行中表示TA SET NAMEを結ぶ割り当て一覧観点です。C: 操作面観点の照合先はデータセット印刷引継ぎで、中心は割り当て一覧照合です。D: 保存面観点の処理段階はTSO Command Processor棚卸で、入力と表示を結ぶ対象は割り当て一覧報告です。制御面観点の用語定義として、割り当て一覧とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む割り当て一覧反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference LISTALC

    ---

    **問題.** 制御面のメンバー一覧表示を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってMEMBERS operandとmember nameを確認する場合、最も適切な確認対象はどれですか。

    - A. ISPF SPLIT screen
    - B. SDSF ? JDS
    - C. LISTDS MEMBERS ✅
    - D. SDSF slash MVS command

    正解: **C** ／ 難易度: 中級

    **解説:** 保存面観点の出力確認としてメンバー一覧表示保守を読み、答えはCで、照合焦点はメンバー一覧表示監査です。応答面観点のメンバー一覧表示引継ぎは、PDSまたはPDSEのメンバー一覧を確認することを満たす入力、画面、応答を同じ証跡で確認するメンバー一覧表示引継ぎです。一覧面観点で残すメンバー一覧表示棚卸は、MEMBERS operandとmember nameをコマンドまたはパネル形式と照合するメンバー一覧表示棚卸です。制御面観点のメンバー一覧表示復旧は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するメンバー一覧表示復旧です。A: 投入面観点の比較先は画面分割監査で、要求対象はメンバー一覧表示照合です。B: 操作面観点の照合先はJob Data Set表示引継ぎで、中心はメンバー一覧表示報告です。C: 通信面観点のメンバー一覧表示棚卸は、入力名と画面内のMEMBERS operandとmember nameを結ぶメンバー一覧表示証跡です。D: 管理面観点の参照先はMVSコマンド発行復旧で、作業記録で追跡する対象はメンバー一覧表示反映です。端末面観点の用語定義として、メンバー一覧表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むメンバー一覧表示観点です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference LISTDS

    ---

    **問題.** 端末面のデータセット割り当てを表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って割り当て データセット and DD名を確認する場合、この状況で優先する項目はどれですか。

    - A. FREE DDNAME
    - B. OUTDES
    - C. ISPF option 3.3 Move Copy
    - D. ALLOCATE DATASET ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 確認面観点のデータセット割り当て監査は正答Dで、表記上の手掛かりは割り当て データセット引継ぎです。制御面観点のデータセット割り当て棚卸は、TSO/Eコマンド処理で使うDD名をデータセットへ割り当てることを満たす入力、画面、応答を同じ証跡で確認するデータセット割り当て棚卸です。選択面観点で読むデータセット割り当て復旧は、割り当て データセット and DD名を資料のコマンド形式やパネル形式と照合するデータセット割り当て復旧です。端末面観点のデータセット割り当て照合は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明するデータセット割り当て照合です。A: 操作面観点の照合先はDD名解放引継ぎで、中心はデータセット割り当て選択です。B: 保存面観点の処理段階は出力記述子作成棚卸で、入力と表示を結ぶ対象はデータセット割り当て反映です。C: 管理面観点の参照先はMOVE/COPY復旧で、作業記録で追跡する対象はデータセット割り当て観点です。D: 確認面観点のデータセット割り当て照合は、入力名と画面内の割り当て データセット and DD名を結ぶデータセット割り当て読取です。表示面観点の用語定義として、データセット割り当てとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット割り当て証跡です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference ALLOCATE

    ---

    **問題.** 表示面のDD名解放を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って解放 FILE operandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. FREE DDNAME ✅
    - B. ISPF EDIT CANCEL
    - C. LOG and LIST disposition
    - D. SDSF PREFIX

    正解: **A** ／ 難易度: 中級

    **解説:** 保存面観点で読むDD名解放引継ぎは正答位置Aで、記録する焦点は解放 DD名棚卸です。端末面観点のDD名解放復旧は、不要になったDD名割り当てをセッションから外すことを満たす入力、画面、応答を同じ証跡で確認するDD名解放復旧です。一覧面観点のDD名解放照合は、解放 FILE operandを入力記録と合わせて処理対象を見分けるDD名解放照合です。表示面観点のDD名解放報告は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明するDD名解放報告です。A: 通信面観点のDD名解放棚卸は、入力名と画面内の解放 FILE operandを結ぶDD名解放状態です。B: 管理面観点の参照先は編集取消復旧で、作業記録で追跡する対象はDD名解放証跡です。C: 確認面観点の比較先はログリスト処理照合で、要求対象はDD名解放選択です。D: 照合面観点の照合先はジョブ名接頭辞報告で、中心はDD名解放反映です。編集面観点の用語定義として、DD名解放とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むDD名解放読取です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference FREE

    ---

    **問題.** 編集面のデータセット改名を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってold データセット name and new データセット nameを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. PROFILE PREFIX
    - B. RENAME DATASET ✅
    - C. DELETE DATASET
    - D. ISPF Primary Option Menu

    正解: **B** ／ 難易度: 中級

    **解説:** 選択面観点の資料照合としてデータセット改名棚卸を選び、答えはBで、記録焦点はデータセット改名復旧です。表示面観点のデータセット改名照合は、既存データセット名を新しい名前へ変更することを満たす入力、画面、応答を同じ証跡で確認するデータセット改名照合です。制御面観点から見るデータセット改名報告は、old データセット name and new データセット nameを応答画面と対応させるデータセット改名報告です。編集面観点のデータセット改名選択は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するデータセット改名選択です。A: 管理面観点の参照先はデータセット接頭辞復旧で、作業記録で追跡する対象はデータセット改名読取です。B: 確認面観点のデータセット改名照合は、入力名と画面内のold データセット name and new データセット nameを結ぶデータセット改名定義です。C: 照合面観点の照合先はデータセット削除報告で、中心はデータセット改名観点です。D: 一覧面観点の処理段階は基本選択メニュー表示選択で、入力と表示を結ぶ対象はデータセット改名証跡です。出力面観点の用語定義として、データセット改名とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット改名状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference RENAME

    ---

    **問題.** 出力面のデータセット削除を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って削除 command and データセット nameを確認する場合、どの項目を選ぶべきですか。

    - A. ISPF EDIT CANCEL
    - B. LOG and LIST disposition
    - C. DELETE DATASET ✅
    - D. SDSF PREFIX

    正解: **C** ／ 難易度: 中級

    **解説:** 一覧面観点の出力確認としてデータセット削除復旧を読み、答えはCで、照合焦点はデータセット削除照合です。編集面観点のデータセット削除報告は、不要なデータセットをTSO/Eコマンドで削除することを満たす入力、画面、応答を同じ証跡で確認するデータセット削除報告です。表示面観点で残すデータセット削除選択は、削除 command and データセット nameをコマンドまたはパネル形式と照合するデータセット削除選択です。出力面観点のデータセット削除反映は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するデータセット削除反映です。A: 確認面観点の比較先は編集取消照合で、要求対象はデータセット削除観点です。B: 照合面観点の照合先はログリスト処理報告で、中心はデータセット削除証跡です。C: 保存面観点のデータセット削除選択は、入力名と画面内の削除 command and データセット nameを結ぶデータセット削除根拠です。D: 端末面観点の参照先はジョブ名接頭辞反映で、作業記録で追跡する対象はデータセット削除状態です。投入面観点の用語定義として、データセット削除とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット削除定義です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference DELETE

    ---

    **問題.** 投入面の短文メッセージ送信を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って送信 command and target userを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF FILTER
    - B. LOGOFF command
    - C. RENAME DATASET
    - D. SEND USER ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 選択面観点の短文メッセージ送信照合は正答Dで、表記上の手掛かりは送信 USER報告です。出力面観点の短文メッセージ送信選択は、同一システムの利用者へ短いメッセージを送ることを満たす入力、画面、応答を同じ証跡で確認する短文メッセージ送信選択です。制御面観点で読む短文メッセージ送信反映は、送信 command and target userを資料のコマンド形式やパネル形式と照合する短文メッセージ送信反映です。投入面観点の短文メッセージ送信観点は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明する短文メッセージ送信観点です。A: 照合面観点の照合先は条件フィルター報告で、中心は短文メッセージ送信読取です。B: 一覧面観点の処理段階はセッション終了選択で、入力と表示を結ぶ対象は短文メッセージ送信状態です。C: 端末面観点の参照先はデータセット改名反映で、作業記録で追跡する対象は短文メッセージ送信定義です。D: 選択面観点の短文メッセージ送信観点は、入力名と画面内の送信 command and target userを結ぶ短文メッセージ送信応答です。検索面観点の用語定義として、短文メッセージ送信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む短文メッセージ送信根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide SEND

    ---

    **問題.** 検索面のブロードキャスト表示を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってbroadcast データセット messagesを確認する場合、この状況で優先する項目はどれですか。

    - A. LISTBC ✅
    - B. OUTDES
    - C. ISPF option 3.2 Data Set Utility
    - D. PF3 END

    正解: **A** ／ 難易度: 初級

    **解説:** 一覧面観点で読むブロードキャスト表示報告は正答位置Aで、記録する焦点はブロードキャスト表示選択です。投入面観点のブロードキャスト表示反映は、システムや他利用者からのメッセージを確認することを満たす入力、画面、応答を同じ証跡で確認するブロードキャスト表示反映です。表示面観点のブロードキャスト表示観点は、broadcast データセット messagesを入力記録と合わせて処理対象を見分けるブロードキャスト表示観点です。検索面観点のブロードキャスト表示証跡は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明するブロードキャスト表示証跡です。A: 保存面観点のブロードキャスト表示選択は、入力名と画面内のbroadcast データセット messagesを結ぶブロードキャスト表示保守です。B: 端末面観点の参照先は出力記述子作成反映で、作業記録で追跡する対象はブロードキャスト表示根拠です。C: 選択面観点の比較先はData Set Utility観点で、要求対象はブロードキャスト表示読取です。D: 応答面観点の照合先は終了キー終了証跡で、中心はブロードキャスト表示状態です。通信面観点の用語定義として、ブロードキャスト表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むブロードキャスト表示応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide LISTBC

    ---

    **問題.** 通信面のデータセット送信を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って転送送信 target and データセット operandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF P purge
    - B. TRANSMIT DATASET ✅
    - C. LISTALC STATUS
    - D. RECEIVE DATASET

    正解: **B** ／ 難易度: 上級

    **解説:** 制御面観点の資料照合としてデータセット送信選択を選び、答えはBで、記録焦点はデータセット送信反映です。検索面観点のデータセット送信観点は、別ユーザーまたは別ノードへデータセットを送信することを満たす入力、画面、応答を同じ証跡で確認するデータセット送信観点です。出力面観点から見るデータセット送信証跡は、転送送信 target and データセット operandを応答画面と対応させるデータセット送信証跡です。通信面観点のデータセット送信読取は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明するデータセット送信読取です。A: 端末面観点の参照先はジョブ取消と出力削除反映で、作業記録で追跡する対象はデータセット送信応答です。B: 選択面観点のデータセット送信観点は、入力名と画面内の転送送信 target and データセット operandを結ぶデータセット送信監査です。C: 応答面観点の照合先は割り当て一覧証跡で、中心はデータセット送信定義です。D: 表示面観点の処理段階は送信データ受信読取で、入力と表示を結ぶ対象はデータセット送信根拠です。操作面観点の用語定義として、データセット送信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット送信保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference TRANSMIT

    ---

    **問題.** 操作面の送信データ受信を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って転送受信 prompt and データセット nameを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF option 3.4 DSLIST
    - B. ISPF FIND
    - C. RECEIVE DATASET ✅
    - D. SDSF I panel

    正解: **C** ／ 難易度: 中級

    **解説:** 表示面観点の出力確認として送信データ受信反映を読み、答えはCで、照合焦点は送信データ受信観点です。通信面観点の送信データ受信証跡は、転送送信されたデータセットや長文メッセージを受信することを満たす入力、画面、応答を同じ証跡で確認する送信データ受信証跡です。検索面観点で残す送信データ受信読取は、転送受信 prompt and データセット nameをコマンドまたはパネル形式と照合する送信データ受信読取です。操作面観点の送信データ受信状態は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明する送信データ受信状態です。A: 選択面観点の比較先はデータセット一覧一覧観点で、要求対象は送信データ受信定義です。B: 応答面観点の照合先は文字列検索証跡で、中心は送信データ受信根拠です。C: 一覧面観点の送信データ受信読取は、入力名と画面内の転送受信 prompt and データセット nameを結ぶ送信データ受信引継ぎです。D: 投入面観点の参照先はInput Queue状態で、作業記録で追跡する対象は送信データ受信保守です。確認面観点の用語定義として、送信データ受信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む送信データ受信監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference RECEIVE

    ---

    **問題.** 確認面の出力記述子作成を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って出力記述子 operand and destinationを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF DA panel
    - B. SDSF OWNER
    - C. READY prompt
    - D. OUTDES ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 制御面観点の出力記述子作成観点は正答Dで、表記上の手掛かりは出力記述子証跡です。操作面観点の出力記述子作成読取は、印刷や出力処理の宛先属性を定義することを満たす入力、画面、応答を同じ証跡で確認する出力記述子作成読取です。出力面観点で読む出力記述子作成状態は、出力記述子 operand and destinationを資料のコマンド形式やパネル形式と照合する出力記述子作成状態です。確認面観点の出力記述子作成定義は、TSO/E出力の入力要求と戻った表示を結び、運用状態を説明する出力記述子作成定義です。A: 応答面観点の照合先は実行中利用者表示証跡で、中心は出力記述子作成応答です。B: 表示面観点の処理段階は所有者絞り込み読取で、入力と表示を結ぶ対象は出力記述子作成保守です。C: 投入面観点の参照先はREADYプロンプト確認状態で、作業記録で追跡する対象は出力記述子作成監査です。D: 制御面観点の出力記述子作成定義は、入力名と画面内の出力記述子 operand and destinationを結ぶ出力記述子作成棚卸です。監査面観点の用語定義として、出力記述子作成とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む出力記述子作成引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference OUTDES

    ---

    **問題.** 監査面のデータセット印刷を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って印刷 データセット operandを確認する場合、最も適切な確認対象はどれですか。

    - A. PRINTDS ✅
    - B. RENAME DATASET
    - C. CALL command
    - D. ISPF EDIT SAVE

    正解: **A** ／ 難易度: 中級

    **解説:** 表示面観点で読むデータセット印刷証跡は正答位置Aで、記録する焦点は印刷読取です。確認面観点のデータセット印刷状態は、データセット内容を印刷または出力キューへ送ることを満たす入力、画面、応答を同じ証跡で確認するデータセット印刷状態です。検索面観点のデータセット印刷定義は、印刷 データセット operandを入力記録と合わせて処理対象を見分けるデータセット印刷定義です。監査面観点のデータセット印刷根拠は、TSO/E出力の入力要求と戻った表示を結び、運用状態を説明するデータセット印刷根拠です。A: 一覧面観点のデータセット印刷読取は、入力名と画面内の印刷 データセット operandを結ぶデータセット印刷復旧です。B: 投入面観点の参照先はデータセット改名状態で、作業記録で追跡する対象はデータセット印刷引継ぎです。C: 制御面観点の比較先はロードモジュール呼出定義で、要求対象はデータセット印刷応答です。D: 編集面観点の照合先は編集保存根拠で、中心はデータセット印刷保守です。保存面観点の用語定義として、データセット印刷とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット印刷棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PRINTDS

    ---

    **問題.** 選択面の表示選択を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って表示 option and データセット nameを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF SORT
    - B. READY prompt
    - C. FREE DDNAME
    - D. ISPF option 1 BROWSE ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力面観点の表示選択定義は正答Dで、表記上の手掛かりは対話式生産性機能 option 1 表示根拠です。照合面観点の表示選択応答は、データセットを更新せず表示することを満たす入力、画面、応答を同じ証跡で確認する表示選択応答です。操作面観点で読む表示選択保守は、表示 option and データセット nameを資料のコマンド形式やパネル形式と照合する表示選択保守です。選択面観点の表示選択監査は、対話式生産性機能表示の入力要求と戻った表示を結び、運用状態を説明する表示選択監査です。A: 編集面観点の照合先は列ソート根拠で、中心は表示選択棚卸です。B: 検索面観点の処理段階はREADYプロンプト確認応答で、入力と表示を結ぶ対象は表示選択復旧です。C: 確認面観点の参照先はDD名解放保守で、作業記録で追跡する対象は表示選択照合です。D: 出力面観点の表示選択監査は、入力名と画面内の表示 option and データセット nameを結ぶ表示選択選択です。管理面観点の用語定義として、表示選択とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む表示選択報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide BROWSE

    ---

    **問題.** 管理面の編集選択を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って編集 option and edit パネルを確認する場合、どの項目を選ぶべきですか。

    - A. ISPF option 2 EDIT ✅
    - B. RECEIVE DATASET
    - C. ISPF option 3.2 Data Set Utility
    - D. PF3 END

    正解: **A** ／ 難易度: 初級

    **解説:** 検索面観点で読む編集選択根拠は正答位置Aで、記録する焦点は対話式生産性機能 option 2 編集応答です。選択面観点の編集選択保守は、ソースやJCLメンバーを編集することを満たす入力、画面、応答を同じ証跡で確認する編集選択保守です。監査面観点の編集選択監査は、編集 option and edit パネルを入力記録と合わせて処理対象を見分ける編集選択監査です。管理面観点の編集選択引継ぎは、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集選択引継ぎです。A: 表示面観点の編集選択応答は、入力名と画面内の編集 option and edit パネルを結ぶ編集選択反映です。B: 確認面観点の参照先は送信データ受信保守で、作業記録で追跡する対象は編集選択報告です。C: 出力面観点の比較先はData Set Utility監査で、要求対象は編集選択棚卸です。D: 通信面観点の照合先は終了キー終了引継ぎで、中心は編集選択復旧です。一覧面観点の用語定義として、編集選択とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集選択選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide EDIT

    ---

    **問題.** 一覧面のデータセット一覧一覧を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってデータセット一覧 パネル and DSNAME LEVELを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF OWNER
    - B. ISPF option 3.4 DSLIST ✅
    - C. SDSF H hold
    - D. ALLOCATE DATASET

    正解: **B** ／ 難易度: 中級

    **解説:** 操作面観点の資料照合としてデータセット一覧一覧応答を選び、答えはBで、記録焦点はデータセット一覧一覧保守です。管理面観点のデータセット一覧一覧監査は、データセット一覧から表示、編集、削除などを行うことを満たす入力、画面、応答を同じ証跡で確認するデータセット一覧一覧監査です。照合面観点から見るデータセット一覧一覧引継ぎは、データセット一覧 パネル and DSNAME LEVELを応答画面と対応させるデータセット一覧一覧引継ぎです。一覧面観点のデータセット一覧一覧棚卸は、対話式生産性機能ユーティリティの入力要求と戻った表示を結び、運用状態を説明するデータセット一覧一覧棚卸です。A: 確認面観点の参照先は所有者絞り込み保守で、作業記録で追跡する対象はデータセット一覧一覧選択です。B: 出力面観点のデータセット一覧一覧監査は、入力名と画面内のデータセット一覧 パネル and DSNAME LEVELを結ぶデータセット一覧一覧観点です。C: 通信面観点の照合先はジョブ保留引継ぎで、中心はデータセット一覧一覧照合です。D: 監査面観点の処理段階はデータセット割り当て棚卸で、入力と表示を結ぶ対象はデータセット一覧一覧報告です。応答面観点の用語定義として、データセット一覧一覧とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット一覧一覧反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide DSLIST

    ---

    **問題.** 制御面のMOVE/COPYを証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってMove/Copy utility パネルを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF OWNER
    - B. SDSF H hold
    - C. ALLOCATE DATASET
    - D. ISPF option 3.3 Move Copy ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 操作面観点のMOVE/COPY監査は正答Dで、表記上の手掛かりは対話式生産性機能 option 3.3 Move Copy引継ぎです。応答面観点のMOVE/COPY棚卸は、データセットやメンバーを移動またはコピーすることを満たす入力、画面、応答を同じ証跡で確認するMOVE/COPY棚卸です。照合面観点で読むMOVE/COPY復旧は、Move/Copy utility パネルを資料のコマンド形式やパネル形式と照合するMOVE/COPY復旧です。制御面観点のMOVE/COPY照合は、対話式生産性機能ユーティリティの入力要求と戻った表示を結び、運用状態を説明するMOVE/COPY照合です。A: 通信面観点の照合先は所有者絞り込み引継ぎで、中心はMOVE/COPY選択です。B: 監査面観点の処理段階はジョブ保留棚卸で、入力と表示を結ぶ対象はMOVE/COPY反映です。C: 選択面観点の参照先はデータセット割り当て復旧で、作業記録で追跡する対象はMOVE/COPY観点です。D: 操作面観点のMOVE/COPY照合は、入力名と画面内のMove/Copy utility パネルを結ぶMOVE/COPY読取です。端末面観点の用語定義として、MOVE/COPYとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むMOVE/COPY証跡です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide Move Copy

    ---

    **問題.** 表示面の編集保存を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って保存 primary commandを確認する場合、どの項目を選ぶべきですか。

    - A. ISPF FIND
    - B. ISPF EDIT SAVE ✅
    - C. SDSF DA panel
    - D. SDSF SORT

    正解: **B** ／ 難易度: 中級

    **解説:** 照合面観点の資料照合として編集保存棚卸を選び、答えはBで、記録焦点は編集保存復旧です。端末面観点の編集保存照合は、編集したメンバーを保存してセッションを継続または終了することを満たす入力、画面、応答を同じ証跡で確認する編集保存照合です。応答面観点から見る編集保存報告は、保存 primary commandを応答画面と対応させる編集保存報告です。表示面観点の編集保存選択は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集保存選択です。A: 選択面観点の参照先は文字列検索復旧で、作業記録で追跡する対象は編集保存読取です。B: 操作面観点の編集保存照合は、入力名と画面内の保存 primary commandを結ぶ編集保存定義です。C: 保存面観点の照合先は実行中利用者表示報告で、中心は編集保存観点です。D: 管理面観点の処理段階は列ソート選択で、入力と表示を結ぶ対象は編集保存証跡です。編集面観点の用語定義として、編集保存とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集保存状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide editor SAVE

    ---

    **問題.** 編集面の編集取消を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って取消 primary commandを確認する場合、最も適切な確認対象はどれですか。

    - A. PROFILE MSGID
    - B. DELETE DATASET
    - C. ISPF EDIT CANCEL ✅
    - D. ISPF Primary Option Menu

    正解: **C** ／ 難易度: 中級

    **解説:** 管理面観点の出力確認として編集取消復旧を読み、答えはCで、照合焦点は編集取消照合です。表示面観点の編集取消報告は、保存せず編集内容を破棄して終了することを満たす入力、画面、応答を同じ証跡で確認する編集取消報告です。端末面観点で残す編集取消選択は、取消 primary commandをコマンドまたはパネル形式と照合する編集取消選択です。編集面観点の編集取消反映は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集取消反映です。A: 操作面観点の比較先はメッセージID表示照合で、要求対象は編集取消観点です。B: 保存面観点の照合先はデータセット削除報告で、中心は編集取消証跡です。C: 監査面観点の編集取消選択は、入力名と画面内の取消 primary commandを結ぶ編集取消根拠です。D: 制御面観点の参照先は基本選択メニュー表示反映で、作業記録で追跡する対象は編集取消状態です。出力面観点の用語定義として、編集取消とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集取消定義です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide editor CANCEL

    ---

    **問題.** 出力面のJCLサブミットを表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って投入 primary command and JOB statementを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF EDIT CANCEL
    - B. SDSF ST panel
    - C. SDSF OWNER
    - D. ISPF EDIT SUBMIT ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 照合面観点のJCLサブミット照合は正答Dで、表記上の手掛かりは対話式生産性機能 編集 投入報告です。編集面観点のJCLサブミット選択は、編集画面からJCLをJESへ投入することを満たす入力、画面、応答を同じ証跡で確認するJCLサブミット選択です。応答面観点で読むJCLサブミット反映は、投入 primary command and JOB statementを資料のコマンド形式やパネル形式と照合するJCLサブミット反映です。出力面観点のJCLサブミット観点は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明するJCLサブミット観点です。A: 保存面観点の照合先は編集取消報告で、中心はJCLサブミット読取です。B: 管理面観点の処理段階はStatus パネル選択で、入力と表示を結ぶ対象はJCLサブミット状態です。C: 制御面観点の参照先は所有者絞り込み反映で、作業記録で追跡する対象はJCLサブミット定義です。D: 照合面観点のJCLサブミット観点は、入力名と画面内の投入 primary command and JOB statementを結ぶJCLサブミット応答です。投入面観点の用語定義として、JCLサブミットとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むJCLサブミット根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide SUBMIT

    ---

    **問題.** 投入面の文字列検索を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って検索 primary commandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. ISPF FIND ✅
    - B. SDSF SORT
    - C. READY prompt
    - D. FREE DDNAME

    正解: **A** ／ 難易度: 初級

    **解説:** 管理面観点で読む文字列検索報告は正答位置Aで、記録する焦点は対話式生産性機能 検索選択です。出力面観点の文字列検索反映は、編集または表示中のデータから文字列を探すことを満たす入力、画面、応答を同じ証跡で確認する文字列検索反映です。端末面観点の文字列検索観点は、検索 primary commandを入力記録と合わせて処理対象を見分ける文字列検索観点です。投入面観点の文字列検索証跡は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する文字列検索証跡です。A: 監査面観点の文字列検索選択は、入力名と画面内の検索 primary commandを結ぶ文字列検索保守です。B: 制御面観点の参照先は列ソート反映で、作業記録で追跡する対象は文字列検索根拠です。C: 照合面観点の比較先はREADYプロンプト確認観点で、要求対象は文字列検索読取です。D: 一覧面観点の照合先はDD名解放証跡で、中心は文字列検索状態です。検索面観点の用語定義として、文字列検索とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む文字列検索応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide FIND

    ---

    **問題.** 検索面の文字列置換を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って置換 primary commandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF Primary Option Menu
    - B. ISPF CHANGE ✅
    - C. ISPF EDIT SAVE
    - D. SDSF ST panel

    正解: **B** ／ 難易度: 中級

    **解説:** 応答面観点の資料照合として文字列置換選択を選び、答えはBで、記録焦点は文字列置換反映です。投入面観点の文字列置換観点は、編集データ内の文字列を別の値へ置き換えることを満たす入力、画面、応答を同じ証跡で確認する文字列置換観点です。編集面観点から見る文字列置換証跡は、置換 primary commandを応答画面と対応させる文字列置換証跡です。検索面観点の文字列置換読取は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する文字列置換読取です。A: 制御面観点の参照先は基本選択メニュー表示反映で、作業記録で追跡する対象は文字列置換応答です。B: 照合面観点の文字列置換観点は、入力名と画面内の置換 primary commandを結ぶ文字列置換監査です。C: 一覧面観点の照合先は編集保存証跡で、中心は文字列置換定義です。D: 端末面観点の処理段階はStatus パネル読取で、入力と表示を結ぶ対象は文字列置換根拠です。通信面観点の用語定義として、文字列置換とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む文字列置換保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide CHANGE

    ---

    **問題.** 通信面の終了キー終了を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って終了キー 終了 keyを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF H panel
    - B. SDSF ARRANGE
    - C. PF3 END ✅
    - D. PROFILE MSGID

    正解: **C** ／ 難易度: 初級

    **解説:** 端末面観点の出力確認として終了キー終了反映を読み、答えはCで、照合焦点は終了キー終了観点です。検索面観点の終了キー終了証跡は、現在のパネルから前画面へ戻ることを満たす入力、画面、応答を同じ証跡で確認する終了キー終了証跡です。投入面観点で残す終了キー終了読取は、終了キー 終了 keyをコマンドまたはパネル形式と照合する終了キー終了読取です。通信面観点の終了キー終了状態は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する終了キー終了状態です。A: 照合面観点の比較先はHeld Output Queue観点で、要求対象は終了キー終了定義です。B: 一覧面観点の照合先は列配置変更証跡で、中心は終了キー終了根拠です。C: 管理面観点の終了キー終了読取は、入力名と画面内の終了キー 終了 keyを結ぶ終了キー終了引継ぎです。D: 出力面観点の参照先はメッセージID表示状態で、作業記録で追跡する対象は終了キー終了保守です。操作面観点の用語定義として、終了キー終了とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む終了キー終了監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide END PF key

    ---

    **問題.** 操作面のヘルプキー表示を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってヘルプキー ヘルプ keyを確認する場合、最も適切な確認対象はどれですか。

    - A. LISTBC
    - B. ISPF option 1 BROWSE
    - C. ISPF EDIT SUBMIT
    - D. PF1 HELP ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 応答面観点のヘルプキー表示観点は正答Dで、表記上の手掛かりはヘルプキー ヘルプ証跡です。通信面観点のヘルプキー表示読取は、現在パネルに対応するチュートリアルやヘルプを表示することを満たす入力、画面、応答を同じ証跡で確認するヘルプキー表示読取です。編集面観点で読むヘルプキー表示状態は、ヘルプキー ヘルプ keyを資料のコマンド形式やパネル形式と照合するヘルプキー表示状態です。操作面観点のヘルプキー表示定義は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明するヘルプキー表示定義です。A: 一覧面観点の照合先はブロードキャスト表示証跡で、中心はヘルプキー表示応答です。B: 端末面観点の処理段階は表示選択読取で、入力と表示を結ぶ対象はヘルプキー表示保守です。C: 出力面観点の参照先はJCLサブミット状態で、作業記録で追跡する対象はヘルプキー表示監査です。D: 応答面観点のヘルプキー表示定義は、入力名と画面内のヘルプキー ヘルプ keyを結ぶヘルプキー表示棚卸です。確認面観点の用語定義として、ヘルプキー表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むヘルプキー表示引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide HELP PF key

    ---

    **問題.** 確認面の画面分割を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って画面分割 and SWAP behaviorを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF SPLIT screen ✅
    - B. SDSF ARRANGE
    - C. PROFILE PREFIX
    - D. DELETE DATASET

    正解: **A** ／ 難易度: 上級

    **解説:** 端末面観点で読む画面分割証跡は正答位置Aで、記録する焦点は対話式生産性機能 画面分割 screen読取です。操作面観点の画面分割状態は、複数論理画面を切り替えて作業することを満たす入力、画面、応答を同じ証跡で確認する画面分割状態です。投入面観点の画面分割定義は、画面分割 and SWAP behaviorを入力記録と合わせて処理対象を見分ける画面分割定義です。確認面観点の画面分割根拠は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する画面分割根拠です。A: 管理面観点の画面分割読取は、入力名と画面内の画面分割 and SWAP behaviorを結ぶ画面分割復旧です。B: 出力面観点の参照先は列配置変更状態で、作業記録で追跡する対象は画面分割引継ぎです。C: 応答面観点の比較先はデータセット接頭辞定義で、要求対象は画面分割応答です。D: 表示面観点の照合先はデータセット削除根拠で、中心は画面分割保守です。監査面観点の用語定義として、画面分割とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む画面分割棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide split screen

    ---

    **問題.** 監査面のログリスト処理を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってログ and リスト disposition パネルを確認する場合、証跡として中心に置く項目はどれですか。

    - A. ISPF EDIT SAVE
    - B. LOG and LIST disposition ✅
    - C. ISPF SPLIT screen
    - D. SDSF PREFIX

    正解: **B** ／ 難易度: 中級

    **解説:** 編集面観点の資料照合としてログリスト処理読取を選び、答えはBで、記録焦点はログリスト処理状態です。確認面観点のログリスト処理定義は、対話式生産性機能終了時のログ/リスト出力を印刷または削除することを満たす入力、画面、応答を同じ証跡で確認するログリスト処理定義です。通信面観点から見るログリスト処理根拠は、ログ and リスト disposition パネルを応答画面と対応させるログリスト処理根拠です。監査面観点のログリスト処理応答は、対話式生産性機能終了の入力要求と戻った表示を結び、運用状態を説明するログリスト処理応答です。A: 出力面観点の参照先は編集保存状態で、作業記録で追跡する対象はログリスト処理棚卸です。B: 応答面観点のログリスト処理定義は、入力名と画面内のログ and リスト disposition パネルを結ぶログリスト処理照合です。C: 表示面観点の照合先は画面分割根拠で、中心はログリスト処理監査です。D: 投入面観点の処理段階はジョブ名接頭辞応答で、入力と表示を結ぶ対象はログリスト処理引継ぎです。保存面観点の用語定義として、ログリスト処理とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むログリスト処理復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide LOG LIST disposition

    ---

    **問題.** 照合面の実行中利用者表示を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って実行中表示 パネル and 実行中アドレス空間を確認する場合、どの項目を選ぶべきですか。

    - A. SEND USER
    - B. ISPF Primary Option Menu
    - C. ISPF EDIT CANCEL
    - D. SDSF DA panel ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 編集面観点の実行中利用者表示定義は正答Dで、表記上の手掛かりはスプール表示検索機能 実行中表示 パネル根拠です。保存面観点の実行中利用者表示応答は、実行中アドレス空間やジョブの状態を確認することを満たす入力、画面、応答を同じ証跡で確認する実行中利用者表示応答です。通信面観点で読む実行中利用者表示保守は、実行中表示 パネル and 実行中アドレス空間を資料のコマンド形式やパネル形式と照合する実行中利用者表示保守です。照合面観点の実行中利用者表示監査は、スプール表示検索機能ジョブ管理の入力要求と戻った表示を結び、運用状態を説明する実行中利用者表示監査です。A: 表示面観点の照合先は短文メッセージ送信根拠で、中心は実行中利用者表示棚卸です。B: 投入面観点の処理段階は基本選択メニュー表示応答で、入力と表示を結ぶ対象は実行中利用者表示復旧です。C: 操作面観点の参照先は編集取消保守で、作業記録で追跡する対象は実行中利用者表示照合です。D: 編集面観点の実行中利用者表示監査は、入力名と画面内の実行中表示 パネル and 実行中アドレス空間を結ぶ実行中利用者表示選択です。選択面観点の用語定義として、実行中利用者表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む実行中利用者表示報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide DA panel

    ---

    **問題.** 選択面のInput Queueを操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってI パネル job queueを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF I panel ✅
    - B. LOG and LIST disposition
    - C. SDSF PREFIX
    - D. SDSF H hold

    正解: **A** ／ 難易度: 中級

    **解説:** 投入面観点で読むInput Queue根拠は正答位置Aで、記録する焦点はスプール表示検索機能 I パネル応答です。照合面観点のInput Queue保守は、入力キュー上または実行中ジョブを確認することを満たす入力、画面、応答を同じ証跡で確認するInput Queue保守です。確認面観点のInput Queue監査は、I パネル job queueを入力記録と合わせて処理対象を見分けるInput Queue監査です。選択面観点のInput Queue引継ぎは、スプール表示検索機能キューの入力要求と戻った表示を結び、運用状態を説明するInput Queue引継ぎです。A: 端末面観点のInput Queue応答は、入力名と画面内のI パネル job queueを結ぶInput Queue反映です。B: 操作面観点の参照先はログリスト処理保守で、作業記録で追跡する対象はInput Queue報告です。C: 編集面観点の比較先はジョブ名接頭辞監査で、要求対象はInput Queue棚卸です。D: 検索面観点の照合先はジョブ保留引継ぎで、中心はInput Queue復旧です。管理面観点の用語定義として、Input Queueとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むInput Queue選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide Input Queue

    ---

    **問題.** 制御面の出力データセット表示を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってS 行操作 and 出力表示を確認する場合、どの項目を選ぶべきですか。

    - A. SDSF S output data set ✅
    - B. SDSF O panel
    - C. SDSF ARRANGE
    - D. PROFILE MSGID

    正解: **A** ／ 難易度: 初級

    **解説:** 確認面観点で読む出力データセット表示引継ぎは正答位置Aで、記録する焦点はスプール表示検索機能 S 出力データセット棚卸です。応答面観点の出力データセット表示復旧は、ジョブデータセット表示パネル上で個別出力データセットを表示することを満たす入力、画面、応答を同じ証跡で確認する出力データセット表示復旧です。選択面観点の出力データセット表示照合は、S 行操作 and 出力表示を入力記録と合わせて処理対象を見分ける出力データセット表示照合です。制御面観点の出力データセット表示報告は、スプール表示検索機能出力参照の入力要求と戻った表示を結び、運用状態を説明する出力データセット表示報告です。A: 投入面観点の出力データセット表示棚卸は、入力名と画面内のS 行操作 and 出力表示を結ぶ出力データセット表示状態です。B: 照合面観点の参照先はOutput Queue復旧で、作業記録で追跡する対象は出力データセット表示証跡です。C: 通信面観点の比較先は列配置変更照合で、要求対象は出力データセット表示選択です。D: 監査面観点の照合先はメッセージID表示報告で、中心は出力データセット表示反映です。端末面観点の用語定義として、出力データセット表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む出力データセット表示読取です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide output browse

    ---

    **問題.** 端末面のジョブ名接頭辞を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って接頭辞 commandを確認する場合、最も適切な確認対象はどれですか。

    - A. READY prompt
    - B. SDSF PREFIX ✅
    - C. ALLOCATE DATASET
    - D. OUTDES

    正解: **B** ／ 難易度: 中級

    **解説:** 保存面観点の資料照合としてジョブ名接頭辞棚卸を選び、答えはBで、記録焦点はジョブ名接頭辞復旧です。制御面観点のジョブ名接頭辞照合は、表示対象ジョブ名を接頭辞で絞り込むことを満たす入力、画面、応答を同じ証跡で確認するジョブ名接頭辞照合です。一覧面観点から見るジョブ名接頭辞報告は、接頭辞 commandを応答画面と対応させるジョブ名接頭辞報告です。端末面観点のジョブ名接頭辞選択は、スプール表示検索機能フィルターの入力要求と戻った表示を結び、運用状態を説明するジョブ名接頭辞選択です。A: 照合面観点の参照先はREADYプロンプト確認復旧で、作業記録で追跡する対象はジョブ名接頭辞読取です。B: 通信面観点のジョブ名接頭辞照合は、入力名と画面内の接頭辞 commandを結ぶジョブ名接頭辞定義です。C: 監査面観点の照合先はデータセット割り当て報告で、中心はジョブ名接頭辞観点です。D: 選択面観点の処理段階は出力記述子作成選択で、入力と表示を結ぶ対象はジョブ名接頭辞証跡です。表示面観点の用語定義として、ジョブ名接頭辞とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ名接頭辞状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide PREFIX

    ---

    **問題.** 表示面の所有者絞り込みを表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って所有者 commandを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF option 3.2 Data Set Utility
    - B. ISPF CHANGE
    - C. SDSF OWNER ✅
    - D. SDSF O panel

    正解: **C** ／ 難易度: 中級

    **解説:** 選択面観点の出力確認として所有者絞り込み復旧を読み、答えはCで、照合焦点は所有者絞り込み照合です。端末面観点の所有者絞り込み報告は、ジョブ所有者で表示対象を制限することを満たす入力、画面、応答を同じ証跡で確認する所有者絞り込み報告です。制御面観点で残す所有者絞り込み選択は、所有者 commandをコマンドまたはパネル形式と照合する所有者絞り込み選択です。表示面観点の所有者絞り込み反映は、スプール表示検索機能フィルターの入力要求と戻った表示を結び、運用状態を説明する所有者絞り込み反映です。A: 通信面観点の比較先はData Set Utility照合で、要求対象は所有者絞り込み観点です。B: 監査面観点の照合先は文字列置換報告で、中心は所有者絞り込み証跡です。C: 確認面観点の所有者絞り込み選択は、入力名と画面内の所有者 commandを結ぶ所有者絞り込み根拠です。D: 応答面観点の参照先はOutput Queue反映で、作業記録で追跡する対象は所有者絞り込み状態です。編集面観点の用語定義として、所有者絞り込みとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む所有者絞り込み定義です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide OWNER

    ---

    **問題.** 編集面の列ソートを証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってソート commandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF ARRANGE
    - B. PROFILE PREFIX
    - C. DELETE DATASET
    - D. SDSF SORT ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 保存面観点の列ソート照合は正答Dで、表記上の手掛かりはスプール表示検索機能 ソート報告です。表示面観点の列ソート選択は、表形式パネルの列を基準に並べ替えることを満たす入力、画面、応答を同じ証跡で確認する列ソート選択です。一覧面観点で読む列ソート反映は、ソート commandを資料のコマンド形式やパネル形式と照合する列ソート反映です。編集面観点の列ソート観点は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する列ソート観点です。A: 監査面観点の照合先は列配置変更報告で、中心は列ソート読取です。B: 選択面観点の処理段階はデータセット接頭辞選択で、入力と表示を結ぶ対象は列ソート状態です。C: 応答面観点の参照先はデータセット削除反映で、作業記録で追跡する対象は列ソート定義です。D: 保存面観点の列ソート観点は、入力名と画面内のソート commandを結ぶ列ソート応答です。出力面観点の用語定義として、列ソートとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む列ソート根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide SORT

    ---

    **問題.** 出力面の条件フィルターを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってフィルター commandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF FILTER ✅
    - B. ISPF option 2 EDIT
    - C. ISPF EDIT SUBMIT
    - D. SDSF DA panel

    正解: **A** ／ 難易度: 上級

    **解説:** 選択面観点で読む条件フィルター報告は正答位置Aで、記録する焦点はスプール表示検索機能 フィルター選択です。編集面観点の条件フィルター反映は、列値条件で表示行を絞り込むことを満たす入力、画面、応答を同じ証跡で確認する条件フィルター反映です。制御面観点の条件フィルター観点は、フィルター commandを入力記録と合わせて処理対象を見分ける条件フィルター観点です。出力面観点の条件フィルター証跡は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する条件フィルター証跡です。A: 確認面観点の条件フィルター選択は、入力名と画面内のフィルター commandを結ぶ条件フィルター保守です。B: 応答面観点の参照先は編集選択反映で、作業記録で追跡する対象は条件フィルター根拠です。C: 保存面観点の比較先はJCLサブミット観点で、要求対象は条件フィルター読取です。D: 管理面観点の照合先は実行中利用者表示証跡で、中心は条件フィルター状態です。投入面観点の用語定義として、条件フィルターとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む条件フィルター応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide FILTER

    ---

    **問題.** 投入面の列配置変更を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って列配置 commandを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF FILTER
    - B. SDSF ARRANGE ✅
    - C. PROFILE PREFIX
    - D. DELETE DATASET

    正解: **B** ／ 難易度: 上級

    **解説:** 一覧面観点の資料照合として列配置変更選択を選び、答えはBで、記録焦点は列配置変更反映です。出力面観点の列配置変更観点は、パネル列の順序や幅を調整することを満たす入力、画面、応答を同じ証跡で確認する列配置変更観点です。表示面観点から見る列配置変更証跡は、列配置 commandを応答画面と対応させる列配置変更証跡です。投入面観点の列配置変更読取は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する列配置変更読取です。A: 応答面観点の参照先は条件フィルター反映で、作業記録で追跡する対象は列配置変更応答です。B: 保存面観点の列配置変更観点は、入力名と画面内の列配置 commandを結ぶ列配置変更監査です。C: 管理面観点の照合先はデータセット接頭辞証跡で、中心は列配置変更定義です。D: 制御面観点の処理段階はデータセット削除読取で、入力と表示を結ぶ対象は列配置変更根拠です。検索面観点の用語定義として、列配置変更とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む列配置変更保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide ARRANGE

    ---

    **問題.** 操作面のジョブ取消と出力削除を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってP action characterを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF P purge ✅
    - B. OUTDES
    - C. ISPF option 3.2 Data Set Utility
    - D. PF3 END

    正解: **A** ／ 難易度: 上級

    **解説:** 制御面観点で読むジョブ取消と出力削除証跡は正答位置Aで、記録する焦点はスプール表示検索機能 P purge読取です。通信面観点のジョブ取消と出力削除状態は、ジョブを取り消して出力をパージすることを満たす入力、画面、応答を同じ証跡で確認するジョブ取消と出力削除状態です。出力面観点のジョブ取消と出力削除定義は、P action characterを入力記録と合わせて処理対象を見分けるジョブ取消と出力削除定義です。操作面観点のジョブ取消と出力削除根拠は、スプール表示検索機能ジョブ操作の入力要求と戻った表示を結び、運用状態を説明するジョブ取消と出力削除根拠です。A: 選択面観点のジョブ取消と出力削除読取は、入力名と画面内のP action characterを結ぶジョブ取消と出力削除復旧です。B: 編集面観点の参照先は出力記述子作成状態で、作業記録で追跡する対象はジョブ取消と出力削除引継ぎです。C: 一覧面観点の比較先はData Set Utility定義で、要求対象はジョブ取消と出力削除応答です。D: 端末面観点の照合先は終了キー終了根拠で、中心はジョブ取消と出力削除保守です。確認面観点の用語定義として、ジョブ取消と出力削除とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ取消と出力削除棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide ST action characters

    ---

    **問題.** 確認面のジョブ保留を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってH action characterを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF O panel
    - B. SDSF H hold ✅
    - C. SDSF FILTER
    - D. PROFILE MSGID

    正解: **B** ／ 難易度: 中級

    **解説:** 表示面観点の資料照合としてジョブ保留読取を選び、答えはBで、記録焦点はジョブ保留状態です。操作面観点のジョブ保留定義は、ジョブまたは出力を保留状態へ変更することを満たす入力、画面、応答を同じ証跡で確認するジョブ保留定義です。検索面観点から見るジョブ保留根拠は、H action characterを応答画面と対応させるジョブ保留根拠です。確認面観点のジョブ保留応答は、スプール表示検索機能ジョブ操作の入力要求と戻った表示を結び、運用状態を説明するジョブ保留応答です。A: 編集面観点の参照先はOutput Queue状態で、作業記録で追跡する対象はジョブ保留棚卸です。B: 一覧面観点のジョブ保留定義は、入力名と画面内のH action characterを結ぶジョブ保留照合です。C: 端末面観点の照合先は条件フィルター根拠で、中心はジョブ保留監査です。D: 出力面観点の処理段階はメッセージID表示応答で、入力と表示を結ぶ対象はジョブ保留引継ぎです。監査面観点の用語定義として、ジョブ保留とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ保留復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide DA action characters

    ---

    **問題.** 監査面のREADYプロンプト確認を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってREADY表示と入力待ち状態を確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF H hold
    - B. ALLOCATE DATASET
    - C. READY prompt ✅
    - D. OUTDES

    正解: **C** ／ 難易度: 初級

    **解説:** 出力面観点の出力確認としてREADYプロンプト確認状態を読み、答えはCで、照合焦点はREADYプロンプト確認定義です。確認面観点のREADYプロンプト確認根拠は、TSO/Eコマンド入力可能な状態を識別することを満たす入力、画面、応答を同じ証跡で確認するREADYプロンプト確認根拠です。操作面観点で残すREADYプロンプト確認応答は、READY表示と入力待ち状態をコマンドまたはパネル形式と照合するREADYプロンプト確認応答です。監査面観点のREADYプロンプト確認保守は、TSO/Eセッションの入力要求と戻った表示を結び、運用状態を説明するREADYプロンプト確認保守です。A: 一覧面観点の比較先はジョブ保留定義で、要求対象はREADYプロンプト確認監査です。B: 端末面観点の照合先はデータセット割り当て根拠で、中心はREADYプロンプト確認引継ぎです。C: 制御面観点のREADYプロンプト確認応答は、入力名と画面内のREADY表示と入力待ち状態を結ぶREADYプロンプト確認報告です。D: 通信面観点の参照先は出力記述子作成保守で、作業記録で追跡する対象はREADYプロンプト確認復旧です。保存面観点の用語定義として、READYプロンプト確認とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むREADYプロンプト確認照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide READY

    ---

    **問題.** 保存面のセッション終了を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってREADY配下のログオフ入力を確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF EDIT SAVE
    - B. ISPF SPLIT screen
    - C. SDSF S output data set
    - D. LOGOFF command ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 表示面観点のセッション終了定義は正答Dで、表記上の手掛かりはログオフ command根拠です。監査面観点のセッション終了応答は、TSO/E利用後にログオフして端末セッションを閉じることを満たす入力、画面、応答を同じ証跡で確認するセッション終了応答です。検索面観点で読むセッション終了保守は、READY配下のログオフ入力を資料のコマンド形式やパネル形式と照合するセッション終了保守です。保存面観点のセッション終了監査は、TSO/Eセッションの入力要求と戻った表示を結び、運用状態を説明するセッション終了監査です。A: 端末面観点の照合先は編集保存根拠で、中心はセッション終了棚卸です。B: 出力面観点の処理段階は画面分割応答で、入力と表示を結ぶ対象はセッション終了復旧です。C: 通信面観点の参照先は出力データセット表示保守で、作業記録で追跡する対象はセッション終了照合です。D: 表示面観点のセッション終了監査は、入力名と画面内のREADY配下のログオフ入力を結ぶセッション終了選択です。照合面観点の用語定義として、セッション終了とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むセッション終了報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide LOGOFF

    ---

    **問題.** 選択面のメッセージID表示を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってプロファイル メッセージID表示を確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF option 3.4 DSLIST
    - B. PROFILE MSGID ✅
    - C. ISPF FIND
    - D. SDSF I panel

    正解: **B** ／ 難易度: 中級

    **解説:** 検索面観点の資料照合としてメッセージID表示応答を選び、答えはBで、記録焦点はメッセージID表示保守です。照合面観点のメッセージID表示監査は、TSO/E応答にメッセージIDを表示する設定を確認することを満たす入力、画面、応答を同じ証跡で確認するメッセージID表示監査です。監査面観点から見るメッセージID表示引継ぎは、プロファイル メッセージID表示を応答画面と対応させるメッセージID表示引継ぎです。選択面観点のメッセージID表示棚卸は、TSO/Eプロファイルの入力要求と戻った表示を結び、運用状態を説明するメッセージID表示棚卸です。A: 通信面観点の参照先はデータセット一覧一覧保守で、作業記録で追跡する対象はメッセージID表示選択です。B: 表示面観点のメッセージID表示監査は、入力名と画面内のプロファイル メッセージID表示を結ぶメッセージID表示観点です。C: 投入面観点の照合先は文字列検索引継ぎで、中心はメッセージID表示照合です。D: 操作面観点の処理段階はInput Queue棚卸で、入力と表示を結ぶ対象はメッセージID表示報告です。管理面観点の用語定義として、メッセージID表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むメッセージID表示反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PROFILE MSGID

    ---

    **問題.** 管理面のコマンドヘルプ表示を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってヘルプ member textとprompt modeを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF SORT
    - B. READY prompt
    - C. HELP command ✅
    - D. RENAME DATASET

    正解: **C** ／ 難易度: 初級

    **解説:** 操作面観点の出力確認としてコマンドヘルプ表示保守を読み、答えはCで、照合焦点はコマンドヘルプ表示監査です。選択面観点のコマンドヘルプ表示引継ぎは、コマンドの構文やオペランド説明をヘルプデータから確認することを満たす入力、画面、応答を同じ証跡で確認するコマンドヘルプ表示引継ぎです。照合面観点で残すコマンドヘルプ表示棚卸は、ヘルプ member textとprompt modeをコマンドまたはパネル形式と照合するコマンドヘルプ表示棚卸です。管理面観点のコマンドヘルプ表示復旧は、TSO/Eヘルプの入力要求と戻った表示を結び、運用状態を説明するコマンドヘルプ表示復旧です。A: 表示面観点の比較先は列ソート監査で、要求対象はコマンドヘルプ表示照合です。B: 投入面観点の照合先はREADYプロンプト確認引継ぎで、中心はコマンドヘルプ表示報告です。C: 出力面観点のコマンドヘルプ表示棚卸は、入力名と画面内のヘルプ member textとprompt modeを結ぶコマンドヘルプ表示証跡です。D: 保存面観点の参照先はデータセット改名復旧で、作業記録で追跡する対象はコマンドヘルプ表示反映です。一覧面観点の用語定義として、コマンドヘルプ表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むコマンドヘルプ表示観点です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference HELP

    ---

    **問題.** 一覧面の割り当て一覧を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってDD名と実行中表示TA SET NAMEを確認する場合、最も適切な確認対象はどれですか。

    - A. ISPF option 1 BROWSE
    - B. ISPF EDIT CANCEL
    - C. SDSF ST panel
    - D. LISTALC STATUS ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 検索面観点の割り当て一覧監査は正答Dで、表記上の手掛かりは割り当て一覧 状態パネルATUS引継ぎです。管理面観点の割り当て一覧棚卸は、セッション中に割り当て済みのDD名とデータセットを確認することを満たす入力、画面、応答を同じ証跡で確認する割り当て一覧棚卸です。監査面観点で読む割り当て一覧復旧は、DD名と実行中表示TA SET NAMEを資料のコマンド形式やパネル形式と照合する割り当て一覧復旧です。一覧面観点の割り当て一覧照合は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明する割り当て一覧照合です。A: 投入面観点の照合先は表示選択引継ぎで、中心は割り当て一覧選択です。B: 操作面観点の処理段階は編集取消棚卸で、入力と表示を結ぶ対象は割り当て一覧反映です。C: 保存面観点の参照先はStatus パネル復旧で、作業記録で追跡する対象は割り当て一覧観点です。D: 検索面観点の割り当て一覧照合は、入力名と画面内のDD名と実行中表示TA SET NAMEを結ぶ割り当て一覧読取です。応答面観点の用語定義として、割り当て一覧とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む割り当て一覧証跡です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference LISTALC

    ---

    **問題.** 応答面のメンバー一覧表示を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってMEMBERS operandとmember nameを確認する場合、この状況で優先する項目はどれですか。

    - A. LISTDS MEMBERS ✅
    - B. SDSF OWNER
    - C. SDSF H hold
    - D. FREE DDNAME

    正解: **A** ／ 難易度: 中級

    **解説:** 操作面観点で読むメンバー一覧表示引継ぎは正答位置Aで、記録する焦点はデータセット表示 MEMBERS棚卸です。一覧面観点のメンバー一覧表示復旧は、PDSまたはPDSEのメンバー一覧を確認することを満たす入力、画面、応答を同じ証跡で確認するメンバー一覧表示復旧です。照合面観点のメンバー一覧表示照合は、MEMBERS operandとmember nameを入力記録と合わせて処理対象を見分けるメンバー一覧表示照合です。応答面観点のメンバー一覧表示報告は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するメンバー一覧表示報告です。A: 出力面観点のメンバー一覧表示棚卸は、入力名と画面内のMEMBERS operandとmember nameを結ぶメンバー一覧表示状態です。B: 保存面観点の参照先は所有者絞り込み復旧で、作業記録で追跡する対象はメンバー一覧表示証跡です。C: 検索面観点の比較先はジョブ保留照合で、要求対象はメンバー一覧表示選択です。D: 確認面観点の照合先はDD名解放報告で、中心はメンバー一覧表示反映です。制御面観点の用語定義として、メンバー一覧表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むメンバー一覧表示読取です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference LISTDS

    ---

    **問題.** 制御面のデータセット割り当てを証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って割り当て データセット and DD名を確認する場合、証跡として中心に置く項目はどれですか。

    - A. ISPF Primary Option Menu
    - B. ALLOCATE DATASET ✅
    - C. ISPF EDIT SAVE
    - D. LOG and LIST disposition

    正解: **B** ／ 難易度: 中級

    **解説:** 監査面観点の資料照合としてデータセット割り当て棚卸を選び、答えはBで、記録焦点はデータセット割り当て復旧です。応答面観点のデータセット割り当て照合は、TSO/Eコマンド処理で使うDD名をデータセットへ割り当てることを満たす入力、画面、応答を同じ証跡で確認するデータセット割り当て照合です。管理面観点から見るデータセット割り当て報告は、割り当て データセット and DD名を応答画面と対応させるデータセット割り当て報告です。制御面観点のデータセット割り当て選択は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明するデータセット割り当て選択です。A: 保存面観点の参照先は基本選択メニュー表示復旧で、作業記録で追跡する対象はデータセット割り当て読取です。B: 検索面観点のデータセット割り当て照合は、入力名と画面内の割り当て データセット and DD名を結ぶデータセット割り当て定義です。C: 確認面観点の照合先は編集保存報告で、中心はデータセット割り当て観点です。D: 照合面観点の処理段階はログリスト処理選択で、入力と表示を結ぶ対象はデータセット割り当て証跡です。端末面観点の用語定義として、データセット割り当てとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット割り当て状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference ALLOCATE

    ---

    **問題.** 端末面のDD名解放を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って解放 FILE operandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF I panel
    - B. SDSF SORT
    - C. FREE DDNAME ✅
    - D. LOGOFF command

    正解: **C** ／ 難易度: 中級

    **解説:** 照合面観点の出力確認としてDD名解放復旧を読み、答えはCで、照合焦点はDD名解放照合です。制御面観点のDD名解放報告は、不要になったDD名割り当てをセッションから外すことを満たす入力、画面、応答を同じ証跡で確認するDD名解放報告です。応答面観点で残すDD名解放選択は、解放 FILE operandをコマンドまたはパネル形式と照合するDD名解放選択です。端末面観点のDD名解放反映は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明するDD名解放反映です。A: 検索面観点の比較先はInput Queue照合で、要求対象はDD名解放観点です。B: 確認面観点の照合先は列ソート報告で、中心はDD名解放証跡です。C: 操作面観点のDD名解放選択は、入力名と画面内の解放 FILE operandを結ぶDD名解放根拠です。D: 一覧面観点の参照先はセッション終了反映で、作業記録で追跡する対象はDD名解放状態です。表示面観点の用語定義として、DD名解放とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むDD名解放定義です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference FREE

    ---

    **問題.** 表示面のデータセット改名を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってold データセット name and new データセット nameを確認する場合、どの項目を選ぶべきですか。

    - A. TRANSMIT DATASET
    - B. ISPF option 2 EDIT
    - C. ISPF FIND
    - D. RENAME DATASET ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 監査面観点のデータセット改名照合は正答Dで、表記上の手掛かりは改名 データセット報告です。端末面観点のデータセット改名選択は、既存データセット名を新しい名前へ変更することを満たす入力、画面、応答を同じ証跡で確認するデータセット改名選択です。管理面観点で読むデータセット改名反映は、old データセット name and new データセット nameを資料のコマンド形式やパネル形式と照合するデータセット改名反映です。表示面観点のデータセット改名観点は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するデータセット改名観点です。A: 確認面観点の照合先はデータセット送信報告で、中心はデータセット改名読取です。B: 照合面観点の処理段階は編集選択選択で、入力と表示を結ぶ対象はデータセット改名状態です。C: 一覧面観点の参照先は文字列検索反映で、作業記録で追跡する対象はデータセット改名定義です。D: 監査面観点のデータセット改名観点は、入力名と画面内のold データセット name and new データセット nameを結ぶデータセット改名応答です。編集面観点の用語定義として、データセット改名とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット改名根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference RENAME

    ---

    **問題.** 編集面のデータセット削除を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って削除 command and データセット nameを確認する場合、最も適切な確認対象はどれですか。

    - A. DELETE DATASET ✅
    - B. SDSF I panel
    - C. SDSF SORT
    - D. LOGOFF command

    正解: **A** ／ 難易度: 中級

    **解説:** 照合面観点で読むデータセット削除報告は正答位置Aで、記録する焦点は削除 データセット選択です。表示面観点のデータセット削除反映は、不要なデータセットをTSO/Eコマンドで削除することを満たす入力、画面、応答を同じ証跡で確認するデータセット削除反映です。応答面観点のデータセット削除観点は、削除 command and データセット nameを入力記録と合わせて処理対象を見分けるデータセット削除観点です。編集面観点のデータセット削除証跡は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するデータセット削除証跡です。A: 操作面観点のデータセット削除選択は、入力名と画面内の削除 command and データセット nameを結ぶデータセット削除保守です。B: 一覧面観点の参照先はInput Queue反映で、作業記録で追跡する対象はデータセット削除根拠です。C: 監査面観点の比較先は列ソート観点で、要求対象はデータセット削除読取です。D: 選択面観点の照合先はセッション終了証跡で、中心はデータセット削除状態です。出力面観点の用語定義として、データセット削除とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット削除応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference DELETE

    ---

    **問題.** 出力面の短文メッセージ送信を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って送信 command and target userを確認する場合、この状況で優先する項目はどれですか。

    - A. HELP command
    - B. SEND USER ✅
    - C. LISTBC
    - D. ISPF option 2 EDIT

    正解: **B** ／ 難易度: 初級

    **解説:** 管理面観点の資料照合として短文メッセージ送信選択を選び、答えはBで、記録焦点は短文メッセージ送信反映です。編集面観点の短文メッセージ送信観点は、同一システムの利用者へ短いメッセージを送ることを満たす入力、画面、応答を同じ証跡で確認する短文メッセージ送信観点です。端末面観点から見る短文メッセージ送信証跡は、送信 command and target userを応答画面と対応させる短文メッセージ送信証跡です。出力面観点の短文メッセージ送信読取は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明する短文メッセージ送信読取です。A: 一覧面観点の参照先はコマンドヘルプ表示反映で、作業記録で追跡する対象は短文メッセージ送信応答です。B: 監査面観点の短文メッセージ送信観点は、入力名と画面内の送信 command and target userを結ぶ短文メッセージ送信監査です。C: 選択面観点の照合先はブロードキャスト表示証跡で、中心は短文メッセージ送信定義です。D: 応答面観点の処理段階は編集選択読取で、入力と表示を結ぶ対象は短文メッセージ送信根拠です。投入面観点の用語定義として、短文メッセージ送信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む短文メッセージ送信保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide SEND

    ---

    **問題.** 投入面のブロードキャスト表示を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってbroadcast データセット messagesを確認する場合、証跡として中心に置く項目はどれですか。

    - A. ISPF EDIT SAVE
    - B. ISPF SPLIT screen
    - C. LISTBC ✅
    - D. SDSF S output data set

    正解: **C** ／ 難易度: 初級

    **解説:** 応答面観点の出力確認としてブロードキャスト表示反映を読み、答えはCで、照合焦点はブロードキャスト表示観点です。出力面観点のブロードキャスト表示証跡は、システムや他利用者からのメッセージを確認することを満たす入力、画面、応答を同じ証跡で確認するブロードキャスト表示証跡です。編集面観点で残すブロードキャスト表示読取は、broadcast データセット messagesをコマンドまたはパネル形式と照合するブロードキャスト表示読取です。投入面観点のブロードキャスト表示状態は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明するブロードキャスト表示状態です。A: 監査面観点の比較先は編集保存観点で、要求対象はブロードキャスト表示定義です。B: 選択面観点の照合先は画面分割証跡で、中心はブロードキャスト表示根拠です。C: 照合面観点のブロードキャスト表示読取は、入力名と画面内のbroadcast データセット messagesを結ぶブロードキャスト表示引継ぎです。D: 表示面観点の参照先は出力データセット表示状態で、作業記録で追跡する対象はブロードキャスト表示保守です。検索面観点の用語定義として、ブロードキャスト表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むブロードキャスト表示監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide LISTBC

    ---

    **問題.** 検索面のデータセット送信を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って転送送信 target and データセット operandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. FREE DDNAME
    - B. PRINTDS
    - C. ISPF option 6 Command
    - D. TRANSMIT DATASET ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 管理面観点のデータセット送信観点は正答Dで、表記上の手掛かりは転送送信 データセット証跡です。投入面観点のデータセット送信読取は、別ユーザーまたは別ノードへデータセットを送信することを満たす入力、画面、応答を同じ証跡で確認するデータセット送信読取です。端末面観点で読むデータセット送信状態は、転送送信 target and データセット operandを資料のコマンド形式やパネル形式と照合するデータセット送信状態です。検索面観点のデータセット送信定義は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明するデータセット送信定義です。A: 選択面観点の照合先はDD名解放証跡で、中心はデータセット送信応答です。B: 応答面観点の処理段階はデータセット印刷読取で、入力と表示を結ぶ対象はデータセット送信保守です。C: 表示面観点の参照先はTSO Command Processor状態で、作業記録で追跡する対象はデータセット送信監査です。D: 管理面観点のデータセット送信定義は、入力名と画面内の転送送信 target and データセット operandを結ぶデータセット送信棚卸です。通信面観点の用語定義として、データセット送信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット送信引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference TRANSMIT

    ---

    **問題.** 通信面の送信データ受信を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って転送受信 prompt and データセット nameを確認する場合、どの項目を選ぶべきですか。

    - A. RECEIVE DATASET ✅
    - B. PF1 HELP
    - C. SDSF H panel
    - D. SDSF ULOG

    正解: **A** ／ 難易度: 中級

    **解説:** 応答面観点で読む送信データ受信証跡は正答位置Aで、記録する焦点は転送受信 データセット読取です。検索面観点の送信データ受信状態は、転送送信されたデータセットや長文メッセージを受信することを満たす入力、画面、応答を同じ証跡で確認する送信データ受信状態です。編集面観点の送信データ受信定義は、転送受信 prompt and データセット nameを入力記録と合わせて処理対象を見分ける送信データ受信定義です。通信面観点の送信データ受信根拠は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明する送信データ受信根拠です。A: 照合面観点の送信データ受信読取は、入力名と画面内の転送受信 prompt and データセット nameを結ぶ送信データ受信復旧です。B: 表示面観点の参照先はヘルプキー表示状態で、作業記録で追跡する対象は送信データ受信引継ぎです。C: 管理面観点の比較先はHeld Output Queue定義で、要求対象は送信データ受信応答です。D: 制御面観点の照合先はユーザーセッションログ根拠で、中心は送信データ受信保守です。操作面観点の用語定義として、送信データ受信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む送信データ受信棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference RECEIVE

    ---

    **問題.** 操作面の出力記述子作成を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って出力記述子 operand and destinationを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF ARRANGE
    - B. OUTDES ✅
    - C. PROFILE PREFIX
    - D. DELETE DATASET

    正解: **B** ／ 難易度: 上級

    **解説:** 端末面観点の資料照合として出力記述子作成読取を選び、答えはBで、記録焦点は出力記述子作成状態です。通信面観点の出力記述子作成定義は、印刷や出力処理の宛先属性を定義することを満たす入力、画面、応答を同じ証跡で確認する出力記述子作成定義です。投入面観点から見る出力記述子作成根拠は、出力記述子 operand and destinationを応答画面と対応させる出力記述子作成根拠です。操作面観点の出力記述子作成応答は、TSO/E出力の入力要求と戻った表示を結び、運用状態を説明する出力記述子作成応答です。A: 表示面観点の参照先は列配置変更状態で、作業記録で追跡する対象は出力記述子作成棚卸です。B: 管理面観点の出力記述子作成定義は、入力名と画面内の出力記述子 operand and destinationを結ぶ出力記述子作成照合です。C: 制御面観点の照合先はデータセット接頭辞根拠で、中心は出力記述子作成監査です。D: 編集面観点の処理段階はデータセット削除応答で、入力と表示を結ぶ対象は出力記述子作成引継ぎです。確認面観点の用語定義として、出力記述子作成とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む出力記述子作成復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference OUTDES

    ---

    **問題.** 確認面のデータセット印刷を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って印刷 データセット operandを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF option 2 EDIT
    - B. ISPF EDIT SUBMIT
    - C. PRINTDS ✅
    - D. SDSF DA panel

    正解: **C** ／ 難易度: 中級

    **解説:** 編集面観点の出力確認としてデータセット印刷状態を読み、答えはCで、照合焦点はデータセット印刷定義です。操作面観点のデータセット印刷根拠は、データセット内容を印刷または出力キューへ送ることを満たす入力、画面、応答を同じ証跡で確認するデータセット印刷根拠です。通信面観点で残すデータセット印刷応答は、印刷 データセット operandをコマンドまたはパネル形式と照合するデータセット印刷応答です。確認面観点のデータセット印刷保守は、TSO/E出力の入力要求と戻った表示を結び、運用状態を説明するデータセット印刷保守です。A: 管理面観点の比較先は編集選択定義で、要求対象はデータセット印刷監査です。B: 制御面観点の照合先はJCLサブミット根拠で、中心はデータセット印刷引継ぎです。C: 応答面観点のデータセット印刷応答は、入力名と画面内の印刷 データセット operandを結ぶデータセット印刷報告です。D: 検索面観点の参照先は実行中利用者表示保守で、作業記録で追跡する対象はデータセット印刷復旧です。監査面観点の用語定義として、データセット印刷とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット印刷照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PRINTDS

    ---

    **問題.** 保存面の基本選択メニュー表示を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってOPTION line and menu entriesを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF Primary Option Menu ✅
    - B. SDSF ST panel
    - C. SDSF PREFIX
    - D. SDSF H hold

    正解: **A** ／ 難易度: 初級

    **解説:** 編集面観点で読む基本選択メニュー表示根拠は正答位置Aで、記録する焦点は対話式生産性機能 基本選択メニュー応答です。監査面観点の基本選択メニュー表示保守は、対話式生産性機能/PDFの主要機能を選択する入口を確認することを満たす入力、画面、応答を同じ証跡で確認する基本選択メニュー表示保守です。通信面観点の基本選択メニュー表示監査は、OPTION line and menu entriesを入力記録と合わせて処理対象を見分ける基本選択メニュー表示監査です。保存面観点の基本選択メニュー表示引継ぎは、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する基本選択メニュー表示引継ぎです。A: 応答面観点の基本選択メニュー表示応答は、入力名と画面内のOPTION line and menu entriesを結ぶ基本選択メニュー表示反映です。B: 検索面観点の参照先はStatus パネル保守で、作業記録で追跡する対象は基本選択メニュー表示報告です。C: 端末面観点の比較先はジョブ名接頭辞監査で、要求対象は基本選択メニュー表示棚卸です。D: 出力面観点の照合先はジョブ保留引継ぎで、中心は基本選択メニュー表示復旧です。照合面観点の用語定義として、基本選択メニュー表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む基本選択メニュー表示選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide Primary Option Menu

    ---

    **問題.** 照合面の表示選択を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って表示 option and データセット nameを確認する場合、どの項目を選ぶべきですか。

    - A. PROFILE MSGID
    - B. ISPF option 1 BROWSE ✅
    - C. DELETE DATASET
    - D. ISPF Primary Option Menu

    正解: **B** ／ 難易度: 初級

    **解説:** 投入面観点の資料照合として表示選択応答を選び、答えはBで、記録焦点は表示選択保守です。保存面観点の表示選択監査は、データセットを更新せず表示することを満たす入力、画面、応答を同じ証跡で確認する表示選択監査です。確認面観点から見る表示選択引継ぎは、表示 option and データセット nameを応答画面と対応させる表示選択引継ぎです。照合面観点の表示選択棚卸は、対話式生産性機能表示の入力要求と戻った表示を結び、運用状態を説明する表示選択棚卸です。A: 検索面観点の参照先はメッセージID表示保守で、作業記録で追跡する対象は表示選択選択です。B: 端末面観点の表示選択監査は、入力名と画面内の表示 option and データセット nameを結ぶ表示選択観点です。C: 出力面観点の照合先はデータセット削除引継ぎで、中心は表示選択照合です。D: 通信面観点の処理段階は基本選択メニュー表示棚卸で、入力と表示を結ぶ対象は表示選択報告です。選択面観点の用語定義として、表示選択とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む表示選択反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide BROWSE

    ---

    **問題.** 選択面の編集選択を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って編集 option and edit パネルを確認する場合、最も適切な確認対象はどれですか。

    - A. ISPF EDIT SAVE
    - B. ISPF SPLIT screen
    - C. ISPF option 2 EDIT ✅
    - D. SDSF S output data set

    正解: **C** ／ 難易度: 初級

    **解説:** 通信面観点の出力確認として編集選択保守を読み、答えはCで、照合焦点は編集選択監査です。照合面観点の編集選択引継ぎは、ソースやJCLメンバーを編集することを満たす入力、画面、応答を同じ証跡で確認する編集選択引継ぎです。保存面観点で残す編集選択棚卸は、編集 option and edit パネルをコマンドまたはパネル形式と照合する編集選択棚卸です。選択面観点の編集選択復旧は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集選択復旧です。A: 端末面観点の比較先は編集保存監査で、要求対象は編集選択照合です。B: 出力面観点の照合先は画面分割引継ぎで、中心は編集選択報告です。C: 編集面観点の編集選択棚卸は、入力名と画面内の編集 option and edit パネルを結ぶ編集選択証跡です。D: 監査面観点の参照先は出力データセット表示復旧で、作業記録で追跡する対象は編集選択反映です。管理面観点の用語定義として、編集選択とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集選択観点です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide EDIT

    ---

    **問題.** 応答面のMOVE/COPYを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってMove/Copy utility パネルを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. PROFILE PREFIX
    - B. ISPF option 3.3 Move Copy ✅
    - C. RENAME DATASET
    - D. CALL command

    正解: **B** ／ 難易度: 中級

    **解説:** 確認面観点の資料照合としてMOVE/COPY棚卸を選び、答えはBで、記録焦点はMOVE/COPY復旧です。一覧面観点のMOVE/COPY照合は、データセットやメンバーを移動またはコピーすることを満たす入力、画面、応答を同じ証跡で確認するMOVE/COPY照合です。選択面観点から見るMOVE/COPY報告は、Move/Copy utility パネルを応答画面と対応させるMOVE/COPY報告です。応答面観点のMOVE/COPY選択は、対話式生産性機能ユーティリティの入力要求と戻った表示を結び、運用状態を説明するMOVE/COPY選択です。A: 監査面観点の参照先はデータセット接頭辞復旧で、作業記録で追跡する対象はMOVE/COPY読取です。B: 投入面観点のMOVE/COPY照合は、入力名と画面内のMove/Copy utility パネルを結ぶMOVE/COPY定義です。C: 操作面観点の照合先はデータセット改名報告で、中心はMOVE/COPY観点です。D: 保存面観点の処理段階はロードモジュール呼出選択で、入力と表示を結ぶ対象はMOVE/COPY証跡です。制御面観点の用語定義として、MOVE/COPYとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むMOVE/COPY状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide Move Copy

    ---

    **問題.** 端末面の編集保存を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って保存 primary commandを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF H panel
    - B. SDSF ARRANGE
    - C. PROFILE MSGID
    - D. ISPF EDIT SAVE ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 確認面観点の編集保存照合は正答Dで、表記上の手掛かりは対話式生産性機能 編集 保存報告です。制御面観点の編集保存選択は、編集したメンバーを保存してセッションを継続または終了することを満たす入力、画面、応答を同じ証跡で確認する編集保存選択です。選択面観点で読む編集保存反映は、保存 primary commandを資料のコマンド形式やパネル形式と照合する編集保存反映です。端末面観点の編集保存観点は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集保存観点です。A: 操作面観点の照合先はHeld Output Queue報告で、中心は編集保存読取です。B: 保存面観点の処理段階は列配置変更選択で、入力と表示を結ぶ対象は編集保存状態です。C: 管理面観点の参照先はメッセージID表示反映で、作業記録で追跡する対象は編集保存定義です。D: 確認面観点の編集保存観点は、入力名と画面内の保存 primary commandを結ぶ編集保存応答です。表示面観点の用語定義として、編集保存とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集保存根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide editor SAVE

    ---

    **問題.** 表示面の編集取消を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って取消 primary commandを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF EDIT CANCEL ✅
    - B. TRANSMIT DATASET
    - C. ISPF option 2 EDIT
    - D. ISPF CHANGE

    正解: **A** ／ 難易度: 中級

    **解説:** 保存面観点で読む編集取消報告は正答位置Aで、記録する焦点は対話式生産性機能 編集 取消選択です。端末面観点の編集取消反映は、保存せず編集内容を破棄して終了することを満たす入力、画面、応答を同じ証跡で確認する編集取消反映です。一覧面観点の編集取消観点は、取消 primary commandを入力記録と合わせて処理対象を見分ける編集取消観点です。表示面観点の編集取消証跡は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集取消証跡です。A: 通信面観点の編集取消選択は、入力名と画面内の取消 primary commandを結ぶ編集取消保守です。B: 管理面観点の参照先はデータセット送信反映で、作業記録で追跡する対象は編集取消根拠です。C: 確認面観点の比較先は編集選択観点で、要求対象は編集取消読取です。D: 照合面観点の照合先は文字列置換証跡で、中心は編集取消状態です。編集面観点の用語定義として、編集取消とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集取消応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide editor CANCEL

    ---

    **問題.** 編集面のJCLサブミットを証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って投入 primary command and JOB statementを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF O panel
    - B. ISPF EDIT SUBMIT ✅
    - C. SDSF FILTER
    - D. PROFILE PREFIX

    正解: **B** ／ 難易度: 中級

    **解説:** 選択面観点の資料照合としてJCLサブミット選択を選び、答えはBで、記録焦点はJCLサブミット反映です。表示面観点のJCLサブミット観点は、編集画面からJCLをJESへ投入することを満たす入力、画面、応答を同じ証跡で確認するJCLサブミット観点です。制御面観点から見るJCLサブミット証跡は、投入 primary command and JOB statementを応答画面と対応させるJCLサブミット証跡です。編集面観点のJCLサブミット読取は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明するJCLサブミット読取です。A: 管理面観点の参照先はOutput Queue反映で、作業記録で追跡する対象はJCLサブミット応答です。B: 確認面観点のJCLサブミット観点は、入力名と画面内の投入 primary command and JOB statementを結ぶJCLサブミット監査です。C: 照合面観点の照合先は条件フィルター証跡で、中心はJCLサブミット定義です。D: 一覧面観点の処理段階はデータセット接頭辞読取で、入力と表示を結ぶ対象はJCLサブミット根拠です。出力面観点の用語定義として、JCLサブミットとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むJCLサブミット保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide SUBMIT

    ---

    **問題.** 出力面の文字列検索を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って検索 primary commandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. PROFILE MSGID
    - B. DELETE DATASET
    - C. ISPF FIND ✅
    - D. ISPF Primary Option Menu

    正解: **C** ／ 難易度: 初級

    **解説:** 一覧面観点の出力確認として文字列検索反映を読み、答えはCで、照合焦点は文字列検索観点です。編集面観点の文字列検索証跡は、編集または表示中のデータから文字列を探すことを満たす入力、画面、応答を同じ証跡で確認する文字列検索証跡です。表示面観点で残す文字列検索読取は、検索 primary commandをコマンドまたはパネル形式と照合する文字列検索読取です。出力面観点の文字列検索状態は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する文字列検索状態です。A: 確認面観点の比較先はメッセージID表示観点で、要求対象は文字列検索定義です。B: 照合面観点の照合先はデータセット削除証跡で、中心は文字列検索根拠です。C: 保存面観点の文字列検索読取は、入力名と画面内の検索 primary commandを結ぶ文字列検索引継ぎです。D: 端末面観点の参照先は基本選択メニュー表示状態で、作業記録で追跡する対象は文字列検索保守です。投入面観点の用語定義として、文字列検索とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む文字列検索監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide FIND

    ---

    **問題.** 投入面の文字列置換を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って置換 primary commandを確認する場合、どの項目を選ぶべきですか。

    - A. ISPF FIND
    - B. SDSF I panel
    - C. SDSF FILTER
    - D. ISPF CHANGE ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 選択面観点の文字列置換観点は正答Dで、表記上の手掛かりは対話式生産性機能 置換証跡です。出力面観点の文字列置換読取は、編集データ内の文字列を別の値へ置き換えることを満たす入力、画面、応答を同じ証跡で確認する文字列置換読取です。制御面観点で読む文字列置換状態は、置換 primary commandを資料のコマンド形式やパネル形式と照合する文字列置換状態です。投入面観点の文字列置換定義は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する文字列置換定義です。A: 照合面観点の照合先は文字列検索証跡で、中心は文字列置換応答です。B: 一覧面観点の処理段階はInput Queue読取で、入力と表示を結ぶ対象は文字列置換保守です。C: 端末面観点の参照先は条件フィルター状態で、作業記録で追跡する対象は文字列置換監査です。D: 選択面観点の文字列置換定義は、入力名と画面内の置換 primary commandを結ぶ文字列置換棚卸です。検索面観点の用語定義として、文字列置換とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む文字列置換引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide CHANGE

    ---

    **問題.** 検索面の終了キー終了を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って終了キー 終了 keyを確認する場合、最も適切な確認対象はどれですか。

    - A. PF3 END ✅
    - B. SDSF P purge
    - C. LISTALC STATUS
    - D. TRANSMIT DATASET

    正解: **A** ／ 難易度: 初級

    **解説:** 一覧面観点で読む終了キー終了証跡は正答位置Aで、記録する焦点は終了キー 終了読取です。投入面観点の終了キー終了状態は、現在のパネルから前画面へ戻ることを満たす入力、画面、応答を同じ証跡で確認する終了キー終了状態です。表示面観点の終了キー終了定義は、終了キー 終了 keyを入力記録と合わせて処理対象を見分ける終了キー終了定義です。検索面観点の終了キー終了根拠は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する終了キー終了根拠です。A: 保存面観点の終了キー終了読取は、入力名と画面内の終了キー 終了 keyを結ぶ終了キー終了復旧です。B: 端末面観点の参照先はジョブ取消と出力削除状態で、作業記録で追跡する対象は終了キー終了引継ぎです。C: 選択面観点の比較先は割り当て一覧定義で、要求対象は終了キー終了応答です。D: 応答面観点の照合先はデータセット送信根拠で、中心は終了キー終了保守です。通信面観点の用語定義として、終了キー終了とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む終了キー終了棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide END PF key

    ---

    **問題.** 通信面のヘルプキー表示を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってヘルプキー ヘルプ keyを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF option 3.2 Data Set Utility
    - B. PF1 HELP ✅
    - C. ISPF CHANGE
    - D. SDSF H panel

    正解: **B** ／ 難易度: 初級

    **解説:** 制御面観点の資料照合としてヘルプキー表示読取を選び、答えはBで、記録焦点はヘルプキー表示状態です。検索面観点のヘルプキー表示定義は、現在パネルに対応するチュートリアルやヘルプを表示することを満たす入力、画面、応答を同じ証跡で確認するヘルプキー表示定義です。出力面観点から見るヘルプキー表示根拠は、ヘルプキー ヘルプ keyを応答画面と対応させるヘルプキー表示根拠です。通信面観点のヘルプキー表示応答は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明するヘルプキー表示応答です。A: 端末面観点の参照先はData Set Utility状態で、作業記録で追跡する対象はヘルプキー表示棚卸です。B: 選択面観点のヘルプキー表示定義は、入力名と画面内のヘルプキー ヘルプ keyを結ぶヘルプキー表示照合です。C: 応答面観点の照合先は文字列置換根拠で、中心はヘルプキー表示監査です。D: 表示面観点の処理段階はHeld Output Queue応答で、入力と表示を結ぶ対象はヘルプキー表示引継ぎです。操作面観点の用語定義として、ヘルプキー表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むヘルプキー表示復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide HELP PF key

    ---

    **問題.** 操作面の画面分割を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って画面分割 and SWAP behaviorを確認する場合、証跡として中心に置く項目はどれですか。

    - A. LISTALC STATUS
    - B. LISTBC
    - C. ISPF SPLIT screen ✅
    - D. ISPF option 2 EDIT

    正解: **C** ／ 難易度: 上級

    **解説:** 表示面観点の出力確認として画面分割状態を読み、答えはCで、照合焦点は画面分割定義です。通信面観点の画面分割根拠は、複数論理画面を切り替えて作業することを満たす入力、画面、応答を同じ証跡で確認する画面分割根拠です。検索面観点で残す画面分割応答は、画面分割 and SWAP behaviorをコマンドまたはパネル形式と照合する画面分割応答です。操作面観点の画面分割保守は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する画面分割保守です。A: 選択面観点の比較先は割り当て一覧定義で、要求対象は画面分割監査です。B: 応答面観点の照合先はブロードキャスト表示根拠で、中心は画面分割引継ぎです。C: 一覧面観点の画面分割応答は、入力名と画面内の画面分割 and SWAP behaviorを結ぶ画面分割報告です。D: 投入面観点の参照先は編集選択保守で、作業記録で追跡する対象は画面分割復旧です。確認面観点の用語定義として、画面分割とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む画面分割照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide split screen

    ---

    **問題.** 確認面のログリスト処理を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってログ and リスト disposition パネルを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF I panel
    - B. SDSF SORT
    - C. LOGOFF command
    - D. LOG and LIST disposition ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 制御面観点のログリスト処理定義は正答Dで、表記上の手掛かりはログ and リスト disposition根拠です。操作面観点のログリスト処理応答は、対話式生産性機能終了時のログ/リスト出力を印刷または削除することを満たす入力、画面、応答を同じ証跡で確認するログリスト処理応答です。出力面観点で読むログリスト処理保守は、ログ and リスト disposition パネルを資料のコマンド形式やパネル形式と照合するログリスト処理保守です。確認面観点のログリスト処理監査は、対話式生産性機能終了の入力要求と戻った表示を結び、運用状態を説明するログリスト処理監査です。A: 応答面観点の照合先はInput Queue根拠で、中心はログリスト処理棚卸です。B: 表示面観点の処理段階は列ソート応答で、入力と表示を結ぶ対象はログリスト処理復旧です。C: 投入面観点の参照先はセッション終了保守で、作業記録で追跡する対象はログリスト処理照合です。D: 制御面観点のログリスト処理監査は、入力名と画面内のログ and リスト disposition パネルを結ぶログリスト処理選択です。監査面観点の用語定義として、ログリスト処理とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むログリスト処理報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide LOG LIST disposition

    ---

    **問題.** 保存面の実行中利用者表示を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って実行中表示 パネル and 実行中アドレス空間を確認する場合、最も適切な確認対象はどれですか。

    - A. ISPF option 3.4 DSLIST
    - B. SDSF DA panel ✅
    - C. ISPF FIND
    - D. SDSF O panel

    正解: **B** ／ 難易度: 中級

    **解説:** 出力面観点の資料照合として実行中利用者表示応答を選び、答えはBで、記録焦点は実行中利用者表示保守です。監査面観点の実行中利用者表示監査は、実行中アドレス空間やジョブの状態を確認することを満たす入力、画面、応答を同じ証跡で確認する実行中利用者表示監査です。操作面観点から見る実行中利用者表示引継ぎは、実行中表示 パネル and 実行中アドレス空間を応答画面と対応させる実行中利用者表示引継ぎです。保存面観点の実行中利用者表示棚卸は、スプール表示検索機能ジョブ管理の入力要求と戻った表示を結び、運用状態を説明する実行中利用者表示棚卸です。A: 投入面観点の参照先はデータセット一覧一覧保守で、作業記録で追跡する対象は実行中利用者表示選択です。B: 制御面観点の実行中利用者表示監査は、入力名と画面内の実行中表示 パネル and 実行中アドレス空間を結ぶ実行中利用者表示観点です。C: 編集面観点の照合先は文字列検索引継ぎで、中心は実行中利用者表示照合です。D: 検索面観点の処理段階はOutput Queue棚卸で、入力と表示を結ぶ対象は実行中利用者表示報告です。照合面観点の用語定義として、実行中利用者表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む実行中利用者表示反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide DA panel

    ---

    **問題.** 照合面のInput Queueを表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってI パネル job queueを確認する場合、この状況で優先する項目はどれですか。

    - A. SDSF FILTER
    - B. LOGOFF command
    - C. SDSF I panel ✅
    - D. RENAME DATASET

    正解: **C** ／ 難易度: 中級

    **解説:** 検索面観点の出力確認としてInput Queue保守を読み、答えはCで、照合焦点はInput Queue監査です。保存面観点のInput Queue引継ぎは、入力キュー上または実行中ジョブを確認することを満たす入力、画面、応答を同じ証跡で確認するInput Queue引継ぎです。監査面観点で残すInput Queue棚卸は、I パネル job queueをコマンドまたはパネル形式と照合するInput Queue棚卸です。照合面観点のInput Queue復旧は、スプール表示検索機能キューの入力要求と戻った表示を結び、運用状態を説明するInput Queue復旧です。A: 制御面観点の比較先は条件フィルター監査で、要求対象はInput Queue照合です。B: 編集面観点の照合先はセッション終了引継ぎで、中心はInput Queue報告です。C: 表示面観点のInput Queue棚卸は、入力名と画面内のI パネル job queueを結ぶInput Queue証跡です。D: 確認面観点の参照先はデータセット改名復旧で、作業記録で追跡する対象はInput Queue反映です。選択面観点の用語定義として、Input Queueとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むInput Queue観点です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide Input Queue

    ---

    **問題.** 応答面の出力データセット表示を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってS 行操作 and 出力表示を確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF P purge
    - B. LISTALC STATUS
    - C. SDSF S output data set ✅
    - D. TRANSMIT DATASET

    正解: **C** ／ 難易度: 初級

    **解説:** 監査面観点の出力確認として出力データセット表示復旧を読み、答えはCで、照合焦点は出力データセット表示照合です。一覧面観点の出力データセット表示報告は、ジョブデータセット表示パネル上で個別出力データセットを表示することを満たす入力、画面、応答を同じ証跡で確認する出力データセット表示報告です。管理面観点で残す出力データセット表示選択は、S 行操作 and 出力表示をコマンドまたはパネル形式と照合する出力データセット表示選択です。応答面観点の出力データセット表示反映は、スプール表示検索機能出力参照の入力要求と戻った表示を結び、運用状態を説明する出力データセット表示反映です。A: 出力面観点の比較先はジョブ取消と出力削除照合で、要求対象は出力データセット表示観点です。B: 通信面観点の照合先は割り当て一覧報告で、中心は出力データセット表示証跡です。C: 検索面観点の出力データセット表示選択は、入力名と画面内のS 行操作 and 出力表示を結ぶ出力データセット表示根拠です。D: 選択面観点の参照先はデータセット送信反映で、作業記録で追跡する対象は出力データセット表示状態です。制御面観点の用語定義として、出力データセット表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む出力データセット表示定義です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide output browse

    ---

    **問題.** 制御面のジョブ名接頭辞を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って接頭辞 commandを確認する場合、この状況で優先する項目はどれですか。

    - A. DELETE DATASET
    - B. CALL command
    - C. ISPF EDIT SAVE
    - D. SDSF PREFIX ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 操作面観点のジョブ名接頭辞照合は正答Dで、表記上の手掛かりはスプール表示検索機能 接頭辞報告です。応答面観点のジョブ名接頭辞選択は、表示対象ジョブ名を接頭辞で絞り込むことを満たす入力、画面、応答を同じ証跡で確認するジョブ名接頭辞選択です。照合面観点で読むジョブ名接頭辞反映は、接頭辞 commandを資料のコマンド形式やパネル形式と照合するジョブ名接頭辞反映です。制御面観点のジョブ名接頭辞観点は、スプール表示検索機能フィルターの入力要求と戻った表示を結び、運用状態を説明するジョブ名接頭辞観点です。A: 通信面観点の照合先はデータセット削除報告で、中心はジョブ名接頭辞読取です。B: 監査面観点の処理段階はロードモジュール呼出選択で、入力と表示を結ぶ対象はジョブ名接頭辞状態です。C: 選択面観点の参照先は編集保存反映で、作業記録で追跡する対象はジョブ名接頭辞定義です。D: 操作面観点のジョブ名接頭辞観点は、入力名と画面内の接頭辞 commandを結ぶジョブ名接頭辞応答です。端末面観点の用語定義として、ジョブ名接頭辞とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ名接頭辞根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide PREFIX

    ---

    **問題.** 端末面の所有者絞り込みを証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って所有者 commandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF OWNER ✅
    - B. ISPF SPLIT screen
    - C. SDSF ? JDS
    - D. SDSF P purge

    正解: **A** ／ 難易度: 中級

    **解説:** 監査面観点で読む所有者絞り込み報告は正答位置Aで、記録する焦点はスプール表示検索機能 所有者選択です。制御面観点の所有者絞り込み反映は、ジョブ所有者で表示対象を制限することを満たす入力、画面、応答を同じ証跡で確認する所有者絞り込み反映です。管理面観点の所有者絞り込み観点は、所有者 commandを入力記録と合わせて処理対象を見分ける所有者絞り込み観点です。端末面観点の所有者絞り込み証跡は、スプール表示検索機能フィルターの入力要求と戻った表示を結び、運用状態を説明する所有者絞り込み証跡です。A: 検索面観点の所有者絞り込み選択は、入力名と画面内の所有者 commandを結ぶ所有者絞り込み保守です。B: 選択面観点の参照先は画面分割反映で、作業記録で追跡する対象は所有者絞り込み根拠です。C: 操作面観点の比較先はJob Data Set表示観点で、要求対象は所有者絞り込み読取です。D: 保存面観点の照合先はジョブ取消と出力削除証跡で、中心は所有者絞り込み状態です。表示面観点の用語定義として、所有者絞り込みとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む所有者絞り込み応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide OWNER

    ---

    **問題.** 表示面の列ソートを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってソート commandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. LISTALC STATUS
    - B. SDSF SORT ✅
    - C. LISTBC
    - D. ISPF option 2 EDIT

    正解: **B** ／ 難易度: 中級

    **解説:** 照合面観点の資料照合として列ソート選択を選び、答えはBで、記録焦点は列ソート反映です。端末面観点の列ソート観点は、表形式パネルの列を基準に並べ替えることを満たす入力、画面、応答を同じ証跡で確認する列ソート観点です。応答面観点から見る列ソート証跡は、ソート commandを応答画面と対応させる列ソート証跡です。表示面観点の列ソート読取は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する列ソート読取です。A: 選択面観点の参照先は割り当て一覧反映で、作業記録で追跡する対象は列ソート応答です。B: 操作面観点の列ソート観点は、入力名と画面内のソート commandを結ぶ列ソート監査です。C: 保存面観点の照合先はブロードキャスト表示証跡で、中心は列ソート定義です。D: 管理面観点の処理段階は編集選択読取で、入力と表示を結ぶ対象は列ソート根拠です。編集面観点の用語定義として、列ソートとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む列ソート保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide SORT

    ---

    **問題.** 編集面の条件フィルターを定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってフィルター commandを確認する場合、どの項目を選ぶべきですか。

    - A. PF3 END
    - B. SDSF O panel
    - C. SDSF FILTER ✅
    - D. SDSF ULOG

    正解: **C** ／ 難易度: 上級

    **解説:** 管理面観点の出力確認として条件フィルター反映を読み、答えはCで、照合焦点は条件フィルター観点です。表示面観点の条件フィルター証跡は、列値条件で表示行を絞り込むことを満たす入力、画面、応答を同じ証跡で確認する条件フィルター証跡です。端末面観点で残す条件フィルター読取は、フィルター commandをコマンドまたはパネル形式と照合する条件フィルター読取です。編集面観点の条件フィルター状態は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する条件フィルター状態です。A: 操作面観点の比較先は終了キー終了観点で、要求対象は条件フィルター定義です。B: 保存面観点の照合先はOutput Queue証跡で、中心は条件フィルター根拠です。C: 監査面観点の条件フィルター読取は、入力名と画面内のフィルター commandを結ぶ条件フィルター引継ぎです。D: 制御面観点の参照先はユーザーセッションログ状態で、作業記録で追跡する対象は条件フィルター保守です。出力面観点の用語定義として、条件フィルターとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む条件フィルター監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide FILTER

    ---

    **問題.** 出力面の列配置変更を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って列配置 commandを確認する場合、最も適切な確認対象はどれですか。

    - A. LISTALC STATUS
    - B. LISTBC
    - C. ISPF option 2 EDIT
    - D. SDSF ARRANGE ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 照合面観点の列配置変更観点は正答Dで、表記上の手掛かりはスプール表示検索機能 列配置証跡です。編集面観点の列配置変更読取は、パネル列の順序や幅を調整することを満たす入力、画面、応答を同じ証跡で確認する列配置変更読取です。応答面観点で読む列配置変更状態は、列配置 commandを資料のコマンド形式やパネル形式と照合する列配置変更状態です。出力面観点の列配置変更定義は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する列配置変更定義です。A: 保存面観点の照合先は割り当て一覧証跡で、中心は列配置変更応答です。B: 管理面観点の処理段階はブロードキャスト表示読取で、入力と表示を結ぶ対象は列配置変更保守です。C: 制御面観点の参照先は編集選択状態で、作業記録で追跡する対象は列配置変更監査です。D: 照合面観点の列配置変更定義は、入力名と画面内の列配置 commandを結ぶ列配置変更棚卸です。投入面観点の用語定義として、列配置変更とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む列配置変更引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide ARRANGE

    ---

    **問題.** 検索面のMVSコマンド発行を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってslash command and Uログ responseを確認する場合、証跡として中心に置く項目はどれですか。

    - A. LISTBC
    - B. SDSF slash MVS command ✅
    - C. ISPF option 1 BROWSE
    - D. ISPF EDIT SUBMIT

    正解: **B** ／ 難易度: 上級

    **解説:** 応答面観点の資料照合としてMVSコマンド発行読取を選び、答えはBで、記録焦点はMVSコマンド発行状態です。投入面観点のMVSコマンド発行定義は、スプール表示検索機能コマンド行からMVSまたはJESコマンドを発行することを満たす入力、画面、応答を同じ証跡で確認するMVSコマンド発行定義です。編集面観点から見るMVSコマンド発行根拠は、slash command and Uログ responseを応答画面と対応させるMVSコマンド発行根拠です。検索面観点のMVSコマンド発行応答は、スプール表示検索機能コマンドの入力要求と戻った表示を結び、運用状態を説明するMVSコマンド発行応答です。A: 制御面観点の参照先はブロードキャスト表示状態で、作業記録で追跡する対象はMVSコマンド発行棚卸です。B: 照合面観点のMVSコマンド発行定義は、入力名と画面内のslash command and Uログ responseを結ぶMVSコマンド発行照合です。C: 一覧面観点の照合先は表示選択根拠で、中心はMVSコマンド発行監査です。D: 端末面観点の処理段階はJCLサブミット応答で、入力と表示を結ぶ対象はMVSコマンド発行引継ぎです。通信面観点の用語定義として、MVSコマンド発行とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むMVSコマンド発行復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide slash command

    ---

    **問題.** 通信面のジョブ取消と出力削除を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってP action characterを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF EDIT SAVE
    - B. ISPF SPLIT screen
    - C. SDSF P purge ✅
    - D. SDSF S output data set

    正解: **C** ／ 難易度: 上級

    **解説:** 端末面観点の出力確認としてジョブ取消と出力削除状態を読み、答えはCで、照合焦点はジョブ取消と出力削除定義です。検索面観点のジョブ取消と出力削除根拠は、ジョブを取り消して出力をパージすることを満たす入力、画面、応答を同じ証跡で確認するジョブ取消と出力削除根拠です。投入面観点で残すジョブ取消と出力削除応答は、P action characterをコマンドまたはパネル形式と照合するジョブ取消と出力削除応答です。通信面観点のジョブ取消と出力削除保守は、スプール表示検索機能ジョブ操作の入力要求と戻った表示を結び、運用状態を説明するジョブ取消と出力削除保守です。A: 照合面観点の比較先は編集保存定義で、要求対象はジョブ取消と出力削除監査です。B: 一覧面観点の照合先は画面分割根拠で、中心はジョブ取消と出力削除引継ぎです。C: 管理面観点のジョブ取消と出力削除応答は、入力名と画面内のP action characterを結ぶジョブ取消と出力削除報告です。D: 出力面観点の参照先は出力データセット表示保守で、作業記録で追跡する対象はジョブ取消と出力削除復旧です。操作面観点の用語定義として、ジョブ取消と出力削除とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ取消と出力削除照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide ST action characters

    ---

    **問題.** 操作面のジョブ保留を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってH action characterを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF slash MVS command
    - B. LISTALC STATUS
    - C. TRANSMIT DATASET
    - D. SDSF H hold ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 応答面観点のジョブ保留定義は正答Dで、表記上の手掛かりはスプール表示検索機能 H hold根拠です。通信面観点のジョブ保留応答は、ジョブまたは出力を保留状態へ変更することを満たす入力、画面、応答を同じ証跡で確認するジョブ保留応答です。編集面観点で読むジョブ保留保守は、H action characterを資料のコマンド形式やパネル形式と照合するジョブ保留保守です。操作面観点のジョブ保留監査は、スプール表示検索機能ジョブ操作の入力要求と戻った表示を結び、運用状態を説明するジョブ保留監査です。A: 一覧面観点の照合先はMVSコマンド発行根拠で、中心はジョブ保留棚卸です。B: 端末面観点の処理段階は割り当て一覧応答で、入力と表示を結ぶ対象はジョブ保留復旧です。C: 出力面観点の参照先はデータセット送信保守で、作業記録で追跡する対象はジョブ保留照合です。D: 応答面観点のジョブ保留監査は、入力名と画面内のH action characterを結ぶジョブ保留選択です。確認面観点の用語定義として、ジョブ保留とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ保留報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide DA action characters

    ---

    **問題.** 確認面のREADYプロンプト確認を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってREADY表示と入力待ち状態を確認する場合、この状況で優先する項目はどれですか。

    - A. READY prompt ✅
    - B. DELETE DATASET
    - C. CALL command
    - D. ISPF EDIT SAVE

    正解: **A** ／ 難易度: 初級

    **解説:** 端末面観点で読むREADYプロンプト確認根拠は正答位置Aで、記録する焦点はREADY prompt応答です。操作面観点のREADYプロンプト確認保守は、TSO/Eコマンド入力可能な状態を識別することを満たす入力、画面、応答を同じ証跡で確認するREADYプロンプト確認保守です。投入面観点のREADYプロンプト確認監査は、READY表示と入力待ち状態を入力記録と合わせて処理対象を見分けるREADYプロンプト確認監査です。確認面観点のREADYプロンプト確認引継ぎは、TSO/Eセッションの入力要求と戻った表示を結び、運用状態を説明するREADYプロンプト確認引継ぎです。A: 管理面観点のREADYプロンプト確認応答は、入力名と画面内のREADY表示と入力待ち状態を結ぶREADYプロンプト確認反映です。B: 出力面観点の参照先はデータセット削除保守で、作業記録で追跡する対象はREADYプロンプト確認報告です。C: 応答面観点の比較先はロードモジュール呼出監査で、要求対象はREADYプロンプト確認棚卸です。D: 表示面観点の照合先は編集保存引継ぎで、中心はREADYプロンプト確認復旧です。監査面観点の用語定義として、READYプロンプト確認とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むREADYプロンプト確認選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide READY

    ---

    **問題.** 監査面のセッション終了を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってREADY配下のログオフ入力を確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF DA panel
    - B. LOGOFF command ✅
    - C. SDSF OWNER
    - D. READY prompt

    正解: **B** ／ 難易度: 初級

    **解説:** 編集面観点の資料照合としてセッション終了応答を選び、答えはBで、記録焦点はセッション終了保守です。確認面観点のセッション終了監査は、TSO/E利用後にログオフして端末セッションを閉じることを満たす入力、画面、応答を同じ証跡で確認するセッション終了監査です。通信面観点から見るセッション終了引継ぎは、READY配下のログオフ入力を応答画面と対応させるセッション終了引継ぎです。監査面観点のセッション終了棚卸は、TSO/Eセッションの入力要求と戻った表示を結び、運用状態を説明するセッション終了棚卸です。A: 出力面観点の参照先は実行中利用者表示保守で、作業記録で追跡する対象はセッション終了選択です。B: 応答面観点のセッション終了監査は、入力名と画面内のREADY配下のログオフ入力を結ぶセッション終了観点です。C: 表示面観点の照合先は所有者絞り込み引継ぎで、中心はセッション終了照合です。D: 投入面観点の処理段階はREADYプロンプト確認棚卸で、入力と表示を結ぶ対象はセッション終了報告です。保存面観点の用語定義として、セッション終了とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むセッション終了反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide LOGOFF

    ---

    **問題.** 照合面のメッセージID表示を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってプロファイル メッセージID表示を確認する場合、どの項目を選ぶべきですか。

    - A. PF1 HELP
    - B. SDSF H panel
    - C. SDSF ULOG
    - D. PROFILE MSGID ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 編集面観点のメッセージID表示監査は正答Dで、表記上の手掛かりはプロファイル メッセージID引継ぎです。保存面観点のメッセージID表示棚卸は、TSO/E応答にメッセージIDを表示する設定を確認することを満たす入力、画面、応答を同じ証跡で確認するメッセージID表示棚卸です。通信面観点で読むメッセージID表示復旧は、プロファイル メッセージID表示を資料のコマンド形式やパネル形式と照合するメッセージID表示復旧です。照合面観点のメッセージID表示照合は、TSO/Eプロファイルの入力要求と戻った表示を結び、運用状態を説明するメッセージID表示照合です。A: 表示面観点の照合先はヘルプキー表示引継ぎで、中心はメッセージID表示選択です。B: 投入面観点の処理段階はHeld Output Queue棚卸で、入力と表示を結ぶ対象はメッセージID表示反映です。C: 操作面観点の参照先はユーザーセッションログ復旧で、作業記録で追跡する対象はメッセージID表示観点です。D: 編集面観点のメッセージID表示照合は、入力名と画面内のプロファイル メッセージID表示を結ぶメッセージID表示読取です。選択面観点の用語定義として、メッセージID表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むメッセージID表示証跡です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PROFILE MSGID

    ---

    **問題.** 選択面のコマンドヘルプ表示を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってヘルプ member textとprompt modeを確認する場合、最も適切な確認対象はどれですか。

    - A. HELP command ✅
    - B. PROFILE MSGID
    - C. SEND USER
    - D. ISPF option 1 BROWSE

    正解: **A** ／ 難易度: 初級

    **解説:** 投入面観点で読むコマンドヘルプ表示引継ぎは正答位置Aで、記録する焦点はヘルプ command棚卸です。照合面観点のコマンドヘルプ表示復旧は、コマンドの構文やオペランド説明をヘルプデータから確認することを満たす入力、画面、応答を同じ証跡で確認するコマンドヘルプ表示復旧です。確認面観点のコマンドヘルプ表示照合は、ヘルプ member textとprompt modeを入力記録と合わせて処理対象を見分けるコマンドヘルプ表示照合です。選択面観点のコマンドヘルプ表示報告は、TSO/Eヘルプの入力要求と戻った表示を結び、運用状態を説明するコマンドヘルプ表示報告です。A: 端末面観点のコマンドヘルプ表示棚卸は、入力名と画面内のヘルプ member textとprompt modeを結ぶコマンドヘルプ表示状態です。B: 操作面観点の参照先はメッセージID表示復旧で、作業記録で追跡する対象はコマンドヘルプ表示証跡です。C: 編集面観点の比較先は短文メッセージ送信照合で、要求対象はコマンドヘルプ表示選択です。D: 検索面観点の照合先は表示選択報告で、中心はコマンドヘルプ表示反映です。管理面観点の用語定義として、コマンドヘルプ表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むコマンドヘルプ表示読取です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference HELP

    ---

    **問題.** 管理面の割り当て一覧を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってDD名と実行中表示TA SET NAMEを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF CHANGE
    - B. LISTALC STATUS ✅
    - C. SDSF I panel
    - D. SDSF FILTER

    正解: **B** ／ 難易度: 中級

    **解説:** 通信面観点の資料照合として割り当て一覧棚卸を選び、答えはBで、記録焦点は割り当て一覧復旧です。選択面観点の割り当て一覧照合は、セッション中に割り当て済みのDD名とデータセットを確認することを満たす入力、画面、応答を同じ証跡で確認する割り当て一覧照合です。保存面観点から見る割り当て一覧報告は、DD名と実行中表示TA SET NAMEを応答画面と対応させる割り当て一覧報告です。管理面観点の割り当て一覧選択は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明する割り当て一覧選択です。A: 操作面観点の参照先は文字列置換復旧で、作業記録で追跡する対象は割り当て一覧読取です。B: 編集面観点の割り当て一覧照合は、入力名と画面内のDD名と実行中表示TA SET NAMEを結ぶ割り当て一覧定義です。C: 検索面観点の照合先はInput Queue報告で、中心は割り当て一覧観点です。D: 確認面観点の処理段階は条件フィルター選択で、入力と表示を結ぶ対象は割り当て一覧証跡です。一覧面観点の用語定義として、割り当て一覧とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む割り当て一覧状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference LISTALC

    ---

    **問題.** 一覧面のメンバー一覧表示を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってMEMBERS operandとmember nameを確認する場合、証跡として中心に置く項目はどれですか。

    - A. PROFILE PREFIX
    - B. DELETE DATASET
    - C. LISTDS MEMBERS ✅
    - D. ISPF Primary Option Menu

    正解: **C** ／ 難易度: 中級

    **解説:** 確認面観点の出力確認としてメンバー一覧表示復旧を読み、答えはCで、照合焦点はメンバー一覧表示照合です。管理面観点のメンバー一覧表示報告は、PDSまたはPDSEのメンバー一覧を確認することを満たす入力、画面、応答を同じ証跡で確認するメンバー一覧表示報告です。選択面観点で残すメンバー一覧表示選択は、MEMBERS operandとmember nameをコマンドまたはパネル形式と照合するメンバー一覧表示選択です。一覧面観点のメンバー一覧表示反映は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するメンバー一覧表示反映です。A: 編集面観点の比較先はデータセット接頭辞照合で、要求対象はメンバー一覧表示観点です。B: 検索面観点の照合先はデータセット削除報告で、中心はメンバー一覧表示証跡です。C: 投入面観点のメンバー一覧表示選択は、入力名と画面内のMEMBERS operandとmember nameを結ぶメンバー一覧表示根拠です。D: 照合面観点の参照先は基本選択メニュー表示反映で、作業記録で追跡する対象はメンバー一覧表示状態です。応答面観点の用語定義として、メンバー一覧表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むメンバー一覧表示定義です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference LISTDS

    ---

    **問題.** 応答面のデータセット割り当てを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って割り当て データセット and DD名を確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF FIND
    - B. SDSF DA panel
    - C. SDSF SORT
    - D. ALLOCATE DATASET ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 通信面観点のデータセット割り当て照合は正答Dで、表記上の手掛かりは割り当て データセット報告です。一覧面観点のデータセット割り当て選択は、TSO/Eコマンド処理で使うDD名をデータセットへ割り当てることを満たす入力、画面、応答を同じ証跡で確認するデータセット割り当て選択です。保存面観点で読むデータセット割り当て反映は、割り当て データセット and DD名を資料のコマンド形式やパネル形式と照合するデータセット割り当て反映です。応答面観点のデータセット割り当て観点は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明するデータセット割り当て観点です。A: 検索面観点の照合先は文字列検索報告で、中心はデータセット割り当て読取です。B: 確認面観点の処理段階は実行中利用者表示選択で、入力と表示を結ぶ対象はデータセット割り当て状態です。C: 照合面観点の参照先は列ソート反映で、作業記録で追跡する対象はデータセット割り当て定義です。D: 通信面観点のデータセット割り当て観点は、入力名と画面内の割り当て データセット and DD名を結ぶデータセット割り当て応答です。制御面観点の用語定義として、データセット割り当てとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット割り当て根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference ALLOCATE

    ---

    **問題.** 制御面のDD名解放を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って解放 FILE operandを確認する場合、どの項目を選ぶべきですか。

    - A. FREE DDNAME ✅
    - B. SDSF ULOG
    - C. PROFILE MSGID
    - D. LISTBC

    正解: **A** ／ 難易度: 中級

    **解説:** 確認面観点で読むDD名解放報告は正答位置Aで、記録する焦点は解放 DD名選択です。応答面観点のDD名解放反映は、不要になったDD名割り当てをセッションから外すことを満たす入力、画面、応答を同じ証跡で確認するDD名解放反映です。選択面観点のDD名解放観点は、解放 FILE operandを入力記録と合わせて処理対象を見分けるDD名解放観点です。制御面観点のDD名解放証跡は、TSO/E割り当ての入力要求と戻った表示を結び、運用状態を説明するDD名解放証跡です。A: 投入面観点のDD名解放選択は、入力名と画面内の解放 FILE operandを結ぶDD名解放保守です。B: 照合面観点の参照先はユーザーセッションログ反映で、作業記録で追跡する対象はDD名解放根拠です。C: 通信面観点の比較先はメッセージID表示観点で、要求対象はDD名解放読取です。D: 監査面観点の照合先はブロードキャスト表示証跡で、中心はDD名解放状態です。端末面観点の用語定義として、DD名解放とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むDD名解放応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference FREE

    ---

    **問題.** 端末面のデータセット改名を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってold データセット name and new データセット nameを確認する場合、最も適切な確認対象はどれですか。

    - A. ISPF option 3.3 Move Copy
    - B. RENAME DATASET ✅
    - C. PF3 END
    - D. SDSF H panel

    正解: **B** ／ 難易度: 中級

    **解説:** 保存面観点の資料照合としてデータセット改名選択を選び、答えはBで、記録焦点はデータセット改名反映です。制御面観点のデータセット改名観点は、既存データセット名を新しい名前へ変更することを満たす入力、画面、応答を同じ証跡で確認するデータセット改名観点です。一覧面観点から見るデータセット改名証跡は、old データセット name and new データセット nameを応答画面と対応させるデータセット改名証跡です。端末面観点のデータセット改名読取は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するデータセット改名読取です。A: 照合面観点の参照先はMOVE/COPY反映で、作業記録で追跡する対象はデータセット改名応答です。B: 通信面観点のデータセット改名観点は、入力名と画面内のold データセット name and new データセット nameを結ぶデータセット改名監査です。C: 監査面観点の照合先は終了キー終了証跡で、中心はデータセット改名定義です。D: 選択面観点の処理段階はHeld Output Queue読取で、入力と表示を結ぶ対象はデータセット改名根拠です。表示面観点の用語定義として、データセット改名とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット改名保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference RENAME

    ---

    **問題.** 表示面のデータセット削除を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って削除 command and データセット nameを確認する場合、この状況で優先する項目はどれですか。

    - A. SDSF ULOG
    - B. PROFILE MSGID
    - C. DELETE DATASET ✅
    - D. LISTBC

    正解: **C** ／ 難易度: 中級

    **解説:** 選択面観点の出力確認としてデータセット削除反映を読み、答えはCで、照合焦点はデータセット削除観点です。端末面観点のデータセット削除証跡は、不要なデータセットをTSO/Eコマンドで削除することを満たす入力、画面、応答を同じ証跡で確認するデータセット削除証跡です。制御面観点で残すデータセット削除読取は、削除 command and データセット nameをコマンドまたはパネル形式と照合するデータセット削除読取です。表示面観点のデータセット削除状態は、TSO/Eデータセットの入力要求と戻った表示を結び、運用状態を説明するデータセット削除状態です。A: 通信面観点の比較先はユーザーセッションログ観点で、要求対象はデータセット削除定義です。B: 監査面観点の照合先はメッセージID表示証跡で、中心はデータセット削除根拠です。C: 確認面観点のデータセット削除読取は、入力名と画面内の削除 command and データセット nameを結ぶデータセット削除引継ぎです。D: 応答面観点の参照先はブロードキャスト表示状態で、作業記録で追跡する対象はデータセット削除保守です。編集面観点の用語定義として、データセット削除とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット削除監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference DELETE

    ---

    **問題.** 編集面の短文メッセージ送信を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って送信 command and target userを確認する場合、証跡として中心に置く項目はどれですか。

    - A. OUTDES
    - B. ISPF option 3.2 Data Set Utility
    - C. PF3 END
    - D. SEND USER ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 保存面観点の短文メッセージ送信観点は正答Dで、表記上の手掛かりは送信 USER証跡です。表示面観点の短文メッセージ送信読取は、同一システムの利用者へ短いメッセージを送ることを満たす入力、画面、応答を同じ証跡で確認する短文メッセージ送信読取です。一覧面観点で読む短文メッセージ送信状態は、送信 command and target userを資料のコマンド形式やパネル形式と照合する短文メッセージ送信状態です。編集面観点の短文メッセージ送信定義は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明する短文メッセージ送信定義です。A: 監査面観点の照合先は出力記述子作成証跡で、中心は短文メッセージ送信応答です。B: 選択面観点の処理段階はData Set Utility読取で、入力と表示を結ぶ対象は短文メッセージ送信保守です。C: 応答面観点の参照先は終了キー終了状態で、作業記録で追跡する対象は短文メッセージ送信監査です。D: 保存面観点の短文メッセージ送信定義は、入力名と画面内の送信 command and target userを結ぶ短文メッセージ送信棚卸です。出力面観点の用語定義として、短文メッセージ送信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む短文メッセージ送信引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide SEND

    ---

    **問題.** 出力面のブロードキャスト表示を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってbroadcast データセット messagesを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. LISTBC ✅
    - B. SDSF DA panel
    - C. SDSF OWNER
    - D. READY prompt

    正解: **A** ／ 難易度: 初級

    **解説:** 選択面観点で読むブロードキャスト表示証跡は正答位置Aで、記録する焦点はブロードキャスト表示読取です。編集面観点のブロードキャスト表示状態は、システムや他利用者からのメッセージを確認することを満たす入力、画面、応答を同じ証跡で確認するブロードキャスト表示状態です。制御面観点のブロードキャスト表示定義は、broadcast データセット messagesを入力記録と合わせて処理対象を見分けるブロードキャスト表示定義です。出力面観点のブロードキャスト表示根拠は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明するブロードキャスト表示根拠です。A: 確認面観点のブロードキャスト表示読取は、入力名と画面内のbroadcast データセット messagesを結ぶブロードキャスト表示復旧です。B: 応答面観点の参照先は実行中利用者表示状態で、作業記録で追跡する対象はブロードキャスト表示引継ぎです。C: 保存面観点の比較先は所有者絞り込み定義で、要求対象はブロードキャスト表示応答です。D: 管理面観点の照合先はREADYプロンプト確認根拠で、中心はブロードキャスト表示保守です。投入面観点の用語定義として、ブロードキャスト表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むブロードキャスト表示棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E User's Guide LISTBC

    ---

    **問題.** 投入面のデータセット送信を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って転送送信 target and データセット operandを確認する場合、どの項目を選ぶべきですか。

    - A. ISPF option 1 BROWSE
    - B. TRANSMIT DATASET ✅
    - C. ISPF EDIT CANCEL
    - D. SDSF ST panel

    正解: **B** ／ 難易度: 上級

    **解説:** 一覧面観点の資料照合としてデータセット送信読取を選び、答えはBで、記録焦点はデータセット送信状態です。出力面観点のデータセット送信定義は、別ユーザーまたは別ノードへデータセットを送信することを満たす入力、画面、応答を同じ証跡で確認するデータセット送信定義です。表示面観点から見るデータセット送信根拠は、転送送信 target and データセット operandを応答画面と対応させるデータセット送信根拠です。投入面観点のデータセット送信応答は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明するデータセット送信応答です。A: 応答面観点の参照先は表示選択状態で、作業記録で追跡する対象はデータセット送信棚卸です。B: 保存面観点のデータセット送信定義は、入力名と画面内の転送送信 target and データセット operandを結ぶデータセット送信照合です。C: 管理面観点の照合先は編集取消根拠で、中心はデータセット送信監査です。D: 制御面観点の処理段階はStatus パネル応答で、入力と表示を結ぶ対象はデータセット送信引継ぎです。検索面観点の用語定義として、データセット送信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット送信復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference TRANSMIT

    ---

    **問題.** 検索面の送信データ受信を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って転送受信 prompt and データセット nameを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF PREFIX
    - B. SDSF P purge
    - C. RECEIVE DATASET ✅
    - D. LISTDS MEMBERS

    正解: **C** ／ 難易度: 中級

    **解説:** 制御面観点の出力確認として送信データ受信状態を読み、答えはCで、照合焦点は送信データ受信定義です。投入面観点の送信データ受信根拠は、転送送信されたデータセットや長文メッセージを受信することを満たす入力、画面、応答を同じ証跡で確認する送信データ受信根拠です。出力面観点で残す送信データ受信応答は、転送受信 prompt and データセット nameをコマンドまたはパネル形式と照合する送信データ受信応答です。検索面観点の送信データ受信保守は、TSO/E通信の入力要求と戻った表示を結び、運用状態を説明する送信データ受信保守です。A: 保存面観点の比較先はジョブ名接頭辞定義で、要求対象は送信データ受信監査です。B: 管理面観点の照合先はジョブ取消と出力削除根拠で、中心は送信データ受信引継ぎです。C: 選択面観点の送信データ受信応答は、入力名と画面内の転送受信 prompt and データセット nameを結ぶ送信データ受信報告です。D: 編集面観点の参照先はメンバー一覧表示保守で、作業記録で追跡する対象は送信データ受信復旧です。通信面観点の用語定義として、送信データ受信とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む送信データ受信照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference RECEIVE

    ---

    **問題.** 通信面の出力記述子作成を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って出力記述子 operand and destinationを確認する場合、この状況で優先する項目はどれですか。

    - A. LISTALC STATUS
    - B. LISTBC
    - C. ISPF option 3.4 DSLIST
    - D. OUTDES ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 一覧面観点の出力記述子作成定義は正答Dで、表記上の手掛かりは出力記述子根拠です。検索面観点の出力記述子作成応答は、印刷や出力処理の宛先属性を定義することを満たす入力、画面、応答を同じ証跡で確認する出力記述子作成応答です。表示面観点で読む出力記述子作成保守は、出力記述子 operand and destinationを資料のコマンド形式やパネル形式と照合する出力記述子作成保守です。通信面観点の出力記述子作成監査は、TSO/E出力の入力要求と戻った表示を結び、運用状態を説明する出力記述子作成監査です。A: 管理面観点の照合先は割り当て一覧根拠で、中心は出力記述子作成棚卸です。B: 制御面観点の処理段階はブロードキャスト表示応答で、入力と表示を結ぶ対象は出力記述子作成復旧です。C: 編集面観点の参照先はデータセット一覧一覧保守で、作業記録で追跡する対象は出力記述子作成照合です。D: 一覧面観点の出力記述子作成監査は、入力名と画面内の出力記述子 operand and destinationを結ぶ出力記述子作成選択です。操作面観点の用語定義として、出力記述子作成とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む出力記述子作成報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference OUTDES

    ---

    **問題.** 操作面のデータセット印刷を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って印刷 データセット operandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. PRINTDS ✅
    - B. PF3 END
    - C. SDSF O panel
    - D. SDSF ARRANGE

    正解: **A** ／ 難易度: 中級

    **解説:** 制御面観点で読むデータセット印刷根拠は正答位置Aで、記録する焦点は印刷応答です。通信面観点のデータセット印刷保守は、データセット内容を印刷または出力キューへ送ることを満たす入力、画面、応答を同じ証跡で確認するデータセット印刷保守です。出力面観点のデータセット印刷監査は、印刷 データセット operandを入力記録と合わせて処理対象を見分けるデータセット印刷監査です。操作面観点のデータセット印刷引継ぎは、TSO/E出力の入力要求と戻った表示を結び、運用状態を説明するデータセット印刷引継ぎです。A: 選択面観点のデータセット印刷応答は、入力名と画面内の印刷 データセット operandを結ぶデータセット印刷反映です。B: 編集面観点の参照先は終了キー終了保守で、作業記録で追跡する対象はデータセット印刷報告です。C: 一覧面観点の比較先はOutput Queue監査で、要求対象はデータセット印刷棚卸です。D: 端末面観点の照合先は列配置変更引継ぎで、中心はデータセット印刷復旧です。確認面観点の用語定義として、データセット印刷とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット印刷選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / TSO / E Command Reference PRINTDS

    ---

    **問題.** 監査面の基本選択メニュー表示を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってOPTION line and menu entriesを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF FILTER
    - B. LOGOFF command
    - C. ISPF Primary Option Menu ✅
    - D. RENAME DATASET

    正解: **C** ／ 難易度: 初級

    **解説:** 出力面観点の出力確認として基本選択メニュー表示保守を読み、答えはCで、照合焦点は基本選択メニュー表示監査です。確認面観点の基本選択メニュー表示引継ぎは、対話式生産性機能/PDFの主要機能を選択する入口を確認することを満たす入力、画面、応答を同じ証跡で確認する基本選択メニュー表示引継ぎです。操作面観点で残す基本選択メニュー表示棚卸は、OPTION line and menu entriesをコマンドまたはパネル形式と照合する基本選択メニュー表示棚卸です。監査面観点の基本選択メニュー表示復旧は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する基本選択メニュー表示復旧です。A: 一覧面観点の比較先は条件フィルター監査で、要求対象は基本選択メニュー表示照合です。B: 端末面観点の照合先はセッション終了引継ぎで、中心は基本選択メニュー表示報告です。C: 制御面観点の基本選択メニュー表示棚卸は、入力名と画面内のOPTION line and menu entriesを結ぶ基本選択メニュー表示証跡です。D: 通信面観点の参照先はデータセット改名復旧で、作業記録で追跡する対象は基本選択メニュー表示反映です。保存面観点の用語定義として、基本選択メニュー表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む基本選択メニュー表示観点です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide Primary Option Menu

    ---

    **問題.** 保存面の表示選択を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って表示 option and データセット nameを確認する場合、最も適切な確認対象はどれですか。

    - A. TRANSMIT DATASET
    - B. ISPF option 3.4 DSLIST
    - C. ISPF CHANGE
    - D. ISPF option 1 BROWSE ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 表示面観点の表示選択監査は正答Dで、表記上の手掛かりは対話式生産性機能 option 1 表示引継ぎです。監査面観点の表示選択棚卸は、データセットを更新せず表示することを満たす入力、画面、応答を同じ証跡で確認する表示選択棚卸です。検索面観点で読む表示選択復旧は、表示 option and データセット nameを資料のコマンド形式やパネル形式と照合する表示選択復旧です。保存面観点の表示選択照合は、対話式生産性機能表示の入力要求と戻った表示を結び、運用状態を説明する表示選択照合です。A: 端末面観点の照合先はデータセット送信引継ぎで、中心は表示選択選択です。B: 出力面観点の処理段階はデータセット一覧一覧棚卸で、入力と表示を結ぶ対象は表示選択反映です。C: 通信面観点の参照先は文字列置換復旧で、作業記録で追跡する対象は表示選択観点です。D: 表示面観点の表示選択照合は、入力名と画面内の表示 option and データセット nameを結ぶ表示選択読取です。照合面観点の用語定義として、表示選択とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む表示選択証跡です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide BROWSE

    ---

    **問題.** 照合面の編集選択を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って編集 option and edit パネルを確認する場合、この状況で優先する項目はどれですか。

    - A. ISPF option 2 EDIT ✅
    - B. SDSF DA panel
    - C. SDSF OWNER
    - D. READY prompt

    正解: **A** ／ 難易度: 初級

    **解説:** 出力面観点で読む編集選択引継ぎは正答位置Aで、記録する焦点は対話式生産性機能 option 2 編集棚卸です。保存面観点の編集選択復旧は、ソースやJCLメンバーを編集することを満たす入力、画面、応答を同じ証跡で確認する編集選択復旧です。操作面観点の編集選択照合は、編集 option and edit パネルを入力記録と合わせて処理対象を見分ける編集選択照合です。照合面観点の編集選択報告は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集選択報告です。A: 制御面観点の編集選択棚卸は、入力名と画面内の編集 option and edit パネルを結ぶ編集選択状態です。B: 通信面観点の参照先は実行中利用者表示復旧で、作業記録で追跡する対象は編集選択証跡です。C: 表示面観点の比較先は所有者絞り込み照合で、要求対象は編集選択選択です。D: 投入面観点の照合先はREADYプロンプト確認報告で、中心は編集選択反映です。選択面観点の用語定義として、編集選択とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集選択読取です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide EDIT

    ---

    **問題.** 選択面のデータセット一覧一覧を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってデータセット一覧 パネル and DSNAME LEVELを確認する場合、証跡として中心に置く項目はどれですか。

    - A. LISTBC
    - B. ISPF option 3.4 DSLIST ✅
    - C. ISPF option 1 BROWSE
    - D. ISPF FIND

    正解: **B** ／ 難易度: 中級

    **解説:** 検索面観点の資料照合としてデータセット一覧一覧棚卸を選び、答えはBで、記録焦点はデータセット一覧一覧復旧です。照合面観点のデータセット一覧一覧照合は、データセット一覧から表示、編集、削除などを行うことを満たす入力、画面、応答を同じ証跡で確認するデータセット一覧一覧照合です。監査面観点から見るデータセット一覧一覧報告は、データセット一覧 パネル and DSNAME LEVELを応答画面と対応させるデータセット一覧一覧報告です。選択面観点のデータセット一覧一覧選択は、対話式生産性機能ユーティリティの入力要求と戻った表示を結び、運用状態を説明するデータセット一覧一覧選択です。A: 通信面観点の参照先はブロードキャスト表示復旧で、作業記録で追跡する対象はデータセット一覧一覧読取です。B: 表示面観点のデータセット一覧一覧照合は、入力名と画面内のデータセット一覧 パネル and DSNAME LEVELを結ぶデータセット一覧一覧定義です。C: 投入面観点の照合先は表示選択報告で、中心はデータセット一覧一覧観点です。D: 操作面観点の処理段階は文字列検索選択で、入力と表示を結ぶ対象はデータセット一覧一覧証跡です。管理面観点の用語定義として、データセット一覧一覧とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むデータセット一覧一覧状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide DSLIST

    ---

    **問題.** 一覧面のMOVE/COPYを定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってMove/Copy utility パネルを確認する場合、どの項目を選ぶべきですか。

    - A. LISTBC
    - B. ISPF option 1 BROWSE
    - C. ISPF FIND
    - D. ISPF option 3.3 Move Copy ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 検索面観点のMOVE/COPY照合は正答Dで、表記上の手掛かりは対話式生産性機能 option 3.3 Move Copy報告です。管理面観点のMOVE/COPY選択は、データセットやメンバーを移動またはコピーすることを満たす入力、画面、応答を同じ証跡で確認するMOVE/COPY選択です。監査面観点で読むMOVE/COPY反映は、Move/Copy utility パネルを資料のコマンド形式やパネル形式と照合するMOVE/COPY反映です。一覧面観点のMOVE/COPY観点は、対話式生産性機能ユーティリティの入力要求と戻った表示を結び、運用状態を説明するMOVE/COPY観点です。A: 投入面観点の照合先はブロードキャスト表示報告で、中心はMOVE/COPY読取です。B: 操作面観点の処理段階は表示選択選択で、入力と表示を結ぶ対象はMOVE/COPY状態です。C: 保存面観点の参照先は文字列検索反映で、作業記録で追跡する対象はMOVE/COPY定義です。D: 検索面観点のMOVE/COPY観点は、入力名と画面内のMove/Copy utility パネルを結ぶMOVE/COPY応答です。応答面観点の用語定義として、MOVE/COPYとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むMOVE/COPY根拠です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide Move Copy

    ---

    **問題.** 制御面の編集保存を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って保存 primary commandを確認する場合、この状況で優先する項目はどれですか。

    - A. SDSF P purge
    - B. ISPF EDIT SAVE ✅
    - C. LISTALC STATUS
    - D. TRANSMIT DATASET

    正解: **B** ／ 難易度: 中級

    **解説:** 監査面観点の資料照合として編集保存選択を選び、答えはBで、記録焦点は編集保存反映です。応答面観点の編集保存観点は、編集したメンバーを保存してセッションを継続または終了することを満たす入力、画面、応答を同じ証跡で確認する編集保存観点です。管理面観点から見る編集保存証跡は、保存 primary commandを応答画面と対応させる編集保存証跡です。制御面観点の編集保存読取は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集保存読取です。A: 保存面観点の参照先はジョブ取消と出力削除反映で、作業記録で追跡する対象は編集保存応答です。B: 検索面観点の編集保存観点は、入力名と画面内の保存 primary commandを結ぶ編集保存監査です。C: 確認面観点の照合先は割り当て一覧証跡で、中心は編集保存定義です。D: 照合面観点の処理段階はデータセット送信読取で、入力と表示を結ぶ対象は編集保存根拠です。端末面観点の用語定義として、編集保存とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集保存保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide editor SAVE

    ---

    **問題.** 端末面の編集取消を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って取消 primary commandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. ISPF option 3.3 Move Copy
    - B. PF1 HELP
    - C. ISPF EDIT CANCEL ✅
    - D. SDSF ? JDS

    正解: **C** ／ 難易度: 中級

    **解説:** 照合面観点の出力確認として編集取消反映を読み、答えはCで、照合焦点は編集取消観点です。制御面観点の編集取消証跡は、保存せず編集内容を破棄して終了することを満たす入力、画面、応答を同じ証跡で確認する編集取消証跡です。応答面観点で残す編集取消読取は、取消 primary commandをコマンドまたはパネル形式と照合する編集取消読取です。端末面観点の編集取消状態は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する編集取消状態です。A: 検索面観点の比較先はMOVE/COPY観点で、要求対象は編集取消定義です。B: 確認面観点の照合先はヘルプキー表示証跡で、中心は編集取消根拠です。C: 操作面観点の編集取消読取は、入力名と画面内の取消 primary commandを結ぶ編集取消引継ぎです。D: 一覧面観点の参照先はJob Data Set表示状態で、作業記録で追跡する対象は編集取消保守です。表示面観点の用語定義として、編集取消とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む編集取消監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide editor CANCEL

    ---

    **問題.** 表示面のJCLサブミットを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って投入 primary command and JOB statementを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF slash MVS command
    - B. HELP command
    - C. LISTBC
    - D. ISPF EDIT SUBMIT ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 監査面観点のJCLサブミット観点は正答Dで、表記上の手掛かりは対話式生産性機能 編集 投入証跡です。端末面観点のJCLサブミット読取は、編集画面からJCLをJESへ投入することを満たす入力、画面、応答を同じ証跡で確認するJCLサブミット読取です。管理面観点で読むJCLサブミット状態は、投入 primary command and JOB statementを資料のコマンド形式やパネル形式と照合するJCLサブミット状態です。表示面観点のJCLサブミット定義は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明するJCLサブミット定義です。A: 確認面観点の照合先はMVSコマンド発行証跡で、中心はJCLサブミット応答です。B: 照合面観点の処理段階はコマンドヘルプ表示読取で、入力と表示を結ぶ対象はJCLサブミット保守です。C: 一覧面観点の参照先はブロードキャスト表示状態で、作業記録で追跡する対象はJCLサブミット監査です。D: 監査面観点のJCLサブミット定義は、入力名と画面内の投入 primary command and JOB statementを結ぶJCLサブミット棚卸です。編集面観点の用語定義として、JCLサブミットとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むJCLサブミット引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide SUBMIT

    ---

    **問題.** 編集面の文字列検索を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使って検索 primary commandを確認する場合、どの項目を選ぶべきですか。

    - A. ISPF FIND ✅
    - B. TRANSMIT DATASET
    - C. ISPF option 2 EDIT
    - D. ISPF CHANGE

    正解: **A** ／ 難易度: 初級

    **解説:** 照合面観点で読む文字列検索証跡は正答位置Aで、記録する焦点は対話式生産性機能 検索読取です。表示面観点の文字列検索状態は、編集または表示中のデータから文字列を探すことを満たす入力、画面、応答を同じ証跡で確認する文字列検索状態です。応答面観点の文字列検索定義は、検索 primary commandを入力記録と合わせて処理対象を見分ける文字列検索定義です。編集面観点の文字列検索根拠は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する文字列検索根拠です。A: 操作面観点の文字列検索読取は、入力名と画面内の検索 primary commandを結ぶ文字列検索復旧です。B: 一覧面観点の参照先はデータセット送信状態で、作業記録で追跡する対象は文字列検索引継ぎです。C: 監査面観点の比較先は編集選択定義で、要求対象は文字列検索応答です。D: 選択面観点の照合先は文字列置換根拠で、中心は文字列検索保守です。出力面観点の用語定義として、文字列検索とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む文字列検索棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide FIND

    ---

    **問題.** 出力面の文字列置換を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使って置換 primary commandを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF ? JDS
    - B. ISPF CHANGE ✅
    - C. SDSF ULOG
    - D. HELP command

    正解: **B** ／ 難易度: 中級

    **解説:** 管理面観点の資料照合として文字列置換読取を選び、答えはBで、記録焦点は文字列置換状態です。編集面観点の文字列置換定義は、編集データ内の文字列を別の値へ置き換えることを満たす入力、画面、応答を同じ証跡で確認する文字列置換定義です。端末面観点から見る文字列置換根拠は、置換 primary commandを応答画面と対応させる文字列置換根拠です。出力面観点の文字列置換応答は、対話式生産性機能編集の入力要求と戻った表示を結び、運用状態を説明する文字列置換応答です。A: 一覧面観点の参照先はJob Data Set表示状態で、作業記録で追跡する対象は文字列置換棚卸です。B: 監査面観点の文字列置換定義は、入力名と画面内の置換 primary commandを結ぶ文字列置換照合です。C: 選択面観点の照合先はユーザーセッションログ根拠で、中心は文字列置換監査です。D: 応答面観点の処理段階はコマンドヘルプ表示応答で、入力と表示を結ぶ対象は文字列置換引継ぎです。投入面観点の用語定義として、文字列置換とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む文字列置換復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide CHANGE

    ---

    **問題.** 投入面の終了キー終了を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って終了キー 終了 keyを確認する場合、この状況で優先する項目はどれですか。

    - A. FREE DDNAME
    - B. OUTDES
    - C. PF3 END ✅
    - D. ISPF option 3.3 Move Copy

    正解: **C** ／ 難易度: 初級

    **解説:** 応答面観点の出力確認として終了キー終了状態を読み、答えはCで、照合焦点は終了キー終了定義です。出力面観点の終了キー終了根拠は、現在のパネルから前画面へ戻ることを満たす入力、画面、応答を同じ証跡で確認する終了キー終了根拠です。編集面観点で残す終了キー終了応答は、終了キー 終了 keyをコマンドまたはパネル形式と照合する終了キー終了応答です。投入面観点の終了キー終了保守は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する終了キー終了保守です。A: 監査面観点の比較先はDD名解放定義で、要求対象は終了キー終了監査です。B: 選択面観点の照合先は出力記述子作成根拠で、中心は終了キー終了引継ぎです。C: 照合面観点の終了キー終了応答は、入力名と画面内の終了キー 終了 keyを結ぶ終了キー終了報告です。D: 表示面観点の参照先はMOVE/COPY保守で、作業記録で追跡する対象は終了キー終了復旧です。検索面観点の用語定義として、終了キー終了とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む終了キー終了照合です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide END PF key

    ---

    **問題.** 検索面のヘルプキー表示を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってヘルプキー ヘルプ keyを確認する場合、証跡として中心に置く項目はどれですか。

    - A. LOG and LIST disposition
    - B. SDSF S output data set
    - C. SDSF P purge
    - D. PF1 HELP ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 管理面観点のヘルプキー表示定義は正答Dで、表記上の手掛かりはヘルプキー ヘルプ根拠です。投入面観点のヘルプキー表示応答は、現在パネルに対応するチュートリアルやヘルプを表示することを満たす入力、画面、応答を同じ証跡で確認するヘルプキー表示応答です。端末面観点で読むヘルプキー表示保守は、ヘルプキー ヘルプ keyを資料のコマンド形式やパネル形式と照合するヘルプキー表示保守です。検索面観点のヘルプキー表示監査は、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明するヘルプキー表示監査です。A: 選択面観点の照合先はログリスト処理根拠で、中心はヘルプキー表示棚卸です。B: 応答面観点の処理段階は出力データセット表示応答で、入力と表示を結ぶ対象はヘルプキー表示復旧です。C: 表示面観点の参照先はジョブ取消と出力削除保守で、作業記録で追跡する対象はヘルプキー表示照合です。D: 管理面観点のヘルプキー表示監査は、入力名と画面内のヘルプキー ヘルプ keyを結ぶヘルプキー表示選択です。通信面観点の用語定義として、ヘルプキー表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むヘルプキー表示報告です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide HELP PF key

    ---

    **問題.** 通信面の画面分割を引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って画面分割 and SWAP behaviorを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF SPLIT screen ✅
    - B. OUTDES
    - C. ISPF option 3.2 Data Set Utility
    - D. PF3 END

    正解: **A** ／ 難易度: 上級

    **解説:** 応答面観点で読む画面分割根拠は正答位置Aで、記録する焦点は対話式生産性機能 画面分割 screen応答です。検索面観点の画面分割保守は、複数論理画面を切り替えて作業することを満たす入力、画面、応答を同じ証跡で確認する画面分割保守です。編集面観点の画面分割監査は、画面分割 and SWAP behaviorを入力記録と合わせて処理対象を見分ける画面分割監査です。通信面観点の画面分割引継ぎは、対話式生産性機能基本操作の入力要求と戻った表示を結び、運用状態を説明する画面分割引継ぎです。A: 照合面観点の画面分割応答は、入力名と画面内の画面分割 and SWAP behaviorを結ぶ画面分割反映です。B: 表示面観点の参照先は出力記述子作成保守で、作業記録で追跡する対象は画面分割報告です。C: 管理面観点の比較先はData Set Utility監査で、要求対象は画面分割棚卸です。D: 制御面観点の照合先は終了キー終了引継ぎで、中心は画面分割復旧です。操作面観点の用語定義として、画面分割とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む画面分割選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide split screen

    ---

    **問題.** 操作面のログリスト処理を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってログ and リスト disposition パネルを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF ULOG
    - B. LOG and LIST disposition ✅
    - C. PROFILE MSGID
    - D. SEND USER

    正解: **B** ／ 難易度: 中級

    **解説:** 端末面観点の資料照合としてログリスト処理応答を選び、答えはBで、記録焦点はログリスト処理保守です。通信面観点のログリスト処理監査は、対話式生産性機能終了時のログ/リスト出力を印刷または削除することを満たす入力、画面、応答を同じ証跡で確認するログリスト処理監査です。投入面観点から見るログリスト処理引継ぎは、ログ and リスト disposition パネルを応答画面と対応させるログリスト処理引継ぎです。操作面観点のログリスト処理棚卸は、対話式生産性機能終了の入力要求と戻った表示を結び、運用状態を説明するログリスト処理棚卸です。A: 表示面観点の参照先はユーザーセッションログ保守で、作業記録で追跡する対象はログリスト処理選択です。B: 管理面観点のログリスト処理監査は、入力名と画面内のログ and リスト disposition パネルを結ぶログリスト処理観点です。C: 制御面観点の照合先はメッセージID表示引継ぎで、中心はログリスト処理照合です。D: 編集面観点の処理段階は短文メッセージ送信棚卸で、入力と表示を結ぶ対象はログリスト処理報告です。確認面観点の用語定義として、ログリスト処理とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むログリスト処理反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / ISPF User's Guide LOG LIST disposition

    ---

    **問題.** 監査面の実行中利用者表示を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って実行中表示 パネル and 実行中アドレス空間を確認する場合、この状況で優先する項目はどれですか。

    - A. PF1 HELP
    - B. SDSF ? JDS
    - C. SDSF slash MVS command
    - D. SDSF DA panel ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 端末面観点の実行中利用者表示監査は正答Dで、表記上の手掛かりはスプール表示検索機能 実行中表示 パネル引継ぎです。確認面観点の実行中利用者表示棚卸は、実行中アドレス空間やジョブの状態を確認することを満たす入力、画面、応答を同じ証跡で確認する実行中利用者表示棚卸です。投入面観点で読む実行中利用者表示復旧は、実行中表示 パネル and 実行中アドレス空間を資料のコマンド形式やパネル形式と照合する実行中利用者表示復旧です。監査面観点の実行中利用者表示照合は、スプール表示検索機能ジョブ管理の入力要求と戻った表示を結び、運用状態を説明する実行中利用者表示照合です。A: 制御面観点の照合先はヘルプキー表示引継ぎで、中心は実行中利用者表示選択です。B: 編集面観点の処理段階はJob Data Set表示棚卸で、入力と表示を結ぶ対象は実行中利用者表示反映です。C: 検索面観点の参照先はMVSコマンド発行復旧で、作業記録で追跡する対象は実行中利用者表示観点です。D: 端末面観点の実行中利用者表示照合は、入力名と画面内の実行中表示 パネル and 実行中アドレス空間を結ぶ実行中利用者表示読取です。保存面観点の用語定義として、実行中利用者表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む実行中利用者表示証跡です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide DA panel

    ---

    **問題.** 保存面のInput Queueを証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使ってI パネル job queueを確認する場合、証跡として中心に置く項目はどれですか。

    - A. SDSF I panel ✅
    - B. HELP command
    - C. SEND USER
    - D. ISPF option 1 BROWSE

    正解: **A** ／ 難易度: 中級

    **解説:** 編集面観点で読むInput Queue引継ぎは正答位置Aで、記録する焦点はスプール表示検索機能 I パネル棚卸です。監査面観点のInput Queue復旧は、入力キュー上または実行中ジョブを確認することを満たす入力、画面、応答を同じ証跡で確認するInput Queue復旧です。通信面観点のInput Queue照合は、I パネル job queueを入力記録と合わせて処理対象を見分けるInput Queue照合です。保存面観点のInput Queue報告は、スプール表示検索機能キューの入力要求と戻った表示を結び、運用状態を説明するInput Queue報告です。A: 応答面観点のInput Queue棚卸は、入力名と画面内のI パネル job queueを結ぶInput Queue状態です。B: 検索面観点の参照先はコマンドヘルプ表示復旧で、作業記録で追跡する対象はInput Queue証跡です。C: 端末面観点の比較先は短文メッセージ送信照合で、要求対象はInput Queue選択です。D: 出力面観点の照合先は表示選択報告で、中心はInput Queue反映です。照合面観点の用語定義として、Input Queueとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むInput Queue読取です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide Input Queue

    ---

    **問題.** 照合面のOutput Queueを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使ってO パネル output queueを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. ISPF EDIT SUBMIT
    - B. SDSF O panel ✅
    - C. SDSF ST panel
    - D. SDSF SORT

    正解: **B** ／ 難易度: 中級

    **解説:** 投入面観点の資料照合としてOutput Queue棚卸を選び、答えはBで、記録焦点はOutput Queue復旧です。保存面観点のOutput Queue照合は、JES2出力キューのジョブ出力を確認することを満たす入力、画面、応答を同じ証跡で確認するOutput Queue照合です。確認面観点から見るOutput Queue報告は、O パネル output queueを応答画面と対応させるOutput Queue報告です。照合面観点のOutput Queue選択は、スプール表示検索機能出力の入力要求と戻った表示を結び、運用状態を説明するOutput Queue選択です。A: 検索面観点の参照先はJCLサブミット復旧で、作業記録で追跡する対象はOutput Queue読取です。B: 端末面観点のOutput Queue照合は、入力名と画面内のO パネル output queueを結ぶOutput Queue定義です。C: 出力面観点の照合先はStatus パネル報告で、中心はOutput Queue観点です。D: 通信面観点の処理段階は列ソート選択で、入力と表示を結ぶ対象はOutput Queue証跡です。選択面観点の用語定義として、Output Queueとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むOutput Queue状態です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide Output Queue

    ---

    **問題.** 一覧面の出力データセット表示を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使ってS 行操作 and 出力表示を確認する場合、この状況で優先する項目はどれですか。

    - A. SDSF S output data set ✅
    - B. FREE DDNAME
    - C. OUTDES
    - D. ISPF option 3.3 Move Copy

    正解: **A** ／ 難易度: 初級

    **解説:** 通信面観点で読む出力データセット表示報告は正答位置Aで、記録する焦点はスプール表示検索機能 S 出力データセット選択です。管理面観点の出力データセット表示反映は、ジョブデータセット表示パネル上で個別出力データセットを表示することを満たす入力、画面、応答を同じ証跡で確認する出力データセット表示反映です。保存面観点の出力データセット表示観点は、S 行操作 and 出力表示を入力記録と合わせて処理対象を見分ける出力データセット表示観点です。一覧面観点の出力データセット表示証跡は、スプール表示検索機能出力参照の入力要求と戻った表示を結び、運用状態を説明する出力データセット表示証跡です。A: 編集面観点の出力データセット表示選択は、入力名と画面内のS 行操作 and 出力表示を結ぶ出力データセット表示保守です。B: 監査面観点の参照先はDD名解放反映で、作業記録で追跡する対象は出力データセット表示根拠です。C: 投入面観点の比較先は出力記述子作成観点で、要求対象は出力データセット表示読取です。D: 操作面観点の照合先はMOVE/COPY証跡で、中心は出力データセット表示状態です。応答面観点の用語定義として、出力データセット表示とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む出力データセット表示応答です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide output browse

    ---

    **問題.** 応答面のジョブ名接頭辞を証跡保存で確認します。入力内容と画面出力を同じ作業記録に残します。資料のコマンド形式、パネル名、または行コマンドを使って接頭辞 commandを確認する場合、証跡として中心に置く項目はどれですか。

    - A. ISPF option 2 EDIT
    - B. SDSF PREFIX ✅
    - C. ISPF EDIT SUBMIT
    - D. SDSF DA panel

    正解: **B** ／ 難易度: 中級

    **解説:** 確認面観点の資料照合としてジョブ名接頭辞選択を選び、答えはBで、記録焦点はジョブ名接頭辞反映です。一覧面観点のジョブ名接頭辞観点は、表示対象ジョブ名を接頭辞で絞り込むことを満たす入力、画面、応答を同じ証跡で確認するジョブ名接頭辞観点です。選択面観点から見るジョブ名接頭辞証跡は、接頭辞 commandを応答画面と対応させるジョブ名接頭辞証跡です。応答面観点のジョブ名接頭辞読取は、スプール表示検索機能フィルターの入力要求と戻った表示を結び、運用状態を説明するジョブ名接頭辞読取です。A: 監査面観点の参照先は編集選択反映で、作業記録で追跡する対象はジョブ名接頭辞応答です。B: 投入面観点のジョブ名接頭辞観点は、入力名と画面内の接頭辞 commandを結ぶジョブ名接頭辞監査です。C: 操作面観点の照合先はJCLサブミット証跡で、中心はジョブ名接頭辞定義です。D: 保存面観点の処理段階は実行中利用者表示読取で、入力と表示を結ぶ対象はジョブ名接頭辞根拠です。制御面観点の用語定義として、ジョブ名接頭辞とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ名接頭辞保守です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide PREFIX

    ---

    **問題.** 制御面の所有者絞り込みを引継ぎ確認で確認します。次の担当者が同じ画面を追える粒度で説明します。資料のコマンド形式、パネル名、または行コマンドを使って所有者 commandを確認する場合、引継ぎ対象として適切な項目はどれですか。

    - A. SDSF SORT
    - B. READY prompt
    - C. SDSF OWNER ✅
    - D. FREE DDNAME

    正解: **C** ／ 難易度: 中級

    **解説:** 保存面観点の出力確認として所有者絞り込み反映を読み、答えはCで、照合焦点は所有者絞り込み観点です。応答面観点の所有者絞り込み証跡は、ジョブ所有者で表示対象を制限することを満たす入力、画面、応答を同じ証跡で確認する所有者絞り込み証跡です。一覧面観点で残す所有者絞り込み読取は、所有者 commandをコマンドまたはパネル形式と照合する所有者絞り込み読取です。制御面観点の所有者絞り込み状態は、スプール表示検索機能フィルターの入力要求と戻った表示を結び、運用状態を説明する所有者絞り込み状態です。A: 投入面観点の比較先は列ソート観点で、要求対象は所有者絞り込み定義です。B: 操作面観点の照合先はREADYプロンプト確認証跡で、中心は所有者絞り込み根拠です。C: 通信面観点の所有者絞り込み読取は、入力名と画面内の所有者 commandを結ぶ所有者絞り込み引継ぎです。D: 管理面観点の参照先はDD名解放状態で、作業記録で追跡する対象は所有者絞り込み保守です。端末面観点の用語定義として、所有者絞り込みとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む所有者絞り込み監査です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide OWNER

    ---

    **問題.** 端末面の列ソートを定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってソート commandを確認する場合、どの項目を選ぶべきですか。

    - A. OUTDES
    - B. ISPF option 3.2 Data Set Utility
    - C. PF3 END
    - D. SDSF SORT ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 確認面観点の列ソート観点は正答Dで、表記上の手掛かりはスプール表示検索機能 ソート証跡です。制御面観点の列ソート読取は、表形式パネルの列を基準に並べ替えることを満たす入力、画面、応答を同じ証跡で確認する列ソート読取です。選択面観点で読む列ソート状態は、ソート commandを資料のコマンド形式やパネル形式と照合する列ソート状態です。端末面観点の列ソート定義は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する列ソート定義です。A: 操作面観点の照合先は出力記述子作成証跡で、中心は列ソート応答です。B: 保存面観点の処理段階はData Set Utility読取で、入力と表示を結ぶ対象は列ソート保守です。C: 管理面観点の参照先は終了キー終了状態で、作業記録で追跡する対象は列ソート監査です。D: 確認面観点の列ソート定義は、入力名と画面内のソート commandを結ぶ列ソート棚卸です。表示面観点の用語定義として、列ソートとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む列ソート引継ぎです。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide SORT

    ---

    **問題.** 表示面の条件フィルターを操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってフィルター commandを確認する場合、最も適切な確認対象はどれですか。

    - A. SDSF FILTER ✅
    - B. SDSF S output data set
    - C. SDSF P purge
    - D. LISTDS MEMBERS

    正解: **A** ／ 難易度: 上級

    **解説:** 保存面観点で読む条件フィルター証跡は正答位置Aで、記録する焦点はスプール表示検索機能 フィルター読取です。端末面観点の条件フィルター状態は、列値条件で表示行を絞り込むことを満たす入力、画面、応答を同じ証跡で確認する条件フィルター状態です。一覧面観点の条件フィルター定義は、フィルター commandを入力記録と合わせて処理対象を見分ける条件フィルター定義です。表示面観点の条件フィルター根拠は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する条件フィルター根拠です。A: 通信面観点の条件フィルター読取は、入力名と画面内のフィルター commandを結ぶ条件フィルター復旧です。B: 管理面観点の参照先は出力データセット表示状態で、作業記録で追跡する対象は条件フィルター引継ぎです。C: 確認面観点の比較先はジョブ取消と出力削除定義で、要求対象は条件フィルター応答です。D: 照合面観点の照合先はメンバー一覧表示根拠で、中心は条件フィルター保守です。編集面観点の用語定義として、条件フィルターとはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む条件フィルター棚卸です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide FILTER

    ---

    **問題.** 編集面の列配置変更を表示確認で確認します。応答画面または表形式パネルから状態を読み取ります。資料のコマンド形式、パネル名、または行コマンドを使って列配置 commandを確認する場合、この状況で優先する項目はどれですか。

    - A. OUTDES
    - B. SDSF ARRANGE ✅
    - C. ISPF option 3.2 Data Set Utility
    - D. PF3 END

    正解: **B** ／ 難易度: 上級

    **解説:** 選択面観点の資料照合として列配置変更読取を選び、答えはBで、記録焦点は列配置変更状態です。表示面観点の列配置変更定義は、パネル列の順序や幅を調整することを満たす入力、画面、応答を同じ証跡で確認する列配置変更定義です。制御面観点から見る列配置変更根拠は、列配置 commandを応答画面と対応させる列配置変更根拠です。編集面観点の列配置変更応答は、スプール表示検索機能表示調整の入力要求と戻った表示を結び、運用状態を説明する列配置変更応答です。A: 管理面観点の参照先は出力記述子作成状態で、作業記録で追跡する対象は列配置変更棚卸です。B: 確認面観点の列配置変更定義は、入力名と画面内の列配置 commandを結ぶ列配置変更照合です。C: 照合面観点の照合先はData Set Utility根拠で、中心は列配置変更監査です。D: 一覧面観点の処理段階は終了キー終了応答で、入力と表示を結ぶ対象は列配置変更引継ぎです。出力面観点の用語定義として、列配置変更とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読む列配置変更復旧です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide ARRANGE

    ---

    **問題.** 検索面のジョブ取消と出力削除を定義確認で確認します。入力画面と表示項目を読み取り、作業対象を確認します。資料のコマンド形式、パネル名、または行コマンドを使ってP action characterを確認する場合、どの項目を選ぶべきですか。

    - A. SDSF P purge ✅
    - B. SDSF DA panel
    - C. SDSF OWNER
    - D. LOGOFF command

    正解: **A** ／ 難易度: 上級

    **解説:** 一覧面観点で読むジョブ取消と出力削除根拠は正答位置Aで、記録する焦点はスプール表示検索機能 P purge応答です。投入面観点のジョブ取消と出力削除保守は、ジョブを取り消して出力をパージすることを満たす入力、画面、応答を同じ証跡で確認するジョブ取消と出力削除保守です。表示面観点のジョブ取消と出力削除監査は、P action characterを入力記録と合わせて処理対象を見分けるジョブ取消と出力削除監査です。検索面観点のジョブ取消と出力削除引継ぎは、スプール表示検索機能ジョブ操作の入力要求と戻った表示を結び、運用状態を説明するジョブ取消と出力削除引継ぎです。A: 保存面観点のジョブ取消と出力削除応答は、入力名と画面内のP action characterを結ぶジョブ取消と出力削除反映です。B: 端末面観点の参照先は実行中利用者表示保守で、作業記録で追跡する対象はジョブ取消と出力削除報告です。C: 選択面観点の比較先は所有者絞り込み監査で、要求対象はジョブ取消と出力削除棚卸です。D: 応答面観点の照合先はセッション終了引継ぎで、中心はジョブ取消と出力削除復旧です。通信面観点の用語定義として、ジョブ取消と出力削除とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ取消と出力削除選択です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide ST action characters

    ---

    **問題.** 通信面のジョブ保留を操作前確認で確認します。実行前にコマンド、パネル名、対象データを照合します。資料のコマンド形式、パネル名、または行コマンドを使ってH action characterを確認する場合、最も適切な確認対象はどれですか。

    - A. FREE DDNAME
    - B. SDSF H hold ✅
    - C. OUTDES
    - D. ISPF option 3.3 Move Copy

    正解: **B** ／ 難易度: 中級

    **解説:** 制御面観点の資料照合としてジョブ保留応答を選び、答えはBで、記録焦点はジョブ保留保守です。検索面観点のジョブ保留監査は、ジョブまたは出力を保留状態へ変更することを満たす入力、画面、応答を同じ証跡で確認するジョブ保留監査です。出力面観点から見るジョブ保留引継ぎは、H action characterを応答画面と対応させるジョブ保留引継ぎです。通信面観点のジョブ保留棚卸は、スプール表示検索機能ジョブ操作の入力要求と戻った表示を結び、運用状態を説明するジョブ保留棚卸です。A: 端末面観点の参照先はDD名解放保守で、作業記録で追跡する対象はジョブ保留選択です。B: 選択面観点のジョブ保留監査は、入力名と画面内のH action characterを結ぶジョブ保留観点です。C: 応答面観点の照合先は出力記述子作成引継ぎで、中心はジョブ保留照合です。D: 表示面観点の処理段階はMOVE/COPY棚卸で、入力と表示を結ぶ対象はジョブ保留報告です。操作面観点の用語定義として、ジョブ保留とはz/OSの対話操作、パネル操作、またはスプール表示で、入力と表示を対応させて状態を読むジョブ保留反映です。

    **出典:** zOS31_ikjc500.pdf z / OS TSO / E Command Reference / zOS31_ikjc200.pdf z / E User's Guide / zOS31_ikjp100.pdf z / OS ISPF User's Guide Vol I / zOS31_f54pc00.pdf z / OS ISPF Planning and Customizing / zOS31_isfa600.pdf z / OS SDSF User's Guide / zOS31_ieab500.pdf z / OS MVS JCL User's Guide / SDSF User's Guide DA action characters


??? note "検証手順（3件）"
    **COPY 順次から順次**

    - 検証目的: 出力検査の順次から順次について、COPY 順次から順次は、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、出力検査の順次から順次の確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY 順次から順次を指定し、OSKB010068の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY 順次から順次
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY 順次から順次
    CASE OSKB010068
    SOURCE TSO ISPF SDSF
    ```

    COPY 順次から順次とOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010068を同じ出力で読み、出力検査の順次から順次の根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010068
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010068
    COMMAND ===> SDSF DA
    ISF031I COPY 順次から順次 DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY 順次から順次 と OSKB010068 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

    ---

    **COPY PDS から PDS**

    - 検証目的: 条件検査のからについて、COPY PDS から PDS は、TSO / ISPF / SDSF の TSO_COPY で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、条件検査のからの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にCOPY PDS から PDSを指定し、OSKB010069の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND COPY PDS から PDS
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM COPY PDS から PDS
    CASE OSKB010069
    SOURCE TSO ISPF SDSF
    ```

    COPY PDS から PDSとOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010069を同じ出力で読み、条件検査のからの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010069
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010069
    COMMAND ===> SDSF DA
    ISF031I COPY PDS から PDS DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の COPY PDS から PDS と OSKB010069 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS DFSMSdfp Utilities (IEBCOPY)

    ---

    **SUBMIT 'など' オペランド**

    - 検証目的: 展開判定のなど オペランドについて、TSO ISPF SDSF の TSO_SUBMIT では、対象資源、指定値、実行時の出力を対応付けて確認します。TSO_SUBMIT は、TSO ISPF SDSF の運用で指定値に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: TSO/ISPFまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。
    - セッション環境: TSO/ISPFでSDSF DAを実行し、ISF031Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はTSO/ISPFのコマンド入力画面です。COMMAND INPUT ===> に SDSF DA を入力し、展開判定のなど オペランドの確認表示へ進みます。
    操作（入力）:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF)
    COMMAND INPUT ===> SDSF DA
    ```

    COMMAND INPUTにSDSF DAが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はTSO/ISPFの表示結果です。FIND欄にSUBMIT 'など' オペランドを指定し、OSKB010082の対象行を見つけます。
    操作（入力）:
    ```text
    (TSO/ISPF Result)
    COMMAND INPUT ===> FIND SUBMIT 'など' オペランド
    CASE OSKB010082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (TSO/ISPF Result)
    ITEM SUBMIT 'など' オペランド
    CASE OSKB010082
    SOURCE TSO ISPF SDSF
    ```

    SUBMIT 'など' オペランドとOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はTSO/ISPFの詳細表示です。ISF031IとOSKB010082を同じ出力で読み、展開判定のなど オペランドの根拠を記録します。
    操作（入力）:
    ```text
    (TSO/ISPF Detail)
    COMMAND INPUT ===> SDSF DA
    CASE OSKB010082
    → Enter を押す
    ```

    画面・出力:
    ```text
    TSO/ISPF PANEL OSKB010082
    COMMAND ===> SDSF DA
    ISF031I SUBMIT 'など' オペランド DISPLAY COMPLETED
    USERID OSKBUSR  PREFIX OSKB
    ```

    ISF031IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> SDSF DA が画面・出力に表示されること
    ② ステップ2 の SUBMIT 'など' オペランド と OSKB010082 が画面・出力に表示されること
    ③ ステップ3 の ISF031I と OSKB010082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference、z / OS MVS JCL User's Guide

