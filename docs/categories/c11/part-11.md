---
search:
  exclude: true
---

# IBM IIDR 11.4 — 詳細 (11/11)

[← IBM IIDR 11.4 の概要へ戻る](index.md)


## IBM IIDR 11.4 > 複製状態監視

### apply task ログ位置照合 データソース {#c11-i0538}
*分類: 複製状態監視*  ・  難易度: 上級

IBM IIDR 11.4 の 複製状態監視 で扱う「apply task ログ位置照合 データソース」は、ターゲットへ変更を反映し適用済み位置を記録する処理をログ位置照合の観点で確認する技術項目です。list subscriptions の表とBMK076を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** apply task ログ位置照合 データソースの技術的な意味を資料で確認するとき、CDCミラーリング Event Severity 0049との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は復旧でミラー開始を証跡に残し・CDCのミラー開始と取得時刻を記録し。
    - B. コマンドまたは機能の用途は確認でDDL対象表を証跡に残し・DDLのDDL対象表と取得時刻を記録し。
    - C. コマンドまたは機能の用途はログ位置照合でデータソースを証跡に残し・ターゲットへ変更を反映し適用済み位置を記録する処理。 ✅
    - D. コマンドまたは機能の用途はログとの照合で通信統計を証跡に残し・CDC Communicationsで通信統計からSends。

    正解: **C** ／ 難易度: 上級

    **解説:** ログ・データ・データソでCの記述「ターゲットへ変更を反映し適用済み位置を記録する処理である」に対応する項目はログ位置照合 データソース（app・データ・データソ・ログ位）です。ログ位置時のデータソーに関する複製状態監視の仕様は「ターゲットへ変更を反映し適用済み位置を記録する処理」で、確認対象はapp・データ・データソ・ログ位です。ミラ・復旧・ミラー開のA:は「CDCのミラー開始と取得時刻を記録し、Refresh未完了の見落とし」を述べ、対象はEvent Severity（ミラー・ミラー・Refr・復旧）です。確認・DDL・ログ先頭のB:は「DDLのDDL対象表と取得時刻を記録し、ログ先頭未到達の見落としを防」を述べ、対象はTable Definition（後の表・DDL・ログ先頭・確認）です。通信統計をログとの照のD:は「CDC Communicationsで通信統計からSendsを読み」を述べ、対象はログとの照合 STAT07（CDC・通信統・送信回数・ログと）です。データソーをログ位置照という用語は「ターゲットへ変更を反映し適用済み位置を記録する処理」を指し、ログ位置照合 データソース（app・データ・データソ・ログ位）で照合する値はデータソースです。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **apply task ログ位置照合 データソース**

    - 検証目的: 複製状態監視のapply task ログ位置照合 データソースについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。list subscriptions の表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB076           DS076          Mirroring   BMK076
    ```

    画面・出力には Subscription が含まれ、apply task ログ位置照合 データソースの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、適用遅延を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB076           DS076          BMK076
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### apply task 失敗時切り分け 例外記録 {#c11-i0539}
*分類: 複製状態監視*  ・  難易度: 中級

IBM IIDR 11.4 の 複製状態監視 で扱う「apply task 失敗時切り分け 例外記録」は、ターゲットへ変更を反映し適用済み位置を記録する処理を失敗時切り分けの観点で確認する技術項目です。list subscriptions の表とBMK036を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** apply task 失敗時切り分け 例外記録の技術的な意味を資料で確認するとき、複製位置管理 Locale 0027との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は複製状態監視で例外記録を確認することで例外記録を確認し・例外記録の誤読を防ぐ。 ✅
    - B. 管理対象との関係を表す説明は監査操作で記録欄を比較することでサブスクリプを確認し・データ欠落を防ぐ。
    - C. 管理対象との関係を表す説明は監査操作で記録欄を比較することでインスタンスを確認し・データ欠落を防ぐ。
    - D. 管理対象との関係を表す説明はデータストアで障害切り分けを確認することで障害切り分けを確認し・ホスト名変更後の購読構成を更を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 複製状態対象applyでAの記述「ターゲットへ変更を反映し適用済み位置を記録する処理を失敗時切り分けと」に対応する項目は失敗時切り分け 例外記録（apply・複製状・例外記・例外記録）です。複製状態時のapplyに関する複製状態監視の仕様は「ターゲットへ変更を反映し適用済み位置を記録する処理を失敗時切り分けと」で、確認対象はappl・複製状・例外記・例外記録です。棚卸対象LocalのB:は「Localeのサブスクリプション名と取得時刻を記録し」を述べ、対象は複製位置管理 Locale（Local・棚卸・サブス・データ欠）です。確認時のHexのC:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・確認・インス・データ欠）です。障害切り分をデータスのD:は「CDC Datastoreで障害切り分けではデータストア接続の」を述べ、対象は障害切り分け STORE04（CDC・データ・障害切・ホスト名）です。applを複製状態監という用語は「ターゲットへ変更を反映し適用済み位置を記録する処理を」を指し、失敗時切り分け 例外記録（apply・複製状・例外記・例外記録）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **apply task 失敗時切り分け 例外記録**

    - 検証目的: 複製状態監視のapply task 失敗時切り分け 例外記録について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。list subscriptions の表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB036           DS036          Mirroring   BMK036
    ```

    画面・出力には Subscription が含まれ、apply task 失敗時切り分け 例外記録の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、適用遅延を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB036           DS036          BMK036
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### bookmark マッピング検査 対象表 {#c11-i0540}
*分類: 複製状態監視*  ・  難易度: 初級

