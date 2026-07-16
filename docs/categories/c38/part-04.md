---
search:
  exclude: true
---

# z/OS System Programming — 詳細 (4/4)

[← z/OS System Programming の概要へ戻る](index.md)


## z/OS System Programming > システム出口

### システム出口 動的出口管理 構成監査 EXIT08 {#c38-i0268}
*分類: システム出口*  ・  難易度: 上級

構成監査では システム出口 の 個別出口 を主操作として EXIT08 を判定します。定義値と稼働値の一致への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT08 に残します。構成監査を補助する モジュール所在 では CSV411I を補助値として EXIT08 へ保存します。主判定の構成監査ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT08 へ残します。証跡照合の構成監査ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT08 に保存します。記録対応の構成監査ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で システム出口 の 個別出口 と モジュール所在 を照合し 定義値と稼働値の一致 を確かめます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読む前に対象 EXIT08 へ行う確認はどれですか。

    - A. 保存済みのEXIT08の出力を再利用する。今回のD PROG,EXIT,EX=EXIT08とD PROG,LPA,MODNAME=MOD08は実行済みとして扱う。
    - B. D PROG,LPA,MODNAME=MOD08の結果だけでは確定しない。D PROG,EXIT,EX=EXIT08のCSV463Iを主証跡として構成差分を監査する。 ✅
    - C. D PROG,LPA,MODNAME=MOD08のCSV411IをEXIT名とMODULEの主判定に採用する。D PROG,EXIT,EX=EXIT08の応答は採取対象から外す。
    - D. D PROG,EXITのCSV460IをCSV463Iと同義の成功表示として扱う。D PROG,EXIT,EX=EXIT08は実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: Bは個別出口で CSV463I を読みEXIT名とMODULEの主値として構成差分を監査しEXIT08に残します。
    実行時の背景: 構成監査ではモジュール所在を補助操作とし動的出口管理の定義値と稼働値の一致をCSV411Iと対象EXIT08で照合します。
    四つの候補の理由: 個別出口とモジュール所在の役割を分けるとA: 過去出力では今回の構成監査を示せない点でシステム出口に使いません、B: CSV463Iを主証跡として区別する点で正答です、C: CSV411IはCSV463Iを代替しない点でEXIT08を採用できません、D: CSV460IとCSV463Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のシステム出口・動的出口管理で判定する対象は EXIT08 です。
    初出語定義: 構成監査で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 構成監査 EXIT08**

    - 検証目的: システム出口の動的出口管理について構成差分を監査し、EXIT08のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT08を指定し、EXIT08の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT08
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT08 MODULE MOD08 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD08を指定し、EXIT08のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD08
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD08 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT08の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT08 MODULE MOD08 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
    ② ステップ2 の CSV411I が画面・出力に表示されること
    ③ ステップ3 の CSV460I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 通常状態の確認 EXIT01 {#c38-i0269}
*分類: システム出口*  ・  難易度: 上級

通常状態の確認では システム出口 の 出口一覧 を主操作として EXIT01 を判定します。基準値と現在値の差への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT01 に残します。通常状態の確認を補助する 個別出口 では CSV463I を補助値として EXIT01 へ保存します。主判定の通常状態の確認ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT01 へ残します。証跡照合の通常状態の確認ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT01 に保存します。記録対応の通常状態の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で システム出口 の 出口一覧 と 個別出口 を用い 通常状態を確定 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV460I で対象 EXIT01 の EXIT名とMODULE を再現できる記録はどれですか。

    - A. D PROG,EXIT,EX=EXIT01のCSV463IをEXIT名とMODULEの主判定に採用する。D PROG,EXITの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. D PROG,LPA,MODNAME=MOD01のCSV411IをCSV460Iと同義の成功表示として扱う。D PROG,EXITは実行しない。
    - C. D PROG,EXITを先に実行する。対象EXIT01のCSV460IをEXIT名とMODULEとして記録する。続いてD PROG,EXIT,EX=EXIT01で同一対象を照合する。 ✅
    - D. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cは出口一覧で CSV460I を読みEXIT名とMODULEの主値として通常状態を確定しEXIT01に残します。
    背景・仕組み: 通常状態の確認では個別出口を補助操作とし動的出口管理の基準値と現在値の差をCSV463Iと対象EXIT01で照合します。
    選択肢の理由: 出口一覧と個別出口の役割を分けるとA: CSV463IはCSV460Iを代替しないうえに追加前提も不正な点で動的出口管理に使えません、B: CSV411IとCSV460Iは確認項目が異なる点でEXIT01を採用できません、C: CSV460Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではEXIT名とMODULEを判定できない点で一次資料と一致しません。結論として通常状態の確認のシステム出口・動的出口管理で判定する対象は EXIT01 です。
    用語の初出定義: 通常状態の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 通常状態の確認 EXIT01**

    - 検証目的: システム出口の動的出口管理について通常状態を確定し、EXIT01のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT01の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT01 MODULE MOD01 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT01を指定し、EXIT01の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT01
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT01 MODULE MOD01 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD01を指定し、EXIT01のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD01
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD01 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
    ② ステップ2 の CSV463I が画面・出力に表示されること
    ③ ステップ3 の CSV411I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### システム出口 動的出口管理 障害切り分け EXIT04 {#c38-i0270}
*分類: システム出口*  ・  難易度: 上級

障害切り分けでは システム出口 の 出口一覧 を主操作として EXIT04 を判定します。最初に失敗した処理への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT04 に残します。障害切り分けを補助する 個別出口 では CSV463I を補助値として EXIT04 へ保存します。主判定の障害切り分けではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT04 へ残します。証跡照合の障害切り分けではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT04 に保存します。記録対応の障害切り分けではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで システム出口 の 出口一覧 と 個別出口 の役割を分け 最初に失敗した処理 を調べます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT04 を誤判定しない進め方はどれですか。

    - A. D PROG,LPA,MODNAME=MOD04のCSV411IをCSV460Iと同義の成功表示として扱う。D PROG,EXITは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D PROG,EXITの出力でEXIT04とCSV460Iが同じ応答にあることを確認する。EXIT名とMODULEをその応答から採取する。 ✅
    - C. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。
    - D. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bは出口一覧で CSV460I を読みEXIT名とMODULEの主値として障害範囲を限定しEXIT04に残します。
    技術的背景: 障害切り分けでは個別出口を補助操作とし動的出口管理の最初に失敗した処理をCSV463Iと対象EXIT04で照合します。
    四択の評価: 出口一覧と個別出口の役割を分けるとA: CSV411IとCSV460Iは確認項目が異なるうえに追加前提も不正な点でEXIT04を採用できません、B: EXIT04とCSV460Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではEXIT名とMODULEを判定できない点で一次資料と一致しません、D: 入力記録だけではEXIT名とMODULEを証明できない点でEXIT名とMODULEを確認できません。結論として障害切り分けのシステム出口・動的出口管理で判定する対象は EXIT04 です。
    初出語の意味: 障害切り分けで使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **システム出口 動的出口管理 障害切り分け EXIT04**

    - 検証目的: システム出口の動的出口管理について障害範囲を限定し、EXIT04のEXIT名とMODULEを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT04の出口一覧を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV460I EXIT DISPLAY EXITNAME EXIT04 MODULE MOD04 STATE ACTIVE
    ```

    画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT04を指定し、EXIT04の個別出口を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,EXIT,EX=EXIT04
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV463I EXIT EXIT04 MODULE MOD04 STATE ACTIVE ABENDNUM 0
    ```

    画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD04を指定し、EXIT04のモジュール所在を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D PROG,LPA,MODNAME=MOD04
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV411I MODULE MOD04 FOUND IN LPA DATASET SYS1.LPALIB
    ```

    画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
    ② ステップ2 の CSV463I が画面・出力に表示されること
    ③ ステップ3 の CSV411I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12




## z/OS System Programming > ディスパッチ制御

### FLIH処理 ストレージ確認 運用確認078 {#c38-i0271}
*分類: ディスパッチ制御*  ・  難易度: 中級

第七十八観点 FLIH処理 は z/OS System Programming の ディスパッチ制御 で扱う管理項目です（第七十八観点）。第七十八観点 割り込みを受け、PSWやレジスター状態を保存して適切な処理へ渡す入口という説明を操作結果と照合します（第七十八観点）。第七十八観点 SYS1.PARMLIB(PROGSP)、parmlibメンバーの該当ステートメント、定義メンバーを照合し、診断ログの再現性確保を確認します（第七十八観点）。第七十八観点 証跡には資料IDと確認値を併記し、zOSSP記録078として保存します（第七十八観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第七十八証跡です。FLIH処理 の記録を監査用に整えます。確認観点は FLIH処理、ストレージ確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. SMF記録 の一般メモを採り、SYS1.PARMLIB(PROGSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記078として調査範囲を狭める。
    - B. FLIH処理 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延078として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在078として残す。
    - D. parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を同一票へ記録し、FLIH処理 を zOSSP正078で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第七十八観点 正答根拠: Dは parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を結び付けるため、対象システムの取り違えを防げます（第七十八観点）。第七十八観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第七十八観点）。第七十八観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第七十八観点）。第七十八観点 初出定義: PSWは実行状態を示す語です（第七十八観点）。第七十八観点 SVCは監視プログラム呼出しです（第七十八観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **FLIH処理 ストレージ確認 運用確認078**

    - 検証目的: FLIH処理 の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: IPCS / dump analysis

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により FLIH処理 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    IPCS option 6
    COMMAND ===> VERBX LOGDATA
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOGDATA VERBEXIT PROCESSING
    LOGREC BUFFER RECORDS LOCATED
    EREP DETAIL EDIT REPORT FOLLOWS
    ```

    画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により FLIH処理 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.30.06 TRACE DISPLAY 177
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
    ```

    画面・出力には IEE843I が含まれる。IEE843I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により FLIH処理 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    IPCS command line
    COMMAND ===> STATUS CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IPCS STATUS CPU
    PSW=070C1000 81234567  ASID=0010
    CURRENT TCB ADDRESS SYS1.PARMLIB(PROGSP)
    ```

    画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### IEFU29出口 定義照合 運用確認061 {#c38-i0272}
*分類: ディスパッチ制御*  ・  難易度: 中級

第六十一観点 ディスパッチ制御 で IEFU29出口 は 定義照合 の対象です（第六十一観点）。第六十一観点 確認時には SMF記録データセットが満杯になった時にダンプ処理へつなぐ出口という性質を前提にします（第六十一観点）。第六十一観点 SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同じ証跡に置き、共通ストレージ変更の記録を管理します（第六十一観点）。第六十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録061から再現します（第六十一観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第六十一証跡です。ディスパッチ制御 の運用で IEFU29出口 を点検します。確認観点は IEFU29出口、定義照合、運用確認 です。SYS1.LINKLIB を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同一票へ記録し、IEFU29出口 を zOSSP正061で確定する。 ✅
    - B. ENQ資源管理 の一般メモを採り、SYS1.LINKLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記061として調査範囲を狭める。
    - C. IEFU29出口 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延061として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在061として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第六十一観点 正解確認: Aは IEFU29出口 と SYS1.LINKLIB を同じ証跡で扱うため、後続の照合に使えます（第六十一観点）。第六十一観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第六十一観点）。第六十一観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第六十一観点）。第六十一観点 用語確認: APFは許可ライブラリーの管理機能です（第六十一観点）。第六十一観点 PROGxxは動的なプログラム管理指定です（第六十一観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **IEFU29出口 定義照合 運用確認061**

    - 検証目的: IEFU29出口 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU29出口 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.13 DISPLAY R 760
    REPLY ID   MESSAGE TEXT
    005        IEA793A SPECIFY DUMP OPTION FOR SYS1.LINKLIB
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU29出口 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.13 CONSOLE DISPLAY 490
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU29出口 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> R 005,INFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO 005 IS;INFO
    IEA631I OPERATOR OPER13 NOW ACTIVE, SYSTEM=SC65
    ```

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### IFASMFDP 定義照合 運用確認011 {#c38-i0273}
*分類: ディスパッチ制御*  ・  難易度: 初級

第十一観点 ディスパッチ制御 の運用では IFASMFDP を表示、定義、証跡で確認します（第十一観点）。第十一観点 役割は SMFデータセットの内容を別データセットへ退避し、再利用できる状態へという範囲です（第十一観点）。第十一観点 SET PROG=xx後のIEE252I表示 の値を TRACE DISPLAY と合わせ、共通ストレージ変更の記録を記録します（第十一観点）。第十一観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録011に残します（第十一観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **IFASMFDP 定義照合 運用確認011**

    - 検証目的: IFASMFDP の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IFASMFDP の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.11 GRS STATUS 830
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IFASMFDP の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.11 GRS STATUS 840
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IFASMFDP の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.11 DISPLAY XCF 850
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### SYS1.PARMLIB 出口確認 運用確認045 {#c38-i0274}
*分類: ディスパッチ制御*  ・  難易度: 中級

第四十五観点 ディスパッチ制御 で SYS1.PARMLIB は 出口確認 の対象です（第四十五観点）。第四十五観点 確認時には IEASYSxx、PROGxx、SMFPRMxx、GRSRNLxxなという性質を前提にします（第四十五観点）。第四十五観点 IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同じ証跡に置き、割り込み経路の説明性確保を管理します（第四十五観点）。第四十五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録045から再現します（第四十五観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第四十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は SYS1.PARMLIB、出口確認、運用確認 です。IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を合わせて読む時の採用方針として正しいものはどれか。

    - A. TCB/SRB管理 の一般メモを採り、QNAME=SYSDSN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記045として調査範囲を狭める。
    - B. IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同一票へ記録し、SYS1.PARMLIB を zOSSP正045で確定する。 ✅
    - C. SYS1.PARMLIB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延045として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在045として残す。

    正解: **B** ／ 難易度: 中級

    **解説:** 第四十五観点 正解確認: Bは SYS1.PARMLIB と QNAME=SYSDSN を同じ証跡で扱うため、後続の照合に使えます（第四十五観点）。第四十五観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第四十五観点）。第四十五観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十五観点）。第四十五観点 用語整理: SMFはシステム測定記録です（第四十五観点）。第四十五観点 IFASMFDPはSMFデータ退避に使います（第四十五観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **SYS1.PARMLIB 出口確認 運用確認045**

    - 検証目的: SYS1.PARMLIB の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / operations

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SYS1.PARMLIB の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY R,ALL
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE112I 11.15.21 DISPLAY R 744
    REPLY ID   MESSAGE TEXT
    005        IEA793A SPECIFY DUMP OPTION FOR QNAME=SYSDSN
    ```

    画面・出力には IEE112I が含まれる。IEE112I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SYS1.PARMLIB の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D C
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE889I 15.33.21 CONSOLE DISPLAY 534
    MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
    CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
    ```

    画面・出力には IEE889I が含まれる。IEE889I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SYS1.PARMLIB の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> R 005,INFO
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE600I REPLY TO 005 IS;INFO
    IEA631I OPERATOR OPER21 NOW ACTIVE, SYSTEM=SC65
    ```

    画面・出力には IEE600I が含まれる。IEE600I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### TCB ストレージ確認 運用確認028 {#c38-i0275}
*分類: ディスパッチ制御*  ・  難易度: 中級

第二十八観点 z/OS System Programming の ディスパッチ制御 では TCB を障害調査で照合します（第二十八観点）。第二十八観点 資料上は タスクの状態、保存情報、実行文脈を保持する制御ブロックとして扱います（第二十八観点）。第二十八観点 SMF.LOGSTREAM.SP を起点に表示値を戻し、診断ログの再現性確保を点検します（第二十八観点）。第二十八観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録028へ書きます（第二十八観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第二十八証跡です。TCB の記録を監査用に整えます。確認観点は TCB、ストレージ確認、運用確認 です。診断ログの再現性確保のために、parmlibメンバーの該当ステートメント を使った運用記録として最も適切な扱いはどれか。

    - A. アドレス空間 の一般メモを採り、SMF.LOGSTREAM.SP、メッセージID、時刻の対応を記録外に置き、zOSSP誤記028として調査範囲を狭める。
    - B. TCB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延028として扱う。
    - C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在028として残す。
    - D. parmlibメンバーの該当ステートメント と SMF.LOGSTREAM.SP を同一票へ記録し、TCB を zOSSP正028で確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第二十八観点 照合結果: Dは SMF.LOGSTREAM.SP をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第二十八観点）。第二十八観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第二十八観点）。第二十八観点 誤答確認: Aは SMF.LOGSTREAM.SP 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第二十八観点）。第二十八観点 用語説明: WTOは通知メッセージです（第二十八観点）。第二十八観点 WTORは応答を求めるメッセージです（第二十八観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **TCB ストレージ確認 運用確認028**

    - 検証目的: TCB の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により TCB の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.04 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により TCB の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SWITCH SMF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
    IEE360I SMF NOW RECORDING ON SMF.MAN2
    ```

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により TCB の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD04
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD04 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、診断ログの再現性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### コンポーネントトレース 出口確認 運用確認095 {#c38-i0276}
*分類: ディスパッチ制御*  ・  難易度: 上級

第九十五観点 ディスパッチ制御 の運用では コンポーネントトレース を表示、定義、証跡で確認します（第九十五観点）。第九十五観点 役割は 指定コンポーネントの内部事象を記録し、障害調査に使うトレース機構という範囲です（第九十五観点）。第九十五観点 IFASMFDPジョブログのSYSPRINT の値を WTOR reply 005 と合わせ、割り込み経路の説明性確保を記録します（第九十五観点）。第九十五観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録095に残します（第九十五観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **コンポーネントトレース 出口確認 運用確認095**

    - 検証目的: コンポーネントトレース の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / WLM dispatch

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により コンポーネントトレース の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D A,L
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE114I 12.05.23 ACTIVE JOBS DISPLAY 614
    JOBNAME  ASID  STATUS
    WLM      000A  ACTIVE
    JES2     0012  ACTIVE
    ```

    画面・出力には IEE114I が含まれる。IEE114I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により コンポーネントトレース の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D WLM,SYSTEMS
    → Enter を押す
    ```

    画面・出力:
    ```text
    IWM026I 12.06.23 WLM DISPLAY 624
    SYSTEM   MODE     POLICY
    SC65     GOAL     POLSP23
    ```

    画面・出力には GOAL が含まれる。GOAL を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により コンポーネントトレース の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    SDSF DA panel
    COMMAND ===> DA
    → Enter を押す
    ```

    画面・出力:
    ```text
    SDSF DA DISPLAY
    JOBNAME  ASID  CPU%  DP
    BATCH23 0023  02.1  245
    ```

    画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。

    - 合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### ディスパッチ制御 SRMディスパッチ状態 ログとの照合 SRM07 {#c38-i0277}
*分類: ディスパッチ制御*  ・  難易度: 中級

ログとの照合では ディスパッチ制御 の CPU表示 を主操作として SRM07 を判定します。時刻と対象識別子への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM07 に残します。ログとの照合を補助する SRM表示 では IRA200I を補助値として SRM07 へ保存します。主判定のログとの照合ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM07 へ残します。証跡照合のログとの照合ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM07 に保存します。記録対応のログとの照合ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で ディスパッチ制御 の CPU表示 と SRM表示 を使い 操作とログを対応 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読み対象 SRM07 を切り分ける確認方法はどれですか。

    - A. IEE174Iを含むCPU表示の応答行を保存する。その応答を得るためD M=CPUを使用する。対象SRM07のCPU使用率と待ちとして記録する。 ✅
    - B. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。RMFをIEE174Iと同じ判定値とみなし対象SRM07の主証跡にする。
    - C. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。
    - D. SRMディスパッチ状態の停止または再定義を実施する。その後にD M=CPUでIEE174Iを採取する。

    正解: **A** ／ 難易度: 中級

    **解説:** 適切な判定: AはCPU表示で IEE174I を読みCPU使用率と待ちの主値として操作とログを対応しSRM07に残します。
    機能の仕組み: ログとの照合ではSRM表示を補助操作としSRMディスパッチ状態の時刻と対象識別子をIRA200Iと対象SRM07で照合します。
    各候補の評価: CPU表示とSRM表示の役割を分けるとA: IEE174Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではCPU使用率と待ちを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではCPU使用率と待ちを証明できない点でCPU使用率と待ちを確認できません、D: 変更前のCPU使用率と待ちを失う点でSRM表示の範囲を越えます。結論としてログとの照合のディスパッチ制御・ディスパッチ状態で判定する対象は SRM07 です。
    用語の定義: ログとの照合で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 ログとの照合 SRM07**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について操作とログを対応し、SRM07のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM07のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM07のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM07のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 代替経路の確認 SRM10 {#c38-i0278}
*分類: ディスパッチ制御*  ・  難易度: 中級

代替経路の確認では ディスパッチ制御 の CPU表示 を主操作として SRM10 を判定します。主経路との役割差への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM10 に残します。代替経路の確認を補助する SRM表示 では IRA200I を補助値として SRM10 へ保存します。主判定の代替経路の確認ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM10 へ残します。証跡照合の代替経路の確認ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM10 に保存します。記録対応の代替経路の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で ディスパッチ制御 の CPU表示 と SRM表示 を照合し 主経路との役割差 を確かめます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読む前に対象 SRM10 へ行う確認はどれですか。

    - A. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。
    - B. SRMディスパッチ状態の停止または再定義を実施する。その後にD M=CPUでIEE174Iを採取する。
    - C. APF管理のDSNAMEとVOLSERを確認する。その値をディスパッチ制御のSRM10にも適用する。
    - D. D M=CPUとD SRMの対象名をそろえる。前者のIEE174IをCPU使用率と待ちの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正しい判定結果: DはCPU表示で IEE174I を読みCPU使用率と待ちの主値として代替手段の成立を確認しSRM10に残します。
    運用上の背景: 代替経路の確認ではSRM表示を補助操作としSRMディスパッチ状態の主経路との役割差をIRA200Iと対象SRM10で照合します。
    候補別の検討: CPU表示とSRM表示の役割を分けるとA: 入力記録だけではCPU使用率と待ちを証明できない点で一次資料と一致しません、B: 変更前のCPU使用率と待ちを失う点でCPU使用率と待ちを確認できません、C: APF管理の値ではIEE174Iを確認できない点でSRM表示の範囲を越えます、D: 同じ対象名のIEE174Iを採用する点で現在値を示します。結論として代替経路の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM10 です。
    重要用語の定義: 代替経路の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 代替経路の確認 SRM10**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について代替手段の成立を確認し、SRM10のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM10のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM10のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM10のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 変更前の確認 SRM02 {#c38-i0279}
*分類: ディスパッチ制御*  ・  難易度: 中級

変更前の確認では ディスパッチ制御 の SRM表示 を主操作として SRM02 を判定します。変更対象と非対象の境界への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM02 に残します。変更前の確認を補助する RMF確認 では RMF を補助値として SRM02 へ保存します。主判定の変更前の確認ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM02 へ残します。証跡照合の変更前の確認ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM02 に保存します。記録対応の変更前の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で ディスパッチ制御 の SRM表示 と RMF確認 を実施し SRMディスパッチ状態 の役割を確認します。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM02 の証跡を取る方法はどれですか。

    - A. D SRMを対象名なしで実行する。一覧の先頭行をSRM02の結果として記録する。
    - B. 前回保存したD SRMの結果を使う。今回のRMF III DELAYの結果と同一時点の証跡として比較する。
    - C. 保存済みのSRM02の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象SRM02についてD SRMの応答からIRA200Iを確認する。RMF III DELAYは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 採用理由: DはSRM表示で IRA200I を読みCPU使用率と待ちの主値として変更前の証跡を保存しSRM02に残します。
    動作の背景: 変更前の確認ではRMF確認を補助操作としSRMディスパッチ状態の変更対象と非対象の境界をRMFと対象SRM02で照合します。
    各選択肢の検討: SRM表示とRMF確認の役割を分けるとA: 先頭行はSRM02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でSRM表示を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でディスパッチ制御に使いません、D: IRA200Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM02 です。
    初出用語の定義: 変更前の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 変更前の確認 SRM02**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について変更前の証跡を保存し、SRM02のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM02のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM02のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM02のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
    ② ステップ2 の DELAY が画面・出力に表示されること
    ③ ステップ3 の IEE174I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 変更後の確認 SRM03 {#c38-i0280}
*分類: ディスパッチ制御*  ・  難易度: 中級

変更後の確認では ディスパッチ制御 の RMF確認 を主操作として SRM03 を判定します。反映値と残存値への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM03 に残します。変更後の確認を補助する CPU表示 では IEE174I を補助値として SRM03 へ保存します。主判定の変更後の確認ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM03 へ残します。証跡照合の変更後の確認ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM03 に保存します。記録対応の変更後の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で ディスパッチ制御 の RMF確認 と CPU表示 を用い 変更結果を検証 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。RMF で対象 SRM03 の CPU使用率と待ち を再現できる記録はどれですか。

    - A. D M=CPUで周辺状態を押さえる。その後にRMF III DELAYでRMFを確認して変更結果を検証する。 ✅
    - B. SRMディスパッチ状態の停止または再定義を実施する。その後にRMF III DELAYでRMFを採取する。
    - C. SAF連携のSAF RCとRACF RCを確認する。その値をディスパッチ制御のSRM03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 中級

    **解説:** 正答の根拠: AはRMF確認で RMF を読みCPU使用率と待ちの主値として変更結果を検証しSRM03に残します。
    内部の仕組み: 変更後の確認ではCPU表示を補助操作としSRMディスパッチ状態の反映値と残存値をIEE174Iと対象SRM03で照合します。
    誤答を含む比較: RMF確認とCPU表示の役割を分けるとA: 周辺状態の後にRMFを確認する点でSRM03を判定できます、B: 変更前のCPU使用率と待ちを失う点でCPU表示の範囲を越えます、C: SAF連携の値ではRMFを確認できないうえに追加前提も不正な点でSRM03の値を示しません、D: 補助操作の成功ではRMFを確定できない点で変更後の確認に合いません。結論として変更後の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM03 です。
    用語定義: 変更後の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 変更後の確認 SRM03**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について変更結果を検証し、SRM03のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM03のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM03のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM03のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
    ② ステップ2 の IEE174I が画面・出力に表示されること
    ③ ステップ3 の IRA200I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 引継ぎ記録 SRM09 {#c38-i0281}
*分類: ディスパッチ制御*  ・  難易度: 中級

引継ぎ記録では ディスパッチ制御 の RMF確認 を主操作として SRM09 を判定します。次担当者が追跡できる証跡への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM09 に残します。引継ぎ記録を補助する CPU表示 では IEE174I を補助値として SRM09 へ保存します。主判定の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM09 へ残します。証跡照合の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM09 に保存します。記録対応の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で ディスパッチ制御 の RMF確認 と CPU表示 を用い 再現可能な記録を作成 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。RMF で対象 SRM09 の CPU使用率と待ち を再現できる記録はどれですか。

    - A. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。
    - B. RMF III DELAYを対象名なしで実行する。一覧の先頭行をSRM09の結果として記録する。
    - C. 対象名SRM09を指定してRMF III DELAYを実行する。応答中のRMFと時刻を保存する。D M=CPUで周辺状態を補完する。 ✅
    - D. 前回保存したRMF III DELAYの結果を使う。今回のD M=CPUの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 中級

    **解説:** 採用操作の理由: CはRMF確認で RMF を読みCPU使用率と待ちの主値として再現可能な記録を作成しSRM09に残します。
    製品内の仕組み: 引継ぎ記録ではCPU表示を補助操作としSRMディスパッチ状態の次担当者が追跡できる証跡をIEE174Iと対象SRM09で照合します。
    選択肢別の説明: RMF確認とCPU表示の役割を分けるとA: 補助操作の成功ではRMFを確定できない点でSRM09の値を示しません、B: 先頭行はSRM09と確定できない点で引継ぎ記録に合いません、C: RMFと時刻を保存する点でRMF確認に合います、D: 採取時刻が異なる点でディスパッチ制御に使いません。結論として引継ぎ記録のディスパッチ制御・ディスパッチ状態で判定する対象は SRM09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 引継ぎ記録 SRM09**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について再現可能な記録を作成し、SRM09のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM09のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM09のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM09のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
    ② ステップ2 の IEE174I が画面・出力に表示されること
    ③ ステップ3 の IRA200I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 復旧後の確認 SRM06 {#c38-i0282}
*分類: ディスパッチ制御*  ・  難易度: 中級

復旧後の確認では ディスパッチ制御 の RMF確認 を主操作として SRM06 を判定します。再発していないことを示す値への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM06 に残します。復旧後の確認を補助する CPU表示 では IEE174I を補助値として SRM06 へ保存します。主判定の復旧後の確認ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM06 へ残します。証跡照合の復旧後の確認ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM06 に保存します。記録対応の復旧後の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で ディスパッチ制御 の RMF確認 と CPU表示 の役割を分け 再発していないことを示す値 を調べます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM06 を誤判定しない進め方はどれですか。

    - A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をディスパッチ制御のSRM06にも適用する。
    - B. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SRM06へ引き継げるものとする。
    - C. RMF III DELAYを対象名なしで実行する。一覧の先頭行をSRM06の結果として記録する。
    - D. RMF III DELAYでRMFを取得してからD SRMでIRA200Iを照合する。SRM06のCPU使用率と待ちを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 正答内容: DはRMF確認で RMF を読みCPU使用率と待ちの主値として復旧後の安定性を確認しSRM06に残します。
    構成上の背景: 復旧後の確認ではCPU表示を補助操作としSRMディスパッチ状態の再発していないことを示す値をIEE174Iと対象SRM06で照合します。
    候補ごとの理由: RMF確認とCPU表示の役割を分けるとA: Cross Memoryの値ではRMFを確認できない点でCPU表示の範囲を越えます、B: 補助操作の成功ではRMFを確定できないうえに追加前提も不正な点でSRM06の値を示しません、C: 先頭行はSRM06と確定できない点で復旧後の確認に合いません、D: RMFとIRA200Iを順に照合する点でRMF確認に合います。結論として復旧後の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM06 です。
    初出用語: 復旧後の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 復旧後の確認 SRM06**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について復旧後の安定性を確認し、SRM06のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM06のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM06のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM06のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
    ② ステップ2 の IEE174I が画面・出力に表示されること
    ③ ステップ3 の IRA200I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 復旧準備 SRM05 {#c38-i0283}
*分類: ディスパッチ制御*  ・  難易度: 中級

復旧準備では ディスパッチ制御 の SRM表示 を主操作として SRM05 を判定します。再開前に必要な整合性への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM05 に残します。復旧準備を補助する RMF確認 では RMF を補助値として SRM05 へ保存します。主判定の復旧準備ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM05 へ残します。証跡照合の復旧準備ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM05 に保存します。記録対応の復旧準備ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で ディスパッチ制御 の SRM表示 と RMF確認 を組み合わせる際は SRMディスパッチ状態 がサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能という仕組みを前提にします。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IRA200I と CPU使用率と待ち を対象 SRM05 で確認する組合せはどれですか。

    - A. 前回保存したD SRMの結果を使う。今回のRMF III DELAYの結果と同一時点の証跡として比較する。
    - B. 保存済みのSRM05の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。
    - C. 変更を加えずD SRMを実行する。IRA200Iを保存する。差分はRMF III DELAYの結果と対象名で対応させる。 ✅
    - D. RMF III DELAYのRMFをCPU使用率と待ちの主判定に採用する。D SRMの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 中級

    **解説:** 選定理由: CはSRM表示で IRA200I を読みCPU使用率と待ちの主値として復旧条件を確認しSRM05に残します。
    処理の仕組み: 復旧準備ではRMF確認を補助操作としSRMディスパッチ状態の再開前に必要な整合性をRMFと対象SRM05で照合します。
    選択結果の内訳: SRM表示とRMF確認の役割を分けるとA: 採取時刻が異なる点でSRM表示を代替しません、B: 過去出力では今回の復旧準備を示せない点でディスパッチ制御に使いません、C: 変更前のIRA200Iを保存する点で正答です、D: RMFはIRA200Iを代替しないうえに追加前提も不正な点でSRM05を採用できません。結論として復旧準備のディスパッチ制御・ディスパッチ状態で判定する対象は SRM05 です。
    用語の説明: 復旧準備で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 復旧準備 SRM05**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について復旧条件を確認し、SRM05のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM05のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM05のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM05のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
    ② ステップ2 の DELAY が画面・出力に表示されること
    ③ ステップ3 の IEE174I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 構成監査 SRM08 {#c38-i0284}
*分類: ディスパッチ制御*  ・  難易度: 中級

構成監査では ディスパッチ制御 の SRM表示 を主操作として SRM08 を判定します。定義値と稼働値の一致への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM08 に残します。構成監査を補助する RMF確認 では RMF を補助値として SRM08 へ保存します。主判定の構成監査ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM08 へ残します。証跡照合の構成監査ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM08 に保存します。記録対応の構成監査ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で ディスパッチ制御 の SRM表示 と RMF確認 を実施し SRMディスパッチ状態 の役割を確認します。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM08 の証跡を取る方法はどれですか。

    - A. 保存済みのSRM08の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。
    - B. RMF III DELAYの結果だけでは確定しない。D SRMのIRA200Iを主証跡として構成差分を監査する。 ✅
    - C. RMF III DELAYのRMFをCPU使用率と待ちの主判定に採用する。D SRMの応答は採取対象から外す。
    - D. D M=CPUのIEE174IをIRA200Iと同義の成功表示として扱う。D SRMは実行しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 技術上の正答: BはSRM表示で IRA200I を読みCPU使用率と待ちの主値として構成差分を監査しSRM08に残します。
    実行時の背景: 構成監査ではRMF確認を補助操作としSRMディスパッチ状態の定義値と稼働値の一致をRMFと対象SRM08で照合します。
    四つの候補の理由: SRM表示とRMF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でディスパッチ制御に使いません、B: IRA200Iを主証跡として区別する点で正答です、C: RMFはIRA200Iを代替しない点でSRM08を採用できません、D: IEE174IとIRA200Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のディスパッチ制御・ディスパッチ状態で判定する対象は SRM08 です。
    初出語定義: 構成監査で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 構成監査 SRM08**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について構成差分を監査し、SRM08のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM08のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM08のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM08のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
    ② ステップ2 の DELAY が画面・出力に表示されること
    ③ ステップ3 の IEE174I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 通常状態の確認 SRM01 {#c38-i0285}
*分類: ディスパッチ制御*  ・  難易度: 中級

通常状態の確認では ディスパッチ制御 の CPU表示 を主操作として SRM01 を判定します。基準値と現在値の差への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM01 に残します。通常状態の確認を補助する SRM表示 では IRA200I を補助値として SRM01 へ保存します。主判定の通常状態の確認ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM01 へ残します。証跡照合の通常状態の確認ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM01 に保存します。記録対応の通常状態の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で ディスパッチ制御 の CPU表示 と SRM表示 を使い 通常状態を確定 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読み対象 SRM01 を切り分ける確認方法はどれですか。

    - A. D SRMのIRA200IをCPU使用率と待ちの主判定に採用する。D M=CPUの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. RMF III DELAYのRMFをIEE174Iと同義の成功表示として扱う。D M=CPUは実行しない。
    - C. D M=CPUを先に実行する。対象SRM01のIEE174IをCPU使用率と待ちとして記録する。続いてD SRMで同一対象を照合する。 ✅
    - D. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。

    正解: **C** ／ 難易度: 中級

    **解説:** 正解の説明: CはCPU表示で IEE174I を読みCPU使用率と待ちの主値として通常状態を確定しSRM01に残します。
    背景・仕組み: 通常状態の確認ではSRM表示を補助操作としSRMディスパッチ状態の基準値と現在値の差をIRA200Iと対象SRM01で照合します。
    選択肢の理由: CPU表示とSRM表示の役割を分けるとA: IRA200IはIEE174Iを代替しないうえに追加前提も不正な点でSRMディスパッチ状態に使えません、B: RMFとIEE174Iは確認項目が異なる点でSRM01を採用できません、C: IEE174Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではCPU使用率と待ちを判定できない点で一次資料と一致しません。結論として通常状態の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM01 です。
    用語の初出定義: 通常状態の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 通常状態の確認 SRM01**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について通常状態を確定し、SRM01のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM01のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM01のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM01のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### ディスパッチ制御 SRMディスパッチ状態 障害切り分け SRM04 {#c38-i0286}
*分類: ディスパッチ制御*  ・  難易度: 中級

障害切り分けでは ディスパッチ制御 の CPU表示 を主操作として SRM04 を判定します。最初に失敗した処理への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM04 に残します。障害切り分けを補助する SRM表示 では IRA200I を補助値として SRM04 へ保存します。主判定の障害切り分けではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM04 へ残します。証跡照合の障害切り分けではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM04 に保存します。記録対応の障害切り分けではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで ディスパッチ制御 の CPU表示 と SRM表示 を照合し 最初に失敗した処理 を確かめます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読む前に対象 SRM04 へ行う確認はどれですか。

    - A. RMF III DELAYのRMFをIEE174Iと同義の成功表示として扱う。D M=CPUは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D M=CPUの出力でSRM04とIEE174Iが同じ応答にあることを確認する。CPU使用率と待ちをその応答から採取する。 ✅
    - C. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。
    - D. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 中級

    **解説:** 正しい操作の説明: BはCPU表示で IEE174I を読みCPU使用率と待ちの主値として障害範囲を限定しSRM04に残します。
    技術的背景: 障害切り分けではSRM表示を補助操作としSRMディスパッチ状態の最初に失敗した処理をIRA200Iと対象SRM04で照合します。
    四択の評価: CPU表示とSRM表示の役割を分けるとA: RMFとIEE174Iは確認項目が異なるうえに追加前提も不正な点でSRM04を採用できません、B: SRM04とIEE174Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではCPU使用率と待ちを判定できない点で一次資料と一致しません、D: 入力記録だけではCPU使用率と待ちを証明できない点でCPU使用率と待ちを確認できません。結論として障害切り分けのディスパッチ制御・ディスパッチ状態で判定する対象は SRM04 です。
    初出語の意味: 障害切り分けで使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **ディスパッチ制御 SRMディスパッチ状態 障害切り分け SRM04**

    - 検証目的: ディスパッチ制御のSRMディスパッチ状態について障害範囲を限定し、SRM04のCPU使用率と待ちを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象SRM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM04のCPU表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D M=CPU
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
    ```

    画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM04のSRM表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D SRM
    → Enter を押す
    ```

    画面・出力:
    ```text
    IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
    ```

    画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM04のRMF確認を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> RMF III DELAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
    ```

    画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
    ② ステップ2 の IRA200I が画面・出力に表示されること
    ③ ステップ3 の DELAY が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12




## z/OS System Programming > トレース診断

### DEQマクロ 割り込み確認 運用確認067 {#c38-i0287}
*分類: トレース診断*  ・  難易度: 中級

第六十七観点 トレース診断 の運用では DEQマクロ を表示、定義、証跡で確認します（第六十七観点）。第六十七観点 役割は ENQで取得した資源の直列化を解放し、後続処理へ資源を渡すマクロという範囲です（第六十七観点）。第六十七観点 IPCS VERBX LOGDATA出力 の値を SMF.MAN1 と合わせ、オペレーター応答漏れの防止を記録します（第六十七観点）。第六十七観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録067に残します（第六十七観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第六十七証跡です。トレース診断 の当日作業で SMF.MAN1 を追跡します。確認観点は DEQマクロ、割り込み確認、運用確認 です。SMF.MAN1 を根拠として残す時、対象の取り違えを抑える対応はどれか。

    - A. PSW/割り込み の一般メモを採り、SMF.MAN1、メッセージID、時刻の対応を記録外に置き、zOSSP誤記067として調査範囲を狭める。
    - B. DEQマクロ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延067として扱う。
    - C. IPCS VERBX LOGDATA出力 と SMF.MAN1 を同一票へ記録し、DEQマクロ を zOSSP正067で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在067として残す。

    正解: **C** ／ 難易度: 中級

    **解説:** 第六十七観点 採用理由: Cは DEQマクロ の状態を表示値と定義の両方から確認するため、記録として妥当です（第六十七観点）。第六十七観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第六十七観点）。第六十七観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第六十七観点）。第六十七観点 用語確認: APFは許可ライブラリーの管理機能です（第六十七観点）。第六十七観点 PROGxxは動的なプログラム管理指定です（第六十七観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **DEQマクロ 割り込み確認 運用確認067**

    - 検証目的: DEQマクロ の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / GRS

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により DEQマクロ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.27.19 GRS STATUS 886
    SYSTEM    STATE               SYSTEM    STATE
    SC65      CONNECTED           SC63      CONNECTED
    GRS STAR MODE INFORMATION
    ```

    画面・出力には ISG343I が含まれる。ISG343I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により DEQマクロ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> DISPLAY GRS,RNL=INCL
    → Enter を押す
    ```

    画面・出力:
    ```text
    ISG343I 10.28.19 GRS STATUS 896
    RNL=INCL
    QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
    ```

    画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により DEQマクロ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D XCF,STR,STRNAME=ISGLOCK
    → Enter を押す
    ```

    画面・出力:
    ```text
    IXC360I 10.29.19 DISPLAY XCF 906
    STRUCTURE NAME: ISGLOCK
    STATUS: ALLOCATED IN CFRM POLICY
    ```

    画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### ISGENQマクロ 割り込み確認 運用確認017 {#c38-i0288}
*分類: トレース診断*  ・  難易度: 初級

第十七観点 トレース診断 で ISGENQマクロ は 割り込み確認 の対象です（第十七観点）。第十七観点 確認時には ENQ、DEQ、RESERVEの機能を統合し、31ビットと64ビットという性質を前提にします（第十七観点）。第十七観点 IPCS VERBX LOGDATA出力 と AUTH=CMDS を同じ証跡に置き、オペレーター応答漏れの防止を管理します（第十七観点）。第十七観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録017から再現します（第十七観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? note "検証手順（1件）"
    **ISGENQマクロ 割り込み確認 運用確認017**

    - 検証目的: ISGENQマクロ の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SDSF LOG

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ISGENQマクロ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.18.17 PROG,APF DISPLAY 916
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       2  MPRES1 SYS1.SVCLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ISGENQマクロ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
    ```

    画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ISGENQマクロ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF,ENTRY=(1-5)
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 05.26.17 PROG,APF DISPLAY 966
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
       1  MPRES1 SYS1.LINKLIB
       5  MPRES1 ISF.SISFLPA
    ```

    画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。

    - 合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### トレース診断 システムトレース ログとの照合 TRC07 {#c38-i0289}
*分類: トレース診断*  ・  難易度: 上級

ログとの照合では トレース診断 の トレース状態 を主操作として TRC07 を判定します。時刻と対象識別子への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC07 に残します。ログとの照合を補助する バッファ指定 では IEE839I を補助値として TRC07 へ保存します。主判定のログとの照合ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC07 へ残します。証跡照合のログとの照合ではトレース診断・システムトレースの IEE843I と IEE839I を TRC07 に保存します。記録対応のログとの照合ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で トレース診断 の トレース状態 と バッファ指定 を使い 操作とログを対応 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読み対象 TRC07 を切り分ける確認方法はどれですか。

    - A. IEE843Iを含むトレース状態の応答行を保存する。その応答を得るためD TRACEを使用する。対象TRC07のTRACE STATUSとBUFFERとして記録する。 ✅
    - B. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。SYSTEMをIEE843Iと同じ判定値とみなし対象TRC07の主証跡にする。システムトレースの時刻と対象識別子は確認済みとして扱う。さらにIP SYSTRACEのSYSTEMをIEE843Iと同種の値として併記する。
    - C. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。
    - D. システムトレースの停止または再定義を実施する。その後にD TRACEでIEE843Iを採取する。

    正解: **A** ／ 難易度: 上級

    **解説:** 適切な判定: Aはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として操作とログを対応しTRC07に残します。
    機能の仕組み: ログとの照合ではバッファ指定を補助操作としシステムトレースの時刻と対象識別子をIEE839Iと対象TRC07で照合します。
    各候補の評価: トレース状態とバッファ指定の役割を分けるとA: IEE843Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではTRACE STATUSとBUFFERを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではTRACE STATUSとBUFFERを証明できない点でTRACE STATUSとBUFFERを確認できません、D: 変更前のTRACE STATUSとBUFFERを失う点でバッファ指定の範囲を越えます。結論としてログとの照合のトレース診断・システムトレースで判定する対象は TRC07 です。
    用語の定義: ログとの照合で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース ログとの照合 TRC07**

    - 検証目的: トレース診断のシステムトレースについて操作とログを対応し、TRC07のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC07のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC07のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC07のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0007 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 代替経路の確認 TRC10 {#c38-i0290}
*分類: トレース診断*  ・  難易度: 上級

代替経路の確認では トレース診断 の トレース状態 を主操作として TRC10 を判定します。主経路との役割差への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC10 に残します。代替経路の確認を補助する バッファ指定 では IEE839I を補助値として TRC10 へ保存します。主判定の代替経路の確認ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC10 へ残します。証跡照合の代替経路の確認ではトレース診断・システムトレースの IEE843I と IEE839I を TRC10 に保存します。記録対応の代替経路の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で トレース診断 の トレース状態 と バッファ指定 を照合し 主経路との役割差 を確かめます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読む前に対象 TRC10 へ行う確認はどれですか。

    - A. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。
    - B. システムトレースの停止または再定義を実施する。その後にD TRACEでIEE843Iを採取する。
    - C. APF管理のDSNAMEとVOLSERを確認する。その値をトレース診断のTRC10にも適用する。
    - D. D TRACEとTRACE ST,2Mの対象名をそろえる。前者のIEE843IをTRACE STATUSとBUFFERの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正しい判定結果: Dはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として代替手段の成立を確認しTRC10に残します。
    運用上の背景: 代替経路の確認ではバッファ指定を補助操作としシステムトレースの主経路との役割差をIEE839Iと対象TRC10で照合します。
    候補別の検討: トレース状態とバッファ指定の役割を分けるとA: 入力記録だけではTRACE STATUSとBUFFERを証明できない点で一次資料と一致しません、B: 変更前のTRACE STATUSとBUFFERを失う点でTRACE STATUSとBUFFERを確認できません、C: APF管理の値ではIEE843Iを確認できない点でバッファ指定の範囲を越えます、D: 同じ対象名のIEE843Iを採用する点で現在値を示します。結論として代替経路の確認のトレース診断・システムトレースで判定する対象は TRC10 です。
    重要用語の定義: 代替経路の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 代替経路の確認 TRC10**

    - 検証目的: トレース診断のシステムトレースについて代替手段の成立を確認し、TRC10のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC10のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC10のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC10のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0010 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 変更前の確認 TRC02 {#c38-i0291}
*分類: トレース診断*  ・  難易度: 上級

変更前の確認では トレース診断 の バッファ指定 を主操作として TRC02 を判定します。変更対象と非対象の境界への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC02 に残します。変更前の確認を補助する IPCS表示 では SYSTEM を補助値として TRC02 へ保存します。主判定の変更前の確認ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC02 へ残します。証跡照合の変更前の確認ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC02 に保存します。記録対応の変更前の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で トレース診断 の バッファ指定 と IPCS表示 を実施し システムトレース の役割を確認します。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC02 の証跡を取る方法はどれですか。

    - A. TRACE ST,2Mを対象名なしで実行する。一覧の先頭行をTRC02の結果として記録する。
    - B. 前回保存したTRACE ST,2Mの結果を使う。今回のIP SYSTRACEの結果と同一時点の証跡として比較する。
    - C. 保存済みのTRC02の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象TRC02についてTRACE ST,2Mの応答からIEE839Iを確認する。IP SYSTRACEは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 採用理由: Dはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として変更前の証跡を保存しTRC02に残します。
    動作の背景: 変更前の確認ではIPCS表示を補助操作としシステムトレースの変更対象と非対象の境界をSYSTEMと対象TRC02で照合します。
    各選択肢の検討: バッファ指定とIPCS表示の役割を分けるとA: 先頭行はTRC02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でバッファ指定を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でトレース診断に使いません、D: IEE839Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のトレース診断・システムトレースで判定する対象は TRC02 です。
    初出用語の定義: 変更前の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 変更前の確認 TRC02**

    - 検証目的: トレース診断のシステムトレースについて変更前の証跡を保存し、TRC02のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC02のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC02のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0002 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC02のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
    ② ステップ2 の SYSTEM が画面・出力に表示されること
    ③ ステップ3 の IEE843I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 変更後の確認 TRC03 {#c38-i0292}
*分類: トレース診断*  ・  難易度: 上級

変更後の確認では トレース診断 の IPCS表示 を主操作として TRC03 を判定します。反映値と残存値への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC03 に残します。変更後の確認を補助する トレース状態 では IEE843I を補助値として TRC03 へ保存します。主判定の変更後の確認ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC03 へ残します。証跡照合の変更後の確認ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC03 に保存します。記録対応の変更後の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で トレース診断 の IPCS表示 と トレース状態 を用い 変更結果を検証 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。SYSTEM で対象 TRC03 の TRACE STATUSとBUFFER を再現できる記録はどれですか。

    - A. D TRACEで周辺状態を押さえる。その後にIP SYSTRACEでSYSTEMを確認して変更結果を検証する。 ✅
    - B. システムトレースの停止または再定義を実施する。その後にIP SYSTRACEでSYSTEMを採取する。
    - C. SAF連携のSAF RCとRACF RCを確認する。その値をトレース診断のTRC03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正答の根拠: AはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として変更結果を検証しTRC03に残します。
    内部の仕組み: 変更後の確認ではトレース状態を補助操作としシステムトレースの反映値と残存値をIEE843Iと対象TRC03で照合します。
    誤答を含む比較: IPCS表示とトレース状態の役割を分けるとA: 周辺状態の後にSYSTEMを確認する点でTRC03を判定できます、B: 変更前のTRACE STATUSとBUFFERを失う点でトレース状態の範囲を越えます、C: SAF連携の値ではSYSTEMを確認できないうえに追加前提も不正な点でTRC03の値を示しません、D: 補助操作の成功ではSYSTEMを確定できない点で変更後の確認に合いません。結論として変更後の確認のトレース診断・システムトレースで判定する対象は TRC03 です。
    用語定義: 変更後の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 変更後の確認 TRC03**

    - 検証目的: トレース診断のシステムトレースについて変更結果を検証し、TRC03のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC03のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0003 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC03のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC03のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
    ② ステップ2 の IEE843I が画面・出力に表示されること
    ③ ステップ3 の IEE839I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 引継ぎ記録 TRC09 {#c38-i0293}
*分類: トレース診断*  ・  難易度: 上級

引継ぎ記録では トレース診断 の IPCS表示 を主操作として TRC09 を判定します。次担当者が追跡できる証跡への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC09 に残します。引継ぎ記録を補助する トレース状態 では IEE843I を補助値として TRC09 へ保存します。主判定の引継ぎ記録ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC09 へ残します。証跡照合の引継ぎ記録ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC09 に保存します。記録対応の引継ぎ記録ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で トレース診断 の IPCS表示 と トレース状態 を用い 再現可能な記録を作成 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。SYSTEM で対象 TRC09 の TRACE STATUSとBUFFER を再現できる記録はどれですか。

    - A. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。
    - B. IP SYSTRACEを対象名なしで実行する。一覧の先頭行をTRC09の結果として記録する。
    - C. 対象名TRC09を指定してIP SYSTRACEを実行する。応答中のSYSTEMと時刻を保存する。D TRACEで周辺状態を補完する。 ✅
    - D. 前回保存したIP SYSTRACEの結果を使う。今回のD TRACEの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 上級

    **解説:** 採用操作の理由: CはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として再現可能な記録を作成しTRC09に残します。
    製品内の仕組み: 引継ぎ記録ではトレース状態を補助操作としシステムトレースの次担当者が追跡できる証跡をIEE843Iと対象TRC09で照合します。
    選択肢別の説明: IPCS表示とトレース状態の役割を分けるとA: 補助操作の成功ではSYSTEMを確定できない点でTRC09の値を示しません、B: 先頭行はTRC09と確定できない点で引継ぎ記録に合いません、C: SYSTEMと時刻を保存する点でIPCS表示に合います、D: 採取時刻が異なる点でトレース診断に使いません。結論として引継ぎ記録のトレース診断・システムトレースで判定する対象は TRC09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 引継ぎ記録 TRC09**

    - 検証目的: トレース診断のシステムトレースについて再現可能な記録を作成し、TRC09のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC09のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0009 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC09のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC09のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
    ② ステップ2 の IEE843I が画面・出力に表示されること
    ③ ステップ3 の IEE839I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 復旧後の確認 TRC06 {#c38-i0294}
*分類: トレース診断*  ・  難易度: 上級

復旧後の確認では トレース診断 の IPCS表示 を主操作として TRC06 を判定します。再発していないことを示す値への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC06 に残します。復旧後の確認を補助する トレース状態 では IEE843I を補助値として TRC06 へ保存します。主判定の復旧後の確認ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC06 へ残します。証跡照合の復旧後の確認ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC06 に保存します。記録対応の復旧後の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で トレース診断 の IPCS表示 と トレース状態 の役割を分け 再発していないことを示す値 を調べます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC06 を誤判定しない進め方はどれですか。

    - A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をトレース診断のTRC06にも適用する。
    - B. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象TRC06へ引き継げるものとする。システムトレースの再発していないことを示す値は確認済みとして扱う。さらにTRACE ST,2MのIEE839IをSYSTEMと同種の値として併記する。
    - C. IP SYSTRACEを対象名なしで実行する。一覧の先頭行をTRC06の結果として記録する。
    - D. IP SYSTRACEでSYSTEMを取得してからTRACE ST,2MでIEE839Iを照合する。TRC06のTRACE STATUSとBUFFERを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正答内容: DはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として復旧後の安定性を確認しTRC06に残します。
    構成上の背景: 復旧後の確認ではトレース状態を補助操作としシステムトレースの再発していないことを示す値をIEE843Iと対象TRC06で照合します。
    候補ごとの理由: IPCS表示とトレース状態の役割を分けるとA: Cross Memoryの値ではSYSTEMを確認できない点でトレース状態の範囲を越えます、B: 補助操作の成功ではSYSTEMを確定できないうえに追加前提も不正な点でTRC06の値を示しません、C: 先頭行はTRC06と確定できない点で復旧後の確認に合いません、D: SYSTEMとIEE839Iを順に照合する点でIPCS表示に合います。結論として復旧後の確認のトレース診断・システムトレースで判定する対象は TRC06 です。
    初出用語: 復旧後の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 復旧後の確認 TRC06**

    - 検証目的: トレース診断のシステムトレースについて復旧後の安定性を確認し、TRC06のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC06のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0006 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC06のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC06のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
    ② ステップ2 の IEE843I が画面・出力に表示されること
    ③ ステップ3 の IEE839I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 復旧準備 TRC05 {#c38-i0295}
*分類: トレース診断*  ・  難易度: 上級

復旧準備では トレース診断 の バッファ指定 を主操作として TRC05 を判定します。再開前に必要な整合性への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC05 に残します。復旧準備を補助する IPCS表示 では SYSTEM を補助値として TRC05 へ保存します。主判定の復旧準備ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC05 へ残します。証跡照合の復旧準備ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC05 に保存します。記録対応の復旧準備ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で トレース診断 の バッファ指定 と IPCS表示 を組み合わせる際は システムトレース が割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能という仕組みを前提にします。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE839I と TRACE STATUSとBUFFER を対象 TRC05 で確認する組合せはどれですか。

    - A. 前回保存したTRACE ST,2Mの結果を使う。今回のIP SYSTRACEの結果と同一時点の証跡として比較する。
    - B. 保存済みのTRC05の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。
    - C. 変更を加えずTRACE ST,2Mを実行する。IEE839Iを保存する。差分はIP SYSTRACEの結果と対象名で対応させる。 ✅
    - D. IP SYSTRACEのSYSTEMをTRACE STATUSとBUFFERの主判定に採用する。TRACE ST,2Mの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: Cはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として復旧条件を確認しTRC05に残します。
    処理の仕組み: 復旧準備ではIPCS表示を補助操作としシステムトレースの再開前に必要な整合性をSYSTEMと対象TRC05で照合します。
    選択結果の内訳: バッファ指定とIPCS表示の役割を分けるとA: 採取時刻が異なる点でバッファ指定を代替しません、B: 過去出力では今回の復旧準備を示せない点でトレース診断に使いません、C: 変更前のIEE839Iを保存する点で正答です、D: SYSTEMはIEE839Iを代替しないうえに追加前提も不正な点でTRC05を採用できません。結論として復旧準備のトレース診断・システムトレースで判定する対象は TRC05 です。
    用語の説明: 復旧準備で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 復旧準備 TRC05**

    - 検証目的: トレース診断のシステムトレースについて復旧条件を確認し、TRC05のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC05のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC05のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0005 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC05のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
    ② ステップ2 の SYSTEM が画面・出力に表示されること
    ③ ステップ3 の IEE843I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 構成監査 TRC08 {#c38-i0296}
*分類: トレース診断*  ・  難易度: 上級

構成監査では トレース診断 の バッファ指定 を主操作として TRC08 を判定します。定義値と稼働値の一致への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC08 に残します。構成監査を補助する IPCS表示 では SYSTEM を補助値として TRC08 へ保存します。主判定の構成監査ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC08 へ残します。証跡照合の構成監査ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC08 に保存します。記録対応の構成監査ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で トレース診断 の バッファ指定 と IPCS表示 を実施し システムトレース の役割を確認します。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC08 の証跡を取る方法はどれですか。

    - A. 保存済みのTRC08の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。
    - B. IP SYSTRACEの結果だけでは確定しない。TRACE ST,2MのIEE839Iを主証跡として構成差分を監査する。 ✅
    - C. IP SYSTRACEのSYSTEMをTRACE STATUSとBUFFERの主判定に採用する。TRACE ST,2Mの応答は採取対象から外す。
    - D. D TRACEのIEE843IをIEE839Iと同義の成功表示として扱う。TRACE ST,2Mは実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: Bはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として構成差分を監査しTRC08に残します。
    実行時の背景: 構成監査ではIPCS表示を補助操作としシステムトレースの定義値と稼働値の一致をSYSTEMと対象TRC08で照合します。
    四つの候補の理由: バッファ指定とIPCS表示の役割を分けるとA: 過去出力では今回の構成監査を示せない点でトレース診断に使いません、B: IEE839Iを主証跡として区別する点で正答です、C: SYSTEMはIEE839Iを代替しない点でTRC08を採用できません、D: IEE843IとIEE839Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のトレース診断・システムトレースで判定する対象は TRC08 です。
    初出語定義: 構成監査で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 構成監査 TRC08**

    - 検証目的: トレース診断のシステムトレースについて構成差分を監査し、TRC08のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC08のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC08のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0008 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC08のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
    ② ステップ2 の SYSTEM が画面・出力に表示されること
    ③ ステップ3 の IEE843I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 通常状態の確認 TRC01 {#c38-i0297}
*分類: トレース診断*  ・  難易度: 上級

通常状態の確認では トレース診断 の トレース状態 を主操作として TRC01 を判定します。基準値と現在値の差への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC01 に残します。通常状態の確認を補助する バッファ指定 では IEE839I を補助値として TRC01 へ保存します。主判定の通常状態の確認ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC01 へ残します。証跡照合の通常状態の確認ではトレース診断・システムトレースの IEE843I と IEE839I を TRC01 に保存します。記録対応の通常状態の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で トレース診断 の トレース状態 と バッファ指定 を使い 通常状態を確定 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読み対象 TRC01 を切り分ける確認方法はどれですか。

    - A. TRACE ST,2MのIEE839IをTRACE STATUSとBUFFERの主判定に採用する。D TRACEの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. IP SYSTRACEのSYSTEMをIEE843Iと同義の成功表示として扱う。D TRACEは実行しない。
    - C. D TRACEを先に実行する。対象TRC01のIEE843IをTRACE STATUSとBUFFERとして記録する。続いてTRACE ST,2Mで同一対象を照合する。 ✅
    - D. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として通常状態を確定しTRC01に残します。
    背景・仕組み: 通常状態の確認ではバッファ指定を補助操作としシステムトレースの基準値と現在値の差をIEE839Iと対象TRC01で照合します。
    選択肢の理由: トレース状態とバッファ指定の役割を分けるとA: IEE839IはIEE843Iを代替しないうえに追加前提も不正な点でシステムトレースに使えません、B: SYSTEMとIEE843Iは確認項目が異なる点でTRC01を採用できません、C: IEE843Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではTRACE STATUSとBUFFERを判定できない点で一次資料と一致しません。結論として通常状態の確認のトレース診断・システムトレースで判定する対象は TRC01 です。
    用語の初出定義: 通常状態の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 通常状態の確認 TRC01**

    - 検証目的: トレース診断のシステムトレースについて通常状態を確定し、TRC01のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC01のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC01のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC01のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0001 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 障害切り分け TRC04 {#c38-i0298}
*分類: トレース診断*  ・  難易度: 上級

障害切り分けでは トレース診断 の トレース状態 を主操作として TRC04 を判定します。最初に失敗した処理への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC04 に残します。障害切り分けを補助する バッファ指定 では IEE839I を補助値として TRC04 へ保存します。主判定の障害切り分けではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC04 へ残します。証跡照合の障害切り分けではトレース診断・システムトレースの IEE843I と IEE839I を TRC04 に保存します。記録対応の障害切り分けではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで トレース診断 の トレース状態 と バッファ指定 を照合し 最初に失敗した処理 を確かめます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読む前に対象 TRC04 へ行う確認はどれですか。

    - A. IP SYSTRACEのSYSTEMをIEE843Iと同義の成功表示として扱う。D TRACEは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D TRACEの出力でTRC04とIEE843Iが同じ応答にあることを確認する。TRACE STATUSとBUFFERをその応答から採取する。 ✅
    - C. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。
    - D. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として障害範囲を限定しTRC04に残します。
    技術的背景: 障害切り分けではバッファ指定を補助操作としシステムトレースの最初に失敗した処理をIEE839Iと対象TRC04で照合します。
    四択の評価: トレース状態とバッファ指定の役割を分けるとA: SYSTEMとIEE843Iは確認項目が異なるうえに追加前提も不正な点でTRC04を採用できません、B: TRC04とIEE843Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではTRACE STATUSとBUFFERを判定できない点で一次資料と一致しません、D: 入力記録だけではTRACE STATUSとBUFFERを証明できない点でTRACE STATUSとBUFFERを確認できません。結論として障害切り分けのトレース診断・システムトレースで判定する対象は TRC04 です。
    初出語の意味: 障害切り分けで使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 障害切り分け TRC04**

    - 検証目的: トレース診断のシステムトレースについて障害範囲を限定し、TRC04のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC04のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC04のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC04のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0004 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### 共通サービス域 ログ確認 運用確認084 {#c38-i0299}
*分類: トレース診断*  ・  難易度: 上級

第八十四観点 z/OS System Programming の トレース診断 では 共通サービス域 を障害調査で照合します（第八十四観点）。第八十四観点 資料上は CSAなど複数アドレス空間から参照される共通ストレージ領域として扱います（第八十四観点）。第八十四観点 ISGLOCK を起点に表示値を戻し、共通ストレージ変更の記録を点検します（第八十四観点）。第八十四観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録084へ書きます（第八十四観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第八十四証跡です。z/OS System Programming の トレース診断 で切分けを行います。確認観点は 共通サービス域、ログ確認、運用確認 です。共通ストレージ変更の記録を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. SVC処理 の一般メモを採り、ISGLOCK、メッセージID、時刻の対応を記録外に置き、zOSSP誤記084として調査範囲を狭める。
    - B. 共通サービス域 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延084として扱う。
    - C. SWITCH SMF後のSMF切替記録 と ISGLOCK を同一票へ記録し、共通サービス域 を zOSSP正084で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在084として残す。

    正解: **C** ／ 難易度: 上級

    **解説:** 第八十四観点 照合結果: Cは ISGLOCK をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十四観点）。第八十四観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第八十四観点）。第八十四観点 誤答確認: Aは ISGLOCK 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第八十四観点）。第八十四観点 初出定義: PSWは実行状態を示す語です（第八十四観点）。第八十四観点 SVCは監視プログラム呼出しです（第八十四観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **共通サービス域 ログ確認 運用確認084**

    - 検証目的: 共通サービス域 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により 共通サービス域 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.12 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により 共通サービス域 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SWITCH SMF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
    IEE360I SMF NOW RECORDING ON SMF.MAN2
    ```

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により 共通サービス域 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD12
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD12 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### 私用域 ログ確認 運用確認034 {#c38-i0300}
*分類: トレース診断*  ・  難易度: 中級

第三十四観点 私用域 は z/OS System Programming の トレース診断 で扱う管理項目です（第三十四観点）。第三十四観点 各アドレス空間内で利用者プログラムが使う独立した仮想記憶領域という説明を操作結果と照合します（第三十四観点）。第三十四観点 SRB=00AF1100、SWITCH SMF後のSMF切替記録、定義メンバーを照合し、共通ストレージ変更の記録を確認します（第三十四観点）。第三十四観点 証跡には資料IDと確認値を併記し、zOSSP記録034として保存します（第三十四観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第三十四証跡です。z/OS System Programming の トレース診断 で切分けを行います。確認観点は 私用域、ログ確認、運用確認 です。共通ストレージ変更の記録のために、SWITCH SMF後のSMF切替記録 を使った運用記録として最も適切な扱いはどれか。

    - A. SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を同一票へ記録し、私用域 を zOSSP正034で確定する。 ✅
    - B. APF管理 の一般メモを採り、SRB=00AF1100、メッセージID、時刻の対応を記録外に置き、zOSSP誤記034として調査範囲を狭める。
    - C. 私用域 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延034として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在034として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第三十四観点 正答根拠: Aは SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を結び付けるため、対象システムの取り違えを防げます（第三十四観点）。第三十四観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第三十四観点）。第三十四観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第三十四観点）。第三十四観点 用語説明: WTOは通知メッセージです（第三十四観点）。第三十四観点 WTORは応答を求めるメッセージです（第三十四観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **私用域 ログ確認 運用確認034**

    - 検証目的: 私用域 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により 私用域 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(PROGSP)
    → Enter を押す
    ```

    画面・出力:
    ```text
    APF FORMAT(DYNAMIC)
    APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
    LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
    ```

    画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により 私用域 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SET PROG=SP
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
    IEE536I PROG VALUE SP NOW IN EFFECT
    ```

    画面・出力には IEE252I が含まれる。IEE252I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により 私用域 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 06.10.10 PROG,APF DISPLAY 833
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
      12  MPRES3 MYPROG.LOADLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


