---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (10/10)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > 性能管理

### vmstat -c 2 1 構成照合 csz 0240 {#c01-i0885}
*分類: 性能管理*  ・  難易度: 上級

青葉監査ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。青葉監査の性能管理では csz とtopasディスク表示を同じ証跡に残します。青葉監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。青葉監査の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、青葉監査を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 構成照合 csz 0240を同一分類のrbacqry -u user1 -T 変更後確認 audit class 0241と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。
    - B. 構成を確認する際の意味はJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味は論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - D. 構成を確認する際の意味は性能管理でvmstat -c 2 1を用い・csz とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でvmstat -c 2 1を用い、csz」に対応する項目は構成照合 csz（構成・vmst）です。構成に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、csz」で、確認対象はvm・構成です。変更後・rbacのA:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（変更・rbac）です。起動・crfsのB:は「JFS2でcrfsを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・crfs）です。性能・起動・lslvのC:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は性能確認 起動確認（性能・lslv）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、csz」を指し、構成照合 cszではvm・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 構成照合 csz 0240**

    - 検証目的: 性能管理のvmstat -c 2 1 構成照合 csz 0240について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合120-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0240A
    ```

    画面・出力には AIX0240A が表示され、vmstat -c 2 1 構成照合 csz 0240 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0240B
    ```

    画面・出力には AIX0240B が表示され、vmstat -c 2 1 構成照合 csz 0240 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0240C
    ```

    画面・出力には AIX0240C が表示され、vmstat -c 2 1 構成照合 csz 0240 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0240A が画面・出力に表示されること
    ② ステップ2 の AIX0240B が画面・出力に表示されること
    ③ ステップ3 の AIX0240C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 構成照合 fre 0180 {#c01-i0886}
*分類: 性能管理*  ・  難易度: 中級

薄明判定ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。薄明判定の性能管理では fre とtopasディスク表示を同じ証跡に残します。薄明判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。薄明判定の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、薄明判定を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 構成照合 fre 0180の技術的な意味を資料で確認するとき、rolelist -u user1 変更前確認 roles 0181との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はセキュリティでrolelist -u user1を用い・roles と監査設定を確認する。
    - B. 構成を確認する際の意味はJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味は性能管理でvmstat -c 2 1を用い・fre とtopasディスク表示を確認する。 ✅
    - D. 構成を確認する際の意味はセキュリティでusrck -n ALLを用い・audit class と監査設定を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmstat -c 2 1を用い、fre」に対応する項目は構成照合 fre（構成・vmst）です。構成に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、fre」で、確認対象はvm・構成です。変更前・roleのA:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は変更前確認 roles（変更・role）です。起動・crfsのB:は「JFS2でcrfsを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・crfs）です。運用引・usrcのD:は「セキュリティでusrck -n ALLを用い、audit」を述べ、対象はaudit class（運用・usrc）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、fre」を指し、構成照合 freではvm・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 構成照合 fre 0180**

    - 検証目的: 性能管理のvmstat -c 2 1 構成照合 fre 0180について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合060-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0180A
    ```

    画面・出力には AIX0180A が表示され、vmstat -c 2 1 構成照合 fre 0180 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0180B
    ```

    画面・出力には AIX0180B が表示され、vmstat -c 2 1 構成照合 fre 0180 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0180C
    ```

    画面・出力には AIX0180C が表示され、vmstat -c 2 1 構成照合 fre 0180 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0180A が画面・出力に表示されること
    ② ステップ2 の AIX0180B が画面・出力に表示されること
    ③ ステップ3 の AIX0180C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 構成照合 po 0716 {#c01-i0887}
*分類: 性能管理*  ・  難易度: 上級

若潮保守ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。若潮保守の性能管理では po とtopasディスク表示を引継ぎ票へ保管します。若潮保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若潮保守の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、若潮保守を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 構成照合 po 0716の技術的な意味を資料で確認するとき、rolelist -u user1 変更前確認 user attributesとの境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でvmstat -c 2 1を用い・po とtopasディスク表示を確認する。 ✅
    - B. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。
    - C. コマンドまたは機能の用途はSRCとログでrefresh -s syslogdを用い・IDENTIFIERである。
    - D. コマンドまたは機能の用途はLVMでlsvg -lを用い・STALE PARTITIONS とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、po とtopasディスク表示を確認する」に対応する項目は構成照合 po（構成・vmst）です。構成に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、po」で、確認対象はvm・構成です。変更前・roleのB:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。監査・refrのC:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は監査記録 IDENTIFIER（監査・refr）です。障害切・lsvgのD:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（障害・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、po」を指し、構成照合 poではvm・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 構成照合 po 0716**

    - 検証目的: 性能管理のvmstat -c 2 1 構成照合 po 0716について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合116-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0716A
    ```

    画面・出力には AIX0716A が表示され、vmstat -c 2 1 構成照合 po 0716 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0716B
    ```

    画面・出力には AIX0716B が表示され、vmstat -c 2 1 構成照合 po 0716 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0716C
    ```

    画面・出力には AIX0716C が表示され、vmstat -c 2 1 構成照合 po 0716 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0716A が画面・出力に表示されること
    ② ステップ2 の AIX0716B が画面・出力に表示されること
    ③ ステップ3 の AIX0716C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 運用引継ぎ Busy% 0686 {#c01-i0888}
*分類: 性能管理*  ・  難易度: 中級

朝凪保守ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。朝凪保守の性能管理では Busy% とvmstat表示を確認票へ整理します。朝凪保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。朝凪保守の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、朝凪保守を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 運用引継ぎ Busy% 0686に関する障害切り分けの前提を確認しています。rolelist -u user1 容量確認 user attributesの機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・user attributesである。
    - B. 障害切り分けに用いる役割は導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。
    - C. 障害切り分けに用いる役割はLVMでlsvg -lを用い・VG STATE とボリュームグループ属性を確認する。
    - D. 障害切り分けに用いる役割は性能管理でvmstat -c 2 1を用い・Busy% とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmstat -c 2 1を用い、Busy% とvmstat表示を確認する」に対応する項目は運用引継ぎ Busy%（運用・vmst）です。運用引に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、Busy%」で、確認対象はvm・運用引です。容量・roleのA:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（容量・role）です。状態・instのB:は「導入と起動でinstallp -Cを用い、Technology」を述べ、対象はTechnology Level（状態・inst）です。起動・lsvgのC:は「LVMでlsvg -lを用い、VG STATE」を述べ、対象はVG STATE（起動・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、Busy%」を指し、運用引継ぎ Busy%ではvm・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 運用引継ぎ Busy% 0686**

    - 検証目的: 性能管理のvmstat -c 2 1 運用引継ぎ Busy% 0686について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ086-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0686A
    ```

    画面・出力には AIX0686A が表示され、vmstat -c 2 1 運用引継ぎ Busy% 0686 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0686B
    ```

    画面・出力には AIX0686B が表示され、vmstat -c 2 1 運用引継ぎ Busy% 0686 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0686C
    ```

    画面・出力には AIX0686C が表示され、vmstat -c 2 1 運用引継ぎ Busy% 0686 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0686A が画面・出力に表示されること
    ② ステップ2 の AIX0686B が画面・出力に表示されること
    ③ ステップ3 の AIX0686C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 運用引継ぎ PhysB 0210 {#c01-i0889}
*分類: 性能管理*  ・  難易度: 中級

桜雲保守ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。桜雲保守の性能管理では PhysB とvmstat表示を変更票へ記録します。桜雲保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。桜雲保守の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、桜雲保守を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 運用引継ぎ PhysB 0210の役割を調べています。rolelist -u user1 容量確認 roles 0211の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては性能管理でvmstat -c 2 1を用い・PhysB とvmstat表示を確認する。 ✅
    - B. 機能の説明としてはセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。
    - C. 機能の説明としてはJFS2でcrfsを用い・lff とログデバイス設定を確認する。
    - D. 機能の説明としてはセキュリティでusrck -n ALLを用い・audit class とロール一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、PhysB とvmstat表示を確認する」に対応する項目は運用引継ぎ PhysB（運用・vmst）です。運用引に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、PhysB」で、確認対象はvm・運用引です。容量・roleのB:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。障害切・crfsのC:は「JFS2でcrfsを用い、lff とログデバイス設定を確認する」を述べ、対象は障害切り分け lff（障害・crfs）です。構成・usrcのD:は「セキュリティでusrck -n ALLを用い、audit」を述べ、対象はaudit class（構成・usrc）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、PhysB」を指し、運用引継ぎ PhysBではvm・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 運用引継ぎ PhysB 0210**

    - 検証目的: 性能管理のvmstat -c 2 1 運用引継ぎ PhysB 0210について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ090-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0210A
    ```

    画面・出力には AIX0210A が表示され、vmstat -c 2 1 運用引継ぎ PhysB 0210 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0210B
    ```

    画面・出力には AIX0210B が表示され、vmstat -c 2 1 運用引継ぎ PhysB 0210 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0210C
    ```

    画面・出力には AIX0210C が表示され、vmstat -c 2 1 運用引継ぎ PhysB 0210 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0210A が画面・出力に表示されること
    ② ステップ2 の AIX0210B が画面・出力に表示されること
    ③ ステップ3 の AIX0210C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 運用引継ぎ csz 0150 {#c01-i0890}
*分類: 性能管理*  ・  難易度: 中級

早苗採取ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。早苗採取の性能管理では csz とvmstat表示を変更票へ記録します。早苗採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。早苗採取の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、早苗採取を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 運用引継ぎ csz 0150に関する障害切り分けの前提を確認しています。rolelist -u user1 容量確認 roles 0151の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては性能管理でvmstat -c 2 1を用い・csz とvmstat表示を確認する。 ✅
    - B. 機能の説明としてはセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。
    - C. 機能の説明としてはJFS2でdefragfsを用い・mountguard とログデバイス設定を確認する。
    - D. 機能の説明としてはセキュリティでusrck -n ALLを用い・audit class とロール一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、csz とvmstat表示を確認する」に対応する項目は運用引継ぎ csz（運用・vmst）です。運用引に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、csz」で、確認対象はvm・運用引です。容量・roleのB:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。変更後・defrのC:は「JFS2でdefragfsを用い、mountguard」を述べ、対象は変更後確認 mountguard（変更・defr）です。構成・usrcのD:は「セキュリティでusrck -n ALLを用い、audit」を述べ、対象はaudit class（構成・usrc）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、csz」を指し、運用引継ぎ cszではvm・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 運用引継ぎ csz 0150**

    - 検証目的: 性能管理のvmstat -c 2 1 運用引継ぎ csz 0150について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ030-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0150A
    ```

    画面・出力には AIX0150A が表示され、vmstat -c 2 1 運用引継ぎ csz 0150 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0150B
    ```

    画面・出力には AIX0150B が表示され、vmstat -c 2 1 運用引継ぎ csz 0150 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0150C
    ```

    画面・出力には AIX0150C が表示され、vmstat -c 2 1 運用引継ぎ csz 0150 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0150A が画面・出力に表示されること
    ② ステップ2 の AIX0150B が画面・出力に表示されること
    ③ ステップ3 の AIX0150C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 運用引継ぎ po 0626 {#c01-i0891}
*分類: 性能管理*  ・  難易度: 中級

陽炎採取ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。陽炎採取の性能管理では po とvmstat表示を確認票へ整理します。陽炎採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。陽炎採取の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、陽炎採取を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 運用引継ぎ po 0626の役割を調べています。rolelist -u user1 容量確認 user attributesの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・user attributesである。
    - B. 障害切り分けに用いる役割は導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。
    - C. 障害切り分けに用いる役割は性能管理でvmstat -c 2 1を用い・po とvmstat表示を確認する。 ✅
    - D. 障害切り分けに用いる役割はLVMでlsvgを用い・PVID とボリュームグループ属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmstat -c 2 1を用い、po とvmstat表示を確認する」に対応する項目は運用引継ぎ po（運用・vmst）です。運用引に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、po」で、確認対象はvm・運用引です。容量・roleのA:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（容量・role）です。状態・instのB:は「導入と起動でinstallp -Cを用い、Technology」を述べ、対象はTechnology Level（状態・inst）です。性能・lsvgのD:は「LVMでlsvgを用い、PVID とボリュームグループ属性を確認する」を述べ、対象は性能確認 PVID（性能・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、po」を指し、運用引継ぎ poではvm・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 運用引継ぎ po 0626**

    - 検証目的: 性能管理のvmstat -c 2 1 運用引継ぎ po 0626について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ026-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0626A
    ```

    画面・出力には AIX0626A が表示され、vmstat -c 2 1 運用引継ぎ po 0626 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0626B
    ```

    画面・出力には AIX0626B が表示され、vmstat -c 2 1 運用引継ぎ po 0626 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0626C
    ```

    画面・出力には AIX0626C が表示され、vmstat -c 2 1 運用引継ぎ po 0626 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0626A が画面・出力に表示されること
    ② ステップ2 の AIX0626B が画面・出力に表示されること
    ③ ステップ3 の AIX0626C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 変更前確認 avm 0407 {#c01-i0892}
*分類: 性能管理*  ・  難易度: 中級

夕凪評価ではAIX 7.3の性能管理で vmstat 2 2 を確認します。夕凪評価の性能管理では avm とsvmon全体表示を照合票へ整理します。夕凪評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。夕凪評価の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、夕凪評価を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 変更前確認 avm 0407の設定や表示を読む前に役割を確認します。lsrole 変更後確認 roles 0408ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はセキュリティでlsroleを用い・roles とユーザー属性を確認する。
    - B. 一次資料が示す主目的は性能管理でvmstat 2 2を用い・avm とsvmon全体表示を確認する。 ✅
    - C. 一次資料が示す主目的はJFS2でlogformを用い・isnapshot とマウントオプションを確認する。
    - D. 一次資料が示す主目的はLVMでlspvを用い・LV STATE と論理ボリューム配置を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmstat 2 2を用い、avm とsvmon全体表示を確認する」に対応する項目は変更前確認 avm（変更・vmst）です。変更前に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、avm」で、確認対象はvm・変更前です。変更後・lsroのA:は「セキュリティでlsroleを用い、roles」を述べ、対象は変更後確認 roles（変更・lsro）です。起動・logfのC:は「JFS2でlogformを用い、isnapshot」を述べ、対象は起動確認 isnapshot（起動・logf）です。障害切・lspvのD:は「LVMでlspvを用い、LV STATE」を述べ、対象はLV STATE（障害・lspv）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、avm」を指し、変更前確認 avmではvm・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 変更前確認 avm 0407**

    - 検証目的: 性能管理のvmstat 2 2 変更前確認 avm 0407について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認047-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0407A
    ```

    画面・出力には AIX0407A が表示され、vmstat 2 2 変更前確認 avm 0407 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0407B
    ```

    画面・出力には AIX0407B が表示され、vmstat 2 2 変更前確認 avm 0407 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0407C
    ```

    画面・出力には AIX0407C が表示され、vmstat 2 2 変更前確認 avm 0407 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0407A が画面・出力に表示されること
    ② ステップ2 の AIX0407B が画面・出力に表示されること
    ③ ステップ3 の AIX0407C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 変更前確認 po 0467 {#c01-i0893}
*分類: 性能管理*  ・  難易度: 上級

風花整理ではAIX 7.3の性能管理で vmstat 2 2 を確認します。風花整理の性能管理では po とsvmon全体表示を照合票へ整理します。風花整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。風花整理の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、風花整理を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 変更前確認 po 0467について構成や状態を確認します。lsrole 変更後確認 roles 0468ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は性能管理でvmstat 2 2を用い・po とsvmon全体表示を確認する。 ✅
    - B. 一次資料が示す主目的はセキュリティでlsroleを用い・roles とユーザー属性を確認する。
    - C. 一次資料が示す主目的はJFS2でdefragfsを用い・mountguard とマウントオプションを確認する。
    - D. 一次資料が示す主目的はLVMでlsvgを用い・PP SIZE と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「性能管理でvmstat 2 2を用い、po とsvmon全体表示を確認する」に対応する項目は変更前確認 po（変更・vmst）です。変更前に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、po」で、確認対象はvm・変更前です。変更後・lsroのB:は「セキュリティでlsroleを用い、roles」を述べ、対象は変更後確認 roles（変更・lsro）です。属性・defrのC:は「JFS2でdefragfsを用い、mountguard」を述べ、対象は属性確認 mountguard（属性・defr）です。バック・lsvgのD:は「LVMでlsvgを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（バッ・lsvg）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、po」を指し、変更前確認 poではvm・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 変更前確認 po 0467**

    - 検証目的: 性能管理のvmstat 2 2 変更前確認 po 0467について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認107-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0467A
    ```

    画面・出力には AIX0467A が表示され、vmstat 2 2 変更前確認 po 0467 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0467B
    ```

    画面・出力には AIX0467B が表示され、vmstat 2 2 変更前確認 po 0467 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0467C
    ```

    画面・出力には AIX0467C が表示され、vmstat 2 2 変更前確認 po 0467 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0467A が画面・出力に表示されること
    ② ステップ2 の AIX0467B が画面・出力に表示されること
    ③ ステップ3 の AIX0467C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 容量確認 Busy% 0437 {#c01-i0894}
*分類: 性能管理*  ・  難易度: 中級

冬晴評価ではAIX 7.3の性能管理で vmstat 2 2 を確認します。冬晴評価の性能管理では Busy% とAME統計を復旧票へ残します。冬晴評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。冬晴評価の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、冬晴評価を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 容量確認 Busy% 0437を保守記録に説明する必要があります。lsrole 性能確認 roles 0438と取り違えない説明はどれですか。

    - A. 仕様上の役割はセキュリティでlsroleを用い・roles とRBAC属性を確認する。
    - B. 仕様上の役割はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。
    - C. 仕様上の役割はLVMでlsvgを用い・PVID と物理ボリューム一覧を確認する。
    - D. 仕様上の役割は性能管理でvmstat 2 2を用い・Busy% とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmstat 2 2を用い、Busy% とAME統計を確認する」に対応する項目は容量確認 Busy%（容量・vmst）です。容量に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、Busy%」で、確認対象はvm・容量です。性能・lsroのA:は「セキュリティでlsroleを用い、roles」を述べ、対象は性能確認 roles（性能・lsro）です。バック・defrのB:は「JFS2でdefragfsを用い、log=INLINE」を述べ、対象はバックアウト確認 log=INLIN（バッ・defr）です。属性・lsvgのC:は「LVMでlsvgを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は属性確認 PVID（属性・lsvg）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、Busy%」を指し、容量確認 Busy%ではvm・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 容量確認 Busy% 0437**

    - 検証目的: 性能管理のvmstat 2 2 容量確認 Busy% 0437について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認077-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0437A
    ```

    画面・出力には AIX0437A が表示され、vmstat 2 2 容量確認 Busy% 0437 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0437B
    ```

    画面・出力には AIX0437B が表示され、vmstat 2 2 容量確認 Busy% 0437 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0437C
    ```

    画面・出力には AIX0437C が表示され、vmstat 2 2 容量確認 Busy% 0437 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0437A が画面・出力に表示されること
    ② ステップ2 の AIX0437B が画面・出力に表示されること
    ③ ステップ3 の AIX0437C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 起動確認 Entitled Capacity 0724 {#c01-i0895}
*分類: 性能管理*  ・  難易度: 初級

若草監査ではAIX 7.3の性能管理で vmstat 2 2 を確認します。若草監査の性能管理では Entitled Capacity とtopasディスク表示を監査票へ転記します。若草監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若草監査の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、若草監査を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 起動確認 Entitled Capacity 0724の技術的な意味を資料で確認するとき、lsrole 属性確認 user attributes 0725との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でvmstat 2 2を用い・Entitled Capacity とtopasディスク表示を確認する。 ✅
    - B. 管理対象との関係を表す説明はセキュリティでlsroleを用い・user attributes と監査設定を確認する。
    - C. 管理対象との関係を表す説明は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。oslevel -s 変更前確認 fileset level 0110固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明はLVMでlspvを用い・LV STATE とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でvmstat 2 2を用い、Entitled Capacity」に対応する項目はEntitled Capacity（起動・vmst）です。起動に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、Entitled」で、確認対象はvm・起動です。属性・lsroのB:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（属性・lsro）です。変更前・osleのC:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（変更・osle）です。状態・lspvのD:は「LVMでlspvを用い、LV STATE」を述べ、対象はLV STATE（状態・lspv）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、Entitled」を指し、Entitled Capacityではvm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 起動確認 Entitled Capacity 0724**

    - 検証目的: 性能管理のvmstat 2 2 起動確認 Entitled Capacity 0724について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認004-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0724A
    ```

    画面・出力には AIX0724A が表示され、vmstat 2 2 起動確認 Entitled Capacity 0724 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0724B
    ```

    画面・出力には AIX0724B が表示され、vmstat 2 2 起動確認 Entitled Capacity 0724 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0724C
    ```

    画面・出力には AIX0724C が表示され、vmstat 2 2 起動確認 Entitled Capacity 0724 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0724A が画面・出力に表示されること
    ② ステップ2 の AIX0724B が画面・出力に表示されること
    ③ ステップ3 の AIX0724C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 起動確認 avm 0248 {#c01-i0896}
*分類: 性能管理*  ・  難易度: 初級

翠風監査ではAIX 7.3の性能管理で vmstat 2 2 を確認します。翠風監査の性能管理では avm とtopasディスク表示を引継ぎ票へ保管します。翠風監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。翠風監査の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、翠風監査を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 起動確認 avm 0248を同一分類のlsrole 属性確認 roles 0249と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はセキュリティでlsroleを用い・roles と監査設定を確認する。
    - B. コマンドまたは機能の用途はJFS2でlogformを用い・ファイルシステム使用率 とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途は性能管理でvmstat 2 2を用い・avm とtopasディスク表示を確認する。 ✅
    - D. コマンドまたは機能の用途は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「性能管理でvmstat 2 2を用い、avm とtopasディスク表示を確認する」に対応する項目は起動確認 avm（起動・vmst）です。起動に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、avm」で、確認対象はvm・起動です。属性・lsroのA:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。監査・ファ・logfのB:は「JFS2でlogformを用い、ファイルシステム使用率」を述べ、対象は監査記録 ファイルシステム使用率（監査・logf）です。変更前・lspvのD:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は変更前確認 保持設定（変更・lspv）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、avm」を指し、起動確認 avmではvm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 起動確認 avm 0248**

    - 検証目的: 性能管理のvmstat 2 2 起動確認 avm 0248について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認008-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0248A
    ```

    画面・出力には AIX0248A が表示され、vmstat 2 2 起動確認 avm 0248 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0248B
    ```

    画面・出力には AIX0248B が表示され、vmstat 2 2 起動確認 avm 0248 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0248C
    ```

    画面・出力には AIX0248C が表示され、vmstat 2 2 起動確認 avm 0248 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0248A が画面・出力に表示されること
    ② ステップ2 の AIX0248B が画面・出力に表示されること
    ③ ステップ3 の AIX0248C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 起動確認 pi 0784 {#c01-i0897}
*分類: 性能管理*  ・  難易度: 中級

霜月復旧ではAIX 7.3の性能管理で vmstat 2 2 を確認します。霜月復旧の性能管理では pi とtopasディスク表示を監査票へ転記します。霜月復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。霜月復旧の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、霜月復旧を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 起動確認 pi 0784を同一分類のsplitcopy 構成照合 lff 0811と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・lff と内部スナップショットを確認する。
    - B. 管理対象との関係を表す説明は性能管理でvmstat 2 2を用い・pi とtopasディスク表示を確認する。 ✅
    - C. 管理対象との関係を表す説明は導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。
    - D. 管理対象との関係を表す説明はLVMでchvgを用い・STALE PARTITIONS とボリュームグループ属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** 起動・vmstでBの記述「性能管理でvmstat 2 2を用い、pi」に対応する項目は起動確認 pi（起動・vmst）です。起動に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、pi」で、確認対象はvm・起動です。構成・spliのA:は「JFS2でsplitcopyを用い、lff」を述べ、対象は構成照合 lff（構成・spli）です。容量・bootのC:は「導入と起動でbootlist -m normalを用い」を述べ、対象はmksysb image（容量・boot）です。変更後・chvgのD:は「LVMでchvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・chvg）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、pi」を指し、起動確認 piではvm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 起動確認 pi 0784**

    - 検証目的: 性能管理のvmstat 2 2 起動確認 pi 0784について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認064-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0784A
    ```

    画面・出力には AIX0784A が表示され、vmstat 2 2 起動確認 pi 0784 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0784B
    ```

    画面・出力には AIX0784B が表示され、vmstat 2 2 起動確認 pi 0784 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0784C
    ```

    画面・出力には AIX0784C が表示され、vmstat 2 2 起動確認 pi 0784 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0784A が画面・出力に表示されること
    ② ステップ2 の AIX0784B が画面・出力に表示されること
    ③ ステップ3 の AIX0784C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 起動確認 po 0308 {#c01-i0898}
*分類: 性能管理*  ・  難易度: 中級

雪解復旧ではAIX 7.3の性能管理で vmstat 2 2 を確認します。雪解復旧の性能管理では po とtopasディスク表示を引継ぎ票へ保管します。雪解復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。雪解復旧の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、雪解復旧を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 起動確認 po 0308の技術的な意味を資料で確認するとき、lsrole 属性確認 roles 0309との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はセキュリティでlsroleを用い・roles と監査設定を確認する。
    - B. コマンドまたは機能の用途はJFS2でdefragfsを用い・log=INLINE とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途はLVMでlsvgを用い・VG STATE とミラーコピー状態を確認する。
    - D. コマンドまたは機能の用途は性能管理でvmstat 2 2を用い・po とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmstat 2 2を用い、po とtopasディスク表示を確認する」に対応する項目は起動確認 po（起動・vmst）です。起動に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、po」で、確認対象はvm・起動です。属性・lsroのA:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。運用引・defrのB:は「JFS2でdefragfsを用い、log=INLINE」を述べ、対象は運用引継ぎ log=INLINE（運用・defr）です。構成・lsvgのC:は「LVMでlsvgを用い、VG STATE」を述べ、対象はVG STATE（構成・lsvg）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、po」を指し、起動確認 poではvm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 起動確認 po 0308**

    - 検証目的: 性能管理のvmstat 2 2 起動確認 po 0308について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認068-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0308A
    ```

    画面・出力には AIX0308A が表示され、vmstat 2 2 起動確認 po 0308 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0308B
    ```

    画面・出力には AIX0308B が表示され、vmstat 2 2 起動確認 po 0308 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0308C
    ```

    画面・出力には AIX0308C が表示され、vmstat 2 2 起動確認 po 0308 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0308A が画面・出力に表示されること
    ② ステップ2 の AIX0308B が画面・出力に表示されること
    ③ ステップ3 の AIX0308C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 障害切り分け Busy% 0278 {#c01-i0899}
*分類: 性能管理*  ・  難易度: 中級

春霞監査ではAIX 7.3の性能管理で vmstat 2 2 を確認します。春霞監査の性能管理では Busy% とvmstat表示を確認票へ整理します。春霞監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春霞監査の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、春霞監査を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 障害切り分け Busy% 0278に関する障害切り分けの前提を確認しています。lsrole バックアウト確認 roles 0279の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでlsroleを用い・roles とロール一覧を確認する。
    - B. 障害切り分けに用いる役割はJFS2でlogformを用い・isnapshot とログデバイス設定を確認する。
    - C. 障害切り分けに用いる役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - D. 障害切り分けに用いる役割は性能管理でvmstat 2 2を用い・Busy% とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmstat 2 2を用い、Busy% とvmstat表示を確認する」に対応する項目は障害切り分け Busy%（障害・vmst）です。障害切に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、Busy%」で、確認対象はvm・障害切です。バック・lsroのA:は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を述べ、対象はバックアウト確認 roles（バッ・lsro）です。状態・logfのB:は「JFS2でlogformを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・logf）です。復旧前・lspvのC:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は復旧前確認 状態確認（復旧・lspv）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、Busy%」を指し、障害切り分け Busy%ではvm・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 障害切り分け Busy% 0278**

    - 検証目的: 性能管理のvmstat 2 2 障害切り分け Busy% 0278について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け038-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0278A
    ```

    画面・出力には AIX0278A が表示され、vmstat 2 2 障害切り分け Busy% 0278 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0278B
    ```

    画面・出力には AIX0278B が表示され、vmstat 2 2 障害切り分け Busy% 0278 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0278C
    ```

    画面・出力には AIX0278C が表示され、vmstat 2 2 障害切り分け Busy% 0278 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0278A が画面・出力に表示されること
    ② ステップ2 の AIX0278B が画面・出力に表示されること
    ③ ステップ3 の AIX0278C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat 2 2 障害切り分け dxm 0754 {#c01-i0900}
*分類: 性能管理*  ・  難易度: 中級

銀嶺監査ではAIX 7.3の性能管理で vmstat 2 2 を確認します。銀嶺監査の性能管理では dxm とvmstat表示を保守票へ記録します。銀嶺監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。銀嶺監査の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、銀嶺監査を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat 2 2 障害切り分け dxm 0754の役割を調べています。lsrole バックアウト確認 user attributes 0755の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はセキュリティでlsroleを用い・user attributes とロール一覧を確認する。
    - B. 表示や設定で扱う内容は性能管理でvmstat 2 2を用い・dxm とvmstat表示を確認する。 ✅
    - C. 表示や設定で扱う内容は導入と起動でlslpp -Lを用い・mksysb image と代替ディスク状態を確認する。
    - D. 表示や設定で扱う内容はLVMでlspvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmstat 2 2を用い、dxm とvmstat表示を確認する」に対応する項目は障害切り分け dxm（障害・vmst）です。障害切に関する性能管理の仕様は「性能管理でvmstat 2 2を用い、dxm」で、確認対象はvm・障害切です。バック・lsroのA:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（バッ・lsro）です。性能・lslpのC:は「導入と起動でlslpp -Lを用い、mksysb image」を述べ、対象はmksysb image（性能・lslp）です。監査・lspvのD:は「LVMでlspvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（監査・lspv）です。「vmstat 2 2」は「性能管理でvmstat 2 2を用い、dxm」を指し、障害切り分け dxmではvm・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat 2 2 障害切り分け dxm 0754**

    - 検証目的: 性能管理のvmstat 2 2 障害切り分け dxm 0754について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け034-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0754A
    ```

    画面・出力には AIX0754A が表示され、vmstat 2 2 障害切り分け dxm 0754 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0754B
    ```

    画面・出力には AIX0754B が表示され、vmstat 2 2 障害切り分け dxm 0754 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0754C
    ```

    画面・出力には AIX0754C が表示され、vmstat 2 2 障害切り分け dxm 0754 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0754A が画面・出力に表示されること
    ② ステップ2 の AIX0754B が画面・出力に表示されること
    ③ ステップ3 の AIX0754C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en




## AIX 7.3 > 物理ボリューム

### lparstat 性能確認 警告行 {#c01-i0901}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lparstat 性能確認 警告行」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを性能確認の観点で確認する技術項目です。VG STATE 欄とpaging050を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lparstat 性能確認 警告行の役割を調べています。lspv 復旧前確認 状態確認の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 ✅
    - B. 機能の説明としては物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - C. 機能の説明としては導入と起動でbootlist -m normalを用い・EFIX LABEL と代替ディスク状態を確認する。
    - D. 機能の説明としてはLVMでmigratepvを用い・LV STATE とボリュームグループ属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は性能確認 警告行（性能・lpar）です。物理ボリュームの仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・性能・警告です。復旧前・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は復旧前確認 状態確認（復旧・lspv）です。変更前・bootのC:は「導入と起動でbootlist -m normalを用い、EFIX」を述べ、対象はEFIX LABEL（変更・boot）です。属性・migrのD:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（属性・migr）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、性能確認 警告行ではlp・性能・警告に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lparstat 性能確認 警告行**

    - 検証目的: 物理ボリュームのlparstat 性能確認 警告行について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には System が含まれ、lparstat 性能確認 警告行の証跡を確認できます。

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



### lparstat 詳細確認 保存場所 {#c01-i0902}
*分類: 物理ボリューム*  ・  難易度: 初級

AIX 7.3 の 物理ボリューム で扱う「lparstat 詳細確認 保存場所」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを詳細確認の観点で確認する技術項目です。VG STATE 欄とpaging010を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lparstat 詳細確認 保存場所の役割を調べています。lspv 属性照合 照合単位の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - B. 障害切り分けに用いる役割はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。
    - C. 障害切り分けに用いる役割は性能管理でfilemonを用い・Busy% とsvmon全体表示を確認する。
    - D. 障害切り分けに用いる役割はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は詳細確認 保存場所（詳細・lpar）です。物理ボリュームの仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・詳細・保存です。属性・照合・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は属性照合 照合単位（属性・lspv）です。性能・migrのB:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・migr）です。運用引・fileのC:は「性能管理でfilemonを用い、Busy%」を述べ、対象は運用引継ぎ Busy%（運用・file）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、詳細確認 保存場所ではlp・詳細・保存に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lparstat 詳細確認 保存場所**

    - 検証目的: 物理ボリュームのlparstat 詳細確認 保存場所について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には System が含まれ、lparstat 詳細確認 保存場所の証跡を確認できます。

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



### lsattr 属性照合 ディスク状態 {#c01-i0903}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lsattr 属性照合 ディスク状態」は、デバイスや sys0 などの属性値を表示するコマンドを属性照合の観点で確認する技術項目です。VG STATE 欄とpaging026を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsattr 属性照合 ディスク状態の役割を調べています。chdev 障害切り分け ボリューム状態の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはデバイスや sys0 などの属性値を表示するコマンドである。 ✅
    - B. 機能の説明としてはデバイス属性を変更する管理コマンドである。
    - C. 機能の説明としてはJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。
    - D. 機能の説明としてはセキュリティでrbacqry -u user1 -Tを用い・user attributesである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は属性照合 ディスク状態（属性・lsat）です。物理ボリュームの仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・属性・ディです。障害切・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。変更前・fsckのC:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。属性・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はuser attributes（属性・rbac）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、属性照合 ディスク状態ではls・属性・ディに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsattr 属性照合 ディスク状態**

    - 検証目的: 物理ボリュームのlsattr 属性照合 ディスク状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e26        rootvg          active
    hdisk1          00f6a1b2c3d5e26        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には VOLUME が含まれ、lsattr 属性照合 ディスク状態の証跡を確認できます。

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



### lsattr 復旧前確認 対象ファイル {#c01-i0904}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lsattr 復旧前確認 対象ファイル」は、デバイスや sys0 などの属性値を表示するコマンドを復旧前確認の観点で確認する技術項目です。VG STATE 欄とpaging066を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsattr 復旧前確認 対象ファイルの役割を調べています。chdev 一覧確認 一致条件の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はデバイス属性を変更する管理コマンドである。
    - B. 表示や設定で扱う内容はネットワークでnetstat -rnを用い・Gateway と経路表を確認する。
    - C. 表示や設定で扱う内容はデバイスや sys0 などの属性値を表示するコマンドである。 ✅
    - D. 表示や設定で扱う内容はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は復旧前確認 対象ファイル（復旧・lsat）です。物理ボリュームの仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・復旧前です。一覧・一致・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は一覧確認 一致条件（一覧・chde）です。監査・netsのB:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は監査記録 Gateway（監査・nets）です。変更後・mounのD:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、復旧前確認 対象ファイルではls・復旧前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsattr 復旧前確認 対象ファイル**

    - 検証目的: 物理ボリュームのlsattr 復旧前確認 対象ファイルについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e66        rootvg          active
    hdisk1          00f6a1b2c3d5e66        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には VOLUME が含まれ、lsattr 復旧前確認 対象ファイルの証跡を確認できます。

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



### lscfg 変更前確認 障害記録 {#c01-i0905}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lscfg 変更前確認 障害記録」は、構成済みデバイスと VPD を表示するコマンドを変更前確認の観点で確認する技術項目です。VG STATE 欄とpaging058を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lscfg 変更前確認 障害記録の役割を調べています。vmstat 復旧前確認 出力見出しの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - B. 障害切り分けに用いる役割は構成済みデバイスと VPD を表示するコマンドである。 ✅
    - C. 障害切り分けに用いる役割は導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。
    - D. 障害切り分けに用いる役割はLVMでchlvを用い・PVID とボリュームグループ属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は変更前確認 障害記録（変更・lscf）です。物理ボリュームの仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・変更前です。復旧前・vmstのA:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は復旧前確認 出力見出し（復旧・vmst）です。起動・mksyのC:は「導入と起動でmksysbを用い、Technology Level」を述べ、対象はTechnology Level（起動・mksy）です。運用引・chlvのD:は「LVMでchlvを用い、PVID とボリュームグループ属性を確認する」を述べ、対象は運用引継ぎ PVID（運用・chlv）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、変更前確認 障害記録ではls・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lscfg 変更前確認 障害記録**

    - 検証目的: 物理ボリュームのlscfg 変更前確認 障害記録について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には LABEL が含まれ、lscfg 変更前確認 障害記録の証跡を確認できます。

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



### lscfg 状態判定 除外条件 {#c01-i0906}
*分類: 物理ボリューム*  ・  難易度: 中級

AIX 7.3 の 物理ボリューム で扱う「lscfg 状態判定 除外条件」は、構成済みデバイスと VPD を表示するコマンドを状態判定の観点で確認する技術項目です。VG STATE 欄とpaging018を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lscfg 状態判定 除外条件の役割を調べています。vmstat 属性照合 イベント転送の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は構成済みデバイスと VPD を表示するコマンドである。 ✅
    - B. 表示や設定で扱う内容はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - C. 表示や設定で扱う内容はJFS2でsnapを用い・lff とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は状態判定 除外条件（状態・lscf）です。物理ボリュームの仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・状態・除外です。属性・イベ・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は属性照合 イベント転送（属性・vmst）です。監査・snapのC:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は監査記録 lff（監査・snap）です。変更後・setsのD:は「セキュリティでsetsecattrを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・sets）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、状態判定 除外条件ではls・状態・除外に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lscfg 状態判定 除外条件**

    - 検証目的: 物理ボリュームのlscfg 状態判定 除外条件について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、物理ボリュームの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。VG STATE 欄を読むため、対象名を含む操作を入力します。
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

    画面・出力には LABEL が含まれ、lscfg 状態判定 除外条件の証跡を確認できます。

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