IBM IIDR 11.4 の 複製状態監視 で扱う「bookmark マッピング検査 対象表」は、ログ上の適用位置と時刻を追跡する複製の進行点をマッピング検査の観点で確認する技術項目です。target datastore の統計とSUB004を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** bookmark マッピング検査 対象表の技術的な意味を資料で確認するとき、capture service 開始位置指定 検査エンジンとの境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はログ上の適用位置と時刻を追跡する複製の進行点をマッピング検査として確認する。複製状態監視で対象表を確認するときは対象表の誤読を防ぐ。 ✅
    - B. コマンドまたは機能の用途はソース変更を読み取りサブスクリプションへ渡す処理である。マッピングで検査エンジンを確認するときは検査エンジンの誤読を防ぐ。
    - C. コマンドまたは機能の用途はDDLの表定義再読込と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - D. コマンドまたは機能の用途はCDC Subscriptionで引継ぎ記録ではサブスクリプション管理のである。サブスクリプで引継ぎ記録でを確認するときは別サブスクリプションを停止まを防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 複製状態対象bookmでAの記述「ログ上の適用位置と時刻を追跡する複製の進行点をマッピング検査として確」に対応する項目はマッピング検査 対象表（bookm・複製状・対象表・対象表の）です。複製状態時のbookmに関する複製状態監視の仕様は「ログ上の適用位置と時刻を追跡する複製の進行点をマッピング検査として確」で、確認対象はbook・複製状・対象表・対象表のです。マッピン対象captuのB:は「ソース変更を読み取りサブスクリプションへ渡す処理」を述べ、対象は開始位置指定 検査エンジン（captu・マッピ・検査エ・検査エン）です。保守時の後の表定義のC:は「DDLの表定義再読込と取得時刻を記録し、ログ先頭未到達の見落としを防」を述べ、対象はSource Table（後の表定義・保守・表定義・ログ先頭）です。引継ぎ記録をサブスクのD:は「CDC Subscriptionで引継ぎ記録ではサブスクリプション管」を述べ、対象は引継ぎ記録 SUB09（CDC・サブス・引継ぎ・別サブス）です。bookを複製状態監という用語は「ログ上の適用位置と時刻を追跡する複製の進行点をマッピ」を指し、マッピング検査 対象表（bookm・複製状・対象表・対象表の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **bookmark マッピング検査 対象表**

    - 検証目的: 複製状態監視のbookmark マッピング検査 対象表について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。target datastore の統計を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB004           DS004          Mirroring   BMK004
    ```

    画面・出力には Subscription が含まれ、bookmark マッピング検査 対象表の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、再同期範囲の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB004           DS004          BMK004
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### bookmark 統計採取 回収対象 {#c11-i0541}
*分類: 複製状態監視*  ・  難易度: 中級

IBM IIDR 11.4 の 複製状態監視 で扱う「bookmark 統計採取 回収対象」は、ログ上の適用位置と時刻を追跡する複製の進行点を統計採取の観点で確認する技術項目です。target datastore の統計とSUB044を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** bookmark 統計採取 回収対象の技術的な意味を資料で確認するとき、CDCミラーリング Subscription 0061との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は監査でイベントログを証跡に残し・CDCのイベントログと取得時刻を記録し。
    - B. 構成を確認する際の意味は統計採取で回収対象を証跡に残し・ログ上の適用位置と時刻を追跡する複製の進行点を統計採取として。 ✅
    - C. 構成を確認する際の意味は切替でサブスクリプを証跡に残し・Localeのサブスクリプション名と取得時刻を記録し。
    - D. 構成を確認する際の意味は再始動確認で確認ではサブを証跡に残し・CDC Subscriptionで再始動後の確認ではサブスク。

    正解: **B** ／ 難易度: 中級

    **解説:** 統計採取対象bookmでBの記述「ログ上の適用位置と時刻を追跡する複製の進行点を統計採取として確認する」に対応する項目は統計採取 回収対象（bookm・統計採・回収対・回収対象）です。統計採取時のbookmに関する複製状態監視の仕様は「ログ上の適用位置と時刻を追跡する複製の進行点を統計採取として確認する」で、確認対象はbook・統計採・回収対・回収対象です。ミラーリン・監査のA:は「CDCのイベントログと取得時刻を記録し、Refresh未完了の見落と」を述べ、対象はCDCミラーリング Subscrip（ミラーリン・監査・イベン・Refr）です。切替時のLocalのC:は「Localeのサブスクリプション名と取得時刻を記録し、重複反映を防ぐ」を述べ、対象は複製位置管理 Locale（Local・切替・サブス・重複反映）です。確認ではサを再始動確のD:は「CDC Subscriptionで再始動後の確認ではサブスクリプショ」を述べ、対象は再始動後の確認 SUB15（CDC・再始動・確認で・別サブス）です。bookを統計採取という用語は「ログ上の適用位置と時刻を追跡する複製の進行点を統計採」を指し、統計採取 回収対象（bookm・統計採・回収対・回収対象）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **bookmark 統計採取 回収対象**

    - 検証目的: 複製状態監視のbookmark 統計採取 回収対象について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。target datastore の統計を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB044           DS044          Mirroring   BMK044
    ```

    画面・出力には Subscription が含まれ、bookmark 統計採取 回収対象の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、再同期範囲の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB044           DS044          BMK044
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### datastore 状態確認 イベント識別 {#c11-i0542}
*分類: 複製状態監視*  ・  難易度: 中級

IBM IIDR 11.4 の 複製状態監視 で扱う「datastore 状態確認 イベント識別」は、CDC Replication が接続するソースまたはターゲットの接続定義を状態確認の観点で確認する技術項目です。bookmark valueとLOG052を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** datastore 状態確認 イベント識別の技術的な意味を資料で確認するとき、CHC0368I マッピング検査 セッション上限との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は性能統計でセッション上を確認することでセッション上を確認し・セッション上の誤読を防ぐ。
    - B. コマンドまたは機能の用途は復旧操作で点検欄を確認することでログ先頭到達を確認し・DDL対象表の漏れを防ぐ。
    - C. コマンドまたは機能の用途は状態確認でイベント識別を確認することでイベント識別を確認し・イベント識別の誤読を防ぐ。 ✅
    - D. コマンドまたは機能の用途は購読再記述からMappedTableを読ことで購読再記述を確認し・DDL変更後に古い列定義で複を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 状態・イベン・イベントでCの記述「CDC Replication が接続するソースまたはターゲットの接」に対応する項目は状態確認 イベント識別（dat・イベン・イベント・状態確）です。状態確認時のイベント識に関する複製状態監視の仕様は「CDC Replication が接続するソースまたはターゲットの接」で、確認対象はdat・イベン・イベント・状態確です。マッ・性能・セッショのA:は「bookmark まで適用したことを示す CDC」を述べ、対象はマッピング検査 セッション上限（マッピ・セッシ・セッショ・性能統）です。収集・ログ先・DDL対のB:は「DDLのログ先頭到達と取得時刻を記録し、DDL対象表の漏れを防ぐ」を述べ、対象はDDL後の表定義更新（後の表・ログ先・DDL対・収集）です。購読再記述をマッピングのD:は「Table Mappingで購読再記述からMappedTableを読」を述べ、対象は引継ぎ記録 MAP09（Tab・購読再・DDL変・マッピ）です。イベント識を状態確認という用語は「CDC Replication」を指し、状態確認 イベント識別（dat・イベン・イベント・状態確）で照合する値はイベント識別です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **datastore 状態確認 イベント識別**

    - 検証目的: 複製状態監視のdatastore 状態確認 イベント識別について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。bookmark valueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB052           DS052          Mirroring   BMK052
    ```

    画面・出力には Subscription が含まれ、datastore 状態確認 イベント識別の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、対象表の不一致を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB052           DS052          BMK052
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### datastore 遅延監視 宛先定義 {#c11-i0543}
*分類: 複製状態監視*  ・  難易度: 初級

IBM IIDR 11.4 の 複製状態監視 で扱う「datastore 遅延監視 宛先定義」は、CDC Replication が接続するソースまたはターゲットの接続定義を遅延監視の観点で確認する技術項目です。bookmark valueとLOG012を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** datastore 遅延監視 宛先定義の技術的な意味を資料で確認するとき、DDL後の表定義更新 Head of Log 0026との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は表定義未更新を避けるため・点検操作で判定欄を記録するしてサブスクリプを照合する。
    - B. 管理対象との関係を表す説明はDDL対象表の漏れを避けるため・復旧操作で点検欄を確認するしてログ先頭到達を照合する。
    - C. 管理対象との関係を表す説明はIBM指示なしの位置変更を避けるため・主操作で出力欄を評価するして戻り値を照合する。
    - D. 管理対象との関係を表す説明は宛先定義の誤読を避けるため・複製状態監視で宛先定義を確認するして宛先定義を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 複製状態対象datasでDの記述「CDC Replication が接続するソースまたはターゲットの接」に対応する項目は遅延監視 宛先定義（datas・複製状・宛先定・宛先定義）です。複製状態時のdatasに関する複製状態監視の仕様は「CDC Replication が接続するソースまたはターゲットの接」で、確認対象はdata・複製状・宛先定・宛先定義です。後の表定義・棚卸のA:は「DDLのサブスクリプション記述と取得時刻を記録し、表定義未更新を防ぐ」を述べ、対象はof Log（後の表定義・棚卸・サブス・表定義未）です。診断対象後の表定義のB:は「DDLのログ先頭到達と取得時刻を記録し、DDL対象表の漏れを防ぐ」を述べ、対象はDDL後の表定義更新（後の表定義・診断・ログ先・DDL対）です。計画時のInstaのC:は「Instanceの戻り値と取得時刻を記録し」を述べ、対象は複製位置管理 Instance（Insta・計画・戻り値・IBM指）です。dataを複製状態監という用語は「CDC Replication」を指し、遅延監視 宛先定義（datas・複製状・宛先定・宛先定義）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **datastore 遅延監視 宛先定義**

    - 検証目的: 複製状態監視のdatastore 遅延監視 宛先定義について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。bookmark valueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB012           DS012          Mirroring   BMK012
    ```

    画面・出力には Subscription が含まれ、datastore 遅延監視 宛先定義の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、対象表の不一致を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB012           DS012          BMK012
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### performance statistics 初期同期判定 出力見出し {#c11-i0544}
*分類: 複製状態監視*  ・  難易度: 中級

