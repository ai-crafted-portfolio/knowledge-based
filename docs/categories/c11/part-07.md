---
search:
  exclude: true
---

# IBM IIDR 11.4 — 詳細 (7/11)

[← IBM IIDR 11.4 の概要へ戻る](index.md)


## IBM IIDR 11.4 > ブックマーク管理

### performance statistics マッピング検査 プール宛先 {#c11-i0324}
*分類: ブックマーク管理*  ・  難易度: 中級

IBM IIDR 11.4 の ブックマーク管理 で扱う「performance statistics マッピング検査 プール宛先」は、サブスクリプションやデータストアの処理量と遅延を測る情報をマッピング検査の観点で確認する技術項目です。CHC0368I メッセージとMAP048を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** performance statistics マッピング検査 プール宛先を同一分類の複製位置管理 Subscription 0060と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は監査で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - B. 管理対象との関係を表す説明はブックマークでプール宛先を証跡に残し・サブスクリプションやデータストアの処理量と遅延を測る情報をマ。 ✅
    - C. 管理対象との関係を表す説明は登録でサブスクリプを証跡に残し・CDCのサブスクリプション状態と取得時刻を記録し。
    - D. 管理対象との関係を表す説明は代替経路確認で代替経路の確を証跡に残し・CDC Datastoreで代替経路の確認ではデータストア接。

    正解: **B** ／ 難易度: 中級

    **解説:** ブックマ対象perfoでBの記述「サブスクリプションやデータストアの処理量と遅延を測る情報をマッピング」に対応する項目はマッピング検査 プール宛先（perfo・ブック・プール・プール宛）です。ブックマ時のperfoに関するブックマーク管理の仕様は「サブスクリプションやデータストアの処理量と遅延を測る情報をマッピング」で、確認対象はperf・ブック・プール・プール宛です。Subsc・監査のA:は「Subscriptionの16進ブックマークと取得時刻を記録し」を述べ、対象は複製位置管理 Subscriptio（Subsc・監査・16進・対象イン）です。登録時のミラーリンのC:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラーリン・登録・サブス・対象サブ）です。代替経路のを代替経路のD:は「CDC Datastoreで代替経路の確認ではデータストア接続の」を述べ、対象は代替経路の確認 STORE10（CDC・代替経・代替経・ホスト名）です。perfをブックマーという用語は「サブスクリプションやデータストアの処理量と遅延を測る」を指し、マッピング検査 プール宛先（perfo・ブック・プール・プール宛）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **performance statistics マッピング検査 プール宛先**

    - 検証目的: ブックマーク管理のperformance statistics マッピング検査 プール宛先について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ブックマーク管理の対象へ進みます。
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
    SUB048           DS048          Mirroring   BMK048
    ```

    画面・出力には Subscription が含まれ、performance statistics マッピング検査 プール宛先の証跡を確認できます。

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
    SUB048           DS048          BMK048
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### performance statistics 統計採取 差分確認 {#c11-i0325}
*分類: ブックマーク管理*  ・  難易度: 初級

IBM IIDR 11.4 の ブックマーク管理 で扱う「performance statistics 統計採取 差分確認」は、サブスクリプションやデータストアの処理量と遅延を測る情報を統計採取の観点で確認する技術項目です。CHC0368I メッセージとMAP008を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** performance statistics 統計採取 差分確認を同一分類のperformance statistics 失敗時切り分け 一覧画面と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はデータストアで一覧画面を確認することで一覧画面を確認し・一覧画面の誤読を防ぐ。
    - B. 構成を確認する際の意味は差分確認で差分確認を確認することで差分確認を確認し・差分確認の誤読を防ぐ。 ✅
    - C. 構成を確認する際の意味は表示操作で対象欄を追跡することで再開条件を確認し・Refresh中の再開を防ぐ。
    - D. 構成を確認する際の意味は権限境界確認で確認ではデーを確認することで確認ではデーを確認し・ホスト名変更後の購読構成を更を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 差分確認対象perfoでBの記述「サブスクリプションやデータストアの処理量と遅延を測る情報を統計採取と」に対応する項目は統計採取 差分確認（perfo・差分確・差分確・差分確認）です。差分確認時のperfoに関するブックマーク管理の仕様は「サブスクリプションやデータストアの処理量と遅延を測る情報を統計採取と」で、確認対象はperf・差分確・差分確・差分確認です。perfo・データストのA:は「サブスクリプションやデータストアの処理量と遅延を測る情報を失敗時切り」を述べ、対象は失敗時切り分け 一覧画面（perfo・データ・一覧画・一覧画面）です。登録時の後の表定義のC:は「DDLの再開条件と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はRefresh Table（後の表定義・登録・再開条・Refr）です。確認ではデを権限境界のD:は「CDC Datastoreで権限境界の確認ではデータストア接続の」を述べ、対象は権限境界の確認 STORE12（CDC・権限境・確認で・ホスト名）です。perfを差分確認という用語は「サブスクリプションやデータストアの処理量と遅延を測る」を指し、統計採取 差分確認（perfo・差分確・差分確・差分確認）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **performance statistics 統計採取 差分確認**

    - 検証目的: ブックマーク管理のperformance statistics 統計採取 差分確認について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ブックマーク管理の対象へ進みます。
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
    SUB008           DS008          Mirroring   BMK008
    ```

    画面・出力には Subscription が含まれ、performance statistics 統計採取 差分確認の証跡を確認できます。

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
    SUB008           DS008          BMK008
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I




## IBM IIDR 11.4 > マッピング管理

### CHCCLP マッピング検査 変換規則 {#c11-i0326}
*分類: マッピング管理*  ・  難易度: 中級

IBM IIDR 11.4 の マッピング管理 で扱う「CHCCLP マッピング検査 変換規則」は、CDC Replication のスクリプト操作に使うコマンドライン機能をマッピング検査の観点で確認する技術項目です。target datastore の統計とSUB019を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHCCLP マッピング検査 変換規則について構成や状態を確認します。複製位置管理 Hex Position 0006ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は重複反映を避けるため・変更確認操作で採取欄を棚卸するしてインスタンスを照合する。
    - B. 一次資料が示す主目的はRefresh中の再開を避けるため・表示操作で対象欄を追跡するしてDDL対象表を照合する。
    - C. 一次資料が示す主目的は変換規則の誤読を避けるため・マッピングで変換規則を確認するして変換規則を照合する。 ✅
    - D. 一次資料が示す主目的はDDL変更後に古い列定義で複製をを避けるため・再始動確認で再始動後の確を確認するして再始動後の確を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** マッピン対象マッピングでCの記述「CDC Replication のスクリプト操作に使うコマンドライン」に対応する項目はマッピング検査 変換規則（マッピング・マッピ・変換規・変換規則）です。マッピン時のマッピングに関するマッピング管理の仕様は「CDC Replication のスクリプト操作に使うコマンドライン」で、確認対象はマッピン・マッピ・変換規・変換規則です。Hex・巡回のA:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・巡回・インス・重複反映）です。切替対象後の表定義のB:は「DDLのDDL対象表と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はTable Definition（後の表定義・切替・DDL・Refr）です。Tablを再始動確認のD:は「Table Mappingで再始動後の確認ではマッピング管理の」を述べ、対象は再始動後の確認 MAP15（Table・再始動・再始動・DDL変）です。マッピンをマッピングという用語は「CDC Replication」を指し、マッピング検査 変換規則（マッピング・マッピ・変換規・変換規則）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHCCLP マッピング検査 変換規則**

    - 検証目的: マッピング管理のCHCCLP マッピング検査 変換規則について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB019           DS019          Mirroring   BMK019
    ```

    画面・出力には Subscription が含まれ、CHCCLP マッピング検査 変換規則の証跡を確認できます。

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
    SUB019           DS019          BMK019
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### CHCCLP 統計採取 詳細タブ {#c11-i0327}
*分類: マッピング管理*  ・  難易度: 中級

IBM IIDR 11.4 の マッピング管理 で扱う「CHCCLP 統計採取 詳細タブ」は、CDC Replication のスクリプト操作に使うコマンドライン機能を統計採取の観点で確認する技術項目です。target datastore の統計とSUB059を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHCCLP 統計採取 詳細タブについて構成や状態を確認します。CDCミラーリング Replication Method 0043ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは詳細タブの誤読を避けるため・統計採取で詳細タブを確認するして詳細タブを照合する。 ✅
    - B. 状態を読み取るための働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてサブスクリプを照合する。
    - C. 状態を読み取るための働きはデータ欠落を避けるため・監査操作で記録欄を比較するしてサブスクリプを照合する。
    - D. 状態を読み取るための働きは別サブスクリプションを停止またはを避けるため・イベント表示からSeverityを読むしてイベント表示を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 統計・詳細タ・詳細タブでAの記述「CDC Replication のスクリプト操作に使うコマンドライン」に対応する項目は統計採取 詳細タブ（統計採・詳細タ・詳細タブ・統計採）です。統計採取時の詳細タブに関するマッピング管理の仕様は「CDC Replication のスクリプト操作に使うコマンドライン」で、確認対象は統計採・詳細タ・詳細タブ・統計採です。復旧・サブス・イベントのB:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラー・サブス・イベント・復旧）です。登録時のサブスクリのC:は「Localeのサブスクリプション名と取得時刻を記録し」を述べ、対象は複製位置管理 Locale（Loc・サブス・データ欠・登録）です。イベント表を構成監査のD:は「CDC Subscriptionでイベント表示からSeverityを」を述べ、対象は構成監査 SUB08（CDC・イベン・別サブス・構成監）です。詳細タブを統計採取という用語は「CDC Replication」を指し、統計採取 詳細タブ（統計採・詳細タ・詳細タブ・統計採）で照合する値は詳細タブです。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHCCLP 統計採取 詳細タブ**

    - 検証目的: マッピング管理のCHCCLP 統計採取 詳細タブについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB059           DS059          Mirroring   BMK059
    ```

    画面・出力には Subscription が含まれ、CHCCLP 統計採取 詳細タブの証跡を確認できます。

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
    SUB059           DS059          BMK059
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### capture service 初期同期判定 取得間隔 {#c11-i0328}
*分類: マッピング管理*  ・  難易度: 中級

IBM IIDR 11.4 の マッピング管理 で扱う「capture service 初期同期判定 取得間隔」は、ソース変更を読み取りサブスクリプションへ渡す処理を初期同期判定の観点で確認する技術項目です。replication mapping 名とDS035を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** capture service 初期同期判定 取得間隔について構成や状態を確認します。CDCミラーリング Latency 0037ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはRefresh未完了の見落としを避けるため・記録操作で証跡欄を照合するして遅延確認を照合する。
    - B. 状態を読み取るための働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてRefresを照合する。
    - C. 状態を読み取るための働きは取得間隔の誤読を避けるため・初期同期判定で取得間隔を確認するして取得間隔を照合する。 ✅
    - D. 状態を読み取るための働きはRefresh中の表をMirroを避けるため・代替経路確認で代替経路の確を確認するして代替経路の確を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 初期同期対象captuでCの記述「ソース変更を読み取りサブスクリプションへ渡す処理を初期同期判定として」に対応する項目は初期同期判定 取得間隔（captu・初期同・取得間・取得間隔）です。初期同期時のcaptuに関するマッピング管理の仕様は「ソース変更を読み取りサブスクリプションへ渡す処理を初期同期判定として」で、確認対象はcapt・初期同・取得間・取得間隔です。ミラーリン・棚卸のA:は「CDCの遅延確認と取得時刻を記録し、Refresh未完了の見落としを」を述べ、対象はCDCミラーリング Latency（ミラーリン・棚卸・遅延確・Refr）です。確認対象ミラーリンのB:は「CDCのRefresh状態と取得時刻を記録し」を述べ、対象はTable Status（ミラーリン・確認・Ref・イベント）です。Mirrを代替経路確のD:は「Mirror Statusで代替経路の確認では複製状態監視の」を述べ、対象は代替経路の確認 MIR10（Mirro・代替経・代替経・Refr）です。captを初期同期判という用語は「ソース変更を読み取りサブスクリプションへ渡す処理を初」を指し、初期同期判定 取得間隔（captu・初期同・取得間・取得間隔）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **capture service 初期同期判定 取得間隔**

    - 検証目的: マッピング管理のcapture service 初期同期判定 取得間隔について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    現在の画面はIBM IIDR 11.4の確認画面です。replication mapping 名を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB035           DS035          Mirroring   BMK035
    ```

    画面・出力には Subscription が含まれ、capture service 初期同期判定 取得間隔の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、開始位置の取り違えを切り分けます。
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
    SUB035           DS035          BMK035
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### capture service 開始位置指定 検査エンジン {#c11-i0329}
*分類: マッピング管理*  ・  難易度: 上級

IBM IIDR 11.4 の マッピング管理 で扱う「capture service 開始位置指定 検査エンジン」は、ソース変更を読み取りサブスクリプションへ渡す処理を開始位置指定の観点で確認する技術項目です。replication mapping 名とDS075を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** capture service 開始位置指定 検査エンジンについて構成や状態を確認します。CDCミラーリング Latency 0022ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはマッピングで検査エンジンを確認することで検査エンジンを確認し・検査エンジンの誤読を防ぐ。 ✅
    - B. 対象資源に対する働きは確認操作で状態欄を整理することで遅延確認を確認し・遅延ゼロ確認の欠落を防ぐ。
    - C. 対象資源に対する働きは採取操作で照合欄を点検することでミラー開始を確認し・イベント重大度の誤読を防ぐ。
    - D. 対象資源に対する働きは表再読込からrefreshedを読むことで表再読込を確認し・DDL変更後に古い列定義で複を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** マッ・検査エ・検査エンでAの記述「ソース変更を読み取りサブスクリプションへ渡す処理である」に対応する項目は開始位置指定 検査エンジン（cap・検査エ・検査エン・マッピ）です。マッピン時の検査エンジに関するマッピング管理の仕様は「ソース変更を読み取りサブスクリプションへ渡す処理」で、確認対象はcap・検査エ・検査エン・マッピです。棚卸・遅延確・遅延ゼロのB:は「CDCの遅延確認と取得時刻を記録し、遅延ゼロ確認の欠落を防ぐ」を述べ、対象はCDCミラーリング Latency（ミラー・遅延確・遅延ゼロ・棚卸）です。保護時のミラー開始のC:は「CDCのミラー開始と取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はEvent Severity（ミラー・ミラー・イベント・保護）です。表再読込を性能影響確のD:は「Table Mappingで表再読込からrefreshedを読み」を述べ、対象は性能影響の確認 MAP11（Tab・表再読・DDL変・性能影）です。検査エンジをマッピングという用語は「ソース変更を読み取りサブスクリプションへ渡す処理」を指し、開始位置指定 検査エンジン（cap・検査エ・検査エン・マッピ）で照合する値は検査エンジンです。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **capture service 開始位置指定 検査エンジン**

    - 検証目的: マッピング管理のcapture service 開始位置指定 検査エンジンについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    現在の画面はIBM IIDR 11.4の確認画面です。replication mapping 名を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB075           DS075          Mirroring   BMK075
    ```

    画面・出力には Subscription が含まれ、capture service 開始位置指定 検査エンジンの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、開始位置の取り違えを切り分けます。
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
    SUB075           DS075          BMK075
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### refresh 状態確認 外部連携 {#c11-i0330}
*分類: マッピング管理*  ・  難易度: 上級

