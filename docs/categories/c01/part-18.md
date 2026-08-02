# AIX 7.3 — 詳細 (18/18)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > 物理ボリューム

### lsps 一覧確認 メッセージ行 {#c01-i0907}
*分類: 物理ボリューム*  ・  難易度: 上級

AIX 7.3 の 物理ボリューム で扱う「lsps 一覧確認 メッセージ行」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを一覧確認の観点で確認する技術項目です。VG STATE 欄とpaging074を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsps 一覧確認 メッセージ行の役割を調べています。errpt 詳細確認 表形式の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはAIX エラーログから要約または詳細レポートを生成するコマンドである。
    - B. 機能の説明としてはネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。
    - C. 機能の説明としてはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 ✅
    - D. 機能の説明としてはJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は一覧確認 メッセージ行（一覧・lsps）です。物理ボリュームの仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・一覧・メッです。詳細・表形・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は詳細確認 表形式（詳細・errp）です。変更前・chdeのB:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。状態・lsfsのD:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・lsfs）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、一覧確認 メッセージ行ではls・一覧・メッに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsps 一覧確認 メッセージ行**

    - 検証目的: 物理ボリュームのlsps 一覧確認 メッセージ行について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には sys0 が含まれ、lsps 一覧確認 メッセージ行の証跡を確認できます。

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



### lsps 障害切り分け ファイルセット {#c01-i0908}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lsps 障害切り分け ファイルセット」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを障害切り分けの観点で確認する技術項目です。VG STATE 欄とpaging034を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsps 障害切り分け ファイルセットの役割を調べています。errpt 性能確認 チューニング値の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。
    - B. 障害切り分けに用いる役割はSRCとログでrefresh -s syslogdを用い・Subsystemである。
    - C. 障害切り分けに用いる役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。
    - D. 障害切り分けに用いる役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は障害切り分け ファイルセット（障害・lsps）です。物理ボリュームの仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・障害切です。性能・チュ・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は性能確認 チューニング値（性能・errp）です。起動・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は起動確認 Subsystem（起動・refr）です。運用引・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、障害切り分け ファイルセットではls・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsps 障害切り分け ファイルセット**

    - 検証目的: 物理ボリュームのlsps 障害切り分け ファイルセットについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には sys0 が含まれ、lsps 障害切り分け ファイルセットの証跡を確認できます。

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



### lsvg 性能確認 資料見出し {#c01-i0909}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lsvg 性能確認 資料見出し」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを性能確認の観点で確認する技術項目です。VG STATE 欄とpaging042を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsvg 性能確認 資料見出しの役割を調べています。lslv 変更前確認 運用記録の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - B. 表示や設定で扱う内容はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 ✅
    - C. 表示や設定で扱う内容はSRCとログでlssrc -s syslogdを用い・TIMESTAMP とsyslog設定変換を確認する。
    - D. 表示や設定で扱う内容はデバイス管理でlsmpio -l hdisk0を用い・path status とODM属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は性能確認 資料見出し（性能・lsvg）です。物理ボリュームの仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・性能・資料です。変更前・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は変更前確認 運用記録（変更・lslv）です。監査・lssrのC:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 TIMESTAMP（監査・lssr）です。変更後・lsmpのD:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（変更・lsmp）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、性能確認 資料見出しではls・性能・資料に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsvg 性能確認 資料見出し**

    - 検証目的: 物理ボリュームのlsvg 性能確認 資料見出しについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には Page が含まれ、lsvg 性能確認 資料見出しの証跡を確認できます。

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



### lsvg 詳細確認 詳細表示 {#c01-i0910}
*分類: 物理ボリューム*  ・  難易度: 初級

