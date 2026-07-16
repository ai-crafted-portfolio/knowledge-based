---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (14/18)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > ページング

### lsps 復旧前確認 復旧手掛かり {#c01-i0690}
*分類: ページング*  ・  難易度: 中級

AIX 7.3 の ページング で扱う「lsps 復旧前確認 復旧手掛かり」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを復旧前確認の観点で確認する技術項目です。Paging Space 表とsys0 044を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsps 復旧前確認 復旧手掛かりの技術的な意味を資料で確認するとき、errpt 一覧確認 監査証跡との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はAIX エラーログから要約または詳細レポートを生成するコマンドである。
    - B. 構成を確認する際の意味はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 ✅
    - C. 構成を確認する際の意味はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。
    - D. 構成を確認する際の意味はJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は復旧前確認 復旧手掛かり（復旧・lsps）です。ページングの仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・復旧前です。一覧・監査・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は一覧確認 監査証跡（一覧・errp）です。容量・chdeのC:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。バック・chfsのD:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・chfs）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、復旧前確認 復旧手掛かりではls・復旧前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsps 復旧前確認 復旧手掛かり**

    - 検証目的: ページングのlsps 復旧前確認 復旧手掛かりについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsattr -E -l sys0 -a iostat
    → Enter を押す
    ```

    画面・出力:
    ```text
    iostat true Continuously maintain disk I/O history True
    ```

    画面・出力には iostat が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> chdev -l sys0 -a iostat=true
    → Enter を押す
    ```

    画面・出力:
    ```text
    sys0 changed
    ```

    画面・出力には sys0 が含まれ、lsps 復旧前確認 復旧手掛かりの証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lscfg -l sysplanar0
    → Enter を押す
    ```

    画面・出力:
    ```text
    DEVICE          LOCATION     DESCRIPTION
    sysplanar0      00-00        CPU Planar
    ```

    画面・出力には DEVICE が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の iostat が画面・出力に表示されること
    ② ステップ2 の sys0 が画面・出力に表示されること
    ③ ステップ3 の DEVICE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lsvg 一覧確認 詳細表示 {#c01-i0691}
*分類: ページング*  ・  難易度: 中級

AIX 7.3 の ページング で扱う「lsvg 一覧確認 詳細表示」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを一覧確認の観点で確認する技術項目です。Paging Space 表とsys0 052を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsvg 一覧確認 詳細表示の技術的な意味を資料で確認するとき、lslv 詳細確認 構成照合との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - B. コマンドまたは機能の用途は性能管理でvmstat 2 2を用い・Busy% とvmstat表示を確認する。
    - C. コマンドまたは機能の用途はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。
    - D. コマンドまたは機能の用途はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は一覧確認 詳細表示（一覧・lsvg）です。ページングの仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・一覧・詳細です。詳細・構成・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は詳細確認 構成照合（詳細・lslv）です。障害切・vmstのB:は「性能管理でvmstat 2 2を用い、Busy%」を述べ、対象は障害切り分け Busy%（障害・vmst）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、一覧確認 詳細表示ではls・一覧・詳細に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsvg 一覧確認 詳細表示**

    - 検証目的: ページングのlsvg 一覧確認 詳細表示について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lslv hd4
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOGICAL VOLUME: hd4
    VOLUME GROUP: rootvg
    LV STATE: opened/syncd
    TYPE: jfs2
    ```

    画面・出力には LOGICAL が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsps -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
    hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
    ```

    画面・出力には Page が含まれ、lsvg 一覧確認 詳細表示の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> smit lsps
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMIT fast path: lsps
    Command to run: lsps -a
    Paging space list displayed
    ```

    画面・出力には SMIT が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
    ② ステップ2 の Page が画面・出力に表示されること
    ③ ステップ3 の SMIT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lsvg 障害切り分け 設定値 {#c01-i0692}
*分類: ページング*  ・  難易度: 初級

AIX 7.3 の ページング で扱う「lsvg 障害切り分け 設定値」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを障害切り分けの観点で確認する技術項目です。Paging Space 表とsys0 012を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsvg 障害切り分け 設定値の技術的な意味を資料で確認するとき、lslv 性能確認 起動確認との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - B. 管理対象との関係を表す説明はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。
    - C. 管理対象との関係を表す説明はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 ✅
    - D. 管理対象との関係を表す説明はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は障害切り分け 設定値（障害・lsvg）です。ページングの仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・障害切です。性能・起動・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は性能確認 起動確認（性能・lslv）です。属性・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Subsystem（属性・tail）です。性能・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（性能・chvg）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、障害切り分け 設定値ではls・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsvg 障害切り分け 設定値**

    - 検証目的: ページングのlsvg 障害切り分け 設定値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lslv hd4
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOGICAL VOLUME: hd4
    VOLUME GROUP: rootvg
    LV STATE: opened/syncd
    TYPE: jfs2
    ```

    画面・出力には LOGICAL が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsps -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
    hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
    ```

    画面・出力には Page が含まれ、lsvg 障害切り分け 設定値の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> smit lsps
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMIT fast path: lsps
    Command to run: lsps -a
    Paging space list displayed
    ```

    画面・出力には SMIT が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
    ② ステップ2 の Page が画面・出力に表示されること
    ③ ステップ3 の SMIT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en




## AIX 7.3 > 導入と起動

### alt_disk_copy 変更前確認 EFIX LABEL 0133 {#c01-i0693}
*分類: 導入と起動*  ・  難易度: 初級

月影採取ではAIX 7.3の導入と起動で alt_disk_copy を確認します。月影採取の導入と起動では EFIX LABEL と起動デバイス設定を採取票へ記録します。月影採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。月影採取の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、月影採取を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 変更前確認 EFIX LABEL 0133を保守記録に説明する必要があります。netstat -v 変更後確認 MTU 0134と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。
    - B. 保守作業で参照する機能はデバイス管理でchdev -l hdisk0を用い・location code とODM属性を確認する。
    - C. 保守作業で参照する機能は導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。 ✅
    - D. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でalt_disk_copyを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、EFIX LABEL」で、確認対象はal・変更前です。変更後・netsのA:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。起動・chdeのB:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（起動・chde）です。容量・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を指し、EFIX LABELではal・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 変更前確認 EFIX LABEL 0133**

    - 検証目的: 導入と起動のalt_disk_copy 変更前確認 EFIX LABEL 0133について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認013-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0133A
    ```

    画面・出力には AIX0133A が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0133 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0133B
    ```

    画面・出力には AIX0133B が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0133 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0133C
    ```

    画面・出力には AIX0133C が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0133 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0133A が画面・出力に表示されること
    ② ステップ2 の AIX0133B が画面・出力に表示されること
    ③ ステップ3 の AIX0133C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 変更前確認 EFIX LABEL 0193 {#c01-i0694}
*分類: 導入と起動*  ・  難易度: 中級

朝霧判定ではAIX 7.3の導入と起動で alt_disk_copy を確認します。朝霧判定の導入と起動では EFIX LABEL と起動デバイス設定を採取票へ記録します。朝霧判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。朝霧判定の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、朝霧判定を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「alt_disk_copy 変更前確認 EFIX LABEL 0193」を「netstat -v 変更後確認 MTU 0194」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。 ✅
    - B. 保守作業で参照する機能はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。
    - C. 保守作業で参照する機能はデバイス管理でcfgmgrを用い・attribute とODM属性を確認する。
    - D. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。chdev -l en0 -a mtu=1500 容量確認 Media固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でalt_disk_copyを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、EFIX LABEL」で、確認対象はal・変更前です。変更後・netsのB:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。属性・cfgmのC:は「デバイス管理でcfgmgrを用い、attribute」を述べ、対象は属性確認 attribute（属性・cfgm）です。容量・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を指し、EFIX LABELではal・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 変更前確認 EFIX LABEL 0193**

    - 検証目的: 導入と起動のalt_disk_copy 変更前確認 EFIX LABEL 0193について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認073-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0193A
    ```

    画面・出力には AIX0193A が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0193 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0193B
    ```

    画面・出力には AIX0193B が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0193 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0193C
    ```

    画面・出力には AIX0193C が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0193 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0193A が画面・出力に表示されること
    ② ステップ2 の AIX0193B が画面・出力に表示されること
    ③ ステップ3 の AIX0193C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 変更前確認 altinst_rootvg 0609 {#c01-i0695}
*分類: 導入と起動*  ・  難易度: 初級

銀砂採取ではAIX 7.3の導入と起動で alt_disk_copy を確認します。銀砂採取の導入と起動では altinst_rootvg と起動デバイス設定を判定票へ残します。銀砂採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。銀砂採取の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、銀砂採取を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「alt_disk_copy 変更前確認 altinst_rootvg 0609」を「netstat -v 変更後確認 Gateway 0610」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。netstat -v 変更後確認 Gateway 0610固有の属性も確認対象に含める。
    - B. 運用時に利用する技術的役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。
    - C. 運用時に利用する技術的役割は導入と起動でalt_disk_copyを用い・altinst_rootvg と起動デバイス設定を確認する。 ✅
    - D. 運用時に利用する技術的役割はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でalt_disk_copyを用い、altinst_rootvg」に対応する項目は変更前確認 altinst_root（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い」で、確認対象はal・変更前です。変更後・netsのA:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。詳細・表形・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は詳細確認 表形式（詳細・errp）です。障害切・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（障害・lsse）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い」を指し、変更前確認 altinst_rootではal・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 変更前確認 altinst_rootvg 0609**

    - 検証目的: 導入と起動のalt_disk_copy 変更前確認 altinst_rootvg 0609について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認009-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0609A
    ```

    画面・出力には AIX0609A が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0609 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0609B
    ```

    画面・出力には AIX0609B が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0609 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0609C
    ```

    画面・出力には AIX0609C が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0609 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0609A が画面・出力に表示されること
    ② ステップ2 の AIX0609B が画面・出力に表示されること
    ③ ステップ3 の AIX0609C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 変更前確認 altinst_rootvg 0669 {#c01-i0696}
*分類: 導入と起動*  ・  難易度: 中級

梅雨晴判定ではAIX 7.3の導入と起動で alt_disk_copy を確認します。梅雨晴判定の導入と起動では altinst_rootvg と起動デバイス設定を判定票へ残します。梅雨晴判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。梅雨晴判定の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、梅雨晴判定を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 変更前確認 altinst_rootvg 0669を保守記録に説明する必要があります。netstat -v 変更後確認 Gateway 0670と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は導入と起動でalt_disk_copyを用い・altinst_rootvg と起動デバイス設定を確認する。 ✅
    - B. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。netstat -v 変更後確認 Gateway 0670固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割はJFS2でdf -gを用い・lff と内部スナップショットを確認する。
    - D. 運用時に利用する技術的役割はセキュリティでsetsecattrを用い・user attributes とRBAC属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でalt_disk_copyを用い、altinst_rootvg」に対応する項目は変更前確認 altinst_root（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い」で、確認対象はal・変更前です。変更後・netsのB:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。運用引・dfのC:は「JFS2でdf -gを用い、lff と内部スナップショットを確認する」を述べ、対象は運用引継ぎ lff（運用・df）です。バック・setsのD:は「セキュリティでsetsecattrを用い、user」を述べ、対象はuser attributes（バッ・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い」を指し、変更前確認 altinst_rootではal・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 変更前確認 altinst_rootvg 0669**

    - 検証目的: 導入と起動のalt_disk_copy 変更前確認 altinst_rootvg 0669について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認069-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0669A
    ```

    画面・出力には AIX0669A が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0669 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0669B
    ```

    画面・出力には AIX0669B が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0669 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0669C
    ```

    画面・出力には AIX0669C が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0669 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0669A が画面・出力に表示されること
    ② ステップ2 の AIX0669B が画面・出力に表示されること
    ③ ステップ3 の AIX0669C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 容量確認 fileset level 0639 {#c01-i0697}
*分類: 導入と起動*  ・  難易度: 中級

秋桜採取ではAIX 7.3の導入と起動で alt_disk_copy を確認します。秋桜採取の導入と起動では fileset level とfileset一覧を作業票へ保管します。秋桜採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋桜採取の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、秋桜採取を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 容量確認 fileset level 0639の設定や表示を読む前に役割を確認します。netstat -v 性能確認 Media Speed Running 0640ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。netstat -v 性能確認 Media Speed Running固有の属性も確認対象に含める。
    - B. 状態を読み取るための働きはJFS2でdf -gを用い・agblksize とマウントオプションを確認する。
    - C. 状態を読み取るための働きは導入と起動でalt_disk_copyを用い・fileset level とfileset一覧を確認する。 ✅
    - D. 状態を読み取るための働きはセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でalt_disk_copyを用い、fileset level」に対応する項目はfileset level（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、fileset」で、確認対象はal・容量です。性能・netsのA:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。構成・dfのB:は「JFS2でdf -gを用い、agblksize」を述べ、対象は構成照合 agblksize（構成・df）です。起動・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（起動・lsse）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、fileset」を指し、fileset levelではal・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 容量確認 fileset level 0639**

    - 検証目的: 導入と起動のalt_disk_copy 容量確認 fileset level 0639について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認039-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0639A
    ```

    画面・出力には AIX0639A が表示され、alt_disk_copy 容量確認 fileset level 0639 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0639B
    ```

    画面・出力には AIX0639B が表示され、alt_disk_copy 容量確認 fileset level 0639 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0639C
    ```

    画面・出力には AIX0639C が表示され、alt_disk_copy 容量確認 fileset level 0639 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0639A が画面・出力に表示されること
    ② ステップ2 の AIX0639B が画面・出力に表示されること
    ③ ステップ3 の AIX0639C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 容量確認 fileset level 0699 {#c01-i0698}
*分類: 導入と起動*  ・  難易度: 中級

山吹保守ではAIX 7.3の導入と起動で alt_disk_copy を確認します。山吹保守の導入と起動では fileset level とfileset一覧を作業票へ保管します。山吹保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。山吹保守の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、山吹保守を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 容量確認 fileset level 0699について構成や状態を確認します。netstat -v 性能確認 Media Speed Running 0700ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。netstat -v 性能確認 Media Speed Running固有の属性も確認対象に含める。
    - B. 状態を読み取るための働きはLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。
    - C. 状態を読み取るための働きはセキュリティでsetsecattrを用い・user attributes とユーザー属性を確認する。
    - D. 状態を読み取るための働きは導入と起動でalt_disk_copyを用い・fileset level とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でalt_disk_copyを用い、fileset level」に対応する項目はfileset level（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、fileset」で、確認対象はal・容量です。性能・netsのA:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。構成・chlvのB:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（構成・chlv）です。属性・setsのC:は「セキュリティでsetsecattrを用い、user」を述べ、対象はuser attributes（属性・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、fileset」を指し、fileset levelではal・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 容量確認 fileset level 0699**

    - 検証目的: 導入と起動のalt_disk_copy 容量確認 fileset level 0699について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認099-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0699A
    ```

    画面・出力には AIX0699A が表示され、alt_disk_copy 容量確認 fileset level 0699 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0699B
    ```

    画面・出力には AIX0699B が表示され、alt_disk_copy 容量確認 fileset level 0699 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0699C
    ```

    画面・出力には AIX0699C が表示され、alt_disk_copy 容量確認 fileset level 0699 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0699A が画面・出力に表示されること
    ② ステップ2 の AIX0699B が画面・出力に表示されること
    ③ ステップ3 の AIX0699C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 容量確認 mksysb image 0163 {#c01-i0699}
*分類: 導入と起動*  ・  難易度: 中級

秋声判定ではAIX 7.3の導入と起動で alt_disk_copy を確認します。秋声判定の導入と起動では mksysb image とfileset一覧を点検票へ整理します。秋声判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋声判定の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、秋声判定を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 容量確認 mksysb image 0163について構成や状態を確認します。netstat -v 性能確認 EtherChannel 0164ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。 ✅
    - B. 対象資源に対する働きはネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。
    - C. 対象資源に対する働きはデバイス管理でchdev -l hdisk0を用い・path status と診断対象表示を確認する。chdev -l hdisk0 障害切り分け path status固有の属性も確認対象に含める。
    - D. 対象資源に対する働きはネットワークでchdev -l en0 -aを用い・Gateway と経路表を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でalt_disk_copyを用い、mksysb image」に対応する項目はmksysb image（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、mksysb」で、確認対象はal・容量です。性能・netsのB:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は性能確認 EtherChannel（性能・nets）です。障害切・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、path」を述べ、対象はpath status（障害・chde）です。変更前・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、mksysb」を指し、mksysb imageではal・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 容量確認 mksysb image 0163**

    - 検証目的: 導入と起動のalt_disk_copy 容量確認 mksysb image 0163について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認043-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0163A
    ```

    画面・出力には AIX0163A が表示され、alt_disk_copy 容量確認 mksysb image 0163 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0163B
    ```

    画面・出力には AIX0163B が表示され、alt_disk_copy 容量確認 mksysb image 0163 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0163C
    ```

    画面・出力には AIX0163C が表示され、alt_disk_copy 容量確認 mksysb image 0163 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0163A が画面・出力に表示されること
    ② ステップ2 の AIX0163B が画面・出力に表示されること
    ③ ステップ3 の AIX0163C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 容量確認 mksysb image 0223 {#c01-i0700}
*分類: 導入と起動*  ・  難易度: 上級

新緑保守ではAIX 7.3の導入と起動で alt_disk_copy を確認します。新緑保守の導入と起動では mksysb image とfileset一覧を点検票へ整理します。新緑保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。新緑保守の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、新緑保守を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 容量確認 mksysb image 0223の設定や表示を読む前に役割を確認します。netstat -v 性能確認 EtherChannel 0224ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。 ✅
    - B. 対象資源に対する働きはネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。
    - C. 対象資源に対する働きはデバイス管理でcfgmgrを用い・microcode level と診断対象表示を確認する。
    - D. 対象資源に対する働きはネットワークでchdev -l en0 -aを用い・Gateway と経路表を確認する。chdev -l en0 -a mtu=1500 変更前確認固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「導入と起動でalt_disk_copyを用い、mksysb image」に対応する項目はmksysb image（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、mksysb」で、確認対象はal・容量です。性能・netsのB:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は性能確認 EtherChannel（性能・nets）です。バック・cfgmのC:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（バッ・cfgm）です。変更前・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、mksysb」を指し、mksysb imageではal・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 容量確認 mksysb image 0223**

    - 検証目的: 導入と起動のalt_disk_copy 容量確認 mksysb image 0223について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認103-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0223A
    ```

    画面・出力には AIX0223A が表示され、alt_disk_copy 容量確認 mksysb image 0223 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0223B
    ```

    画面・出力には AIX0223B が表示され、alt_disk_copy 容量確認 mksysb image 0223 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0223C
    ```

    画面・出力には AIX0223C が表示され、alt_disk_copy 容量確認 mksysb image 0223 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0223A が画面・出力に表示されること
    ② ステップ2 の AIX0223B が画面・出力に表示されること
    ③ ステップ3 の AIX0223C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 状態確認 bootlist 0798 {#c01-i0701}
*分類: 導入と起動*  ・  難易度: 中級

春霞復旧ではAIX 7.3の導入と起動で alt_disk_copy を確認します。春霞復旧の導入と起動では bootlist とOSレベル表示を変更票へ記録します。春霞復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春霞復旧の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、春霞復旧を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 状態確認 bootlist 0798に関する障害切り分けの前提を確認しています。lslv 変更前確認 運用記録の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては導入と起動でalt_disk_copyを用い・bootlist とOSレベル表示を確認する。 ✅
    - B. 機能の説明としては論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - C. 機能の説明としてはセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。
    - D. 機能の説明としては導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** 状態・alt_でAの記述「導入と起動でalt_disk_copyを用い、bootlist」に対応する項目は状態確認 bootlist（状態・alt_）です。状態に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、bootlist」で、確認対象はal・状態です。変更前・lslvのB:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は変更前確認 運用記録（変更・lslv）です。バック・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。変更後・bosbのD:は「導入と起動でbosboot -a -dを用い」を述べ、対象は変更後確認 altinst_root（変更・bosb）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、bootlist」を指し、状態確認 bootlistではal・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 状態確認 bootlist 0798**

    - 検証目的: 導入と起動のalt_disk_copy 状態確認 bootlist 0798について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認078-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0798A
    ```

    画面・出力には AIX0798A が表示され、alt_disk_copy 状態確認 bootlist 0798 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0798B
    ```

    画面・出力には AIX0798B が表示され、alt_disk_copy 状態確認 bootlist 0798 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0798C
    ```

    画面・出力には AIX0798C が表示され、alt_disk_copy 状態確認 bootlist 0798 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0798A が画面・出力に表示されること
    ② ステップ2 の AIX0798B が画面・出力に表示されること
    ③ ステップ3 の AIX0798C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 状態確認 fileset level 0322 {#c01-i0702}
*分類: 導入と起動*  ・  難易度: 中級

春分変更ではAIX 7.3の導入と起動で alt_disk_copy を確認します。春分変更の導入と起動では fileset level とOSレベル表示を保守票へ記録します。春分変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春分変更の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、春分変更を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 状態確認 fileset level 0322の役割を調べています。netstat -v 構成照合 MTU 0323の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はネットワークでnetstat -vを用い・MTU とEthernet統計を確認する。
    - B. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。
    - C. 表示や設定で扱う内容は導入と起動でalt_disk_copyを用い・fileset level とOSレベル表示を確認する。 ✅
    - D. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。setsecattr 変更後確認 audit class 0015固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でalt_disk_copyを用い、fileset level」に対応する項目はfileset level（状態・alt_）です。状態に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、fileset」で、確認対象はal・状態です。構成・netsのA:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は構成照合 MTU（構成・nets）です。性能・cfgmのB:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。変更後・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、fileset」を指し、fileset levelではal・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 状態確認 fileset level 0322**

    - 検証目的: 導入と起動のalt_disk_copy 状態確認 fileset level 0322について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認082-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0322A
    ```

    画面・出力には AIX0322A が表示され、alt_disk_copy 状態確認 fileset level 0322 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0322B
    ```

    画面・出力には AIX0322B が表示され、alt_disk_copy 状態確認 fileset level 0322 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0322C
    ```

    画面・出力には AIX0322C が表示され、alt_disk_copy 状態確認 fileset level 0322 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0322A が画面・出力に表示されること
    ② ステップ2 の AIX0322B が画面・出力に表示されること
    ③ ステップ3 の AIX0322C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 監査記録 Technology Level 0828 {#c01-i0703}
*分類: 導入と起動*  ・  難易度: 上級

雪解変更ではAIX 7.3の導入と起動で alt_disk_copy を確認します。雪解変更の導入と起動では Technology Level と代替ディスク状態を同じ証跡に残します。雪解変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。雪解変更の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、雪解変更を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 監査記録 Technology Level 0828の技術的な意味を資料で確認するとき、alt_disk_copy 障害切り分け EFIX LABEL 0004との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。
    - B. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。pwdck -n ALL 監査記録 enhanced_RBAC 0256固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。
    - D. 構成を確認する際の意味は導入と起動でalt_disk_copyを用い・Technology Level と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 監査・alt_でDの記述「導入と起動でalt_disk_copyを用い、Technology」に対応する項目はTechnology Level（監査・alt_）です。監査に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、Technology」で、確認対象はal・監査です。障害切・alt_のA:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（障害・alt_）です。監査・pwdcのB:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・pwdc）です。障害切・syslのC:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、Technology」を指し、Technology Levelではal・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 監査記録 Technology Level 0828**

    - 検証目的: 導入と起動のalt_disk_copy 監査記録 Technology Level 0828について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録108-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0828A
    ```

    画面・出力には AIX0828A が表示され、alt_disk_copy 監査記録 Technology Level 0828 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0828B
    ```

    画面・出力には AIX0828B が表示され、alt_disk_copy 監査記録 Technology Level 0828 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0828C
    ```

    画面・出力には AIX0828C が表示され、alt_disk_copy 監査記録 Technology Level 0828 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0828A が画面・出力に表示されること
    ② ステップ2 の AIX0828B が画面・出力に表示されること
    ③ ステップ3 の AIX0828C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 監査記録 altinst_rootvg 0352 {#c01-i0704}
*分類: 導入と起動*  ・  難易度: 上級

夕映変更ではAIX 7.3の導入と起動で alt_disk_copy を確認します。夕映変更の導入と起動では altinst_rootvg と代替ディスク状態を監査票へ転記します。夕映変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。夕映変更の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、夕映変更を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 監査記録 altinst_rootvg 0352を同一分類のnetstat -v 運用引継ぎ EtherChannel 0353と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。
    - B. 管理対象との関係を表す説明は導入と起動でalt_disk_copyを用い・altinst_rootvg と代替ディスク状態を確認する。 ✅
    - C. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。cfgmgr 変更後確認 path status 0658固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「導入と起動でalt_disk_copyを用い、altinst_rootvg」に対応する項目は監査記録 altinst_rootv（監査・alt_）です。監査に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い」で、確認対象はal・監査です。運用引・netsのA:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は運用引継ぎ EtherChannel（運用・nets）です。変更後・cfgmのC:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。性能・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い」を指し、監査記録 altinst_rootvではal・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 監査記録 altinst_rootvg 0352**

    - 検証目的: 導入と起動のalt_disk_copy 監査記録 altinst_rootvg 0352について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録112-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0352A
    ```

    画面・出力には AIX0352A が表示され、alt_disk_copy 監査記録 altinst_rootvg 0352 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0352B
    ```

    画面・出力には AIX0352B が表示され、alt_disk_copy 監査記録 altinst_rootvg 0352 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0352C
    ```

    画面・出力には AIX0352C が表示され、alt_disk_copy 監査記録 altinst_rootvg 0352 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0352A が画面・出力に表示されること
    ② ステップ2 の AIX0352B が画面・出力に表示されること
    ③ ステップ3 の AIX0352C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_copy 障害切り分け EFIX LABEL 0004 {#c01-i0705}
*分類: 導入と起動*  ・  難易度: 初級

若草確認ではAIX 7.3の導入と起動で alt_disk_copy を確認します。若草確認の導入と起動では EFIX LABEL と代替ディスク状態を監査票へ転記します。若草確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若草確認の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若草確認を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_copy 障害切り分け EFIX LABEL 0004の技術的な意味を資料で確認するとき、netstat -v バックアウト確認 Destination 0005との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・Destination とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。
    - C. 管理対象との関係を表す説明は導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。 ✅
    - D. 管理対象との関係を表す説明はネットワークでchdev -l en0 -aを用い・MTU とMTU属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でalt_disk_copyを用い、EFIX LABEL」に対応する項目はEFIX LABEL（障害・alt_）です。導入と起動の仕様は「導入と起動でalt_disk_copyを用い、EFIX LABEL」で、確認対象はal・障害切です。バック・netsのA:は「ネットワークでnetstat -vを用い、Destination」を述べ、対象はバックアウト確認 Destinati（バッ・nets）です。状態・chdeのB:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（状態・chde）です。起動・chdeのD:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は起動確認 MTU（起動・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を指し、EFIX LABELではal・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_copy 障害切り分け EFIX LABEL 0004**

    - 検証目的: 導入と起動のalt_disk_copy 障害切り分け EFIX LABEL 0004について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け004-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_copy
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0004A
    ```

    画面・出力には AIX0004A が表示され、alt_disk_copy 障害切り分け EFIX LABEL 0004 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0004B
    ```

    画面・出力には AIX0004B が表示され、alt_disk_copy 障害切り分け EFIX LABEL 0004 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0004C
    ```

    画面・出力には AIX0004C が表示され、alt_disk_copy 障害切り分け EFIX LABEL 0004 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0004A が画面・出力に表示されること
    ② ステップ2 の AIX0004B が画面・出力に表示されること
    ③ ステップ3 の AIX0004C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_mksysb バックアウト確認 bootlist 0065 {#c01-i0706}
*分類: 導入と起動*  ・  難易度: 中級

花冷照合ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。花冷照合の導入と起動では bootlist と起動デバイス設定を復旧票へ残します。花冷照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。花冷照合の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、花冷照合を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「alt_disk_mksysb バックアウト確認 bootlist 0065」を「smitty etherchannel 監査記録 Destination 0066」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はネットワークでsmitty etherchannelを用い・Destinationである。
    - B. 仕様上の役割は導入と起動でalt_disk_mksysbを用い・bootlist と起動デバイス設定を確認する。 ✅
    - C. 仕様上の役割はデバイス管理でodmget CuDvを用い・PVID とODM属性を確認する。odmget CuDv 変更前確認 PVID 0371固有の属性も確認対象に含める。
    - D. 仕様上の役割はネットワークでentstat -d ent0を用い・MTU とアダプター一覧を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でalt_disk_mksysbを用い、bootlist」に対応する項目はバックアウト確認 bootlist（バッ・alt_）です。導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、bootlist」で、確認対象はal・バックです。監査・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 Destination（監査・smit）です。変更前・odmgのC:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は変更前確認 PVID（変更・odmg）です。属性・entsのD:は「ネットワークでentstat -d ent0を用い、MTU」を述べ、対象は属性確認 MTU（属性・ents）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、bootlist」を指し、バックアウト確認 bootlistではal・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_mksysb バックアウト確認 bootlist 0065**

    - 検証目的: 導入と起動のalt_disk_mksysb バックアウト確認 bootlist 0065について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認065-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0065A
    ```

    画面・出力には AIX0065A が表示され、alt_disk_mksysb バックアウト確認 bootlist 0065 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0065B
    ```

    画面・出力には AIX0065B が表示され、alt_disk_mksysb バックアウト確認 bootlist 0065 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0065C
    ```

    画面・出力には AIX0065C が表示され、alt_disk_mksysb バックアウト確認 bootlist 0065 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0065A が画面・出力に表示されること
    ② ステップ2 の AIX0065B が画面・出力に表示されること
    ③ ステップ3 の AIX0065C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_mksysb バックアウト確認 mksysb image 0541 {#c01-i0707}
*分類: 導入と起動*  ・  難易度: 中級

群青照合ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。群青照合の導入と起動では mksysb image と起動デバイス設定を採取票へ記録します。群青照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。群青照合の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、群青照合を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_mksysb バックアウト確認 mksysb image 0541を保守記録に説明する必要があります。smitty etherchannel 監査記録 EtherChannel 0542と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はネットワークでsmitty etherchannelを用い・EtherChannelである。
    - B. 保守作業で参照する機能は導入と起動でalt_disk_mksysbを用い・mksysb image と起動デバイス設定を確認する。 ✅
    - C. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。
    - D. 保守作業で参照する機能はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。setsecattr 運用引継ぎ audit class 0234固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でalt_disk_mksysbを用い、mksysb image」に対応する項目はmksysb image（バッ・alt_）です。バックに関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、mksysb」で、確認対象はal・バックです。監査・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 EtherChannel（監査・smit）です。変更前・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は変更前確認 識別値（変更・chde）です。運用引・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、mksysb」を指し、mksysb imageではal・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_mksysb バックアウト確認 mksysb image 0541**

    - 検証目的: 導入と起動のalt_disk_mksysb バックアウト確認 mksysb image 0541について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認061-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0541A
    ```

    画面・出力には AIX0541A が表示され、alt_disk_mksysb バックアウト確認 mksysb image 0541 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0541B
    ```

    画面・出力には AIX0541B が表示され、alt_disk_mksysb バックアウト確認 mksysb image 0541 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0541C
    ```

    画面・出力には AIX0541C が表示され、alt_disk_mksysb バックアウト確認 mksysb image 0541 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0541A が画面・出力に表示されること
    ② ステップ2 の AIX0541B が画面・出力に表示されること
    ③ ステップ3 の AIX0541C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_mksysb 属性確認 EFIX LABEL 0571 {#c01-i0708}
*分類: 導入と起動*  ・  難易度: 中級

松風点検ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。松風点検の導入と起動では EFIX LABEL とfileset一覧を点検票へ整理します。松風点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。松風点検の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、松風点検を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_mksysb 属性確認 EFIX LABEL 0571について構成や状態を確認します。smitty etherchannel 状態確認 MTU 0572ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはネットワークでsmitty etherchannelを用い・MTU と経路表を確認する。
    - B. 対象資源に対する働きは導入と起動でalt_disk_mksysbを用い・EFIX LABEL とfileset一覧を確認する。 ✅
    - C. 対象資源に対する働きはデバイス属性を変更する管理コマンドである。
    - D. 対象資源に対する働きはセキュリティでchuserを用い・user attributes とユーザー属性を確認する。chuser 変更前確認 user attributes 0264固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でalt_disk_mksysbを用い、EFIX LABEL」に対応する項目はEFIX LABEL（属性・alt_）です。属性に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、EFIX」で、確認対象はal・属性です。状態・smitのA:は「ネットワークでsmitty etherchannelを用い、MTU」を述べ、対象は状態確認 MTU（状態・smit）です。復旧前・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は復旧前確認 仮想化表示（復旧・chde）です。変更前・chusのD:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、EFIX」を指し、EFIX LABELではal・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_mksysb 属性確認 EFIX LABEL 0571**

    - 検証目的: 導入と起動のalt_disk_mksysb 属性確認 EFIX LABEL 0571について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認091-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0571A
    ```

    画面・出力には AIX0571A が表示され、alt_disk_mksysb 属性確認 EFIX LABEL 0571 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0571B
    ```

    画面・出力には AIX0571B が表示され、alt_disk_mksysb 属性確認 EFIX LABEL 0571 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0571C
    ```

    画面・出力には AIX0571C が表示され、alt_disk_mksysb 属性確認 EFIX LABEL 0571 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0571A が画面・出力に表示されること
    ② ステップ2 の AIX0571B が画面・出力に表示されること
    ③ ステップ3 の AIX0571C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_mksysb 属性確認 Technology Level 0095 {#c01-i0709}
*分類: 導入と起動*  ・  難易度: 中級

岩清水点検ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。岩清水点検の導入と起動では Technology Level とfileset一覧を照合票へ整理します。岩清水点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。岩清水点検の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、岩清水点検を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_mksysb 属性確認 Technology Level 0095の設定や表示を読む前に役割を確認します。smitty etherchannel 状態確認 Link Status 0096ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はネットワークでsmitty etherchannelを用い・Link Status と経路表を確認する。
    - B. 一次資料が示す主目的はデバイス管理でodmget CuDvを用い・Available と診断対象表示を確認する。
    - C. 一次資料が示す主目的はネットワークでentstat -d ent0を用い・EtherChannel と経路表を確認する。
    - D. 一次資料が示す主目的は導入と起動でalt_disk_mksysbを用い・Technology Levelである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でalt_disk_mksysbを用い、Technology」に対応する項目はTechnology Level（属性・alt_）です。属性に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い」で、確認対象はal・属性です。状態・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（状態・smit）です。容量・odmgのB:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は容量確認 Available（容量・odmg）です。バック・entsのC:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 EtherChan（バッ・ents）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い」を指し、Technology Levelではal・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_mksysb 属性確認 Technology Level 0095**

    - 検証目的: 導入と起動のalt_disk_mksysb 属性確認 Technology Level 0095について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認095-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0095A
    ```

    画面・出力には AIX0095A が表示され、alt_disk_mksysb 属性確認 Technology Level 0095 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0095B
    ```

    画面・出力には AIX0095B が表示され、alt_disk_mksysb 属性確認 Technology Level 0095 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0095C
    ```

    画面・出力には AIX0095C が表示され、alt_disk_mksysb 属性確認 Technology Level 0095 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0095A が画面・出力に表示されること
    ② ステップ2 の AIX0095B が画面・出力に表示されること
    ③ ステップ3 の AIX0095C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_mksysb 構成照合 EFIX LABEL 0382 {#c01-i0710}
*分類: 導入と起動*  ・  難易度: 初級

紅葉記録ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。紅葉記録の導入と起動では EFIX LABEL とOSレベル表示を保守票へ記録します。紅葉記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。紅葉記録の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、紅葉記録を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_mksysb 構成照合 EFIX LABEL 0382に関する障害切り分けの前提を確認しています。smitty etherchannel 変更前確認 Destination 0383の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はネットワークでsmitty etherchannelを用い・Destinationである。smitty etherchannel 変更前確認固有の属性も確認対象に含める。
    - B. 表示や設定で扱う内容は導入と起動でalt_disk_mksysbを用い・EFIX LABEL とOSレベル表示を確認する。 ✅
    - C. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。
    - D. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「導入と起動でalt_disk_mksysbを用い、EFIX LABEL」に対応する項目はEFIX LABEL（構成・alt_）です。構成に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、EFIX」で、確認対象はal・構成です。変更前・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は変更前確認 Destination（変更・smit）です。性能・cfgmのC:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。変更後・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、EFIX」を指し、EFIX LABELではal・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_mksysb 構成照合 EFIX LABEL 0382**

    - 検証目的: 導入と起動のalt_disk_mksysb 構成照合 EFIX LABEL 0382について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合022-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0382A
    ```

    画面・出力には AIX0382A が表示され、alt_disk_mksysb 構成照合 EFIX LABEL 0382 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0382B
    ```

    画面・出力には AIX0382B が表示され、alt_disk_mksysb 構成照合 EFIX LABEL 0382 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0382C
    ```

    画面・出力には AIX0382C が表示され、alt_disk_mksysb 構成照合 EFIX LABEL 0382 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0382A が画面・出力に表示されること
    ② ステップ2 の AIX0382B が画面・出力に表示されること
    ③ ステップ3 の AIX0382C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### alt_disk_mksysb 運用引継ぎ mksysb image 0412 {#c01-i0711}
*分類: 導入と起動*  ・  難易度: 中級

水音評価ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。水音評価の導入と起動では mksysb image と代替ディスク状態を監査票へ転記します。水音評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。水音評価の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、水音評価を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** alt_disk_mksysb 運用引継ぎ mksysb image 0412の技術的な意味を資料で確認するとき、smitty etherchannel 容量確認 Link Status 0413との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでsmitty etherchannelを用い・Link Status とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。
    - C. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。
    - D. 管理対象との関係を表す説明は導入と起動でalt_disk_mksysbを用い・mksysb image と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でalt_disk_mksysbを用い、mksysb image」に対応する項目はmksysb image（運用・alt_）です。運用引に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、mksysb」で、確認対象はal・運用引です。容量・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（容量・smit）です。変更後・cfgmのB:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。性能・setsのC:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、mksysb」を指し、mksysb imageではal・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **alt_disk_mksysb 運用引継ぎ mksysb image 0412**

    - 検証目的: 導入と起動のalt_disk_mksysb 運用引継ぎ mksysb image 0412について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ052-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> alt_disk_mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0412A
    ```

    画面・出力には AIX0412A が表示され、alt_disk_mksysb 運用引継ぎ mksysb image 0412 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0412B
    ```

    画面・出力には AIX0412B が表示され、alt_disk_mksysb 運用引継ぎ mksysb image 0412 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0412C
    ```

    画面・出力には AIX0412C が表示され、alt_disk_mksysb 運用引継ぎ mksysb image 0412 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0412A が画面・出力に表示されること
    ② ステップ2 の AIX0412B が画面・出力に表示されること
    ③ ステップ3 の AIX0412C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 変更前確認 EFIX LABEL 0276 {#c01-i0712}
*分類: 導入と起動*  ・  難易度: 中級

若潮監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。若潮監査の導入と起動では EFIX LABEL と代替ディスク状態を同じ証跡に残します。若潮監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若潮監査の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、若潮監査を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 変更前確認 EFIX LABEL 0276の技術的な意味を資料で確認するとき、cfgmgr 変更後確認 Destination 0277との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はネットワークでcfgmgrを用い・Destination とMTU属性を確認する。cfgmgr 変更後確認 Destination 0277固有の属性も確認対象に含める。
    - B. 構成を確認する際の意味はデバイス管理でdiag -d ent0を用い・location code とデバイス一覧を確認する。
    - C. 構成を確認する際の意味はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - D. 構成を確認する際の意味は導入と起動でbootlist -m normalを用い・EFIX LABEL と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でbootlist -m normalを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・boot）です。変更前に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い、EFIX」で、確認対象はbo・変更前です。変更後・cfgmのA:は「ネットワークでcfgmgrを用い、Destination」を述べ、対象は変更後確認 Destination（変更・cfgm）です。起動・diagのB:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（起動・diag）です。障害切・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は障害切り分け 統計値（障害・vmst）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い、EFIX」を指し、EFIX LABELではbo・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 変更前確認 EFIX LABEL 0276**

    - 検証目的: 導入と起動のbootlist -m normal 変更前確認 EFIX LABEL 0276について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認036-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0276A
    ```

    画面・出力には AIX0276A が表示され、bootlist -m normal 変更前確認 EFIX LABEL 0276 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0276B
    ```

    画面・出力には AIX0276B が表示され、bootlist -m normal 変更前確認 EFIX LABEL 0276 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0276C
    ```

    画面・出力には AIX0276C が表示され、bootlist -m normal 変更前確認 EFIX LABEL 0276 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0276A が画面・出力に表示されること
    ② ステップ2 の AIX0276B が画面・出力に表示されること
    ③ ステップ3 の AIX0276C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 変更前確認 altinst_rootvg 0752 {#c01-i0713}
*分類: 導入と起動*  ・  難易度: 中級

夕映監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。夕映監査の導入と起動では altinst_rootvg と代替ディスク状態を引継ぎ票へ保管します。夕映監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映監査の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、夕映監査を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 変更前確認 altinst_rootvg 0752を同一分類のcfgmgr 変更後確認 EtherChannel 0753と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は導入と起動でbootlist -m normalを用い・altinst_rootvgである。 ✅
    - B. コマンドまたは機能の用途はネットワークでcfgmgrを用い・EtherChannel とMTU属性を確認する。
    - C. コマンドまたは機能の用途はJFS2でdefragfsを用い・lff とファイルシステム属性を確認する。
    - D. コマンドまたは機能の用途はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でbootlist -m normalを用い」に対応する項目は変更前確認 altinst_root（変更・boot）です。変更前に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・変更前です。変更後・cfgmのB:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は変更後確認 EtherChannel（変更・cfgm）です。運用引・defrのC:は「JFS2でdefragfsを用い、lff」を述べ、対象は運用引継ぎ lff（運用・defr）です。障害切・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、変更前確認 altinst_rootではbo・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 変更前確認 altinst_rootvg 0752**

    - 検証目的: 導入と起動のbootlist -m normal 変更前確認 altinst_rootvg 0752について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認032-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0752A
    ```

    画面・出力には AIX0752A が表示され、bootlist -m normal 変更前確認 altinst_rootvg 0752 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0752B
    ```

    画面・出力には AIX0752B が表示され、bootlist -m normal 変更前確認 altinst_rootvg 0752 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0752C
    ```

    画面・出力には AIX0752C が表示され、bootlist -m normal 変更前確認 altinst_rootvg 0752 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0752A が画面・出力に表示されること
    ② ステップ2 の AIX0752B が画面・出力に表示されること
    ③ ステップ3 の AIX0752C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 容量確認 fileset level 0722 {#c01-i0714}
*分類: 導入と起動*  ・  難易度: 初級

春分監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。春分監査の導入と起動では fileset level とOSレベル表示を確認票へ整理します。春分監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春分監査の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、春分監査を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 容量確認 fileset level 0722の役割を調べています。cfgmgr 性能確認 MTU 0723の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。
    - B. 障害切り分けに用いる役割は導入と起動でbootlist -m normalを用い・fileset levelである。 ✅
    - C. 障害切り分けに用いる役割はJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。
    - D. 障害切り分けに用いる役割はセキュリティでpwdck -n ALLを用い・authorizations とロール一覧を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「導入と起動でbootlist -m normalを用い、fileset」に対応する項目はfileset level（容量・boot）です。容量に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・容量です。性能・cfgmのA:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。状態・logfのC:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は状態確認 log=INLINE（状態・logf）です。起動・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は起動確認 authorization（起動・pwdc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、fileset levelではbo・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 容量確認 fileset level 0722**

    - 検証目的: 導入と起動のbootlist -m normal 容量確認 fileset level 0722について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認002-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0722A
    ```

    画面・出力には AIX0722A が表示され、bootlist -m normal 容量確認 fileset level 0722 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0722B
    ```

    画面・出力には AIX0722B が表示され、bootlist -m normal 容量確認 fileset level 0722 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0722C
    ```

    画面・出力には AIX0722C が表示され、bootlist -m normal 容量確認 fileset level 0722 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0722A が画面・出力に表示されること
    ② ステップ2 の AIX0722B が画面・出力に表示されること
    ③ ステップ3 の AIX0722C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 容量確認 mksysb image 0246 {#c01-i0715}
*分類: 導入と起動*  ・  難易度: 初級

朝凪監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。朝凪監査の導入と起動では mksysb image とOSレベル表示を変更票へ記録します。朝凪監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。朝凪監査の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、朝凪監査を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 容量確認 mksysb image 0246に関する障害切り分けの前提を確認しています。cfgmgr 性能確認 Link Status 0247の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。cfgmgr 性能確認 Link Status 0247固有の属性も確認対象に含める。
    - B. 機能の説明としてはデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。
    - C. 機能の説明としてはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - D. 機能の説明としては導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「導入と起動でbootlist -m normalを用い、mksysb image」に対応する項目はmksysb image（容量・boot）です。容量に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・容量です。性能・cfgmのA:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（性能・cfgm）です。障害切・diagのB:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。属性・イベ・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は属性照合 イベント転送（属性・vmst）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、mksysb imageではbo・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 容量確認 mksysb image 0246**

    - 検証目的: 導入と起動のbootlist -m normal 容量確認 mksysb image 0246について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認006-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0246A
    ```

    画面・出力には AIX0246A が表示され、bootlist -m normal 容量確認 mksysb image 0246 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0246B
    ```

    画面・出力には AIX0246B が表示され、bootlist -m normal 容量確認 mksysb image 0246 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0246C
    ```

    画面・出力には AIX0246C が表示され、bootlist -m normal 容量確認 mksysb image 0246 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0246A が画面・出力に表示されること
    ② ステップ2 の AIX0246B が画面・出力に表示されること
    ③ ステップ3 の AIX0246C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 状態確認 EFIX LABEL 0405 {#c01-i0716}
*分類: 導入と起動*  ・  難易度: 中級

深雪評価ではAIX 7.3の導入と起動で bootlist -m normal を確認します。深雪評価の導入と起動では EFIX LABEL と起動デバイス設定を判定票へ残します。深雪評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪評価の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、深雪評価を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 状態確認 EFIX LABEL 0405を保守記録に説明する必要があります。cfgmgr 構成照合 MTU 0406と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。cfgmgr 構成照合 MTU 0406固有の属性も確認対象に含める。
    - B. 運用時に利用する技術的役割はデバイス管理でdiag -d ent0を用い・location code とODM属性を確認する。
    - C. 運用時に利用する技術的役割は導入と起動でbootlist -m normalを用い・EFIX LABEL と起動デバイス設定を確認する。 ✅
    - D. 運用時に利用する技術的役割はセキュリティでpwdck -n ALLを用い・user attributes とRBAC属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でbootlist -m normalを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・boot）です。状態に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い、EFIX」で、確認対象はbo・状態です。構成・cfgmのA:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。容量・diagのB:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（容量・diag）です。変更前・pwdcのD:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（変更・pwdc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い、EFIX」を指し、EFIX LABELではbo・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 状態確認 EFIX LABEL 0405**

    - 検証目的: 導入と起動のbootlist -m normal 状態確認 EFIX LABEL 0405について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認045-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0405A
    ```

    画面・出力には AIX0405A が表示され、bootlist -m normal 状態確認 EFIX LABEL 0405 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0405B
    ```

    画面・出力には AIX0405B が表示され、bootlist -m normal 状態確認 EFIX LABEL 0405 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0405C
    ```

    画面・出力には AIX0405C が表示され、bootlist -m normal 状態確認 EFIX LABEL 0405 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0405A が画面・出力に表示されること
    ② ステップ2 の AIX0405B が画面・出力に表示されること
    ③ ステップ3 の AIX0405C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 状態確認 EFIX LABEL 0465 {#c01-i0717}
*分類: 導入と起動*  ・  難易度: 上級

花冷整理ではAIX 7.3の導入と起動で bootlist -m normal を確認します。花冷整理の導入と起動では EFIX LABEL と起動デバイス設定を判定票へ残します。花冷整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷整理の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、花冷整理を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「bootlist -m normal 状態確認 EFIX LABEL 0465」を「cfgmgr 構成照合 MTU 0466」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。
    - B. 運用時に利用する技術的役割はデバイス管理でrmdev -Rl ent1を用い・attribute とODM属性を確認する。rmdev -Rl ent1 性能確認 attribute 0771固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割は導入と起動でbootlist -m normalを用い・EFIX LABEL と起動デバイス設定を確認する。 ✅
    - D. 運用時に利用する技術的役割はセキュリティでusrck -n ALLを用い・enhanced_RBAC とRBAC属性を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「導入と起動でbootlist -m normalを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・boot）です。状態に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い、EFIX」で、確認対象はbo・状態です。構成・cfgmのA:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。性能・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 attribute（性能・rmde）です。変更後・usrcのD:は「セキュリティでusrck -n ALLを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・usrc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い、EFIX」を指し、EFIX LABELではbo・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 状態確認 EFIX LABEL 0465**

    - 検証目的: 導入と起動のbootlist -m normal 状態確認 EFIX LABEL 0465について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認105-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0465A
    ```

    画面・出力には AIX0465A が表示され、bootlist -m normal 状態確認 EFIX LABEL 0465 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0465B
    ```

    画面・出力には AIX0465B が表示され、bootlist -m normal 状態確認 EFIX LABEL 0465 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0465C
    ```

    画面・出力には AIX0465C が表示され、bootlist -m normal 状態確認 EFIX LABEL 0465 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0465A が画面・出力に表示されること
    ② ステップ2 の AIX0465B が画面・出力に表示されること
    ③ ステップ3 の AIX0465C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 監査記録 mksysb image 0435 {#c01-i0718}
*分類: 導入と起動*  ・  難易度: 中級

青磁評価ではAIX 7.3の導入と起動で bootlist -m normal を確認します。青磁評価の導入と起動では mksysb image とfileset一覧を作業票へ保管します。青磁評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。青磁評価の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、青磁評価を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 監査記録 mksysb image 0435について構成や状態を確認します。cfgmgr 運用引継ぎ EtherChannel 0436ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはネットワークでcfgmgrを用い・EtherChannel と経路表を確認する。
    - B. 状態を読み取るための働きはデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。
    - C. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。
    - D. 状態を読み取るための働きは導入と起動でbootlist -m normalを用い・mksysb imageである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でbootlist -m normalを用い、mksysb」に対応する項目はmksysb image（監査・boot）です。監査に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・監査です。運用引・cfgmのA:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は運用引継ぎ EtherChannel（運用・cfgm）です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。性能・usrcのC:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、mksysb imageではbo・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 監査記録 mksysb image 0435**

    - 検証目的: 導入と起動のbootlist -m normal 監査記録 mksysb image 0435について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録075-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0435A
    ```

    画面・出力には AIX0435A が表示され、bootlist -m normal 監査記録 mksysb image 0435 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0435B
    ```

    画面・出力には AIX0435B が表示され、bootlist -m normal 監査記録 mksysb image 0435 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0435C
    ```

    画面・出力には AIX0435C が表示され、bootlist -m normal 監査記録 mksysb image 0435 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0435A が画面・出力に表示されること
    ② ステップ2 の AIX0435B が画面・出力に表示されること
    ③ ステップ3 の AIX0435C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 起動確認 fileset level 0594 {#c01-i0719}
*分類: 導入と起動*  ・  難易度: 上級

銀嶺点検ではAIX 7.3の導入と起動で bootlist -m normal を確認します。銀嶺点検の導入と起動では fileset level とOSレベル表示を変更票へ記録します。銀嶺点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。銀嶺点検の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、銀嶺点検を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 起動確認 fileset level 0594の役割を調べています。cfgmgr 属性確認 MTU 0595の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。
    - B. 機能の説明としては導入と起動でbootlist -m normalを用い・fileset levelである。 ✅
    - C. 機能の説明としてはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。
    - D. 機能の説明としてはセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「導入と起動でbootlist -m normalを用い、fileset」に対応する項目はfileset level（起動・boot）です。起動に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・起動です。属性・cfgmのA:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は属性確認 MTU（属性・cfgm）です。一覧・保存・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は一覧確認 保存場所（一覧・lpar）です。構成・usrcのD:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、fileset levelではbo・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 起動確認 fileset level 0594**

    - 検証目的: 導入と起動のbootlist -m normal 起動確認 fileset level 0594について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認114-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0594A
    ```

    画面・出力には AIX0594A が表示され、bootlist -m normal 起動確認 fileset level 0594 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0594B
    ```

    画面・出力には AIX0594B が表示され、bootlist -m normal 起動確認 fileset level 0594 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0594C
    ```

    画面・出力には AIX0594C が表示され、bootlist -m normal 起動確認 fileset level 0594 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0594A が画面・出力に表示されること
    ② ステップ2 の AIX0594B が画面・出力に表示されること
    ③ ステップ3 の AIX0594C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bootlist -m normal 起動確認 mksysb image 0118 {#c01-i0720}
*分類: 導入と起動*  ・  難易度: 上級

春霞点検ではAIX 7.3の導入と起動で bootlist -m normal を確認します。春霞点検の導入と起動では mksysb image とOSレベル表示を保守票へ記録します。春霞点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春霞点検の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、春霞点検を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bootlist -m normal 起動確認 mksysb image 0118に関する障害切り分けの前提を確認しています。cfgmgr 属性確認 Link Status 0119の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。
    - B. 表示や設定で扱う内容は導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。 ✅
    - C. 表示や設定で扱う内容はデバイス管理でrmdev -Rl ent1を用い・microcode levelである。rmdev -Rl ent1 運用引継ぎ microcode固有の属性も確認対象に含める。
    - D. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「導入と起動でbootlist -m normalを用い、mksysb image」に対応する項目はmksysb image（起動・boot）です。起動に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・起動です。属性・cfgmのA:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（属性・cfgm）です。運用引・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（運用・rmde）です。バック・noのD:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、mksysb imageではbo・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bootlist -m normal 起動確認 mksysb image 0118**

    - 検証目的: 導入と起動のbootlist -m normal 起動確認 mksysb image 0118について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認118-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0118A
    ```

    画面・出力には AIX0118A が表示され、bootlist -m normal 起動確認 mksysb image 0118 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0118B
    ```

    画面・出力には AIX0118B が表示され、bootlist -m normal 起動確認 mksysb image 0118 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0118C
    ```

    画面・出力には AIX0118C が表示され、bootlist -m normal 起動確認 mksysb image 0118 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0118A が画面・出力に表示されること
    ② ステップ2 の AIX0118B が画面・出力に表示されること
    ③ ステップ3 の AIX0118C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 変更後確認 EFIX LABEL 0027 {#c01-i0721}
*分類: 導入と起動*  ・  難易度: 中級

風花確認ではAIX 7.3の導入と起動で bosboot -a -d を確認します。風花確認の導入と起動では EFIX LABEL とfileset一覧を作業票へ保管します。風花確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。風花確認の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、風花確認を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 変更後確認 EFIX LABEL 0027について構成や状態を確認します。route -n get 障害切り分け MTU 0028ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはネットワークでroute -n getを用い・MTU と経路表を確認する。
    - B. 状態を読み取るための働きは導入と起動でbosboot -a -dを用い・EFIX LABEL とfileset一覧を確認する。 ✅
    - C. 状態を読み取るための働きはデバイス管理でlscfg -vl ent0を用い・location code と診断対象表示を確認する。
    - D. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でbosboot -a -dを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・bosb）です。導入と起動の仕様は「導入と起動でbosboot -a -dを用い、EFIX LABEL」で、確認対象はbo・変更後です。障害切・routのA:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。属性・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、location」を述べ、対象はlocation code（属性・lscf）です。性能・netsのD:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、EFIX LABEL」を指し、EFIX LABELではbo・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 変更後確認 EFIX LABEL 0027**

    - 検証目的: 導入と起動のbosboot -a -d 変更後確認 EFIX LABEL 0027について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認027-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0027A
    ```

    画面・出力には AIX0027A が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0027 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0027B
    ```

    画面・出力には AIX0027B が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0027 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0027C
    ```

    画面・出力には AIX0027C が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0027 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0027A が画面・出力に表示されること
    ② ステップ2 の AIX0027B が画面・出力に表示されること
    ③ ステップ3 の AIX0027C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 変更後確認 EFIX LABEL 0087 {#c01-i0722}
*分類: 導入と起動*  ・  難易度: 中級

夕凪点検ではAIX 7.3の導入と起動で bosboot -a -d を確認します。夕凪点検の導入と起動では EFIX LABEL とfileset一覧を作業票へ保管します。夕凪点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。夕凪点検の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、夕凪点検を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 変更後確認 EFIX LABEL 0087の設定や表示を読む前に役割を確認します。route -n get 障害切り分け MTU 0088ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはネットワークでroute -n getを用い・MTU と経路表を確認する。
    - B. 状態を読み取るための働きは導入と起動でbosboot -a -dを用い・EFIX LABEL とfileset一覧を確認する。 ✅
    - C. 状態を読み取るための働きはデバイス管理でdiag -d ent0を用い・attribute と診断対象表示を確認する。
    - D. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でbosboot -a -dを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・bosb）です。変更後に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、EFIX LABEL」で、確認対象はbo・変更後です。障害切・routのA:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。状態・diagのC:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は状態確認 attribute（状態・diag）です。性能・netsのD:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、EFIX LABEL」を指し、EFIX LABELではbo・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 変更後確認 EFIX LABEL 0087**

    - 検証目的: 導入と起動のbosboot -a -d 変更後確認 EFIX LABEL 0087について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認087-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0087A
    ```

    画面・出力には AIX0087A が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0087 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0087B
    ```

    画面・出力には AIX0087B が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0087 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0087C
    ```

    画面・出力には AIX0087C が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0087 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0087A が画面・出力に表示されること
    ② ステップ2 の AIX0087B が画面・出力に表示されること
    ③ ステップ3 の AIX0087C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 変更後確認 altinst_rootvg 0503 {#c01-i0723}
*分類: 導入と起動*  ・  難易度: 中級

新緑確認ではAIX 7.3の導入と起動で bosboot -a -d を確認します。新緑確認の導入と起動では altinst_rootvg とfileset一覧を照合票へ整理します。新緑確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑確認の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、新緑確認を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 変更後確認 altinst_rootvg 0503の設定や表示を読む前に役割を確認します。route -n get 障害切り分け Gateway 0504ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。 ✅
    - B. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。
    - C. 一次資料が示す主目的はデバイス管理でlscfg -vl ent0を用い・PVID と診断対象表示を確認する。lscfg -vl ent0 属性確認 PVID 0809固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でbosboot -a -dを用い、altinst_rootvg」に対応する項目は変更後確認 altinst_root（変更・bosb）です。変更後に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い」で、確認対象はbo・変更後です。障害切・routのB:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。属性・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は属性確認 PVID（属性・lscf）です。バック・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い」を指し、変更後確認 altinst_rootではbo・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 変更後確認 altinst_rootvg 0503**

    - 検証目的: 導入と起動のbosboot -a -d 変更後確認 altinst_rootvg 0503について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認023-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0503A
    ```

    画面・出力には AIX0503A が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0503 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0503B
    ```

    画面・出力には AIX0503B が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0503 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0503C
    ```

    画面・出力には AIX0503C が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0503 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0503A が画面・出力に表示されること
    ② ステップ2 の AIX0503B が画面・出力に表示されること
    ③ ステップ3 の AIX0503C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 変更後確認 altinst_rootvg 0563 {#c01-i0724}
*分類: 導入と起動*  ・  難易度: 中級

秋声点検ではAIX 7.3の導入と起動で bosboot -a -d を確認します。秋声点検の導入と起動では altinst_rootvg とfileset一覧を照合票へ整理します。秋声点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声点検の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、秋声点検を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 変更後確認 altinst_rootvg 0563について構成や状態を確認します。route -n get 障害切り分け Gateway 0564ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。route -n get 障害切り分け Gateway 0564固有の属性も確認対象に含める。
    - B. 一次資料が示す主目的はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - C. 一次資料が示す主目的はセキュリティでpwdck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。
    - D. 一次資料が示す主目的は導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でbosboot -a -dを用い、altinst_rootvg」に対応する項目は変更後確認 altinst_root（変更・bosb）です。変更後に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い」で、確認対象はbo・変更後です。障害切・routのA:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。変更前・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は変更前確認 性能値（変更・vmst）です。監査・pwdcのC:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・pwdc）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い」を指し、変更後確認 altinst_rootではbo・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 変更後確認 altinst_rootvg 0563**

    - 検証目的: 導入と起動のbosboot -a -d 変更後確認 altinst_rootvg 0563について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認083-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0563A
    ```

    画面・出力には AIX0563A が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0563 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0563B
    ```

    画面・出力には AIX0563B が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0563 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0563C
    ```

    画面・出力には AIX0563C が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0563 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0563A が画面・出力に表示されること
    ② ステップ2 の AIX0563B が画面・出力に表示されること
    ③ ステップ3 の AIX0563C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 性能確認 fileset level 0533 {#c01-i0725}
*分類: 導入と起動*  ・  難易度: 中級

月影照合ではAIX 7.3の導入と起動で bosboot -a -d を確認します。月影照合の導入と起動では fileset level と起動デバイス設定を復旧票へ残します。月影照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影照合の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、月影照合を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 性能確認 fileset level 0533を保守記録に説明する必要があります。route -n get 起動確認 Media Speed Running 0534と取り違えない説明はどれですか。

    - A. 仕様上の役割は導入と起動でbosboot -a -dを用い・fileset level と起動デバイス設定を確認する。 ✅
    - B. 仕様上の役割はネットワークでroute -n getを用い・Media Speed Runningである。
    - C. 仕様上の役割はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。lscfg -vl ent0 バックアウト確認 Available固有の属性も確認対象に含める。
    - D. 仕様上の役割はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でbosboot -a -dを用い、fileset level」に対応する項目はfileset level（性能・bosb）です。性能に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、fileset」で、確認対象はbo・性能です。起動・routのB:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（起動・rout）です。バック・lscfのC:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。属性・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（属性・lsus）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、fileset」を指し、fileset levelではbo・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 性能確認 fileset level 0533**

    - 検証目的: 導入と起動のbosboot -a -d 性能確認 fileset level 0533について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認053-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0533A
    ```

    画面・出力には AIX0533A が表示され、bosboot -a -d 性能確認 fileset level 0533 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0533B
    ```

    画面・出力には AIX0533B が表示され、bosboot -a -d 性能確認 fileset level 0533 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0533C
    ```

    画面・出力には AIX0533C が表示され、bosboot -a -d 性能確認 fileset level 0533 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0533A が画面・出力に表示されること
    ② ステップ2 の AIX0533B が画面・出力に表示されること
    ③ ステップ3 の AIX0533C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 性能確認 mksysb image 0057 {#c01-i0726}
*分類: 導入と起動*  ・  難易度: 中級

初霜照合ではAIX 7.3の導入と起動で bosboot -a -d を確認します。初霜照合の導入と起動では mksysb image と起動デバイス設定を判定票へ残します。初霜照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。初霜照合の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、初霜照合を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「bosboot -a -d 性能確認 mksysb image 0057」を「route -n get 起動確認 EtherChannel 0058」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は導入と起動でbosboot -a -dを用い・mksysb image と起動デバイス設定を確認する。 ✅
    - B. 運用時に利用する技術的役割はネットワークでroute -n getを用い・EtherChannel とアダプター一覧を確認する。
    - C. 運用時に利用する技術的役割はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。diag -d ent0 監査記録 microcode level固有の属性も確認対象に含める。
    - D. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でbosboot -a -dを用い、mksysb image」に対応する項目はmksysb image（性能・bosb）です。導入と起動の仕様は「導入と起動でbosboot -a -dを用い、mksysb image」で、確認対象はbo・性能です。起動・routのB:は「ネットワークでroute -n getを用い」を述べ、対象は起動確認 EtherChannel（起動・rout）です。監査・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（監査・diag）です。変更後・netsのD:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、mksysb」を指し、mksysb imageではbo・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 性能確認 mksysb image 0057**

    - 検証目的: 導入と起動のbosboot -a -d 性能確認 mksysb image 0057について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認057-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0057A
    ```

    画面・出力には AIX0057A が表示され、bosboot -a -d 性能確認 mksysb image 0057 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0057B
    ```

    画面・出力には AIX0057B が表示され、bosboot -a -d 性能確認 mksysb image 0057 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0057C
    ```

    画面・出力には AIX0057C が表示され、bosboot -a -d 性能確認 mksysb image 0057 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0057A が画面・出力に表示されること
    ② ステップ2 の AIX0057B が画面・出力に表示されること
    ③ ステップ3 の AIX0057C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 構成照合 bootlist 0692 {#c01-i0727}
*分類: 導入と起動*  ・  難易度: 中級

水音保守ではAIX 7.3の導入と起動で bosboot -a -d を確認します。水音保守の導入と起動では bootlist と代替ディスク状態を引継ぎ票へ保管します。水音保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音保守の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、水音保守を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 構成照合 bootlist 0692の技術的な意味を資料で確認するとき、route -n get 変更前確認 Gateway 0693との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。
    - B. コマンドまたは機能の用途はJFS2でlogformを用い・mountguard とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途は導入と起動でbosboot -a -dを用い・bootlist と代替ディスク状態を確認する。 ✅
    - D. コマンドまたは機能の用途はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でbosboot -a -dを用い、bootlist」に対応する項目は構成照合 bootlist（構成・bosb）です。構成に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、bootlist」で、確認対象はbo・構成です。変更前・routのA:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・rout）です。監査・logfのB:は「JFS2でlogformを用い、mountguard」を述べ、対象は監査記録 mountguard（監査・logf）です。障害切・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、bootlist」を指し、構成照合 bootlistではbo・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 構成照合 bootlist 0692**

    - 検証目的: 導入と起動のbosboot -a -d 構成照合 bootlist 0692について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合092-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0692A
    ```

    画面・出力には AIX0692A が表示され、bosboot -a -d 構成照合 bootlist 0692 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0692B
    ```

    画面・出力には AIX0692B が表示され、bosboot -a -d 構成照合 bootlist 0692 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0692C
    ```

    画面・出力には AIX0692C が表示され、bosboot -a -d 構成照合 bootlist 0692 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0692A が画面・出力に表示されること
    ② ステップ2 の AIX0692B が画面・出力に表示されること
    ③ ステップ3 の AIX0692C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 構成照合 fileset level 0216 {#c01-i0728}
*分類: 導入と起動*  ・  難易度: 中級

若竹保守ではAIX 7.3の導入と起動で bosboot -a -d を確認します。若竹保守の導入と起動では fileset level と代替ディスク状態を同じ証跡に残します。若竹保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若竹保守の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、若竹保守を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 構成照合 fileset level 0216を同一分類のroute -n get 変更前確認 MTU 0217と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は導入と起動でbosboot -a -dを用い・fileset level と代替ディスク状態を確認する。 ✅
    - B. 構成を確認する際の意味はネットワークでroute -n getを用い・MTU とMTU属性を確認する。
    - C. 構成を確認する際の意味はデバイス管理でdiag -d ent0を用い・location code とデバイス一覧を確認する。
    - D. 構成を確認する際の意味はネットワークでnetstat -vを用い・Media Speed Running とMTU属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でbosboot -a -dを用い、fileset level」に対応する項目はfileset level（構成・bosb）です。構成に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、fileset」で、確認対象はbo・構成です。変更前・routのB:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は変更前確認 MTU（変更・rout）です。起動・diagのC:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（起動・diag）です。運用引・netsのD:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（運用・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、fileset」を指し、fileset levelではbo・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 構成照合 fileset level 0216**

    - 検証目的: 導入と起動のbosboot -a -d 構成照合 fileset level 0216について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合096-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0216A
    ```

    画面・出力には AIX0216A が表示され、bosboot -a -d 構成照合 fileset level 0216 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0216B
    ```

    画面・出力には AIX0216B が表示され、bosboot -a -d 構成照合 fileset level 0216 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0216C
    ```

    画面・出力には AIX0216C が表示され、bosboot -a -d 構成照合 fileset level 0216 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0216A が画面・出力に表示されること
    ② ステップ2 の AIX0216B が画面・出力に表示されること
    ③ ステップ3 の AIX0216C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 運用引継ぎ Technology Level 0662 {#c01-i0729}
*分類: 導入と起動*  ・  難易度: 中級

紅葉判定ではAIX 7.3の導入と起動で bosboot -a -d を確認します。紅葉判定の導入と起動では Technology Level とOSレベル表示を確認票へ整理します。紅葉判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉判定の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、紅葉判定を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 運用引継ぎ Technology Level 0662に関する障害切り分けの前提を確認しています。route -n get 容量確認 Media Speed Running 0663の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はネットワークでroute -n getを用い・Media Speed Runningである。route -n get 容量確認 Media Speed固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割はJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。
    - C. 障害切り分けに用いる役割は導入と起動でbosboot -a -dを用い・Technology Level とOSレベル表示を確認する。 ✅
    - D. 障害切り分けに用いる役割はセキュリティでlsuserを用い・enhanced_RBAC とロール一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でbosboot -a -dを用い、Technology Level」に対応する項目はTechnology Level（運用・bosb）です。運用引に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、Technology」で、確認対象はbo・運用引です。容量・routのA:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（容量・rout）です。状態・logfのB:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は状態確認 log=INLINE（状態・logf）です。性能・lsusのD:は「セキュリティでlsuserを用い、enhanced_RBAC」を述べ、対象は性能確認 enhanced_RBAC（性能・lsus）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、Technology」を指し、Technology Levelではbo・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 運用引継ぎ Technology Level 0662**

    - 検証目的: 導入と起動のbosboot -a -d 運用引継ぎ Technology Level 0662について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ062-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0662A
    ```

    画面・出力には AIX0662A が表示され、bosboot -a -d 運用引継ぎ Technology Level 0662 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0662B
    ```

    画面・出力には AIX0662B が表示され、bosboot -a -d 運用引継ぎ Technology Level 0662 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0662C
    ```

    画面・出力には AIX0662C が表示され、bosboot -a -d 運用引継ぎ Technology Level 0662 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0662A が画面・出力に表示されること
    ② ステップ2 の AIX0662B が画面・出力に表示されること
    ③ ステップ3 の AIX0662C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### bosboot -a -d 運用引継ぎ altinst_rootvg 0186 {#c01-i0730}
*分類: 導入と起動*  ・  難易度: 中級

陽炎判定ではAIX 7.3の導入と起動で bosboot -a -d を確認します。陽炎判定の導入と起動では altinst_rootvg とOSレベル表示を変更票へ記録します。陽炎判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。陽炎判定の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、陽炎判定を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** bosboot -a -d 運用引継ぎ altinst_rootvg 0186の役割を調べています。route -n get 容量確認 EtherChannel 0187の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては導入と起動でbosboot -a -dを用い・altinst_rootvg とOSレベル表示を確認する。 ✅
    - B. 機能の説明としてはネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。
    - C. 機能の説明としてはデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。
    - D. 機能の説明としてはネットワークでnetstat -vを用い・Gateway とEthernet統計を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でbosboot -a -dを用い、altinst_rootvg」に対応する項目は運用引継ぎ altinst_root（運用・bosb）です。運用引に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い」で、確認対象はbo・運用引です。容量・routのB:は「ネットワークでroute -n getを用い」を述べ、対象は容量確認 EtherChannel（容量・rout）です。障害切・diagのC:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。構成・netsのD:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は構成照合 Gateway（構成・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い」を指し、運用引継ぎ altinst_rootではbo・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **bosboot -a -d 運用引継ぎ altinst_rootvg 0186**

    - 検証目的: 導入と起動のbosboot -a -d 運用引継ぎ altinst_rootvg 0186について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ066-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bosboot -a -d
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0186A
    ```

    画面・出力には AIX0186A が表示され、bosboot -a -d 運用引継ぎ altinst_rootvg 0186 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0186B
    ```

    画面・出力には AIX0186B が表示され、bosboot -a -d 運用引継ぎ altinst_rootvg 0186 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0186C
    ```

    画面・出力には AIX0186C が表示され、bosboot -a -d 運用引継ぎ altinst_rootvg 0186 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0186A が画面・出力に表示されること
    ② ステップ2 の AIX0186B が画面・出力に表示されること
    ③ ステップ3 の AIX0186C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l バックアウト確認 Technology Level 0767 {#c01-i0731}
*分類: 導入と起動*  ・  難易度: 中級

夕凪復旧ではAIX 7.3の導入と起動で emgr -l を確認します。夕凪復旧の導入と起動では Technology Level とfileset一覧を照合票へ整理します。夕凪復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。夕凪復旧の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、夕凪復旧を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l バックアウト確認 Technology Level 0767の設定や表示を読む前に役割を確認します。netstat -rn 監査記録 Link Status 0768ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はネットワークでnetstat -rnを用い・Link Status と経路表を確認する。
    - B. 一次資料が示す主目的はLVMでmklvを用い・PVID とミラーコピー状態を確認する。
    - C. 一次資料が示す主目的はセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。
    - D. 一次資料が示す主目的は導入と起動でemgr -lを用い・Technology Level とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でemgr -lを用い、Technology Level」に対応する項目はTechnology Level（バッ・emgr）です。バックに関する導入と起動の仕様は「導入と起動でemgr -lを用い、Technology Level」で、確認対象はem・バックです。監査・netsのA:は「ネットワークでnetstat -rnを用い、Link Status」を述べ、対象はLink Status（監査・nets）です。起動・mklvのB:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。運用引・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（運用・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、Technology Level」を指し、Technology Levelではem・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l バックアウト確認 Technology Level 0767**

    - 検証目的: 導入と起動のemgr -l バックアウト確認 Technology Level 0767について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認047-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0767A
    ```

    画面・出力には AIX0767A が表示され、emgr -l バックアウト確認 Technology Level 0767 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0767B
    ```

    画面・出力には AIX0767B が表示され、emgr -l バックアウト確認 Technology Level 0767 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0767C
    ```

    画面・出力には AIX0767C が表示され、emgr -l バックアウト確認 Technology Level 0767 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0767A が画面・出力に表示されること
    ② ステップ2 の AIX0767B が画面・出力に表示されること
    ③ ステップ3 の AIX0767C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l バックアウト確認 altinst_rootvg 0291 {#c01-i0732}
*分類: 導入と起動*  ・  難易度: 中級

松風復旧ではAIX 7.3の導入と起動で emgr -l を確認します。松風復旧の導入と起動では altinst_rootvg とfileset一覧を作業票へ保管します。松風復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。松風復旧の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、松風復旧を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l バックアウト確認 altinst_rootvg 0291について構成や状態を確認します。netstat -rn 監査記録 Gateway 0292ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはネットワークでnetstat -rnを用い・Gateway と経路表を確認する。
    - B. 状態を読み取るための働きはデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。lsattr -El hdisk0 構成照合 PVID 0597固有の属性も確認対象に含める。
    - C. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - D. 状態を読み取るための働きは導入と起動でemgr -lを用い・altinst_rootvg とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でemgr -lを用い、altinst_rootvg」に対応する項目はバックアウト確認 altinst_r（バッ・emgr）です。バックに関する導入と起動の仕様は「導入と起動でemgr -lを用い、altinst_rootvg」で、確認対象はem・バックです。監査・netsのA:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は監査記録 Gateway（監査・nets）です。構成・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。性能・停止・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は性能確認 停止確認（性能・lsps）です。「emgr -l」は「導入と起動でemgr -lを用い、altinst_rootvg」を指し、バックアウト確認 altinst_rではem・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l バックアウト確認 altinst_rootvg 0291**

    - 検証目的: 導入と起動のemgr -l バックアウト確認 altinst_rootvg 0291について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認051-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0291A
    ```

    画面・出力には AIX0291A が表示され、emgr -l バックアウト確認 altinst_rootvg 0291 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0291B
    ```

    画面・出力には AIX0291B が表示され、emgr -l バックアウト確認 altinst_rootvg 0291 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0291C
    ```

    画面・出力には AIX0291C が表示され、emgr -l バックアウト確認 altinst_rootvg 0291 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0291A が画面・出力に表示されること
    ② ステップ2 の AIX0291B が画面・出力に表示されること
    ③ ステップ3 の AIX0291C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l 変更後確認 bootlist 0420 {#c01-i0733}
*分類: 導入と起動*  ・  難易度: 中級

薄明評価ではAIX 7.3の導入と起動で emgr -l を確認します。薄明評価の導入と起動では bootlist と代替ディスク状態を同じ証跡に残します。薄明評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。薄明評価の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、薄明評価を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l 変更後確認 bootlist 0420の技術的な意味を資料で確認するとき、netstat -rn 障害切り分け Gateway 0421との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は導入と起動でemgr -lを用い・bootlist と代替ディスク状態を確認する。 ✅
    - B. 構成を確認する際の意味はネットワークでnetstat -rnを用い・Gateway とMTU属性を確認する。
    - C. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。
    - D. 構成を確認する際の意味はセキュリティでrbacqry -u user1 -Tを用い・roles と監査設定を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でemgr -lを用い、bootlist と代替ディスク状態を確認する」に対応する項目は変更後確認 bootlist（変更・emgr）です。変更後に関する導入と起動の仕様は「導入と起動でemgr -lを用い、bootlist」で、確認対象はem・変更後です。障害切・netsのB:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・nets）です。状態・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。バック・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はバックアウト確認 roles（バッ・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、bootlist」を指し、変更後確認 bootlistではem・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l 変更後確認 bootlist 0420**

    - 検証目的: 導入と起動のemgr -l 変更後確認 bootlist 0420について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認060-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0420A
    ```

    画面・出力には AIX0420A が表示され、emgr -l 変更後確認 bootlist 0420 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0420B
    ```

    画面・出力には AIX0420B が表示され、emgr -l 変更後確認 bootlist 0420 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0420C
    ```

    画面・出力には AIX0420C が表示され、emgr -l 変更後確認 bootlist 0420 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0420A が画面・出力に表示されること
    ② ステップ2 の AIX0420B が画面・出力に表示されること
    ③ ステップ3 の AIX0420C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l 変更後確認 bootlist 0480 {#c01-i0734}
*分類: 導入と起動*  ・  難易度: 上級

青葉確認ではAIX 7.3の導入と起動で emgr -l を確認します。青葉確認の導入と起動では bootlist と代替ディスク状態を同じ証跡に残します。青葉確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。青葉確認の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、青葉確認を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l 変更後確認 bootlist 0480を同一分類のnetstat -v バックアウト確認 EtherChannel 0481と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は導入と起動でemgr -lを用い・bootlist と代替ディスク状態を確認する。 ✅
    - B. 構成を確認する際の意味はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。
    - C. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。
    - D. 構成を確認する際の意味はセキュリティでlssecattr -cを用い・audit class と監査設定を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「導入と起動でemgr -lを用い、bootlist と代替ディスク状態を確認する」に対応する項目は変更後確認 bootlist（変更・emgr）です。変更後に関する導入と起動の仕様は「導入と起動でemgr -lを用い、bootlist」で、確認対象はem・変更後です。バック・netsのB:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象はバックアウト確認 EtherChan（バッ・nets）です。状態・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。監査・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（監査・lsse）です。「emgr -l」は「導入と起動でemgr -lを用い、bootlist」を指し、変更後確認 bootlistではem・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l 変更後確認 bootlist 0480**

    - 検証目的: 導入と起動のemgr -l 変更後確認 bootlist 0480について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認120-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0480A
    ```

    画面・出力には AIX0480A が表示され、emgr -l 変更後確認 bootlist 0480 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0480B
    ```

    画面・出力には AIX0480B が表示され、emgr -l 変更後確認 bootlist 0480 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0480C
    ```

    画面・出力には AIX0480C が表示され、emgr -l 変更後確認 bootlist 0480 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0480A が画面・出力に表示されること
    ② ステップ2 の AIX0480B が画面・出力に表示されること
    ③ ステップ3 の AIX0480C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l 属性確認 bootlist 0737 {#c01-i0735}
*分類: 導入と起動*  ・  難易度: 初級

初霜監査ではAIX 7.3の導入と起動で emgr -l を確認します。初霜監査の導入と起動では bootlist と起動デバイス設定を復旧票へ残します。初霜監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。初霜監査の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、初霜監査を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「emgr -l 属性確認 bootlist 0737」を「netstat -rn 状態確認 Destination 0738」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はネットワークでnetstat -rnを用い・Destination とアダプター一覧を確認する。
    - B. 仕様上の役割はJFS2でfsckを用い・mountguard と内部スナップショットを確認する。
    - C. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。
    - D. 仕様上の役割は導入と起動でemgr -lを用い・bootlist と起動デバイス設定を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「導入と起動でemgr -lを用い、bootlist と起動デバイス設定を確認する」に対応する項目は属性確認 bootlist（属性・emgr）です。属性に関する導入と起動の仕様は「導入と起動でemgr -lを用い、bootlist」で、確認対象はem・属性です。状態・netsのA:は「ネットワークでnetstat -rnを用い、Destination」を述べ、対象は状態確認 Destination（状態・nets）です。障害切・fsckのB:は「JFS2でfsckを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・fsck）です。構成・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（構成・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、bootlist」を指し、属性確認 bootlistではem・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l 属性確認 bootlist 0737**

    - 検証目的: 導入と起動のemgr -l 属性確認 bootlist 0737について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認017-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0737A
    ```

    画面・出力には AIX0737A が表示され、emgr -l 属性確認 bootlist 0737 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0737B
    ```

    画面・出力には AIX0737B が表示され、emgr -l 属性確認 bootlist 0737 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0737C
    ```

    画面・出力には AIX0737C が表示され、emgr -l 属性確認 bootlist 0737 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0737A が画面・出力に表示されること
    ② ステップ2 の AIX0737B が画面・出力に表示されること
    ③ ステップ3 の AIX0737C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l 属性確認 fileset level 0261 {#c01-i0736}
*分類: 導入と起動*  ・  難易度: 初級

群青監査ではAIX 7.3の導入と起動で emgr -l を確認します。群青監査の導入と起動では fileset level と起動デバイス設定を判定票へ残します。群青監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。群青監査の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、群青監査を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l 属性確認 fileset level 0261を保守記録に説明する必要があります。netstat -rn 状態確認 Media Speed Running 0262と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はネットワークでnetstat -rnを用い・Media Speed Runningである。
    - B. 運用時に利用する技術的役割は導入と起動でemgr -lを用い・fileset level と起動デバイス設定を確認する。 ✅
    - C. 運用時に利用する技術的役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。
    - D. 運用時に利用する技術的役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「導入と起動でemgr -lを用い、fileset level」に対応する項目はfileset level（属性・emgr）です。属性に関する導入と起動の仕様は「導入と起動でemgr -lを用い、fileset level」で、確認対象はem・属性です。状態・netsのA:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（状態・nets）です。運用引・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。障害切・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は障害切り分け ファイルセット（障害・lsps）です。「emgr -l」は「導入と起動でemgr -lを用い、fileset level」を指し、fileset levelではem・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l 属性確認 fileset level 0261**

    - 検証目的: 導入と起動のemgr -l 属性確認 fileset level 0261について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認021-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0261A
    ```

    画面・出力には AIX0261A が表示され、emgr -l 属性確認 fileset level 0261 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0261B
    ```

    画面・出力には AIX0261B が表示され、emgr -l 属性確認 fileset level 0261 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0261C
    ```

    画面・出力には AIX0261C が表示され、emgr -l 属性確認 fileset level 0261 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0261A が画面・出力に表示されること
    ② ステップ2 の AIX0261B が画面・出力に表示されること
    ③ ステップ3 の AIX0261C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l 性能確認 Technology Level 0390 {#c01-i0737}
*分類: 導入と起動*  ・  難易度: 中級

早苗記録ではAIX 7.3の導入と起動で emgr -l を確認します。早苗記録の導入と起動では Technology Level とOSレベル表示を変更票へ記録します。早苗記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。早苗記録の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、早苗記録を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l 性能確認 Technology Level 0390に関する障害切り分けの前提を確認しています。netstat -rn 起動確認 Media Speed Running 0391の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはネットワークでnetstat -rnを用い・Media Speed Runningである。
    - B. 機能の説明としてはデバイス管理でlsattr -El hdisk0を用い・microcode levelである。
    - C. 機能の説明としてはセキュリティでrbacqry -u user1 -Tを用い・roles とロール一覧を確認する。
    - D. 機能の説明としては導入と起動でemgr -lを用い・Technology Level とOSレベル表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でemgr -lを用い、Technology Level」に対応する項目はTechnology Level（性能・emgr）です。性能に関する導入と起動の仕様は「導入と起動でemgr -lを用い、Technology Level」で、確認対象はem・性能です。起動・netsのA:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（起動・nets）です。バック・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象はmicrocode level（バッ・lsat）です。属性・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象は属性確認 roles（属性・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、Technology Level」を指し、Technology Levelではem・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l 性能確認 Technology Level 0390**

    - 検証目的: 導入と起動のemgr -l 性能確認 Technology Level 0390について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認030-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0390A
    ```

    画面・出力には AIX0390A が表示され、emgr -l 性能確認 Technology Level 0390 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0390B
    ```

    画面・出力には AIX0390B が表示され、emgr -l 性能確認 Technology Level 0390 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0390C
    ```

    画面・出力には AIX0390C が表示され、emgr -l 性能確認 Technology Level 0390 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0390A が画面・出力に表示されること
    ② ステップ2 の AIX0390B が画面・出力に表示されること
    ③ ステップ3 の AIX0390C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### emgr -l 性能確認 Technology Level 0450 {#c01-i0738}
*分類: 導入と起動*  ・  難易度: 中級

桜雲整理ではAIX 7.3の導入と起動で emgr -l を確認します。桜雲整理の導入と起動では Technology Level とOSレベル表示を変更票へ記録します。桜雲整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。桜雲整理の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、桜雲整理を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** emgr -l 性能確認 Technology Level 0450の役割を調べています。netstat -rn 起動確認 Media Speed Running 0451の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはネットワークでnetstat -rnを用い・Media Speed Runningである。
    - B. 機能の説明としては導入と起動でemgr -lを用い・Technology Level とOSレベル表示を確認する。 ✅
    - C. 機能の説明としてはデバイス管理でchdev -l hdisk0を用い・Available と構成マネージャー結果を確認する。
    - D. 機能の説明としてはセキュリティでlssecattr -cを用い・audit class とロール一覧を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でemgr -lを用い、Technology Level」に対応する項目はTechnology Level（性能・emgr）です。性能に関する導入と起動の仕様は「導入と起動でemgr -lを用い、Technology Level」で、確認対象はem・性能です。起動・netsのA:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（起動・nets）です。監査・chdeのC:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象は監査記録 Available（監査・chde）です。状態・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（状態・lsse）です。「emgr -l」は「導入と起動でemgr -lを用い、Technology Level」を指し、Technology Levelではem・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **emgr -l 性能確認 Technology Level 0450**

    - 検証目的: 導入と起動のemgr -l 性能確認 Technology Level 0450について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認090-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> emgr -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0450A
    ```

    画面・出力には AIX0450A が表示され、emgr -l 性能確認 Technology Level 0450 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0450B
    ```

    画面・出力には AIX0450B が表示され、emgr -l 性能確認 Technology Level 0450 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0450C
    ```

    画面・出力には AIX0450C が表示され、emgr -l 性能確認 Technology Level 0450 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0450A が画面・出力に表示されること
    ② ステップ2 の AIX0450B が画面・出力に表示されること
    ③ ステップ3 の AIX0450C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 状態確認 EFIX LABEL 0488 {#c01-i0739}
*分類: 導入と起動*  ・  難易度: 初級

翠風確認ではAIX 7.3の導入と起動で installp -C を確認します。翠風確認の導入と起動では EFIX LABEL と代替ディスク状態を引継ぎ票へ保管します。翠風確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。翠風確認の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、翠風確認を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 状態確認 EFIX LABEL 0488を同一分類のentstat -d ent0 構成照合 Destination 0489と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Destination とMTU属性を確認する。
    - B. コマンドまたは機能の用途はデバイス管理でlsdev -Cc diskを用い・location code とデバイス一覧を確認する。
    - C. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・roles と監査設定を確認する。
    - D. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「導入と起動でinstallp -Cを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・inst）です。状態に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、EFIX LABEL」で、確認対象はin・状態です。構成・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象は構成照合 Destination（構成・ents）です。容量・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、location」を述べ、対象はlocation code（容量・lsde）です。変更前・roleのC:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は変更前確認 roles（変更・role）です。「installp -C」は「導入と起動でinstallp -Cを用い、EFIX LABEL」を指し、EFIX LABELではin・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 状態確認 EFIX LABEL 0488**

    - 検証目的: 導入と起動のinstallp -C 状態確認 EFIX LABEL 0488について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認008-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0488A
    ```

    画面・出力には AIX0488A が表示され、installp -C 状態確認 EFIX LABEL 0488 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0488B
    ```

    画面・出力には AIX0488B が表示され、installp -C 状態確認 EFIX LABEL 0488 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0488C
    ```

    画面・出力には AIX0488C が表示され、installp -C 状態確認 EFIX LABEL 0488 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0488A が画面・出力に表示されること
    ② ステップ2 の AIX0488B が画面・出力に表示されること
    ③ ステップ3 の AIX0488C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 状態確認 EFIX LABEL 0548 {#c01-i0740}
*分類: 導入と起動*  ・  難易度: 中級

雪解照合ではAIX 7.3の導入と起動で installp -C を確認します。雪解照合の導入と起動では EFIX LABEL と代替ディスク状態を引継ぎ票へ保管します。雪解照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。雪解照合の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、雪解照合を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 状態確認 EFIX LABEL 0548の技術的な意味を資料で確認するとき、entstat -d ent0 構成照合 Destination 0549との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Destination とMTU属性を確認する。
    - B. コマンドまたは機能の用途はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - C. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。 ✅
    - D. コマンドまたは機能の用途はセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でinstallp -Cを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・inst）です。状態に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、EFIX LABEL」で、確認対象はin・状態です。構成・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象は構成照合 Destination（構成・ents）です。変更前・lspsのB:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は変更前確認 停止確認（変更・lsps）です。変更後・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（変更・rbac）です。「installp -C」は「導入と起動でinstallp -Cを用い、EFIX LABEL」を指し、EFIX LABELではin・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 状態確認 EFIX LABEL 0548**

    - 検証目的: 導入と起動のinstallp -C 状態確認 EFIX LABEL 0548について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認068-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0548A
    ```

    画面・出力には AIX0548A が表示され、installp -C 状態確認 EFIX LABEL 0548 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0548B
    ```

    画面・出力には AIX0548B が表示され、installp -C 状態確認 EFIX LABEL 0548 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0548C
    ```

    画面・出力には AIX0548C が表示され、installp -C 状態確認 EFIX LABEL 0548 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0548A が画面・出力に表示されること
    ② ステップ2 の AIX0548B が画面・出力に表示されること
    ③ ステップ3 の AIX0548C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 状態確認 Technology Level 0012 {#c01-i0741}
*分類: 導入と起動*  ・  難易度: 初級

水音確認ではAIX 7.3の導入と起動で installp -C を確認します。水音確認の導入と起動では Technology Level と代替ディスク状態を同じ証跡に残します。水音確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。水音確認の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、水音確認を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 状態確認 Technology Level 0012の技術的な意味を資料で確認するとき、entstat -d ent0 構成照合 Media Speed Runningとの境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。 ✅
    - B. 構成を確認する際の意味はネットワークでentstat -d ent0を用い・Media Speed Runningである。
    - C. 構成を確認する際の意味はデバイス管理でlsdev -Cc diskを用い・microcode level とデバイス一覧を確認する。
    - D. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「導入と起動でinstallp -Cを用い、Technology Level」に対応する項目はTechnology Level（状態・inst）です。導入と起動の仕様は「導入と起動でinstallp -Cを用い、Technology」で、確認対象はin・状態です。構成・entsのB:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。容量・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（容量・lsde）です。監査・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、Technology」を指し、Technology Levelではin・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 状態確認 Technology Level 0012**

    - 検証目的: 導入と起動のinstallp -C 状態確認 Technology Level 0012について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認012-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0012A
    ```

    画面・出力には AIX0012A が表示され、installp -C 状態確認 Technology Level 0012 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0012B
    ```

    画面・出力には AIX0012B が表示され、installp -C 状態確認 Technology Level 0012 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0012C
    ```

    画面・出力には AIX0012C が表示され、installp -C 状態確認 Technology Level 0012 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0012A が画面・出力に表示されること
    ② ステップ2 の AIX0012B が画面・出力に表示されること
    ③ ステップ3 の AIX0012C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 状態確認 Technology Level 0072 {#c01-i0742}
*分類: 導入と起動*  ・  難易度: 中級

夕映照合ではAIX 7.3の導入と起動で installp -C を確認します。夕映照合の導入と起動では Technology Level と代替ディスク状態を同じ証跡に残します。夕映照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。夕映照合の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、夕映照合を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 状態確認 Technology Level 0072を同一分類のentstat -d ent0 構成照合 Media Speed Runningと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はネットワークでentstat -d ent0を用い・Media Speed Runningである。
    - B. 構成を確認する際の意味は導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。 ✅
    - C. 構成を確認する際の意味はデバイス管理でlsattr -El hdisk0を用い・Available とデバイス一覧を確認する。
    - D. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。lsdev -Cc adapter 監査記録 Link Status固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でinstallp -Cを用い、Technology Level」に対応する項目はTechnology Level（状態・inst）です。状態に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、Technology」で、確認対象はin・状態です。構成・entsのA:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。性能・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は性能確認 Available（性能・lsat）です。監査・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、Technology」を指し、Technology Levelではin・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 状態確認 Technology Level 0072**

    - 検証目的: 導入と起動のinstallp -C 状態確認 Technology Level 0072について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認072-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0072A
    ```

    画面・出力には AIX0072A が表示され、installp -C 状態確認 Technology Level 0072 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0072B
    ```

    画面・出力には AIX0072B が表示され、installp -C 状態確認 Technology Level 0072 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0072C
    ```

    画面・出力には AIX0072C が表示され、installp -C 状態確認 Technology Level 0072 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0072A が画面・出力に表示されること
    ② ステップ2 の AIX0072B が画面・出力に表示されること
    ③ ステップ3 の AIX0072C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 監査記録 bootlist 0042 {#c01-i0743}
*分類: 導入と起動*  ・  難易度: 中級

春分照合ではAIX 7.3の導入と起動で installp -C を確認します。春分照合の導入と起動では bootlist とOSレベル表示を変更票へ記録します。春分照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春分照合の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、春分照合を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 監査記録 bootlist 0042の役割を調べています。entstat -d ent0 運用引継ぎ Gateway 0043の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはネットワークでentstat -d ent0を用い・Gateway とEthernet統計を確認する。
    - B. 機能の説明としては導入と起動でinstallp -Cを用い・bootlist とOSレベル表示を確認する。 ✅
    - C. 機能の説明としてはデバイス管理でlsdev -Cc diskを用い・attribute と構成マネージャー結果を確認する。
    - D. 機能の説明としてはネットワークでlsdev -Cc adapterを用い・Destinationである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でinstallp -Cを用い、bootlist」に対応する項目は監査記録 bootlist（監査・inst）です。導入と起動の仕様は「導入と起動でinstallp -Cを用い、bootlist」で、確認対象はin・監査です。運用引・entsのA:は「ネットワークでentstat -d ent0を用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・ents）です。変更前・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は変更前確認 attribute（変更・lsde）です。状態・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は状態確認 Destination（状態・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、bootlist」を指し、監査記録 bootlistではin・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 監査記録 bootlist 0042**

    - 検証目的: 導入と起動のinstallp -C 監査記録 bootlist 0042について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録042-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0042A
    ```

    画面・出力には AIX0042A が表示され、installp -C 監査記録 bootlist 0042 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0042B
    ```

    画面・出力には AIX0042B が表示され、installp -C 監査記録 bootlist 0042 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0042C
    ```

    画面・出力には AIX0042C が表示され、installp -C 監査記録 bootlist 0042 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0042A が画面・出力に表示されること
    ② ステップ2 の AIX0042B が画面・出力に表示されること
    ③ ステップ3 の AIX0042C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