IBM IIDR 11.4 の 複製状態監視 で扱う「performance statistics 初期同期判定 出力見出し」は、サブスクリプションやデータストアの処理量と遅延を測る情報を初期同期判定の観点で確認する技術項目です。CHC0368I メッセージとMAP028を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** performance statistics 初期同期判定 出力見出しの技術的な意味を資料で確認するとき、DDL後の表定義更新 Subscription 0032との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてログ先頭到達を照合する。
    - B. コマンドまたは機能の用途はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてミラー開始を照合する。
    - C. コマンドまたは機能の用途はデータ欠落を避けるため・監査操作で記録欄を比較するしてインスタンスを照合する。
    - D. コマンドまたは機能の用途は出力見出しの誤読を避けるため・初期同期判定で出力見出しを確認するして出力見出しを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 初期同期対象perfoでDの記述「サブスクリプションやデータストアの処理量と遅延を測る情報を初期同期判」に対応する項目は初期同期判定 出力見出し（perfo・初期同・出力見・出力見出）です。初期同期時のperfoに関する複製状態監視の仕様は「サブスクリプションやデータストアの処理量と遅延を測る情報を初期同期判」で、確認対象はperf・初期同・出力見・出力見出です。後の表定義・棚卸のA:は「DDLのログ先頭到達と取得時刻を記録し、ログ先頭未到達の見落としを防」を述べ、対象はDDL後の表定義更新（後の表定義・棚卸・ログ先・ログ先頭）です。診断対象ミラーリンのB:は「CDCのミラー開始と取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はEvent Severity（ミラーリン・診断・ミラー・イベント）です。解除時のHexのC:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・解除・インス・データ欠）です。perfを初期同期判という用語は「サブスクリプションやデータストアの処理量と遅延を測る」を指し、初期同期判定 出力見出し（perfo・初期同・出力見・出力見出）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **performance statistics 初期同期判定 出力見出し**

    - 検証目的: 複製状態監視のperformance statistics 初期同期判定 出力見出しについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。CHC0368I メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB028           DS028          Mirroring   BMK028
    ```

    画面・出力には Subscription が含まれ、performance statistics 初期同期判定 出力見出しの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、データストア接続失敗を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB028           DS028          BMK028
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### performance statistics 開始位置指定 画面タグ {#c11-i0545}
*分類: 複製状態監視*  ・  難易度: 上級

IBM IIDR 11.4 の 複製状態監視 で扱う「performance statistics 開始位置指定 画面タグ」は、サブスクリプションやデータストアの処理量と遅延を測る情報を開始位置指定の観点で確認する技術項目です。CHC0368I メッセージとMAP068を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** performance statistics 開始位置指定 画面タグの技術的な意味を資料で確認するとき、DDL後の表定義更新 Refresh Table 0023との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はRefresh中の再開を避けるため・表示操作で対象欄を追跡するして再開条件を照合する。
    - B. 構成を確認する際の意味は画面タグの誤読を避けるため・複製状態監視で画面タグを確認するして画面タグを照合する。 ✅
    - C. 構成を確認する際の意味は重複反映を避けるため・変更確認操作で採取欄を棚卸するして複製位置を照合する。
    - D. 構成を確認する際の意味はRefresh未完了でMirroを避けるため・方式変更からReturnvalueを読むして方式変更を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 複製・画面タ・画面タグでBの記述「サブスクリプションやデータストアの処理量と遅延を測る情報である」に対応する項目は開始位置指定 画面タグ（per・画面タ・画面タグ・複製状）です。複製状態時の画面タグに関する複製状態監視の仕様は「サブスクリプションやデータストアの処理量と遅延を測る情報」で、確認対象はper・画面タ・画面タグ・複製状です。後の・棚卸・再開条件のA:は「DDLの再開条件と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はRefresh Table（後の表・再開条・Refr・棚卸）です。確認時の複製位置のC:は「Bookmarkの複製位置と取得時刻を記録し、重複反映を防ぐ」を述べ、対象は複製位置管理 Bookmark（Boo・複製位・重複反映・確認）です。方式変更を復旧準備のD:は「CDC Refreshで方式変更からReturnvalueを読み」を述べ、対象は復旧準備 REF05（CDC・方式変・Refr・復旧準）です。画面タグを複製状態監という用語は「サブスクリプションやデータストアの処理量と遅延を測る」を指し、開始位置指定 画面タグ（per・画面タ・画面タグ・複製状）で照合する値は画面タグです。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **performance statistics 開始位置指定 画面タグ**

    - 検証目的: 複製状態監視のperformance statistics 開始位置指定 画面タグについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。CHC0368I メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB068           DS068          Mirroring   BMK068
    ```

    画面・出力には Subscription が含まれ、performance statistics 開始位置指定 画面タグの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、データストア接続失敗を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB068           DS068          BMK068
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### 複製状態監視 Mirror Status ログとの照合 MIR07 {#c11-i0546}
*分類: 複製状態監視*  ・  難易度: 中級

