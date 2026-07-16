---
search:
  exclude: true
---

# JCL JOB 文 — 詳細 (4/4)

[← JCL JOB 文 の概要へ戻る](index.md)


## その他

### その他（特定項目に紐づかないQA・手順） {#c19-other}

このカテゴリで項目名が個別の技術項目に一致しなかったQA・手順です。

??? question "確認問題（9問）"
    **問題.** 時間目的を引継ぎ資料に書く必要があります。標準JCLの見直しで明示指定と導入先の既定値を分けています。正しく説明している選択肢はどれですか。

    - A. 出力クラスの保留属性を指定する
    - B. 64-bit記憶域の上限を指定する
    - C. JCL構文チェックだけを実行する
    - D. CPU時間の上限を指定する ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dが正解です。時間目的の正答理由として、JOB文のTIMEは、ジョブ全体に許されるCPU時間の上限を指定します。誤答A時間目的はMSGCLASSの出力クラス指定で読む内容で、時間目的の指定値とは結び付かないため時間目的Aで区別します。誤答B時間目的はMEMLIMITによる64-bit記憶域制御を扱う説明で、JOB 文 TIME の目的の根拠にならないため時間目的Bとして外します。誤答C時間目的はTYPRUN=SCANのJCL検査を説明しており、JOB 文 TIME の目的の判断点とは見る欄が違うことを時間目的Cで分けます。時間目的で項目「JOB 文 TIME の目的」を見る際は、似たパラメータ名と混同しやすいため効く対象を先に確認します。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 分秒構文を説明する資料に載せる文を選んでいます。障害調査でJESJCLとジョブログの出方を突き合わせています。正しいものはどれですか。

    - A. 戻りコードと演算子を組で指定する
    - B. 出力クラスと保留属性を組で指定する
    - C. 記憶域のMB値とGB値を組で指定する
    - D. 分と秒を組で指定する ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dが正解です。分秒構文の正答理由として、TIME=(mm,ss)は、分と秒の組でCPU時間上限を指定する形式です。誤答A分秒構文はCONDによる戻りコード制御に関する内容で、分秒構文の確認対象ではないため分秒構文Aとして退けます。誤答B分秒構文はTIME=(mm,ss)ではなくMSGCLASSの出力クラス指定を見分けるための説明なので分秒構文Bに分類します。誤答C分秒構文はREGIONやMEMLIMITの記憶域制御で読む内容で、分秒構文の指定値とは結び付かないため分秒構文Cで区別します。分秒構文の確認結果は、投入前レビューと障害調査のどちらで使う証跡かを区別します。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 時間超過の根拠を整理しています。標準JCLの見直しで明示指定と導入先の既定値を分けています。TIME 上限超過時の異常終了に対応する説明はどれですか。

    - A. 超過時はSYSOUTへコピーされる
    - B. 超過時はS322で異常終了する ✅
    - C. 超過時はJCL変換前に保留される
    - D. 超過時はMSGCLASSが既定値に戻る

    正解: **B** ／ 難易度: 初級

    **解説:** Bが正解です。時間超過の正答理由として、TIMEで定めたCPU時間を超えると、ジョブまたはステップはS322で異常終了します。誤答A時間超過はTYPRUN=COPYや出力クラスの扱いで読む内容で、時間超過の指定値とは結び付かないため時間超過Aで区別します。誤答C時間超過はTYPRUN=HOLDやJCLHOLDの保留制御を説明しており、TIME 上限超過時の異常終了の判断点とは見る欄が違うことを時間超過Cで分けます。誤答D時間超過は別のJOB文パラメータの説明で、TIME 上限超過時の異常終了で問われる効き方とは対象がずれるため時間超過Dで外します。時間超過の記録では、明示値、既定値、実行後に見えた値を別々に残します。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 時間既定を確認しています。本番投入前に時間制限や保留指定の扱いを確認しています。担当者がTIME 省略時の既定値の意味として選ぶべき説明はどれですか。

    - A. MSGCLASSの出力クラスを使う
    - B. MEMLIMITの64-bit上限を使う
    - C. JOBCLASSやシステム既定を使う ✅
    - D. CONDの戻りコード比較を使う

    正解: **C** ／ 難易度: 初級

    **解説:** Cが正解です。時間既定の正答理由として、JOB文でTIMEを省略すると、JOBCLASSの指定やシステム既定値がCPU時間上限として使われます。誤答A時間既定はMSGCLASSの出力クラス指定を扱う説明で、TIME 省略時の既定値の根拠にならないため時間既定Aとして外します。誤答B時間既定はMEMLIMITによる64-bit記憶域制御を説明しており、TIME 省略時の既定値の判断点とは見る欄が違うことを時間既定Bで分けます。誤答D時間既定はCONDによる戻りコード制御に関する内容で、時間既定の確認対象ではないため時間既定Dとして退けます。時間既定では、指定がジョブ識別、出力制御、メッセージ制御、記憶制限、時間制限、実行制御のどこに効くかを分けます。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 時間優先の説明を選ぶ作業です。ジョブ異常終了後の初動で戻りコードと後続ステップの関係を整理しています。項目「JOB 文 TIME と EXEC 文 TIME」に最も合うものはどれですか。

    - A. SYSOUTだけの上限として働く
    - B. JCL変換前だけの保留条件になる
    - C. 64-bit領域だけの単位指定になる
    - D. JOB全体の上限として働く ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dが正解です。時間優先の正答理由として、JOB文TIMEはジョブ全体の上限で、EXEC文TIMEは各ステップの制限としてその範囲内で働きます。誤答A時間優先はTYPRUN=COPYや出力クラスの扱いを説明しており、JOB 文 TIME と EXEC 文 TIMEの判断点とは見る欄が違うことを時間優先Aで分けます。誤答B時間優先はTYPRUN=HOLDやJCLHOLDの保留制御の説明で、JOB 文 TIME と EXEC 文 TIMEで問われる効き方とは対象がずれるため時間優先Bで外します。誤答C時間優先はMEMLIMITによる64-bit記憶域制御に関する内容で、時間優先の確認対象ではないため時間優先Cとして退けます。時間優先で項目「JOB 文 TIME と EXEC 文 TIME」を確認するときは、元JCLの欄と実行後ログの欄を同じものとして扱わないことが大切です。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 条件目的をレビュー対象にしています。投入前レビューでJOB文の資源制御欄を読んでいます。担当者が押さえるべき説明はどれですか。

    - A. CPU時間の上限を制御する
    - B. ジョブログ出力クラスを制御する
    - C. 戻りコードで後続ステップを制御する ✅
    - D. 64-bit記憶域の上限を制御する

    正解: **C** ／ 難易度: 初級

    **解説:** Cが正解です。条件目的の正答理由として、JOB文のCONDは、前のステップの戻りコードを見て後続ステップを実行するかどうかを制御します。誤答A条件目的はJOB文TIMEのCPU時間制御の説明で、JOB 文 COND の目的で問われる効き方とは対象がずれるため条件目的Aで外します。誤答B条件目的はMSGCLASSによるジョブログ出力に関する内容で、条件目的の確認対象ではないため条件目的Bとして退けます。誤答D条件目的はMEMLIMITによる64-bit記憶域制御で読む内容で、条件目的の指定値とは結び付かないため条件目的Dで区別します。条件目的を説明するときは、同じJOB文内の隣接パラメータと効き方を比べます。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 条件構文の根拠を整理しています。障害調査でJESJCLとジョブログの出方を突き合わせています。COND=(code,operator)に対応する説明はどれですか。

    - A. 分と秒の組で時間を指定する
    - B. クラス名と保留属性を組にする
    - C. MB値とGB値で記憶域を分ける
    - D. 数値と比較演算子で判定する ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dが正解です。条件構文の正答理由として、COND=(code,operator)は、指定した数値と実際の戻りコードを比較演算子で判定します。誤答A条件構文はTIMEの分秒指定に関する内容で、条件構文の確認対象ではないため条件構文Aとして退けます。誤答B条件構文はCOND=(code,operator)ではなくTYPRUN=HOLDやJCLHOLDの保留制御を見分けるための説明なので条件構文Bに分類します。誤答C条件構文はREGIONやMEMLIMITの記憶域制御で読む内容で、条件構文の指定値とは結び付かないため条件構文Cで区別します。条件構文の記録では、明示値、既定値、実行後に見えた値を別々に残します。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 比較方向の影響範囲を確認しています。運用引継ぎでJOB文指定が実行に与える影響を説明しています。最も適切な説明はどれですか。

    - A. 左辺が実RCで右辺が指定値である
    - B. 左辺が出力クラスで右辺が保留属性である
    - C. 左辺が指定値で右辺が実RCである ✅
    - D. 左辺が分で右辺が秒である

    正解: **C** ／ 難易度: 中級

    **解説:** Cが正解です。比較方向の正答理由として、CONDの比較は、左辺を指定したcode、右辺を実際の戻りコードとして読んで判定します。誤答A比較方向はCOND 比較方向ではなくCONDの戻りコード比較を見分けるための説明なので比較方向Aに分類します。誤答B比較方向はMSGCLASSの出力クラス指定で読む内容で、比較方向の指定値とは結び付かないため比較方向Bで区別します。誤答D比較方向はTIMEの分秒指定を説明しており、COND 比較方向の判断点とは見る欄が違うことを比較方向Dで分けます。比較方向では、JES2定義、ジョブカード、SDSF表示のどれを根拠にしたかを分けます。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）

    ---

    **問題.** 複数条件を説明する資料に載せる文を選んでいます。標準JCLの見直しで明示指定と導入先の既定値を分けています。正しいものはどれですか。

    - A. すべて真の時だけ実行する
    - B. 最後の条件だけを常に無視する
    - C. 時間上限だけを最大にする
    - D. いずれか真ならスキップする ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dが正解です。複数条件の正答理由として、CONDに複数条件を書くと、どれか一つでも真になった場合にスキップ条件が成立します。誤答A複数条件は別のJOB文パラメータで読む内容で、複数条件の指定値とは結び付かないため複数条件Aで区別します。誤答B複数条件は別のJOB文パラメータを扱う説明で、COND 複数条件の OR 関係の根拠にならないため複数条件Bとして外します。誤答C複数条件は別のJOB文パラメータを説明しており、COND 複数条件の OR 関係の判断点とは見る欄が違うことを複数条件Cで分けます。複数条件の確認結果は、投入前レビューと障害調査のどちらで使う証跡かを区別します。

    **出典:** OS MVS JCL Reference（zOS31_ieab600）


