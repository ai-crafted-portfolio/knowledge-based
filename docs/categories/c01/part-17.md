---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (17/18)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > 性能管理

### topas -C 属性確認 csz 0452 {#c01-i0853}
*分類: 性能管理*  ・  難易度: 中級

水音整理ではAIX 7.3の性能管理で topas -C を確認します。水音整理の性能管理では csz とtopasディスク表示を引継ぎ票へ保管します。水音整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音整理の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、水音整理を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 属性確認 csz 0452の技術的な意味を資料で確認するとき、chuser 状態確認 enhanced_RBAC 0453との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はセキュリティでchuserを用い・enhanced_RBAC と監査設定を確認する。
    - B. コマンドまたは機能の用途はJFS2でfsckを用い・agblksize とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途は性能管理でtopas -Cを用い・csz とtopasディスク表示を確認する。 ✅
    - D. コマンドまたは機能の用途はLVMでmirrorvgを用い・LV STATE とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でtopas -Cを用い、csz とtopasディスク表示を確認する」に対応する項目は属性確認 csz（属性・topa）です。属性に関する性能管理の仕様は「性能管理でtopas -Cを用い、csz」で、確認対象はto・属性です。状態・chusのA:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は状態確認 enhanced_RBAC（状態・chus）です。容量・fsckのB:は「JFS2でfsckを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・fsck）です。変更前・mirrのD:は「LVMでmirrorvgを用い、LV STATE」を述べ、対象はLV STATE（変更・mirr）です。「topas -C」は「性能管理でtopas -Cを用い、csz」を指し、属性確認 cszではto・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 属性確認 csz 0452**

    - 検証目的: 性能管理のtopas -C 属性確認 csz 0452について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認092-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0452A
    ```

    画面・出力には AIX0452A が表示され、topas -C 属性確認 csz 0452 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0452B
    ```

    画面・出力には AIX0452B が表示され、topas -C 属性確認 csz 0452 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0452C
    ```

    画面・出力には AIX0452C が表示され、topas -C 属性確認 csz 0452 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0452A が画面・出力に表示されること
    ② ステップ2 の AIX0452B が画面・出力に表示されること
    ③ ステップ3 の AIX0452C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 構成照合 Entitled Capacity 0263 {#c01-i0854}
*分類: 性能管理*  ・  難易度: 中級

新緑監査ではAIX 7.3の性能管理で topas -C を確認します。新緑監査の性能管理では Entitled Capacity とsvmon全体表示を照合票へ整理します。新緑監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑監査の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、新緑監査を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 構成照合 Entitled Capacity 0263の設定や表示を読む前に役割を確認します。chuser 変更前確認 user attributes 0264ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は性能管理でtopas -Cを用い・Entitled Capacity とsvmon全体表示を確認する。 ✅
    - B. 一次資料が示す主目的はセキュリティでchuserを用い・user attributes とユーザー属性を確認する。
    - C. 一次資料が示す主目的はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。mount -o remount 性能確認 agblksize 0569固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Cを用い、Entitled Capacity」に対応する項目はEntitled Capacity（構成・topa）です。構成に関する性能管理の仕様は「性能管理でtopas -Cを用い、Entitled」で、確認対象はto・構成です。変更前・chusのB:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。性能・mounのC:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。変更前・lsatのD:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は変更前確認 パス状態（変更・lsat）です。「topas -C」は「性能管理でtopas -Cを用い、Entitled」を指し、Entitled Capacityではto・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 構成照合 Entitled Capacity 0263**

    - 検証目的: 性能管理のtopas -C 構成照合 Entitled Capacity 0263について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合023-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0263A
    ```

    画面・出力には AIX0263A が表示され、topas -C 構成照合 Entitled Capacity 0263 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0263B
    ```

    画面・出力には AIX0263B が表示され、topas -C 構成照合 Entitled Capacity 0263 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0263C
    ```

    画面・出力には AIX0263C が表示され、topas -C 構成照合 Entitled Capacity 0263 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0263A が画面・出力に表示されること
    ② ステップ2 の AIX0263B が画面・出力に表示されること
    ③ ステップ3 の AIX0263C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 構成照合 PhysB 0739 {#c01-i0855}
*分類: 性能管理*  ・  難易度: 初級

山吹監査ではAIX 7.3の性能管理で topas -C を確認します。山吹監査の性能管理では PhysB とsvmon全体表示を点検票へ整理します。山吹監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。山吹監査の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、山吹監査を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 構成照合 PhysB 0739について構成や状態を確認します。chuser 変更前確認 authorizations 0740ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは性能管理でtopas -Cを用い・PhysB とsvmon全体表示を確認する。 ✅
    - B. 対象資源に対する働きはセキュリティでchuserを用い・authorizations とユーザー属性を確認する。
    - C. 対象資源に対する働きは導入と起動でmksysbを用い・altinst_rootvg と起動デバイス設定を確認する。
    - D. 対象資源に対する働きはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Cを用い、PhysB とsvmon全体表示を確認する」に対応する項目は構成照合 PhysB（構成・topa）です。構成に関する性能管理の仕様は「性能管理でtopas -Cを用い、PhysB」で、確認対象はto・構成です。変更前・chusのB:は「セキュリティでchuserを用い、authorizations」を述べ、対象は変更前確認 authorizatio（変更・chus）です。監査・mksyのC:は「導入と起動でmksysbを用い、altinst_rootvg」を述べ、対象は監査記録 altinst_rootv（監査・mksy）です。変更後・chlvのD:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。「topas -C」は「性能管理でtopas -Cを用い、PhysB」を指し、構成照合 PhysBではto・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 構成照合 PhysB 0739**

    - 検証目的: 性能管理のtopas -C 構成照合 PhysB 0739について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合019-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0739A
    ```

    画面・出力には AIX0739A が表示され、topas -C 構成照合 PhysB 0739 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0739B
    ```

    画面・出力には AIX0739B が表示され、topas -C 構成照合 PhysB 0739 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0739C
    ```

    画面・出力には AIX0739C が表示され、topas -C 構成照合 PhysB 0739 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0739A が画面・出力に表示されること
    ② ステップ2 の AIX0739B が画面・出力に表示されること
    ③ ステップ3 の AIX0739C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 運用引継ぎ csz 0769 {#c01-i0856}
*分類: 性能管理*  ・  難易度: 中級

銀砂復旧ではAIX 7.3の性能管理で topas -C を確認します。銀砂復旧の性能管理では csz とAME統計を採取票へ記録します。銀砂復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。銀砂復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、銀砂復旧を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「topas -C 運用引継ぎ csz 0769」を「chuser 容量確認 authorizations 0770」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は性能管理でtopas -Cを用い・csz とAME統計を確認する。 ✅
    - B. 保守作業で参照する機能はセキュリティでchuserを用い・authorizations とRBAC属性を確認する。
    - C. 保守作業で参照する機能は導入と起動でmksysbを用い・fileset level とfileset一覧を確認する。
    - D. 保守作業で参照する機能はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Cを用い、csz とAME統計を確認する」に対応する項目は運用引継ぎ csz（運用・topa）です。運用引に関する性能管理の仕様は「性能管理でtopas -Cを用い、csz とAME統計を確認する」で、確認対象はto・運用引です。容量・chusのB:は「セキュリティでchuserを用い、authorizations」を述べ、対象は容量確認 authorization（容量・chus）です。状態・mksyのC:は「導入と起動でmksysbを用い、fileset level」を述べ、対象はfileset level（状態・mksy）です。性能・chlvのD:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。「topas -C」は「性能管理でtopas -Cを用い、csz とAME統計を確認する」を指し、運用引継ぎ cszではto・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 運用引継ぎ csz 0769**

    - 検証目的: 性能管理のtopas -C 運用引継ぎ csz 0769について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ049-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0769A
    ```

    画面・出力には AIX0769A が表示され、topas -C 運用引継ぎ csz 0769 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0769B
    ```

    画面・出力には AIX0769B が表示され、topas -C 運用引継ぎ csz 0769 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0769C
    ```

    画面・出力には AIX0769C が表示され、topas -C 運用引継ぎ csz 0769 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0769A が画面・出力に表示されること
    ② ステップ2 の AIX0769B が画面・出力に表示されること
    ③ ステップ3 の AIX0769C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 運用引継ぎ dxm 0293 {#c01-i0857}
*分類: 性能管理*  ・  難易度: 中級

月影復旧ではAIX 7.3の性能管理で topas -C を確認します。月影復旧の性能管理では dxm とAME統計を復旧票へ残します。月影復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、月影復旧を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 運用引継ぎ dxm 0293を保守記録に説明する必要があります。chuser 容量確認 user attributes 0294と取り違えない説明はどれですか。

    - A. 仕様上の役割はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。
    - B. 仕様上の役割はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。
    - C. 仕様上の役割はデバイスや sys0 などの属性値を表示するコマンドである。
    - D. 仕様上の役割は性能管理でtopas -Cを用い・dxm とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Cを用い、dxm とAME統計を確認する」に対応する項目は運用引継ぎ dxm（運用・topa）です。運用引に関する性能管理の仕様は「性能管理でtopas -Cを用い、dxm とAME統計を確認する」で、確認対象はto・運用引です。容量・chusのA:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。変更後・mounのB:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。復旧前・lsatのC:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は復旧前確認 対象ファイル（復旧・lsat）です。「topas -C」は「性能管理でtopas -Cを用い、dxm とAME統計を確認する」を指し、運用引継ぎ dxmではto・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 運用引継ぎ dxm 0293**

    - 検証目的: 性能管理のtopas -C 運用引継ぎ dxm 0293について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ053-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0293A
    ```

    画面・出力には AIX0293A が表示され、topas -C 運用引継ぎ dxm 0293 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0293B
    ```

    画面・出力には AIX0293B が表示され、topas -C 運用引継ぎ dxm 0293 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0293C
    ```

    画面・出力には AIX0293C が表示され、topas -C 運用引継ぎ dxm 0293 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0293A が画面・出力に表示されること
    ② ステップ2 の AIX0293B が画面・出力に表示されること
    ③ ステップ3 の AIX0293C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 Busy% 0490 {#c01-i0858}
*分類: 性能管理*  ・  難易度: 初級

桜雲確認ではAIX 7.3の性能管理で topas -D を確認します。桜雲確認の性能管理では Busy% とvmstat表示を保守票へ記録します。桜雲確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲確認の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、桜雲確認を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 Busy% 0490の役割を調べています。setsecattr 変更後確認 enhanced_RBAC 0491の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は性能管理でtopas -Dを用い・Busy% とvmstat表示を確認する。 ✅
    - B. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。
    - C. 表示や設定で扱う内容はJFS2でlsfs -qを用い・isnapshot とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はLVMでmklvを用い・PP SIZE とボリュームグループ属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Dを用い、Busy% とvmstat表示を確認する」に対応する項目は変更前確認 Busy%（変更・topa）です。変更前に関する性能管理の仕様は「性能管理でtopas -Dを用い、Busy%」で、確認対象はto・変更前です。変更後・setsのB:は「セキュリティでsetsecattrを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・sets）です。起動・lsfsのC:は「JFS2でlsfs -qを用い、isnapshot」を述べ、対象は起動確認 isnapshot（起動・lsfs）です。障害切・mklvのD:は「LVMでmklvを用い、PP SIZE とボリュームグループ属性を確」を述べ、対象はPP SIZE（障害・mklv）です。「topas -D」は「性能管理でtopas -Dを用い、Busy%」を指し、変更前確認 Busy%ではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 Busy% 0490**

    - 検証目的: 性能管理のtopas -D 変更前確認 Busy% 0490について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認010-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0490A
    ```

    画面・出力には AIX0490A が表示され、topas -D 変更前確認 Busy% 0490 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0490B
    ```

    画面・出力には AIX0490B が表示され、topas -D 変更前確認 Busy% 0490 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0490C
    ```

    画面・出力には AIX0490C が表示され、topas -D 変更前確認 Busy% 0490 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0490A が画面・出力に表示されること
    ② ステップ2 の AIX0490B が画面・出力に表示されること
    ③ ステップ3 の AIX0490C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 PhysB 0014 {#c01-i0859}
*分類: 性能管理*  ・  難易度: 初級

星霜確認ではAIX 7.3の性能管理で topas -D を確認します。星霜確認の性能管理では PhysB とvmstat表示を確認票へ整理します。星霜確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。星霜確認の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、星霜確認を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 PhysB 0014に関する障害切り分けの前提を確認しています。setsecattr 変更後確認 audit class 0015の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は性能管理でtopas -Dを用い・PhysB とvmstat表示を確認する。 ✅
    - B. 障害切り分けに用いる役割はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。
    - C. 障害切り分けに用いる役割はJFS2でlsfs -qを用い・log=INLINE とログデバイス設定を確認する。
    - D. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・user attributesである。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Dを用い、PhysB とvmstat表示を確認する」に対応する項目は変更前確認 PhysB（変更・topa）です。性能管理の仕様は「性能管理でtopas -Dを用い、PhysB」で、確認対象はto・変更前です。変更後・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。起動・lsfsのC:は「JFS2でlsfs -qを用い、log=INLINE」を述べ、対象は起動確認 log=INLINE（起動・lsfs）です。容量・roleのD:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（容量・role）です。「topas -D」は「性能管理でtopas -Dを用い、PhysB」を指し、変更前確認 PhysBではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 PhysB 0014**

    - 検証目的: 性能管理のtopas -D 変更前確認 PhysB 0014について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認014-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0014A
    ```

    画面・出力には AIX0014A が表示され、topas -D 変更前確認 PhysB 0014 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0014B
    ```

    画面・出力には AIX0014B が表示され、topas -D 変更前確認 PhysB 0014 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0014C
    ```

    画面・出力には AIX0014C が表示され、topas -D 変更前確認 PhysB 0014 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0014A が画面・出力に表示されること
    ② ステップ2 の AIX0014B が画面・出力に表示されること
    ③ ステップ3 の AIX0014C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 avm 0550 {#c01-i0860}
*分類: 性能管理*  ・  難易度: 中級

早苗照合ではAIX 7.3の性能管理で topas -D を確認します。早苗照合の性能管理では avm とvmstat表示を保守票へ記録します。早苗照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗照合の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、早苗照合を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 avm 0550に関する障害切り分けの前提を確認しています。setsecattr 変更後確認 enhanced_RBAC 0551の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。
    - B. 表示や設定で扱う内容はデバイスや sys0 などの属性値を表示するコマンドである。
    - C. 表示や設定で扱う内容はLVMでchlvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。
    - D. 表示や設定で扱う内容は性能管理でtopas -Dを用い・avm とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Dを用い、avm とvmstat表示を確認する」に対応する項目は変更前確認 avm（変更・topa）です。変更前に関する性能管理の仕様は「性能管理でtopas -Dを用い、avm」で、確認対象はto・変更前です。変更後・setsのA:は「セキュリティでsetsecattrを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・sets）です。一覧・対象・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は一覧確認 対象ファイル（一覧・lsat）です。バック・chlvのC:は「LVMでchlvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（バッ・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、avm」を指し、変更前確認 avmではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 avm 0550**

    - 検証目的: 性能管理のtopas -D 変更前確認 avm 0550について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認070-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0550A
    ```

    画面・出力には AIX0550A が表示され、topas -D 変更前確認 avm 0550 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0550B
    ```

    画面・出力には AIX0550B が表示され、topas -D 変更前確認 avm 0550 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0550C
    ```

    画面・出力には AIX0550C が表示され、topas -D 変更前確認 avm 0550 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0550A が画面・出力に表示されること
    ② ステップ2 の AIX0550B が画面・出力に表示されること
    ③ ステップ3 の AIX0550C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 fre 0074 {#c01-i0861}
*分類: 性能管理*  ・  難易度: 中級

銀嶺照合ではAIX 7.3の性能管理で topas -D を確認します。銀嶺照合の性能管理では fre とvmstat表示を確認票へ整理します。銀嶺照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。銀嶺照合の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、銀嶺照合を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 fre 0074の役割を調べています。setsecattr 変更後確認 audit class 0075の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。
    - B. 障害切り分けに用いる役割はJFS2でmount -o remountを用い・agblksize とログデバイス設定を確認する。
    - C. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・user attributesである。
    - D. 障害切り分けに用いる役割は性能管理でtopas -Dを用い・fre とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Dを用い、fre とvmstat表示を確認する」に対応する項目は変更前確認 fre（変更・topa）です。変更前に関する性能管理の仕様は「性能管理でtopas -Dを用い、fre」で、確認対象はto・変更前です。変更後・setsのA:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。属性・mounのB:は「JFS2でmount -o remountを用い」を述べ、対象は属性確認 agblksize（属性・moun）です。容量・roleのC:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（容量・role）です。「topas -D」は「性能管理でtopas -Dを用い、fre」を指し、変更前確認 freではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 fre 0074**

    - 検証目的: 性能管理のtopas -D 変更前確認 fre 0074について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認074-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0074A
    ```

    画面・出力には AIX0074A が表示され、topas -D 変更前確認 fre 0074 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0074B
    ```

    画面・出力には AIX0074B が表示され、topas -D 変更前確認 fre 0074 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0074C
    ```

    画面・出力には AIX0074C が表示され、topas -D 変更前確認 fre 0074 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0074A が画面・出力に表示されること
    ② ステップ2 の AIX0074B が画面・出力に表示されること
    ③ ステップ3 の AIX0074C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 Busy% 0580 {#c01-i0862}
*分類: 性能管理*  ・  難易度: 上級

薄明点検ではAIX 7.3の性能管理で topas -D を確認します。薄明点検の性能管理では Busy% とtopasディスク表示を監査票へ転記します。薄明点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明点検の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、薄明点検を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 Busy% 0580の技術的な意味を資料で確認するとき、setsecattr 性能確認 enhanced_RBAC 0581との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。
    - B. 管理対象との関係を表す説明はデバイスや sys0 などの属性値を表示するコマンドである。
    - C. 管理対象との関係を表す説明はLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。
    - D. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でtopas -Dを用い、Busy% とtopasディスク表示を確認する」に対応する項目は容量確認 Busy%（容量・topa）です。容量に関する性能管理の仕様は「性能管理でtopas -Dを用い、Busy%」で、確認対象はto・容量です。性能・setsのA:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。詳細・確認・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は詳細確認 確認範囲（詳細・lsat）です。属性・chlvのC:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（属性・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、Busy%」を指し、容量確認 Busy%ではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 Busy% 0580**

    - 検証目的: 性能管理のtopas -D 容量確認 Busy% 0580について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認100-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0580A
    ```

    画面・出力には AIX0580A が表示され、topas -D 容量確認 Busy% 0580 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0580B
    ```

    画面・出力には AIX0580B が表示され、topas -D 容量確認 Busy% 0580 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0580C
    ```

    画面・出力には AIX0580C が表示され、topas -D 容量確認 Busy% 0580 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0580A が画面・出力に表示されること
    ② ステップ2 の AIX0580B が画面・出力に表示されること
    ③ ステップ3 の AIX0580C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 PhysB 0104 {#c01-i0863}
*分類: 性能管理*  ・  難易度: 上級

霜月点検ではAIX 7.3の性能管理で topas -D を確認します。霜月点検の性能管理では PhysB とtopasディスク表示を引継ぎ票へ保管します。霜月点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。霜月点検の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、霜月点検を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 PhysB 0104を同一分類のsetsecattr 性能確認 audit class 0105と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。
    - B. コマンドまたは機能の用途はJFS2でmount -o remountを用い・lff とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。
    - D. コマンドまたは機能の用途は性能管理でtopas -Dを用い・PhysB とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でtopas -Dを用い、PhysB とtopasディスク表示を確認する」に対応する項目は容量確認 PhysB（容量・topa）です。容量に関する性能管理の仕様は「性能管理でtopas -Dを用い、PhysB」で、確認対象はto・容量です。性能・setsのA:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。バック・mounのB:は「JFS2でmount -o remountを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・moun）です。変更前・roleのC:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。「topas -D」は「性能管理でtopas -Dを用い、PhysB」を指し、容量確認 PhysBではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 PhysB 0104**

    - 検証目的: 性能管理のtopas -D 容量確認 PhysB 0104について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認104-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0104A
    ```

    画面・出力には AIX0104A が表示され、topas -D 容量確認 PhysB 0104 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0104B
    ```

    画面・出力には AIX0104B が表示され、topas -D 容量確認 PhysB 0104 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0104C
    ```

    画面・出力には AIX0104C が表示され、topas -D 容量確認 PhysB 0104 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0104A が画面・出力に表示されること
    ② ステップ2 の AIX0104B が画面・出力に表示されること
    ③ ステップ3 の AIX0104C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 csz 0044 {#c01-i0864}
*分類: 性能管理*  ・  難易度: 中級

若草照合ではAIX 7.3の性能管理で topas -D を確認します。若草照合の性能管理では csz とtopasディスク表示を引継ぎ票へ保管します。若草照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若草照合の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、若草照合を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 csz 0044の技術的な意味を資料で確認するとき、setsecattr 性能確認 audit class 0045との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でtopas -Dを用い・csz とtopasディスク表示を確認する。 ✅
    - B. コマンドまたは機能の用途はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。
    - C. コマンドまたは機能の用途はJFS2でlsfs -qを用い・mountguard とファイルシステム属性を確認する。
    - D. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、csz とtopasディスク表示を確認する」に対応する項目は容量確認 csz（容量・topa）です。性能管理の仕様は「性能管理でtopas -Dを用い、csz とtopasディスク表示を確認」で、確認対象はto・容量です。性能・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。障害切・lsfsのC:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・lsfs）です。変更前・roleのD:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。「topas -D」は「性能管理でtopas -Dを用い、csz」を指し、容量確認 cszではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 csz 0044**

    - 検証目的: 性能管理のtopas -D 容量確認 csz 0044について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認044-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0044A
    ```

    画面・出力には AIX0044A が表示され、topas -D 容量確認 csz 0044 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0044B
    ```

    画面・出力には AIX0044B が表示され、topas -D 容量確認 csz 0044 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0044C
    ```

    画面・出力には AIX0044C が表示され、topas -D 容量確認 csz 0044 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0044A が画面・出力に表示されること
    ② ステップ2 の AIX0044B が画面・出力に表示されること
    ③ ステップ3 の AIX0044C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 po 0520 {#c01-i0865}
*分類: 性能管理*  ・  難易度: 中級

青葉照合ではAIX 7.3の性能管理で topas -D を確認します。青葉照合の性能管理では po とtopasディスク表示を監査票へ転記します。青葉照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。青葉照合の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、青葉照合を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 po 0520を同一分類のsetsecattr 性能確認 enhanced_RBAC 0521と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・po とtopasディスク表示を確認する。 ✅
    - B. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。
    - C. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・ファイルシステム使用率 とファイルシステム属性を確認する。
    - D. 管理対象との関係を表す説明はLVMでmklvを用い・PVID とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、po とtopasディスク表示を確認する」に対応する項目は容量確認 po（容量・topa）です。容量に関する性能管理の仕様は「性能管理でtopas -Dを用い、po とtopasディスク表示を確」で、確認対象はto・容量です。性能・setsのB:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。障害切・lsfsのC:は「JFS2でlsfs -qを用い、ファイルシステム使用率」を述べ、対象は障害切り分け ファイルシステム使用率（障害・lsfs）です。起動・mklvのD:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。「topas -D」は「性能管理でtopas -Dを用い、po とtopasディスク表示を確」を指し、容量確認 poではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 po 0520**

    - 検証目的: 性能管理のtopas -D 容量確認 po 0520について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認040-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0520A
    ```

    画面・出力には AIX0520A が表示され、topas -D 容量確認 po 0520 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0520B
    ```

    画面・出力には AIX0520B が表示され、topas -D 容量確認 po 0520 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0520C
    ```

    画面・出力には AIX0520C が表示され、topas -D 容量確認 po 0520 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0520A が画面・出力に表示されること
    ② ステップ2 の AIX0520B が画面・出力に表示されること
    ③ ステップ3 の AIX0520C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 状態確認 csz 0203 {#c01-i0866}
*分類: 性能管理*  ・  難易度: 中級

秋声保守ではAIX 7.3の性能管理で topas -D を確認します。秋声保守の性能管理では csz とsvmon全体表示を照合票へ整理します。秋声保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声保守の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、秋声保守を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 状態確認 csz 0203について構成や状態を確認します。setsecattr 構成照合 audit class 0204ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は性能管理でtopas -Dを用い・csz とsvmon全体表示を確認する。 ✅
    - B. 一次資料が示す主目的はセキュリティでsetsecattrを用い・audit class とユーザー属性を確認する。
    - C. 一次資料が示す主目的はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。
    - D. 一次資料が示す主目的はセキュリティでrolelist -u user1を用い・user attributesである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、csz とsvmon全体表示を確認する」に対応する項目は状態確認 csz（状態・topa）です。状態に関する性能管理の仕様は「性能管理でtopas -Dを用い、csz」で、確認対象はto・状態です。構成・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（構成・sets）です。性能・mounのC:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。監査・roleのD:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（監査・role）です。「topas -D」は「性能管理でtopas -Dを用い、csz」を指し、状態確認 cszではto・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 状態確認 csz 0203**

    - 検証目的: 性能管理のtopas -D 状態確認 csz 0203について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認083-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0203A
    ```

    画面・出力には AIX0203A が表示され、topas -D 状態確認 csz 0203 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0203B
    ```

    画面・出力には AIX0203B が表示され、topas -D 状態確認 csz 0203 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0203C
    ```

    画面・出力には AIX0203C が表示され、topas -D 状態確認 csz 0203 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0203A が画面・出力に表示されること
    ② ステップ2 の AIX0203B が画面・出力に表示されること
    ③ ステップ3 の AIX0203C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 状態確認 po 0679 {#c01-i0867}
*分類: 性能管理*  ・  難易度: 中級

秋桜判定ではAIX 7.3の性能管理で topas -D を確認します。秋桜判定の性能管理では po とsvmon全体表示を点検票へ整理します。秋桜判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋桜判定の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、秋桜判定を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 状態確認 po 0679の設定や表示を読む前に役割を確認します。setsecattr 構成照合 enhanced_RBAC 0680ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは性能管理でtopas -Dを用い・po とsvmon全体表示を確認する。 ✅
    - B. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC とユーザー属性を確認する。
    - C. 対象資源に対する働きは導入と起動でalt_disk_mksysbを用い・bootlist と起動デバイス設定を確認する。
    - D. 対象資源に対する働きはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、po とsvmon全体表示を確認する」に対応する項目は状態確認 po（状態・topa）です。状態に関する性能管理の仕様は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」で、確認対象はto・状態です。構成・setsのB:は「セキュリティでsetsecattrを用い」を述べ、対象は構成照合 enhanced_RBAC（構成・sets）です。バック・alt_のC:は「導入と起動でalt_disk_mksysbを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・alt_）です。変更後・chlvのD:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」を指し、状態確認 poではto・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 状態確認 po 0679**

    - 検証目的: 性能管理のtopas -D 状態確認 po 0679について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認079-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0679A
    ```

    画面・出力には AIX0679A が表示され、topas -D 状態確認 po 0679 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0679B
    ```

    画面・出力には AIX0679B が表示され、topas -D 状態確認 po 0679 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0679C
    ```

    画面・出力には AIX0679C が表示され、topas -D 状態確認 po 0679 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0679A が画面・出力に表示されること
    ② ステップ2 の AIX0679B が画面・出力に表示されること
    ③ ステップ3 の AIX0679C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 監査記録 avm 0709 {#c01-i0868}
*分類: 性能管理*  ・  難易度: 上級

梅雨晴保守ではAIX 7.3の性能管理で topas -D を確認します。梅雨晴保守の性能管理では avm とAME統計を採取票へ記録します。梅雨晴保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。梅雨晴保守の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、梅雨晴保守を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 監査記録 avm 0709を保守記録に説明する必要があります。setsecattr 運用引継ぎ enhanced_RBAC 0710と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はセキュリティでsetsecattrを用い・enhanced_RBAC とRBAC属性を確認する。
    - B. 保守作業で参照する機能は導入と起動でalt_disk_mksysbを用い・Technology Levelである。
    - C. 保守作業で参照する機能はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。
    - D. 保守作業で参照する機能は性能管理でtopas -Dを用い・avm とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でtopas -Dを用い、avm とAME統計を確認する」に対応する項目は監査記録 avm（監査・topa）です。監査に関する性能管理の仕様は「性能管理でtopas -Dを用い、avm とAME統計を確認する」で、確認対象はto・監査です。運用引・setsのA:は「セキュリティでsetsecattrを用い」を述べ、対象は運用引継ぎ enhanced_RBA（運用・sets）です。属性・alt_のB:は「導入と起動でalt_disk_mksysbを用い」を述べ、対象はTechnology Level（属性・alt_）です。性能・chlvのC:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、avm とAME統計を確認する」を指し、監査記録 avmではto・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 監査記録 avm 0709**

    - 検証目的: 性能管理のtopas -D 監査記録 avm 0709について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録109-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0709A
    ```

    画面・出力には AIX0709A が表示され、topas -D 監査記録 avm 0709 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0709B
    ```

    画面・出力には AIX0709B が表示され、topas -D 監査記録 avm 0709 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0709C
    ```

    画面・出力には AIX0709C が表示され、topas -D 監査記録 avm 0709 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0709A が画面・出力に表示されること
    ② ステップ2 の AIX0709B が画面・出力に表示されること
    ③ ステップ3 の AIX0709C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 監査記録 fre 0233 {#c01-i0869}
*分類: 性能管理*  ・  難易度: 上級

朝霧保守ではAIX 7.3の性能管理で topas -D を確認します。朝霧保守の性能管理では fre とAME統計を復旧票へ残します。朝霧保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。朝霧保守の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、朝霧保守を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「topas -D 監査記録 fre 0233」を「setsecattr 運用引継ぎ audit class 0234」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。
    - B. 仕様上の役割は性能管理でtopas -Dを用い・fre とAME統計を確認する。 ✅
    - C. 仕様上の役割はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。
    - D. 仕様上の役割はデバイスや sys0 などの属性値を表示するコマンドである。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「性能管理でtopas -Dを用い、fre とAME統計を確認する」に対応する項目は監査記録 fre（監査・topa）です。監査に関する性能管理の仕様は「性能管理でtopas -Dを用い、fre とAME統計を確認する」で、確認対象はto・監査です。運用引・setsのA:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。変更後・mounのC:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。性能・実行・lsatのD:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は性能確認 実行結果（性能・lsat）です。「topas -D」は「性能管理でtopas -Dを用い、fre とAME統計を確認する」を指し、監査記録 freではto・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 監査記録 fre 0233**

    - 検証目的: 性能管理のtopas -D 監査記録 fre 0233について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録113-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0233A
    ```

    画面・出力には AIX0233A が表示され、topas -D 監査記録 fre 0233 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0233B
    ```

    画面・出力には AIX0233B が表示され、topas -D 監査記録 fre 0233 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0233C
    ```

    画面・出力には AIX0233C が表示され、topas -D 監査記録 fre 0233 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0233A が画面・出力に表示されること
    ② ステップ2 の AIX0233B が画面・出力に表示されること
    ③ ステップ3 の AIX0233C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 障害切り分け csz 0361 {#c01-i0870}
*分類: 性能管理*  ・  難易度: 初級

白露記録ではAIX 7.3の性能管理で topas -D を確認します。白露記録の性能管理では csz とAME統計を採取票へ記録します。白露記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露記録の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、白露記録を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「topas -D 障害切り分け csz 0361」を「setsecattr バックアウト確認 user attributes 0362」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は性能管理でtopas -Dを用い・csz とAME統計を確認する。 ✅
    - B. 保守作業で参照する機能はセキュリティでsetsecattrを用い・user attributes とRBAC属性を確認する。
    - C. 保守作業で参照する機能はJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。
    - D. 保守作業で参照する機能はLVMでmklvを用い・PP SIZE と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Dを用い、csz とAME統計を確認する」に対応する項目は障害切り分け csz（障害・topa）です。障害切に関する性能管理の仕様は「性能管理でtopas -Dを用い、csz とAME統計を確認する」で、確認対象はto・障害切です。バック・setsのB:は「セキュリティでsetsecattrを用い、user」を述べ、対象はuser attributes（バッ・sets）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・lsfs）です。監査・mklvのD:は「LVMでmklvを用い、PP SIZE と物理ボリューム一覧を確認す」を述べ、対象はPP SIZE（監査・mklv）です。「topas -D」は「性能管理でtopas -Dを用い、csz とAME統計を確認する」を指し、障害切り分け cszではto・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 障害切り分け csz 0361**

    - 検証目的: 性能管理のtopas -D 障害切り分け csz 0361について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け001-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0361A
    ```

    画面・出力には AIX0361A が表示され、topas -D 障害切り分け csz 0361 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0361B
    ```

    画面・出力には AIX0361B が表示され、topas -D 障害切り分け csz 0361 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0361C
    ```

    画面・出力には AIX0361C が表示され、topas -D 障害切り分け csz 0361 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0361A が画面・出力に表示されること
    ② ステップ2 の AIX0361B が画面・出力に表示されること
    ③ ステップ3 の AIX0361C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 Busy% 0029 {#c01-i0871}
*分類: 性能管理*  ・  難易度: 中級

梅雨晴確認ではAIX 7.3の性能管理で vmo -a を確認します。梅雨晴確認の性能管理では Busy% とAME統計を復旧票へ残します。梅雨晴確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。梅雨晴確認の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、梅雨晴確認を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a バックアウト確認 Busy% 0029を保守記録に説明する必要があります。lsattr -E -l sys0 -a enhanced_RBAC 監査記録と取り違えない説明はどれですか。

    - A. 仕様上の役割はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。
    - B. 仕様上の役割はJFS2でsplitcopyを用い・isnapshot と内部スナップショットを確認する。
    - C. 仕様上の役割はセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。
    - D. 仕様上の役割は性能管理でvmo -aを用い・Busy% とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmo -aを用い、Busy% とAME統計を確認する」に対応する項目はバックアウト確認 Busy%（バッ・vmo）です。性能管理の仕様は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。構成・spliのB:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・spli）です。属性・lsusのC:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は属性確認 authorization（属性・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」を指し、バックアウト確認 Busy%ではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 Busy% 0029**

    - 検証目的: 性能管理のvmo -a バックアウト確認 Busy% 0029について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認029-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0029A
    ```

    画面・出力には AIX0029A が表示され、vmo -a バックアウト確認 Busy% 0029 の入力欄確認を確認できます。

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
    確認コード AIX0029B
    ```

    画面・出力には AIX0029B が表示され、vmo -a バックアウト確認 Busy% 0029 の証跡表示確認を確認できます。

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
    確認コード AIX0029C
    ```

    画面・出力には AIX0029C が表示され、vmo -a バックアウト確認 Busy% 0029 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0029A が画面・出力に表示されること
    ② ステップ2 の AIX0029B が画面・出力に表示されること
    ③ ステップ3 の AIX0029C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 Entitled Capacity 0565 {#c01-i0872}
*分類: 性能管理*  ・  難易度: 中級

深雪点検ではAIX 7.3の性能管理で vmo -a を確認します。深雪点検の性能管理では Entitled Capacity とAME統計を採取票へ記録します。深雪点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。深雪点検の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、深雪点検を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a バックアウト確認 Entitled Capacity 0565を保守記録に説明する必要があります。lsattr -E -l sys0 -a enhanced_RBAC 監査記録と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。
    - B. 保守作業で参照する機能は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - C. 保守作業で参照する機能は性能管理でvmo -aを用い・Entitled Capacity とAME統計を確認する。 ✅
    - D. 保守作業で参照する機能はLVMでlspvを用い・MIRROR WRITE CONSISTENCY と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、Entitled Capacity」に対応する項目はEntitled Capacity（バッ・vmo）です。バックに関する性能管理の仕様は「性能管理でvmo -aを用い、Entitled Capacity」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。詳細・装置・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は詳細確認 装置一覧（詳細・lspv）です。容量・lspvのD:は「LVMでlspvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（容量・lspv）です。「vmo -a」は「性能管理でvmo -aを用い、Entitled Capacity」を指し、Entitled Capacityではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 Entitled Capacity 0565**

    - 検証目的: 性能管理のvmo -a バックアウト確認 Entitled Capacity 0565について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認085-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0565A
    ```

    画面・出力には AIX0565A が表示され、vmo -a バックアウト確認 Entitled Capacity 0565 の入力欄確認を確認できます。

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
    確認コード AIX0565B
    ```

    画面・出力には AIX0565B が表示され、vmo -a バックアウト確認 Entitled Capacity 0565 の証跡表示確認を確認できます。

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
    確認コード AIX0565C
    ```

    画面・出力には AIX0565C が表示され、vmo -a バックアウト確認 Entitled Capacity 0565 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0565A が画面・出力に表示されること
    ② ステップ2 の AIX0565B が画面・出力に表示されること
    ③ ステップ3 の AIX0565C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 avm 0089 {#c01-i0873}
*分類: 性能管理*  ・  難易度: 中級

銀砂点検ではAIX 7.3の性能管理で vmo -a を確認します。銀砂点検の性能管理では avm とAME統計を復旧票へ残します。銀砂点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。銀砂点検の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、銀砂点検を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「vmo -a バックアウト確認 avm 0089」を「lsattr -E -l sys0 -a enhanced_RBAC 監査記録」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。
    - B. 仕様上の役割はJFS2でlogformを用い・mountguard と内部スナップショットを確認する。
    - C. 仕様上の役割は性能管理でvmo -aを用い・avm とAME統計を確認する。 ✅
    - D. 仕様上の役割はセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、avm とAME統計を確認する」に対応する項目はバックアウト確認 avm（バッ・vmo）です。バックに関する性能管理の仕様は「性能管理でvmo -aを用い、avm とAME統計を確認する」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。変更前・logfのB:は「JFS2でlogformを用い、mountguard」を述べ、対象は変更前確認 mountguard（変更・logf）です。属性・lsusのD:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は属性確認 authorization（属性・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、avm とAME統計を確認する」を指し、バックアウト確認 avmではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 avm 0089**

    - 検証目的: 性能管理のvmo -a バックアウト確認 avm 0089について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認089-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0089A
    ```

    画面・出力には AIX0089A が表示され、vmo -a バックアウト確認 avm 0089 の入力欄確認を確認できます。

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
    確認コード AIX0089B
    ```

    画面・出力には AIX0089B が表示され、vmo -a バックアウト確認 avm 0089 の証跡表示確認を確認できます。

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
    確認コード AIX0089C
    ```

    画面・出力には AIX0089C が表示され、vmo -a バックアウト確認 avm 0089 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0089A が画面・出力に表示されること
    ② ステップ2 の AIX0089B が画面・出力に表示されること
    ③ ステップ3 の AIX0089C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 dxm 0505 {#c01-i0874}
*分類: 性能管理*  ・  難易度: 中級

花冷確認ではAIX 7.3の性能管理で vmo -a を確認します。花冷確認の性能管理では dxm とAME統計を採取票へ記録します。花冷確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。花冷確認の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、花冷確認を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「vmo -a バックアウト確認 dxm 0505」を「lsattr -E -l sys0 -a enhanced_RBAC 監査記録」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。
    - B. 保守作業で参照する機能はJFS2でsplitcopyを用い・lff と内部スナップショットを確認する。
    - C. 保守作業で参照する機能は性能管理でvmo -aを用い・dxm とAME統計を確認する。 ✅
    - D. 保守作業で参照する機能はLVMでchvgを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、dxm とAME統計を確認する」に対応する項目はバックアウト確認 dxm（バッ・vmo）です。バックに関する性能管理の仕様は「性能管理でvmo -aを用い、dxm とAME統計を確認する」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。構成・spliのB:は「JFS2でsplitcopyを用い、lff」を述べ、対象は構成照合 lff（構成・spli）です。運用引・chvgのD:は「LVMでchvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（運用・chvg）です。「vmo -a」は「性能管理でvmo -aを用い、dxm とAME統計を確認する」を指し、バックアウト確認 dxmではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 dxm 0505**

    - 検証目的: 性能管理のvmo -a バックアウト確認 dxm 0505について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認025-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0505A
    ```

    画面・出力には AIX0505A が表示され、vmo -a バックアウト確認 dxm 0505 の入力欄確認を確認できます。

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
    確認コード AIX0505B
    ```

    画面・出力には AIX0505B が表示され、vmo -a バックアウト確認 dxm 0505 の証跡表示確認を確認できます。

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
    確認コード AIX0505C
    ```

    画面・出力には AIX0505C が表示され、vmo -a バックアウト確認 dxm 0505 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0505A が画面・出力に表示されること
    ② ステップ2 の AIX0505B が画面・出力に表示されること
    ③ ステップ3 の AIX0505C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 変更後確認 fre 0694 {#c01-i0875}
*分類: 性能管理*  ・  難易度: 中級

星霜保守ではAIX 7.3の性能管理で vmo -a を確認します。星霜保守の性能管理では fre とvmstat表示を保守票へ記録します。星霜保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。星霜保守の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、星霜保守を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 変更後確認 fre 0694に関する障害切り分けの前提を確認しています。lsattr -E -l sys0 -a enhanced_RBAC 障害切り分けの機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はセキュリティでlsattr -E -l sys0 -aを用い・audit class とロール一覧を確認する。
    - B. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。
    - C. 表示や設定で扱う内容はLVMでlspvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。
    - D. 表示や設定で扱う内容は性能管理でvmo -aを用い・fre とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmo -aを用い、fre とvmstat表示を確認する」に対応する項目は変更後確認 fre（変更・vmo）です。変更後に関する性能管理の仕様は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」で、確認対象はvm・変更後です。障害切・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象はaudit class（障害・lsat）です。容量・osleのB:は「導入と起動でoslevel -sを用い、altinst_rootvg」を述べ、対象は容量確認 altinst_rootv（容量・osle）です。監査・lspvのC:は「LVMでlspvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（監査・lspv）です。「vmo -a」は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」を指し、変更後確認 freではvm・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 変更後確認 fre 0694**

    - 検証目的: 性能管理のvmo -a 変更後確認 fre 0694について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認094-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0694A
    ```

    画面・出力には AIX0694A が表示され、vmo -a 変更後確認 fre 0694 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0694B
    ```

    画面・出力には AIX0694B が表示され、vmo -a 変更後確認 fre 0694 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0694C
    ```

    画面・出力には AIX0694C が表示され、vmo -a 変更後確認 fre 0694 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0694A が画面・出力に表示されること
    ② ステップ2 の AIX0694B が画面・出力に表示されること
    ③ ステップ3 の AIX0694C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 変更後確認 pi 0218 {#c01-i0876}
*分類: 性能管理*  ・  難易度: 中級

潮騒保守ではAIX 7.3の性能管理で vmo -a を確認します。潮騒保守の性能管理では pi とvmstat表示を確認票へ整理します。潮騒保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。潮騒保守の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、潮騒保守を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 変更後確認 pi 0218の役割を調べています。lsattr -E -l sys0 -a enhanced_RBAC 障害切り分けの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・authorizationsである。
    - B. 障害切り分けに用いる役割は性能管理でvmo -aを用い・pi とvmstat表示を確認する。 ✅
    - C. 障害切り分けに用いる役割はJFS2でlogformを用い・isnapshot とログデバイス設定を確認する。
    - D. 障害切り分けに用いる役割はセキュリティでlsuserを用い・roles とロール一覧を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmo -aを用い、pi とvmstat表示を確認する」に対応する項目は変更後確認 pi（変更・vmo）です。変更後に関する性能管理の仕様は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」で、確認対象はvm・変更後です。障害切・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は障害切り分け authorizati（障害・lsat）です。状態・logfのC:は「JFS2でlogformを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・logf）です。性能・lsusのD:は「セキュリティでlsuserを用い、roles とロール一覧を確認する」を述べ、対象は性能確認 roles（性能・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」を指し、変更後確認 piではvm・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 変更後確認 pi 0218**

    - 検証目的: 性能管理のvmo -a 変更後確認 pi 0218について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認098-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0218A
    ```

    画面・出力には AIX0218A が表示され、vmo -a 変更後確認 pi 0218 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0218B
    ```

    画面・出力には AIX0218B が表示され、vmo -a 変更後確認 pi 0218 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0218C
    ```

    画面・出力には AIX0218C が表示され、vmo -a 変更後確認 pi 0218 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0218A が画面・出力に表示されること
    ② ステップ2 の AIX0218B が画面・出力に表示されること
    ③ ステップ3 の AIX0218C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 属性確認 pi 0535 {#c01-i0877}
*分類: 性能管理*  ・  難易度: 中級

岩清水照合ではAIX 7.3の性能管理で vmo -a を確認します。岩清水照合の性能管理では pi とsvmon全体表示を点検票へ整理します。岩清水照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。岩清水照合の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、岩清水照合を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 属性確認 pi 0535の設定や表示を読む前に役割を確認します。lsattr -E -l sys0 -a enhanced_RBAC 状態確認ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。
    - B. 対象資源に対する働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - C. 対象資源に対する働きは性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。 ✅
    - D. 対象資源に対する働きはLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」に対応する項目は属性確認 pi（属性・vmo）です。属性に関する性能管理の仕様は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」で、確認対象はvm・属性です。状態・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。一覧・状態・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は一覧確認 状態確認（一覧・lspv）です。構成・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（構成・chvg）です。「vmo -a」は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を指し、属性確認 piではvm・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 属性確認 pi 0535**

    - 検証目的: 性能管理のvmo -a 属性確認 pi 0535について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認055-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0535A
    ```

    画面・出力には AIX0535A が表示され、vmo -a 属性確認 pi 0535 の入力欄確認を確認できます。

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
    確認コード AIX0535B
    ```

    画面・出力には AIX0535B が表示され、vmo -a 属性確認 pi 0535 の証跡表示確認を確認できます。

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
    確認コード AIX0535C
    ```

    画面・出力には AIX0535C が表示され、vmo -a 属性確認 pi 0535 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0535A が画面・出力に表示されること
    ② ステップ2 の AIX0535B が画面・出力に表示されること
    ③ ステップ3 の AIX0535C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 属性確認 po 0059 {#c01-i0878}
*分類: 性能管理*  ・  難易度: 中級

山吹照合ではAIX 7.3の性能管理で vmo -a を確認します。山吹照合の性能管理では po とsvmon全体表示を照合票へ整理します。山吹照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。山吹照合の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、山吹照合を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 属性確認 po 0059について構成や状態を確認します。lsattr -E -l sys0 -a enhanced_RBAC 状態確認ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。
    - B. 一次資料が示す主目的は性能管理でvmo -aを用い・po とsvmon全体表示を確認する。 ✅
    - C. 一次資料が示す主目的はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。
    - D. 一次資料が示す主目的はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」に対応する項目は属性確認 po（属性・vmo）です。性能管理の仕様は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」で、確認対象はvm・属性です。状態・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。容量・logfのC:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は容量確認 log=INLINE（容量・logf）です。バック・lsusのD:は「セキュリティでlsuserを用い、authorizations」を述べ、対象はバックアウト確認 authoriza（バッ・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」を指し、属性確認 poではvm・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 属性確認 po 0059**

    - 検証目的: 性能管理のvmo -a 属性確認 po 0059について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認059-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0059A
    ```

    画面・出力には AIX0059A が表示され、vmo -a 属性確認 po 0059 の入力欄確認を確認できます。

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
    確認コード AIX0059B
    ```

    画面・出力には AIX0059B が表示され、vmo -a 属性確認 po 0059 の証跡表示確認を確認できます。

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
    確認コード AIX0059C
    ```

    画面・出力には AIX0059C が表示され、vmo -a 属性確認 po 0059 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0059A が画面・出力に表示されること
    ② ステップ2 の AIX0059B が画面・出力に表示されること
    ③ ステップ3 の AIX0059C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 運用引継ぎ pi 0376 {#c01-i0879}
*分類: 性能管理*  ・  難易度: 初級

若竹記録ではAIX 7.3の性能管理で vmo -a を確認します。若竹記録の性能管理では pi とtopasディスク表示を監査票へ転記します。若竹記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若竹記録の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、若竹記録を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 運用引継ぎ pi 0376を同一分類のlsattr -E -l sys0 -a enhanced_RBAC 容量確認と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でvmo -aを用い・pi とtopasディスク表示を確認する。 ✅
    - B. 管理対象との関係を表す説明はセキュリティでlsattr -E -l sys0 -aを用い・roles と監査設定を確認する。
    - C. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。
    - D. 管理対象との関係を表す説明はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でvmo -aを用い、pi とtopasディスク表示を確認する」に対応する項目は運用引継ぎ pi（運用・vmo）です。運用引に関する性能管理の仕様は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」で、確認対象はvm・運用引です。容量・lsatのB:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は容量確認 roles（容量・lsat）です。変更後・spliのC:は「JFS2でsplitcopyを用い、lff」を述べ、対象は変更後確認 lff（変更・spli）です。性能・chvgのD:は「LVMでchvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・chvg）です。「vmo -a」は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」を指し、運用引継ぎ piではvm・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 運用引継ぎ pi 0376**

    - 検証目的: 性能管理のvmo -a 運用引継ぎ pi 0376について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ016-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0376A
    ```

    画面・出力には AIX0376A が表示され、vmo -a 運用引継ぎ pi 0376 の入力欄確認を確認できます。

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
    確認コード AIX0376B
    ```

    画面・出力には AIX0376B が表示され、vmo -a 運用引継ぎ pi 0376 の証跡表示確認を確認できます。

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
    確認コード AIX0376C
    ```

    画面・出力には AIX0376C が表示され、vmo -a 運用引継ぎ pi 0376 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0376A が画面・出力に表示されること
    ② ステップ2 の AIX0376B が画面・出力に表示されること
    ③ ステップ3 の AIX0376C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 バックアウト確認 avm 0815 {#c01-i0880}
*分類: 性能管理*  ・  難易度: 中級

岩清水変更ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。岩清水変更の性能管理では avm とsvmon全体表示を照合票へ整理します。岩清水変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。岩清水変更の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、岩清水変更を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 バックアウト確認 avm 0815の設定や表示を読む前に役割を確認します。lspv 障害切り分け 出力比較ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - B. 一次資料が示す主目的は性能管理でvmstat -c 2 1を用い・avm とsvmon全体表示を確認する。 ✅
    - C. 一次資料が示す主目的はセキュリティでlsroleを用い・roles とロール一覧を確認する。
    - D. 一次資料が示す主目的はデバイス管理でcfgmgrを用い・microcode level と診断対象表示を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** バック・vmstでBの記述「性能管理でvmstat -c 2 1を用い、avm」に対応する項目はバックアウト確認 avm（バッ・vmst）です。バックに関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、avm」で、確認対象はvm・バックです。障害切・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は障害切り分け 出力比較（障害・lspv）です。バック・lsroのC:は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を述べ、対象はバックアウト確認 roles（バッ・lsro）です。バック・cfgmのD:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（バッ・cfgm）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、avm」を指し、バックアウト確認 avmではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 バックアウト確認 avm 0815**

    - 検証目的: 性能管理のvmstat -c 2 1 バックアウト確認 avm 0815について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認095-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0815A
    ```

    画面・出力には AIX0815A が表示され、vmstat -c 2 1 バックアウト確認 avm 0815 の入力欄確認を確認できます。

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
    確認コード AIX0815B
    ```

    画面・出力には AIX0815B が表示され、vmstat -c 2 1 バックアウト確認 avm 0815 の証跡表示確認を確認できます。

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
    確認コード AIX0815C
    ```

    画面・出力には AIX0815C が表示され、vmstat -c 2 1 バックアウト確認 avm 0815 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0815A が画面・出力に表示されること
    ② ステップ2 の AIX0815B が画面・出力に表示されること
    ③ ステップ3 の AIX0815C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 バックアウト確認 fre 0339 {#c01-i0881}
*分類: 性能管理*  ・  難易度: 中級

山吹変更ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。山吹変更の性能管理では fre とsvmon全体表示を作業票へ保管します。山吹変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。山吹変更の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、山吹変更を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 バックアウト確認 fre 0339について構成や状態を確認します。rolelist -u user1 監査記録 roles 0340ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはセキュリティでrolelist -u user1を用い・roles とユーザー属性を確認する。
    - B. 状態を読み取るための働きは性能管理でvmstat -c 2 1を用い・fre とsvmon全体表示を確認する。 ✅
    - C. 状態を読み取るための働きはJFS2でcrfsを用い・lff とマウントオプションを確認する。
    - D. 状態を読み取るための働きはLVMでlsvg -lを用い・STALE PARTITIONS と論理ボリューム配置を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmstat -c 2 1を用い、fre とsvmon全体表示を確認する」に対応する項目はバックアウト確認 fre（バッ・vmst）です。バックに関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、fre」で、確認対象はvm・バックです。監査・roleのA:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は監査記録 roles（監査・role）です。変更前・crfsのC:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。容量・lsvgのD:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（容量・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、fre」を指し、バックアウト確認 freではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 バックアウト確認 fre 0339**

    - 検証目的: 性能管理のvmstat -c 2 1 バックアウト確認 fre 0339について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認099-03
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
    確認コード AIX0339A
    ```

    画面・出力には AIX0339A が表示され、vmstat -c 2 1 バックアウト確認 fre 0339 の入力欄確認を確認できます。

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
    確認コード AIX0339B
    ```

    画面・出力には AIX0339B が表示され、vmstat -c 2 1 バックアウト確認 fre 0339 の証跡表示確認を確認できます。

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
    確認コード AIX0339C
    ```

    画面・出力には AIX0339C が表示され、vmstat -c 2 1 バックアウト確認 fre 0339 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0339A が画面・出力に表示されること
    ② ステップ2 の AIX0339B が画面・出力に表示されること
    ③ ステップ3 の AIX0339C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 性能確認 fre 0497 {#c01-i0882}
*分類: 性能管理*  ・  難易度: 初級

初霜確認ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。初霜確認の性能管理では fre とAME統計を復旧票へ残します。初霜確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。初霜確認の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、初霜確認を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「vmstat -c 2 1 性能確認 fre 0497」を「rolelist -u user1 起動確認 audit class 0498」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はセキュリティでrolelist -u user1を用い・audit class とRBAC属性を確認する。
    - B. 仕様上の役割はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。
    - C. 仕様上の役割は性能管理でvmstat -c 2 1を用い・fre とAME統計を確認する。 ✅
    - D. 仕様上の役割はLVMでlsvgを用い・PVID と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「性能管理でvmstat -c 2 1を用い、fre とAME統計を確認する」に対応する項目は性能確認 fre（性能・vmst）です。性能に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、fre」で、確認対象はvm・性能です。起動・roleのA:は「セキュリティでrolelist -u user1を用い、audit」を述べ、対象はaudit class（起動・role）です。バック・defrのB:は「JFS2でdefragfsを用い、log=INLINE」を述べ、対象はバックアウト確認 log=INLIN（バッ・defr）です。属性・lsvgのD:は「LVMでlsvgを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は属性確認 PVID（属性・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、fre」を指し、性能確認 freではvm・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 性能確認 fre 0497**

    - 検証目的: 性能管理のvmstat -c 2 1 性能確認 fre 0497について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認017-05
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
    確認コード AIX0497A
    ```

    画面・出力には AIX0497A が表示され、vmstat -c 2 1 性能確認 fre 0497 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0497B
    ```

    画面・出力には AIX0497B が表示され、vmstat -c 2 1 性能確認 fre 0497 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0497C
    ```

    画面・出力には AIX0497C が表示され、vmstat -c 2 1 性能確認 fre 0497 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0497A が画面・出力に表示されること
    ② ステップ2 の AIX0497B が画面・出力に表示されること
    ③ ステップ3 の AIX0497C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 性能確認 pi 0021 {#c01-i0883}
*分類: 性能管理*  ・  難易度: 初級

群青確認ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。群青確認の性能管理では pi とAME統計を判定票へ残します。群青確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。群青確認の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、群青確認を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 性能確認 pi 0021を保守記録に説明する必要があります。rolelist -u user1 起動確認 authorizations 0022と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は性能管理でvmstat -c 2 1を用い・pi とAME統計を確認する。 ✅
    - B. 運用時に利用する技術的役割はセキュリティでrolelist -u user1を用い・authorizationsである。
    - C. 運用時に利用する技術的役割はJFS2でdefragfsを用い・lff と内部スナップショットを確認する。
    - D. 運用時に利用する技術的役割はセキュリティでusrck -n ALLを用い・roles とRBAC属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、pi とAME統計を確認する」に対応する項目は性能確認 pi（性能・vmst）です。性能管理の仕様は「性能管理でvmstat -c 2 1を用い、pi とAME統計を確認する」で、確認対象はvm・性能です。起動・roleのB:は「セキュリティでrolelist -u user1を用い」を述べ、対象は起動確認 authorization（起動・role）です。バック・defrのC:は「JFS2でdefragfsを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・defr）です。変更後・usrcのD:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は変更後確認 roles（変更・usrc）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、pi」を指し、性能確認 piではvm・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 性能確認 pi 0021**

    - 検証目的: 性能管理のvmstat -c 2 1 性能確認 pi 0021について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認021-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0021A
    ```

    画面・出力には AIX0021A が表示され、vmstat -c 2 1 性能確認 pi 0021 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0021B
    ```

    画面・出力には AIX0021B が表示され、vmstat -c 2 1 性能確認 pi 0021 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0021C
    ```

    画面・出力には AIX0021C が表示され、vmstat -c 2 1 性能確認 pi 0021 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0021A が画面・出力に表示されること
    ② ステップ2 の AIX0021B が画面・出力に表示されること
    ③ ステップ3 の AIX0021C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 構成照合 avm 0656 {#c01-i0884}
*分類: 性能管理*  ・  難易度: 中級

若竹判定ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。若竹判定の性能管理では avm とtopasディスク表示を引継ぎ票へ保管します。若竹判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若竹判定の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、若竹判定を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 構成照合 avm 0656を同一分類のrolelist -u user1 変更前確認 user attributesと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でvmstat -c 2 1を用い・avm とtopasディスク表示を確認する。 ✅
    - B. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。
    - C. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・bootlist とOSレベル表示を確認する。
    - D. コマンドまたは機能の用途はLVMでlsvgを用い・PP SIZE とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、avm」に対応する項目は構成照合 avm（構成・vmst）です。構成に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、avm」で、確認対象はvm・構成です。変更前・roleのB:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。監査・instのC:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は監査記録 bootlist（監査・inst）です。変更後・lsvgのD:は「LVMでlsvgを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（変更・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、avm」を指し、構成照合 avmではvm・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 構成照合 avm 0656**

    - 検証目的: 性能管理のvmstat -c 2 1 構成照合 avm 0656について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合056-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
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
    確認コード AIX0656A
    ```

    画面・出力には AIX0656A が表示され、vmstat -c 2 1 構成照合 avm 0656 の入力欄確認を確認できます。

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
    確認コード AIX0656B
    ```

    画面・出力には AIX0656B が表示され、vmstat -c 2 1 構成照合 avm 0656 の証跡表示確認を確認できます。

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
    確認コード AIX0656C
    ```

    画面・出力には AIX0656C が表示され、vmstat -c 2 1 構成照合 avm 0656 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0656A が画面・出力に表示されること
    ② ステップ2 の AIX0656B が画面・出力に表示されること
    ③ ステップ3 の AIX0656C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



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