ログとの照合では 複製状態監視 の 状態表示 を主操作として MIR07 を判定します。時刻と対象識別子への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR07 に残します。ログとの照合を補助する イベント表示 では headoflog を補助値として MIR07 へ保存します。主判定のログとの照合では複製状態監視の 状態表示 から Latency を読み MIR07 へ残します。証跡照合のログとの照合では複製状態監視の Latency と headoflog を MIR07 に保存します。記録対応のログとの照合では複製状態監視の Table StatusとLatency の証跡へ MIR07 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status ログとの照合 MIR07の技術的な意味を資料で確認するとき、performance statistics 初期同期判定 出力見出しとの境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は状態表示からLatencyを読むことで状態表示を確認し・初期ロード中の表をMirroを防ぐ。 ✅
    - B. 管理対象との関係を表す説明は初期同期判定で出力見出しを確認することで出力見出しを確認し・出力見出しの誤読を防ぐ。
    - C. 管理対象との関係を表す説明は照合操作で確認欄を採取することで複製位置を確認し・対象インスタンスの取り違えを防ぐ。
    - D. 管理対象との関係を表す説明は記録操作で証跡欄を照合することでイベントログを確認し・初期ロード未完了の見落としを防ぐ。CDCミラーリング Subscription 0301固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能状態表・初期ロでAの記述「複製状態で状態表示から Latency を読み」に対応する項目はログとの照合 MIR07（複製状・状態表・ログと）です。照合状態表・ログとに関する複製状態監視の仕様は「複製状態で状態表示から Latency を読み、Latency と」で、確認対象は状態表・ログと・初期ロです。運用ログと・複製状でB:の初期同期判定 出力見出しは「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸は状態表・複製状・ログとです。項目状態表・ログとでC:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・複製状・状態表です。仕様状態表・ログとでD:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸はログと・初期ロ・状態表です。用語状態表・ログとという用語は「複製状態で状態表示から Latency を読み」を指し、照合する値と誤認リスクの組合せは複製状・状態表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status ログとの照合 MIR07**

    - 検証目的: 複製状態監視のMirror Statusについて操作とログを対応し、MIR07のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB07を指定し、MIR07の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB07
    Table: APP.MIR07
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB07を指定し、MIR07のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB07 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR07の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Latency が画面・出力に表示されること
    ② ステップ2 の Event が画面・出力に表示されること
    ③ ステップ3 の CHC9788I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 代替経路の確認 MIR10 {#c11-i0547}
*分類: 複製状態監視*  ・  難易度: 中級

代替経路の確認では 複製状態監視 の 状態表示 を主操作として MIR10 を判定します。主経路との役割差への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR10 に残します。代替経路の確認を補助する イベント表示 では headoflog を補助値として MIR10 へ保存します。主判定の代替経路の確認では複製状態監視の 状態表示 から Latency を読み MIR10 へ残します。証跡照合の代替経路の確認では複製状態監視の Latency と headoflog を MIR10 に保存します。記録対応の代替経路の確認では複製状態監視の Table StatusとLatency の証跡へ MIR10 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 代替経路の確認 MIR10の設定や表示を読む前に役割を確認します。ログ依存・サポート Log Dependency 依存関係の確認 LOG13ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは依存表示からOldestrequiredことで依存表示を確認し・休止購読を見落として必要ログを防ぐ。
    - B. 対象資源に対する働きは表示操作で対象欄を追跡することでデータ定義対を確認し・初期ロード中の再開を防ぐ。
    - C. 対象資源に対する働きは状態表示からLatencyを読むことで状態表示を確認し・初期ロード中の表をMirroを防ぐ。 ✅
    - D. 対象資源に対する働きは保守操作で監査欄を保存することでミラー開始を確認し・対象サブスクリプションの取りを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能状態表・初期ロでCの記述「複製状態で状態表示から Latency を読み」に対応する項目は代替経路の確認 MIR10（複製状・状態表・代替経）です。照合状態表・代替経に関する複製状態監視の仕様は「複製状態で状態表示から Latency を読み、Latency と」で、確認対象は状態表・代替経・初期ロです。比較複製状・代替経でA:の依存関係の確認 LOG13は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸は複製状・代替経・状態表です。運用代替経・複製状でB:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は状態表・複製状・代替経です。仕様状態表・代替経でD:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は代替経・初期ロ・状態表です。用語状態表・代替経という用語は「複製状態で状態表示から Latency を読み」を指し、照合する値と誤認リスクの組合せは複製状・状態表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 代替経路の確認 MIR10**

    - 検証目的: 複製状態監視のMirror Statusについて代替手段の成立を確認し、MIR10のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB10を指定し、MIR10の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB10
    Table: APP.MIR10
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB10を指定し、MIR10のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB10 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR10の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Latency が画面・出力に表示されること
    ② ステップ2 の Event が画面・出力に表示されること
    ③ ステップ3 の CHC9788I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 依存関係の確認 MIR13 {#c11-i0548}
*分類: 複製状態監視*  ・  難易度: 中級

依存関係の確認では 複製状態監視 の 状態表示 を主操作として MIR13 を判定します。前提資源と後続処理の順序への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR13 に残します。依存関係の確認を補助する イベント表示 では headoflog を補助値として MIR13 へ保存します。主判定の依存関係の確認では複製状態監視の 状態表示 から Latency を読み MIR13 へ残します。証跡照合の依存関係の確認では複製状態監視の Latency と headoflog を MIR13 に保存します。記録対応の依存関係の確認では複製状態監視の Table StatusとLatency の証跡へ MIR13 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 依存関係の確認 MIR13の役割を調べています。apply task 状態確認 構成配布の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は依存関係確認で状態表示を証跡に残し・複製状態で状態表示から Latency を読み。 ✅
    - B. 表示や設定で扱う内容は状態確認で構成配布を証跡に残し・ターゲットへ変更を反映し適用済み位置を記録する処理。
    - C. 表示や設定で扱う内容は変更で遅延確認を証跡に残し・変更データ取得の遅延確認と取得時刻を記録し。
    - D. 表示や設定で扱う内容は抑止で初期ロード状を証跡に残し・変更データ取得の初期ロード状態と取得時刻を記録し。CDCミラーリング Table Status 0295固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能状態表・初期ロでAの記述「複製状態で状態表示から Latency を読み」に対応する項目は依存関係の確認 MIR13（複製状・状態表・依存関）です。照合状態表・依存関に関する複製状態監視の仕様は「複製状態で状態表示から Latency を読み、Latency と」で、確認対象は状態表・依存関・初期ロです。運用依存関・複製状でB:の状態確認 構成配布は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は状態表・複製状・依存関です。項目状態表・依存関でC:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・複製状・状態表です。仕様状態表・依存関でD:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸は依存関・初期ロ・状態表です。用語状態表・依存関という用語は「複製状態で状態表示から Latency を読み」を指し、照合する値と誤認リスクの組合せは複製状・状態表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 依存関係の確認 MIR13**

    - 検証目的: 複製状態監視のMirror Statusについて依存資源を点検し、MIR13のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB13を指定し、MIR13の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB13
    Table: APP.MIR13
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB13を指定し、MIR13のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB13 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR13の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Latency が画面・出力に表示されること
    ② ステップ2 の Event が画面・出力に表示されること
    ③ ステップ3 の CHC9788I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 停止前の確認 MIR14 {#c11-i0549}
*分類: 複製状態監視*  ・  難易度: 中級

停止前の確認では 複製状態監視 の イベント表示 を主操作として MIR14 を判定します。処理中資源と未完了要求への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR14 に残します。停止前の確認を補助する 通信活動 では CHC9788I を補助値として MIR14 へ保存します。主判定の停止前の確認では複製状態監視の イベント表示 から headoflog を読み MIR14 へ残します。証跡照合の停止前の確認では複製状態監視の headoflog と CHC9788I を MIR14 に保存します。記録対応の停止前の確認では複製状態監視の Table StatusとLatency の証跡へ MIR14 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 停止前の確認 MIR14について構成や状態を確認します。subscription マッピング検査 保持期間ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はマッピングで保持期間を証跡に残し・複製対象の表対応と開始位置をまとめる管理単位をマッピング検査。
    - B. 一次資料が示す主目的は監査で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。
    - C. 一次資料が示す主目的は抑止でイベントログを証跡に残し・変更データ取得のイベントログと取得時刻を記録し。
    - D. 一次資料が示す主目的は停止確認でイベント表示を証跡に残し・複製状態でイベント表示から headoflog を読み。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでDの記述「複製状態でイベント表示から headoflog を読み」に対応する項目は停止前の確認 MIR14（複製状・イベン・停止確）です。照合イベン・停止確に関する複製状態監視の仕様は「複製状態でイベント表示から headoflog を読み」で、確認対象はイベン・停止確・初期ロです。比較複製状・停止確でA:のマッピング検査 保持期間は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は複製状・停止確・イベンです。運用停止確・複製状でB:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はイベン・複製状・停止確です。項目イベン・停止確でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は初期ロ・複製状・イベンです。用語イベン・停止確という用語は「複製状態でイベント表示から headoflog」を指し、照合する値と誤認リスクの組合せは複製状・イベン・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 停止前の確認 MIR14**

    - 検証目的: 複製状態監視のMirror Statusについて安全な停止条件を確認し、MIR14のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB14を指定し、MIR14のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB14 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR14の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB14を指定し、MIR14の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB14
    Table: APP.MIR14
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Event が画面・出力に表示されること
    ② ステップ2 の CHC9788I が画面・出力に表示されること
    ③ ステップ3 の Latency が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 再始動後の確認 MIR15 {#c11-i0550}
*分類: 複製状態監視*  ・  難易度: 中級

再始動後の確認では 複製状態監視 の 通信活動 を主操作として MIR15 を判定します。再開点と未処理データへの注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR15 に残します。再始動後の確認を補助する 状態表示 では Latency を補助値として MIR15 へ保存します。主判定の再始動後の確認では複製状態監視の 通信活動 から CHC9788I を読み MIR15 へ残します。証跡照合の再始動後の確認では複製状態監視の CHC9788I と Latency を MIR15 に保存します。記録対応の再始動後の確認では複製状態監視の Table StatusとLatency の証跡へ MIR15 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 再始動後の確認 MIR15の技術的な意味を資料で確認するとき、apply task マッピング検査 保存場所との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は複製状態で通信活動から CHC9788I を読み・CHC9788I と Latency を照合する。通信活動からCHC9788Iを読むときは初期ロード中の表をMirroを防ぐ。 ✅
    - B. 構成を確認する際の意味はターゲットへ変更を反映し適用済み位置を記録する処理をマッピング検査として確認する。データストアで保存場所を確認するときは保存場所の誤読を防ぐ。
    - C. 構成を確認する際の意味は後の表定義更新の項目のデータ定義対象表と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。DDL後の表定義更新 Table Definition 0104固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味はLocaleのサブスクリプション名と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能通信活・初期ロでAの記述「複製状態で通信活動から CHC9788I を読み」に対応する項目は再始動後の確認 MIR15（複製状・通信活・再始動）です。照合通信活・再始動に関する複製状態監視の仕様は「複製状態で通信活動から CHC9788I を読み、CHC9788I」で、確認対象は通信活・再始動・初期ロです。運用再始動・複製状でB:のマッピング検査 保存場所は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は通信活・複製状・再始動です。項目通信活・再始動でC:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は初期ロ・複製状・通信活です。仕様通信活・再始動でD:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は再始動・初期ロ・通信活です。用語通信活・再始動という用語は「複製状態で通信活動から CHC9788I を読み」を指し、照合する値と誤認リスクの組合せは複製状・通信活・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 再始動後の確認 MIR15**

    - 検証目的: 複製状態監視のMirror Statusについて再始動結果を検証し、MIR15のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR15の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB15を指定し、MIR15の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB15
    Table: APP.MIR15
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB15を指定し、MIR15のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB15 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CHC9788I が画面・出力に表示されること
    ② ステップ2 の Latency が画面・出力に表示されること
    ③ ステップ3 の Event が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 変更前の確認 MIR02 {#c11-i0551}
*分類: 複製状態監視*  ・  難易度: 中級

変更前の確認では 複製状態監視 の イベント表示 を主操作として MIR02 を判定します。変更対象と非対象の境界への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR02 に残します。変更前の確認を補助する 通信活動 では CHC9788I を補助値として MIR02 へ保存します。主判定の変更前の確認では複製状態監視の イベント表示 から headoflog を読み MIR02 へ残します。証跡照合の変更前の確認では複製状態監視の headoflog と CHC9788I を MIR02 に保存します。記録対応の変更前の確認では複製状態監視の Table StatusとLatency の証跡へ MIR02 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 変更前の確認 MIR02の設定や表示を読む前に役割を確認します。リフレッシュ制御 CDC Refresh 権限境界の確認 REF12ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は変更データ取得 初期ロードで完了確認から Rowsapplied を読み・Rowsapplied とである。完了確認からRowsappliedをときは初期ロード未完了でMirroを防ぐ。
    - B. 一次資料が示す主目的は変更データ取得の初期ロード状態と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - C. 一次資料が示す主目的は複製状態でイベント表示から headoflog を読み・headoflog と CHC9788I を照合する。イベント表示からheadoflogをときは初期ロード中の表をMirroを防ぐ。 ✅
    - D. 一次資料が示す主目的はサブスクリプションの16進ブックマークと取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。複製位置管理 Subscription 0315固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでCの記述「複製状態でイベント表示から headoflog を読み」に対応する項目は変更前の確認 MIR02（複製状・イベン・変更確）です。照合イベン・変更確に関する複製状態監視の仕様は「複製状態でイベント表示から headoflog を読み」で、確認対象はイベン・変更確・初期ロです。比較複製状・変更確でA:の権限境界の確認 REF12は「変更データ取得 初期ロードで完了確認から」を述べるため、正答側の照合軸は複製状・変更確・イベンです。運用変更確・複製状でB:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸はイベン・複製状・変更確です。仕様イベン・変更確でD:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は変更確・初期ロ・イベンです。用語イベン・変更確という用語は「複製状態でイベント表示から headoflog」を指し、照合する値と誤認リスクの組合せは複製状・イベン・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 変更前の確認 MIR02**

    - 検証目的: 複製状態監視のMirror Statusについて変更前の証跡を保存し、MIR02のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB02を指定し、MIR02のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB02 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR02の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB02を指定し、MIR02の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB02
    Table: APP.MIR02
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Event が画面・出力に表示されること
    ② ステップ2 の CHC9788I が画面・出力に表示されること
    ③ ステップ3 の Latency が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 変更後の確認 MIR03 {#c11-i0552}
*分類: 複製状態監視*  ・  難易度: 中級

変更後の確認では 複製状態監視 の 通信活動 を主操作として MIR03 を判定します。反映値と残存値への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR03 に残します。変更後の確認を補助する 状態表示 では Latency を補助値として MIR03 へ保存します。主判定の変更後の確認では複製状態監視の 通信活動 から CHC9788I を読み MIR03 へ残します。証跡照合の変更後の確認では複製状態監視の CHC9788I と Latency を MIR03 に保存します。記録対応の変更後の確認では複製状態監視の Table StatusとLatency の証跡へ MIR03 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 変更後の確認 MIR03を同一分類のリフレッシュ制御 CDC Refresh 依存関係の確認 REF13と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は依存関係確認で方式表示を証跡に残し・変更データ取得 初期ロードで方式表示から 初期ロードing。
    - B. 構成を確認する際の意味は移行で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 構成を確認する際の意味は変更確認で通信活動を証跡に残し・複製状態で通信活動から CHC9788I を読み。 ✅
    - D. 構成を確認する際の意味は解析でサブスクリプを証跡に残し・Localeのサブスクリプション名と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能通信活・初期ロでCの記述「複製状態で通信活動から CHC9788I を読み」に対応する項目は変更後の確認 MIR03（複製状・通信活・変更確）です。照合通信活・変更確に関する複製状態監視の仕様は「複製状態で通信活動から CHC9788I を読み、CHC9788I」で、確認対象は通信活・変更確・初期ロです。比較複製状・変更確でA:の依存関係の確認 REF13は「変更データ取得 初期ロードで方式表示から」を述べるため、正答側の照合軸は複製状・変更確・通信活です。運用変更確・複製状でB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は通信活・複製状・変更確です。仕様通信活・変更確でD:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は変更確・初期ロ・通信活です。用語通信活・変更確という用語は「複製状態で通信活動から CHC9788I を読み」を指し、照合する値と誤認リスクの組合せは複製状・通信活・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 変更後の確認 MIR03**

    - 検証目的: 複製状態監視のMirror Statusについて変更結果を検証し、MIR03のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR03の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB03を指定し、MIR03の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB03
    Table: APP.MIR03
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB03を指定し、MIR03のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB03 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CHC9788I が画面・出力に表示されること
    ② ステップ2 の Latency が画面・出力に表示されること
    ③ ステップ3 の Event が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 引継ぎ記録 MIR09 {#c11-i0553}
*分類: 複製状態監視*  ・  難易度: 中級

引継ぎ記録では 複製状態監視 の 通信活動 を主操作として MIR09 を判定します。次担当者が追跡できる証跡への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR09 に残します。引継ぎ記録を補助する 状態表示 では Latency を補助値として MIR09 へ保存します。主判定の引継ぎ記録では複製状態監視の 通信活動 から CHC9788I を読み MIR09 へ残します。証跡照合の引継ぎ記録では複製状態監視の CHC9788I と Latency を MIR09 に保存します。記録対応の引継ぎ記録では複製状態監視の Table StatusとLatency の証跡へ MIR09 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 引継ぎ記録 MIR09に関する障害切り分けの前提を確認しています。リフレッシュ制御 CDC Refresh 性能影響の確認 REF11の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては性能影響確認で方式変更を証跡に残し・変更データ取得 初期ロードで方式変更から。リフレッシュ制御 CDC Refresh 性能影響の確認 REF11固有の属性も確認対象に含める。
    - B. 機能の説明としては監査でイベントログを証跡に残し・変更データ取得のイベントログと取得時刻を記録し。
    - C. 機能の説明としては複製状態監視で通信活動を証跡に残し・複製状態で通信活動から CHC9788I を読み。 ✅
    - D. 機能の説明としては抑止でログ先頭到達を証跡に残し・後の表定義更新の項目のログ先頭到達と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能通信活・初期ロでCの記述「複製状態で通信活動から CHC9788I を読み」に対応する項目は引継ぎ記録 MIR09（複製状・通信活・複製状）です。照合通信活・複製状に関する複製状態監視の仕様は「複製状態で通信活動から CHC9788I を読み、CHC9788I」で、確認対象は通信活・複製状・初期ロです。比較複製状・複製状でA:の性能影響の確認 REF11は「変更データ取得 初期ロードで方式変更から」を述べるため、正答側の照合軸は複製状・複製状・通信活です。運用複製状・複製状でB:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は通信活・複製状・複製状です。仕様通信活・複製状でD:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は複製状・初期ロ・通信活です。用語通信活・複製状という用語は「複製状態で通信活動から CHC9788I を読み」を指し、照合する値と誤認リスクの組合せは複製状・通信活・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 引継ぎ記録 MIR09**

    - 検証目的: 複製状態監視のMirror Statusについて再現可能な記録を作成し、MIR09のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR09の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB09を指定し、MIR09の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB09
    Table: APP.MIR09
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB09を指定し、MIR09のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB09 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CHC9788I が画面・出力に表示されること
    ② ステップ2 の Latency が画面・出力に表示されること
    ③ ステップ3 の Event が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 復旧後の確認 MIR06 {#c11-i0554}
*分類: 複製状態監視*  ・  難易度: 中級

復旧後の確認では 複製状態監視 の 通信活動 を主操作として MIR06 を判定します。再発していないことを示す値への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR06 に残します。復旧後の確認を補助する 状態表示 では Latency を補助値として MIR06 へ保存します。主判定の復旧後の確認では複製状態監視の 通信活動 から CHC9788I を読み MIR06 へ残します。証跡照合の復旧後の確認では複製状態監視の CHC9788I と Latency を MIR06 に保存します。記録対応の復旧後の確認では複製状態監視の Table StatusとLatency の証跡へ MIR06 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 復旧後の確認 MIR06について構成や状態を確認します。性能統計 CDC Communications Activity 代替経路の確認ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは代替経路確認で通信統計を証跡に残し・変更データ取得 通信で通信統計から Sends を読み。
    - B. 状態を読み取るための働きは復旧でミラー開始を証跡に残し・変更データ取得のミラー開始と取得時刻を記録し。
    - C. 状態を読み取るための働きは解析でイベントログを証跡に残し・変更データ取得のイベントログと取得時刻を記録し。
    - D. 状態を読み取るための働きは復旧確認で通信活動を証跡に残し・複製状態で通信活動から CHC9788I を読み。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能通信活・初期ロでDの記述「複製状態で通信活動から CHC9788I を読み」に対応する項目は復旧後の確認 MIR06（複製状・通信活・復旧確）です。照合通信活・復旧確に関する複製状態監視の仕様は「複製状態で通信活動から CHC9788I を読み、CHC9788I」で、確認対象は通信活・復旧確・初期ロです。比較複製状・復旧確でA:の代替経路の確認 STAT10は「変更データ取得 通信で通信統計から」を述べるため、正答側の照合軸は複製状・復旧確・通信活です。運用復旧確・複製状でB:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は通信活・複製状・復旧確です。項目通信活・復旧確でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は初期ロ・複製状・通信活です。用語通信活・復旧確という用語は「複製状態で通信活動から CHC9788I を読み」を指し、照合する値と誤認リスクの組合せは複製状・通信活・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 復旧後の確認 MIR06**

    - 検証目的: 複製状態監視のMirror Statusについて復旧後の安定性を確認し、MIR06のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR06の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB06を指定し、MIR06の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB06
    Table: APP.MIR06
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB06を指定し、MIR06のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB06 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CHC9788I が画面・出力に表示されること
    ② ステップ2 の Latency が画面・出力に表示されること
    ③ ステップ3 の Event が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 復旧準備 MIR05 {#c11-i0555}
*分類: 複製状態監視*  ・  難易度: 中級

復旧準備では 複製状態監視 の イベント表示 を主操作として MIR05 を判定します。再開前に必要な整合性への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR05 に残します。復旧準備を補助する 通信活動 では CHC9788I を補助値として MIR05 へ保存します。主判定の復旧準備では複製状態監視の イベント表示 から headoflog を読み MIR05 へ残します。証跡照合の復旧準備では複製状態監視の headoflog と CHC9788I を MIR05 に保存します。記録対応の復旧準備では複製状態監視の Table StatusとLatency の証跡へ MIR05 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 復旧準備 MIR05の役割を調べています。リフレッシュ制御 CDC Refresh 引継ぎ記録 REF09の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は初期ロード未完了でMirrorへを避けるため・完了確認からRowsappliedを読むして完了確認を照合する。リフレッシュ制御 CDC Refresh 引継ぎ記録 REF09固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割は初期ロード中の表をMirror完を避けるため・イベント表示からheadoflogを読むしてイベント表示を照合する。 ✅
    - C. 障害切り分けに用いる役割はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして遅延確認を照合する。
    - D. 障害切り分けに用いる役割は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてミラー開始を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでBの記述「複製状態でイベント表示から headoflog を読み」に対応する項目は復旧準備 MIR05（複製状・イベン・復旧準）です。照合イベン・復旧準に関する複製状態監視の仕様は「複製状態でイベント表示から headoflog を読み」で、確認対象はイベン・復旧準・初期ロです。比較複製状・復旧準でA:の引継ぎ記録 REF09は「変更データ取得 初期ロードで完了確認から」を述べるため、正答側の照合軸は複製状・復旧準・イベンです。項目イベン・復旧準でC:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・複製状・イベンです。仕様イベン・復旧準でD:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は復旧準・初期ロ・イベンです。用語イベン・復旧準という用語は「複製状態でイベント表示から headoflog」を指し、照合する値と誤認リスクの組合せは複製状・イベン・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 復旧準備 MIR05**

    - 検証目的: 複製状態監視のMirror Statusについて復旧条件を確認し、MIR05のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB05を指定し、MIR05のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB05 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR05の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB05を指定し、MIR05の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB05
    Table: APP.MIR05
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Event が画面・出力に表示されること
    ② ステップ2 の CHC9788I が画面・出力に表示されること
    ③ ステップ3 の Latency が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 性能影響の確認 MIR11 {#c11-i0556}
*分類: 複製状態監視*  ・  難易度: 中級

性能影響の確認では 複製状態監視 の イベント表示 を主操作として MIR11 を判定します。処理時間と滞留箇所への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR11 に残します。性能影響の確認を補助する 通信活動 では CHC9788I を補助値として MIR11 へ保存します。主判定の性能影響の確認では複製状態監視の イベント表示 から headoflog を読み MIR11 へ残します。証跡照合の性能影響の確認では複製状態監視の headoflog と CHC9788I を MIR11 に保存します。記録対応の性能影響の確認では複製状態監視の Table StatusとLatency の証跡へ MIR11 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 性能影響の確認 MIR11を同一分類のログ依存・サポート Log Dependency 通常状態の確認 LOG01と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は通常状態確認で依存表示を証跡に残し・ログ依存で依存表示から Oldestrequired。
    - B. コマンドまたは機能の用途は性能影響確認でイベント表示を証跡に残し・複製状態でイベント表示から headoflog を読み。 ✅
    - C. コマンドまたは機能の用途は復旧でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。複製位置管理 Hex Position 0051固有の属性も確認対象に含める。
    - D. コマンドまたは機能の用途は保護で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでBの記述「複製状態でイベント表示から headoflog を読み」に対応する項目は性能影響の確認 MIR11（複製状・イベン・性能影）です。照合イベン・性能影に関する複製状態監視の仕様は「複製状態でイベント表示から headoflog を読み」で、確認対象はイベン・性能影・初期ロです。比較複製状・性能影でA:の通常状態の確認 LOG01は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸は複製状・性能影・イベンです。項目イベン・性能影でC:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は初期ロ・複製状・イベンです。仕様イベン・性能影でD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は性能影・初期ロ・イベンです。用語イベン・性能影という用語は「複製状態でイベント表示から headoflog」を指し、照合する値と誤認リスクの組合せは複製状・イベン・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 性能影響の確認 MIR11**

    - 検証目的: 複製状態監視のMirror Statusについて負荷と待ちを確認し、MIR11のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB11を指定し、MIR11のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB11 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR11の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB11を指定し、MIR11の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB11
    Table: APP.MIR11
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Event が画面・出力に表示されること
    ② ステップ2 の CHC9788I が画面・出力に表示されること
    ③ ステップ3 の Latency が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 構成監査 MIR08 {#c11-i0557}
*分類: 複製状態監視*  ・  難易度: 中級

構成監査では 複製状態監視 の イベント表示 を主操作として MIR08 を判定します。定義値と稼働値の一致への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR08 に残します。構成監査を補助する 通信活動 では CHC9788I を補助値として MIR08 へ保存します。主判定の構成監査では複製状態監視の イベント表示 から headoflog を読み MIR08 へ残します。証跡照合の構成監査では複製状態監視の headoflog と CHC9788I を MIR08 に保存します。記録対応の構成監査では複製状態監視の Table StatusとLatency の証跡へ MIR08 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 構成監査 MIR08を保守記録に説明する必要があります。capture service 統計採取 接続状態と取り違えない説明はどれですか。

    - A. 仕様上の役割は構成監査でイベント表示を証跡に残し・複製状態でイベント表示から headoflog を読み。 ✅
    - B. 仕様上の役割は統計採取で接続状態を証跡に残し・ソース変更を読み取りサブスクリプションへ渡す処理を統計採取と。
    - C. 仕様上の役割は監査でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。
    - D. 仕様上の役割は計画で遅延確認を証跡に残し・変更データ取得の遅延確認と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでAの記述「複製状態でイベント表示から headoflog を読み」に対応する項目は構成監査 MIR08（複製状・イベン・構成監）です。照合イベン・構成監に関する複製状態監視の仕様は「複製状態でイベント表示から headoflog を読み」で、確認対象はイベン・構成監・初期ロです。運用構成監・複製状でB:の統計採取 接続状態は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸はイベン・複製状・構成監です。項目イベン・構成監でC:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は初期ロ・複製状・イベンです。仕様イベン・構成監でD:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は構成監・初期ロ・イベンです。用語イベン・構成監という用語は「複製状態でイベント表示から headoflog」を指し、照合する値と誤認リスクの組合せは複製状・イベン・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 構成監査 MIR08**

    - 検証目的: 複製状態監視のMirror Statusについて構成差分を監査し、MIR08のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB08を指定し、MIR08のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB08 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR08の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB08を指定し、MIR08の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB08
    Table: APP.MIR08
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Event が画面・出力に表示されること
    ② ステップ2 の CHC9788I が画面・出力に表示されること
    ③ ステップ3 の Latency が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 権限境界の確認 MIR12 {#c11-i0558}
*分類: 複製状態監視*  ・  難易度: 中級

権限境界の確認では 複製状態監視 の 通信活動 を主操作として MIR12 を判定します。参照操作と変更操作の分離への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR12 に残します。権限境界の確認を補助する 状態表示 では Latency を補助値として MIR12 へ保存します。主判定の権限境界の確認では複製状態監視の 通信活動 から CHC9788I を読み MIR12 へ残します。証跡照合の権限境界の確認では複製状態監視の CHC9788I と Latency を MIR12 に保存します。記録対応の権限境界の確認では複製状態監視の Table StatusとLatency の証跡へ MIR12 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「複製状態監視 Mirror Status 権限境界の確認 MIR12」を「bookmark 遅延監視 適用位置」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はログ上の適用位置と時刻を追跡する複製の進行点を遅延監視として確認する。データストアで適用位置を確認するときは適用位置の誤読を防ぐ。
    - B. 運用時に利用する技術的役割はBookmarkの複製位置と取得時刻を記録し・ベンダー指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはベンダー指示なしの位置変更を防ぐ。複製位置管理 Bookmark 0069固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割は複製状態で通信活動から CHC9788I を読み・CHC9788I と Latency を照合する。通信活動からCHC9788Iを読むときは初期ロード中の表をMirroを防ぐ。 ✅
    - D. 運用時に利用する技術的役割はサブスクリプションの16進ブックマークと取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能通信活・初期ロでCの記述「複製状態で通信活動から CHC9788I を読み」に対応する項目は権限境界の確認 MIR12（複製状・通信活・権限境）です。照合通信活・権限境に関する複製状態監視の仕様は「複製状態で通信活動から CHC9788I を読み、CHC9788I」で、確認対象は通信活・権限境・初期ロです。比較複製状・権限境でA:の遅延監視 適用位置は「ログ上の適用位置と時刻を追跡する複製の進行点」を述べるため、正答側の照合軸は複製状・権限境・通信活です。運用権限境・複製状でB:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は通信活・複製状・権限境です。仕様通信活・権限境でD:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は権限境・初期ロ・通信活です。用語通信活・権限境という用語は「複製状態で通信活動から CHC9788I を読み」を指し、照合する値と誤認リスクの組合せは複製状・通信活・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 権限境界の確認 MIR12**

    - 検証目的: 複製状態監視のMirror Statusについて実行権限を点検し、MIR12のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR12の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB12を指定し、MIR12の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB12
    Table: APP.MIR12
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB12を指定し、MIR12のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB12 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CHC9788I が画面・出力に表示されること
    ② ステップ2 の Latency が画面・出力に表示されること
    ③ ステップ3 の Event が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 通常状態の確認 MIR01 {#c11-i0559}
*分類: 複製状態監視*  ・  難易度: 中級

通常状態の確認では 複製状態監視 の 状態表示 を主操作として MIR01 を判定します。基準値と現在値の差への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR01 に残します。通常状態の確認を補助する イベント表示 では headoflog を補助値として MIR01 へ保存します。主判定の通常状態の確認では複製状態監視の 状態表示 から Latency を読み MIR01 へ残します。証跡照合の通常状態の確認では複製状態監視の Latency と headoflog を MIR01 に保存します。記録対応の通常状態の確認では複製状態監視の Table StatusとLatency の証跡へ MIR01 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 複製状態監視 Mirror Status 通常状態の確認 MIR01に関する障害切り分けの前提を確認しています。subscription 状態確認 開始時刻の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は状態確認で開始時刻を確認することで開始時刻を確認し・開始時刻の誤読を防ぐ。
    - B. 表示や設定で扱う内容は採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。CDCミラーリング Subscription 0091固有の属性も確認対象に含める。
    - C. 表示や設定で扱う内容は状態表示からLatencyを読むことで状態表示を確認し・初期ロード中の表をMirroを防ぐ。 ✅
    - D. 表示や設定で扱う内容は保守操作で監査欄を保存することでサブスクリプを確認し・対象サブスクリプションの取りを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能状態表・初期ロでCの記述「複製状態で状態表示から Latency を読み」に対応する項目は通常状態の確認 MIR01（複製状・状態表・通常状）です。照合状態表・通常状に関する複製状態監視の仕様は「複製状態で状態表示から Latency を読み、Latency と」で、確認対象は状態表・通常状・初期ロです。比較複製状・通常状でA:の状態確認 開始時刻は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は複製状・通常状・状態表です。運用通常状・複製状でB:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は状態表・複製状・通常状です。仕様状態表・通常状でD:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は通常状・初期ロ・状態表です。用語状態表・通常状という用語は「複製状態で状態表示から Latency を読み」を指し、照合する値と誤認リスクの組合せは複製状・状態表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 通常状態の確認 MIR01**

    - 検証目的: 複製状態監視のMirror Statusについて通常状態を確定し、MIR01のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB01を指定し、MIR01の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB01
    Table: APP.MIR01
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB01を指定し、MIR01のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB01 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR01の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Latency が画面・出力に表示されること
    ② ステップ2 の Event が画面・出力に表示されること
    ③ ステップ3 の CHC9788I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 複製状態監視 Mirror Status 障害切り分け MIR04 {#c11-i0560}
*分類: 複製状態監視*  ・  難易度: 中級

障害切り分けでは 複製状態監視 の 状態表示 を主操作として MIR04 を判定します。最初に失敗した処理への注意として「Refresh中の表をMirror完了と誤認する危険があります」を MIR04 に残します。障害切り分けを補助する イベント表示 では headoflog を補助値として MIR04 へ保存します。主判定の障害切り分けでは複製状態監視の 状態表示 から Latency を読み MIR04 へ残します。証跡照合の障害切り分けでは複製状態監視の Latency と headoflog を MIR04 に保存します。記録対応の障害切り分けでは複製状態監視の Table StatusとLatency の証跡へ MIR04 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「複製状態監視 Mirror Status 障害切り分け MIR04」を「エラー処理 CDC Event Log 代替経路の確認 ERR10」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はイベント一覧から2931を読むことでイベント一覧を確認し・情報イベントと停止を伴うエラを防ぐ。
    - B. 保守作業で参照する機能は確認操作で状態欄を整理することでイベントログを確認し・遅延ゼロ確認の欠落を防ぐ。
    - C. 保守作業で参照する機能は監査操作で記録欄を比較することで16進ブックを確認し・データ欠落を防ぐ。
    - D. 保守作業で参照する機能は状態表示からLatencyを読むことで状態表示を確認し・初期ロード中の表をMirroを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能状態表・初期ロでDの記述「複製状態で状態表示から Latency を読み」に対応する項目は障害切り分け MIR04（複製状・状態表・複製状）です。照合状態表・複製状に関する複製状態監視の仕様は「複製状態で状態表示から Latency を読み、Latency と」で、確認対象は状態表・複製状・初期ロです。比較複製状・複製状でA:の代替経路の確認 ERR10は「変更データ取得 イベントログでイベント一覧か」を述べるため、正答側の照合軸は複製状・複製状・状態表です。運用複製状・複製状でB:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は状態表・複製状・複製状です。項目状態表・複製状でC:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は初期ロ・複製状・状態表です。用語状態表・複製状という用語は「複製状態で状態表示から Latency を読み」を指し、照合する値と誤認リスクの組合せは複製状・状態表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **複製状態監視 Mirror Status 障害切り分け MIR04**

    - 検証目的: 複製状態監視のMirror Statusについて障害範囲を限定し、MIR04のTable StatusとLatencyを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MIR04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB04を指定し、MIR04の状態表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB04
    Table: APP.MIR04
    Status: Mirroring
    Latency: 2 seconds
    ```

    画面・出力にあるLatencyを読み、Table StatusとLatencyと対象MIR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へdmshowevents -I SRC1 -s SUB04を指定し、MIR04のイベント表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowevents -I SRC1 -s SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Event 1204 Severity INFO Subscription SUB04 reached head of log
    ```

    画面・出力にあるEventを読み、Table StatusとLatencyと対象MIR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の複製状態監視を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=ALLを指定し、MIR04の通信活動を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 21002, Recvs = 20998
    ```

    画面・出力にあるCHC9788Iを読み、Table StatusとLatencyと対象MIR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Latency が画面・出力に表示されること
    ② ステップ2 の Event が画面・出力に表示されること
    ③ ステップ3 の CHC9788I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