AIX 7.3 の 物理ボリューム で扱う「lsvg 詳細確認 詳細表示」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを詳細確認の観点で確認する技術項目です。VG STATE 欄とpaging002を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsvg 詳細確認 詳細表示の役割を調べています。lslv 状態判定 構成照合の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - B. 機能の説明としてはLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。chvg 構成照合 VG STATE 0228固有の属性も確認対象に含める。
    - C. 機能の説明としてはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 ✅
    - D. 機能の説明としては性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は詳細確認 詳細表示（詳細・lsvg）です。物理ボリュームの仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・詳細・詳細です。状態・構成・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は状態判定 構成照合（状態・lslv）です。構成・chvgのB:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（構成・chvg）です。属性・vmoのD:は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を述べ、対象は属性確認 pi（属性・vmo）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、詳細確認 詳細表示ではls・詳細・詳細に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsvg 詳細確認 詳細表示**

    - 検証目的: 物理ボリュームのlsvg 詳細確認 詳細表示について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には Page が含まれ、lsvg 詳細確認 詳細表示の証跡を確認できます。

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




## AIX 7.3 > 論理ボリューム

### chdev 一覧確認 一致条件 {#c01-i0911}
*分類: 論理ボリューム*  ・  難易度: 上級

AIX 7.3 の 論理ボリューム で扱う「chdev 一覧確認 一致条件」は、デバイス属性を変更する管理コマンドを一覧確認の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 067を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** chdev 一覧確認 一致条件について構成や状態を確認します。lscfg 詳細確認 除外条件ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は構成済みデバイスと VPD を表示するコマンドである。
    - B. 一次資料が示す主目的は性能管理でtopas -Cを用い・dxm とAME統計を確認する。
    - C. 一次資料が示す主目的はデバイス属性を変更する管理コマンドである。 ✅
    - D. 一次資料が示す主目的はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「デバイス属性を変更する管理コマンドである」に対応する項目は一覧確認 一致条件（一覧・chde）です。論理ボリュームの仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・一覧・一致です。詳細・除外・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は詳細確認 除外条件（詳細・lscf）です。運用引・topaのB:は「性能管理でtopas -Cを用い、dxm とAME統計を確認する」を述べ、対象は運用引継ぎ dxm（運用・topa）です。障害切・syslのD:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、一覧確認 一致条件ではch・一覧・一致に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **chdev 一覧確認 一致条件**

    - 検証目的: 論理ボリュームのchdev 一覧確認 一致条件について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には Page が含まれ、chdev 一覧確認 一致条件の証跡を確認できます。

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



### chdev 障害切り分け ボリューム状態 {#c01-i0912}
*分類: 論理ボリューム*  ・  難易度: 中級

AIX 7.3 の 論理ボリューム で扱う「chdev 障害切り分け ボリューム状態」は、デバイス属性を変更する管理コマンドを障害切り分けの観点で確認する技術項目です。LV STATE 欄とerrpt sequence 027を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** chdev 障害切り分け ボリューム状態について構成や状態を確認します。lscfg 性能確認 ページング状態ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは構成済みデバイスと VPD を表示するコマンドである。
    - B. 対象資源に対する働きはSRCとログでerrptを用い・IDENTIFIER とinetdデバッグ出力を確認する。
    - C. 対象資源に対する働きはデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。
    - D. 対象資源に対する働きはデバイス属性を変更する管理コマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「デバイス属性を変更する管理コマンドである」に対応する項目は障害切り分け ボリューム状態（障害・chde）です。論理ボリュームの仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・障害切です。性能・ペー・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は性能確認 ページング状態（性能・lscf）です。変更後・errpのB:は「SRCとログでerrptを用い、IDENTIFIER」を述べ、対象は変更後確認 IDENTIFIER（変更・errp）です。状態・odmgのC:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、障害切り分け ボリューム状態ではch・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **chdev 障害切り分け ボリューム状態**

    - 検証目的: 論理ボリュームのchdev 障害切り分け ボリューム状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には Page が含まれ、chdev 障害切り分け ボリューム状態の証跡を確認できます。

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



### errpt 性能確認 チューニング値 {#c01-i0913}
*分類: 論理ボリューム*  ・  難易度: 中級