??? note "検証手順（197件）"
    **JOB ステートメントの位置付け 確認手順**

    - 検証目的: JOB ステートメントの位置付けについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00174を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00174 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00174
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00174
    ```

    COMMAND INPUTにST JJB00174が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00174 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00174 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00174
    $HASP395 JJB00174 ENDED - RC=0000
    ```

    $HASP373とJJB00174が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00174 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00174 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL User's Guide (zOS31_ieab500) / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **JOB 文コメントの記述位置 確認手順**

    - 検証目的: JOB 文コメントの記述位置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00175を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00175 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00175
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00175
    ```

    COMMAND INPUTにST JJB00175が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00175 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00175 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00175
    $HASP395 JJB00175 ENDED - RC=0000
    ```

    $HASP373とJJB00175が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00175 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00175 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **jobname 第 1 桁の制約 確認手順**

    - 検証目的: jobname 第 1 桁の制約について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00176を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00176 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00176
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00176
    ```

    COMMAND INPUTにST JJB00176が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00176 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00176 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00176
    $HASP395 JJB00176 ENDED - RC=0000
    ```

    $HASP373とJJB00176が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00176 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00176 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **アカウンティング情報の位置 確認手順**

    - 検証目的: アカウンティング情報の位置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00177を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00177 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00177
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00177
    ```

    COMMAND INPUTにST JJB00177が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00177 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00177 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00177
    $HASP395 JJB00177 ENDED - RC=0000
    ```

    ICH70001IとJJB00177が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00177 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00177 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング情報の省略 確認手順**

    - 検証目的: アカウンティング情報の省略について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00178を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00178 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00178
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00178
    ```

    COMMAND INPUTにST JJB00178が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00178 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00178 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00178
    $HASP395 JJB00178 ENDED - RC=0000
    ```

    $HASP373とJJB00178が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00178 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00178 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **プログラマ名の最大長 確認手順**

    - 検証目的: プログラマ名の最大長について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00179を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00179 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00179
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00179
    ```

    COMMAND INPUTにST JJB00179が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00179 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00179 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00179
    $HASP395 JJB00179 ENDED - RC=0000
    ```

    $HASP373とJJB00179が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00179 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00179 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS の値域 確認手順**

    - 検証目的: CLASS の値域について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00180を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00180 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00180
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00180
    ```

    COMMAND INPUTにST JJB00180が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00180 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00180 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00180
    $HASP395 JJB00180 ENDED - RC=0000
    ```

    $HASP373とJJB00180が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00180 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00180 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS と SCHENV の関係 確認手順**

    - 検証目的: CLASS と SCHENV の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00181を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00181 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00181
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00181
    ```

    COMMAND INPUTにST JJB00181が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00181 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00181 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00181
    $HASP395 JJB00181 ENDED - RC=0000
    ```

    $HASP373とJJB00181が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00181 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00181 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGCLASS と SYSOUT のクラス継承 確認手順**

    - 検証目的: MSGCLASS と SYSOUT のクラス継承について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00182を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00182 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00182
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00182
    ```

    COMMAND INPUTにST JJB00182が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00182 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00182 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00182
    $HASP395 JJB00182 ENDED - RC=0000
    ```

    IEF236IとJJB00182が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00182 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00182 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL statements=1 確認手順**

    - 検証目的: MSGLEVEL statements=1について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00183を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00183 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00183
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00183
    ```

    COMMAND INPUTにST JJB00183が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00183 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00183 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00183
    $HASP395 JJB00183 ENDED - RC=0000
    ```

    IEF236IとJJB00183が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00183 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00183 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL 省略時 確認手順**

    - 検証目的: MSGLEVEL 省略時について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00184を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00184 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00184
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00184
    ```

    COMMAND INPUTにST JJB00184が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00184 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00184 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00184
    $HASP395 JJB00184 ENDED - RC=0000
    ```

    IEF236IとJJB00184が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00184 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00184 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=NM の意味 確認手順**

    - 検証目的: REGION=NM の意味について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00185を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00185 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00185
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00185
    ```

    COMMAND INPUTにST JJB00185が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00185 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00185 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00185
    $HASP395 JJB00185 ENDED - RC=0000
    ```

    IEF236IとJJB00185が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00185 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00185 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION の値域 (MB) 確認手順**

    - 検証目的: REGION の値域 (MB)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00186を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00186 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00186
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00186
    ```

    COMMAND INPUTにST JJB00186が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00186 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00186 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00186
    $HASP395 JJB00186 ENDED - RC=0000
    ```

    IEF236IとJJB00186が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00186 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00186 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION と IEFUSI 出口 確認手順**

    - 検証目的: REGION と IEFUSI 出口について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00187を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00187 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00187
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00187
    ```

    COMMAND INPUTにST JJB00187が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00187 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00187 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00187
    $HASP395 JJB00187 ENDED - RC=0000
    ```

    IEF236IとJJB00187が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00187 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00187 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT=NG 確認手順**

    - 検証目的: MEMLIMIT=NGについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00188を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00188 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00188
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00188
    ```

    COMMAND INPUTにST JJB00188が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00188 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00188 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00188
    $HASP395 JJB00188 ENDED - RC=0000
    ```

    $HASP373とJJB00188が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00188 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00188 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT 省略時の既定値 確認手順**

    - 検証目的: MEMLIMIT 省略時の既定値について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00189を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00189 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00189
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00189
    ```

    COMMAND INPUTにST JJB00189が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00189 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00189 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00189
    $HASP395 JJB00189 ENDED - RC=0000
    ```

    ICH70001IとJJB00189が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00189 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00189 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=NOLIMIT 確認手順**

    - 検証目的: TIME=NOLIMITについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00190を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00190 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00190
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00190
    ```

    COMMAND INPUTにST JJB00190が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00190 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00190 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00190
    $HASP395 JJB00190 ENDED - RC=0000
    ```

    IEF236IとJJB00190が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00190 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00190 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=分のみ指定 確認手順**

    - 検証目的: TIME=分のみ指定について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00191を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00191 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00191
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00191
    ```

    COMMAND INPUTにST JJB00191が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00191 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00191 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00191
    $HASP395 JJB00191 ENDED - RC=0000
    ```

    IEF236IとJJB00191が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00191 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00191 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=SCAN 確認手順**

    - 検証目的: TYPRUN=SCANについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00192を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00192 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00192
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00192
    ```

    COMMAND INPUTにST JJB00192が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00192 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00192 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00192
    $HASP395 JJB00192 ENDED - RC=0000
    ```

    $HASP373とJJB00192が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00192 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00192 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=SCAN と JES2 構文検証 確認手順**

    - 検証目的: TYPRUN=SCAN と JES2 構文検証について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00193を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00193 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00193
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00193
    ```

    COMMAND INPUTにST JJB00193が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00193 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00193 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00193
    $HASP395 JJB00193 ENDED - RC=0000
    ```

    $HASP373とJJB00193が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00193 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00193 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 LT 確認手順**

    - 検証目的: COND 演算子 LTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00194を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00194 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00194
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00194
    ```

    COMMAND INPUTにST JJB00194が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00194 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00194 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00194
    $HASP395 JJB00194 ENDED - RC=0000
    ```

    $HASP373とJJB00194が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00194 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00194 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 GT 確認手順**

    - 検証目的: COND 演算子 GTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00195を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00195 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00195
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00195
    ```

    COMMAND INPUTにST JJB00195が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00195 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00195 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00195
    $HASP395 JJB00195 ENDED - RC=0000
    ```

    ICH70001IとJJB00195が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00195 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00195 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND=EVEN 確認手順**

    - 検証目的: COND=EVENについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00196を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00196 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00196
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00196
    ```

    COMMAND INPUTにST JJB00196が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00196 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00196 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00196
    $HASP395 JJB00196 ENDED - RC=0000
    ```

    $HASP373とJJB00196が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00196 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00196 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND と IF/THEN/ELSE/ENDIF の関係 確認手順**

    - 検証目的: COND と IF/THEN/ELSE/ENDIF の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00197を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00197 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00197
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00197
    ```

    COMMAND INPUTにST JJB00197が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00197 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00197 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00197
    $HASP395 JJB00197 ENDED - RC=0000
    ```

    $HASP373とJJB00197が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00197 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00197 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART=stepname.procstep 確認手順**

    - 検証目的: RESTART=stepname.procstepについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00198を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00198 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00198
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00198
    ```

    COMMAND INPUTにST JJB00198が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00198 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00198 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00198
    $HASP395 JJB00198 ENDED - RC=0000
    ```

    ICH70001IとJJB00198が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00198 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00198 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART と DD DISP=(NEW,...) の整合 確認手順**

    - 検証目的: RESTART と DD DISP=(NEW,...) の整合について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00199を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00199 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00199
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00199
    ```

    COMMAND INPUTにST JJB00199が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00199 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00199 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00199
    $HASP395 JJB00199 ENDED - RC=0000
    ```

    $HASP395とJJB00199が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00199 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00199 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PRTY 省略時のデフォルト 確認手順**

    - 検証目的: PRTY 省略時のデフォルトについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00200を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00200 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00200
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00200
    ```

    COMMAND INPUTにST JJB00200が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00200 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00200 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00200
    $HASP395 JJB00200 ENDED - RC=0000
    ```

    $HASP373とJJB00200が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00200 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00200 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **USER 省略時のユーザ 確認手順**

    - 検証目的: USER 省略時のユーザについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00201を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00201 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00201
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00201
    ```

    COMMAND INPUTにST JJB00201が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00201 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00201 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00201
    $HASP395 JJB00201 ENDED - RC=0000
    ```

    ICH70001IとJJB00201が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00201 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00201 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **GROUP パラメータの目的 確認手順**

    - 検証目的: GROUP パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00202を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00202 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00202
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00202
    ```

    COMMAND INPUTにST JJB00202が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00202 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00202 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00202
    $HASP395 JJB00202 ENDED - RC=0000
    ```

    $HASP373とJJB00202が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00202 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00202 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **Surrogate ユーザ運用 確認手順**

    - 検証目的: Surrogate ユーザ運用について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00203を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00203 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00203
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00203
    ```

    COMMAND INPUTにST JJB00203が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00203 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00203 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00203
    $HASP395 JJB00203 ENDED - RC=0000
    ```

    ICH70001IとJJB00203が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00203 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00203 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **NOTIFY と TSO SEND の関係 確認手順**

    - 検証目的: NOTIFY と TSO SEND の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00204を表示し、JESJCLとJESYSMSGにあるNOTIFY=&SYSUIDと$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00204 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00204
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00204
    ```

    COMMAND INPUTにST JJB00204が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00204 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにNOTIFY=&SYSUIDが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00204 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00204
    $HASP395 JJB00204 ENDED - RC=0000
    ```

    $HASP395とJJB00204が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00204 が画面・出力に表示されること
    ② ステップ2 の NOTIFY=&SYSUID が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00204 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **ADDRSPC=VIRT 確認手順**

    - 検証目的: ADDRSPC=VIRTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00205を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00205 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00205
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00205
    ```

    COMMAND INPUTにST JJB00205が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00205 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00205 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00205
    $HASP395 JJB00205 ENDED - RC=0000
    ```

    $HASP373とJJB00205が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00205 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00205 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **BYTES パラメータの目的 確認手順**

    - 検証目的: BYTES パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00206を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00206 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00206
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00206
    ```

    COMMAND INPUTにST JJB00206が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00206 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00206 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00206
    $HASP395 JJB00206 ENDED - RC=0000
    ```

    $HASP373とJJB00206が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00206 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00206 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **LINES パラメータの目的 確認手順**

    - 検証目的: LINES パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00207を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00207 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00207
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00207
    ```

    COMMAND INPUTにST JJB00207が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00207 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00207 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00207
    $HASP395 JJB00207 ENDED - RC=0000
    ```

    ICH70001IとJJB00207が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00207 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00207 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **BYTES/LINES と JES2 ESTBYTE/ESTLNCT の関係 確認手順**

    - 検証目的: BYTES/LINES と JES2 ESTBYTE/ESTLNCT の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00208を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00208 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00208
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00208
    ```

    COMMAND INPUTにST JJB00208が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00208 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00208 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00208
    $HASP395 JJB00208 ENDED - RC=0000
    ```

    $HASP373とJJB00208が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00208 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00208 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **DSENQSHR パラメータ 確認手順**

    - 検証目的: DSENQSHR パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00209を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00209 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00209
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00209
    ```

    COMMAND INPUTにST JJB00209が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00209 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00209 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00209
    $HASP395 JJB00209 ENDED - RC=0000
    ```

    $HASP373とJJB00209が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00209 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00209 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CCSID パラメータ 確認手順**

    - 検証目的: CCSID パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00210を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00210 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00210
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00210
    ```

    COMMAND INPUTにST JJB00210が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00210 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00210 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00210
    $HASP395 JJB00210 ENDED - RC=0000
    ```

    ICH70001IとJJB00210が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00210 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00210 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **IF 条件と ABEND 検査 確認手順**

    - 検証目的: IF 条件と ABEND 検査について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00211を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00211 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00211
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00211
    ```

    COMMAND INPUTにST JJB00211が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00211 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00211 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00211
    $HASP395 JJB00211 ENDED - RC=0000
    ```

    $HASP373とJJB00211が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00211 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00211 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOB 文 IEFUJV 出口検証 確認手順**

    - 検証目的: JOB 文 IEFUJV 出口検証について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00212を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00212 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00212
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00212
    ```

    COMMAND INPUTにST JJB00212が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00212 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00212 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00212
    $HASP395 JJB00212 ENDED - RC=0000
    ```

    $HASP373とJJB00212が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00212 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00212 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOBPARM JES2 制御文 確認手順**

    - 検証目的: JOBPARM JES2 制御文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00213を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00213 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00213
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00213
    ```

    COMMAND INPUTにST JJB00213が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00213 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00213 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00213
    $HASP395 JJB00213 ENDED - RC=0000
    ```

    ICH70001IとJJB00213が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00213 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00213 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **//* コメント文との違い 確認手順**

    - 検証目的: //* コメント文との違いについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00001を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00001 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00001
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00001
    ```

    COMMAND INPUTにST JJB00001が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00001 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00001 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00001
    $HASP395 JJB00001 ENDED - RC=0000
    ```

    $HASP373とJJB00001が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00001 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00001 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **jobname の長さ制限 確認手順**

    - 検証目的: jobname の長さ制限について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00002を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00002 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00002
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00002
    ```

    COMMAND INPUTにST JJB00002が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00002 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00002 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00002
    $HASP395 JJB00002 ENDED - RC=0000
    ```

    $HASP373とJJB00002が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00002 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00002 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **jobname の文字種 確認手順**

    - 検証目的: jobname の文字種について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00003を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00003 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00003
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00003
    ```

    COMMAND INPUTにST JJB00003が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00003 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00003 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00003
    $HASP395 JJB00003 ENDED - RC=0000
    ```

    $HASP373とJJB00003が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00003 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00003 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **jobname 第 1 桁の制約 確認手順**

    - 検証目的: jobname 第 1 桁の制約について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00004を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00004 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00004
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00004
    ```

    COMMAND INPUTにST JJB00004が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00004 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00004 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00004
    $HASP395 JJB00004 ENDED - RC=0000
    ```

    $HASP373とJJB00004が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00004 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00004 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600)

    ---

    **jobname の // 直後配置 確認手順**

    - 検証目的: jobname の // 直後配置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00005を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00005 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00005
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00005
    ```

    COMMAND INPUTにST JJB00005が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00005 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00005 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00005
    $HASP395 JJB00005 ENDED - RC=0000
    ```

    $HASP373とJJB00005が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00005 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00005 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference (zOS31_ieab600) / JES2 Initialization (zOS31_hasa300)

    ---

    **jobname 重複時の動作 確認手順**

    - 検証目的: jobname 重複時の動作について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00006を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00006 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00006
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00006
    ```

    COMMAND INPUTにST JJB00006が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00006 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00006 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00006
    $HASP395 JJB00006 ENDED - RC=0000
    ```

    $HASP373とJJB00006が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00006 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00006 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **jobname の命名規約とユーザ ID 連携 確認手順**

    - 検証目的: jobname の命名規約とユーザ ID 連携について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00007を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00007 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00007
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00007
    ```

    COMMAND INPUTにST JJB00007が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00007 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00007 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00007
    $HASP395 JJB00007 ENDED - RC=0000
    ```

    $HASP373とJJB00007が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00007 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00007 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング情報の位置 確認手順**

    - 検証目的: アカウンティング情報の位置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00008を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00008 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00008
    ```

    COMMAND INPUTにST JJB00008が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00008 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00008 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00008
    $HASP395 JJB00008 ENDED - RC=0000
    ```

    ICH70001IとJJB00008が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00008 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング情報の構文 確認手順**

    - 検証目的: アカウンティング情報の構文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00009を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00009 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00009
    ```

    COMMAND INPUTにST JJB00009が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00009 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00009 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00009
    $HASP395 JJB00009 ENDED - RC=0000
    ```

    $HASP373とJJB00009が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00009 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング情報の最大長 確認手順**

    - 検証目的: アカウンティング情報の最大長について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00010を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00010 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00010
    ```

    COMMAND INPUTにST JJB00010が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00010 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00010 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00010
    $HASP395 JJB00010 ENDED - RC=0000
    ```

    $HASP373とJJB00010が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00010 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング番号 確認手順**

    - 検証目的: アカウンティング番号について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00011を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00011 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00011
    ```

    COMMAND INPUTにST JJB00011が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00011 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00011 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00011
    $HASP395 JJB00011 ENDED - RC=0000
    ```

    ICH70001IとJJB00011が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00011 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング情報の省略 確認手順**

    - 検証目的: アカウンティング情報の省略について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00012を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00012 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00012
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00012
    ```

    COMMAND INPUTにST JJB00012が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00012 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00012 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00012
    $HASP395 JJB00012 ENDED - RC=0000
    ```

    $HASP373とJJB00012が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00012 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00012 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **アカウンティング情報内の特殊文字 確認手順**

    - 検証目的: アカウンティング情報内の特殊文字について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00013を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00013 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00013
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00013
    ```

    COMMAND INPUTにST JJB00013が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00013 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00013 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00013
    $HASP395 JJB00013 ENDED - RC=0000
    ```

    $HASP373とJJB00013が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00013 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00013 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **IEFUJV アカウンティング検証出口 確認手順**

    - 検証目的: IEFUJV アカウンティング検証出口について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00014を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00014 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00014
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00014
    ```

    COMMAND INPUTにST JJB00014が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00014 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00014 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00014
    $HASP395 JJB00014 ENDED - RC=0000
    ```

    ICH70001IとJJB00014が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00014 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00014 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **プログラマ名の位置 確認手順**

    - 検証目的: プログラマ名の位置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00015を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00015 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00015
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00015
    ```

    COMMAND INPUTにST JJB00015が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00015 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00015 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00015
    $HASP395 JJB00015 ENDED - RC=0000
    ```

    $HASP373とJJB00015が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00015 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00015 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **プログラマ名の最大長 確認手順**

    - 検証目的: プログラマ名の最大長について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00016を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00016 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00016
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00016
    ```

    COMMAND INPUTにST JJB00016が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00016 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00016 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00016
    $HASP395 JJB00016 ENDED - RC=0000
    ```

    $HASP373とJJB00016が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00016 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00016 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **プログラマ名にアポストロフィが必要なケース 確認手順**

    - 検証目的: プログラマ名にアポストロフィが必要なケースについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00017を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00017 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00017
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00017
    ```

    COMMAND INPUTにST JJB00017が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00017 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00017 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00017
    $HASP395 JJB00017 ENDED - RC=0000
    ```

    ICH70001IとJJB00017が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00017 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00017 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **プログラマ名の省略 確認手順**

    - 検証目的: プログラマ名の省略について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00018を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00018 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00018
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00018
    ```

    COMMAND INPUTにST JJB00018が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00018 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00018 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00018
    $HASP395 JJB00018 ENDED - RC=0000
    ```

    $HASP373とJJB00018が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00018 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00018 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS パラメータの目的 確認手順**

    - 検証目的: CLASS パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00019を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00019 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00019
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00019
    ```

    COMMAND INPUTにST JJB00019が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00019 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00019 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00019
    $HASP395 JJB00019 ENDED - RC=0000
    ```

    $HASP373とJJB00019が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00019 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00019 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS の値域 確認手順**

    - 検証目的: CLASS の値域について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00020を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00020 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00020
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00020
    ```

    COMMAND INPUTにST JJB00020が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00020 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00020 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00020
    $HASP395 JJB00020 ENDED - RC=0000
    ```

    $HASP373とJJB00020が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00020 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00020 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS 省略時の既定値 確認手順**

    - 検証目的: CLASS 省略時の既定値について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00021を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00021 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00021
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00021
    ```

    COMMAND INPUTにST JJB00021が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00021 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00021 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00021
    $HASP395 JJB00021 ENDED - RC=0000
    ```

    $HASP373とJJB00021が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00021 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00021 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS と JOBCLASS イニシエータの関係 確認手順**

    - 検証目的: CLASS と JOBCLASS イニシエータの関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00022を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00022 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00022
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00022
    ```

    COMMAND INPUTにST JJB00022が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00022 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00022 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00022
    $HASP395 JJB00022 ENDED - RC=0000
    ```

    $HASP373とJJB00022が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00022 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00022 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS と TIME 上限の関係 確認手順**

    - 検証目的: CLASS と TIME 上限の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00023を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00023 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00023
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00023
    ```

    COMMAND INPUTにST JJB00023が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00023 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00023 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00023
    $HASP395 JJB00023 ENDED - RC=0000
    ```

    $HASP373とJJB00023が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00023 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00023 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CLASS と SCHENV の関係 確認手順**

    - 検証目的: CLASS と SCHENV の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00024を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00024 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00024
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00024
    ```

    COMMAND INPUTにST JJB00024が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00024 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00024 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00024
    $HASP395 JJB00024 ENDED - RC=0000
    ```

    $HASP373とJJB00024が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00024 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00024 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGCLASS パラメータの目的 確認手順**

    - 検証目的: MSGCLASS パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00025を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00025 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00025
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00025
    ```

    COMMAND INPUTにST JJB00025が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00025 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00025 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00025
    $HASP395 JJB00025 ENDED - RC=0000
    ```

    IEF236IとJJB00025が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00025 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00025 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGCLASS の値域 確認手順**

    - 検証目的: MSGCLASS の値域について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00026を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00026 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00026
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00026
    ```

    COMMAND INPUTにST JJB00026が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00026 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00026 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00026
    $HASP395 JJB00026 ENDED - RC=0000
    ```

    IEF236IとJJB00026が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00026 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00026 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGCLASS 省略時の動作 確認手順**

    - 検証目的: MSGCLASS 省略時の動作について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00027を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00027 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00027
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00027
    ```

    COMMAND INPUTにST JJB00027が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00027 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00027 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00027
    $HASP395 JJB00027 ENDED - RC=0000
    ```

    IEF236IとJJB00027が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00027 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00027 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGCLASS と SYSOUT のクラス継承 確認手順**

    - 検証目的: MSGCLASS と SYSOUT のクラス継承について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00028を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00028 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00028
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00028
    ```

    COMMAND INPUTにST JJB00028が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00028 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00028 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00028
    $HASP395 JJB00028 ENDED - RC=0000
    ```

    IEF236IとJJB00028が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00028 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00028 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGCLASS=Z のホールド運用 確認手順**

    - 検証目的: MSGCLASS=Z のホールド運用について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00029を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00029 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00029
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00029
    ```

    COMMAND INPUTにST JJB00029が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00029 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00029 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00029
    $HASP395 JJB00029 ENDED - RC=0000
    ```

    IEF236IとJJB00029が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00029 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00029 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL パラメータ構文 確認手順**

    - 検証目的: MSGLEVEL パラメータ構文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00030を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00030 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00030
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00030
    ```

    COMMAND INPUTにST JJB00030が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00030 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00030 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00030
    $HASP395 JJB00030 ENDED - RC=0000
    ```

    IEF236IとJJB00030が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00030 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00030 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL statements=0 確認手順**

    - 検証目的: MSGLEVEL statements=0について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00031を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00031 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00031
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00031
    ```

    COMMAND INPUTにST JJB00031が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00031 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00031 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00031
    $HASP395 JJB00031 ENDED - RC=0000
    ```

    IEF236IとJJB00031が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00031 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00031 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL statements=1 確認手順**

    - 検証目的: MSGLEVEL statements=1について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00032を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00032 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00032
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00032
    ```

    COMMAND INPUTにST JJB00032が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00032 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00032 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00032
    $HASP395 JJB00032 ENDED - RC=0000
    ```

    IEF236IとJJB00032が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00032 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00032 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL statements=2 確認手順**

    - 検証目的: MSGLEVEL statements=2について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00033を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00033 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00033
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00033
    ```

    COMMAND INPUTにST JJB00033が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00033 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00033 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00033
    $HASP395 JJB00033 ENDED - RC=0000
    ```

    IEF236IとJJB00033が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00033 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00033 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL messages=0 確認手順**

    - 検証目的: MSGLEVEL messages=0について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00034を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00034 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00034
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00034
    ```

    COMMAND INPUTにST JJB00034が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00034 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00034 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00034
    $HASP395 JJB00034 ENDED - RC=0000
    ```

    IEF236IとJJB00034が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00034 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00034 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL messages=1 確認手順**

    - 検証目的: MSGLEVEL messages=1について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00035を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00035 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00035
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00035
    ```

    COMMAND INPUTにST JJB00035が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00035 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00035 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00035
    $HASP395 JJB00035 ENDED - RC=0000
    ```

    IEF236IとJJB00035が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00035 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00035 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MSGLEVEL 省略時 確認手順**

    - 検証目的: MSGLEVEL 省略時について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00036を表示し、JESJCLとJESYSMSGにあるMSGLEVEL=(1,1)とIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00036 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00036
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00036
    ```

    COMMAND INPUTにST JJB00036が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00036 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにMSGLEVEL=(1,1)が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00036 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00036
    $HASP395 JJB00036 ENDED - RC=0000
    ```

    IEF236IとJJB00036が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00036 が画面・出力に表示されること
    ② ステップ2 の MSGLEVEL=(1,1) が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00036 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION パラメータの目的 確認手順**

    - 検証目的: REGION パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00037を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00037 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00037
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00037
    ```

    COMMAND INPUTにST JJB00037が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00037 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00037 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00037
    $HASP395 JJB00037 ENDED - RC=0000
    ```

    IEF236IとJJB00037が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00037 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00037 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=0M 確認手順**

    - 検証目的: REGION=0Mについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00038を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00038 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00038
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00038
    ```

    COMMAND INPUTにST JJB00038が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00038 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00038 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00038
    $HASP395 JJB00038 ENDED - RC=0000
    ```

    IEF236IとJJB00038が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00038 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00038 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=0K 確認手順**

    - 検証目的: REGION=0Kについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00039を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00039 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00039
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00039
    ```

    COMMAND INPUTにST JJB00039が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00039 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00039 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00039
    $HASP395 JJB00039 ENDED - RC=0000
    ```

    IEF236IとJJB00039が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00039 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00039 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=NM の意味 確認手順**

    - 検証目的: REGION=NM の意味について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00040を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00040 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00040
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00040
    ```

    COMMAND INPUTにST JJB00040が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00040 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00040 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00040
    $HASP395 JJB00040 ENDED - RC=0000
    ```

    IEF236IとJJB00040が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00040 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00040 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=NK の意味 確認手順**

    - 検証目的: REGION=NK の意味について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00041を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00041 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00041
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00041
    ```

    COMMAND INPUTにST JJB00041が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00041 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00041 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00041
    $HASP395 JJB00041 ENDED - RC=0000
    ```

    IEF236IとJJB00041が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00041 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00041 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=NM と 16M ラインの関係 確認手順**

    - 検証目的: REGION=NM と 16M ラインの関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00042を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00042 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00042
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00042
    ```

    COMMAND INPUTにST JJB00042が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00042 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00042 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00042
    $HASP395 JJB00042 ENDED - RC=0000
    ```

    IEF236IとJJB00042が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00042 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00042 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION の値域 (KB) 確認手順**

    - 検証目的: REGION の値域 (KB)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00043を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00043 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00043
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00043
    ```

    COMMAND INPUTにST JJB00043が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00043 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00043 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00043
    $HASP395 JJB00043 ENDED - RC=0000
    ```

    IEF236IとJJB00043が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00043 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00043 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION の値域 (MB) 確認手順**

    - 検証目的: REGION の値域 (MB)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00044を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00044 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00044
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00044
    ```

    COMMAND INPUTにST JJB00044が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00044 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00044 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00044
    $HASP395 JJB00044 ENDED - RC=0000
    ```

    IEF236IとJJB00044が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00044 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00044 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION 偶数バイト切り上げ 確認手順**

    - 検証目的: REGION 偶数バイト切り上げについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00045を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00045 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00045
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00045
    ```

    COMMAND INPUTにST JJB00045が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00045 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00045 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00045
    $HASP395 JJB00045 ENDED - RC=0000
    ```

    IEF236IとJJB00045が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00045 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00045 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION の JOB 文と EXEC 文の優先順位 確認手順**

    - 検証目的: REGION の JOB 文と EXEC 文の優先順位について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00046を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00046 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00046
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00046
    ```

    COMMAND INPUTにST JJB00046が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00046 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00046 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00046
    $HASP395 JJB00046 ENDED - RC=0000
    ```

    IEF236IとJJB00046が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00046 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00046 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION 省略時のデフォルト 確認手順**

    - 検証目的: REGION 省略時のデフォルトについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00047を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00047 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00047
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00047
    ```

    COMMAND INPUTにST JJB00047が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00047 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00047 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00047
    $HASP395 JJB00047 ENDED - RC=0000
    ```

    IEF236IとJJB00047が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00047 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00047 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION と IEFUSI 出口 確認手順**

    - 検証目的: REGION と IEFUSI 出口について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00048を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00048 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00048
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00048
    ```

    COMMAND INPUTにST JJB00048が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00048 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00048 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00048
    $HASP395 JJB00048 ENDED - RC=0000
    ```

    IEF236IとJJB00048が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00048 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00048 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION と ABEND 878/80A 確認手順**

    - 検証目的: REGION と ABEND 878/80Aについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00049を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00049 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00049
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00049
    ```

    COMMAND INPUTにST JJB00049が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00049 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00049 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00049
    $HASP395 JJB00049 ENDED - RC=0000
    ```

    IEF236IとJJB00049が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00049 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00049 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT パラメータの目的 確認手順**

    - 検証目的: MEMLIMIT パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00050を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00050 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00050
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00050
    ```

    COMMAND INPUTにST JJB00050が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00050 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00050 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00050
    $HASP395 JJB00050 ENDED - RC=0000
    ```

    ICH70001IとJJB00050が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00050 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00050 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT=NM 確認手順**

    - 検証目的: MEMLIMIT=NMについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00051を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00051 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00051
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00051
    ```

    COMMAND INPUTにST JJB00051が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00051 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00051 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00051
    $HASP395 JJB00051 ENDED - RC=0000
    ```

    $HASP373とJJB00051が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00051 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00051 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT=NG 確認手順**

    - 検証目的: MEMLIMIT=NGについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00052を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00052 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00052
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00052
    ```

    COMMAND INPUTにST JJB00052が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00052 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00052 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00052
    $HASP395 JJB00052 ENDED - RC=0000
    ```

    $HASP373とJJB00052が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00052 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00052 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT=NT 確認手順**

    - 検証目的: MEMLIMIT=NTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00053を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00053 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00053
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00053
    ```

    COMMAND INPUTにST JJB00053が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00053 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00053 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00053
    $HASP395 JJB00053 ENDED - RC=0000
    ```

    ICH70001IとJJB00053が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00053 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00053 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT=NP 確認手順**

    - 検証目的: MEMLIMIT=NPについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00054を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00054 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00054
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00054
    ```

    COMMAND INPUTにST JJB00054が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00054 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00054 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00054
    $HASP395 JJB00054 ENDED - RC=0000
    ```

    $HASP373とJJB00054が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00054 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00054 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT=NOLIMIT 確認手順**

    - 検証目的: MEMLIMIT=NOLIMITについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00055を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00055 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00055
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00055
    ```

    COMMAND INPUTにST JJB00055が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00055 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00055 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00055
    $HASP395 JJB00055 ENDED - RC=0000
    ```

    $HASP373とJJB00055が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00055 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00055 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT 省略時の既定値 確認手順**

    - 検証目的: MEMLIMIT 省略時の既定値について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00056を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00056 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00056
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00056
    ```

    COMMAND INPUTにST JJB00056が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00056 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00056 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00056
    $HASP395 JJB00056 ENDED - RC=0000
    ```

    ICH70001IとJJB00056が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00056 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00056 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGION=0M と MEMLIMIT の関係 確認手順**

    - 検証目的: REGION=0M と MEMLIMIT の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00057を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00057 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00057
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00057
    ```

    COMMAND INPUTにST JJB00057が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00057 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00057 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00057
    $HASP395 JJB00057 ENDED - RC=0000
    ```

    IEF236IとJJB00057が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00057 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00057 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **MEMLIMIT と IARV64 GETSTOR の関係 確認手順**

    - 検証目的: MEMLIMIT と IARV64 GETSTOR の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00058を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00058 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00058
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00058
    ```

    COMMAND INPUTにST JJB00058が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00058 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00058 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00058
    $HASP395 JJB00058 ENDED - RC=0000
    ```

    $HASP373とJJB00058が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00058 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00058 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME パラメータの目的 確認手順**

    - 検証目的: TIME パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00059を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00059 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00059
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00059
    ```

    COMMAND INPUTにST JJB00059が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00059 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00059 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00059
    $HASP395 JJB00059 ENDED - RC=0000
    ```

    IEF236IとJJB00059が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00059 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00059 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=NOLIMIT 確認手順**

    - 検証目的: TIME=NOLIMITについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00060を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00060 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00060
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00060
    ```

    COMMAND INPUTにST JJB00060が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00060 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00060 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00060
    $HASP395 JJB00060 ENDED - RC=0000
    ```

    IEF236IとJJB00060が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00060 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00060 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=MAXIMUM 確認手順**

    - 検証目的: TIME=MAXIMUMについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00061を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00061 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00061
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00061
    ```

    COMMAND INPUTにST JJB00061が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00061 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00061 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00061
    $HASP395 JJB00061 ENDED - RC=0000
    ```

    IEF236IとJJB00061が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00061 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00061 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=1440 の歴史的意味 確認手順**

    - 検証目的: TIME=1440 の歴史的意味について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00062を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00062 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00062
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00062
    ```

    COMMAND INPUTにST JJB00062が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00062 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00062 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00062
    $HASP395 JJB00062 ENDED - RC=0000
    ```

    IEF236IとJJB00062が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00062 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00062 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=(mm,ss) の構文 確認手順**

    - 検証目的: TIME=(mm,ss) の構文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00063を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00063 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00063
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00063
    ```

    COMMAND INPUTにST JJB00063が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00063 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00063 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00063
    $HASP395 JJB00063 ENDED - RC=0000
    ```

    IEF236IとJJB00063が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00063 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00063 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME=分のみ指定 確認手順**

    - 検証目的: TIME=分のみ指定について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00064を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00064 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00064
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00064
    ```

    COMMAND INPUTにST JJB00064が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00064 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00064 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00064
    $HASP395 JJB00064 ENDED - RC=0000
    ```

    IEF236IとJJB00064が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00064 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00064 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME 上限超過時の動作 確認手順**

    - 検証目的: TIME 上限超過時の動作について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00065を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00065 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00065
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00065
    ```

    COMMAND INPUTにST JJB00065が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00065 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00065 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00065
    $HASP395 JJB00065 ENDED - RC=0000
    ```

    IEF236IとJJB00065が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00065 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00065 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TIME 省略時のデフォルト 確認手順**

    - 検証目的: TIME 省略時のデフォルトについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00066を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00066 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00066
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00066
    ```

    COMMAND INPUTにST JJB00066が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00066 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00066 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00066
    $HASP395 JJB00066 ENDED - RC=0000
    ```

    $HASP373とJJB00066が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00066 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00066 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOB 文 TIME と EXEC 文 TIME の優先順位 確認手順**

    - 検証目的: JOB 文 TIME と EXEC 文 TIME の優先順位について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00067を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00067 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00067
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00067
    ```

    COMMAND INPUTにST JJB00067が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00067 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00067 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00067
    $HASP395 JJB00067 ENDED - RC=0000
    ```

    IEF236IとJJB00067が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00067 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00067 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=SCAN 確認手順**

    - 検証目的: TYPRUN=SCANについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00068を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00068 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00068
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00068
    ```

    COMMAND INPUTにST JJB00068が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00068 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00068 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00068
    $HASP395 JJB00068 ENDED - RC=0000
    ```

    $HASP373とJJB00068が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00068 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00068 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=HOLD 確認手順**

    - 検証目的: TYPRUN=HOLDについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00069を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00069 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00069
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00069
    ```

    COMMAND INPUTにST JJB00069が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00069 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00069 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00069
    $HASP395 JJB00069 ENDED - RC=0000
    ```

    $HASP373とJJB00069が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00069 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00069 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=JCLHOLD 確認手順**

    - 検証目的: TYPRUN=JCLHOLDについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00070を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00070 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00070
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00070
    ```

    COMMAND INPUTにST JJB00070が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00070 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00070 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00070
    $HASP395 JJB00070 ENDED - RC=0000
    ```

    $HASP373とJJB00070が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00070 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00070 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=COPY 確認手順**

    - 検証目的: TYPRUN=COPYについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00071を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00071 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00071
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00071
    ```

    COMMAND INPUTにST JJB00071が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00071 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00071 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00071
    $HASP395 JJB00071 ENDED - RC=0000
    ```

    $HASP373とJJB00071が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00071 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00071 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=SCAN と JES2 構文検証 確認手順**

    - 検証目的: TYPRUN=SCAN と JES2 構文検証について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00072を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00072 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00072
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00072
    ```

    COMMAND INPUTにST JJB00072が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00072 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00072 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00072
    $HASP395 JJB00072 ENDED - RC=0000
    ```

    $HASP373とJJB00072が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00072 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00072 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **TYPRUN=HOLD のリリース方法 確認手順**

    - 検証目的: TYPRUN=HOLD のリリース方法について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00073を表示し、JESJCLとJESYSMSGにあるTYPRUN=SCANと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00073 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00073
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00073
    ```

    COMMAND INPUTにST JJB00073が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00073 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,TYPRUN=SCAN
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにTYPRUN=SCANが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00073 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00073
    $HASP395 JJB00073 ENDED - RC=0000
    ```

    $HASP373とJJB00073が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00073 が画面・出力に表示されること
    ② ステップ2 の TYPRUN=SCAN が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00073 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND パラメータの目的 確認手順**

    - 検証目的: COND パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00074を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00074 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00074
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00074
    ```

    COMMAND INPUTにST JJB00074が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00074 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00074 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00074
    $HASP395 JJB00074 ENDED - RC=0000
    ```

    ICH70001IとJJB00074が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00074 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00074 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND=(code,operator) 構文 確認手順**

    - 検証目的: COND=(code,operator) 構文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00075を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00075 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00075
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00075
    ```

    COMMAND INPUTにST JJB00075が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00075 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00075 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00075
    $HASP395 JJB00075 ENDED - RC=0000
    ```

    $HASP373とJJB00075が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00075 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00075 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 LT 確認手順**

    - 検証目的: COND 演算子 LTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00076を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00076 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00076
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00076
    ```

    COMMAND INPUTにST JJB00076が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00076 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00076 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00076
    $HASP395 JJB00076 ENDED - RC=0000
    ```

    $HASP373とJJB00076が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00076 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00076 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 LE 確認手順**

    - 検証目的: COND 演算子 LEについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00077を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00077 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00077
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00077
    ```

    COMMAND INPUTにST JJB00077が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00077 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00077 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00077
    $HASP395 JJB00077 ENDED - RC=0000
    ```

    ICH70001IとJJB00077が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00077 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00077 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 EQ 確認手順**

    - 検証目的: COND 演算子 EQについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00078を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00078 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00078
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00078
    ```

    COMMAND INPUTにST JJB00078が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00078 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00078 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00078
    $HASP395 JJB00078 ENDED - RC=0000
    ```

    $HASP373とJJB00078が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00078 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00078 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 NE 確認手順**

    - 検証目的: COND 演算子 NEについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00079を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00079 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00079
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00079
    ```

    COMMAND INPUTにST JJB00079が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00079 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00079 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00079
    $HASP395 JJB00079 ENDED - RC=0000
    ```

    $HASP373とJJB00079が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00079 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00079 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 GT 確認手順**

    - 検証目的: COND 演算子 GTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00080を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00080 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00080
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00080
    ```

    COMMAND INPUTにST JJB00080が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00080 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00080 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00080
    $HASP395 JJB00080 ENDED - RC=0000
    ```

    ICH70001IとJJB00080が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00080 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00080 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 演算子 GE 確認手順**

    - 検証目的: COND 演算子 GEについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00081を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00081 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00081
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00081
    ```

    COMMAND INPUTにST JJB00081が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00081 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00081 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00081
    $HASP395 JJB00081 ENDED - RC=0000
    ```

    $HASP373とJJB00081が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00081 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00081 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND の解釈方向に注意 確認手順**

    - 検証目的: COND の解釈方向に注意について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00082を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00082 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00082
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00082
    ```

    COMMAND INPUTにST JJB00082が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00082 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00082 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00082
    $HASP395 JJB00082 ENDED - RC=0000
    ```

    $HASP373とJJB00082が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00082 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00082 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND 複数条件 (OR 結合) 確認手順**

    - 検証目的: COND 複数条件 (OR 結合)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00083を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00083 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00083
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00083
    ```

    COMMAND INPUTにST JJB00083が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00083 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00083 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00083
    $HASP395 JJB00083 ENDED - RC=0000
    ```

    ICH70001IとJJB00083が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00083 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00083 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND=EVEN 確認手順**

    - 検証目的: COND=EVENについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00084を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00084 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00084
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00084
    ```

    COMMAND INPUTにST JJB00084が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00084 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00084 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00084
    $HASP395 JJB00084 ENDED - RC=0000
    ```

    $HASP373とJJB00084が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00084 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00084 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND=ONLY 確認手順**

    - 検証目的: COND=ONLYについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00085を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00085 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00085
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00085
    ```

    COMMAND INPUTにST JJB00085が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00085 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00085 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00085
    $HASP395 JJB00085 ENDED - RC=0000
    ```

    $HASP373とJJB00085が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00085 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00085 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOB 文 COND の有効範囲 確認手順**

    - 検証目的: JOB 文 COND の有効範囲について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00086を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00086 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00086
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00086
    ```

    COMMAND INPUTにST JJB00086が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00086 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00086 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00086
    $HASP395 JJB00086 ENDED - RC=0000
    ```

    ICH70001IとJJB00086が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00086 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00086 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOB 文 COND と EXEC 文 COND の併用 確認手順**

    - 検証目的: JOB 文 COND と EXEC 文 COND の併用について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00087を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00087 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00087
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00087
    ```

    COMMAND INPUTにST JJB00087が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00087 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00087 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00087
    $HASP395 JJB00087 ENDED - RC=0000
    ```

    $HASP373とJJB00087が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00087 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00087 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND と IF/THEN/ELSE/ENDIF の関係 確認手順**

    - 検証目的: COND と IF/THEN/ELSE/ENDIF の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00088を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00088 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00088
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00088
    ```

    COMMAND INPUTにST JJB00088が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00088 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00088 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00088
    $HASP395 JJB00088 ENDED - RC=0000
    ```

    $HASP373とJJB00088が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00088 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00088 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND を IF 構造に置き換える推奨 確認手順**

    - 検証目的: COND を IF 構造に置き換える推奨について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00089を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00089 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00089
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00089
    ```

    COMMAND INPUTにST JJB00089が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00089 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00089 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00089
    $HASP395 JJB00089 ENDED - RC=0000
    ```

    ICH70001IとJJB00089が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00089 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00089 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART パラメータの目的 確認手順**

    - 検証目的: RESTART パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00090を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00090 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00090
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00090
    ```

    COMMAND INPUTにST JJB00090が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00090 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00090 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00090
    $HASP395 JJB00090 ENDED - RC=0000
    ```

    $HASP395とJJB00090が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00090 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00090 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART=stepname 確認手順**

    - 検証目的: RESTART=stepnameについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00091を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00091 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00091
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00091
    ```

    COMMAND INPUTにST JJB00091が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00091 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00091 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00091
    $HASP395 JJB00091 ENDED - RC=0000
    ```

    $HASP395とJJB00091が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00091 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00091 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART=stepname.procstep 確認手順**

    - 検証目的: RESTART=stepname.procstepについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00092を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00092 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00092
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00092
    ```

    COMMAND INPUTにST JJB00092が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00092 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00092 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00092
    $HASP395 JJB00092 ENDED - RC=0000
    ```

    ICH70001IとJJB00092が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00092 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00092 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART=* 確認手順**

    - 検証目的: RESTART=*について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00093を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00093 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00093
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00093
    ```

    COMMAND INPUTにST JJB00093が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00093 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00093 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00093
    $HASP395 JJB00093 ENDED - RC=0000
    ```

    $HASP395とJJB00093が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00093 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00093 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART=(stepname,checkid) 確認手順**

    - 検証目的: RESTART=(stepname,checkid)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00094を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00094 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00094
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00094
    ```

    COMMAND INPUTにST JJB00094が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00094 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00094 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00094
    $HASP395 JJB00094 ENDED - RC=0000
    ```

    $HASP395とJJB00094が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00094 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00094 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART と GDG 世代の関係 確認手順**

    - 検証目的: RESTART と GDG 世代の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00095を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00095 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00095
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00095
    ```

    COMMAND INPUTにST JJB00095が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00095 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00095 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00095
    $HASP395 JJB00095 ENDED - RC=0000
    ```

    ICH70001IとJJB00095が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00095 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00095 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART と DD DISP=(NEW,...) の整合 確認手順**

    - 検証目的: RESTART と DD DISP=(NEW,...) の整合について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00096を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00096 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00096
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00096
    ```

    COMMAND INPUTにST JJB00096が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00096 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00096 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00096
    $HASP395 JJB00096 ENDED - RC=0000
    ```

    $HASP395とJJB00096が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00096 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00096 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **RESTART と SYSCHK DD 確認手順**

    - 検証目的: RESTART と SYSCHK DDについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00097を表示し、JESJCLとJESYSMSGにあるRESTART=STEP1と$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00097 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00097
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00097
    ```

    COMMAND INPUTにST JJB00097が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00097 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,RESTART=STEP1
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにRESTART=STEP1が表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00097 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00097
    $HASP395 JJB00097 ENDED - RC=0000
    ```

    $HASP395とJJB00097が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00097 が画面・出力に表示されること
    ② ステップ2 の RESTART=STEP1 が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00097 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PRTY パラメータの目的 確認手順**

    - 検証目的: PRTY パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00098を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00098 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00098
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00098
    ```

    COMMAND INPUTにST JJB00098が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00098 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00098 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00098
    $HASP395 JJB00098 ENDED - RC=0000
    ```

    ICH70001IとJJB00098が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00098 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00098 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PRTY の値域 確認手順**

    - 検証目的: PRTY の値域について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00099を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00099 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00099
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00099
    ```

    COMMAND INPUTにST JJB00099が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00099 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00099 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00099
    $HASP395 JJB00099 ENDED - RC=0000
    ```

    $HASP373とJJB00099が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00099 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00099 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PRTY 省略時のデフォルト 確認手順**

    - 検証目的: PRTY 省略時のデフォルトについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00100を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00100 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00100
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00100
    ```

    COMMAND INPUTにST JJB00100が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00100 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00100 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00100
    $HASP395 JJB00100 ENDED - RC=0000
    ```

    $HASP373とJJB00100が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00100 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00100 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PRTY と WLM サービスクラスの関係 確認手順**

    - 検証目的: PRTY と WLM サービスクラスの関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00101を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00101 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00101
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00101
    ```

    COMMAND INPUTにST JJB00101が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00101 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00101 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00101
    $HASP395 JJB00101 ENDED - RC=0000
    ```

    ICH70001IとJJB00101が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00101 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00101 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **USER パラメータの目的 確認手順**

    - 検証目的: USER パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00102を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00102 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00102
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00102
    ```

    COMMAND INPUTにST JJB00102が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00102 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00102 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00102
    $HASP395 JJB00102 ENDED - RC=0000
    ```

    ICH70001IとJJB00102が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00102 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00102 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **USER の長さと文字種 確認手順**

    - 検証目的: USER の長さと文字種について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00103を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00103 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00103
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00103
    ```

    COMMAND INPUTにST JJB00103が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00103 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00103 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00103
    $HASP395 JJB00103 ENDED - RC=0000
    ```

    ICH70001IとJJB00103が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00103 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00103 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **USER 省略時のユーザ 確認手順**

    - 検証目的: USER 省略時のユーザについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00104を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00104 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00104
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00104
    ```

    COMMAND INPUTにST JJB00104が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00104 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00104 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00104
    $HASP395 JJB00104 ENDED - RC=0000
    ```

    ICH70001IとJJB00104が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00104 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00104 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PASSWORD パラメータの目的 確認手順**

    - 検証目的: PASSWORD パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00105を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00105 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00105
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00105
    ```

    COMMAND INPUTにST JJB00105が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00105 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00105 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00105
    $HASP395 JJB00105 ENDED - RC=0000
    ```

    ICH70001IとJJB00105が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00105 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00105 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PASSWORD 平文記述の危険性 確認手順**

    - 検証目的: PASSWORD 平文記述の危険性について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00106を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00106 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00106
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00106
    ```

    COMMAND INPUTにST JJB00106が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00106 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00106 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00106
    $HASP395 JJB00106 ENDED - RC=0000
    ```

    ICH70001IとJJB00106が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00106 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00106 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PASSWORD/NEWPWD 新旧切替 確認手順**

    - 検証目的: PASSWORD/NEWPWD 新旧切替について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00107を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00107 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00107
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00107
    ```

    COMMAND INPUTにST JJB00107が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00107 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00107 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00107
    $HASP395 JJB00107 ENDED - RC=0000
    ```

    ICH70001IとJJB00107が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00107 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00107 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **GROUP パラメータの目的 確認手順**

    - 検証目的: GROUP パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00108を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00108 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00108
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00108
    ```

    COMMAND INPUTにST JJB00108が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00108 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00108 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00108
    $HASP395 JJB00108 ENDED - RC=0000
    ```

    $HASP373とJJB00108が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00108 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00108 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **GROUP 省略時の動作 確認手順**

    - 検証目的: GROUP 省略時の動作について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00109を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00109 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00109
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00109
    ```

    COMMAND INPUTにST JJB00109が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00109 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00109 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00109
    $HASP395 JJB00109 ENDED - RC=0000
    ```

    ICH70001IとJJB00109が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00109 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00109 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SECLABEL パラメータの目的 確認手順**

    - 検証目的: SECLABEL パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00110を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00110 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00110
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00110
    ```

    COMMAND INPUTにST JJB00110が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00110 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00110 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00110
    $HASP395 JJB00110 ENDED - RC=0000
    ```

    ICH70001IとJJB00110が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00110 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00110 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SECLABEL と MLS 環境 確認手順**

    - 検証目的: SECLABEL と MLS 環境について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00111を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00111 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00111
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00111
    ```

    COMMAND INPUTにST JJB00111が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00111 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00111 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00111
    $HASP395 JJB00111 ENDED - RC=0000
    ```

    ICH70001IとJJB00111が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00111 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00111 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **Surrogate ユーザ運用 確認手順**

    - 検証目的: Surrogate ユーザ運用について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00112を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00112 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00112
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00112
    ```

    COMMAND INPUTにST JJB00112が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00112 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00112 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00112
    $HASP395 JJB00112 ENDED - RC=0000
    ```

    ICH70001IとJJB00112が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00112 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00112 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **NOTIFY パラメータの目的 確認手順**

    - 検証目的: NOTIFY パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00113を表示し、JESJCLとJESYSMSGにあるNOTIFY=&SYSUIDと$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00113 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00113
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00113
    ```

    COMMAND INPUTにST JJB00113が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00113 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにNOTIFY=&SYSUIDが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00113 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00113
    $HASP395 JJB00113 ENDED - RC=0000
    ```

    $HASP395とJJB00113が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00113 が画面・出力に表示されること
    ② ステップ2 の NOTIFY=&SYSUID が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00113 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **NOTIFY=&SYSUID 確認手順**

    - 検証目的: NOTIFY=&SYSUIDについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00114を表示し、JESJCLとJESYSMSGにあるNOTIFY=&SYSUIDと$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00114 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00114
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00114
    ```

    COMMAND INPUTにST JJB00114が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00114 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにNOTIFY=&SYSUIDが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00114 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00114
    $HASP395 JJB00114 ENDED - RC=0000
    ```

    $HASP395とJJB00114が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00114 が画面・出力に表示されること
    ② ステップ2 の NOTIFY=&SYSUID が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00114 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **NOTIFY=user.node 確認手順**

    - 検証目的: NOTIFY=user.nodeについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00115を表示し、JESJCLとJESYSMSGにあるNOTIFY=&SYSUIDと$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00115 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00115
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00115
    ```

    COMMAND INPUTにST JJB00115が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00115 JOB (ACCT),'OSKB',USER=OSKBUSR,SECLABEL=PUBLIC,NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにNOTIFY=&SYSUIDが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00115 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00115
    $HASP395 JJB00115 ENDED - RC=0000
    ```

    $HASP395とJJB00115が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00115 が画面・出力に表示されること
    ② ステップ2 の NOTIFY=&SYSUID が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00115 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **NOTIFY と TSO SEND の関係 確認手順**

    - 検証目的: NOTIFY と TSO SEND の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00116を表示し、JESJCLとJESYSMSGにあるNOTIFY=&SYSUIDと$HASP395を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00116 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00116
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00116
    ```

    COMMAND INPUTにST JJB00116が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00116 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにNOTIFY=&SYSUIDが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP395 JJB00116 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00116
    $HASP395 JJB00116 ENDED - RC=0000
    ```

    $HASP395とJJB00116が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00116 が画面・出力に表示されること
    ② ステップ2 の NOTIFY=&SYSUID が画面・出力に表示されること
    ③ ステップ3 の $HASP395 と JJB00116 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SCHENV パラメータの目的 確認手順**

    - 検証目的: SCHENV パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00117を表示し、JESJCLとJESYSMSGにあるSCHENV=BATCHENVと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00117 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00117
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00117
    ```

    COMMAND INPUTにST JJB00117が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00117 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,SCHENV=BATCHENV
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにSCHENV=BATCHENVが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00117 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00117
    $HASP395 JJB00117 ENDED - RC=0000
    ```

    $HASP373とJJB00117が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00117 が画面・出力に表示されること
    ② ステップ2 の SCHENV=BATCHENV が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00117 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SCHENV と Parallel Sysplex 確認手順**

    - 検証目的: SCHENV と Parallel Sysplexについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00118を表示し、JESJCLとJESYSMSGにあるSCHENV=BATCHENVと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00118 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00118
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00118
    ```

    COMMAND INPUTにST JJB00118が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00118 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,SCHENV=BATCHENV
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにSCHENV=BATCHENVが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00118 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00118
    $HASP395 JJB00118 ENDED - RC=0000
    ```

    $HASP373とJJB00118が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00118 が画面・出力に表示されること
    ② ステップ2 の SCHENV=BATCHENV が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00118 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SCHENV 未充足時の挙動 確認手順**

    - 検証目的: SCHENV 未充足時の挙動について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00119を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00119 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00119
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00119
    ```

    COMMAND INPUTにST JJB00119が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00119 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00119 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00119
    $HASP395 JJB00119 ENDED - RC=0000
    ```

    ICH70001IとJJB00119が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00119 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00119 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **ADDRSPC=VIRT 確認手順**

    - 検証目的: ADDRSPC=VIRTについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00120を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00120 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00120
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00120
    ```

    COMMAND INPUTにST JJB00120が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00120 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00120 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00120
    $HASP395 JJB00120 ENDED - RC=0000
    ```

    $HASP373とJJB00120が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00120 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00120 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **ADDRSPC=REAL 確認手順**

    - 検証目的: ADDRSPC=REALについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00121を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00121 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00121
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00121
    ```

    COMMAND INPUTにST JJB00121が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00121 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00121 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00121
    $HASP395 JJB00121 ENDED - RC=0000
    ```

    $HASP373とJJB00121が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00121 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00121 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **ADDRSPC=REAL の用途 確認手順**

    - 検証目的: ADDRSPC=REAL の用途について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00122を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00122 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00122
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00122
    ```

    COMMAND INPUTにST JJB00122が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00122 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00122 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00122
    $HASP395 JJB00122 ENDED - RC=0000
    ```

    ICH70001IとJJB00122が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00122 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00122 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **ADDRSPC=REAL と REGION 解釈 確認手順**

    - 検証目的: ADDRSPC=REAL と REGION 解釈について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00123を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00123 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00123
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00123
    ```

    COMMAND INPUTにST JJB00123が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00123 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00123 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00123
    $HASP395 JJB00123 ENDED - RC=0000
    ```

    IEF236IとJJB00123が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00123 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00123 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **BYTES パラメータの目的 確認手順**

    - 検証目的: BYTES パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00124を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00124 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00124
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00124
    ```

    COMMAND INPUTにST JJB00124が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00124 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00124 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00124
    $HASP395 JJB00124 ENDED - RC=0000
    ```

    $HASP373とJJB00124が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00124 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00124 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **BYTES=(N,option) 確認手順**

    - 検証目的: BYTES=(N,option)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00125を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00125 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00125
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00125
    ```

    COMMAND INPUTにST JJB00125が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00125 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00125 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00125
    $HASP395 JJB00125 ENDED - RC=0000
    ```

    ICH70001IとJJB00125が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00125 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00125 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CARDS パラメータの目的 確認手順**

    - 検証目的: CARDS パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00126を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00126 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00126
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00126
    ```

    COMMAND INPUTにST JJB00126が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00126 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00126 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00126
    $HASP395 JJB00126 ENDED - RC=0000
    ```

    $HASP373とJJB00126が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00126 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00126 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CARDS=(N,option) 確認手順**

    - 検証目的: CARDS=(N,option)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00127を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00127 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00127
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00127
    ```

    COMMAND INPUTにST JJB00127が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00127 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00127 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00127
    $HASP395 JJB00127 ENDED - RC=0000
    ```

    $HASP373とJJB00127が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00127 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00127 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **LINES パラメータの目的 確認手順**

    - 検証目的: LINES パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00128を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00128 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00128
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00128
    ```

    COMMAND INPUTにST JJB00128が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00128 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00128 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00128
    $HASP395 JJB00128 ENDED - RC=0000
    ```

    ICH70001IとJJB00128が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00128 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00128 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **LINES=(N,option) 確認手順**

    - 検証目的: LINES=(N,option)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00129を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00129 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00129
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00129
    ```

    COMMAND INPUTにST JJB00129が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00129 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00129 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00129
    $HASP395 JJB00129 ENDED - RC=0000
    ```

    $HASP373とJJB00129が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00129 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00129 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PAGES パラメータの目的 確認手順**

    - 検証目的: PAGES パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00130を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00130 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00130
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00130
    ```

    COMMAND INPUTにST JJB00130が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00130 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00130 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00130
    $HASP395 JJB00130 ENDED - RC=0000
    ```

    $HASP373とJJB00130が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00130 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00130 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PAGES=(N,option) 確認手順**

    - 検証目的: PAGES=(N,option)について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00131を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00131 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00131
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00131
    ```

    COMMAND INPUTにST JJB00131が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00131 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00131 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00131
    $HASP395 JJB00131 ENDED - RC=0000
    ```

    ICH70001IとJJB00131が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00131 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00131 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **BYTES/LINES と JES2 ESTBYTE/ESTLNCT の関係 確認手順**

    - 検証目的: BYTES/LINES と JES2 ESTBYTE/ESTLNCT の関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00132を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00132 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00132
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00132
    ```

    COMMAND INPUTにST JJB00132が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00132 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00132 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00132
    $HASP395 JJB00132 ENDED - RC=0000
    ```

    $HASP373とJJB00132が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00132 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00132 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PERFORM パラメータの目的 確認手順**

    - 検証目的: PERFORM パラメータの目的について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00133を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00133 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00133
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00133
    ```

    COMMAND INPUTにST JJB00133が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00133 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00133 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00133
    $HASP395 JJB00133 ENDED - RC=0000
    ```

    $HASP373とJJB00133が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00133 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00133 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **PERFORM の現状 確認手順**

    - 検証目的: PERFORM の現状について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00134を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00134 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00134
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00134
    ```

    COMMAND INPUTにST JJB00134が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00134 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00134 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00134
    $HASP395 JJB00134 ENDED - RC=0000
    ```

    ICH70001IとJJB00134が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00134 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00134 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JESLOG パラメータ 確認手順**

    - 検証目的: JESLOG パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00135を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00135 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00135
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00135
    ```

    COMMAND INPUTにST JJB00135が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00135 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00135 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00135
    $HASP395 JJB00135 ENDED - RC=0000
    ```

    $HASP373とJJB00135が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00135 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00135 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **DSENQSHR パラメータ 確認手順**

    - 検証目的: DSENQSHR パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00136を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00136 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00136
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00136
    ```

    COMMAND INPUTにST JJB00136が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00136 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00136 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00136
    $HASP395 JJB00136 ENDED - RC=0000
    ```

    $HASP373とJJB00136が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00136 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00136 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **REGIONX パラメータ 確認手順**

    - 検証目的: REGIONX パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00137を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00137 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00137
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00137
    ```

    COMMAND INPUTにST JJB00137が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00137 JOB (ACCT),'OSKB',CLASS=A,REGION=0M,TIME=1440
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00137 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00137
    $HASP395 JJB00137 ENDED - RC=0000
    ```

    IEF236IとJJB00137が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00137 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00137 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOBRC パラメータ 確認手順**

    - 検証目的: JOBRC パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00138を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00138 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00138
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00138
    ```

    COMMAND INPUTにST JJB00138が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00138 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00138 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00138
    $HASP395 JJB00138 ENDED - RC=0000
    ```

    $HASP373とJJB00138が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00138 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00138 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **EMAIL パラメータ 確認手順**

    - 検証目的: EMAIL パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00139を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00139 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00139
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00139
    ```

    COMMAND INPUTにST JJB00139が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00139 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00139 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00139
    $HASP395 JJB00139 ENDED - RC=0000
    ```

    $HASP373とJJB00139が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00139 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00139 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **CCSID パラメータ 確認手順**

    - 検証目的: CCSID パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00140を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00140 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00140
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00140
    ```

    COMMAND INPUTにST JJB00140が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00140 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00140 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00140
    $HASP395 JJB00140 ENDED - RC=0000
    ```

    ICH70001IとJJB00140が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00140 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00140 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **SYSAFF パラメータ 確認手順**

    - 検証目的: SYSAFF パラメータについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00141を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00141 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00141
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00141
    ```

    COMMAND INPUTにST JJB00141が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00141 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00141 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00141
    $HASP395 JJB00141 ENDED - RC=0000
    ```

    $HASP373とJJB00141が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00141 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00141 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **IF/THEN/ELSE/ENDIF の位置 確認手順**

    - 検証目的: IF/THEN/ELSE/ENDIF の位置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00142を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00142 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00142
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00142
    ```

    COMMAND INPUTにST JJB00142が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00142 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00142 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00142
    $HASP395 JJB00142 ENDED - RC=0000
    ```

    $HASP373とJJB00142が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00142 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00142 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **IF 条件と RC 参照 確認手順**

    - 検証目的: IF 条件と RC 参照について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00143を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00143 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00143
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00143
    ```

    COMMAND INPUTにST JJB00143が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00143 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00143 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00143
    $HASP395 JJB00143 ENDED - RC=0000
    ```

    ICH70001IとJJB00143が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00143 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00143 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **IF 条件と ABEND 検査 確認手順**

    - 検証目的: IF 条件と ABEND 検査について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00144を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00144 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00144
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00144
    ```

    COMMAND INPUTにST JJB00144が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00144 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00144 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00144
    $HASP395 JJB00144 ENDED - RC=0000
    ```

    $HASP373とJJB00144が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00144 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00144 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **IF 構造のネスト 確認手順**

    - 検証目的: IF 構造のネストについて、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00145を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00145 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00145
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00145
    ```

    COMMAND INPUTにST JJB00145が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00145 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00145 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00145
    $HASP395 JJB00145 ENDED - RC=0000
    ```

    $HASP373とJJB00145が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00145 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00145 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **COND と IF の併用時優先順位 確認手順**

    - 検証目的: COND と IF の併用時優先順位について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00146を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00146 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00146
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00146
    ```

    COMMAND INPUTにST JJB00146が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00146 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00146 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00146
    $HASP395 JJB00146 ENDED - RC=0000
    ```

    ICH70001IとJJB00146が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00146 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00146 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JES2 JOBCLASS の RESTART= 設定 確認手順**

    - 検証目的: JES2 JOBCLASS の RESTART= 設定について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00147を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00147 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00147
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00147
    ```

    COMMAND INPUTにST JJB00147が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00147 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00147 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00147
    $HASP395 JJB00147 ENDED - RC=0000
    ```

    $HASP373とJJB00147が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00147 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00147 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOB 文 IEFUJV 出口検証 確認手順**

    - 検証目的: JOB 文 IEFUJV 出口検証について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00148を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00148 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00148
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00148
    ```

    COMMAND INPUTにST JJB00148が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00148 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00148 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00148
    $HASP395 JJB00148 ENDED - RC=0000
    ```

    $HASP373とJJB00148が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00148 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00148 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOB 文 IEFUJI 出口 確認手順**

    - 検証目的: JOB 文 IEFUJI 出口について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00149を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00149 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00149
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00149
    ```

    COMMAND INPUTにST JJB00149が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00149 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00149 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00149
    $HASP395 JJB00149 ENDED - RC=0000
    ```

    ICH70001IとJJB00149が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00149 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00149 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JCLLIB 文との関係 確認手順**

    - 検証目的: JCLLIB 文との関係について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00150を表示し、JESJCLとJESYSMSGにあるJOBLIBとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00150 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00150
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00150
    ```

    COMMAND INPUTにST JJB00150が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00150 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //JOBLIB DD DSN=APP.LOADLIB,DISP=SHR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにJOBLIBが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00150 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00150
    $HASP395 JJB00150 ENDED - RC=0000
    ```

    IEF236IとJJB00150が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00150 が画面・出力に表示されること
    ② ステップ2 の JOBLIB が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00150 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOBLIB DD 文の位置 確認手順**

    - 検証目的: JOBLIB DD 文の位置について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00151を表示し、JESJCLとJESYSMSGにあるJOBLIBとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00151 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00151
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00151
    ```

    COMMAND INPUTにST JJB00151が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00151 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //JOBLIB DD DSN=APP.LOADLIB,DISP=SHR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにJOBLIBが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00151 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00151
    $HASP395 JJB00151 ENDED - RC=0000
    ```

    IEF236IとJJB00151が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00151 が画面・出力に表示されること
    ② ステップ2 の JOBLIB が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00151 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JOBPARM JES2 制御文 確認手順**

    - 検証目的: JOBPARM JES2 制御文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00152を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00152 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00152
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00152
    ```

    COMMAND INPUTにST JJB00152が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00152 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00152 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00152
    $HASP395 JJB00152 ENDED - RC=0000
    ```

    ICH70001IとJJB00152が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00152 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00152 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **ROUTE XEQ JES2 制御文 確認手順**

    - 検証目的: ROUTE XEQ JES2 制御文について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00153を表示し、JESJCLとJESYSMSGにあるROUTE XEQと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00153 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00153
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00153
    ```

    COMMAND INPUTにST JJB00153が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00153 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    /*ROUTE XEQ NODEA
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにROUTE XEQが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00153 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00153
    $HASP395 JJB00153 ENDED - RC=0000
    ```

    $HASP373とJJB00153が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00153 が画面・出力に表示されること
    ② ステップ2 の ROUTE XEQ が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00153 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **S322 — CPU 時間超過 確認手順**

    - 検証目的: S322 — CPU 時間超過について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00154を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00154 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00154
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00154
    ```

    COMMAND INPUTにST JJB00154が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00154 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,REGION=0M
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00154 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00154
    $HASP395 JJB00154 ENDED - RC=0000
    ```

    IEF236IとJJB00154が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00154 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00154 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **S722 — 出力上限超過 確認手順**

    - 検証目的: S722 — 出力上限超過について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00155を表示し、JESJCLとJESYSMSGにあるUSER=OSKBUSRとICH70001Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00155 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00155
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00155
    ```

    COMMAND INPUTにST JJB00155が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00155 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,USER=OSKBUSR
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにUSER=OSKBUSRが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    ICH70001I JJB00155 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00155
    $HASP395 JJB00155 ENDED - RC=0000
    ```

    ICH70001IとJJB00155が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00155 が画面・出力に表示されること
    ② ステップ2 の USER=OSKBUSR が画面・出力に表示されること
    ③ ステップ3 の ICH70001I と JJB00155 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **S822 — 領域不足 確認手順**

    - 検証目的: S822 — 領域不足について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00156を表示し、JESJCLとJESYSMSGにあるREGION=0MとIEF236Iを確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00156 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00156
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00156
    ```

    COMMAND INPUTにST JJB00156が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00156 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID,REGION=0M
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにREGION=0Mが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    IEF236I JJB00156 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00156
    $HASP395 JJB00156 ENDED - RC=0000
    ```

    IEF236IとJJB00156が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00156 が画面・出力に表示されること
    ② ステップ2 の REGION=0M が画面・出力に表示されること
    ③ ステップ3 の IEF236I と JJB00156 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

    ---

    **JCL ERROR JCL015 確認手順**

    - 検証目的: JCL ERROR JCL015について、JOB文の指定値、JESJCLの再掲、JESYSMSGのメッセージを机上で確認します。ジョブ一覧だけで完了扱いにせず、JOB文に指定した値がジョブログで追えることを確認します。
    - 前提条件: SDSFにログオン済みで、検証用ジョブのJESJCLとJESYSMSGを閲覧できる前提です。実機では変更管理承認を得て、業務ジョブではなく検証用JOB文を使用します。
    - セッション環境: SDSFでJJB00157を表示し、JESJCLとJESYSMSGにあるCLASS=Aと$HASP373を確認します。

    **ステップ 1**
    現在の画面はSDSFの基本メニューです。COMMAND INPUT ===> に ST JJB00157 を入力し、検証用ジョブを一覧表示します。
    操作（入力）:
    ```text
    (SDSF PRIMARY OPTION MENU)
    COMMAND INPUT ===> ST JJB00157
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF)
    COMMAND INPUT ===> ST JJB00157
    ```

    COMMAND INPUTにST JJB00157が表示され、対象ジョブの出力データセットを開く準備ができています。

    **ステップ 2**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESJCLを開き、JOB文の再掲値を確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESJCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESJCL)
    //JJB00157 JOB (ACCT),'OSKB',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
    //STEP1 EXEC PGM=IEFBR14
    ```

    JESJCLにCLASS=Aが表示されていれば、JOB文の指定値を再掲JCLで確認できます。

    **ステップ 3**
    現在の画面はSDSFのジョブデータセット一覧です。NP欄に S を入力してJESYSMSGを開き、JESメッセージを確認します。
    操作（入力）:
    ```text
    (SDSF Job Data Sets)
    NP   DDNAME
    S    JESYSMSG
    → Enter を押す
    ```

    画面・出力:
    ```text
    (SDSF Output JESYSMSG)
    $HASP373 JJB00157 STARTED - INIT 1 - CLASS A
    IEF236I ALLOC. FOR JJB00157
    $HASP395 JJB00157 ENDED - RC=0000
    ```

    $HASP373とJJB00157が同じ出力に現れるため、JOB文指定後のJES処理を確認できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> ST JJB00157 が画面・出力に表示されること
    ② ステップ2 の CLASS=A が画面・出力に表示されること
    ③ ステップ3 の $HASP373 と JJB00157 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: z / OS MVS JCL Reference、z / OS MVS JCL User's Guide

