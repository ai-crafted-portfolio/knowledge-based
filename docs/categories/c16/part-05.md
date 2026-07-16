---
search:
  exclude: true
---

# IMS 15.5 — 詳細 (5/5)

[← IMS 15.5 の概要へ戻る](index.md)


## IMS 15.5 > 障害診断

### 障害診断 IMSメッセージ診断 復旧準備 DIAG05 {#c16-i0233}
*分類: 障害診断*  ・  難易度: 上級

復旧準備では 障害診断 の IMS Connect警告 を主操作として DIAG05 を判定します。再開前に必要な整合性への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG05 に残します。復旧準備を補助する 再始動メッセージ では DFS680I を補助値として DIAG05 へ保存します。主判定の復旧準備では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG05 へ残します。証跡照合の復旧準備では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG05 に保存します。記録対応の復旧準備では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG05 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 復旧準備で 障害診断 の IMS Connect警告 と 再始動メッセージ を組み合わせる際は IMSメッセージ診断 がDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用という仕組みを前提にします。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。HWSQ2240W と メッセージIDと理由コード を対象 DIAG05 で確認する組合せはどれですか。

    - A. 前回保存したF HWS1,VIEWPORT ALLの結果を使う。今回の/DISPLAY OLDSの結果と同一時点の証跡として比較する。
    - B. 保存済みのDIAG05の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。
    - C. 変更を加えずF HWS1,VIEWPORT ALLを実行する。HWSQ2240Wを保存する。差分は/DISPLAY OLDSの結果と対象名で対応させる。 ✅
    - D. /DISPLAY OLDSのDFS680IをメッセージIDと理由コードの主判定に採用する。F HWS1,VIEWPORT ALLの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: CはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として復旧条件を確認しDIAG05に残します。
    処理の仕組み: 復旧準備では再始動メッセージを補助操作としIMSメッセージ診断の再開前に必要な整合性をDFS680Iと対象DIAG05で照合します。
    選択結果の内訳: IMS Connect警告と再始動メッセージの役割を分けるとA: 採取時刻が異なる点でIMS Connect警告を代替しません、B: 過去出力では今回の復旧準備を示せない点で障害診断に使いません、C: 変更前のHWSQ2240Wを保存する点で正答です、D: DFS680IはHWSQ2240Wを代替しないうえに追加前提も不正な点でDIAG05を採用できません。結論として復旧準備の障害診断・メッセージ診断で判定する対象は DIAG05 です。
    用語の説明: 復旧準備で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG05へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 復旧準備 DIAG05**

    - 検証目的: 障害診断のIMSメッセージ診断について復旧条件を確認し、DIAG05のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG05のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG05
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG05の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG05のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
    ② ステップ2 の DFS680I が画面・出力に表示されること
    ③ ステップ3 の status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 構成監査 DIAG08 {#c16-i0234}
*分類: 障害診断*  ・  難易度: 上級

構成監査では 障害診断 の IMS Connect警告 を主操作として DIAG08 を判定します。定義値と稼働値の一致への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG08 に残します。構成監査を補助する 再始動メッセージ では DFS680I を補助値として DIAG08 へ保存します。主判定の構成監査では障害診断・メッセージ診断の IMS Connect警告 から HWSQ2240W を読み DIAG08 へ残します。証跡照合の構成監査では障害診断・メッセージ診断の HWSQ2240W と DFS680I を DIAG08 に保存します。記録対応の構成監査では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG08 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 構成監査で 障害診断 の IMS Connect警告 と 再始動メッセージ を実施し IMSメッセージ診断 の役割を確認します。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。対象 DIAG08 の証跡を取る方法はどれですか。

    - A. 保存済みのDIAG08の出力を再利用する。今回のF HWS1,VIEWPORT ALLと/DISPLAY OLDSは実行済みとして扱う。
    - B. /DISPLAY OLDSの結果だけでは確定しない。F HWS1,VIEWPORT ALLのHWSQ2240Wを主証跡として構成差分を監査する。 ✅
    - C. /DISPLAY OLDSのDFS680IをメッセージIDと理由コードの主判定に採用する。F HWS1,VIEWPORT ALLの応答は採取対象から外す。
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のstatusをHWSQ2240Wと同義の成功表示として扱う。F HWS1,VIEWPORT ALLは実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: BはIMS Connect警告で HWSQ2240W を読みメッセージIDと理由コードの主値として構成差分を監査しDIAG08に残します。
    実行時の背景: 構成監査では再始動メッセージを補助操作としIMSメッセージ診断の定義値と稼働値の一致をDFS680Iと対象DIAG08で照合します。
    四つの候補の理由: IMS Connect警告と再始動メッセージの役割を分けるとA: 過去出力では今回の構成監査を示せない点で障害診断に使いません、B: HWSQ2240Wを主証跡として区別する点で正答です、C: DFS680IはHWSQ2240Wを代替しない点でDIAG08を採用できません、D: statusとHWSQ2240Wは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の障害診断・メッセージ診断で判定する対象は DIAG08 です。
    初出語定義: 構成監査で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG08へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 構成監査 DIAG08**

    - 検証目的: 障害診断のIMSメッセージ診断について構成差分を監査し、DIAG08のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG08のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG08
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG08の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG08のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の HWSQ2240W が画面・出力に表示されること
    ② ステップ2 の DFS680I が画面・出力に表示されること
    ③ ステップ3 の status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 通常状態の確認 DIAG01 {#c16-i0235}
*分類: 障害診断*  ・  難易度: 上級

通常状態の確認では 障害診断 の メンバー照会 を主操作として DIAG01 を判定します。基準値と現在値の差への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG01 に残します。通常状態の確認を補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG01 へ保存します。主判定の通常状態の確認では障害診断・メッセージ診断の メンバー照会 から status を読み DIAG01 へ残します。証跡照合の通常状態の確認では障害診断・メッセージ診断の status と HWSQ2240W を DIAG01 に保存します。記録対応の通常状態の確認では障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG01 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で 障害診断 の メンバー照会 と IMS Connect警告 を使い 通常状態を確定 します。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読み対象 DIAG01 を切り分ける確認方法はどれですか。

    - A. F HWS1,VIEWPORT ALLのHWSQ2240WをメッセージIDと理由コードの主判定に採用する。QUERY MEMBER TYPE(IMS) SHOW(STATUS)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. /DISPLAY OLDSのDFS680Iをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。
    - C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)を先に実行する。対象DIAG01のstatusをメッセージIDと理由コードとして記録する。続いてF HWS1,VIEWPORT ALLで同一対象を照合する。 ✅
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cはメンバー照会で status を読みメッセージIDと理由コードの主値として通常状態を確定しDIAG01に残します。
    背景・仕組み: 通常状態の確認ではIMS Connect警告を補助操作としIMSメッセージ診断の基準値と現在値の差をHWSQ2240Wと対象DIAG01で照合します。
    選択肢の理由: メンバー照会とIMS Connect警告の役割を分けるとA: HWSQ2240Wはstatusを代替しないうえに追加前提も不正な点でIMSメッセージ診断に使えません、B: DFS680Iとstatusは確認項目が異なる点でDIAG01を採用できません、C: statusを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではメッセージIDと理由コードを判定できない点で一次資料と一致しません。結論として通常状態の確認の障害診断・メッセージ診断で判定する対象は DIAG01 です。
    用語の初出定義: 通常状態の確認で使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG01へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 通常状態の確認 DIAG01**

    - 検証目的: 障害診断のIMSメッセージ診断について通常状態を確定し、DIAG01のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG01のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG01のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG01
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG01の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の status が画面・出力に表示されること
    ② ステップ2 の HWSQ2240W が画面・出力に表示されること
    ③ ステップ3 の DFS680I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages



### 障害診断 IMSメッセージ診断 障害切り分け DIAG04 {#c16-i0236}
*分類: 障害診断*  ・  難易度: 上級

障害切り分けでは 障害診断 の メンバー照会 を主操作として DIAG04 を判定します。最初に失敗した処理への注意として「メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります」を DIAG04 に残します。障害切り分けを補助する IMS Connect警告 では HWSQ2240W を補助値として DIAG04 へ保存します。主判定の障害切り分けでは障害診断・メッセージ診断の メンバー照会 から status を読み DIAG04 へ残します。証跡照合の障害切り分けでは障害診断・メッセージ診断の status と HWSQ2240W を DIAG04 に保存します。記録対応の障害切り分けでは障害診断・メッセージ診断の メッセージIDと理由コード の証跡へ DIAG04 を結びます。

**出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages

??? question "確認問題（1問）"
    **問題.** 障害切り分けで 障害診断 の メンバー照会 と IMS Connect警告 を照合し 最初に失敗した処理 を確かめます。IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用です。メッセージ本文だけを読み対象メンバーや理由コードを失う危険があります。status を読む前に対象 DIAG04 へ行う確認はどれですか。

    - A. /DISPLAY OLDSのDFS680Iをstatusと同義の成功表示として扱う。QUERY MEMBER TYPE(IMS) SHOW(STATUS)は実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. QUERY MEMBER TYPE(IMS) SHOW(STATUS)の出力でDIAG04とstatusが同じ応答にあることを確認する。メッセージIDと理由コードをその応答から採取する。 ✅
    - C. QUERY MEMBER TYPE(IMS) SHOW(STATUS)が応答を返した時点で正常とする。応答中のstatusの値は記録しない。
    - D. QUERY MEMBER TYPE(IMS) SHOW(STATUS)のコマンド文字列だけを記録する。statusを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bはメンバー照会で status を読みメッセージIDと理由コードの主値として障害範囲を限定しDIAG04に残します。
    技術的背景: 障害切り分けではIMS Connect警告を補助操作としIMSメッセージ診断の最初に失敗した処理をHWSQ2240Wと対象DIAG04で照合します。
    四択の評価: メンバー照会とIMS Connect警告の役割を分けるとA: DFS680Iとstatusは確認項目が異なるうえに追加前提も不正な点でDIAG04を採用できません、B: DIAG04とstatusを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではメッセージIDと理由コードを判定できない点で一次資料と一致しません、D: 入力記録だけではメッセージIDと理由コードを証明できない点でメッセージIDと理由コードを確認できません。結論として障害切り分けの障害診断・メッセージ診断で判定する対象は DIAG04 です。
    初出語の意味: 障害切り分けで使う IMSメッセージ診断 はDFSおよびHWSメッセージのID、戻りコード、対象メンバーを対応させて障害範囲を絞る運用を表しメッセージIDと理由コードを判定する際にDIAG04へ適用します。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages


??? note "検証手順（1件）"
    **障害診断 IMSメッセージ診断 障害切り分け DIAG04**

    - 検証目的: 障害診断のIMSメッセージ診断について障害範囲を限定し、DIAG04のメッセージIDと理由コードを実出力で確認する。
    - 前提条件: IMS 15.5の参照権限を持ち、対象DIAG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IMS 15.5の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へQUERY MEMBER TYPE(IMS) SHOW(STATUS)を指定し、DIAG04のメンバー照会を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> QUERY MEMBER TYPE(IMS) SHOW(STATUS)
    → Enter を押す
    ```

    画面・出力:
    ```text
    <mbr name='IMS1'><typ>IMS</typ><status>ACTIVE</status><rc>00000000</rc></mbr>
    ```

    画面・出力にあるstatusを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へF HWS1,VIEWPORT ALLを指定し、DIAG04のIMS Connect警告を表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> F HWS1,VIEWPORT ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    HWSQ2240W REGISTRATION TO ODBM FAILED FOR DIAG04
    IMS CONNECT CONTINUES TO RUN
    ```

    画面・出力にあるHWSQ2240Wを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIMS 15.5の障害診断を確認する入力画面です。COMMAND入力口へ/DISPLAY OLDSを指定し、DIAG04の再始動メッセージを表示します。
    操作（入力）:
    ```text
    IMS 15.5 操作画面
    COMMAND ===> /DISPLAY OLDS
    → Enter を押す
    ```

    画面・出力:
    ```text
    DFS058I NRESTART COMMAND IN PROGRESS
    DFS680I USING CHKPT 82170/085820
    ```

    画面・出力にあるDFS680Iを読み、メッセージIDと理由コードと対象DIAG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の status が画面・出力に表示されること
    ② ステップ2 の HWSQ2240W が画面・出力に表示されること
    ③ ステップ3 の DFS680I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Commands_Volume_2_IMS_Commands_N-V / IMS_15.5_Operations_and_Automation / IMS_15.5_Database_Administration / IMS_15.5_Database_Utilities / IMS_15.5_Messages_and_Codes_Volume_2_Non-DFS_Messages




## IMS 15.5 > 領域

### BMP 領域 {#c16-i0237}
*分類: 領域*  ・  難易度: 中級

IMS 15.5 の 領域で扱うBMP 領域は、バッチ処理で IMS データベースやメッセージキューへアクセスする従属領域です。オンライン稼働中のデータと整合させながらバッチ処理できる点が特徴です。排他、チェックポイント、再始動の設計が重要になります

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 区切確認の領域で BMP 領域の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. BMP 領域の出力を取らず区切確認の領域の説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 ✅
    - C. /DISPLAY TRANSACTION OSKB を省略して区切確認の領域の記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切確認の領域へ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では BMP 領域 は「区切確認の領域に関係する定義値と表示行を照合する区切確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では BMP 領域の属性行と DFS058I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明のみに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では BMP 領域を IMS 15.5の運用手順で確認し、初出名は区切確認初出です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **BMP 領域**

    - 検証目的: 区切確認の領域について、IMS 15.5 の 領域で扱う BMP 領域は、バッチ処理で IMS データベースやメッセージキューへアクセスする従属領域です。オンライン稼働中のデータと整合させながらバッに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、区切確認の領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にBMP 領域を指定し、OSKB010010の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND BMP 領域
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM BMP 領域
    CASE OSKB010010
    SOURCE IMS 15.5
    ```

    BMP 領域とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010010を同じ出力で読み、区切確認の領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010010
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010010
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010010  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の BMP 領域 と OSKB010010 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010010 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### IFP 領域 {#c16-i0238}
*分類: 領域*  ・  難易度: 上級

IMS 15.5 の 領域で扱うIFP 領域は、Fast Path 処理向けの IMS 従属領域です。高頻度で短いトランザクションを効率よく処理する用途で使われます。Fast Path データベースやルーティングの設計と合わせて確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 範囲確認の領域でアイエムエスの運用確認を行います。IFP 領域の根拠にできる作業はどれですか。

    - A. IMS 15.5と無関係な一覧で範囲確認の領域を確認した扱いにする。
    - B. DFS058I の有無を確認せず範囲確認の領域を正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 ✅
    - D. IFP 領域の属性行を読まず範囲確認の領域の画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では IFP 領域 は「IMS 15.5で IFP 領域の扱いを記録する範囲確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では IFP 領域の表示結果と DFS058I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明のみに寄り、判定名は範囲確認不足です。範囲確認資料では IFP 領域の使い方を出典欄から追跡し、資料名は範囲確認資料です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **IFP 領域**

    - 検証目的: 範囲確認の領域について、IMS 15.5 の 領域で扱う IFP 領域は、Fast Path 処理向けの IMS 従属領域です。高頻度で短いトランザクションを効率よく処理する用途で使われます。Fasに関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、範囲確認の領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にIFP 領域を指定し、OSKB010011の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND IFP 領域
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM IFP 領域
    CASE OSKB010011
    SOURCE IMS 15.5
    ```

    IFP 領域とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010011を同じ出力で読み、範囲確認の領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010011
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010011
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010011  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の IFP 領域 と OSKB010011 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010011 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### MPP 領域 {#c16-i0239}
*分類: 領域*  ・  難易度: 中級

IMS 15.5 の 領域で扱うMPP 領域は、メッセージ処理プログラムを実行する IMS の従属領域です。入力メッセージを受けて短時間のトランザクション処理を行う用途に向きます。処理遅延では、スケジューリング、キュー滞留、異常終了の有無を確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 条件確認の領域に関係する MPP 領域の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 ✅
    - B. MPP 領域の名称と担当者名のみを残して条件確認の領域の表示本文を確認対象に含めない。
    - C. アイエムエス以外の画面で条件確認の領域を確認し同じ証跡として扱ったことにする。
    - D. DFS058I の有無を見ず条件確認の領域の戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では MPP 領域 は「MPP 領域の用途をアイエムエスの表示で確認する条件確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では IMS 15.5の MPP 領域と DFS058I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明のみに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では MPP 領域を IMS 15.5で扱う確認対象とし、用語名は条件確認用語です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **MPP 領域**

    - 検証目的: 条件確認の領域について、IMS 15.5 の 領域で扱う MPP 領域は、メッセージ処理プログラムを実行する IMS の従属領域です。入力メッセージを受けて短時間のトランザクション処理を行う用途に向に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、条件確認の領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄にMPP 領域を指定し、OSKB010009の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND MPP 領域
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM MPP 領域
    CASE OSKB010009
    SOURCE IMS 15.5
    ```

    MPP 領域とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010009を同じ出力で読み、条件確認の領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010009
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010009
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010009  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の MPP 領域 と OSKB010009 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010009 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands



### 制御領域 {#c16-i0240}
*分類: 領域*  ・  難易度: 初級

IMS 15.5 の 領域で扱う制御領域は、IMS 全体の制御と共通機能を担う中核のアドレス空間です。従属領域や通信、DBRC などの周辺機能と連携して処理を進めます。起動失敗や停止時は、制御領域のメッセージを最初に確認します

**出典:** IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands

??? question "確認問題（1問）"
    **問題.** 出力確認の制御領域に関する制御領域の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. /DISPLAY TRANSACTION OSKB の結果を残さず出力確認の制御領域の担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力確認の制御領域の証跡として保存して根拠にする。
    - C. 制御領域の変更点を出力本文から切り離して出力確認の制御領域の承認欄のみ残す。
    - D. IMS 15.5の表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では制御領域は「制御領域の状態と出力メッセージを結び付ける出力確認項目」と/DISPLAY TRANSACTION OSKB または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では制御領域の出力行と DFS058I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明のみに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では制御領域を IMS 15.5の確認記録に残し、対象名は出力確認対象です。

    **出典:** IMS_15.5_Commands_Volume_1_IMS_Commands_A-M / IMS_15.5_Operations_and_Automation


??? note "検証手順（1件）"
    **制御領域**

    - 検証目的: 出力確認の制御領域について、IMS 15.5 の 領域で扱う制御領域は、IMS 全体の制御と共通機能を担う中核のアドレス空間です。従属領域や通信、DBRC などの周辺機能と連携して処理を進めます。起動に関わる状態・定義・メッセージを机上で照合する。
    - 前提条件: IMS Terminalまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。
    - セッション環境: IMS Terminalで/DISPLAY TRANSACTION OSKBを実行し、DFS058Iを含む表示を確認する。

    **ステップ 1**
    現在の画面はIMS Terminalのコマンド入力画面です。COMMAND INPUT ===> に /DISPLAY TRANSACTION OSKB を入力し、出力確認の制御領域の確認表示へ進みます。
    操作（入力）:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    ```

    COMMAND INPUTに/DISPLAY TRANSACTION OSKBが表示され、対象コマンドを実行する準備ができています。

    **ステップ 2**
    現在の画面はIMS Terminalの表示結果です。FIND欄に制御領域を指定し、OSKB010008の対象行を見つけます。
    操作（入力）:
    ```text
    (IMS Terminal Result)
    COMMAND INPUT ===> FIND 制御領域
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    (IMS Terminal Result)
    ITEM 制御領域
    CASE OSKB010008
    SOURCE IMS 15.5
    ```

    制御領域とOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。

    **ステップ 3**
    現在の画面はIMS Terminalの詳細表示です。DFS058IとOSKB010008を同じ出力で読み、出力確認の制御領域の根拠を記録します。
    操作（入力）:
    ```text
    (IMS Terminal Detail)
    COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB
    CASE OSKB010008
    → Enter を押す
    ```

    画面・出力:
    ```text
    IMS COMMAND RESPONSE OSKB010008
    /DISPLAY TRANSACTION OSKB
    TRAN  OSKB010008  STATUS STARTED  CLASS 1
    DFS058I START COMMAND COMPLETED
    ```

    DFS058IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。

    - 合格条件: ① ステップ1 の COMMAND INPUT ===> /DISPLAY TRANSACTION OSKB が画面・出力に表示されること
    ② ステップ2 の 制御領域 と OSKB010008 が画面・出力に表示されること
    ③ ステップ3 の DFS058I と OSKB010008 が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IMS 15.5 System Administration / IMS 15.5 Database Administration / IMS 15.5 Commands Volume 3: IMS Component and z / OS Commands