AIX 7.3 の 論理ボリューム で扱う「errpt 性能確認 チューニング値」は、AIX エラーログから要約または詳細レポートを生成するコマンドを性能確認の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 035を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** errpt 性能確認 チューニング値について構成や状態を確認します。lsattr 変更前確認 パス状態ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはAIX エラーログから要約または詳細レポートを生成するコマンドである。 ✅
    - B. 状態を読み取るための働きはデバイスや sys0 などの属性値を表示するコマンドである。
    - C. 状態を読み取るための働きは導入と起動でemgr -lを用い・fileset level と起動デバイス設定を確認する。
    - D. 状態を読み取るための働きはLVMでlsvg -lを用い・PVID と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は性能確認 チューニング値（性能・errp）です。論理ボリュームの仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・性能・チュです。変更前・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は変更前確認 パス状態（変更・lsat）です。属性・emgrのC:は「導入と起動でemgr -lを用い、fileset level」を述べ、対象はfileset level（属性・emgr）です。容量・lsvgのD:は「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認す」を述べ、対象は容量確認 PVID（容量・lsvg）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、性能確認 チューニング値ではer・性能・チュに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **errpt 性能確認 チューニング値**

    - 検証目的: 論理ボリュームのerrpt 性能確認 チューニング値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
     r b avm fre csz cfr dxm ci co pi po in sy cs
    ```

    画面・出力には System が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lparstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
    %user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
    ```

    画面・出力には System が含まれ、errpt 性能確認 チューニング値の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> topas
    → Enter を押す
    ```

    画面・出力:
    ```text
    Topas Monitor for host: aixhost
    CPU User% Kern% Wait% Idle%
    AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
    ```

    画面・出力には Topas が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の System が画面・出力に表示されること
    ② ステップ2 の System が画面・出力に表示されること
    ③ ステップ3 の Topas が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### errpt 詳細確認 表形式 {#c01-i0914}
*分類: 論理ボリューム*  ・  難易度: 上級

AIX 7.3 の 論理ボリューム で扱う「errpt 詳細確認 表形式」は、AIX エラーログから要約または詳細レポートを生成するコマンドを詳細確認の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 075を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** errpt 詳細確認 表形式について構成や状態を確認します。lsattr 状態判定 ディスク状態ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはデバイスや sys0 などの属性値を表示するコマンドである。
    - B. 対象資源に対する働きは性能管理でiostat -Dl 2 2を用い・avm とAME統計を確認する。
    - C. 対象資源に対する働きはSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。
    - D. 対象資源に対する働きはAIX エラーログから要約または詳細レポートを生成するコマンドである。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は詳細確認 表形式（詳細・errp）です。論理ボリュームの仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・詳細・表形です。状態・ディ・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は状態判定 ディスク状態（状態・lsat）です。変更後・iostのB:は「性能管理でiostat -Dl 2 2を用い、avm」を述べ、対象は変更後確認 avm（変更・iost）です。構成・syslのC:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、詳細確認 表形式ではer・詳細・表形に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **errpt 詳細確認 表形式**

    - 検証目的: 論理ボリュームのerrpt 詳細確認 表形式について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
     r b avm fre csz cfr dxm ci co pi po in sy cs
    ```

    画面・出力には System が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lparstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
    %user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
    ```

    画面・出力には System が含まれ、errpt 詳細確認 表形式の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> topas
    → Enter を押す
    ```

    画面・出力:
    ```text
    Topas Monitor for host: aixhost
    CPU User% Kern% Wait% Idle%
    AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
    ```

    画面・出力には Topas が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の System が画面・出力に表示されること
    ② ステップ2 の System が画面・出力に表示されること
    ③ ステップ3 の Topas が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lslv 変更前確認 運用記録 {#c01-i0915}
*分類: 論理ボリューム*  ・  難易度: 中級

AIX 7.3 の 論理ボリューム で扱う「lslv 変更前確認 運用記録」は、論理ボリュームの属性と割り当て情報を表示するコマンドを変更前確認の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 043を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lslv 変更前確認 運用記録について構成や状態を確認します。lsps 復旧前確認 復旧手掛かりではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - B. 一次資料が示す主目的は論理ボリュームの属性と割り当て情報を表示するコマンドである。 ✅
    - C. 一次資料が示す主目的は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。
    - D. 一次資料が示す主目的はLVMでlspvを用い・STALE PARTITIONS と論理ボリューム配置を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は変更前確認 運用記録（変更・lslv）です。論理ボリュームの仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・変更前です。復旧前・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は復旧前確認 復旧手掛かり（復旧・lsps）です。運用引・lslpのC:は「導入と起動でlslpp -Lを用い、mksysb image」を述べ、対象はmksysb image（運用・lslp）です。障害切・lspvのD:は「LVMでlspvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（障害・lspv）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、変更前確認 運用記録ではls・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lslv 変更前確認 運用記録**

    - 検証目的: 論理ボリュームのlslv 変更前確認 運用記録について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt
    → Enter を押す
    ```

    画面・出力:
    ```text
    ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
    0E017ED1         0405131090 P H mem2           Memory failure
    ```

    画面・出力には ERROR が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt -a -N hdisk1
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: DISK_ERR4
    RESOURCE NAME: hdisk1
    Description
    DISK OPERATION ERROR
    ```

    画面・出力には LABEL が含まれ、lslv 変更前確認 運用記録の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> /usr/lib/errdemon -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    /var/adm/ras/errlog
    ```

    画面・出力には errlog が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
    ② ステップ2 の LABEL が画面・出力に表示されること
    ③ ステップ3 の errlog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lslv 状態判定 構成照合 {#c01-i0916}
*分類: 論理ボリューム*  ・  難易度: 初級

AIX 7.3 の 論理ボリューム で扱う「lslv 状態判定 構成照合」は、論理ボリュームの属性と割り当て情報を表示するコマンドを状態判定の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 003を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lslv 状態判定 構成照合について構成や状態を確認します。lsps 属性照合 属性確認ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - B. 対象資源に対する働きはJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。
    - C. 対象資源に対する働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 ✅
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は状態判定 構成照合（状態・lslv）です。論理ボリュームの仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・状態・構成です。属性・属性・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は属性照合 属性確認（属性・lsps）です。変更前・crfsのB:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・crfs）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、状態判定 構成照合ではls・状態・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lslv 状態判定 構成照合**

    - 検証目的: 論理ボリュームのlslv 状態判定 構成照合について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt
    → Enter を押す
    ```

    画面・出力:
    ```text
    ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
    0E017ED1         0405131090 P H mem2           Memory failure
    ```

    画面・出力には ERROR が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt -a -N hdisk1
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: DISK_ERR4
    RESOURCE NAME: hdisk1
    Description
    DISK OPERATION ERROR
    ```

    画面・出力には LABEL が含まれ、lslv 状態判定 構成照合の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> /usr/lib/errdemon -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    /var/adm/ras/errlog
    ```

    画面・出力には errlog が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
    ② ステップ2 の LABEL が画面・出力に表示されること
    ③ ステップ3 の errlog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lspv 属性照合 照合単位 {#c01-i0917}
*分類: 論理ボリューム*  ・  難易度: 初級

AIX 7.3 の 論理ボリューム で扱う「lspv 属性照合 照合単位」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを属性照合の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 011を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lspv 属性照合 照合単位について構成や状態を確認します。lsvg 障害切り分け 設定値ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - B. 状態を読み取るための働きはJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。
    - C. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 ✅
    - D. 状態を読み取るための働きはセキュリティでpwdck -n ALLを用い・authorizations とユーザー属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は属性照合 照合単位（属性・lspv）です。論理ボリュームの仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・属性・照合です。障害切・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は障害切り分け 設定値（障害・lsvg）です。起動・logfのB:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は起動確認 log=INLINE（起動・logf）です。容量・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は容量確認 authorization（容量・pwdc）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、属性照合 照合単位ではls・属性・照合に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lspv 属性照合 照合単位**

    - 検証目的: 論理ボリュームのlspv 属性照合 照合単位について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e11        rootvg          active
    hdisk1          00f6a1b2c3d5e11        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    VOLUME GROUP: rootvg
    VG STATE: active
    PP SIZE: 128 megabyte(s)
    TOTAL PPs: 1092
    ```

    画面・出力には VOLUME が含まれ、lspv 属性照合 照合単位の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg -l rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
    hd4                 jfs2       1     1     open/syncd    /
    ```

    画面・出力には NAME が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
    ② ステップ2 の VOLUME が画面・出力に表示されること
    ③ ステップ3 の NAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lspv 復旧前確認 状態確認 {#c01-i0918}
*分類: 論理ボリューム*  ・  難易度: 中級

AIX 7.3 の 論理ボリューム で扱う「lspv 復旧前確認 状態確認」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを復旧前確認の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 051を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lspv 復旧前確認 状態確認について構成や状態を確認します。lsvg 一覧確認 詳細表示ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - B. 対象資源に対する働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 ✅
    - C. 対象資源に対する働きはネットワークでcfgmgrを用い・Destination とMTU属性を確認する。cfgmgr 変更後確認 Destination 0277固有の属性も確認対象に含める。
    - D. 対象資源に対する働きはJFS2でlogformを用い・isnapshot とログデバイス設定を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は復旧前確認 状態確認（復旧・lspv）です。論理ボリュームの仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・復旧前です。一覧・詳細・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は一覧確認 詳細表示（一覧・lsvg）です。変更後・cfgmのC:は「ネットワークでcfgmgrを用い、Destination」を述べ、対象は変更後確認 Destination（変更・cfgm）です。状態・logfのD:は「JFS2でlogformを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・logf）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、復旧前確認 状態確認ではls・復旧前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lspv 復旧前確認 状態確認**

    - 検証目的: 論理ボリュームのlspv 復旧前確認 状態確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e51        rootvg          active
    hdisk1          00f6a1b2c3d5e51        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    VOLUME GROUP: rootvg
    VG STATE: active
    PP SIZE: 128 megabyte(s)
    TOTAL PPs: 1092
    ```

    画面・出力には VOLUME が含まれ、lspv 復旧前確認 状態確認の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg -l rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
    hd4                 jfs2       1     1     open/syncd    /
    ```

    画面・出力には NAME が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
    ② ステップ2 の VOLUME が画面・出力に表示されること
    ③ ステップ3 の NAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### vmstat 属性照合 イベント転送 {#c01-i0919}
*分類: 論理ボリューム*  ・  難易度: 中級

AIX 7.3 の 論理ボリューム で扱う「vmstat 属性照合 イベント転送」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを属性照合の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 019を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** vmstat 属性照合 イベント転送について構成や状態を確認します。lparstat 障害切り分け 受信先ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。
    - B. 一次資料が示す主目的はSRCとログでerrclearを用い・syslog.conf とinetdデバッグ出力を確認する。
    - C. 一次資料が示す主目的はデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。
    - D. 一次資料が示す主目的はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は属性照合 イベント転送（属性・vmst）です。論理ボリュームの仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・属性・イベです。障害切・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は障害切り分け 受信先（障害・lpar）です。運用引・errcのB:は「SRCとログでerrclearを用い、syslog.conf」を述べ、対象は運用引継ぎ syslog.conf（運用・errc）です。障害切・diagのC:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、属性照合 イベント転送ではvm・属性・イベに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **vmstat 属性照合 イベント転送**

    - 検証目的: 論理ボリュームのvmstat 属性照合 イベント転送について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には sys0 が含まれ、vmstat 属性照合 イベント転送の証跡を確認できます。

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



### vmstat 復旧前確認 出力見出し {#c01-i0920}
*分類: 論理ボリューム*  ・  難易度: 中級

AIX 7.3 の 論理ボリューム で扱う「vmstat 復旧前確認 出力見出し」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを復旧前確認の観点で確認する技術項目です。LV STATE 欄とerrpt sequence 059を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** vmstat 復旧前確認 出力見出しについて構成や状態を確認します。lparstat 一覧確認 保存場所ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。
    - B. 状態を読み取るための働きはネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。
    - C. 状態を読み取るための働きはJFS2でsnapを用い・log=INLINE とログデバイス設定を確認する。
    - D. 状態を読み取るための働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は復旧前確認 出力見出し（復旧・vmst）です。論理ボリュームの仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・復旧前です。一覧・保存・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は一覧確認 保存場所（一覧・lpar）です。属性・noのB:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。容量・snapのC:は「JFS2でsnapを用い、log=INLINE」を述べ、対象は容量確認 log=INLINE（容量・snap）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、復旧前確認 出力見出しではvm・復旧前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **vmstat 復旧前確認 出力見出し**

    - 検証目的: 論理ボリュームのvmstat 復旧前確認 出力見出しについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、論理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。LV STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には sys0 が含まれ、vmstat 復旧前確認 出力見出しの証跡を確認できます。

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