IBM IIDR 11.4 の マッピング管理 で扱う「refresh 状態確認 外部連携」は、対象表を初期同期または再同期する複製操作を状態確認の観点で確認する技術項目です。bookmark valueとLOG067を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** refresh 状態確認 外部連携について構成や状態を確認します。複製位置管理 Locale 0057ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は復旧でサブスクリプを証跡に残し・Localeのサブスクリプション名と取得時刻を記録し。
    - B. 一次資料が示す主目的は保護でイベントログを証跡に残し・CDCのイベントログと取得時刻を記録し。
    - C. 一次資料が示す主目的は状態確認で外部連携を証跡に残し・対象表を初期同期または再同期する複製操作。 ✅
    - D. 一次資料が示す主目的は変更確認でイベント確認を証跡に残し・CDC Datastoreでイベント確認からcommunic。

    正解: **C** ／ 難易度: 上級

    **解説:** 状態・外部連・外部連携でCの記述「対象表を初期同期または再同期する複製操作である」に対応する項目は状態確認 外部連携（ref・外部連・外部連携・状態確）です。状態確認時の外部連携に関するマッピング管理の仕様は「対象表を初期同期または再同期する複製操作」で、確認対象はref・外部連・外部連携・状態確です。Lo・復旧・サブスクのA:は「Localeのサブスクリプション名と取得時刻を記録し」を述べ、対象は複製位置管理 Locale（Loc・サブス・IBM指・復旧）です。保護・イベン・対象サブのB:は「CDCのイベントログと取得時刻を記録し、対象サブスクリプションの取り」を述べ、対象はCDCミラーリング Subscrip（ミラー・イベン・対象サブ・保護）です。イベント確を変更確認のD:は「CDC Datastoreでイベント確認からcommunicatio」を述べ、対象は変更後の確認 STORE03（CDC・イベン・ホスト名・変更確）です。外部連携を状態確認という用語は「対象表を初期同期または再同期する複製操作」を指し、状態確認 外部連携（ref・外部連・外部連携・状態確）で照合する値は外部連携です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **refresh 状態確認 外部連携**

    - 検証目的: マッピング管理のrefresh 状態確認 外部連携について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB067           DS067          Mirroring   BMK067
    ```

    画面・出力には Subscription が含まれ、refresh 状態確認 外部連携の証跡を確認できます。

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
    SUB067           DS067          BMK067
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### refresh 遅延監視 入力欄 {#c11-i0331}
*分類: マッピング管理*  ・  難易度: 中級

IBM IIDR 11.4 の マッピング管理 で扱う「refresh 遅延監視 入力欄」は、対象表を初期同期または再同期する複製操作を遅延監視の観点で確認する技術項目です。bookmark valueとLOG027を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** refresh 遅延監視 入力欄について構成や状態を確認します。複製位置管理 Instance 0003ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはデータ欠落を避けるため・監査操作で記録欄を比較するして戻り値を照合する。
    - B. 対象資源に対する働きはデータ欠落を避けるため・監査操作で記録欄を比較するして16進ブックを照合する。
    - C. 対象資源に対する働きはホスト名変更後の購読構成を更新せを避けるため・ログとの照合でログとの照合を確認するしてログとの照合を照合する。
    - D. 対象資源に対する働きは入力欄の誤読を避けるため・マッピングで入力欄を確認するして入力欄を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** マッピン対象refreでDの記述「対象表を初期同期または再同期する複製操作を遅延監視として確認する」に対応する項目は遅延監視 入力欄（refre・マッピ・入力欄・入力欄の）です。マッピン時のrefreに関するマッピング管理の仕様は「対象表を初期同期または再同期する複製操作を遅延監視として確認する」で、確認対象はrefr・マッピ・入力欄・入力欄のです。Insta・巡回のA:は「Instanceの戻り値と取得時刻を記録し、データ欠落を防ぐ」を述べ、対象は複製位置管理 Instance（Insta・巡回・戻り値・データ欠）です。収集対象SubscのB:は「Subscriptionの16進ブックマークと取得時刻を記録し」を述べ、対象は複製位置管理 Subscriptio（Subsc・収集・16進・データ欠）です。ログとの時のCDCのC:は「CDC Datastoreでログとの照合ではデータストア接続の」を述べ、対象はログとの照合 STORE07（CDC・ログと・ログと・ホスト名）です。refrをマッピングという用語は「対象表を初期同期または再同期する複製操作を遅延監視と」を指し、遅延監視 入力欄（refre・マッピ・入力欄・入力欄の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **refresh 遅延監視 入力欄**

    - 検証目的: マッピング管理のrefresh 遅延監視 入力欄について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB027           DS027          Mirroring   BMK027
    ```

    画面・出力には Subscription が含まれ、refresh 遅延監視 入力欄の証跡を確認できます。

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
    SUB027           DS027          BMK027
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### replication mapping ログ位置照合 接続先 {#c11-i0332}
*分類: マッピング管理*  ・  難易度: 初級

IBM IIDR 11.4 の マッピング管理 で扱う「replication mapping ログ位置照合 接続先」は、ソース表とターゲット表の対応および列変換を示す定義をログ位置照合の観点で確認する技術項目です。CHC0368I メッセージとMAP003を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** replication mapping ログ位置照合 接続先について構成や状態を確認します。CHCCLP 遅延監視 ドメイン値ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはCDC Replication のスクリプト操作に使うコマンドライン機能を遅延監視として確認する。サブスクリプでドメイン値を確認するときはドメイン値の誤読を防ぐ。
    - B. 対象資源に対する働きはソース表とターゲット表の対応および列変換を示す定義である。ログ位置照合で接続先を確認するときは接続先の誤読を防ぐ。 ✅
    - C. 対象資源に対する働きはCDCの遅延確認と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - D. 対象資源に対する働きはDDLの再開条件と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** ログ位置対象repliでBの記述「ソース表とターゲット表の対応および列変換を示す定義である」に対応する項目はログ位置照合 接続先（repli・ログ位・接続先・接続先の）です。ログ位置時のrepliに関するマッピング管理の仕様は「ソース表とターゲット表の対応および列変換を示す定義」で、確認対象はrepl・ログ位・接続先・接続先のです。遅延監視・サブスクリのA:は「CDC Replication のスクリプト操作に使うコマンドライン」を述べ、対象は遅延監視 ドメイン値（遅延監視・サブス・ドメイ・ドメイン）です。移行時のミラーリンのC:は「CDCの遅延確認と取得時刻を記録し、対象サブスクリプションの取り違え」を述べ、対象はCDCミラーリング Latency（ミラーリン・移行・遅延確・対象サブ）です。後の表定を計画のD:は「DDLの再開条件と取得時刻を記録し、表定義未更新を防ぐ」を述べ、対象はRefresh Table（後の表定義・計画・再開条・表定義未）です。replをログ位置照という用語は「ソース表とターゲット表の対応および列変換を示す定義」を指し、ログ位置照合 接続先（repli・ログ位・接続先・接続先の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **replication mapping ログ位置照合 接続先**

    - 検証目的: マッピング管理のreplication mapping ログ位置照合 接続先について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB003           DS003          Mirroring   BMK003
    ```

    画面・出力には Subscription が含まれ、replication mapping ログ位置照合 接続先の証跡を確認できます。

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
    SUB003           DS003          BMK003
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### replication mapping 失敗時切り分け 復元前提 {#c11-i0333}
*分類: マッピング管理*  ・  難易度: 中級

IBM IIDR 11.4 の マッピング管理 で扱う「replication mapping 失敗時切り分け 復元前提」は、ソース表とターゲット表の対応および列変換を示す定義を失敗時切り分けの観点で確認する技術項目です。CHC0368I メッセージとMAP043を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** replication mapping 失敗時切り分け 復元前提について構成や状態を確認します。replication mapping 遅延監視 受信操作ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はエラー処理で受信操作を証跡に残し・ソース表とターゲット表の対応および列変換を示す定義を遅延監視。
    - B. 一次資料が示す主目的は収集でログ先頭到達を証跡に残し・DDLのログ先頭到達と取得時刻を記録し。
    - C. 一次資料が示す主目的はマッピングで復元前提を証跡に残し・ソース表とターゲット表の対応および列変換を示す定義を失敗時切。 ✅
    - D. 一次資料が示す主目的はマッピングで障害切り分けを証跡に残し・Table Mappingで障害切り分けではマッピング管理の。

    正解: **C** ／ 難易度: 中級

    **解説:** マッピン対象repliでCの記述「ソース表とターゲット表の対応および列変換を示す定義を失敗時切り分けと」に対応する項目は失敗時切り分け 復元前提（repli・マッピ・復元前・復元前提）です。マッピン時のrepliに関するマッピング管理の仕様は「ソース表とターゲット表の対応および列変換を示す定義を失敗時切り分けと」で、確認対象はrepl・マッピ・復元前・復元前提です。repli・エラー処理のA:は「ソース表とターゲット表の対応および列変換を示す定義を遅延監視として確」を述べ、対象は遅延監視 受信操作（repli・エラー・受信操・受信操作）です。収集対象後の表定義のB:は「DDLのログ先頭到達と取得時刻を記録し、DDL対象表の漏れを防ぐ」を述べ、対象はDDL後の表定義更新（後の表定義・収集・ログ先・DDL対）です。TablをマッピングのD:は「Table Mappingで障害切り分けではマッピング管理の」を述べ、対象は障害切り分け MAP04（Table・マッピ・障害切・DDL変）です。replをマッピングという用語は「ソース表とターゲット表の対応および列変換を示す定義を」を指し、失敗時切り分け 復元前提（repli・マッピ・復元前・復元前提）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **replication mapping 失敗時切り分け 復元前提**

    - 検証目的: マッピング管理のreplication mapping 失敗時切り分け 復元前提について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB043           DS043          Mirroring   BMK043
    ```

    画面・出力には Subscription が含まれ、replication mapping 失敗時切り分け 復元前提の証跡を確認できます。

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
    SUB043           DS043          BMK043
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### subscription マッピング検査 保持期間 {#c11-i0334}
*分類: マッピング管理*  ・  難易度: 初級

IBM IIDR 11.4 の マッピング管理 で扱う「subscription マッピング検査 保持期間」は、複製対象の表対応と開始位置をまとめる管理単位をマッピング検査の観点で確認する技術項目です。list subscriptions の表とBMK011を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** subscription マッピング検査 保持期間について構成や状態を確認します。apply task 遅延監視 更新配布ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはターゲットへ変更を反映し適用済み位置を記録する処理を遅延監視として確認する。ブックマークで更新配布を確認するときは更新配布の誤読を防ぐ。
    - B. 状態を読み取るための働きはLocaleのサブスクリプション名と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - C. 状態を読み取るための働きはDDLのサブスクリプション記述と取得時刻を記録し・Refresh中の再開を防ぐである。表示操作で対象欄を追跡するときはRefresh中の再開を防ぐ。
    - D. 状態を読み取るための働きは複製対象の表対応と開始位置をまとめる管理単位をマッピング検査として確認する。マッピングで保持期間を確認するときは保持期間の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** マッピン対象subscでDの記述「複製対象の表対応と開始位置をまとめる管理単位をマッピング検査として確」に対応する項目はマッピング検査 保持期間（subsc・マッピ・保持期・保持期間）です。マッピン時のsubscに関するマッピング管理の仕様は「複製対象の表対応と開始位置をまとめる管理単位をマッピング検査として確」で、確認対象はsubs・マッピ・保持期・保持期間です。apply・ブックマーのA:は「ターゲットへ変更を反映し適用済み位置を記録する処理を遅延監視として確」を述べ、対象は遅延監視 更新配布（apply・ブック・更新配・更新配布）です。保守対象LocalのB:は「Localeのサブスクリプション名と取得時刻を記録し」を述べ、対象は複製位置管理 Locale（Local・保守・サブス・データ欠）です。解析時の後の表定義のC:は「DDLのサブスクリプション記述と取得時刻を記録し」を述べ、対象はof Log（後の表定義・解析・サブス・Refr）です。subsをマッピングという用語は「複製対象の表対応と開始位置をまとめる管理単位をマッピ」を指し、マッピング検査 保持期間（subsc・マッピ・保持期・保持期間）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **subscription マッピング検査 保持期間**

    - 検証目的: マッピング管理のsubscription マッピング検査 保持期間について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB011           DS011          Mirroring   BMK011
    ```

    画面・出力には Subscription が含まれ、subscription マッピング検査 保持期間の証跡を確認できます。

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
    SUB011           DS011          BMK011
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### subscription 統計採取 重大度 {#c11-i0335}
*分類: マッピング管理*  ・  難易度: 中級

IBM IIDR 11.4 の マッピング管理 で扱う「subscription 統計採取 重大度」は、複製対象の表対応と開始位置をまとめる管理単位を統計採取の観点で確認する技術項目です。list subscriptions の表とBMK051を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** subscription 統計採取 重大度について構成や状態を確認します。複製位置管理 Locale 0012ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはLocaleのサブスクリプション名と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。
    - B. 対象資源に対する働きはCDCの遅延確認と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。
    - C. 対象資源に対する働きは複製対象の表対応と開始位置をまとめる管理単位を統計採取として確認する。統計採取で重大度を確認するときは重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きはSubscriptionの16進ブックマークと取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 統計・重大度・重大度のでCの記述「複製対象の表対応と開始位置をまとめる管理単位を統計採取として確認する」に対応する項目は統計採取 重大度（sub・重大度・重大度の・統計採）です。統計採取時の重大度に関するマッピング管理の仕様は「複製対象の表対応と開始位置をまとめる管理単位を統計採取として確認する」で、確認対象はsub・重大度・重大度の・統計採です。Lo・巡回・サブスクのA:は「Localeのサブスクリプション名と取得時刻を記録し」を述べ、対象は複製位置管理 Locale（Loc・サブス・対象イン・巡回）です。収集・遅延確・イベントのB:は「CDCの遅延確認と取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はCDCミラーリング Latency（ミラー・遅延確・イベント・収集）です。16進ブッを承認のD:は「Subscriptionの16進ブックマークと取得時刻を記録し」を述べ、対象は複製位置管理 Subscriptio（Sub・16進・対象イン・承認）です。重大度を統計採取という用語は「複製対象の表対応と開始位置をまとめる管理単位を統計採」を指し、統計採取 重大度（sub・重大度・重大度の・統計採）で照合する値は重大度です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **subscription 統計採取 重大度**

    - 検証目的: マッピング管理のsubscription 統計採取 重大度について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、マッピング管理の対象へ進みます。
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
    SUB051           DS051          Mirroring   BMK051
    ```

    画面・出力には Subscription が含まれ、subscription 統計採取 重大度の証跡を確認できます。

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
    SUB051           DS051          BMK051
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### マッピング管理 Table Mapping ログとの照合 MAP07 {#c11-i0336}
*分類: マッピング管理*  ・  難易度: 中級

