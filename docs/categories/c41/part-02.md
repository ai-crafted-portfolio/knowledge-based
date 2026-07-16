---
search:
  exclude: true
---

# 診断 (IPCS / Trace / ABEND) — 詳細 (2/2)

[← 診断 (IPCS / Trace / ABEND) の概要へ戻る](index.md)


## その他

### その他（特定項目に紐づかないQA・手順） {#c41-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? note "検証手順（265件）"
    **IPCS の位置付け 確認手順**

    - 検証目的: IPCS の位置付けについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00074のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000431
    CASE DGN00074
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00074が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **STATUS 確認手順**

    - 検証目的: STATUSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00075のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000432
    CASE DGN00075
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00075が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SUMMARY 確認手順**

    - 検証目的: SUMMARYについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00076のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000433
    CASE DGN00076
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00076が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX MTRACE 確認手順**

    - 検証目的: VERBX MTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00077のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000434
    CASE DGN00077
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00077が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX GRSTRACE 確認手順**

    - 検証目的: VERBX GRSTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00078のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000435
    CASE DGN00078
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00078が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **LIST 確認手順**

    - 検証目的: LISTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00079のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000436
    CASE DGN00079
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00079が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **NAME 確認手順**

    - 検証目的: NAMEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00080のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000437
    CASE DGN00080
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00080が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **EQUATE 確認手順**

    - 検証目的: EQUATEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00081のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000438
    CASE DGN00081
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00081が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **LISTDUMP 確認手順**

    - 検証目的: LISTDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00082のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000439
    CASE DGN00082
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00082が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **CTRACE 確認手順**

    - 検証目的: CTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00083のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043A
    CASE DGN00083
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00083が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **PRINT コマンド 確認手順**

    - 検証目的: PRINT コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00084のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043B
    CASE DGN00084
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00084が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS IPCS User's Guide

    ---

    **Symptom String 確認手順**

    - 検証目的: Symptom Stringについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00085のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043C
    CASE DGN00085
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00085が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS User's Guide、z / OS Problem Management

    ---

    **SDATA オペランド 確認手順**

    - 検証目的: SDATA オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00086のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043D
    CASE DGN00086
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00086が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **DUMP コマンド (オペレータ) 確認手順**

    - 検証目的: DUMP コマンド (オペレータ)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00087のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043E
    CASE DGN00087
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00087が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **AMDSADMP 確認手順**

    - 検証目的: AMDSADMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00088のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043F
    CASE DGN00088
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00088が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **SADMP 必要時 確認手順**

    - 検証目的: SADMP 必要時について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00089のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000440
    CASE DGN00089
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00089が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **ABDUMP とは 確認手順**

    - 検証目的: ABDUMP とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00090のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000441
    CASE DGN00090
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00090が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ABDUMP 抑止 確認手順**

    - 検証目的: ABDUMP 抑止について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00091のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000442
    CASE DGN00091
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00091が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **DAE とは 確認手順**

    - 検証目的: DAE とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00092のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000443
    CASE DGN00092
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00092が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (DAE)、z / OS MVS Initialization and Tuning Reference (ADYSETxx)

    ---

    **システムトレースとは 確認手順**

    - 検証目的: システムトレースとはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00093のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000444
    CASE DGN00093
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00093が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **MODE トレース 確認手順**

    - 検証目的: MODE トレースについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00094のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000445
    CASE DGN00094
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00094が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **GTF MODE 確認手順**

    - 検証目的: GTF MODEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00095のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000446
    CASE DGN00095
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00095が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **STOP GTF 確認手順**

    - 検証目的: STOP GTFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00096のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000447
    CASE DGN00096
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00096が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **CTRACE WTR (CTWTR) 確認手順**

    - 検証目的: CTRACE WTR (CTWTR)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00097のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000448
    CASE DGN00097
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00097が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSOMVS 確認手順**

    - 検証目的: SYSOMVSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00098のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000449
    CASE DGN00098
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00098が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSGRS 確認手順**

    - 検証目的: SYSGRSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00099のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044A
    CASE DGN00099
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00099が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SLIP とは 確認手順**

    - 検証目的: SLIP とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00100のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044B
    CASE DGN00100
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00100が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP DISPLAY 確認手順**

    - 検証目的: SLIP DISPLAYについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00101のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044C
    CASE DGN00101
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00101が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ENABLE / DISABLE 確認手順**

    - 検証目的: ENABLE / DISABLEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00102のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044D
    CASE DGN00102
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00102が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **IGNORE オペランド 確認手順**

    - 検証目的: IGNORE オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00103のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044E
    CASE DGN00103
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00103が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ACTION オペランド 確認手順**

    - 検証目的: ACTION オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00104のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044F
    CASE DGN00104
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00104が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP イベント MSG 確認手順**

    - 検証目的: SLIP イベント MSGについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00105のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000450
    CASE DGN00105
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00105が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **S0C1 命令例外 確認手順**

    - 検証目的: S0C1 命令例外について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00106のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000451
    CASE DGN00106
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00106が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C5 addressing 確認手順**

    - 検証目的: S0C5 addressingについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00107のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000452
    CASE DGN00107
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00107が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C9 zero divide 確認手順**

    - 検証目的: S0C9 zero divideについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00108のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000453
    CASE DGN00108
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00108が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S122 オペレータ取消 確認手順**

    - 検証目的: S122 オペレータ取消について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00109のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000454
    CASE DGN00109
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00109が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S806 モジュール未検出 確認手順**

    - 検証目的: S806 モジュール未検出について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00110のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000455
    CASE DGN00110
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00110が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S837 ボリューム不足 確認手順**

    - 検証目的: S837 ボリューム不足について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00111のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000456
    CASE DGN00111
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00111が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S922 ステップ失敗継続 確認手順**

    - 検証目的: S922 ステップ失敗継続について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00112のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000457
    CASE DGN00112
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00112が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **SX13 / SX22 / SDxx 総称 確認手順**

    - 検証目的: SX13 / SX22 / SDxx 総称について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00113のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000458
    CASE DGN00113
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00113が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **U4038 COBOL ランタイム 確認手順**

    - 検証目的: U4038 COBOL ランタイムについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00114のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000459
    CASE DGN00114
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00114が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (User completion codes)、各サブシステム / ランタイム マニュアル

    ---

    **LOGREC とは 確認手順**

    - 検証目的: LOGREC とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00115のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045A
    CASE DGN00115
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00115が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP SOFT / HARD 制御文 確認手順**

    - 検証目的: EREP SOFT / HARD 制御文について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00116のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045B
    CASE DGN00116
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00116が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **ログストリーム LOGREC 確認手順**

    - 検証目的: ログストリーム LOGRECについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00117のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045C
    CASE DGN00117
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00117が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **ENQ コマンド (D GRS) 確認手順**

    - 検証目的: ENQ コマンド (D GRS)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00118のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045D
    CASE DGN00118
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00118が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **GRS リング/STAR 確認手順**

    - 検証目的: GRS リング/STARについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00119のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045E
    CASE DGN00119
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00119が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **REPLY コマンド 確認手順**

    - 検証目的: REPLY コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00120のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045F
    CASE DGN00120
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00120が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (REPLY / D R)、z / OS MVS Authorized Assembler Services Reference (WTOR)

    ---

    **Disabled Wait state 確認手順**

    - 検証目的: Disabled Wait stateについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00121のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000460
    CASE DGN00121
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00121が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Wait state codes)

    ---

    **TEST LIST 確認手順**

    - 検証目的: TEST LISTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00122のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000461
    CASE DGN00122
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00122が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TEST command)、z / E Programming Guide

    ---

    **_CEE_RUNOPTS 確認手順**

    - 検証目的: _CEE_RUNOPTSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00123のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000462
    CASE DGN00123
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00123が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **STATUS REGISTERS 確認手順**

    - 検証目的: STATUS REGISTERSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00001のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003E8
    CASE DGN00001
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00001が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **STATUS FAILDATA 確認手順**

    - 検証目的: STATUS FAILDATAについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00002のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003E9
    CASE DGN00002
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00002が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **STATUS WORKSHEET 確認手順**

    - 検証目的: STATUS WORKSHEETについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00003のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003EA
    CASE DGN00003
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00003が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SUMMARY 確認手順**

    - 検証目的: SUMMARYについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00004のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003EB
    CASE DGN00004
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00004が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SUMMARY FORMAT 確認手順**

    - 検証目的: SUMMARY FORMATについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00005のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003EC
    CASE DGN00005
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00005が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SUMMARY TCBERROR 確認手順**

    - 検証目的: SUMMARY TCBERRORについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00006のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003ED
    CASE DGN00006
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00006が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX 確認手順**

    - 検証目的: VERBXについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00007のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003EE
    CASE DGN00007
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00007が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX MTRACE 確認手順**

    - 検証目的: VERBX MTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00008のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003EF
    CASE DGN00008
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00008が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX LOGDATA 確認手順**

    - 検証目的: VERBX LOGDATAについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00009のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F0
    CASE DGN00009
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00009が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX SUMDUMP 確認手順**

    - 検証目的: VERBX SUMDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00010のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F1
    CASE DGN00010
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00010が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX VSMDATA 確認手順**

    - 検証目的: VERBX VSMDATAについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00011のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F2
    CASE DGN00011
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00011が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX GRSTRACE 確認手順**

    - 検証目的: VERBX GRSTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00012のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F3
    CASE DGN00012
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00012が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX RSMDATA 確認手順**

    - 検証目的: VERBX RSMDATAについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00013のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F4
    CASE DGN00013
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00013が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX TCBERROR 確認手順**

    - 検証目的: VERBX TCBERRORについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00014のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F5
    CASE DGN00014
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00014が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **VERBX BPXMTRCE 確認手順**

    - 検証目的: VERBX BPXMTRCEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00015のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F6
    CASE DGN00015
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00015が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **LIST 確認手順**

    - 検証目的: LISTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00016のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F7
    CASE DGN00016
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00016が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **LIST 構造化表示 確認手順**

    - 検証目的: LIST 構造化表示について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00017のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F8
    CASE DGN00017
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00017が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **FIND 確認手順**

    - 検証目的: FINDについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00018のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003F9
    CASE DGN00018
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00018が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **WHERE 確認手順**

    - 検証目的: WHEREについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00019のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003FA
    CASE DGN00019
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00019が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **NAME 確認手順**

    - 検証目的: NAMEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00020のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003FB
    CASE DGN00020
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00020が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **EVALUATE 確認手順**

    - 検証目的: EVALUATEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00021のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003FC
    CASE DGN00021
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00021が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **COPYDUMP 確認手順**

    - 検証目的: COPYDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00022のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003FD
    CASE DGN00022
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00022が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SCAN / DROPDUMP 確認手順**

    - 検証目的: SCAN / DROPDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00023のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003FE
    CASE DGN00023
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00023が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **EQUATE 確認手順**

    - 検証目的: EQUATEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00024のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800003FF
    CASE DGN00024
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00024が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **NOTE / DELETE 確認手順**

    - 検証目的: NOTE / DELETEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00025のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000400
    CASE DGN00025
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00025が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **OPEN / CLOSE 確認手順**

    - 検証目的: OPEN / CLOSEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00026のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000401
    CASE DGN00026
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00026が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SELECT 確認手順**

    - 検証目的: SELECTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00027のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000402
    CASE DGN00027
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00027が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **LISTDUMP 確認手順**

    - 検証目的: LISTDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00028のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000403
    CASE DGN00028
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00028が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SYSTRACE 確認手順**

    - 検証目的: SYSTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00029のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000404
    CASE DGN00029
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00029が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SYSTRACE ALL 確認手順**

    - 検証目的: SYSTRACE ALLについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00030のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000405
    CASE DGN00030
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00030が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **SYSTRACE ASID/TIME 確認手順**

    - 検証目的: SYSTRACE ASID/TIMEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00031のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000406
    CASE DGN00031
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00031が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **CTRACE 確認手順**

    - 検証目的: CTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00032のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000407
    CASE DGN00032
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00032が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **RUNCHAIN 確認手順**

    - 検証目的: RUNCHAINについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00033のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000408
    CASE DGN00033
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00033が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS Diagnosis: Reference

    ---

    **PROFILE コマンド 確認手順**

    - 検証目的: PROFILE コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00034のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000409
    CASE DGN00034
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00034が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS IPCS User's Guide

    ---

    **RFIND / LOCATE 確認手順**

    - 検証目的: RFIND / LOCATEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00035のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000040A
    CASE DGN00035
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00035が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS IPCS User's Guide

    ---

    **PRINT コマンド 確認手順**

    - 検証目的: PRINT コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00036のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000040B
    CASE DGN00036
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00036が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS IPCS User's Guide

    ---

    **BLSCDDIR ディレクトリ 確認手順**

    - 検証目的: BLSCDDIR ディレクトリについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00037のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000040C
    CASE DGN00037
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00037が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS IPCS User's Guide

    ---

    **DSNAME 既定の優先順位 確認手順**

    - 検証目的: DSNAME 既定の優先順位について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00038のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000040D
    CASE DGN00038
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00038が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS Commands、z / OS MVS IPCS User's Guide

    ---

    **Dump Inventory / Problem 番号 確認手順**

    - 検証目的: Dump Inventory / Problem 番号について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00039のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000040E
    CASE DGN00039
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00039が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS User's Guide、z / OS Problem Management

    ---

    **Symptom String 確認手順**

    - 検証目的: Symptom Stringについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00040のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000040F
    CASE DGN00040
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00040が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS User's Guide、z / OS Problem Management

    ---

    **DAE 連携 確認手順**

    - 検証目的: DAE 連携について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00041のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000410
    CASE DGN00041
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00041が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS User's Guide、z / OS Problem Management

    ---

    **SVC Dump とは 確認手順**

    - 検証目的: SVC Dump とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00042のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000411
    CASE DGN00042
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00042が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **SDUMPX マクロ 確認手順**

    - 検証目的: SDUMPX マクロについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00043のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000412
    CASE DGN00043
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00043が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **SDATA オペランド 確認手順**

    - 検証目的: SDATA オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00044のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000413
    CASE DGN00044
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00044が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **SDUMP の出力先 確認手順**

    - 検証目的: SDUMP の出力先について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00045のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000414
    CASE DGN00045
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00045が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **DUMPDS コマンド 確認手順**

    - 検証目的: DUMPDS コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00046のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000415
    CASE DGN00046
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00046が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **CHNGDUMP コマンド 確認手順**

    - 検証目的: CHNGDUMP コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00047のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000416
    CASE DGN00047
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00047が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **DUMP コマンド (オペレータ) 確認手順**

    - 検証目的: DUMP コマンド (オペレータ)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00048のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000417
    CASE DGN00048
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00048が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **MAXSPACE 確認手順**

    - 検証目的: MAXSPACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00049のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000418
    CASE DGN00049
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00049が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **SUMDUMP 確認手順**

    - 検証目的: SUMDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00050のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000419
    CASE DGN00050
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00050が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids、z / OS MVS System Commands (DUMP / CHNGDUMP / DUMPDS)

    ---

    **SADMP とは 確認手順**

    - 検証目的: SADMP とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00051のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000041A
    CASE DGN00051
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00051が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **AMDSADMP 確認手順**

    - 検証目的: AMDSADMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00052のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000041B
    CASE DGN00052
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00052が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **SADMP 出力データセット 確認手順**

    - 検証目的: SADMP 出力データセットについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00053のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000041C
    CASE DGN00053
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00053が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **IPL 手順 確認手順**

    - 検証目的: IPL 手順について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00054のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000041D
    CASE DGN00054
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00054が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **SADMP プロンプト 確認手順**

    - 検証目的: SADMP プロンプトについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00055のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000041E
    CASE DGN00055
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00055が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **SADMP 必要時 確認手順**

    - 検証目的: SADMP 必要時について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00056のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000041F
    CASE DGN00056
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00056が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **SADMP 解析 確認手順**

    - 検証目的: SADMP 解析について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00057のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000420
    CASE DGN00057
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00057が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Stand-alone dump / AMDSADMP)

    ---

    **Transaction Dump とは 確認手順**

    - 検証目的: Transaction Dump とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00058のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000421
    CASE DGN00058
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00058が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Transaction dump / IEATDUMP)

    ---

    **CICS Transaction Dump 確認手順**

    - 検証目的: CICS Transaction Dumpについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00059のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000422
    CASE DGN00059
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00059が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Transaction dump / IEATDUMP)

    ---

    **ABDUMP とは 確認手順**

    - 検証目的: ABDUMP とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00060のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000423
    CASE DGN00060
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00060が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SYSUDUMP DD 確認手順**

    - 検証目的: SYSUDUMP DDについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00061のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000424
    CASE DGN00061
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00061が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SYSABEND DD 確認手順**

    - 検証目的: SYSABEND DDについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00062のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000425
    CASE DGN00062
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00062が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SYSMDUMP DD 確認手順**

    - 検証目的: SYSMDUMP DDについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00063のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000426
    CASE DGN00063
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00063が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ABDUMP 抑止 確認手順**

    - 検証目的: ABDUMP 抑止について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00064のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000427
    CASE DGN00064
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00064が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **IEAABD00 (SYSABEND) 確認手順**

    - 検証目的: IEAABD00 (SYSABEND)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00065のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000428
    CASE DGN00065
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00065が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **IEADMP00 (SYSUDUMP) 確認手順**

    - 検証目的: IEADMP00 (SYSUDUMP)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00066のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000429
    CASE DGN00066
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00066が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **IEADMR00 (SYSMDUMP) 確認手順**

    - 検証目的: IEADMR00 (SYSMDUMP)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00067のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000042A
    CASE DGN00067
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00067が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (Special DD)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **DAE とは 確認手順**

    - 検証目的: DAE とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00068のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000042B
    CASE DGN00068
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00068が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (DAE)、z / OS MVS Initialization and Tuning Reference (ADYSETxx)

    ---

    **DAE データセット 確認手順**

    - 検証目的: DAE データセットについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00069のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000042C
    CASE DGN00069
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00069が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (DAE)、z / OS MVS Initialization and Tuning Reference (ADYSETxx)

    ---

    **ADYSETxx / SET DAE / D DAE 確認手順**

    - 検証目的: ADYSETxx / SET DAE / D DAEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00070のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000042D
    CASE DGN00070
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00070が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (DAE)、z / OS MVS Initialization and Tuning Reference (ADYSETxx)

    ---

    **DAE 抑止ロジック 確認手順**

    - 検証目的: DAE 抑止ロジックについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00071のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000042E
    CASE DGN00071
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00071が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (DAE)、z / OS MVS Initialization and Tuning Reference (ADYSETxx)

    ---

    **システムトレースとは 確認手順**

    - 検証目的: システムトレースとはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00072のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000042F
    CASE DGN00072
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00072が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **TRACE ST,nnnK 確認手順**

    - 検証目的: TRACE ST,nnnKについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00073のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000430
    CASE DGN00073
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00073が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **TRACE ST,ON/OFF 確認手順**

    - 検証目的: TRACE ST,ON/OFFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00074のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000431
    CASE DGN00074
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00074が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **BRANCH トレース 確認手順**

    - 検証目的: BRANCH トレースについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00075のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000432
    CASE DGN00075
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00075が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **MODE トレース 確認手順**

    - 検証目的: MODE トレースについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00076のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000433
    CASE DGN00076
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00076が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **SYSTRACE 表示 確認手順**

    - 検証目的: SYSTRACE 表示について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00077のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000434
    CASE DGN00077
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00077が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (System trace)、z / OS MVS System Commands (TRACE ST)

    ---

    **GTF とは 確認手順**

    - 検証目的: GTF とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00078のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000435
    CASE DGN00078
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00078が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **START GTF 確認手順**

    - 検証目的: START GTFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00079のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000436
    CASE DGN00079
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00079が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **GTF MODE 確認手順**

    - 検証目的: GTF MODEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00080のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000437
    CASE DGN00080
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00080が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **GTF TRACE オプション 確認手順**

    - 検証目的: GTF TRACE オプションについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00081のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000438
    CASE DGN00081
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00081が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **GTF SLIP イベント 確認手順**

    - 検証目的: GTF SLIP イベントについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00082のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000439
    CASE DGN00082
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00082が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **GTF JOBNAME フィルタ 確認手順**

    - 検証目的: GTF JOBNAME フィルタについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00083のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043A
    CASE DGN00083
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00083が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **STOP GTF 確認手順**

    - 検証目的: STOP GTFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00084のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043B
    CASE DGN00084
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00084が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **AMDPRDMP / IPCS GTFTRACE 確認手順**

    - 検証目的: AMDPRDMP / IPCS GTFTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00085のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043C
    CASE DGN00085
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00085が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (GTF)、z / OS MVS System Commands (TRACE)

    ---

    **Component Trace とは 確認手順**

    - 検証目的: Component Trace とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00086のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043D
    CASE DGN00086
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00086が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **TRACE CT コマンド 確認手順**

    - 検証目的: TRACE CT コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00087のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043E
    CASE DGN00087
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00087が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **CTRACE WTR (CTWTR) 確認手順**

    - 検証目的: CTRACE WTR (CTWTR)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00088のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000043F
    CASE DGN00088
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00088が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **TRACE CT,OFF 確認手順**

    - 検証目的: TRACE CT,OFFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00089のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000440
    CASE DGN00089
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00089が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **CTIxxxxxx PARMLIB 確認手順**

    - 検証目的: CTIxxxxxx PARMLIBについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00090のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000441
    CASE DGN00090
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00090が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSTCPIP 確認手順**

    - 検証目的: SYSTCPIPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00091のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000442
    CASE DGN00091
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00091が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSOMVS 確認手順**

    - 検証目的: SYSOMVSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00092のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000443
    CASE DGN00092
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00092が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSXCF 確認手順**

    - 検証目的: SYSXCFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00093のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000444
    CASE DGN00093
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00093が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSRSM 確認手順**

    - 検証目的: SYSRSMについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00094のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000445
    CASE DGN00094
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00094が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSRRS 確認手順**

    - 検証目的: SYSRRSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00095のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000446
    CASE DGN00095
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00095が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSGRS 確認手順**

    - 検証目的: SYSGRSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00096のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000447
    CASE DGN00096
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00096が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSLOGR 確認手順**

    - 検証目的: SYSLOGRについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00097のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000448
    CASE DGN00097
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00097が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SYSWLM 確認手順**

    - 検証目的: SYSWLMについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00098のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000449
    CASE DGN00098
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00098が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **IPCS CTRACE 表示 確認手順**

    - 検証目的: IPCS CTRACE 表示について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00099のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044A
    CASE DGN00099
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00099が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Component trace)、z / OS MVS System Commands (TRACE CT)

    ---

    **SLIP とは 確認手順**

    - 検証目的: SLIP とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00100のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044B
    CASE DGN00100
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00100が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP SET 確認手順**

    - 検証目的: SLIP SETについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00101のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044C
    CASE DGN00101
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00101が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP MOD 確認手順**

    - 検証目的: SLIP MODについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00102のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044D
    CASE DGN00102
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00102が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP DELETE 確認手順**

    - 検証目的: SLIP DELETEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00103のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044E
    CASE DGN00103
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00103が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP DISPLAY 確認手順**

    - 検証目的: SLIP DISPLAYについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00104のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000044F
    CASE DGN00104
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00104が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **COMP オペランド 確認手順**

    - 検証目的: COMP オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00105のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000450
    CASE DGN00105
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00105が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **REASON オペランド 確認手順**

    - 検証目的: REASON オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00106のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000451
    CASE DGN00106
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00106が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **EVENT オペランド 確認手順**

    - 検証目的: EVENT オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00107のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000452
    CASE DGN00107
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00107が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ENABLE / DISABLE 確認手順**

    - 検証目的: ENABLE / DISABLEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00108のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000453
    CASE DGN00108
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00108が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **MSGID オペランド 確認手順**

    - 検証目的: MSGID オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00109のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000454
    CASE DGN00109
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00109が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **JOBNAME / JOBLIST 確認手順**

    - 検証目的: JOBNAME / JOBLISTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00110のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000455
    CASE DGN00110
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00110が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **PROCESS オペランド 確認手順**

    - 検証目的: PROCESS オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00111のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000456
    CASE DGN00111
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00111が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **IGNORE オペランド 確認手順**

    - 検証目的: IGNORE オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00112のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000457
    CASE DGN00112
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00112が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ASIDLIST オペランド 確認手順**

    - 検証目的: ASIDLIST オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00113のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000458
    CASE DGN00113
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00113が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **PSWASC オペランド 確認手順**

    - 検証目的: PSWASC オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00114のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000459
    CASE DGN00114
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00114が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SADMP オペランド 確認手順**

    - 検証目的: SADMP オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00115のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045A
    CASE DGN00115
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00115が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **ACTION オペランド 確認手順**

    - 検証目的: ACTION オペランドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00116のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045B
    CASE DGN00116
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00116が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **STARTMATCH/ENDMATCH 確認手順**

    - 検証目的: STARTMATCH/ENDMATCHについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00117のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045C
    CASE DGN00117
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00117が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP イベント BR 確認手順**

    - 検証目的: SLIP イベント BRについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00118のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045D
    CASE DGN00118
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00118が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP イベント IF 確認手順**

    - 検証目的: SLIP イベント IFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00119のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045E
    CASE DGN00119
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00119が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP イベント MSG 確認手順**

    - 検証目的: SLIP イベント MSGについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00120のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000045F
    CASE DGN00120
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00120が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP イベント OPERLOG 確認手順**

    - 検証目的: SLIP イベント OPERLOGについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00121のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000460
    CASE DGN00121
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00121が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **SLIP イベント PSW / SYSPLEX / SVCERR / USERCMD 確認手順**

    - 検証目的: SLIP イベント PSW / SYSPLEX / SVCERR / USERCMDについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00122のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000461
    CASE DGN00122
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00122が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **PER との関連 確認手順**

    - 検証目的: PER との関連について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00123のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000462
    CASE DGN00123
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00123が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (SLIP command)、z / OS MVS Diagnosis: Tools and Service Aids

    ---

    **S0C1 命令例外 確認手順**

    - 検証目的: S0C1 命令例外について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00124のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000463
    CASE DGN00124
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00124が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C2 特権命令例外 確認手順**

    - 検証目的: S0C2 特権命令例外について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00125のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000464
    CASE DGN00125
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00125が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C3 実行例外 確認手順**

    - 検証目的: S0C3 実行例外について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00126のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000465
    CASE DGN00126
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00126が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00126 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C4 protection 確認手順**

    - 検証目的: S0C4 protectionについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00127のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000466
    CASE DGN00127
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00127が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00127 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C5 addressing 確認手順**

    - 検証目的: S0C5 addressingについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00128のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000467
    CASE DGN00128
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00128が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00128 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C6 specification 確認手順**

    - 検証目的: S0C6 specificationについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00129のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000468
    CASE DGN00129
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00129が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00129 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C7 数値変換 確認手順**

    - 検証目的: S0C7 数値変換について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00130のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000469
    CASE DGN00130
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00130が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00130 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C8 オーバフロー 確認手順**

    - 検証目的: S0C8 オーバフローについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00131のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000046A
    CASE DGN00131
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00131が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00131 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0C9 zero divide 確認手順**

    - 検証目的: S0C9 zero divideについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00132のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000046B
    CASE DGN00132
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00132が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00132 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0CA 10 進オーバフロー 確認手順**

    - 検証目的: S0CA 10 進オーバフローについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00133のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000046C
    CASE DGN00133
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00133が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00133 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0CB 10 進ゼロ除算 確認手順**

    - 検証目的: S0CB 10 進ゼロ除算について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00134のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000046D
    CASE DGN00134
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00134が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00134 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S0CC〜S0CF 浮動小数例外 確認手順**

    - 検証目的: S0CC〜S0CF 浮動小数例外について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00135のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000046E
    CASE DGN00135
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00135が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00135 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Program interruption / S0Cx)、z / Architecture Principles of Operations

    ---

    **S122 オペレータ取消 確認手順**

    - 検証目的: S122 オペレータ取消について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00136のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000046F
    CASE DGN00136
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00136が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00136 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S222 オペレータ取消 (NODUMP) 確認手順**

    - 検証目的: S222 オペレータ取消 (NODUMP)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00137のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000470
    CASE DGN00137
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00137が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00137 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S322 CPU タイム超過 確認手順**

    - 検証目的: S322 CPU タイム超過について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00138のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000471
    CASE DGN00138
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00138が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00138 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S522 Wait タイム超過 確認手順**

    - 検証目的: S522 Wait タイム超過について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00139のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000472
    CASE DGN00139
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00139が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00139 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S806 モジュール未検出 確認手順**

    - 検証目的: S806 モジュール未検出について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00140のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000473
    CASE DGN00140
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00140が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00140 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S80A 仮想記憶不足 (GETMAIN) 確認手順**

    - 検証目的: S80A 仮想記憶不足 (GETMAIN)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00141のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000474
    CASE DGN00141
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00141が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00141 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S813 DSN 不整合 確認手順**

    - 検証目的: S813 DSN 不整合について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00142のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000475
    CASE DGN00142
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00142が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00142 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S822 リージョン不足 確認手順**

    - 検証目的: S822 リージョン不足について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00143のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000476
    CASE DGN00143
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00143が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00143 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S837 ボリューム不足 確認手順**

    - 検証目的: S837 ボリューム不足について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00144のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000477
    CASE DGN00144
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00144が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00144 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S878 SQA/CSA 不足 確認手順**

    - 検証目的: S878 SQA/CSA 不足について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00145のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000478
    CASE DGN00145
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00145が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00145 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S913 アクセス権限不足 確認手順**

    - 検証目的: S913 アクセス権限不足について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00146のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000479
    CASE DGN00146
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00146が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00146 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S913 RACROUTE / Reason 確認手順**

    - 検証目的: S913 RACROUTE / Reasonについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00147のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000047A
    CASE DGN00147
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00147が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00147 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S922 ステップ失敗継続 確認手順**

    - 検証目的: S922 ステップ失敗継続について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00148のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000047B
    CASE DGN00148
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00148が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00148 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **SB37 EOV ボリューム不足 確認手順**

    - 検証目的: SB37 EOV ボリューム不足について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00149のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000047C
    CASE DGN00149
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00149が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00149 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **SD37 一次割当超過 (SECONDARY 未指定) 確認手順**

    - 検証目的: SD37 一次割当超過 (SECONDARY 未指定)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00150のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000047D
    CASE DGN00150
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00150が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00150 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **SE37 EXTENT 上限 確認手順**

    - 検証目的: SE37 EXTENT 上限について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00151のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000047E
    CASE DGN00151
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00151が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00151 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **SX13 / SX22 / SDxx 総称 確認手順**

    - 検証目的: SX13 / SX22 / SDxx 総称について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00152のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000047F
    CASE DGN00152
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00152が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00152 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S04E Db2 内部 abend 確認手順**

    - 検証目的: S04E Db2 内部 abendについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00153のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000480
    CASE DGN00153
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00153が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00153 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **S0F3 / S0F4 OS 内部 確認手順**

    - 検証目的: S0F3 / S0F4 OS 内部について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00154のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000481
    CASE DGN00154
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00154が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00154 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (System completion codes)

    ---

    **U コード総論 確認手順**

    - 検証目的: U コード総論について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00155のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000482
    CASE DGN00155
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00155が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00155 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (User completion codes)、各サブシステム / ランタイム マニュアル

    ---

    **U4038 COBOL ランタイム 確認手順**

    - 検証目的: U4038 COBOL ランタイムについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00156のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000483
    CASE DGN00156
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00156が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00156 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (User completion codes)、各サブシステム / ランタイム マニュアル

    ---

    **U0001 Db2 切断 確認手順**

    - 検証目的: U0001 Db2 切断について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00157のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000484
    CASE DGN00157
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00157が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00157 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (User completion codes)、各サブシステム / ランタイム マニュアル

    ---

    **U0476 / U0778 サブシステム 確認手順**

    - 検証目的: U0476 / U0778 サブシステムについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00158のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000485
    CASE DGN00158
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00158が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00158 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (User completion codes)、各サブシステム / ランタイム マニュアル

    ---

    **U1000 アプリ既定 確認手順**

    - 検証目的: U1000 アプリ既定について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00159のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000486
    CASE DGN00159
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00159が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00159 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (User completion codes)、各サブシステム / ランタイム マニュアル

    ---

    **LOGREC とは 確認手順**

    - 検証目的: LOGREC とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00160のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000487
    CASE DGN00160
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00160が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00160 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP とは 確認手順**

    - 検証目的: EREP とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00161のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000488
    CASE DGN00161
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00161が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00161 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP HIST 制御文 確認手順**

    - 検証目的: EREP HIST 制御文について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00162のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000489
    CASE DGN00162
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00162が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00162 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP EVENT 制御文 確認手順**

    - 検証目的: EREP EVENT 制御文について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00163のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000048A
    CASE DGN00163
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00163が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00163 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP SOFT / HARD 制御文 確認手順**

    - 検証目的: EREP SOFT / HARD 制御文について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00164のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000048B
    CASE DGN00164
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00164が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00164 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP TYPE 制御文 確認手順**

    - 検証目的: EREP TYPE 制御文について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00165のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000048C
    CASE DGN00165
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00165が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00165 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP SYSID 制御文 確認手順**

    - 検証目的: EREP SYSID 制御文について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00166のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000048D
    CASE DGN00166
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00166が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00166 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **EREP ACC=Y/N / IFCDIP00 確認手順**

    - 検証目的: EREP ACC=Y/N / IFCDIP00について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00167のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000048E
    CASE DGN00167
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00167が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00167 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **ログストリーム LOGREC 確認手順**

    - 検証目的: ログストリーム LOGRECについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00168のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000048F
    CASE DGN00168
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00168が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00168 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Tools and Service Aids (Recording logrec error records)、EREP User's Guide

    ---

    **DDS とは 確認手順**

    - 検証目的: DDS とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00169のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000490
    CASE DGN00169
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00169が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00169 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS User's Guide (Dump Display Services)

    ---

    **IPCS ISPF オプション 確認手順**

    - 検証目的: IPCS ISPF オプションについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00170のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000491
    CASE DGN00170
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00170が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00170 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS IPCS User's Guide (Dump Display Services)

    ---

    **GRS とは 確認手順**

    - 検証目的: GRS とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00171のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000492
    CASE DGN00171
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00171が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00171 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **ENQ コマンド (D GRS) 確認手順**

    - 検証目的: ENQ コマンド (D GRS)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00172のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000493
    CASE DGN00172
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00172が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00172 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **D GRS,ANALYZE 確認手順**

    - 検証目的: D GRS,ANALYZEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00173のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000494
    CASE DGN00173
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00173が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00173 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **VERBX GRSTRACE 確認手順**

    - 検証目的: VERBX GRSTRACEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00174のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000495
    CASE DGN00174
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00174が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00174 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **RESERVE 競合 確認手順**

    - 検証目的: RESERVE 競合について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00175のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000496
    CASE DGN00175
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00175が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00175 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **GRS リング/STAR 確認手順**

    - 検証目的: GRS リング/STARについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00176のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000497
    CASE DGN00176
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00176が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00176 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **IRLM ロック解析 確認手順**

    - 検証目的: IRLM ロック解析について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00177のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000498
    CASE DGN00177
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00177が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00177 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Planning: Global Resource Serialization、z / OS MVS System Commands (D GRS)

    ---

    **WTOR とは 確認手順**

    - 検証目的: WTOR とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00178のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 80000499
    CASE DGN00178
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00178が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00178 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (REPLY / D R)、z / OS MVS Authorized Assembler Services Reference (WTOR)

    ---

    **D R,L コマンド 確認手順**

    - 検証目的: D R,L コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00179のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000049A
    CASE DGN00179
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00179が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00179 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (REPLY / D R)、z / OS MVS Authorized Assembler Services Reference (WTOR)

    ---

    **REPLY コマンド 確認手順**

    - 検証目的: REPLY コマンドについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00180のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000049B
    CASE DGN00180
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00180が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00180 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (REPLY / D R)、z / OS MVS Authorized Assembler Services Reference (WTOR)

    ---

    **ZSYSCM (System Console Message) 確認手順**

    - 検証目的: ZSYSCM (System Console Message)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00181のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000049C
    CASE DGN00181
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00181が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00181 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Commands (REPLY / D R)、z / OS MVS Authorized Assembler Services Reference (WTOR)

    ---

    **Hard Wait state とは 確認手順**

    - 検証目的: Hard Wait state とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00182のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000049D
    CASE DGN00182
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00182が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00182 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Wait state codes)

    ---

    **Wait state code の見方 確認手順**

    - 検証目的: Wait state code の見方について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00183のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000049E
    CASE DGN00183
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00183が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00183 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Wait state codes)

    ---

    **Disabled Wait state 確認手順**

    - 検証目的: Disabled Wait stateについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00184のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 8000049F
    CASE DGN00184
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00184が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00184 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Wait state codes)

    ---

    **Restartable Wait state 確認手順**

    - 検証目的: Restartable Wait stateについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00185のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A0
    CASE DGN00185
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00185が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00185 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS System Codes (Wait state codes)

    ---

    **TSO TEST とは 確認手順**

    - 検証目的: TSO TEST とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00186のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A1
    CASE DGN00186
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00186が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00186 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TEST command)、z / E Programming Guide

    ---

    **TEST AT / IF 確認手順**

    - 検証目的: TEST AT / IFについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00187のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A2
    CASE DGN00187
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00187が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00187 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TEST command)、z / E Programming Guide

    ---

    **TEST LIST 確認手順**

    - 検証目的: TEST LISTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00188のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A3
    CASE DGN00188
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00188が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00188 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TEST command)、z / E Programming Guide

    ---

    **TEST GO/STEP 確認手順**

    - 検証目的: TEST GO/STEPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00189のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A4
    CASE DGN00189
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00189が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00189 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS TSO / E Command Reference (TEST command)、z / E Programming Guide

    ---

    **Language Environment とは 確認手順**

    - 検証目的: Language Environment とはについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00190のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A5
    CASE DGN00190
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00190が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00190 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEEDUMP 確認手順**

    - 検証目的: CEEDUMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00191のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A6
    CASE DGN00191
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00191が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00191 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **_CEE_RUNOPTS 確認手順**

    - 検証目的: _CEE_RUNOPTSについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00192のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A7
    CASE DGN00192
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00192が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00192 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEEROPT / CEEUOPT 確認手順**

    - 検証目的: CEEROPT / CEEUOPTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00193のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A8
    CASE DGN00193
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00193が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00193 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **LE TRAP ランオプション 確認手順**

    - 検証目的: LE TRAP ランオプションについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00194のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004A9
    CASE DGN00194
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00194が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00194 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **LE TRACE ランオプション 確認手順**

    - 検証目的: LE TRACE ランオプションについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00195のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004AA
    CASE DGN00195
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00195が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00195 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **TERMTHDACT 確認手順**

    - 検証目的: TERMTHDACTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00196のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004AB
    CASE DGN00196
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00196が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00196 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEE3xxx メッセージ全般 確認手順**

    - 検証目的: CEE3xxx メッセージ全般について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00197のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004AC
    CASE DGN00197
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00197が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00197 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEE3204S / CEE3207S / CEE3209S 確認手順**

    - 検証目的: CEE3204S / CEE3207S / CEE3209Sについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00198のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004AD
    CASE DGN00198
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00198が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00198 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEE3501S モジュール未検出 確認手順**

    - 検証目的: CEE3501S モジュール未検出について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00199のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004AE
    CASE DGN00199
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00199が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00199 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEE3DMP 確認手順**

    - 検証目的: CEE3DMPについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00200のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004AF
    CASE DGN00200
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00200が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00200 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **CEE3SPM ランオプション 確認手順**

    - 検証目的: CEE3SPM ランオプションについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00201のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B0
    CASE DGN00201
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00201が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00201 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **LANGCEE 過渡名 確認手順**

    - 検証目的: LANGCEE 過渡名について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00202のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B1
    CASE DGN00202
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00202が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00202 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS Language Environment Debugging Guide、z / OS Language Environment Programming Reference

    ---

    **RTM2WA 確認手順**

    - 検証目的: RTM2WAについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00203のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B2
    CASE DGN00203
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00203が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00203 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **ESTAE / ESPIE / FRR / SDWA 確認手順**

    - 検証目的: ESTAE / ESPIE / FRR / SDWAについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00204のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B3
    CASE DGN00204
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00204が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00204 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **Module/CSECT 識別 確認手順**

    - 検証目的: Module/CSECT 識別について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00205のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B4
    CASE DGN00205
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00205が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00205 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **Reason code (R15) 確認手順**

    - 検証目的: Reason code (R15)について、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00206のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B5
    CASE DGN00206
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00206が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00206 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **AMBLIST 確認手順**

    - 検証目的: AMBLISTについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00207のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B6
    CASE DGN00207
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00207が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00207 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **RACF ICH408I 確認手順**

    - 検証目的: RACF ICH408Iについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00208のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B7
    CASE DGN00208
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00208が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00208 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **IEF402I / IEF403I / IEF450I 確認手順**

    - 検証目的: IEF402I / IEF403I / IEF450Iについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00209のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B8
    CASE DGN00209
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00209が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00209 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **IEA995I 確認手順**

    - 検証目的: IEA995Iについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00210のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004B9
    CASE DGN00210
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00210が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00210 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **PSW フォーマット 確認手順**

    - 検証目的: PSW フォーマットについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00211のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004BA
    CASE DGN00211
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00211が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00211 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **Cross Memory / Linkage Stack 確認手順**

    - 検証目的: Cross Memory / Linkage Stackについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00212のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004BB
    CASE DGN00212
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00212が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00212 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **ASCB ⇆ JOBNAME 確認手順**

    - 検証目的: ASCB ⇆ JOBNAMEについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00213のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004BC
    CASE DGN00213
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00213が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00213 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **TCB チェーン 確認手順**

    - 検証目的: TCB チェーンについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00214のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004BD
    CASE DGN00214
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00214が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00214 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

    ---

    **OPERLOG / SYSLOG 確認手順**

    - 検証目的: OPERLOG / SYSLOGについて、IPCSコマンド、ダンプ題名、解析出力を机上で確認します。
    - 前提条件: IPCSダイアログを起動済みで、検証用ダンプデータセットを参照できる前提です。実機では権限と変更管理承認を得て検証用ダンプを使用します。
    - セッション環境: IPCSでDGN00215のダンプを開き、STATUS FAILDATAとSEARCH ARGUMENT ABSTRACTを確認します。

    **ステップ 1**
    現在の画面はIPCSの基本メニューです。OPTION ===> に 4 を入力し、IPCSサブコマンド入力画面へ移動します。
    操作（入力）:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS PRIMARY OPTION MENU)
    OPTION ===> 4
    ```

    OPTION ===> 4 が表示され、IPCSサブコマンドを入力する準備ができています。

    **ステップ 2**
    現在の画面はIPCSサブコマンド入力画面です。COMMAND INPUT ===> に STATUS FAILDATA を入力し、対象ダンプの解析出力を表示します。
    操作（入力）:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Subcommand Entry)
    COMMAND INPUT ===> STATUS FAILDATA
    ```

    COMMAND INPUTにSTATUS FAILDATAが表示され、対象の解析レポートを呼び出しています。

    **ステップ 3**
    現在の画面はIPCS解析レポート表示画面です。PF8を押して続きの行へ進み、メッセージ見出しと障害識別名を照合します。
    操作（入力）:
    ```text
    (IPCS Report Panel)
    COMMAND INPUT ===> STATUS FAILDATA
    PF8
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IPCS Report Panel)
    SEARCH ARGUMENT ABSTRACT
    ABEND CODE 0C4  REASON 00000004
    PSW AT TIME OF ERROR 078D1000 800004BE
    CASE DGN00215
    ```

    SEARCH ARGUMENT ABSTRACTとDGN00215が同じ出力に現れるため、対象診断項目の根拠として記録できます。

    - 合格条件: ① ステップ1 の OPTION ===> 4 が画面・出力に表示されること
    ② ステップ2 の STATUS FAILDATA が画面・出力に表示されること
    ③ ステップ3 の SEARCH ARGUMENT ABSTRACT と DGN00215 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS Diagnosis: Reference (RTM2WA / SDWA / AMBLIST)、z / OS MVS Data Areas