ログとの照合では マッピング管理 の 購読記述 を主操作として MAP07 を判定します。時刻と対象識別子への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP07 に残します。ログとの照合を補助する 表再読込 では refreshed を補助値として MAP07 へ保存します。主判定のログとの照合ではマッピング管理の 購読記述 から SourceTable を読み MAP07 へ残します。証跡照合のログとの照合ではマッピング管理の SourceTable と refreshed を MAP07 に保存します。記録対応のログとの照合ではマッピング管理の Source TableとTarget Table の証跡へ MAP07 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping ログとの照合 MAP07を保守記録に説明する必要があります。ログ依存・サポート Log Dependency 代替経路の確認 LOG10と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は依存表示からOldestrequiredことで依存表示を確認し・休止購読を見落として必要ログを防ぐ。
    - B. 保守作業で参照する機能は購読記述からSourceTableを読むことで購読記述を確認し・データ定義変更後に古い列定義を防ぐ。 ✅
    - C. 保守作業で参照する機能は照合操作で確認欄を採取することでサブスクリプを確認し・対象インスタンスの取り違えを防ぐ。
    - D. 保守作業で参照する機能は監査操作で記録欄を比較することでインスタンスを確認し・データ欠落を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能購読記・データでBの記述「表対応で購読記述から SourceTable を読み」に対応する項目はログとの照合 MAP07（表対応・購読記・ログと）です。照合購読記・ログとに関するマッピング管理の仕様は「表対応で購読記述から SourceTable を読み」で、確認対象は購読記・ログと・データです。比較マッピ・ログとでA:の代替経路の確認 LOG10は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸は表対応・ログと・購読記です。項目購読記・ログとでC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はデータ・マッピ・購読記です。仕様購読記・ログとでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はログと・データ・購読記です。用語購読記・ログとという用語は「表対応で購読記述から SourceTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読記・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping ログとの照合 MAP07**

    - 検証目的: マッピング管理のTable Mappingについて操作とログを対応し、MAP07のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB07を指定し、MAP07の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB07
    Source table: APP.MAP07
    Target table: DW.MAP07
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP07 -aを指定し、MAP07の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP07 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP07 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB07を指定し、MAP07の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP07 to DW.MAP07 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の refreshed が画面・出力に表示されること
    ③ ステップ3 の Mapped が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 代替経路の確認 MAP10 {#c11-i0337}
*分類: マッピング管理*  ・  難易度: 中級

代替経路の確認では マッピング管理 の 購読記述 を主操作として MAP10 を判定します。主経路との役割差への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP10 に残します。代替経路の確認を補助する 表再読込 では refreshed を補助値として MAP10 へ保存します。主判定の代替経路の確認ではマッピング管理の 購読記述 から SourceTable を読み MAP10 へ残します。証跡照合の代替経路の確認ではマッピング管理の SourceTable と refreshed を MAP10 に保存します。記録対応の代替経路の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP10 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 代替経路の確認 MAP10を同一分類のリフレッシュ制御 CDC Refresh ログとの照合 REF07と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は代替経路確認で購読記述を証跡に残し・表対応で購読記述から SourceTable を読み。 ✅
    - B. 管理対象との関係を表す説明はログとの照合で方式表示を証跡に残し・変更データ取得 初期ロードで方式表示から 初期ロードing。
    - C. 管理対象との関係を表す説明は復旧で16進ブックを証跡に残し・サブスクリプションの16進ブックマークと取得時刻を記録し。
    - D. 管理対象との関係を表す説明は解析で再開条件を証跡に残し・後の表定義更新の項目の再開条件と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能購読記・データでAの記述「表対応で購読記述から SourceTable を読み」に対応する項目は代替経路の確認 MAP10（表対応・購読記・代替経）です。照合購読記・代替経に関するマッピング管理の仕様は「表対応で購読記述から SourceTable を読み」で、確認対象は購読記・代替経・データです。運用代替経・表対応でB:のログとの照合 REF07は「変更データ取得 初期ロードで方式表示から」を述べるため、正答側の照合軸は購読記・マッピ・代替経です。項目購読記・代替経でC:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸はデータ・マッピ・購読記です。仕様購読記・代替経でD:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は代替経・データ・購読記です。用語購読記・代替経という用語は「表対応で購読記述から SourceTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読記・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 代替経路の確認 MAP10**

    - 検証目的: マッピング管理のTable Mappingについて代替手段の成立を確認し、MAP10のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB10を指定し、MAP10の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB10
    Source table: APP.MAP10
    Target table: DW.MAP10
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP10 -aを指定し、MAP10の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP10 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP10 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB10を指定し、MAP10の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP10 to DW.MAP10 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の refreshed が画面・出力に表示されること
    ③ ステップ3 の Mapped が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 依存関係の確認 MAP13 {#c11-i0338}
*分類: マッピング管理*  ・  難易度: 中級

依存関係の確認では マッピング管理 の 購読記述 を主操作として MAP13 を判定します。前提資源と後続処理の順序への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP13 に残します。依存関係の確認を補助する 表再読込 では refreshed を補助値として MAP13 へ保存します。主判定の依存関係の確認ではマッピング管理の 購読記述 から SourceTable を読み MAP13 へ残します。証跡照合の依存関係の確認ではマッピング管理の SourceTable と refreshed を MAP13 に保存します。記録対応の依存関係の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP13 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 依存関係の確認 MAP13について構成や状態を確認します。性能統計 CDC Communications Activity 変更後の確認ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは送信回数だけでターゲット適用完了を避けるため・ログ依存からOldestdependenしてログ依存を照合する。
    - B. 対象資源に対する働きは初期ロード中の再開を避けるため・表示操作で対象欄を追跡するしてサブスクリプを照合する。
    - C. 対象資源に対する働きはデータ定義変更後に古い列定義で複を避けるため・購読記述からSourceTableを読むして購読記述を照合する。 ✅
    - D. 対象資源に対する働きは対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するしてサブスクリプを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能購読記・データでCの記述「表対応で購読記述から SourceTable を読み」に対応する項目は依存関係の確認 MAP13（表対応・購読記・依存関）です。照合購読記・依存関に関するマッピング管理の仕様は「表対応で購読記述から SourceTable を読み」で、確認対象は購読記・依存関・データです。比較マッピ・依存関でA:の変更後の確認 STAT03は「変更データ取得 通信でログ依存から」を述べるため、正答側の照合軸は表対応・依存関・購読記です。運用依存関・表対応でB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は購読記・マッピ・依存関です。仕様購読記・依存関でD:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は依存関・データ・購読記です。用語購読記・依存関という用語は「表対応で購読記述から SourceTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読記・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 依存関係の確認 MAP13**

    - 検証目的: マッピング管理のTable Mappingについて依存資源を点検し、MAP13のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB13を指定し、MAP13の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB13
    Source table: APP.MAP13
    Target table: DW.MAP13
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP13 -aを指定し、MAP13の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP13 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP13 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB13を指定し、MAP13の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP13 to DW.MAP13 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の refreshed が画面・出力に表示されること
    ③ ステップ3 の Mapped が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 停止前の確認 MAP14 {#c11-i0339}
*分類: マッピング管理*  ・  難易度: 中級

停止前の確認では マッピング管理 の 表再読込 を主操作として MAP14 を判定します。処理中資源と未完了要求への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP14 に残します。停止前の確認を補助する 購読再記述 では MappedTable を補助値として MAP14 へ保存します。主判定の停止前の確認ではマッピング管理の 表再読込 から refreshed を読み MAP14 へ残します。証跡照合の停止前の確認ではマッピング管理の refreshed と MappedTable を MAP14 に保存します。記録対応の停止前の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP14 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 停止前の確認 MAP14の技術的な意味を資料で確認するとき、refresh 失敗時切り分け 詳細表示との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は詳細表示の誤読を避けるため・詳細表示で詳細表示を確認するして詳細表示を照合する。refresh 失敗時切り分け 詳細表示固有の属性も確認対象に含める。
    - B. コマンドまたは機能の用途はデータ定義変更後に古い列定義で複を避けるため・表再読込から初期ロードedを読むして表再読込を照合する。 ✅
    - C. コマンドまたは機能の用途はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして初期ロード状を照合する。
    - D. コマンドまたは機能の用途は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてミラー開始を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能表再読・データでBの記述「表対応で表再読込から 初期ロードed を読み」に対応する項目は停止前の確認 MAP14（表対応・表再読・停止確）です。照合表再読・停止確に関するマッピング管理の仕様は「表対応で表再読込から 初期ロードed を読み、初期ロードed と」で、確認対象は表再読・停止確・データです。比較マッピ・停止確でA:の失敗時切り分け 詳細表示は「対象表を初期同期または再同期する複製操作を失」を述べるため、正答側の照合軸は表対応・停止確・表再読です。項目表再読・停止確でC:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸はデータ・マッピ・表再読です。仕様表再読・停止確でD:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は停止確・データ・表再読です。用語表再読・停止確という用語は「表対応で表再読込から 初期ロードed を読み」を指し、照合する値と誤認リスクの組合せはマッピ・表再読・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 停止前の確認 MAP14**

    - 検証目的: マッピング管理のTable Mappingについて安全な停止条件を確認し、MAP14のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP14 -aを指定し、MAP14の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP14 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP14 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB14を指定し、MAP14の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP14 to DW.MAP14 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB14を指定し、MAP14の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB14
    Source table: APP.MAP14
    Target table: DW.MAP14
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の refreshed が画面・出力に表示されること
    ② ステップ2 の Mapped が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 再始動後の確認 MAP15 {#c11-i0340}
*分類: マッピング管理*  ・  難易度: 中級

再始動後の確認では マッピング管理 の 購読再記述 を主操作として MAP15 を判定します。再開点と未処理データへの注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP15 に残します。再始動後の確認を補助する 購読記述 では SourceTable を補助値として MAP15 へ保存します。主判定の再始動後の確認ではマッピング管理の 購読再記述 から MappedTable を読み MAP15 へ残します。証跡照合の再始動後の確認ではマッピング管理の MappedTable と SourceTable を MAP15 に保存します。記録対応の再始動後の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP15 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 再始動後の確認 MAP15を保守記録に説明する必要があります。エラー処理 CDC Event Log 変更前の確認 ERR02と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は変更データ取得 イベントログで通信エラーから ERROR を読み・ERROR と Support を照合する。通信エラーからERRORを読むときは情報イベントと停止を伴うエラを防ぐ。
    - B. 運用時に利用する技術的役割は後の表定義更新の項目のログ先頭到達と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。DDL後の表定義更新 Subscription 0107固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - D. 運用時に利用する技術的役割は表対応で購読再記述から MappedTable を読み・MappedTable と SourceTableである。購読再記述からMappedTableときはデータ定義変更後に古い列定義を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能購読再・データでDの記述「表対応で購読再記述から MappedTable を読み」に対応する項目は再始動後の確認 MAP15（表対応・購読再・再始動）です。照合購読再・再始動に関するマッピング管理の仕様は「表対応で購読再記述から MappedTable を読み」で、確認対象は購読再・再始動・データです。比較マッピ・再始動でA:の変更前の確認 ERR02は「変更データ取得 イベントログで通信エラーから」を述べるため、正答側の照合軸は表対応・再始動・購読再です。運用再始動・表対応でB:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は購読再・マッピ・再始動です。項目購読再・再始動でC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はデータ・マッピ・購読再です。用語購読再・再始動という用語は「表対応で購読再記述から MappedTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読再・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 再始動後の確認 MAP15**

    - 検証目的: マッピング管理のTable Mappingについて再始動結果を検証し、MAP15のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB15を指定し、MAP15の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP15 to DW.MAP15 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB15を指定し、MAP15の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB15
    Source table: APP.MAP15
    Target table: DW.MAP15
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP15 -aを指定し、MAP15の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP15 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP15 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Mapped が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の refreshed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 変更前の確認 MAP02 {#c11-i0341}
*分類: マッピング管理*  ・  難易度: 中級

変更前の確認では マッピング管理 の 表再読込 を主操作として MAP02 を判定します。変更対象と非対象の境界への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP02 に残します。変更前の確認を補助する 購読再記述 では MappedTable を補助値として MAP02 へ保存します。主判定の変更前の確認ではマッピング管理の 表再読込 から refreshed を読み MAP02 へ残します。証跡照合の変更前の確認ではマッピング管理の refreshed と MappedTable を MAP02 に保存します。記録対応の変更前の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP02 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 変更前の確認 MAP02を同一分類の複製状態監視 Mirror Status 復旧準備 MIR05と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は表対応で表再読込から 初期ロードed を読み・初期ロードed と MappedTable を照合する。表再読込から初期ロードedを読むときはデータ定義変更後に古い列定義を防ぐ。 ✅
    - B. コマンドまたは機能の用途は複製状態でイベント表示から headoflog を読み・headoflog と CHC9788I を照合する。イベント表示からheadoflogをときは初期ロード中の表をMirroを防ぐ。
    - C. コマンドまたは機能の用途は変更データ取得のサブスクリプション状態と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。
    - D. コマンドまたは機能の用途は後の表定義更新の項目のデータ定義対象表と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能表再読・データでAの記述「表対応で表再読込から 初期ロードed を読み」に対応する項目は変更前の確認 MAP02（表対応・表再読・変更確）です。照合表再読・変更確に関するマッピング管理の仕様は「表対応で表再読込から 初期ロードed を読み、初期ロードed と」で、確認対象は表再読・変更確・データです。運用変更確・表対応でB:の復旧準備 MIR05は「複製状態でイベント表示から」を述べるため、正答側の照合軸は表再読・マッピ・変更確です。項目表再読・変更確でC:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸はデータ・マッピ・表再読です。仕様表再読・変更確でD:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は変更確・データ・表再読です。用語表再読・変更確という用語は「表対応で表再読込から 初期ロードed を読み」を指し、照合する値と誤認リスクの組合せはマッピ・表再読・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 変更前の確認 MAP02**

    - 検証目的: マッピング管理のTable Mappingについて変更前の証跡を保存し、MAP02のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP02 -aを指定し、MAP02の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP02 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP02 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB02を指定し、MAP02の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP02 to DW.MAP02 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB02を指定し、MAP02の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB02
    Source table: APP.MAP02
    Target table: DW.MAP02
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の refreshed が画面・出力に表示されること
    ② ステップ2 の Mapped が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 変更後の確認 MAP03 {#c11-i0342}
*分類: マッピング管理*  ・  難易度: 中級

変更後の確認では マッピング管理 の 購読再記述 を主操作として MAP03 を判定します。反映値と残存値への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP03 に残します。変更後の確認を補助する 購読記述 では SourceTable を補助値として MAP03 へ保存します。主判定の変更後の確認ではマッピング管理の 購読再記述 から MappedTable を読み MAP03 へ残します。証跡照合の変更後の確認ではマッピング管理の MappedTable と SourceTable を MAP03 に保存します。記録対応の変更後の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP03 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「マッピング管理 Table Mapping 変更後の確認 MAP03」を「CHC0368I 開始位置指定 監査証跡」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は監査証跡の誤読を避けるため・監査証跡で監査証跡を確認するして監査証跡を照合する。
    - B. 運用時に利用する技術的役割はデータ定義変更後に古い列定義で複を避けるため・購読再記述からMappedTableを読して購読再記述を照合する。 ✅
    - C. 運用時に利用する技術的役割はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてイベントログを照合する。CDCミラーリング Subscription 0091固有の属性も確認対象に含める。
    - D. 運用時に利用する技術的役割は重複反映を避けるため・変更確認操作で採取欄を棚卸するして16進ブックを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能購読再・データでBの記述「表対応で購読再記述から MappedTable を読み」に対応する項目は変更後の確認 MAP03（表対応・購読再・変更確）です。照合購読再・変更確に関するマッピング管理の仕様は「表対応で購読再記述から MappedTable を読み」で、確認対象は購読再・変更確・データです。比較マッピ・変更確でA:の開始位置指定 監査証跡は「bookmark まで適用したことを示す」を述べるため、正答側の照合軸は表対応・変更確・購読再です。項目購読再・変更確でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸はデータ・マッピ・購読再です。仕様購読再・変更確でD:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は変更確・データ・購読再です。用語購読再・変更確という用語は「表対応で購読再記述から MappedTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読再・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 変更後の確認 MAP03**

    - 検証目的: マッピング管理のTable Mappingについて変更結果を検証し、MAP03のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB03を指定し、MAP03の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP03 to DW.MAP03 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB03を指定し、MAP03の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB03
    Source table: APP.MAP03
    Target table: DW.MAP03
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP03 -aを指定し、MAP03の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP03 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP03 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Mapped が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の refreshed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 引継ぎ記録 MAP09 {#c11-i0343}
*分類: マッピング管理*  ・  難易度: 中級

引継ぎ記録では マッピング管理 の 購読再記述 を主操作として MAP09 を判定します。次担当者が追跡できる証跡への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP09 に残します。引継ぎ記録を補助する 購読記述 では SourceTable を補助値として MAP09 へ保存します。主判定の引継ぎ記録ではマッピング管理の 購読再記述 から MappedTable を読み MAP09 へ残します。証跡照合の引継ぎ記録ではマッピング管理の MappedTable と SourceTable を MAP09 に保存します。記録対応の引継ぎ記録ではマッピング管理の Source TableとTarget Table の証跡へ MAP09 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 引継ぎ記録 MAP09の設定や表示を読む前に役割を確認します。複製状態監視 Mirror Status 引継ぎ記録 MIR09ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはデータ定義変更後に古い列定義で複を避けるため・購読再記述からMappedTableを読して購読再記述を照合する。 ✅
    - B. 状態を読み取るための働きは初期ロード中の表をMirror完を避けるため・通信活動からCHC9788Iを読むして通信活動を照合する。複製状態監視 Mirror Status 引継ぎ記録 MIR09固有の属性も確認対象に含める。
    - C. 状態を読み取るための働きは表定義未更新を避けるため・点検操作で判定欄を記録するして表定義再読込を照合する。
    - D. 状態を読み取るための働きはデータ欠落を避けるため・監査操作で記録欄を比較するしてインスタンスを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能購読再・データでAの記述「表対応で購読再記述から MappedTable を読み」に対応する項目は引継ぎ記録 MAP09（表対応・購読再・マッピ）です。照合購読再・マッピに関するマッピング管理の仕様は「表対応で購読再記述から MappedTable を読み」で、確認対象は購読再・マッピ・データです。運用マッピ・表対応でB:の引継ぎ記録 MIR09は「複製状態で通信活動から CHC9788I」を述べるため、正答側の照合軸は購読再・マッピ・マッピです。項目購読再・マッピでC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はデータ・マッピ・購読再です。仕様購読再・マッピでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はマッピ・データ・購読再です。用語購読再・マッピという用語は「表対応で購読再記述から MappedTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読再・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 引継ぎ記録 MAP09**

    - 検証目的: マッピング管理のTable Mappingについて再現可能な記録を作成し、MAP09のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB09を指定し、MAP09の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP09 to DW.MAP09 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB09を指定し、MAP09の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB09
    Source table: APP.MAP09
    Target table: DW.MAP09
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP09 -aを指定し、MAP09の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP09 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP09 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Mapped が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の refreshed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 復旧後の確認 MAP06 {#c11-i0344}
*分類: マッピング管理*  ・  難易度: 中級

復旧後の確認では マッピング管理 の 購読再記述 を主操作として MAP06 を判定します。再発していないことを示す値への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP06 に残します。復旧後の確認を補助する 購読記述 では SourceTable を補助値として MAP06 へ保存します。主判定の復旧後の確認ではマッピング管理の 購読再記述 から MappedTable を読み MAP06 へ残します。証跡照合の復旧後の確認ではマッピング管理の MappedTable と SourceTable を MAP06 に保存します。記録対応の復旧後の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP06 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 復旧後の確認 MAP06の技術的な意味を資料で確認するとき、ログ依存・サポート Log Dependency 復旧後の確認 LOG06との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はログ依存で支援情報から Returnvalue を読み・Returnvalue とである。支援情報からReturnvalueをときは休止購読を見落として必要ログを防ぐ。
    - B. 構成を確認する際の意味は表対応で購読再記述から MappedTable を読み・MappedTable と SourceTableである。購読再記述からMappedTableときはデータ定義変更後に古い列定義を防ぐ。 ✅
    - C. 構成を確認する際の意味は変更データ取得のイベントログと取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。CDCミラーリング Subscription 0076固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能購読再・データでBの記述「表対応で購読再記述から MappedTable を読み」に対応する項目は復旧後の確認 MAP06（表対応・購読再・復旧確）です。照合購読再・復旧確に関するマッピング管理の仕様は「表対応で購読再記述から MappedTable を読み」で、確認対象は購読再・復旧確・データです。比較マッピ・復旧確でA:の復旧後の確認 LOG06は「ログ依存で支援情報から Returnvalu」を述べるため、正答側の照合軸は表対応・復旧確・購読再です。項目購読再・復旧確でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸はデータ・マッピ・購読再です。仕様購読再・復旧確でD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は復旧確・データ・購読再です。用語購読再・復旧確という用語は「表対応で購読再記述から MappedTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読再・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 復旧後の確認 MAP06**

    - 検証目的: マッピング管理のTable Mappingについて復旧後の安定性を確認し、MAP06のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB06を指定し、MAP06の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP06 to DW.MAP06 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB06を指定し、MAP06の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB06
    Source table: APP.MAP06
    Target table: DW.MAP06
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP06 -aを指定し、MAP06の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP06 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP06 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Mapped が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の refreshed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 復旧準備 MAP05 {#c11-i0345}
*分類: マッピング管理*  ・  難易度: 中級

復旧準備では マッピング管理 の 表再読込 を主操作として MAP05 を判定します。再開前に必要な整合性への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP05 に残します。復旧準備を補助する 購読再記述 では MappedTable を補助値として MAP05 へ保存します。主判定の復旧準備ではマッピング管理の 表再読込 から refreshed を読み MAP05 へ残します。証跡照合の復旧準備ではマッピング管理の refreshed と MappedTable を MAP05 に保存します。記録対応の復旧準備ではマッピング管理の Source TableとTarget Table の証跡へ MAP05 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 復旧準備 MAP05について構成や状態を確認します。ログ依存・サポート Log Dependency 性能影響の確認 LOG11ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は性能影響確認で購読確認を証跡に残し・ログ依存で購読確認から Inactive を読み。
    - B. 一次資料が示す主目的は移行で再開条件を証跡に残し・後の表定義更新の項目の再開条件と取得時刻を記録し。
    - C. 一次資料が示す主目的は登録で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - D. 一次資料が示す主目的は復旧準備で表再読込を証跡に残し・表対応で表再読込から 初期ロードed を読み。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能表再読・データでDの記述「表対応で表再読込から 初期ロードed を読み」に対応する項目は復旧準備 MAP05（表対応・表再読・復旧準）です。照合表再読・復旧準に関するマッピング管理の仕様は「表対応で表再読込から 初期ロードed を読み、初期ロードed と」で、確認対象は表再読・復旧準・データです。比較マッピ・復旧準でA:の性能影響の確認 LOG11は「ログ依存で購読確認から Inactive」を述べるため、正答側の照合軸は表対応・復旧準・表再読です。運用復旧準・表対応でB:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は表再読・マッピ・復旧準です。項目表再読・復旧準でC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はデータ・マッピ・表再読です。用語表再読・復旧準という用語は「表対応で表再読込から 初期ロードed を読み」を指し、照合する値と誤認リスクの組合せはマッピ・表再読・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 復旧準備 MAP05**

    - 検証目的: マッピング管理のTable Mappingについて復旧条件を確認し、MAP05のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP05 -aを指定し、MAP05の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP05 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP05 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB05を指定し、MAP05の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP05 to DW.MAP05 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB05を指定し、MAP05の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB05
    Source table: APP.MAP05
    Target table: DW.MAP05
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の refreshed が画面・出力に表示されること
    ② ステップ2 の Mapped が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 性能影響の確認 MAP11 {#c11-i0346}
*分類: マッピング管理*  ・  難易度: 中級

性能影響の確認では マッピング管理 の 表再読込 を主操作として MAP11 を判定します。処理時間と滞留箇所への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP11 に残します。性能影響の確認を補助する 購読再記述 では MappedTable を補助値として MAP11 へ保存します。主判定の性能影響の確認ではマッピング管理の 表再読込 から refreshed を読み MAP11 へ残します。証跡照合の性能影響の確認ではマッピング管理の refreshed と MappedTable を MAP11 に保存します。記録対応の性能影響の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP11 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「マッピング管理 Table Mapping 性能影響の確認 MAP11」を「subscription 状態確認 開始時刻」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は表再読込から初期ロードedを読むことで表再読込を確認し・データ定義変更後に古い列定義を防ぐ。 ✅
    - B. 仕様上の役割は状態確認で開始時刻を確認することで開始時刻を確認し・開始時刻の誤読を防ぐ。
    - C. 仕様上の役割は採取操作で照合欄を点検することで初期ロード状を確認し・イベント重大度の誤読を防ぐ。CDCミラーリング Table Status 0115固有の属性も確認対象に含める。
    - D. 仕様上の役割は点検操作で判定欄を記録することでサブスクリプを確認し・表定義未更新を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能表再読・データでAの記述「表対応で表再読込から 初期ロードed を読み」に対応する項目は性能影響の確認 MAP11（表対応・表再読・性能影）です。照合表再読・性能影に関するマッピング管理の仕様は「表対応で表再読込から 初期ロードed を読み、初期ロードed と」で、確認対象は表再読・性能影・データです。運用性能影・表対応でB:の状態確認 開始時刻は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は表再読・マッピ・性能影です。項目表再読・性能影でC:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸はデータ・マッピ・表再読です。仕様表再読・性能影でD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は性能影・データ・表再読です。用語表再読・性能影という用語は「表対応で表再読込から 初期ロードed を読み」を指し、照合する値と誤認リスクの組合せはマッピ・表再読・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 性能影響の確認 MAP11**

    - 検証目的: マッピング管理のTable Mappingについて負荷と待ちを確認し、MAP11のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP11 -aを指定し、MAP11の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP11 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP11 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB11を指定し、MAP11の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP11 to DW.MAP11 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB11を指定し、MAP11の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB11
    Source table: APP.MAP11
    Target table: DW.MAP11
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の refreshed が画面・出力に表示されること
    ② ステップ2 の Mapped が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 構成監査 MAP08 {#c11-i0347}
*分類: マッピング管理*  ・  難易度: 中級

構成監査では マッピング管理 の 表再読込 を主操作として MAP08 を判定します。定義値と稼働値の一致への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP08 に残します。構成監査を補助する 購読再記述 では MappedTable を補助値として MAP08 へ保存します。主判定の構成監査ではマッピング管理の 表再読込 から refreshed を読み MAP08 へ残します。証跡照合の構成監査ではマッピング管理の refreshed と MappedTable を MAP08 に保存します。記録対応の構成監査ではマッピング管理の Source TableとTarget Table の証跡へ MAP08 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 構成監査 MAP08に関する障害切り分けの前提を確認しています。リフレッシュ制御 CDC Refresh 構成監査 REF08の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は変更データ取得 初期ロードで方式変更から Returnvalue を読み・Returnvalue とである。方式変更からReturnvalueをときは初期ロード未完了でMirroを防ぐ。
    - B. 障害切り分けに用いる役割はHex Positionのインスタンス名と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - C. 障害切り分けに用いる役割は表対応で表再読込から 初期ロードed を読み・初期ロードed と MappedTable を照合する。表再読込から初期ロードedを読むときはデータ定義変更後に古い列定義を防ぐ。 ✅
    - D. 障害切り分けに用いる役割はLocaleのサブスクリプション名と取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能表再読・データでCの記述「表対応で表再読込から 初期ロードed を読み」に対応する項目は構成監査 MAP08（表対応・表再読・構成監）です。照合表再読・構成監に関するマッピング管理の仕様は「表対応で表再読込から 初期ロードed を読み、初期ロードed と」で、確認対象は表再読・構成監・データです。比較マッピ・構成監でA:の構成監査 REF08は「変更データ取得 初期ロードで方式変更から」を述べるため、正答側の照合軸は表対応・構成監・表再読です。運用構成監・表対応でB:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は表再読・マッピ・構成監です。仕様表再読・構成監でD:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は構成監・データ・表再読です。用語表再読・構成監という用語は「表対応で表再読込から 初期ロードed を読み」を指し、照合する値と誤認リスクの組合せはマッピ・表再読・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 構成監査 MAP08**

    - 検証目的: マッピング管理のTable Mappingについて構成差分を監査し、MAP08のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP08 -aを指定し、MAP08の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP08 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP08 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB08を指定し、MAP08の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP08 to DW.MAP08 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB08を指定し、MAP08の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB08
    Source table: APP.MAP08
    Target table: DW.MAP08
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の refreshed が画面・出力に表示されること
    ② ステップ2 の Mapped が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 権限境界の確認 MAP12 {#c11-i0348}
*分類: マッピング管理*  ・  難易度: 中級

権限境界の確認では マッピング管理 の 購読再記述 を主操作として MAP12 を判定します。参照操作と変更操作の分離への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP12 に残します。権限境界の確認を補助する 購読記述 では SourceTable を補助値として MAP12 へ保存します。主判定の権限境界の確認ではマッピング管理の 購読再記述 から MappedTable を読み MAP12 へ残します。証跡照合の権限境界の確認ではマッピング管理の MappedTable と SourceTable を MAP12 に保存します。記録対応の権限境界の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP12 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 権限境界の確認 MAP12の役割を調べています。リフレッシュ制御 CDC Refresh 障害切り分け REF04の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては初期ロード未完了でMirrorへを避けるため・方式表示から初期ロードingを読むして方式表示を照合する。
    - B. 機能の説明としては対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するしてサブスクリプを照合する。
    - C. 機能の説明としてはデータ定義対象表の漏れを避けるため・復旧操作で点検欄を確認するしてサブスクリプを照合する。DDL後の表定義更新 Head of Log 0221固有の属性も確認対象に含める。
    - D. 機能の説明としてはデータ定義変更後に古い列定義で複を避けるため・購読再記述からMappedTableを読して購読再記述を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能購読再・データでDの記述「表対応で購読再記述から MappedTable を読み」に対応する項目は権限境界の確認 MAP12（表対応・購読再・権限境）です。照合購読再・権限境に関するマッピング管理の仕様は「表対応で購読再記述から MappedTable を読み」で、確認対象は購読再・権限境・データです。比較マッピ・権限境でA:の障害切り分け REF04は「変更データ取得 初期ロードで方式表示から」を述べるため、正答側の照合軸は表対応・権限境・購読再です。運用権限境・表対応でB:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は購読再・マッピ・権限境です。項目購読再・権限境でC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はデータ・マッピ・購読再です。用語購読再・権限境という用語は「表対応で購読再記述から MappedTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読再・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 権限境界の確認 MAP12**

    - 検証目的: マッピング管理のTable Mappingについて実行権限を点検し、MAP12のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB12を指定し、MAP12の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP12 to DW.MAP12 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB12を指定し、MAP12の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB12
    Source table: APP.MAP12
    Target table: DW.MAP12
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP12 -aを指定し、MAP12の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP12 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP12 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Mapped が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の refreshed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 通常状態の確認 MAP01 {#c11-i0349}
*分類: マッピング管理*  ・  難易度: 中級

通常状態の確認では マッピング管理 の 購読記述 を主操作として MAP01 を判定します。基準値と現在値の差への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP01 に残します。通常状態の確認を補助する 表再読込 では refreshed を補助値として MAP01 へ保存します。主判定の通常状態の確認ではマッピング管理の 購読記述 から SourceTable を読み MAP01 へ残します。証跡照合の通常状態の確認ではマッピング管理の SourceTable と refreshed を MAP01 に保存します。記録対応の通常状態の確認ではマッピング管理の Source TableとTarget Table の証跡へ MAP01 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 通常状態の確認 MAP01の設定や表示を読む前に役割を確認します。ログ依存・サポート Log Dependency 復旧準備 LOG05ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは購読確認からInactiveを読むことで購読確認を確認し・休止購読を見落として必要ログを防ぐ。
    - B. 対象資源に対する働きは変更確認操作で採取欄を棚卸することでサブスクリプを確認し・重複反映を防ぐ。
    - C. 対象資源に対する働きは購読記述からSourceTableを読むことで購読記述を確認し・データ定義変更後に古い列定義を防ぐ。 ✅
    - D. 対象資源に対する働きは採取操作で照合欄を点検することでサブスクリプを確認し・イベント重大度の誤読を防ぐ。CDCミラーリング Replication Method 0283固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能購読記・データでCの記述「表対応で購読記述から SourceTable を読み」に対応する項目は通常状態の確認 MAP01（表対応・購読記・通常状）です。照合購読記・通常状に関するマッピング管理の仕様は「表対応で購読記述から SourceTable を読み」で、確認対象は購読記・通常状・データです。比較マッピ・通常状でA:の復旧準備 LOG05は「ログ依存で購読確認から Inactive」を述べるため、正答側の照合軸は表対応・通常状・購読記です。運用通常状・表対応でB:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は購読記・マッピ・通常状です。仕様購読記・通常状でD:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は通常状・データ・購読記です。用語購読記・通常状という用語は「表対応で購読記述から SourceTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読記・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 通常状態の確認 MAP01**

    - 検証目的: マッピング管理のTable Mappingについて通常状態を確定し、MAP01のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB01を指定し、MAP01の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB01
    Source table: APP.MAP01
    Target table: DW.MAP01
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP01 -aを指定し、MAP01の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP01 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP01 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB01を指定し、MAP01の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP01 to DW.MAP01 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の refreshed が画面・出力に表示されること
    ③ ステップ3 の Mapped が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### マッピング管理 Table Mapping 障害切り分け MAP04 {#c11-i0350}
*分類: マッピング管理*  ・  難易度: 中級

障害切り分けでは マッピング管理 の 購読記述 を主操作として MAP04 を判定します。最初に失敗した処理への注意として「DDL変更後に古い列定義で複製を再開する危険があります」を MAP04 に残します。障害切り分けを補助する 表再読込 では refreshed を補助値として MAP04 へ保存します。主判定の障害切り分けではマッピング管理の 購読記述 から SourceTable を読み MAP04 へ残します。証跡照合の障害切り分けではマッピング管理の SourceTable と refreshed を MAP04 に保存します。記録対応の障害切り分けではマッピング管理の Source TableとTarget Table の証跡へ MAP04 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** マッピング管理 Table Mapping 障害切り分け MAP04の役割を調べています。エラー処理 CDC Event Log 復旧準備 ERR05の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はデータ定義変更後に古い列定義で複を避けるため・購読記述からSourceTableを読むして購読記述を照合する。 ✅
    - B. 表示や設定で扱う内容は情報イベントと停止を伴うエラーをを避けるため・通信エラーからERRORを読むして通信エラーを照合する。
    - C. 表示や設定で扱う内容は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。
    - D. 表示や設定で扱う内容はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてイベントログを照合する。CDCミラーリング Subscription 0271固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能購読記・データでAの記述「表対応で購読記述から SourceTable を読み」に対応する項目は障害切り分け MAP04（表対応・購読記・マッピ）です。照合購読記・マッピに関するマッピング管理の仕様は「表対応で購読記述から SourceTable を読み」で、確認対象は購読記・マッピ・データです。運用マッピ・表対応でB:の復旧準備 ERR05は「変更データ取得 イベントログで通信エラーから」を述べるため、正答側の照合軸は購読記・マッピ・マッピです。項目購読記・マッピでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はデータ・マッピ・購読記です。仕様購読記・マッピでD:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸はマッピ・データ・購読記です。用語購読記・マッピという用語は「表対応で購読記述から SourceTable」を指し、照合する値と誤認リスクの組合せはマッピ・購読記・データです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **マッピング管理 Table Mapping 障害切り分け MAP04**

    - 検証目的: マッピング管理のTable Mappingについて障害範囲を限定し、MAP04のSource TableとTarget Tableを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象MAP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB04を指定し、MAP04の購読記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription: SUB04
    Source table: APP.MAP04
    Target table: DW.MAP04
    Mapping status: Active
    ```

    画面・出力にあるSubscriptionを読み、Source TableとTarget Tableと対象MAP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmreaddtable -I SRC1 -t APP.MAP04 -aを指定し、MAP04の表再読込を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmreaddtable -I SRC1 -t APP.MAP04 -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.MAP04 definition refreshed successfully. Return value 0.
    ```

    画面・出力にあるrefreshedを読み、Source TableとTarget Tableと対象MAP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のマッピング管理を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB04を指定し、MAP04の購読再記述を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Mapped table APP.MAP04 to DW.MAP04 Columns 18 Key ID
    ```

    画面・出力にあるMappedを読み、Source TableとTarget Tableと対象MAP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の refreshed が画面・出力に表示されること
    ③ ステップ3 の Mapped が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting




## IBM IIDR 11.4 > ミラーリング

### CDCミラーリング Event Severity 0004 {#c11-i0351}
*分類: ミラーリング*  ・  難易度: 初級

紅E巡回0005ではIBM IIDR 11.4 の ミラーリングを扱う採取票紅E巡回0005です。紅E巡回0005は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録紅E巡回0005です。紅E巡回0005ではミラー開始と取得時刻を採取票紅E巡回0005へ残します。紅E巡回0005では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断紅E巡回0005です。紅E巡回0005の用語整理では複製ミラーリングの対象値を実在出力で区別する記録紅E巡回0005です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0004の技術的な意味を資料で確認するとき、複製位置管理 Bookmark 0024との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は保守操作で監査欄を保存することでミラー開始を確認し・対象サブスクリプションの取りを防ぐ。 ✅
    - B. 管理対象との関係を表す説明は照合操作で確認欄を採取することで複製位置を確認し・対象インスタンスの取り違えを防ぐ。
    - C. 管理対象との関係を表す説明は記録操作で証跡欄を照合することでRefresを確認し・Refresh未完了の見落とを防ぐ。
    - D. 管理対象との関係を表す説明は通信統計からSendsを読むことで通信統計を確認し・送信回数だけでターゲット適用を防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 巡回・ミラー・対象サブでAの記述「CDCのミラー開始と取得時刻を記録し、対象サブスクリプションの取り違」に対応する項目はEvent Severity（ミラー・ミラー・対象サブ・巡回）です。巡回時のミラー開始に関するミラーリングの仕様は「CDCのミラー開始と取得時刻を記録し、対象サブスクリプションの取り違」で、確認対象はミラー・ミラー・対象サブ・巡回です。棚卸・複製位・対象インのB:は「Bookmarkの複製位置と取得時刻を記録し」を述べ、対象は複製位置管理 Bookmark（Boo・複製位・対象イン・棚卸）です。登録時のRefreのC:は「CDCのRefresh状態と取得時刻を記録し」を述べ、対象はTable Status（ミラー・Ref・Refr・登録）です。通信統計を代替経路確のD:は「CDC Communicationsで通信統計からSendsを読み」を述べ、対象は代替経路の確認 STAT10（CDC・通信統・送信回数・代替経）です。ミラー開始を巡回という用語は「CDCのミラー開始と取得時刻を記録し」を指し、Event Severity（ミラー・ミラー・対象サブ・巡回）で照合する値はミラー開始です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0004**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0004について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE004
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0004A
    ```

    画面・出力には IIDR114DD0004A が表示され、CDCミラーリング Event Severity 0004 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE004
    Mirroring request accepted
    確認コード IIDR114DD0004B
    ```

    画面・出力には IIDR114DD0004B が表示され、CDCミラーリング Event Severity 0004 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0004C
    ```

    画面・出力には IIDR114DD0004C が表示され、CDCミラーリング Event Severity 0004 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0004A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0004B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0004C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0019 {#c11-i0352}
*分類: ミラーリング*  ・  難易度: 初級

空T巡回0020ではIBM IIDR 11.4 の ミラーリングを扱う採取票空T巡回0020です。空T巡回0020は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録空T巡回0020です。空T巡回0020ではミラー開始と取得時刻を採取票空T巡回0020へ残します。空T巡回0020ではイベント重大度の誤読を避けるため補助資料も照合する判断空T巡回0020です。空T巡回0020の用語整理では複製ミラーリングの対象値を実在出力で評価する記録空T巡回0020です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0019について構成や状態を確認します。複製位置管理 Instance 0063ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはInstanceの戻り値と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - B. 対象資源に対する働きはCDCのミラー開始と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - C. 対象資源に対する働きはCDCの遅延確認と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - D. 対象資源に対する働きはCDC Refreshで完了確認からRowsappliedを読みである。完了確認からRowsappliedをときはRefresh未完了でMirを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 巡回・ミラー・イベントでBの記述「CDCのミラー開始と取得時刻を記録し、イベント重大度の誤読を防ぐであ」に対応する項目はEvent Severity（ミラー・ミラー・イベント・巡回）です。巡回時のミラー開始に関するミラーリングの仕様は「CDCのミラー開始と取得時刻を記録し、イベント重大度の誤読を防ぐ」で、確認対象はミラー・ミラー・イベント・巡回です。In・監査・戻り値のA:は「Instanceの戻り値と取得時刻を記録し、データ欠落を防ぐ」を述べ、対象は複製位置管理 Instance（Ins・戻り値・データ欠・監査）です。確認時の遅延確認のC:は「CDCの遅延確認と取得時刻を記録し、対象サブスクリプションの取り違え」を述べ、対象はCDCミラーリング Latency（ミラー・遅延確・対象サブ・確認）です。完了確認を変更確認のD:は「CDC Refreshで完了確認からRowsappliedを読み」を述べ、対象は変更後の確認 REF03（CDC・完了確・Refr・変更確）です。ミラー開始を巡回という用語は「CDCのミラー開始と取得時刻を記録し」を指し、Event Severity（ミラー・ミラー・イベント・巡回）で照合する値はミラー開始です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0019**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0019について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE019
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0019A
    ```

    画面・出力には IIDR114DD0019A が表示され、CDCミラーリング Event Severity 0019 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE019
    Mirroring request accepted
    確認コード IIDR114DD0019B
    ```

    画面・出力には IIDR114DD0019B が表示され、CDCミラーリング Event Severity 0019 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0019C
    ```

    画面・出力には IIDR114DD0019C が表示され、CDCミラーリング Event Severity 0019 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0019A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0019B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0019C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0034 {#c11-i0353}
*分類: ミラーリング*  ・  難易度: 中級

翠O棚卸0035ではIBM IIDR 11.4 の ミラーリングを扱う採取票翠O棚卸0035です。翠O棚卸0035は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録翠O棚卸0035です。翠O棚卸0035ではミラー開始と取得時刻を採取票翠O棚卸0035へ残します。翠O棚卸0035では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断翠O棚卸0035です。翠O棚卸0035の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録翠O棚卸0035です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0034の役割を調べています。DDL後の表定義更新 Source Table 0110の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は移行で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - B. 表示や設定で扱う内容は保護でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - C. 表示や設定で扱う内容は復旧準備で通信エラーを証跡に残し・CDC Event Logで通信エラーからERRORを読み。
    - D. 表示や設定で扱う内容は棚卸でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ミラー・遅延ゼでDの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・棚卸）です。照合ミラー・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・遅延ゼです。比較ミラー・棚卸でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・棚卸です。運用棚卸・ミラーでB:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はミラー・ミラー・棚卸です。項目ミラー・遅延ゼでC:の復旧準備 ERR05は「CDC Event Logで通信エラーからE」を述べるため、正答側の照合軸は遅延ゼ・ミラー・ミラーです。用語ミラー・棚卸という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・棚卸です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0034**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0034について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE034
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0034A
    ```

    画面・出力には IIDR114DD0034A が表示され、CDCミラーリング Event Severity 0034 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE034
    Mirroring request accepted
    確認コード IIDR114DD0034B
    ```

    画面・出力には IIDR114DD0034B が表示され、CDCミラーリング Event Severity 0034 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0034C
    ```

    画面・出力には IIDR114DD0034C が表示され、CDCミラーリング Event Severity 0034 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0034A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0034B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0034C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0049 {#c11-i0354}
*分類: ミラーリング*  ・  難易度: 中級

朱J復旧0050ではIBM IIDR 11.4 の ミラーリングを扱う採取票朱J復旧0050です。朱J復旧0050は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録朱J復旧0050です。朱J復旧0050ではミラー開始と取得時刻を採取票朱J復旧0050へ残します。朱J復旧0050ではRefresh未完了の見落としを避けるため補助資料も照合する判断朱J復旧0050です。朱J復旧0050の用語整理では複製ミラーリングの対象値を実在出力で比較する記録朱J復旧0050です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Event Severity 0049」を「DDL後の表定義更新 Source Table 0110」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は後の表定義更新の項目の表定義再読込と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - B. 保守作業で参照する機能はLocaleのサブスクリプション名と取得時刻を記録し・ベンダー指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはベンダー指示なしの位置変更を防ぐ。
    - C. 保守作業で参照する機能はミラーリングの項目のミラー開始と取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。 ✅
    - D. 保守作業で参照する機能はCDC Replication のスクリプト操作に使うコマンドライン機能をマッピング検査として確認する。マッピングで変換規則を確認するときは変換規則の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ミラー・初期ロでCの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・復旧）です。照合ミラー・初期ロに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・初期ロです。比較ミラー・復旧でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・初期ロ・復旧です。運用復旧・ミラーでB:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はミラー・ミラー・復旧です。仕様ミラー・ミラーでD:のマッピング検査 変換規則は「CDC Replication」を述べるため、正答側の照合軸は復旧・初期ロ・ミラーです。用語ミラー・復旧という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0049**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0049について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE049
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0049A
    ```

    画面・出力には IIDR114DD0049A が表示され、CDCミラーリング Event Severity 0049 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE049
    Mirroring request accepted
    確認コード IIDR114DD0049B
    ```

    画面・出力には IIDR114DD0049B が表示され、CDCミラーリング Event Severity 0049 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0049C
    ```

    画面・出力には IIDR114DD0049C が表示され、CDCミラーリング Event Severity 0049 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0049A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0049B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0049C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0064 {#c11-i0355}
*分類: ミラーリング*  ・  難易度: 中級

紅E監査0065ではIBM IIDR 11.4 の ミラーリングを扱う採取票紅E監査0065です。紅E監査0065は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録紅E監査0065です。紅E監査0065ではミラー開始と取得時刻を採取票紅E監査0065へ残します。紅E監査0065では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断紅E監査0065です。紅E監査0065の用語整理では複製ミラーリングの対象値を実在出力で区別する記録紅E監査0065です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0064を同一分類の複製位置管理 Subscription 0105と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は移行で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - B. 管理対象との関係を表す説明は監査でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅
    - C. 管理対象との関係を表す説明は抑止でサブスクリプを証跡に残し・後の表定義更新の項目のサブスクリプション記述と取得時刻を記録。
    - D. 管理対象との関係を表す説明はログ依存で依存表示を証跡に残し・Log Dependencyで依存表示からOldestreq。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ミラー・対象サでBの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・監査）です。照合ミラー・対象サに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・対象サです。比較ミラー・監査でA:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・対象サ・監査です。項目ミラー・対象サでC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は対象サ・ミラー・ミラーです。仕様ミラー・ミラーでD:の障害切り分け LOG04は「Log Dependencyで依存表示からO」を述べるため、正答側の照合軸は監査・対象サ・ミラーです。用語ミラー・監査という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0064**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0064について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE064
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0064A
    ```

    画面・出力には IIDR114DD0064A が表示され、CDCミラーリング Event Severity 0064 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE064
    Mirroring request accepted
    確認コード IIDR114DD0064B
    ```

    画面・出力には IIDR114DD0064B が表示され、CDCミラーリング Event Severity 0064 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0064C
    ```

    画面・出力には IIDR114DD0064C が表示され、CDCミラーリング Event Severity 0064 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0064A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0064B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0064C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0079 {#c11-i0356}
*分類: ミラーリング*  ・  難易度: 中級

空T監査0080ではIBM IIDR 11.4 の ミラーリングを扱う採取票空T監査0080です。空T監査0080は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録空T監査0080です。空T監査0080ではミラー開始と取得時刻を採取票空T監査0080へ残します。空T監査0080ではイベント重大度の誤読を避けるため補助資料も照合する判断空T監査0080です。空T監査0080の用語整理では複製ミラーリングの対象値を実在出力で評価する記録空T監査0080です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0079の設定や表示を読む前に役割を確認します。複製位置管理 Subscription 0165ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは採取操作で照合欄を点検することでミラー開始を確認し・イベント重大度の誤読を防ぐ。 ✅
    - B. 対象資源に対する働きは主操作で出力欄を評価することで16進ブックを確認し・ベンダー指示なしの位置変更を防ぐ。
    - C. 対象資源に対する働きは記録操作で証跡欄を照合することで遅延確認を確認し・初期ロード未完了の見落としを防ぐ。
    - D. 対象資源に対する働きはマッピングで変換規則を確認することで変換規則を確認し・変換規則の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ミラー・イベンでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・監査）です。照合ミラー・イベンに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・イベンです。運用監査・ミラーでB:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・ミラー・監査です。項目ミラー・イベンでC:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸はイベン・ミラー・ミラーです。仕様ミラー・ミラーでD:のマッピング検査 変換規則は「CDC Replication」を述べるため、正答側の照合軸は監査・イベン・ミラーです。用語ミラー・監査という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0079**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0079について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE079
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0079A
    ```

    画面・出力には IIDR114DD0079A が表示され、CDCミラーリング Event Severity 0079 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE079
    Mirroring request accepted
    確認コード IIDR114DD0079B
    ```

    画面・出力には IIDR114DD0079B が表示され、CDCミラーリング Event Severity 0079 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0079C
    ```

    画面・出力には IIDR114DD0079C が表示され、CDCミラーリング Event Severity 0079 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0079A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0079B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0079C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0094 {#c11-i0357}
*分類: ミラーリング*  ・  難易度: 中級

翠O変更0095ではIBM IIDR 11.4 の ミラーリングを扱う採取票翠O変更0095です。翠O変更0095は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録翠O変更0095です。翠O変更0095ではミラー開始と取得時刻を採取票翠O変更0095へ残します。翠O変更0095では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断翠O変更0095です。翠O変更0095の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録翠O変更0095です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0094に関する障害切り分けの前提を確認しています。CDCミラーリング Table Status 0145の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するして初期ロード状を照合する。
    - B. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてミラー開始を照合する。 ✅
    - C. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。
    - D. 表示や設定で扱う内容は期限切れの誤読を避けるため・初期同期判定で期限切れを確認するして期限切れを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ミラー・遅延ゼでBの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・変更）です。照合ミラー・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・遅延ゼです。比較ミラー・変更でA:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・変更です。項目ミラー・遅延ゼでC:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸は遅延ゼ・ミラー・ミラーです。仕様ミラー・ミラーでD:の初期同期判定 期限切れは「CDC Replication」を述べるため、正答側の照合軸は変更・遅延ゼ・ミラーです。用語ミラー・変更という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・変更です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0094**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0094について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE094
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0094A
    ```

    画面・出力には IIDR114DD0094A が表示され、CDCミラーリング Event Severity 0094 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE094
    Mirroring request accepted
    確認コード IIDR114DD0094B
    ```

    画面・出力には IIDR114DD0094B が表示され、CDCミラーリング Event Severity 0094 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0094C
    ```

    画面・出力には IIDR114DD0094C が表示され、CDCミラーリング Event Severity 0094 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0094A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0094B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0094C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0109 {#c11-i0358}
*分類: ミラーリング*  ・  難易度: 上級

朱J移行0110ではIBM IIDR 11.4 の ミラーリングを扱う採取票朱J移行0110です。朱J移行0110は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録朱J移行0110です。朱J移行0110ではミラー開始と取得時刻を採取票朱J移行0110へ残します。朱J移行0110ではRefresh未完了の見落としを避けるため補助資料も照合する判断朱J移行0110です。朱J移行0110の用語整理では複製ミラーリングの対象値を実在出力で比較する記録朱J移行0110です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0109を保守記録に説明する必要があります。DDL後の表定義更新 Source Table 0185と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてミラー開始を照合する。 ✅
    - B. 保守作業で参照する機能はデータ定義対象表の漏れを避けるため・復旧操作で点検欄を確認するして表定義再読込を照合する。
    - C. 保守作業で参照する機能は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。DDL後の表定義更新 Subscription 0302固有の属性も確認対象に含める。
    - D. 保守作業で参照する機能は画面タグの誤読を避けるため・複製状態監視で画面タグを確認するして画面タグを照合する。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能ミラー・初期ロでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・移行）です。照合ミラー・初期ロに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・初期ロです。運用移行・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・ミラー・移行です。項目ミラー・初期ロでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・ミラーです。仕様ミラー・ミラーでD:の開始位置指定 画面タグは「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸は移行・初期ロ・ミラーです。用語ミラー・移行という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0109**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0109について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE109
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0109A
    ```

    画面・出力には IIDR114DD0109A が表示され、CDCミラーリング Event Severity 0109 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE109
    Mirroring request accepted
    確認コード IIDR114DD0109B
    ```

    画面・出力には IIDR114DD0109B が表示され、CDCミラーリング Event Severity 0109 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0109C
    ```

    画面・出力には IIDR114DD0109C が表示され、CDCミラーリング Event Severity 0109 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0109A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0109B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0109C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0124 {#c11-i0359}
*分類: ミラーリング*  ・  難易度: 初級

紅E診断0125ではIBM IIDR 11.4 の ミラーリングを扱う採取票紅E診断0125です。紅E診断0125は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録紅E診断0125です。紅E診断0125ではミラー開始と取得時刻を採取票紅E診断0125へ残します。紅E診断0125では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断紅E診断0125です。紅E診断0125の用語整理では複製ミラーリングの対象値を実在出力で区別する記録紅E診断0125です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0124の技術的な意味を資料で確認するとき、DDL後の表定義更新 Subscription 0182との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。
    - B. 管理対象との関係を表す説明はデータ欠落を避けるため・監査操作で記録欄を比較するしてインスタンスを照合する。
    - C. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてサブスクリプを照合する。
    - D. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてミラー開始を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能ミラー・対象サでDの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・診断）です。照合ミラー・対象サに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・対象サです。比較ミラー・診断でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・診断です。運用診断・ミラーでB:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はミラー・ミラー・診断です。項目ミラー・対象サでC:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は対象サ・ミラー・ミラーです。用語ミラー・診断という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0124**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0124について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE004
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0124A
    ```

    画面・出力には IIDR114DD0124A が表示され、CDCミラーリング Event Severity 0124 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE004
    Mirroring request accepted
    確認コード IIDR114DD0124B
    ```

    画面・出力には IIDR114DD0124B が表示され、CDCミラーリング Event Severity 0124 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0124C
    ```

    画面・出力には IIDR114DD0124C が表示され、CDCミラーリング Event Severity 0124 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0124A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0124B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0124C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0139 {#c11-i0360}
*分類: ミラーリング*  ・  難易度: 初級

空T診断0140ではIBM IIDR 11.4 の ミラーリングを扱う採取票空T診断0140です。空T診断0140は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録空T診断0140です。空T診断0140ではミラー開始と取得時刻を採取票空T診断0140へ残します。空T診断0140ではイベント重大度の誤読を避けるため補助資料も照合する判断空T診断0140です。空T診断0140の用語整理では複製ミラーリングの対象値を実在出力で評価する記録空T診断0140です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0139について構成や状態を確認します。複製位置管理 Bookmark 0144ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはBookmarkの複製位置と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。
    - B. 対象資源に対する働きはCDC Refreshで方式表示から初期ロードingを読み・初期ロードingとReturnvalueを照合すである。方式表示から初期ロードingを読むときは初期ロード未完了でMirroを防ぐ。
    - C. 対象資源に対する働きはミラーリングの項目のミラー開始と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きはSubscriptionの16進ブックマークと取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能ミラー・イベンでCの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・診断）です。照合ミラー・イベンに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・イベンです。比較ミラー・診断でA:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・イベン・診断です。運用診断・ミラーでB:の通常状態の確認 REF01は「CDC Refreshで方式表示から初期ロー」を述べるため、正答側の照合軸はミラー・ミラー・診断です。仕様ミラー・ミラーでD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は診断・イベン・ミラーです。用語ミラー・診断という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0139**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0139について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE019
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0139A
    ```

    画面・出力には IIDR114DD0139A が表示され、CDCミラーリング Event Severity 0139 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE019
    Mirroring request accepted
    確認コード IIDR114DD0139B
    ```

    画面・出力には IIDR114DD0139B が表示され、CDCミラーリング Event Severity 0139 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0139C
    ```

    画面・出力には IIDR114DD0139C が表示され、CDCミラーリング Event Severity 0139 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0139A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0139B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0139C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0154 {#c11-i0361}
*分類: ミラーリング*  ・  難易度: 中級

翠O保守0155ではIBM IIDR 11.4 の ミラーリングを扱う採取票翠O保守0155です。翠O保守0155は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録翠O保守0155です。翠O保守0155ではミラー開始と取得時刻を採取票翠O保守0155へ残します。翠O保守0155では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断翠O保守0155です。翠O保守0155の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録翠O保守0155です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0154の役割を調べています。複製位置管理 Subscription 0180の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するして16進ブックを照合する。
    - B. 表示や設定で扱う内容は初期ロード中の表をMirror完を避けるため・状態表示からLatencyを読むして状態表示を照合する。
    - C. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてミラー開始を照合する。 ✅
    - D. 表示や設定で扱う内容は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてイベントログを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ミラー・遅延ゼでCの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・保守）です。照合ミラー・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・遅延ゼです。比較ミラー・保守でA:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・遅延ゼ・保守です。運用保守・ミラーでB:の障害切り分け MIR04は「Mirror Statusで状態表示からLa」を述べるため、正答側の照合軸はミラー・ミラー・保守です。仕様ミラー・ミラーでD:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸は保守・遅延ゼ・ミラーです。用語ミラー・保守という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・保守です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0154**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0154について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE034
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0154A
    ```

    画面・出力には IIDR114DD0154A が表示され、CDCミラーリング Event Severity 0154 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE034
    Mirroring request accepted
    確認コード IIDR114DD0154B
    ```

    画面・出力には IIDR114DD0154B が表示され、CDCミラーリング Event Severity 0154 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0154C
    ```

    画面・出力には IIDR114DD0154C が表示され、CDCミラーリング Event Severity 0154 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0154A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0154B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0154C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0169 {#c11-i0362}
*分類: ミラーリング*  ・  難易度: 中級

朱J切替0170ではIBM IIDR 11.4 の ミラーリングを扱う採取票朱J切替0170です。朱J切替0170は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録朱J切替0170です。朱J切替0170ではミラー開始と取得時刻を採取票朱J切替0170へ残します。朱J切替0170ではRefresh未完了の見落としを避けるため補助資料も照合する判断朱J切替0170です。朱J切替0170の用語整理では複製ミラーリングの対象値を実在出力で比較する記録朱J切替0170です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Event Severity 0169」を「DDL後の表定義更新 Source Table 0200」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は切替でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅
    - B. 保守作業で参照する機能は登録で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 保守作業で参照する機能はログとの照合で定義表示を証跡に残し・CDC Subscriptionで定義表示からSubscri。
    - D. 保守作業で参照する機能は復旧で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ミラー・初期ロでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・切替）です。照合ミラー・初期ロに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・初期ロです。運用切替・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・ミラー・切替です。項目ミラー・初期ロでC:のログとの照合 SUB07は「CDC Subscriptionで定義表示か」を述べるため、正答側の照合軸は初期ロ・ミラー・ミラーです。仕様ミラー・ミラーでD:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸は切替・初期ロ・ミラーです。用語ミラー・切替という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0169**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0169について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE049
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0169A
    ```

    画面・出力には IIDR114DD0169A が表示され、CDCミラーリング Event Severity 0169 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE049
    Mirroring request accepted
    確認コード IIDR114DD0169B
    ```

    画面・出力には IIDR114DD0169B が表示され、CDCミラーリング Event Severity 0169 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0169C
    ```

    画面・出力には IIDR114DD0169C が表示され、CDCミラーリング Event Severity 0169 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0169A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0169B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0169C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0184 {#c11-i0363}
*分類: ミラーリング*  ・  難易度: 中級

紅E収集0185ではIBM IIDR 11.4 の ミラーリングを扱う採取票紅E収集0185です。紅E収集0185は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録紅E収集0185です。紅E収集0185ではミラー開始と取得時刻を採取票紅E収集0185へ残します。紅E収集0185では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断紅E収集0185です。紅E収集0185の用語整理では複製ミラーリングの対象値を実在出力で区別する記録紅E収集0185です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0184を同一分類のDDL後の表定義更新 Source Table 0275と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は収集でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅
    - B. 管理対象との関係を表す説明は照合で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 管理対象との関係を表す説明は依存関係確認で通信統計を証跡に残し・CDC Communicationsで通信統計からSends。
    - D. 管理対象との関係を表す説明は変更でサブスクリプを証跡に残し・後の表定義更新の項目のサブスクリプション記述と取得時刻を記録。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ミラー・対象サでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・収集）です。照合ミラー・対象サに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・対象サです。運用収集・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・ミラー・収集です。項目ミラー・対象サでC:の依存関係の確認 STAT13は「CDC Communicationsで通信統」を述べるため、正答側の照合軸は対象サ・ミラー・ミラーです。仕様ミラー・ミラーでD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は収集・対象サ・ミラーです。用語ミラー・収集という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0184**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0184について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE064
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0184A
    ```

    画面・出力には IIDR114DD0184A が表示され、CDCミラーリング Event Severity 0184 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE064
    Mirroring request accepted
    確認コード IIDR114DD0184B
    ```

    画面・出力には IIDR114DD0184B が表示され、CDCミラーリング Event Severity 0184 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0184C
    ```

    画面・出力には IIDR114DD0184C が表示され、CDCミラーリング Event Severity 0184 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0184A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0184B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0184C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0199 {#c11-i0364}
*分類: ミラーリング*  ・  難易度: 中級

空T収集0200ではIBM IIDR 11.4 の ミラーリングを扱う採取票空T収集0200です。空T収集0200は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録空T収集0200です。空T収集0200ではミラー開始と取得時刻を採取票空T収集0200へ残します。空T収集0200ではイベント重大度の誤読を避けるため補助資料も照合する判断空T収集0200です。空T収集0200の用語整理では複製ミラーリングの対象値を実在出力で評価する記録空T収集0200です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0199の設定や表示を読む前に役割を確認します。複製位置管理 Hex Position 0201ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは採取操作で照合欄を点検することでミラー開始を確認し・イベント重大度の誤読を防ぐ。 ✅
    - B. 対象資源に対する働きは主操作で出力欄を評価することでインスタンスを確認し・ベンダー指示なしの位置変更を防ぐ。
    - C. 対象資源に対する働きは方式表示から初期ロードingを読むことで方式表示を確認し・初期ロード未完了でMirroを防ぐ。
    - D. 対象資源に対する働きは復旧操作で点検欄を確認することでログ先頭到達を確認し・データ定義対象表の漏れを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ミラー・イベンでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・収集）です。照合ミラー・イベンに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・イベンです。運用収集・ミラーでB:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はミラー・ミラー・収集です。項目ミラー・イベンでC:のログとの照合 REF07は「CDC Refreshで方式表示から初期ロー」を述べるため、正答側の照合軸はイベン・ミラー・ミラーです。仕様ミラー・ミラーでD:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は収集・イベン・ミラーです。用語ミラー・収集という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0199**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0199について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE079
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0199A
    ```

    画面・出力には IIDR114DD0199A が表示され、CDCミラーリング Event Severity 0199 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE079
    Mirroring request accepted
    確認コード IIDR114DD0199B
    ```

    画面・出力には IIDR114DD0199B が表示され、CDCミラーリング Event Severity 0199 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0199C
    ```

    画面・出力には IIDR114DD0199C が表示され、CDCミラーリング Event Severity 0199 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0199A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0199B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0199C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0214 {#c11-i0365}
*分類: ミラーリング*  ・  難易度: 中級

翠O登録0215ではIBM IIDR 11.4 の ミラーリングを扱う採取票翠O登録0215です。翠O登録0215は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録翠O登録0215です。翠O登録0215ではミラー開始と取得時刻を採取票翠O登録0215へ残します。翠O登録0215では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断翠O登録0215です。翠O登録0215の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録翠O登録0215です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0214に関する障害切り分けの前提を確認しています。複製位置管理 Bookmark 0264の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は照合操作で確認欄を採取することで複製位置を確認し・対象インスタンスの取り違えを防ぐ。
    - B. 表示や設定で扱う内容は完了確認からRowsappliedを読むことで完了確認を確認し・初期ロード未完了でMirroを防ぐ。
    - C. 表示や設定で扱う内容は確認操作で状態欄を整理することでミラー開始を確認し・遅延ゼロ確認の欠落を防ぐ。 ✅
    - D. 表示や設定で扱う内容は照合操作で確認欄を採取することで戻り値を確認し・対象インスタンスの取り違えを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ミラー・遅延ゼでCの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・登録）です。照合ミラー・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・遅延ゼです。比較ミラー・登録でA:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・遅延ゼ・登録です。運用登録・ミラーでB:の権限境界の確認 REF12は「CDC Refreshで完了確認からRows」を述べるため、正答側の照合軸はミラー・ミラー・登録です。仕様ミラー・ミラーでD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は登録・遅延ゼ・ミラーです。用語ミラー・登録という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・登録です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0214**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0214について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE094
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0214A
    ```

    画面・出力には IIDR114DD0214A が表示され、CDCミラーリング Event Severity 0214 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE094
    Mirroring request accepted
    確認コード IIDR114DD0214B
    ```

    画面・出力には IIDR114DD0214B が表示され、CDCミラーリング Event Severity 0214 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0214C
    ```

    画面・出力には IIDR114DD0214C が表示され、CDCミラーリング Event Severity 0214 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0214A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0214B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0214C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0229 {#c11-i0366}
*分類: ミラーリング*  ・  難易度: 上級

朱J確認0230ではIBM IIDR 11.4 の ミラーリングを扱う採取票朱J確認0230です。朱J確認0230は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録朱J確認0230です。朱J確認0230ではミラー開始と取得時刻を採取票朱J確認0230へ残します。朱J確認0230ではRefresh未完了の見落としを避けるため補助資料も照合する判断朱J確認0230です。朱J確認0230の用語整理では複製ミラーリングの対象値を実在出力で比較する記録朱J確認0230です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0229を保守記録に説明する必要があります。DDL後の表定義更新 Source Table 0260と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は確認でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅
    - B. 保守作業で参照する機能は照合で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 保守作業で参照する機能は依存関係確認で状態表示を証跡に残し・Mirror Statusで状態表示からLatencyを読み。
    - D. 保守作業で参照する機能は診断で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・データ欠落を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能ミラー・初期ロでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・確認）です。照合ミラー・初期ロに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・初期ロです。運用確認・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・ミラー・確認です。項目ミラー・初期ロでC:の依存関係の確認 MIR13は「Mirror Statusで状態表示からLa」を述べるため、正答側の照合軸は初期ロ・ミラー・ミラーです。仕様ミラー・ミラーでD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は確認・初期ロ・ミラーです。用語ミラー・確認という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0229**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0229について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE109
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0229A
    ```

    画面・出力には IIDR114DD0229A が表示され、CDCミラーリング Event Severity 0229 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE109
    Mirroring request accepted
    確認コード IIDR114DD0229B
    ```

    画面・出力には IIDR114DD0229B が表示され、CDCミラーリング Event Severity 0229 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0229C
    ```

    画面・出力には IIDR114DD0229C が表示され、CDCミラーリング Event Severity 0229 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0229A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0229B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0229C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0244 {#c11-i0367}
*分類: ミラーリング*  ・  難易度: 初級

紅E保護0245ではIBM IIDR 11.4 の ミラーリングを扱う採取票紅E保護0245です。紅E保護0245は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録紅E保護0245です。紅E保護0245ではミラー開始と取得時刻を採取票紅E保護0245へ残します。紅E保護0245では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断紅E保護0245です。紅E保護0245の用語整理では複製ミラーリングの対象値を実在出力で区別する記録紅E保護0245です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0244の技術的な意味を資料で確認するとき、DDL後の表定義更新 Table Definition 0299との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はミラーリングの項目のミラー開始と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅
    - B. 管理対象との関係を表す説明は後の表定義更新の項目のデータ定義対象表と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。
    - C. 管理対象との関係を表す説明はCDC Communicationsでログ依存からOldestdependencyを読みである。ログ依存からOldestdependときは送信回数だけでターゲット適用を防ぐ。
    - D. 管理対象との関係を表す説明は後の表定義更新の項目の表定義再読込と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能ミラー・対象サでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・保護）です。照合ミラー・対象サに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・対象サです。運用保護・ミラーでB:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・ミラー・保護です。項目ミラー・対象サでC:の権限境界の確認 STAT12は「CDC Communicationsでログ依」を述べるため、正答側の照合軸は対象サ・ミラー・ミラーです。仕様ミラー・ミラーでD:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は保護・対象サ・ミラーです。用語ミラー・保護という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0244**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0244について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE004
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0244A
    ```

    画面・出力には IIDR114DD0244A が表示され、CDCミラーリング Event Severity 0244 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE004
    Mirroring request accepted
    確認コード IIDR114DD0244B
    ```

    画面・出力には IIDR114DD0244B が表示され、CDCミラーリング Event Severity 0244 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0244C
    ```

    画面・出力には IIDR114DD0244C が表示され、CDCミラーリング Event Severity 0244 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0244A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0244B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0244C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0259 {#c11-i0368}
*分類: ミラーリング*  ・  難易度: 初級

空T保護0260ではIBM IIDR 11.4 の ミラーリングを扱う採取票空T保護0260です。空T保護0260は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録空T保護0260です。空T保護0260ではミラー開始と取得時刻を採取票空T保護0260へ残します。空T保護0260ではイベント重大度の誤読を避けるため補助資料も照合する判断空T保護0260です。空T保護0260の用語整理では複製ミラーリングの対象値を実在出力で評価する記録空T保護0260です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0259について構成や状態を確認します。DDL後の表定義更新 Head of Log 0296ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは保護でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅
    - B. 対象資源に対する働きは抑止でサブスクリプを証跡に残し・後の表定義更新の項目のサブスクリプション記述と取得時刻を記録。
    - C. 対象資源に対する働きはサブスクリプで再同期判断を証跡に残し・ソース表とターゲット表の対応および列変換を示す定義をマッピン。
    - D. 対象資源に対する働きは変更でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能ミラー・イベンでAの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・保護）です。照合ミラー・イベンに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・イベンです。運用保護・ミラーでB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・ミラー・保護です。項目ミラー・イベンでC:のマッピング検査 再同期判断は「ソース表とターゲット表の対応および列変換を示」を述べるため、正答側の照合軸はイベン・ミラー・ミラーです。仕様ミラー・ミラーでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は保護・イベン・ミラーです。用語ミラー・保護という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0259**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0259について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE019
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0259A
    ```

    画面・出力には IIDR114DD0259A が表示され、CDCミラーリング Event Severity 0259 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE019
    Mirroring request accepted
    確認コード IIDR114DD0259B
    ```

    画面・出力には IIDR114DD0259B が表示され、CDCミラーリング Event Severity 0259 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0259C
    ```

    画面・出力には IIDR114DD0259C が表示され、CDCミラーリング Event Severity 0259 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0259A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0259B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0259C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0274 {#c11-i0369}
*分類: ミラーリング*  ・  難易度: 中級

翠O照合0275ではIBM IIDR 11.4 の ミラーリングを扱う採取票翠O照合0275です。翠O照合0275は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録翠O照合0275です。翠O照合0275ではミラー開始と取得時刻を採取票翠O照合0275へ残します。翠O照合0275では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断翠O照合0275です。翠O照合0275の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録翠O照合0275です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0274の役割を調べています。複製位置管理 Subscription 0285の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は抑止で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - B. 表示や設定で扱う内容は復旧確認で支援情報を証跡に残し・Log Dependencyで支援情報からReturnval。
    - C. 表示や設定で扱う内容は照合でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。 ✅
    - D. 表示や設定で扱う内容は切替でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ミラー・遅延ゼでCの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・照合）です。照合ミラー・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・遅延ゼです。比較ミラー・照合でA:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・遅延ゼ・照合です。運用照合・ミラーでB:の復旧後の確認 LOG06は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸はミラー・ミラー・照合です。仕様ミラー・ミラーでD:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は照合・遅延ゼ・ミラーです。用語ミラー・照合という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・照合です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0274**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0274について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE034
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0274A
    ```

    画面・出力には IIDR114DD0274A が表示され、CDCミラーリング Event Severity 0274 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE034
    Mirroring request accepted
    確認コード IIDR114DD0274B
    ```

    画面・出力には IIDR114DD0274B が表示され、CDCミラーリング Event Severity 0274 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0274C
    ```

    画面・出力には IIDR114DD0274C が表示され、CDCミラーリング Event Severity 0274 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0274A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0274B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0274C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0289 {#c11-i0370}
*分類: ミラーリング*  ・  難易度: 中級

朱J抑止0290ではIBM IIDR 11.4 の ミラーリングを扱う採取票朱J抑止0290です。朱J抑止0290は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録朱J抑止0290です。朱J抑止0290ではミラー開始と取得時刻を採取票朱J抑止0290へ残します。朱J抑止0290ではRefresh未完了の見落としを避けるため補助資料も照合する判断朱J抑止0290です。朱J抑止0290の用語整理では複製ミラーリングの対象値を実在出力で比較する記録朱J抑止0290です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Event Severity 0289」を「CDCミラーリング Latency 0322」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして遅延確認を照合する。
    - B. 保守作業で参照する機能は休止購読を見落として必要ログを削を避けるため・支援情報からReturnvalueを読むして支援情報を照合する。
    - C. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてイベントログを照合する。
    - D. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてミラー開始を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ミラー・初期ロでDの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・抑止）です。照合ミラー・初期ロに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・初期ロです。比較ミラー・抑止でA:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸はミラー・初期ロ・抑止です。運用抑止・ミラーでB:の再始動後の確認 LOG15は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸はミラー・ミラー・抑止です。項目ミラー・初期ロでC:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸は初期ロ・ミラー・ミラーです。用語ミラー・抑止という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0289**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0289について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE049
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0289A
    ```

    画面・出力には IIDR114DD0289A が表示され、CDCミラーリング Event Severity 0289 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE049
    Mirroring request accepted
    確認コード IIDR114DD0289B
    ```

    画面・出力には IIDR114DD0289B が表示され、CDCミラーリング Event Severity 0289 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0289C
    ```

    画面・出力には IIDR114DD0289C が表示され、CDCミラーリング Event Severity 0289 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0289A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0289B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0289C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0304 {#c11-i0371}
*分類: ミラーリング*  ・  難易度: 中級

紅E解析0305ではIBM IIDR 11.4 の ミラーリングを扱う採取票紅E解析0305です。紅E解析0305は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録紅E解析0305です。紅E解析0305ではミラー開始と取得時刻を採取票紅E解析0305へ残します。紅E解析0305では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断紅E解析0305です。紅E解析0305の用語整理では複製ミラーリングの対象値を実在出力で区別する記録紅E解析0305です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0304を同一分類のマッピング管理 Table Mapping 障害切り分け MAP04と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はTable Mappingで購読記述からSourceTableを読みである。購読記述からSourceTableをときはデータ定義変更後に古い列定義を防ぐ。
    - B. 管理対象との関係を表す説明はミラーリングの項目のミラー開始と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅
    - C. 管理対象との関係を表す説明は対象表を初期同期または再同期する複製操作を遅延監視として確認する。マッピングで入力欄を確認するときは入力欄の誤読を防ぐ。
    - D. 管理対象との関係を表す説明はミラーリングの項目のサブスクリプション状態と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ミラー・対象サでBの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・解析）です。照合ミラー・対象サに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・対象サです。比較ミラー・解析でA:の障害切り分け MAP04は「Table Mappingで購読記述からSo」を述べるため、正答側の照合軸はミラー・対象サ・解析です。項目ミラー・対象サでC:の遅延監視 入力欄は「対象表を初期同期または再同期する複製操作を遅」を述べるため、正答側の照合軸は対象サ・ミラー・ミラーです。仕様ミラー・ミラーでD:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は解析・対象サ・ミラーです。用語ミラー・解析という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0304**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0304について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE064
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0304A
    ```

    画面・出力には IIDR114DD0304A が表示され、CDCミラーリング Event Severity 0304 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE064
    Mirroring request accepted
    確認コード IIDR114DD0304B
    ```

    画面・出力には IIDR114DD0304B が表示され、CDCミラーリング Event Severity 0304 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0304C
    ```

    画面・出力には IIDR114DD0304C が表示され、CDCミラーリング Event Severity 0304 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0304A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0304B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0304C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0319 {#c11-i0372}
*分類: ミラーリング*  ・  難易度: 中級

空T解析0320ではIBM IIDR 11.4 の ミラーリングを扱う採取票空T解析0320です。空T解析0320は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録空T解析0320です。空T解析0320ではミラー開始と取得時刻を採取票空T解析0320へ残します。空T解析0320ではイベント重大度の誤読を避けるため補助資料も照合する判断空T解析0320です。空T解析0320の用語整理では複製ミラーリングの対象値を実在出力で評価する記録空T解析0320です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0319の設定や表示を読む前に役割を確認します。複製状態監視 Mirror Status 代替経路の確認 MIR10ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはMirror Statusで状態表示からLatencyを読み・Latencyとheadoflogを照合する。状態表示からLatencyを読むときは初期ロード中の表をMirroを防ぐ。
    - B. 対象資源に対する働きはターゲットへ変更を反映し適用済み位置を記録する処理を統計採取として確認する。統計採取でマクロ実行を確認するときはマクロ実行の誤読を防ぐ。
    - C. 対象資源に対する働きは後の表定義更新の項目の表定義再読込と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - D. 対象資源に対する働きはミラーリングの項目のミラー開始と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ミラー・イベンでDの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・解析）です。照合ミラー・イベンに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・ミラー・イベンです。比較ミラー・解析でA:の代替経路の確認 MIR10は「Mirror Statusで状態表示からLa」を述べるため、正答側の照合軸はミラー・イベン・解析です。運用解析・ミラーでB:の統計採取 マクロ実行は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸はミラー・ミラー・解析です。項目ミラー・イベンでC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はイベン・ミラー・ミラーです。用語ミラー・解析という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0319**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0319について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE079
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0319A
    ```

    画面・出力には IIDR114DD0319A が表示され、CDCミラーリング Event Severity 0319 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE079
    Mirroring request accepted
    確認コード IIDR114DD0319B
    ```

    画面・出力には IIDR114DD0319B が表示され、CDCミラーリング Event Severity 0319 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0319C
    ```

    画面・出力には IIDR114DD0319C が表示され、CDCミラーリング Event Severity 0319 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0319A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0319B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0319C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0334 {#c11-i0373}
*分類: ミラーリング*  ・  難易度: 中級

翠O計画0335ではIBM IIDR 11.4 の ミラーリングを扱う採取票翠O計画0335です。翠O計画0335は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録翠O計画0335です。翠O計画0335ではミラー開始と取得時刻を採取票翠O計画0335へ残します。翠O計画0335では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断翠O計画0335です。翠O計画0335の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録翠O計画0335です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0334に関する障害切り分けの前提を確認しています。サブスクリプション管理 CDC Subscription 構成監査 SUB08の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はCDC Subscriptionでイベント表示からSeverityを読みである。イベント表示からSeverityを読ときは別サブスクリプションを停止まを防ぐ。
    - B. 表示や設定で扱う内容はSubscriptionの16進ブックマークと取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - C. 表示や設定で扱う内容はミラーリングの項目のサブスクリプション状態と取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。
    - D. 表示や設定で扱う内容はミラーリングの項目のミラー開始と取得時刻を記録し・遅延ゼロ確認の欠落を防ぐである。確認操作で状態欄を整理するときは遅延ゼロ確認の欠落を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ミラー・遅延ゼでDの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・計画）です。照合ミラー・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・計画・遅延ゼです。比較ミラー・計画でA:の構成監査 SUB08は「CDC Subscriptionでイベント表」を述べるため、正答側の照合軸はミラー・計画・ミラーです。運用計画・ミラーでB:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・ミラー・計画です。項目ミラー・遅延ゼでC:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は遅延ゼ・ミラー・ミラーです。用語ミラー・計画という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・ミラー・遅延ゼです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0334**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0334について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE094
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0334A
    ```

    画面・出力には IIDR114DD0334A が表示され、CDCミラーリング Event Severity 0334 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE094
    Mirroring request accepted
    確認コード IIDR114DD0334B
    ```

    画面・出力には IIDR114DD0334B が表示され、CDCミラーリング Event Severity 0334 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0334C
    ```

    画面・出力には IIDR114DD0334C が表示され、CDCミラーリング Event Severity 0334 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0334A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0334B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0334C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Event Severity 0349 {#c11-i0374}
*分類: ミラーリング*  ・  難易度: 上級

朱J解除0350ではIBM IIDR 11.4 の ミラーリングを扱う採取票朱J解除0350です。朱J解除0350は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録朱J解除0350です。朱J解除0350ではミラー開始と取得時刻を採取票朱J解除0350へ残します。朱J解除0350ではRefresh未完了の見落としを避けるため補助資料も照合する判断朱J解除0350です。朱J解除0350の用語整理では複製ミラーリングの対象値を実在出力で比較する記録朱J解除0350です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Event Severity 0349を保守記録に説明する必要があります。データストア接続 CDC Datastore ログとの照合 STORE07と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は接続表示からDatastoreを読むことで接続表示を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - B. 保守作業で参照する機能は調査操作で保守欄を引き継ぎすることでデータ定義対を確認し・ログ先頭未到達の見落としを防ぐ。
    - C. 保守作業で参照する機能は主操作で出力欄を評価することでサブスクリプを確認し・ベンダー指示なしの位置変更を防ぐ。
    - D. 保守作業で参照する機能は記録操作で証跡欄を照合することでミラー開始を確認し・初期ロード未完了の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能ミラー・初期ロでDの記述「ミラーリングの項目のミラー開始と取得時刻を記録し」に対応する項目はEvent Severity（ミラー・ミラー・解除）です。照合ミラー・初期ロに関するミラーリングの仕様は「ミラーリングの項目のミラー開始と取得時刻を記録し」で、確認対象はミラー・解除・初期ロです。比較ミラー・解除でA:のログとの照合 STORE07は「CDC Datastoreで接続表示からDa」を述べるため、正答側の照合軸はミラー・解除・ミラーです。運用解除・ミラーでB:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・ミラー・解除です。項目ミラー・初期ロでC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・ミラーです。用語ミラー・解除という用語は「ミラーリングの項目のミラー開始と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・ミラー・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Event Severity 0349**

    - 検証目的: CDCミラーリングのCDCミラーリング Event Severity 0349について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Event Severity と ミラー開始
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmendreplication
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE109
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0349A
    ```

    画面・出力には IIDR114DD0349A が表示され、CDCミラーリング Event Severity 0349 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE109
    Mirroring request accepted
    確認コード IIDR114DD0349B
    ```

    画面・出力には IIDR114DD0349B が表示され、CDCミラーリング Event Severity 0349 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Event Severity を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0349C
    ```

    画面・出力には IIDR114DD0349C が表示され、CDCミラーリング Event Severity 0349 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0349A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0349B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0349C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0007 {#c11-i0375}
*分類: ミラーリング*  ・  難易度: 初級

茶H巡回0008ではIBM IIDR 11.4 の ミラーリングを扱う採取票茶H巡回0008です。茶H巡回0008は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録茶H巡回0008です。茶H巡回0008では遅延確認と取得時刻を採取票茶H巡回0008へ残します。茶H巡回0008ではイベント重大度の誤読を避けるため補助資料も照合する判断茶H巡回0008です。茶H巡回0008の用語整理では複製ミラーリングの対象値を実在出力で評価する記録茶H巡回0008です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0007の設定や表示を読む前に役割を確認します。CDCミラーリング Replication Method 0058ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてサブスクリプを照合する。
    - B. 対象資源に対する働きはログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてログ先頭到達を照合する。
    - C. 対象資源に対する働きは送信回数だけでターゲット適用完了を避けるため・通信統計からSendsを読むして通信統計を照合する。
    - D. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして遅延確認を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 巡回・遅延確・イベントでDの記述「CDCの遅延確認と取得時刻を記録し、イベント重大度の誤読を防ぐである」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・イベント・巡回）です。巡回時の遅延確認に関するミラーリングの仕様は「CDCの遅延確認と取得時刻を記録し、イベント重大度の誤読を防ぐ」で、確認対象はミラー・遅延確・イベント・巡回です。ミラ・復旧・サブスクのA:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラー・サブス・遅延ゼロ・復旧）です。登録・ログ先・ログ先頭のB:は「DDLのログ先頭到達と取得時刻を記録し、ログ先頭未到達の見落としを防」を述べ、対象はDDL後の表定義更新（後の表・ログ先・ログ先頭・登録）です。ログとの時の通信統計のC:は「CDC Communicationsで通信統計からSendsを読み」を述べ、対象はログとの照合 STAT07（CDC・通信統・送信回数・ログと）です。遅延確認を巡回という用語は「CDCの遅延確認と取得時刻を記録し」を指し、CDCミラーリング Latency（ミラー・遅延確・イベント・巡回）で照合する値は遅延確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0007**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0007について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE007
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0007A
    ```

    画面・出力には IIDR114DD0007A が表示され、CDCミラーリング Latency 0007 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE007
    Mirroring request accepted
    確認コード IIDR114DD0007B
    ```

    画面・出力には IIDR114DD0007B が表示され、CDCミラーリング Latency 0007 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0007C
    ```

    画面・出力には IIDR114DD0007C が表示され、CDCミラーリング Latency 0007 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0007A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0007B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0007C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0022 {#c11-i0376}
*分類: ミラーリング*  ・  難易度: 初級

緑C棚卸0023ではIBM IIDR 11.4 の ミラーリングを扱う採取票緑C棚卸0023です。緑C棚卸0023は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録緑C棚卸0023です。緑C棚卸0023では遅延確認と取得時刻を採取票緑C棚卸0023へ残します。緑C棚卸0023では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断緑C棚卸0023です。緑C棚卸0023の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録緑C棚卸0023です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0022に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Source Table 0110の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は移行で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - B. 表示や設定で扱う内容は照合で再開条件を証跡に残し・後の表定義更新の項目の再開条件と取得時刻を記録し。
    - C. 表示や設定で扱う内容はデータストアで停止時刻を証跡に残し・CDC Replication が接続するソースまたはターゲ。
    - D. 表示や設定で扱う内容は棚卸で遅延確認を証跡に残し・ミラーリングの項目の遅延確認と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能遅延確・遅延ゼでDの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・棚卸）です。照合遅延確・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・遅延ゼです。比較ミラー・棚卸でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・棚卸です。運用棚卸・ミラーでB:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は遅延確・ミラー・棚卸です。項目ミラー・遅延ゼでC:の開始位置指定 停止時刻は「CDC Replication」を述べるため、正答側の照合軸は遅延ゼ・ミラー・遅延確です。用語遅延確・棚卸という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・棚卸です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0022**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0022について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE022
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0022A
    ```

    画面・出力には IIDR114DD0022A が表示され、CDCミラーリング Latency 0022 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE022
    Mirroring request accepted
    確認コード IIDR114DD0022B
    ```

    画面・出力には IIDR114DD0022B が表示され、CDCミラーリング Latency 0022 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0022C
    ```

    画面・出力には IIDR114DD0022C が表示され、CDCミラーリング Latency 0022 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0022A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0022B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0022C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0037 {#c11-i0377}
*分類: ミラーリング*  ・  難易度: 中級

藤R棚卸0038ではIBM IIDR 11.4 の ミラーリングを扱う採取票藤R棚卸0038です。藤R棚卸0038は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録藤R棚卸0038です。藤R棚卸0038では遅延確認と取得時刻を採取票藤R棚卸0038へ残します。藤R棚卸0038ではRefresh未完了の見落としを避けるため補助資料も照合する判断藤R棚卸0038です。藤R棚卸0038の用語整理では複製ミラーリングの対象値を実在出力で比較する記録藤R棚卸0038です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0037を保守記録に説明する必要があります。複製位置管理 Instance 0093と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は変更で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し。
    - B. 保守作業で参照する機能は確認で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - C. 保守作業で参照する機能は棚卸で遅延確認を証跡に残し・ミラーリングの項目の遅延確認と取得時刻を記録し。 ✅
    - D. 保守作業で参照する機能はリフレッシュで完了確認を証跡に残し・CDC Refreshで完了確認からRowsappliedを。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能遅延確・初期ロでCの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・棚卸）です。照合遅延確・初期ロに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・初期ロです。比較ミラー・棚卸でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・初期ロ・棚卸です。運用棚卸・ミラーでB:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は遅延確・ミラー・棚卸です。仕様ミラー・遅延確でD:の引継ぎ記録 REF09は「CDC Refreshで完了確認からRows」を述べるため、正答側の照合軸は棚卸・初期ロ・遅延確です。用語遅延確・棚卸という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・棚卸です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0037**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0037について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE037
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0037A
    ```

    画面・出力には IIDR114DD0037A が表示され、CDCミラーリング Latency 0037 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE037
    Mirroring request accepted
    確認コード IIDR114DD0037B
    ```

    画面・出力には IIDR114DD0037B が表示され、CDCミラーリング Latency 0037 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0037C
    ```

    画面・出力には IIDR114DD0037C が表示され、CDCミラーリング Latency 0037 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0037A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0037B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0037C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


