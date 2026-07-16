---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (15/18)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > 導入と起動

### installp -C 監査記録 mksysb image 0518 {#c01-i0744}
*分類: 導入と起動*  ・  難易度: 中級

春霞確認ではAIX 7.3の導入と起動で installp -C を確認します。春霞確認の導入と起動では mksysb image とOSレベル表示を確認票へ整理します。春霞確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春霞確認の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、春霞確認を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 監査記録 mksysb image 0518に関する障害切り分けの前提を確認しています。entstat -d ent0 運用引継ぎ Link Status 0519の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はネットワークでentstat -d ent0を用い・Link Status とEthernet統計を確認する。
    - B. 障害切り分けに用いる役割はデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。
    - C. 障害切り分けに用いる役割は導入と起動でinstallp -Cを用い・mksysb image とOSレベル表示を確認する。 ✅
    - D. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でinstallp -Cを用い、mksysb image」に対応する項目はmksysb image（監査・inst）です。監査に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、mksysb image」で、確認対象はin・監査です。運用引・entsのA:は「ネットワークでentstat -d ent0を用い、Link」を述べ、対象はLink Status（運用・ents）です。変更前・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。容量・roleのD:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。「installp -C」は「導入と起動でinstallp -Cを用い、mksysb image」を指し、mksysb imageではin・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 監査記録 mksysb image 0518**

    - 検証目的: 導入と起動のinstallp -C 監査記録 mksysb image 0518について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録038-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0518A
    ```

    画面・出力には AIX0518A が表示され、installp -C 監査記録 mksysb image 0518 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0518B
    ```

    画面・出力には AIX0518B が表示され、installp -C 監査記録 mksysb image 0518 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0518C
    ```

    画面・出力には AIX0518C が表示され、installp -C 監査記録 mksysb image 0518 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0518A が画面・出力に表示されること
    ② ステップ2 の AIX0518B が画面・出力に表示されること
    ③ ステップ3 の AIX0518C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 起動確認 EFIX LABEL 0677 {#c01-i0745}
*分類: 導入と起動*  ・  難易度: 中級

冬晴判定ではAIX 7.3の導入と起動で installp -C を確認します。冬晴判定の導入と起動では EFIX LABEL と起動デバイス設定を復旧票へ残します。冬晴判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。冬晴判定の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、冬晴判定を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 起動確認 EFIX LABEL 0677を保守記録に説明する必要があります。entstat -d ent0 属性確認 MTU 0678と取り違えない説明はどれですか。

    - A. 仕様上の役割はネットワークでentstat -d ent0を用い・MTU とアダプター一覧を確認する。
    - B. 仕様上の役割は導入と起動でinstallp -Cを用い・EFIX LABEL と起動デバイス設定を確認する。 ✅
    - C. 仕様上の役割はJFS2でmount -o remountを用い・isnapshot と内部スナップショットを確認する。
    - D. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でinstallp -Cを用い、EFIX LABEL」に対応する項目はEFIX LABEL（起動・inst）です。起動に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、EFIX LABEL」で、確認対象はin・起動です。属性・entsのA:は「ネットワークでentstat -d ent0を用い、MTU」を述べ、対象は属性確認 MTU（属性・ents）です。変更後・mounのC:は「JFS2でmount -o remountを用い」を述べ、対象は変更後確認 isnapshot（変更・moun）です。構成・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（構成・rbac）です。「installp -C」は「導入と起動でinstallp -Cを用い、EFIX LABEL」を指し、EFIX LABELではin・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 起動確認 EFIX LABEL 0677**

    - 検証目的: 導入と起動のinstallp -C 起動確認 EFIX LABEL 0677について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認077-06
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
    確認コード AIX0677A
    ```

    画面・出力には AIX0677A が表示され、installp -C 起動確認 EFIX LABEL 0677 の入力欄確認を確認できます。

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
    確認コード AIX0677B
    ```

    画面・出力には AIX0677B が表示され、installp -C 起動確認 EFIX LABEL 0677 の証跡表示確認を確認できます。

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
    確認コード AIX0677C
    ```

    画面・出力には AIX0677C が表示され、installp -C 起動確認 EFIX LABEL 0677 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0677A が画面・出力に表示されること
    ② ステップ2 の AIX0677B が画面・出力に表示されること
    ③ ステップ3 の AIX0677C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 起動確認 Technology Level 0201 {#c01-i0746}
*分類: 導入と起動*  ・  難易度: 中級

白露保守ではAIX 7.3の導入と起動で installp -C を確認します。白露保守の導入と起動では Technology Level と起動デバイス設定を判定票へ残します。白露保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。白露保守の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、白露保守を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「installp -C 起動確認 Technology Level 0201」を「entstat -d ent0 属性確認 Link Status 0202」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はネットワークでentstat -d ent0を用い・Link Status とアダプター一覧を確認する。
    - B. 運用時に利用する技術的役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。
    - C. 運用時に利用する技術的役割は導入と起動でinstallp -Cを用い・Technology Level と起動デバイス設定を確認する。 ✅
    - D. 運用時に利用する技術的役割はネットワークでlsdev -Cc adapterを用い・EtherChannel とアダプター一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でinstallp -Cを用い、Technology Level」に対応する項目はTechnology Level（起動・inst）です。起動に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、Technology」で、確認対象はin・起動です。属性・entsのA:は「ネットワークでentstat -d ent0を用い、Link」を述べ、対象はLink Status（属性・ents）です。運用引・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。障害切・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け EtherChanne（障害・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、Technology」を指し、Technology Levelではin・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 起動確認 Technology Level 0201**

    - 検証目的: 導入と起動のinstallp -C 起動確認 Technology Level 0201について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認081-02
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
    確認コード AIX0201A
    ```

    画面・出力には AIX0201A が表示され、installp -C 起動確認 Technology Level 0201 の入力欄確認を確認できます。

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
    確認コード AIX0201B
    ```

    画面・出力には AIX0201B が表示され、installp -C 起動確認 Technology Level 0201 の証跡表示確認を確認できます。

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
    確認コード AIX0201C
    ```

    画面・出力には AIX0201C が表示され、installp -C 起動確認 Technology Level 0201 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0201A が画面・出力に表示されること
    ② ステップ2 の AIX0201B が画面・出力に表示されること
    ③ ステップ3 の AIX0201C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 障害切り分け bootlist 0231 {#c01-i0747}
*分類: 導入と起動*  ・  難易度: 上級

遠雷保守ではAIX 7.3の導入と起動で installp -C を確認します。遠雷保守の導入と起動では bootlist とfileset一覧を作業票へ保管します。遠雷保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。遠雷保守の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、遠雷保守を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 障害切り分け bootlist 0231の設定や表示を読む前に役割を確認します。entstat -d ent0 バックアウト確認 Destination 0232ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはネットワークでentstat -d ent0を用い・Destination と経路表を確認する。
    - B. 状態を読み取るための働きはデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。
    - C. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - D. 状態を読み取るための働きは導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「導入と起動でinstallp -Cを用い、bootlist」に対応する項目は障害切り分け bootlist（障害・inst）です。障害切に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、bootlist」で、確認対象はin・障害切です。バック・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 Destinati（バッ・ents）です。構成・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。属性・属性・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は属性照合 属性確認（属性・lsps）です。「installp -C」は「導入と起動でinstallp -Cを用い、bootlist」を指し、障害切り分け bootlistではin・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 障害切り分け bootlist 0231**

    - 検証目的: 導入と起動のinstallp -C 障害切り分け bootlist 0231について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け111-02
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
    確認コード AIX0231A
    ```

    画面・出力には AIX0231A が表示され、installp -C 障害切り分け bootlist 0231 の入力欄確認を確認できます。

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
    確認コード AIX0231B
    ```

    画面・出力には AIX0231B が表示され、installp -C 障害切り分け bootlist 0231 の証跡表示確認を確認できます。

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
    確認コード AIX0231C
    ```

    画面・出力には AIX0231C が表示され、installp -C 障害切り分け bootlist 0231 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0231A が画面・出力に表示されること
    ② ステップ2 の AIX0231B が画面・出力に表示されること
    ③ ステップ3 の AIX0231C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### installp -C 障害切り分け mksysb image 0707 {#c01-i0748}
*分類: 導入と起動*  ・  難易度: 上級

風花保守ではAIX 7.3の導入と起動で installp -C を確認します。風花保守の導入と起動では mksysb image とfileset一覧を照合票へ整理します。風花保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。風花保守の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、風花保守を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** installp -C 障害切り分け mksysb image 0707について構成や状態を確認します。entstat -d ent0 バックアウト確認 EtherChannel 0708ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はネットワークでentstat -d ent0を用い・EtherChannel と経路表を確認する。
    - B. 一次資料が示す主目的はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。
    - C. 一次資料が示す主目的は導入と起動でinstallp -Cを用い・mksysb image とfileset一覧を確認する。 ✅
    - D. 一次資料が示す主目的はセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「導入と起動でinstallp -Cを用い、mksysb image」に対応する項目はmksysb image（障害・inst）です。障害切に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、mksysb image」で、確認対象はin・障害切です。バック・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 EtherChan（バッ・ents）です。性能・ファ・mounのB:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 ファイルシステム使用率（性能・moun）です。運用引・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（運用・rbac）です。「installp -C」は「導入と起動でinstallp -Cを用い、mksysb image」を指し、mksysb imageではin・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **installp -C 障害切り分け mksysb image 0707**

    - 検証目的: 導入と起動のinstallp -C 障害切り分け mksysb image 0707について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け107-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> installp -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0707A
    ```

    画面・出力には AIX0707A が表示され、installp -C 障害切り分け mksysb image 0707 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0707B
    ```

    画面・出力には AIX0707B が表示され、installp -C 障害切り分け mksysb image 0707 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0707C
    ```

    画面・出力には AIX0707C が表示され、installp -C 障害切り分け mksysb image 0707 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0707A が画面・出力に表示されること
    ② ステップ2 の AIX0707B が画面・出力に表示されること
    ③ ステップ3 の AIX0707C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L バックアウト確認 altinst_rootvg 0458 {#c01-i0749}
*分類: 導入と起動*  ・  難易度: 中級

潮騒整理ではAIX 7.3の導入と起動で lslpp -L を確認します。潮騒整理の導入と起動では altinst_rootvg とOSレベル表示を確認票へ整理します。潮騒整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。潮騒整理の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、潮騒整理を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L バックアウト確認 altinst_rootvg 0458の役割を調べています。chdev -l en0 -a mtu=1500 監査記録の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はネットワークでchdev -l en0 -aを用い・EtherChannelである。
    - B. 障害切り分けに用いる役割はデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。
    - C. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。
    - D. 障害切り分けに用いる役割は導入と起動でlslpp -Lを用い・altinst_rootvg とOSレベル表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でlslpp -Lを用い、altinst_rootvg」に対応する項目はバックアウト確認 altinst_r（バッ・lslp）です。バックに関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、altinst_rootvg」で、確認対象はls・バックです。監査・chdeのA:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は監査記録 EtherChannel（監査・chde）です。変更前・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。容量・roleのC:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、altinst_rootvg」を指し、バックアウト確認 altinst_rではls・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L バックアウト確認 altinst_rootvg 0458**

    - 検証目的: 導入と起動のlslpp -L バックアウト確認 altinst_rootvg 0458について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認098-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0458A
    ```

    画面・出力には AIX0458A が表示され、lslpp -L バックアウト確認 altinst_rootvg 0458 の入力欄確認を確認できます。

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
    確認コード AIX0458B
    ```

    画面・出力には AIX0458B が表示され、lslpp -L バックアウト確認 altinst_rootvg 0458 の証跡表示確認を確認できます。

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
    確認コード AIX0458C
    ```

    画面・出力には AIX0458C が表示され、lslpp -L バックアウト確認 altinst_rootvg 0458 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0458A が画面・出力に表示されること
    ② ステップ2 の AIX0458B が画面・出力に表示されること
    ③ ステップ3 の AIX0458C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 性能確認 fileset level 0616 {#c01-i0750}
*分類: 導入と起動*  ・  難易度: 初級

若竹採取ではAIX 7.3の導入と起動で lslpp -L を確認します。若竹採取の導入と起動では fileset level と代替ディスク状態を監査票へ転記します。若竹採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若竹採取の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若竹採取を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 性能確認 fileset level 0616を同一分類のchdev -l en0 -a mtu=1500 起動確認 MTU 0617と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでchdev -l en0 -aを用い・MTU とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・agblksize とファイルシステム属性を確認する。lsfs -q 変更前確認 agblksize 0002固有の属性も確認対象に含める。
    - C. 管理対象との関係を表す説明は導入と起動でlslpp -Lを用い・fileset level と代替ディスク状態を確認する。 ✅
    - D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・roles と監査設定を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でlslpp -Lを用い、fileset level」に対応する項目はfileset level（性能・lslp）です。性能に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、fileset level」で、確認対象はls・性能です。起動・chdeのA:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は起動確認 MTU（起動・chde）です。変更前・lsfsのB:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は変更前確認 agblksize（変更・lsfs）です。属性・lsroのD:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、fileset level」を指し、fileset levelではls・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 性能確認 fileset level 0616**

    - 検証目的: 導入と起動のlslpp -L 性能確認 fileset level 0616について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認016-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0616A
    ```

    画面・出力には AIX0616A が表示され、lslpp -L 性能確認 fileset level 0616 の入力欄確認を確認できます。

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
    確認コード AIX0616B
    ```

    画面・出力には AIX0616B が表示され、lslpp -L 性能確認 fileset level 0616 の証跡表示確認を確認できます。

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
    確認コード AIX0616C
    ```

    画面・出力には AIX0616C が表示され、lslpp -L 性能確認 fileset level 0616 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0616A が画面・出力に表示されること
    ② ステップ2 の AIX0616B が画面・出力に表示されること
    ③ ステップ3 の AIX0616C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 性能確認 mksysb image 0140 {#c01-i0751}
*分類: 導入と起動*  ・  難易度: 初級

薄明採取ではAIX 7.3の導入と起動で lslpp -L を確認します。薄明採取の導入と起動では mksysb image と代替ディスク状態を引継ぎ票へ保管します。薄明採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。薄明採取の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、薄明採取を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 性能確認 mksysb image 0140の技術的な意味を資料で確認するとき、chdev -l en0 -a mtu=1500 起動確認 Link Statusとの境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでchdev -l en0 -aを用い・Link Status とMTU属性を確認する。
    - B. コマンドまたは機能の用途はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。
    - C. コマンドまたは機能の用途は導入と起動でlslpp -Lを用い・mksysb image と代替ディスク状態を確認する。 ✅
    - D. コマンドまたは機能の用途はネットワークでcfgmgrを用い・EtherChannel とMTU属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でlslpp -Lを用い、mksysb image」に対応する項目はmksysb image（性能・lslp）です。性能に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、mksysb image」で、確認対象はls・性能です。起動・chdeのA:は「ネットワークでchdev -l en0 -aを用い、Link」を述べ、対象はLink Status（起動・chde）です。バック・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。変更後・cfgmのD:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は変更後確認 EtherChannel（変更・cfgm）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、mksysb image」を指し、mksysb imageではls・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 性能確認 mksysb image 0140**

    - 検証目的: 導入と起動のlslpp -L 性能確認 mksysb image 0140について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認020-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0140A
    ```

    画面・出力には AIX0140A が表示され、lslpp -L 性能確認 mksysb image 0140 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0140B
    ```

    画面・出力には AIX0140B が表示され、lslpp -L 性能確認 mksysb image 0140 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0140C
    ```

    画面・出力には AIX0140C が表示され、lslpp -L 性能確認 mksysb image 0140 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0140A が画面・出力に表示されること
    ② ステップ2 の AIX0140B が画面・出力に表示されること
    ③ ステップ3 の AIX0140C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 構成照合 EFIX LABEL 0299 {#c01-i0752}
*分類: 導入と起動*  ・  難易度: 中級

山吹復旧ではAIX 7.3の導入と起動で lslpp -L を確認します。山吹復旧の導入と起動では EFIX LABEL とfileset一覧を照合票へ整理します。山吹復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。山吹復旧の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、山吹復旧を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 構成照合 EFIX LABEL 0299について構成や状態を確認します。chdev -l en0 -a mtu=1500 変更前確認 MTU 0300ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。
    - B. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。
    - C. 一次資料が示す主目的は導入と起動でlslpp -Lを用い・EFIX LABEL とfileset一覧を確認する。 ✅
    - D. 一次資料が示す主目的はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でlslpp -Lを用い、EFIX LABEL」に対応する項目はEFIX LABEL（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、EFIX LABEL」で、確認対象はls・構成です。変更前・chdeのA:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。起動・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。変更前・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は変更前確認 再開位置（変更・lsvg）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、EFIX LABEL」を指し、EFIX LABELではls・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 構成照合 EFIX LABEL 0299**

    - 検証目的: 導入と起動のlslpp -L 構成照合 EFIX LABEL 0299について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合059-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0299A
    ```

    画面・出力には AIX0299A が表示され、lslpp -L 構成照合 EFIX LABEL 0299 の入力欄確認を確認できます。

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
    確認コード AIX0299B
    ```

    画面・出力には AIX0299B が表示され、lslpp -L 構成照合 EFIX LABEL 0299 の証跡表示確認を確認できます。

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
    確認コード AIX0299C
    ```

    画面・出力には AIX0299C が表示され、lslpp -L 構成照合 EFIX LABEL 0299 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0299A が画面・出力に表示されること
    ② ステップ2 の AIX0299B が画面・出力に表示されること
    ③ ステップ3 の AIX0299C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 構成照合 EFIX LABEL 0359 {#c01-i0753}
*分類: 導入と起動*  ・  難易度: 上級

秋桜変更ではAIX 7.3の導入と起動で lslpp -L を確認します。秋桜変更の導入と起動では EFIX LABEL とfileset一覧を照合票へ整理します。秋桜変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋桜変更の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、秋桜変更を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 構成照合 EFIX LABEL 0359の設定や表示を読む前に役割を確認します。chdev -l en0 -a mtu=1500 変更前確認 MTU 0360ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は導入と起動でlslpp -Lを用い・EFIX LABEL とfileset一覧を確認する。 ✅
    - B. 一次資料が示す主目的はネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。
    - C. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。
    - D. 一次資料が示す主目的はセキュリティでrolelist -u user1を用い・authorizationsである。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「導入と起動でlslpp -Lを用い、EFIX LABEL」に対応する項目はEFIX LABEL（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、EFIX LABEL」で、確認対象はls・構成です。変更前・chdeのB:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。起動・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。障害切・roleのD:は「セキュリティでrolelist -u user1を用い」を述べ、対象は障害切り分け authorizati（障害・role）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、EFIX LABEL」を指し、EFIX LABELではls・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 構成照合 EFIX LABEL 0359**

    - 検証目的: 導入と起動のlslpp -L 構成照合 EFIX LABEL 0359について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合119-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0359A
    ```

    画面・出力には AIX0359A が表示され、lslpp -L 構成照合 EFIX LABEL 0359 の入力欄確認を確認できます。

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
    確認コード AIX0359B
    ```

    画面・出力には AIX0359B が表示され、lslpp -L 構成照合 EFIX LABEL 0359 の証跡表示確認を確認できます。

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
    確認コード AIX0359C
    ```

    画面・出力には AIX0359C が表示され、lslpp -L 構成照合 EFIX LABEL 0359 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0359A が画面・出力に表示されること
    ② ステップ2 の AIX0359B が画面・出力に表示されること
    ③ ステップ3 の AIX0359C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 構成照合 altinst_rootvg 0775 {#c01-i0754}
*分類: 導入と起動*  ・  難易度: 中級

岩清水復旧ではAIX 7.3の導入と起動で lslpp -L を確認します。岩清水復旧の導入と起動では altinst_rootvg とfileset一覧を点検票へ整理します。岩清水復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。岩清水復旧の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、岩清水復旧を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 構成照合 altinst_rootvg 0775の設定や表示を読む前に役割を確認します。mksysb 起動確認 EFIX LABEL 0820ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。
    - B. 対象資源に対する働きはSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。startsrc -s inetd -a "-d" 障害切り分け固有の属性も確認対象に含める。
    - C. 対象資源に対する働きは導入と起動でlslpp -Lを用い・altinst_rootvg とfileset一覧を確認する。 ✅
    - D. 対象資源に対する働きはデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** 構成・lslpでCの記述「導入と起動でlslpp -Lを用い、altinst_rootvg」に対応する項目は構成照合 altinst_rootv（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、altinst_rootvg」で、確認対象はls・構成です。起動・mksyのA:は「導入と起動でmksysbを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（起動・mksy）です。障害切・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。状態・odmgのD:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、altinst_rootvg」を指し、構成照合 altinst_rootvではls・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 構成照合 altinst_rootvg 0775**

    - 検証目的: 導入と起動のlslpp -L 構成照合 altinst_rootvg 0775について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合055-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0775A
    ```

    画面・出力には AIX0775A が表示され、lslpp -L 構成照合 altinst_rootvg 0775 の入力欄確認を確認できます。

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
    確認コード AIX0775B
    ```

    画面・出力には AIX0775B が表示され、lslpp -L 構成照合 altinst_rootvg 0775 の証跡表示確認を確認できます。

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
    確認コード AIX0775C
    ```

    画面・出力には AIX0775C が表示され、lslpp -L 構成照合 altinst_rootvg 0775 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0775A が画面・出力に表示されること
    ② ステップ2 の AIX0775B が画面・出力に表示されること
    ③ ステップ3 の AIX0775C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 構成照合 altinst_rootvg 0835 {#c01-i0755}
*分類: 導入と起動*  ・  難易度: 上級

青磁変更ではAIX 7.3の導入と起動で lslpp -L を確認します。青磁変更の導入と起動では altinst_rootvg とfileset一覧を点検票へ整理します。青磁変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。青磁変更の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、青磁変更を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 構成照合 altinst_rootvg 0835について構成や状態を確認します。lspv 性能確認 保持設定ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - B. 対象資源に対する働きは導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。
    - C. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。
    - D. 対象資源に対する働きは導入と起動でlslpp -Lを用い・altinst_rootvg とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 構成・lslpでDの記述「導入と起動でlslpp -Lを用い、altinst_rootvg」に対応する項目は構成照合 altinst_rootv（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、altinst_rootvg」で、確認対象はls・構成です。性能・保持・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は性能確認 保持設定（性能・lspv）です。容量・alt_のB:は「導入と起動でalt_disk_copyを用い、mksysb」を述べ、対象はmksysb image（容量・alt_）です。性能・setsのC:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、altinst_rootvg」を指し、構成照合 altinst_rootvではls・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 構成照合 altinst_rootvg 0835**

    - 検証目的: 導入と起動のlslpp -L 構成照合 altinst_rootvg 0835について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合115-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0835A
    ```

    画面・出力には AIX0835A が表示され、lslpp -L 構成照合 altinst_rootvg 0835 の入力欄確認を確認できます。

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
    確認コード AIX0835B
    ```

    画面・出力には AIX0835B が表示され、lslpp -L 構成照合 altinst_rootvg 0835 の証跡表示確認を確認できます。

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
    確認コード AIX0835C
    ```

    画面・出力には AIX0835C が表示され、lslpp -L 構成照合 altinst_rootvg 0835 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0835A が画面・出力に表示されること
    ② ステップ2 の AIX0835B が画面・出力に表示されること
    ③ ステップ3 の AIX0835C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 運用引継ぎ fileset level 0745 {#c01-i0756}
*分類: 導入と起動*  ・  難易度: 中級

花冷監査ではAIX 7.3の導入と起動で lslpp -L を確認します。花冷監査の導入と起動では fileset level と起動デバイス設定を採取票へ記録します。花冷監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。花冷監査の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、花冷監査を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「lslpp -L 運用引継ぎ fileset level 0745」を「chdev -l en0 -a mtu=1500 容量確認 Media Speed」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。
    - B. 保守作業で参照する機能は導入と起動でlslpp -Lを用い・fileset level と起動デバイス設定を確認する。 ✅
    - C. 保守作業で参照する機能はJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。
    - D. 保守作業で参照する機能はセキュリティでlsroleを用い・roles とRBAC属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でlslpp -Lを用い、fileset level」に対応する項目はfileset level（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、fileset level」で、確認対象はls・運用引です。容量・chdeのA:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・lsfs）です。性能・lsroのD:は「セキュリティでlsroleを用い、roles」を述べ、対象は性能確認 roles（性能・lsro）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、fileset level」を指し、fileset levelではls・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 運用引継ぎ fileset level 0745**

    - 検証目的: 導入と起動のlslpp -L 運用引継ぎ fileset level 0745について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ025-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0745A
    ```

    画面・出力には AIX0745A が表示され、lslpp -L 運用引継ぎ fileset level 0745 の入力欄確認を確認できます。

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
    確認コード AIX0745B
    ```

    画面・出力には AIX0745B が表示され、lslpp -L 運用引継ぎ fileset level 0745 の証跡表示確認を確認できます。

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
    確認コード AIX0745C
    ```

    画面・出力には AIX0745C が表示され、lslpp -L 運用引継ぎ fileset level 0745 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0745A が画面・出力に表示されること
    ② ステップ2 の AIX0745B が画面・出力に表示されること
    ③ ステップ3 の AIX0745C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 運用引継ぎ fileset level 0805 {#c01-i0757}
*分類: 導入と起動*  ・  難易度: 中級

深雪変更ではAIX 7.3の導入と起動で lslpp -L を確認します。深雪変更の導入と起動では fileset level と起動デバイス設定を採取票へ記録します。深雪変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。深雪変更の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、深雪変更を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 運用引継ぎ fileset level 0805を保守記録に説明する必要があります。lsattr 詳細確認 確認範囲と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は導入と起動でlslpp -Lを用い・fileset level と起動デバイス設定を確認する。 ✅
    - B. 保守作業で参照する機能はデバイスや sys0 などの属性値を表示するコマンドである。
    - C. 保守作業で参照する機能はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。
    - D. 保守作業で参照する機能は導入と起動でbosboot -a -dを用い・fileset level と起動デバイス設定を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** 運用引・lslpでAの記述「導入と起動でlslpp -Lを用い、fileset level」に対応する項目はfileset level（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、fileset level」で、確認対象はls・運用引です。詳細・確認・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は詳細確認 確認範囲（詳細・lsat）です。性能・migrのC:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・migr）です。性能・bosbのD:は「導入と起動でbosboot -a -dを用い、fileset」を述べ、対象はfileset level（性能・bosb）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、fileset level」を指し、fileset levelではls・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 運用引継ぎ fileset level 0805**

    - 検証目的: 導入と起動のlslpp -L 運用引継ぎ fileset level 0805について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ085-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0805A
    ```

    画面・出力には AIX0805A が表示され、lslpp -L 運用引継ぎ fileset level 0805 の入力欄確認を確認できます。

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
    確認コード AIX0805B
    ```

    画面・出力には AIX0805B が表示され、lslpp -L 運用引継ぎ fileset level 0805 の証跡表示確認を確認できます。

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
    確認コード AIX0805C
    ```

    画面・出力には AIX0805C が表示され、lslpp -L 運用引継ぎ fileset level 0805 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0805A が画面・出力に表示されること
    ② ステップ2 の AIX0805B が画面・出力に表示されること
    ③ ステップ3 の AIX0805C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 運用引継ぎ mksysb image 0269 {#c01-i0758}
*分類: 導入と起動*  ・  難易度: 中級

梅雨晴監査ではAIX 7.3の導入と起動で lslpp -L を確認します。梅雨晴監査の導入と起動では mksysb image と起動デバイス設定を復旧票へ残します。梅雨晴監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。梅雨晴監査の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、梅雨晴監査を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lslpp -L 運用引継ぎ mksysb image 0269を保守記録に説明する必要があります。chdev -l en0 -a mtu=1500 容量確認と取り違えない説明はどれですか。

    - A. 仕様上の役割はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。
    - B. 仕様上の役割は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。 ✅
    - C. 仕様上の役割はデバイス管理でlsmpio -l hdisk0を用い・path status とODM属性を確認する。
    - D. 仕様上の役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でlslpp -Lを用い、mksysb image」に対応する項目はmksysb image（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、mksysb image」で、確認対象はls・運用引です。容量・chdeのA:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。変更後・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（変更・lsmp）です。性能・資料・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は性能確認 資料見出し（性能・lsvg）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、mksysb image」を指し、mksysb imageではls・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 運用引継ぎ mksysb image 0269**

    - 検証目的: 導入と起動のlslpp -L 運用引継ぎ mksysb image 0269について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ029-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0269A
    ```

    画面・出力には AIX0269A が表示され、lslpp -L 運用引継ぎ mksysb image 0269 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0269B
    ```

    画面・出力には AIX0269B が表示され、lslpp -L 運用引継ぎ mksysb image 0269 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0269C
    ```

    画面・出力には AIX0269C が表示され、lslpp -L 運用引継ぎ mksysb image 0269 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0269A が画面・出力に表示されること
    ② ステップ2 の AIX0269B が画面・出力に表示されること
    ③ ステップ3 の AIX0269C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lslpp -L 運用引継ぎ mksysb image 0329 {#c01-i0759}
*分類: 導入と起動*  ・  難易度: 中級

銀砂変更ではAIX 7.3の導入と起動で lslpp -L を確認します。銀砂変更の導入と起動では mksysb image と起動デバイス設定を復旧票へ残します。銀砂変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。銀砂変更の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、銀砂変更を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「lslpp -L 運用引継ぎ mksysb image 0329」を「chdev -l en0 -a mtu=1500 容量確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。
    - B. 仕様上の役割は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。 ✅
    - C. 仕様上の役割はデバイス管理でlsdev -Cc diskを用い・microcode level とODM属性を確認する。
    - D. 仕様上の役割はセキュリティでrolelist -u user1を用い・authorizationsである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でlslpp -Lを用い、mksysb image」に対応する項目はmksysb image（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、mksysb image」で、確認対象はls・運用引です。容量・chdeのA:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。障害切・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（障害・lsde）です。起動・roleのD:は「セキュリティでrolelist -u user1を用い」を述べ、対象は起動確認 authorization（起動・role）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、mksysb image」を指し、mksysb imageではls・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lslpp -L 運用引継ぎ mksysb image 0329**

    - 検証目的: 導入と起動のlslpp -L 運用引継ぎ mksysb image 0329について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ089-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0329A
    ```

    画面・出力には AIX0329A が表示され、lslpp -L 運用引継ぎ mksysb image 0329 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0329B
    ```

    画面・出力には AIX0329B が表示され、lslpp -L 運用引継ぎ mksysb image 0329 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0329C
    ```

    画面・出力には AIX0329C が表示され、lslpp -L 運用引継ぎ mksysb image 0329 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0329A が画面・出力に表示されること
    ② ステップ2 の AIX0329B が画面・出力に表示されること
    ③ ステップ3 の AIX0329C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 容量確認 Technology Level 0473 {#c01-i0760}
*分類: 導入と起動*  ・  難易度: 上級

朝霧整理ではAIX 7.3の導入と起動で mksysb を確認します。朝霧整理の導入と起動では Technology Level と起動デバイス設定を復旧票へ残します。朝霧整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。朝霧整理の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、朝霧整理を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「mksysb 容量確認 Technology Level 0473」を「no -a 性能確認 Link Status 0474」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。
    - B. 仕様上の役割はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。
    - C. 仕様上の役割はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。lsuser 属性確認 user attributes 0166固有の属性も確認対象に含める。
    - D. 仕様上の役割は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（容量・mksy）です。容量に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・容量です。性能・noのA:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（性能・no）です。バック・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。属性・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（属性・lsus）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 容量確認 Technology Level 0473**

    - 検証目的: 導入と起動のmksysb 容量確認 Technology Level 0473について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認113-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0473A
    ```

    画面・出力には AIX0473A が表示され、mksysb 容量確認 Technology Level 0473 の入力欄確認を確認できます。

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
    確認コード AIX0473B
    ```

    画面・出力には AIX0473B が表示され、mksysb 容量確認 Technology Level 0473 の証跡表示確認を確認できます。

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
    確認コード AIX0473C
    ```

    画面・出力には AIX0473C が表示され、mksysb 容量確認 Technology Level 0473 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0473A が画面・出力に表示されること
    ② ステップ2 の AIX0473B が画面・出力に表示されること
    ③ ステップ3 の AIX0473C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 状態確認 bootlist 0631 {#c01-i0761}
*分類: 導入と起動*  ・  難易度: 中級

遠雷採取ではAIX 7.3の導入と起動で mksysb を確認します。遠雷採取の導入と起動では bootlist とfileset一覧を点検票へ整理します。遠雷採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。遠雷採取の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、遠雷採取を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 状態確認 bootlist 0631の設定や表示を読む前に役割を確認します。no -a 構成照合 Destination 0632ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはネットワークでno -aを用い・Destination と経路表を確認する。
    - B. 対象資源に対する働きはLVMでmigratepvを用い・PP SIZE とミラーコピー状態を確認する。
    - C. 対象資源に対する働きは導入と起動でmksysbを用い・bootlist とfileset一覧を確認する。 ✅
    - D. 対象資源に対する働きはセキュリティでchuserを用い・user attributes とユーザー属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でmksysbを用い、bootlist とfileset一覧を確認する」に対応する項目は状態確認 bootlist（状態・mksy）です。状態に関する導入と起動の仕様は「導入と起動でmksysbを用い、bootlist」で、確認対象はmk・状態です。構成・noのA:は「ネットワークでno -aを用い、Destination」を述べ、対象は構成照合 Destination（構成・no）です。バック・migrのB:は「LVMでmigratepvを用い、PP SIZE」を述べ、対象はPP SIZE（バッ・migr）です。変更前・chusのD:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。「mksysb」は「導入と起動でmksysbを用い、bootlist」を指し、状態確認 bootlistではmk・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 状態確認 bootlist 0631**

    - 検証目的: 導入と起動のmksysb 状態確認 bootlist 0631について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認031-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0631A
    ```

    画面・出力には AIX0631A が表示され、mksysb 状態確認 bootlist 0631 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0631B
    ```

    画面・出力には AIX0631B が表示され、mksysb 状態確認 bootlist 0631 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0631C
    ```

    画面・出力には AIX0631C が表示され、mksysb 状態確認 bootlist 0631 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0631A が画面・出力に表示されること
    ② ステップ2 の AIX0631B が画面・出力に表示されること
    ③ ステップ3 の AIX0631C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 状態確認 fileset level 0155 {#c01-i0762}
*分類: 導入と起動*  ・  難易度: 中級

青磁採取ではAIX 7.3の導入と起動で mksysb を確認します。青磁採取の導入と起動では fileset level とfileset一覧を照合票へ整理します。青磁採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。青磁採取の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、青磁採取を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 状態確認 fileset level 0155について構成や状態を確認します。no -a 構成照合 Media Speed Running 0156ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はネットワークでno -aを用い・Media Speed Running と経路表を確認する。
    - B. 一次資料が示す主目的はデバイス管理でodmget CuDvを用い・Available と診断対象表示を確認する。
    - C. 一次資料が示す主目的は導入と起動でmksysbを用い・fileset level とfileset一覧を確認する。 ✅
    - D. 一次資料が示す主目的はネットワークでnetstat -rnを用い・Link Status と経路表を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でmksysbを用い、fileset level」に対応する項目はfileset level（状態・mksy）です。状態に関する導入と起動の仕様は「導入と起動でmksysbを用い、fileset level」で、確認対象はmk・状態です。構成・noのA:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（構成・no）です。容量・odmgのB:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は容量確認 Available（容量・odmg）です。監査・netsのD:は「ネットワークでnetstat -rnを用い、Link Status」を述べ、対象はLink Status（監査・nets）です。「mksysb」は「導入と起動でmksysbを用い、fileset level」を指し、fileset levelではmk・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 状態確認 fileset level 0155**

    - 検証目的: 導入と起動のmksysb 状態確認 fileset level 0155について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認035-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0155A
    ```

    画面・出力には AIX0155A が表示され、mksysb 状態確認 fileset level 0155 の入力欄確認を確認できます。

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
    確認コード AIX0155B
    ```

    画面・出力には AIX0155B が表示され、mksysb 状態確認 fileset level 0155 の証跡表示確認を確認できます。

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
    確認コード AIX0155C
    ```

    画面・出力には AIX0155C が表示され、mksysb 状態確認 fileset level 0155 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0155A が画面・出力に表示されること
    ② ステップ2 の AIX0155B が画面・出力に表示されること
    ③ ステップ3 の AIX0155C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 監査記録 Technology Level 0601 {#c01-i0763}
*分類: 導入と起動*  ・  難易度: 初級

白露採取ではAIX 7.3の導入と起動で mksysb を確認します。白露採取の導入と起動では Technology Level と起動デバイス設定を採取票へ記録します。白露採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露採取の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、白露採取を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「mksysb 監査記録 Technology Level 0601」を「no -a 運用引継ぎ Link Status 0602」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。 ✅
    - B. 保守作業で参照する機能はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。
    - C. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。
    - D. 保守作業で参照する機能はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。chuser 容量確認 user attributes 0294固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（監査・mksy）です。監査に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・監査です。運用引・noのB:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（運用・no）です。一覧・一致・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は一覧確認 一致条件（一覧・chde）です。容量・chusのD:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 監査記録 Technology Level 0601**

    - 検証目的: 導入と起動のmksysb 監査記録 Technology Level 0601について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録001-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0601A
    ```

    画面・出力には AIX0601A が表示され、mksysb 監査記録 Technology Level 0601 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0601B
    ```

    画面・出力には AIX0601B が表示され、mksysb 監査記録 Technology Level 0601 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0601C
    ```

    画面・出力には AIX0601C が表示され、mksysb 監査記録 Technology Level 0601 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0601A が画面・出力に表示されること
    ② ステップ2 の AIX0601B が画面・出力に表示されること
    ③ ステップ3 の AIX0601C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 監査記録 altinst_rootvg 0125 {#c01-i0764}
*分類: 導入と起動*  ・  難易度: 初級

深雪採取ではAIX 7.3の導入と起動で mksysb を確認します。深雪採取の導入と起動では altinst_rootvg と起動デバイス設定を復旧票へ残します。深雪採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。深雪採取の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、深雪採取を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 監査記録 altinst_rootvg 0125を保守記録に説明する必要があります。no -a 運用引継ぎ Gateway 0126と取り違えない説明はどれですか。

    - A. 仕様上の役割はネットワークでno -aを用い・Gateway とアダプター一覧を確認する。
    - B. 仕様上の役割は導入と起動でmksysbを用い・altinst_rootvg と起動デバイス設定を確認する。 ✅
    - C. 仕様上の役割はデバイス管理でodmget CuDvを用い・PVID とODM属性を確認する。
    - D. 仕様上の役割はネットワークでnetstat -rnを用い・Destination とアダプター一覧を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「導入と起動でmksysbを用い、altinst_rootvg」に対応する項目は監査記録 altinst_rootv（監査・mksy）です。監査に関する導入と起動の仕様は「導入と起動でmksysbを用い、altinst_rootvg」で、確認対象はmk・監査です。運用引・noのA:は「ネットワークでno -aを用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・no）です。変更前・odmgのC:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は変更前確認 PVID（変更・odmg）です。状態・netsのD:は「ネットワークでnetstat -rnを用い、Destination」を述べ、対象は状態確認 Destination（状態・nets）です。「mksysb」は「導入と起動でmksysbを用い、altinst_rootvg」を指し、監査記録 altinst_rootvではmk・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 監査記録 altinst_rootvg 0125**

    - 検証目的: 導入と起動のmksysb 監査記録 altinst_rootvg 0125について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録005-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0125A
    ```

    画面・出力には AIX0125A が表示され、mksysb 監査記録 altinst_rootvg 0125 の入力欄確認を確認できます。

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
    確認コード AIX0125B
    ```

    画面・出力には AIX0125B が表示され、mksysb 監査記録 altinst_rootvg 0125 の証跡表示確認を確認できます。

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
    確認コード AIX0125C
    ```

    画面・出力には AIX0125C が表示され、mksysb 監査記録 altinst_rootvg 0125 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0125A が画面・出力に表示されること
    ② ステップ2 の AIX0125B が画面・出力に表示されること
    ③ ステップ3 の AIX0125C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 起動確認 EFIX LABEL 0760 {#c01-i0765}
*分類: 導入と起動*  ・  難易度: 中級

青葉復旧ではAIX 7.3の導入と起動で mksysb を確認します。青葉復旧の導入と起動では EFIX LABEL と代替ディスク状態を監査票へ転記します。青葉復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。青葉復旧の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、青葉復旧を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 起動確認 EFIX LABEL 0760を同一分類のno -a 属性確認 Destination 0761と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでno -aを用い・Destination とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・isnapshot とファイルシステム属性を確認する。
    - C. 管理対象との関係を表す説明はセキュリティでchuserを用い・enhanced_RBAC と監査設定を確認する。
    - D. 管理対象との関係を表す説明は導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でmksysbを用い、EFIX LABEL と代替ディスク状態を確認する」に対応する項目はEFIX LABEL（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、EFIX LABEL」で、確認対象はmk・起動です。属性・noのA:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。変更後・spliのB:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は変更後確認 isnapshot（変更・spli）です。状態・chusのC:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は状態確認 enhanced_RBAC（状態・chus）です。「mksysb」は「導入と起動でmksysbを用い、EFIX LABEL」を指し、EFIX LABELではmk・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 起動確認 EFIX LABEL 0760**

    - 検証目的: 導入と起動のmksysb 起動確認 EFIX LABEL 0760について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認040-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0760A
    ```

    画面・出力には AIX0760A が表示され、mksysb 起動確認 EFIX LABEL 0760 の入力欄確認を確認できます。

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
    確認コード AIX0760B
    ```

    画面・出力には AIX0760B が表示され、mksysb 起動確認 EFIX LABEL 0760 の証跡表示確認を確認できます。

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
    確認コード AIX0760C
    ```

    画面・出力には AIX0760C が表示され、mksysb 起動確認 EFIX LABEL 0760 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0760A が画面・出力に表示されること
    ② ステップ2 の AIX0760B が画面・出力に表示されること
    ③ ステップ3 の AIX0760C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 起動確認 EFIX LABEL 0820 {#c01-i0766}
*分類: 導入と起動*  ・  難易度: 上級

薄明変更ではAIX 7.3の導入と起動で mksysb を確認します。薄明変更の導入と起動では EFIX LABEL と代替ディスク状態を監査票へ転記します。薄明変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明変更の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、薄明変更を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 起動確認 EFIX LABEL 0820の技術的な意味を資料で確認するとき、errpt 属性照合 ログ採取との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。 ✅
    - B. 管理対象との関係を表す説明はAIX エラーログから要約または詳細レポートを生成するコマンドである。
    - C. 管理対象との関係を表す説明は導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。
    - D. 管理対象との関係を表す説明はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** 起動・mksyでAの記述「導入と起動でmksysbを用い、EFIX LABEL」に対応する項目はEFIX LABEL（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、EFIX LABEL」で、確認対象はmk・起動です。属性・ログ・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は属性照合 ログ採取（属性・errp）です。障害切・instのC:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・inst）です。起動・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。「mksysb」は「導入と起動でmksysbを用い、EFIX LABEL」を指し、EFIX LABELではmk・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 起動確認 EFIX LABEL 0820**

    - 検証目的: 導入と起動のmksysb 起動確認 EFIX LABEL 0820について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認100-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0820A
    ```

    画面・出力には AIX0820A が表示され、mksysb 起動確認 EFIX LABEL 0820 の入力欄確認を確認できます。

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
    確認コード AIX0820B
    ```

    画面・出力には AIX0820B が表示され、mksysb 起動確認 EFIX LABEL 0820 の証跡表示確認を確認できます。

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
    確認コード AIX0820C
    ```

    画面・出力には AIX0820C が表示され、mksysb 起動確認 EFIX LABEL 0820 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0820A が画面・出力に表示されること
    ② ステップ2 の AIX0820B が画面・出力に表示されること
    ③ ステップ3 の AIX0820C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 起動確認 Technology Level 0284 {#c01-i0767}
*分類: 導入と起動*  ・  難易度: 中級

若草復旧ではAIX 7.3の導入と起動で mksysb を確認します。若草復旧の導入と起動では Technology Level と代替ディスク状態を引継ぎ票へ保管します。若草復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若草復旧の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、若草復旧を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 起動確認 Technology Level 0284の技術的な意味を資料で確認するとき、no -a 属性確認 Media Speed Running 0285との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。
    - B. コマンドまたは機能の用途はデバイス管理でodmget CuDvを用い・microcode level とデバイス一覧を確認する。
    - C. コマンドまたは機能の用途は導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。 ✅
    - D. コマンドまたは機能の用途はデバイス属性を変更する管理コマンドである。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・起動です。属性・noのA:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。監査・odmgのB:は「デバイス管理でodmget CuDvを用い、microcode」を述べ、対象はmicrocode level（監査・odmg）です。性能・識別・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は性能確認 識別値（性能・chde）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 起動確認 Technology Level 0284**

    - 検証目的: 導入と起動のmksysb 起動確認 Technology Level 0284について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認044-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0284A
    ```

    画面・出力には AIX0284A が表示され、mksysb 起動確認 Technology Level 0284 の入力欄確認を確認できます。

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
    確認コード AIX0284B
    ```

    画面・出力には AIX0284B が表示され、mksysb 起動確認 Technology Level 0284 の証跡表示確認を確認できます。

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
    確認コード AIX0284C
    ```

    画面・出力には AIX0284C が表示され、mksysb 起動確認 Technology Level 0284 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0284A が画面・出力に表示されること
    ② ステップ2 の AIX0284B が画面・出力に表示されること
    ③ ステップ3 の AIX0284C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 起動確認 Technology Level 0344 {#c01-i0768}
*分類: 導入と起動*  ・  難易度: 上級

霜月変更ではAIX 7.3の導入と起動で mksysb を確認します。霜月変更の導入と起動では Technology Level と代替ディスク状態を引継ぎ票へ保管します。霜月変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。霜月変更の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、霜月変更を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 起動確認 Technology Level 0344を同一分類のno -a 属性確認 Media Speed Running 0345と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。
    - B. コマンドまたは機能の用途はデバイス管理でlscfg -vl ent0を用い・Available とデバイス一覧を確認する。
    - C. コマンドまたは機能の用途はセキュリティでlsuserを用い・user attributes と監査設定を確認する。
    - D. コマンドまたは機能の用途は導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・起動です。属性・noのA:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。運用引・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象は運用引継ぎ Available（運用・lscf）です。構成・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（構成・lsus）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 起動確認 Technology Level 0344**

    - 検証目的: 導入と起動のmksysb 起動確認 Technology Level 0344について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認104-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0344A
    ```

    画面・出力には AIX0344A が表示され、mksysb 起動確認 Technology Level 0344 の入力欄確認を確認できます。

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
    確認コード AIX0344B
    ```

    画面・出力には AIX0344B が表示され、mksysb 起動確認 Technology Level 0344 の証跡表示確認を確認できます。

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
    確認コード AIX0344C
    ```

    画面・出力には AIX0344C が表示され、mksysb 起動確認 Technology Level 0344 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0344A が画面・出力に表示されること
    ② ステップ2 の AIX0344B が画面・出力に表示されること
    ③ ステップ3 の AIX0344C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 障害切り分け bootlist 0254 {#c01-i0769}
*分類: 導入と起動*  ・  難易度: 初級

星霜監査ではAIX 7.3の導入と起動で mksysb を確認します。星霜監査の導入と起動では bootlist とOSレベル表示を確認票へ整理します。星霜監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。星霜監査の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、星霜監査を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 障害切り分け bootlist 0254に関する障害切り分けの前提を確認しています。no -a バックアウト確認 Gateway 0255の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。 ✅
    - B. 障害切り分けに用いる役割はネットワークでno -aを用い・Gateway とEthernet統計を確認する。
    - C. 障害切り分けに用いる役割はデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。
    - D. 障害切り分けに用いる役割はデバイス属性を変更する管理コマンドである。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「導入と起動でmksysbを用い、bootlist とOSレベル表示を確認する」に対応する項目は障害切り分け bootlist（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、bootlist」で、確認対象はmk・障害切です。バック・noのB:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。状態・odmgのC:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。障害切・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。「mksysb」は「導入と起動でmksysbを用い、bootlist」を指し、障害切り分け bootlistではmk・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 障害切り分け bootlist 0254**

    - 検証目的: 導入と起動のmksysb 障害切り分け bootlist 0254について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け014-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0254A
    ```

    画面・出力には AIX0254A が表示され、mksysb 障害切り分け bootlist 0254 の入力欄確認を確認できます。

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
    確認コード AIX0254B
    ```

    画面・出力には AIX0254B が表示され、mksysb 障害切り分け bootlist 0254 の証跡表示確認を確認できます。

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
    確認コード AIX0254C
    ```

    画面・出力には AIX0254C が表示され、mksysb 障害切り分け bootlist 0254 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0254A が画面・出力に表示されること
    ② ステップ2 の AIX0254B が画面・出力に表示されること
    ③ ステップ3 の AIX0254C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 障害切り分け bootlist 0314 {#c01-i0770}
*分類: 導入と起動*  ・  難易度: 中級

銀嶺復旧ではAIX 7.3の導入と起動で mksysb を確認します。銀嶺復旧の導入と起動では bootlist とOSレベル表示を確認票へ整理します。銀嶺復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。銀嶺復旧の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、銀嶺復旧を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 障害切り分け bootlist 0314の役割を調べています。no -a バックアウト確認 Gateway 0315の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。 ✅
    - B. 障害切り分けに用いる役割はネットワークでno -aを用い・Gateway とEthernet統計を確認する。
    - C. 障害切り分けに用いる役割はデバイス管理でlscfg -vl ent0を用い・PVID と構成マネージャー結果を確認する。
    - D. 障害切り分けに用いる役割はセキュリティでlsuserを用い・user attributes とロール一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でmksysbを用い、bootlist とOSレベル表示を確認する」に対応する項目は障害切り分け bootlist（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、bootlist」で、確認対象はmk・障害切です。バック・noのB:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。構成・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lscf）です。運用引・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（運用・lsus）です。「mksysb」は「導入と起動でmksysbを用い、bootlist」を指し、障害切り分け bootlistではmk・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 障害切り分け bootlist 0314**

    - 検証目的: 導入と起動のmksysb 障害切り分け bootlist 0314について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け074-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0314A
    ```

    画面・出力には AIX0314A が表示され、mksysb 障害切り分け bootlist 0314 の入力欄確認を確認できます。

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
    確認コード AIX0314B
    ```

    画面・出力には AIX0314B が表示され、mksysb 障害切り分け bootlist 0314 の証跡表示確認を確認できます。

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
    確認コード AIX0314C
    ```

    画面・出力には AIX0314C が表示され、mksysb 障害切り分け bootlist 0314 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0314A が画面・出力に表示されること
    ② ステップ2 の AIX0314B が画面・出力に表示されること
    ③ ステップ3 の AIX0314C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 障害切り分け mksysb image 0730 {#c01-i0771}
*分類: 導入と起動*  ・  難易度: 初級

桜雲監査ではAIX 7.3の導入と起動で mksysb を確認します。桜雲監査の導入と起動では mksysb image とOSレベル表示を保守票へ記録します。桜雲監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲監査の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、桜雲監査を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 障害切り分け mksysb image 0730の役割を調べています。no -a バックアウト確認 Link Status 0731の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。
    - B. 表示や設定で扱う内容は導入と起動でmksysbを用い・mksysb image とOSレベル表示を確認する。 ✅
    - C. 表示や設定で扱う内容はJFS2でsnapを用い・lff とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はセキュリティでchuserを用い・enhanced_RBAC とロール一覧を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「導入と起動でmksysbを用い、mksysb image とOSレベル表示を確認する」に対応する項目はmksysb image（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、mksysb image」で、確認対象はmk・障害切です。バック・noのA:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。容量・snapのC:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は容量確認 lff（容量・snap）です。監査・chusのD:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は監査記録 enhanced_RBAC（監査・chus）です。「mksysb」は「導入と起動でmksysbを用い、mksysb image」を指し、mksysb imageではmk・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 障害切り分け mksysb image 0730**

    - 検証目的: 導入と起動のmksysb 障害切り分け mksysb image 0730について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け010-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0730A
    ```

    画面・出力には AIX0730A が表示され、mksysb 障害切り分け mksysb image 0730 の入力欄確認を確認できます。

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
    確認コード AIX0730B
    ```

    画面・出力には AIX0730B が表示され、mksysb 障害切り分け mksysb image 0730 の証跡表示確認を確認できます。

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
    確認コード AIX0730C
    ```

    画面・出力には AIX0730C が表示され、mksysb 障害切り分け mksysb image 0730 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0730A が画面・出力に表示されること
    ② ステップ2 の AIX0730B が画面・出力に表示されること
    ③ ステップ3 の AIX0730C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### mksysb 障害切り分け mksysb image 0790 {#c01-i0772}
*分類: 導入と起動*  ・  難易度: 中級

早苗復旧ではAIX 7.3の導入と起動で mksysb を確認します。早苗復旧の導入と起動では mksysb image とOSレベル表示を保守票へ記録します。早苗復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗復旧の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、早苗復旧を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** mksysb 障害切り分け mksysb image 0790に関する障害切り分けの前提を確認しています。defragfs バックアウト確認 log=INLINE 0803の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は導入と起動でmksysbを用い・mksysb image とOSレベル表示を確認する。 ✅
    - B. 表示や設定で扱う内容はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。
    - C. 表示や設定で扱う内容は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。
    - D. 表示や設定で扱う内容はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** 障害切・mksyでAの記述「導入と起動でmksysbを用い、mksysb image」に対応する項目はmksysb image（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、mksysb image」で、確認対象はmk・障害切です。バック・defrのB:は「JFS2でdefragfsを用い、log=INLINE」を述べ、対象はバックアウト確認 log=INLIN（バッ・defr）です。バック・nimaのC:は「導入と起動でnimadmを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・nima）です。運用引・lsatのD:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。「mksysb」は「導入と起動でmksysbを用い、mksysb image」を指し、mksysb imageではmk・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **mksysb 障害切り分け mksysb image 0790**

    - 検証目的: 導入と起動のmksysb 障害切り分け mksysb image 0790について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け070-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> mksysb
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0790A
    ```

    画面・出力には AIX0790A が表示され、mksysb 障害切り分け mksysb image 0790 の入力欄確認を確認できます。

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
    確認コード AIX0790B
    ```

    画面・出力には AIX0790B が表示され、mksysb 障害切り分け mksysb image 0790 の証跡表示確認を確認できます。

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
    確認コード AIX0790C
    ```

    画面・出力には AIX0790C が表示され、mksysb 障害切り分け mksysb image 0790 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0790A が画面・出力に表示されること
    ② ステップ2 の AIX0790B が画面・出力に表示されること
    ③ ステップ3 の AIX0790C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm バックアウト確認 bootlist 0148 {#c01-i0773}
*分類: 導入と起動*  ・  難易度: 中級

雪解採取ではAIX 7.3の導入と起動で nimadm を確認します。雪解採取の導入と起動では bootlist と代替ディスク状態を監査票へ転記します。雪解採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。雪解採取の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、雪解採取を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm バックアウト確認 bootlist 0148の技術的な意味を資料で確認するとき、lsdev -Cc adapter 監査記録 Gateway 0149との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。 ✅
    - B. 管理対象との関係を表す説明はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。
    - C. 管理対象との関係を表す説明はデバイス管理でrmdev -Rl ent1を用い・attribute とデバイス一覧を確認する。
    - D. 管理対象との関係を表す説明はネットワークでno -aを用い・Destination とMTU属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でnimadmを用い、bootlist と代替ディスク状態を確認する」に対応する項目はバックアウト確認 bootlist（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、bootlist」で、確認対象はni・バックです。監査・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。構成・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は構成照合 attribute（構成・rmde）です。属性・noのD:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。「nimadm」は「導入と起動でnimadmを用い、bootlist」を指し、バックアウト確認 bootlistではni・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm バックアウト確認 bootlist 0148**

    - 検証目的: 導入と起動のnimadm バックアウト確認 bootlist 0148について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認028-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0148A
    ```

    画面・出力には AIX0148A が表示され、nimadm バックアウト確認 bootlist 0148 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0148B
    ```

    画面・出力には AIX0148B が表示され、nimadm バックアウト確認 bootlist 0148 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0148C
    ```

    画面・出力には AIX0148C が表示され、nimadm バックアウト確認 bootlist 0148 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0148A が画面・出力に表示されること
    ② ステップ2 の AIX0148B が画面・出力に表示されること
    ③ ステップ3 の AIX0148C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm バックアウト確認 bootlist 0208 {#c01-i0774}
*分類: 導入と起動*  ・  難易度: 中級

翠風保守ではAIX 7.3の導入と起動で nimadm を確認します。翠風保守の導入と起動では bootlist と代替ディスク状態を監査票へ転記します。翠風保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。翠風保守の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、翠風保守を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm バックアウト確認 bootlist 0208を同一分類のlsdev -Cc adapter 監査記録 Gateway 0209と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はデバイス管理でbootinfo -B hdisk0を用い・PVID とデバイス一覧を確認する。
    - C. 管理対象との関係を表す説明は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。 ✅
    - D. 管理対象との関係を表す説明はネットワークでno -aを用い・Destination とMTU属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でnimadmを用い、bootlist と代替ディスク状態を確認する」に対応する項目はバックアウト確認 bootlist（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、bootlist」で、確認対象はni・バックです。監査・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。変更前・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は変更前確認 PVID（変更・boot）です。属性・noのD:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。「nimadm」は「導入と起動でnimadmを用い、bootlist」を指し、バックアウト確認 bootlistではni・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm バックアウト確認 bootlist 0208**

    - 検証目的: 導入と起動のnimadm バックアウト確認 bootlist 0208について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認088-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0208A
    ```

    画面・出力には AIX0208A が表示され、nimadm バックアウト確認 bootlist 0208 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0208B
    ```

    画面・出力には AIX0208B が表示され、nimadm バックアウト確認 bootlist 0208 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0208C
    ```

    画面・出力には AIX0208C が表示され、nimadm バックアウト確認 bootlist 0208 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0208A が画面・出力に表示されること
    ② ステップ2 の AIX0208B が画面・出力に表示されること
    ③ ステップ3 の AIX0208C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm バックアウト確認 mksysb image 0624 {#c01-i0775}
*分類: 導入と起動*  ・  難易度: 中級

霜月採取ではAIX 7.3の導入と起動で nimadm を確認します。霜月採取の導入と起動では mksysb image と代替ディスク状態を同じ証跡に残します。霜月採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月採取の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、霜月採取を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm バックアウト確認 mksysb image 0624を同一分類のlsdev -Cc adapter 監査記録 Link Status 0625と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。
    - B. 構成を確認する際の意味はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味はセキュリティでusrck -n ALLを用い・authorizations と監査設定を確認する。
    - D. 構成を確認する際の意味は導入と起動でnimadmを用い・mksysb image と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でnimadmを用い、mksysb image」に対応する項目はmksysb image（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、mksysb image」で、確認対象はni・バックです。監査・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。起動・ファ・crfsのB:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。運用引・usrcのC:は「セキュリティでusrck -n ALLを用い」を述べ、対象は運用引継ぎ authorizatio（運用・usrc）です。「nimadm」は「導入と起動でnimadmを用い、mksysb image」を指し、mksysb imageではni・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm バックアウト確認 mksysb image 0624**

    - 検証目的: 導入と起動のnimadm バックアウト確認 mksysb image 0624について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認024-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0624A
    ```

    画面・出力には AIX0624A が表示され、nimadm バックアウト確認 mksysb image 0624 の入力欄確認を確認できます。

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
    確認コード AIX0624B
    ```

    画面・出力には AIX0624B が表示され、nimadm バックアウト確認 mksysb image 0624 の証跡表示確認を確認できます。

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
    確認コード AIX0624C
    ```

    画面・出力には AIX0624C が表示され、nimadm バックアウト確認 mksysb image 0624 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0624A が画面・出力に表示されること
    ② ステップ2 の AIX0624B が画面・出力に表示されること
    ③ ステップ3 の AIX0624C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm バックアウト確認 mksysb image 0684 {#c01-i0776}
*分類: 導入と起動*  ・  難易度: 中級

若草保守ではAIX 7.3の導入と起動で nimadm を確認します。若草保守の導入と起動では mksysb image と代替ディスク状態を同じ証跡に残します。若草保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草保守の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、若草保守を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm バックアウト確認 mksysb image 0684の技術的な意味を資料で確認するとき、lsdev -Cc adapter 監査記録 Link Status 0685との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。
    - B. 構成を確認する際の意味はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味はセキュリティでlsattr -E -l sys0 -aを用い・roles と監査設定を確認する。
    - D. 構成を確認する際の意味は導入と起動でnimadmを用い・mksysb image と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でnimadmを用い、mksysb image」に対応する項目はmksysb image（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、mksysb image」で、確認対象はni・バックです。監査・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。起動・ファ・crfsのB:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。容量・lsatのC:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は容量確認 roles（容量・lsat）です。「nimadm」は「導入と起動でnimadmを用い、mksysb image」を指し、mksysb imageではni・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm バックアウト確認 mksysb image 0684**

    - 検証目的: 導入と起動のnimadm バックアウト確認 mksysb image 0684について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認084-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0684A
    ```

    画面・出力には AIX0684A が表示され、nimadm バックアウト確認 mksysb image 0684 の入力欄確認を確認できます。

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
    確認コード AIX0684B
    ```

    画面・出力には AIX0684B が表示され、nimadm バックアウト確認 mksysb image 0684 の証跡表示確認を確認できます。

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
    確認コード AIX0684C
    ```

    画面・出力には AIX0684C が表示され、nimadm バックアウト確認 mksysb image 0684 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0684A が画面・出力に表示されること
    ② ステップ2 の AIX0684B が画面・出力に表示されること
    ③ ステップ3 の AIX0684C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm 変更後確認 bootlist 0337 {#c01-i0777}
*分類: 導入と起動*  ・  難易度: 中級

初霜変更ではAIX 7.3の導入と起動で nimadm を確認します。初霜変更の導入と起動では bootlist と起動デバイス設定を採取票へ記録します。初霜変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。初霜変更の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、初霜変更を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「nimadm 変更後確認 bootlist 0337」を「lsdev -Cc adapter 障害切り分け Destination 0338」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はネットワークでlsdev -Cc adapterを用い・Destination とアダプター一覧を確認する。
    - B. 保守作業で参照する機能は導入と起動でnimadmを用い・bootlist と起動デバイス設定を確認する。 ✅
    - C. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。
    - D. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でnimadmを用い、bootlist と起動デバイス設定を確認する」に対応する項目は変更後確認 bootlist（変更・nima）です。変更後に関する導入と起動の仕様は「導入と起動でnimadmを用い、bootlist」で、確認対象はni・変更後です。障害切・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け Destination（障害・lsde）です。状態・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。監査・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。「nimadm」は「導入と起動でnimadmを用い、bootlist」を指し、変更後確認 bootlistではni・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm 変更後確認 bootlist 0337**

    - 検証目的: 導入と起動のnimadm 変更後確認 bootlist 0337について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認097-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0337A
    ```

    画面・出力には AIX0337A が表示され、nimadm 変更後確認 bootlist 0337 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0337B
    ```

    画面・出力には AIX0337B が表示され、nimadm 変更後確認 bootlist 0337 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0337C
    ```

    画面・出力には AIX0337C が表示され、nimadm 変更後確認 bootlist 0337 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0337A が画面・出力に表示されること
    ② ステップ2 の AIX0337B が画面・出力に表示されること
    ③ ステップ3 の AIX0337C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm 変更後確認 mksysb image 0813 {#c01-i0778}
*分類: 導入と起動*  ・  難易度: 中級

月影変更ではAIX 7.3の導入と起動で nimadm を確認します。月影変更の導入と起動では mksysb image と起動デバイス設定を判定票へ残します。月影変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影変更の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、月影変更を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm 変更後確認 mksysb image 0813を保守記録に説明する必要があります。lscfg -vl ent0 バックアウト確認 Available 0839と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は導入と起動でnimadmを用い・mksysb image と起動デバイス設定を確認する。 ✅
    - B. 運用時に利用する技術的役割はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。
    - C. 運用時に利用する技術的役割はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。
    - D. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・Status とエラーログ一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** 変更後・nimaでAの記述「導入と起動でnimadmを用い、mksysb image」に対応する項目はmksysb image（変更・nima）です。変更後に関する導入と起動の仕様は「導入と起動でnimadmを用い、mksysb image」で、確認対象はni・変更後です。バック・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。監査・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。属性・starのD:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Status（属性・star）です。「nimadm」は「導入と起動でnimadmを用い、mksysb image」を指し、mksysb imageではni・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm 変更後確認 mksysb image 0813**

    - 検証目的: 導入と起動のnimadm 変更後確認 mksysb image 0813について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認093-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0813A
    ```

    画面・出力には AIX0813A が表示され、nimadm 変更後確認 mksysb image 0813 の入力欄確認を確認できます。

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
    確認コード AIX0813B
    ```

    画面・出力には AIX0813B が表示され、nimadm 変更後確認 mksysb image 0813 の証跡表示確認を確認できます。

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
    確認コード AIX0813C
    ```

    画面・出力には AIX0813C が表示され、nimadm 変更後確認 mksysb image 0813 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0813A が画面・出力に表示されること
    ② ステップ2 の AIX0813B が画面・出力に表示されること
    ③ ステップ3 の AIX0813C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm 属性確認 EFIX LABEL 0654 {#c01-i0779}
*分類: 導入と起動*  ・  難易度: 中級

星霜判定ではAIX 7.3の導入と起動で nimadm を確認します。星霜判定の導入と起動では EFIX LABEL とOSレベル表示を変更票へ記録します。星霜判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜判定の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、星霜判定を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm 属性確認 EFIX LABEL 0654に関する障害切り分けの前提を確認しています。lsdev -Cc adapter 状態確認 Destination 0655の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはネットワークでlsdev -Cc adapterを用い・Destinationである。
    - B. 機能の説明としてはJFS2でcrfsを用い・isnapshot とログデバイス設定を確認する。
    - C. 機能の説明としてはセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。
    - D. 機能の説明としては導入と起動でnimadmを用い・EFIX LABEL とOSレベル表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でnimadmを用い、EFIX LABEL とOSレベル表示を確認する」に対応する項目はEFIX LABEL（属性・nima）です。属性に関する導入と起動の仕様は「導入と起動でnimadmを用い、EFIX LABEL」で、確認対象はni・属性です。状態・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は状態確認 Destination（状態・lsde）です。障害切・crfsのB:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は障害切り分け isnapshot（障害・crfs）です。構成・usrcのC:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。「nimadm」は「導入と起動でnimadmを用い、EFIX LABEL」を指し、EFIX LABELではni・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm 属性確認 EFIX LABEL 0654**

    - 検証目的: 導入と起動のnimadm 属性確認 EFIX LABEL 0654について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認054-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0654A
    ```

    画面・出力には AIX0654A が表示され、nimadm 属性確認 EFIX LABEL 0654 の入力欄確認を確認できます。

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
    確認コード AIX0654B
    ```

    画面・出力には AIX0654B が表示され、nimadm 属性確認 EFIX LABEL 0654 の証跡表示確認を確認できます。

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
    確認コード AIX0654C
    ```

    画面・出力には AIX0654C が表示され、nimadm 属性確認 EFIX LABEL 0654 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0654A が画面・出力に表示されること
    ② ステップ2 の AIX0654B が画面・出力に表示されること
    ③ ステップ3 の AIX0654C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm 属性確認 Technology Level 0178 {#c01-i0780}
*分類: 導入と起動*  ・  難易度: 中級

潮騒判定ではAIX 7.3の導入と起動で nimadm を確認します。潮騒判定の導入と起動では Technology Level とOSレベル表示を保守票へ記録します。潮騒判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。潮騒判定の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、潮騒判定を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm 属性確認 Technology Level 0178の役割を調べています。lsdev -Cc adapter 状態確認 Media Speedの説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は導入と起動でnimadmを用い・Technology Level とOSレベル表示を確認する。 ✅
    - B. 表示や設定で扱う内容はネットワークでlsdev -Cc adapterを用い・Media Speed Runningである。
    - C. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・Availableである。
    - D. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でnimadmを用い、Technology Level」に対応する項目はTechnology Level（属性・nima）です。属性に関する導入と起動の仕様は「導入と起動でnimadmを用い、Technology Level」で、確認対象はni・属性です。状態・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い、Media」を述べ、対象はSpeed Running（状態・lsde）です。容量・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は容量確認 Available（容量・boot）です。バック・noのD:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。「nimadm」は「導入と起動でnimadmを用い、Technology Level」を指し、Technology Levelではni・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm 属性確認 Technology Level 0178**

    - 検証目的: 導入と起動のnimadm 属性確認 Technology Level 0178について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認058-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0178A
    ```

    画面・出力には AIX0178A が表示され、nimadm 属性確認 Technology Level 0178 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0178B
    ```

    画面・出力には AIX0178B が表示され、nimadm 属性確認 Technology Level 0178 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0178C
    ```

    画面・出力には AIX0178C が表示され、nimadm 属性確認 Technology Level 0178 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0178A が画面・出力に表示されること
    ② ステップ2 の AIX0178B が画面・出力に表示されること
    ③ ステップ3 の AIX0178C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm 運用引継ぎ Technology Level 0495 {#c01-i0781}
*分類: 導入と起動*  ・  難易度: 初級

岩清水確認ではAIX 7.3の導入と起動で nimadm を確認します。岩清水確認の導入と起動では Technology Level とfileset一覧を作業票へ保管します。岩清水確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水確認の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、岩清水確認を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm 運用引継ぎ Technology Level 0495の設定や表示を読む前に役割を確認します。lsdev -Cc adapter 容量確認 Link Status 0496ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはネットワークでlsdev -Cc adapterを用い・Link Status と経路表を確認する。
    - B. 状態を読み取るための働きは導入と起動でnimadmを用い・Technology Level とfileset一覧を確認する。 ✅
    - C. 状態を読み取るための働きはデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。
    - D. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「導入と起動でnimadmを用い、Technology Level」に対応する項目はTechnology Level（運用・nima）です。運用引に関する導入と起動の仕様は「導入と起動でnimadmを用い、Technology Level」で、確認対象はni・運用引です。容量・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（容量・lsde）です。変更後・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。性能・usrcのD:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。「nimadm」は「導入と起動でnimadmを用い、Technology Level」を指し、Technology Levelではni・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm 運用引継ぎ Technology Level 0495**

    - 検証目的: 導入と起動のnimadm 運用引継ぎ Technology Level 0495について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ015-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0495A
    ```

    画面・出力には AIX0495A が表示され、nimadm 運用引継ぎ Technology Level 0495 の入力欄確認を確認できます。

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
    確認コード AIX0495B
    ```

    画面・出力には AIX0495B が表示され、nimadm 運用引継ぎ Technology Level 0495 の証跡表示確認を確認できます。

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
    確認コード AIX0495C
    ```

    画面・出力には AIX0495C が表示され、nimadm 運用引継ぎ Technology Level 0495 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0495A が画面・出力に表示されること
    ② ステップ2 の AIX0495B が画面・出力に表示されること
    ③ ステップ3 の AIX0495C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nimadm 運用引継ぎ altinst_rootvg 0019 {#c01-i0782}
*分類: 導入と起動*  ・  難易度: 初級

山吹確認ではAIX 7.3の導入と起動で nimadm を確認します。山吹確認の導入と起動では altinst_rootvg とfileset一覧を点検票へ整理します。山吹確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。山吹確認の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、山吹確認を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nimadm 運用引継ぎ altinst_rootvg 0019について構成や状態を確認します。lsdev -Cc adapter 容量確認 Gateway 0020ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはネットワークでlsdev -Cc adapterを用い・Gateway と経路表を確認する。lsdev -Cc adapter 容量確認 Gateway 0020固有の属性も確認対象に含める。
    - B. 対象資源に対する働きはデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。
    - C. 対象資源に対する働きはネットワークでno -aを用い・Destination と経路表を確認する。
    - D. 対象資源に対する働きは導入と起動でnimadmを用い・altinst_rootvg とfileset一覧を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「導入と起動でnimadmを用い、altinst_rootvg」に対応する項目は運用引継ぎ altinst_root（運用・nima）です。導入と起動の仕様は「導入と起動でnimadmを用い、altinst_rootvg」で、確認対象はni・運用引です。容量・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は容量確認 Gateway（容量・lsde）です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。構成・noのC:は「ネットワークでno -aを用い、Destination」を述べ、対象は構成照合 Destination（構成・no）です。「nimadm」は「導入と起動でnimadmを用い、altinst_rootvg」を指し、運用引継ぎ altinst_rootではni・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nimadm 運用引継ぎ altinst_rootvg 0019**

    - 検証目的: 導入と起動のnimadm 運用引継ぎ altinst_rootvg 0019について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ019-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nimadm
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0019A
    ```

    画面・出力には AIX0019A が表示され、nimadm 運用引継ぎ altinst_rootvg 0019 の入力欄確認を確認できます。

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
    確認コード AIX0019B
    ```

    画面・出力には AIX0019B が表示され、nimadm 運用引継ぎ altinst_rootvg 0019 の証跡表示確認を確認できます。

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
    確認コード AIX0019C
    ```

    画面・出力には AIX0019C が表示され、nimadm 運用引継ぎ altinst_rootvg 0019 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0019A が画面・出力に表示されること
    ② ステップ2 の AIX0019B が画面・出力に表示されること
    ③ ステップ3 の AIX0019C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 変更前確認 bootlist 0526 {#c01-i0783}
*分類: 導入と起動*  ・  難易度: 中級

朝凪照合ではAIX 7.3の導入と起動で oslevel -s を確認します。朝凪照合の導入と起動では bootlist とOSレベル表示を保守票へ記録します。朝凪照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。朝凪照合の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、朝凪照合を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 変更前確認 bootlist 0526に関する障害切り分けの前提を確認しています。ifconfig en0 変更後確認 Gateway 0527の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。 ✅
    - B. 表示や設定で扱う内容はネットワークでifconfig en0を用い・Gateway とEthernet統計を確認する。
    - C. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・attributeである。
    - D. 表示や設定で扱う内容はセキュリティでlsattr -E -l sys0 -aを用い・authorizationsである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でoslevel -sを用い、bootlist とOSレベル表示を確認する」に対応する項目は変更前確認 bootlist（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、bootlist」で、確認対象はos・変更前です。変更後・ifcoのB:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・ifco）です。起動・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 attribute（起動・boot）です。障害切・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は障害切り分け authorizati（障害・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、bootlist」を指し、変更前確認 bootlistではos・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 変更前確認 bootlist 0526**

    - 検証目的: 導入と起動のoslevel -s 変更前確認 bootlist 0526について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認046-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0526A
    ```

    画面・出力には AIX0526A が表示され、oslevel -s 変更前確認 bootlist 0526 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0526B
    ```

    画面・出力には AIX0526B が表示され、oslevel -s 変更前確認 bootlist 0526 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0526C
    ```

    画面・出力には AIX0526C が表示され、oslevel -s 変更前確認 bootlist 0526 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0526A が画面・出力に表示されること
    ② ステップ2 の AIX0526B が画面・出力に表示されること
    ③ ステップ3 の AIX0526C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 変更前確認 bootlist 0586 {#c01-i0784}
*分類: 導入と起動*  ・  難易度: 上級

陽炎点検ではAIX 7.3の導入と起動で oslevel -s を確認します。陽炎点検の導入と起動では bootlist とOSレベル表示を保守票へ記録します。陽炎点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。陽炎点検の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、陽炎点検を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 変更前確認 bootlist 0586の役割を調べています。ifconfig en0 変更後確認 Gateway 0587の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はネットワークでifconfig en0を用い・Gateway とEthernet統計を確認する。
    - B. 表示や設定で扱う内容はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - C. 表示や設定で扱う内容はセキュリティでlsroleを用い・roles とロール一覧を確認する。
    - D. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「導入と起動でoslevel -sを用い、bootlist とOSレベル表示を確認する」に対応する項目は変更前確認 bootlist（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、bootlist」で、確認対象はos・変更前です。変更後・ifcoのA:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・ifco）です。一覧・詳細・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は一覧確認 詳細表示（一覧・lsvg）です。バック・lsroのC:は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を述べ、対象はバックアウト確認 roles（バッ・lsro）です。「oslevel -s」は「導入と起動でoslevel -sを用い、bootlist」を指し、変更前確認 bootlistではos・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 変更前確認 bootlist 0586**

    - 検証目的: 導入と起動のoslevel -s 変更前確認 bootlist 0586について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認106-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0586A
    ```

    画面・出力には AIX0586A が表示され、oslevel -s 変更前確認 bootlist 0586 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0586B
    ```

    画面・出力には AIX0586B が表示され、oslevel -s 変更前確認 bootlist 0586 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0586C
    ```

    画面・出力には AIX0586C が表示され、oslevel -s 変更前確認 bootlist 0586 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0586A が画面・出力に表示されること
    ② ステップ2 の AIX0586B が画面・出力に表示されること
    ③ ステップ3 の AIX0586C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 変更前確認 fileset level 0050 {#c01-i0785}
*分類: 導入と起動*  ・  難易度: 中級

桜雲照合ではAIX 7.3の導入と起動で oslevel -s を確認します。桜雲照合の導入と起動では fileset level とOSレベル表示を確認票へ整理します。桜雲照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。桜雲照合の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、桜雲照合を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 変更前確認 fileset level 0050の役割を調べています。ifconfig en0 変更後確認 MTU 0051の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。 ✅
    - B. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。
    - C. 障害切り分けに用いる役割はデバイス管理でbootinfo -B hdisk0を用い・Availableである。bootinfo -B hdisk0 起動確認 Available固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はネットワークでroute -n getを用い・Media Speed Runningである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（変更・osle）です。導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・変更前です。変更後・ifcoのB:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。起動・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 Available（起動・boot）です。容量・routのD:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（容量・rout）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 変更前確認 fileset level 0050**

    - 検証目的: 導入と起動のoslevel -s 変更前確認 fileset level 0050について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認050-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0050A
    ```

    画面・出力には AIX0050A が表示され、oslevel -s 変更前確認 fileset level 0050 の入力欄確認を確認できます。

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
    確認コード AIX0050B
    ```

    画面・出力には AIX0050B が表示され、oslevel -s 変更前確認 fileset level 0050 の証跡表示確認を確認できます。

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
    確認コード AIX0050C
    ```

    画面・出力には AIX0050C が表示され、oslevel -s 変更前確認 fileset level 0050 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0050A が画面・出力に表示されること
    ② ステップ2 の AIX0050B が画面・出力に表示されること
    ③ ステップ3 の AIX0050C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 変更前確認 fileset level 0110 {#c01-i0786}
*分類: 導入と起動*  ・  難易度: 上級

早苗点検ではAIX 7.3の導入と起動で oslevel -s を確認します。早苗点検の導入と起動では fileset level とOSレベル表示を確認票へ整理します。早苗点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。早苗点検の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、早苗点検を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 変更前確認 fileset level 0110に関する障害切り分けの前提を確認しています。ifconfig en0 変更後確認 MTU 0111の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。
    - B. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。 ✅
    - C. 障害切り分けに用いる役割はデバイス管理でlsmpio -l hdisk0を用い・location codeである。
    - D. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。cfgmgr 性能確認 MTU 0723固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・変更前です。変更後・ifcoのA:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。属性・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（属性・lsmp）です。性能・cfgmのD:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 変更前確認 fileset level 0110**

    - 検証目的: 導入と起動のoslevel -s 変更前確認 fileset level 0110について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認110-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0110A
    ```

    画面・出力には AIX0110A が表示され、oslevel -s 変更前確認 fileset level 0110 の入力欄確認を確認できます。

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
    確認コード AIX0110B
    ```

    画面・出力には AIX0110B が表示され、oslevel -s 変更前確認 fileset level 0110 の証跡表示確認を確認できます。

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
    確認コード AIX0110C
    ```

    画面・出力には AIX0110C が表示され、oslevel -s 変更前確認 fileset level 0110 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0110A が画面・出力に表示されること
    ② ステップ2 の AIX0110B が画面・出力に表示されること
    ③ ステップ3 の AIX0110C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 容量確認 Technology Level 0556 {#c01-i0787}
*分類: 導入と起動*  ・  難易度: 中級

若潮照合ではAIX 7.3の導入と起動で oslevel -s を確認します。若潮照合の導入と起動では Technology Level と代替ディスク状態を監査票へ転記します。若潮照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若潮照合の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若潮照合を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 容量確認 Technology Level 0556の技術的な意味を資料で確認するとき、ifconfig en0 性能確認 Media Speed Running 0557との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでifconfig en0を用い・Media Speed Running とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - C. 管理対象との関係を表す説明は導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。 ✅
    - D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・roles と監査設定を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でoslevel -sを用い、Technology Level」に対応する項目はTechnology Level（容量・osle）です。容量に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、Technology」で、確認対象はos・容量です。性能・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（性能・ifco）です。復旧前・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は復旧前確認 再開位置（復旧・lsvg）です。属性・lsroのD:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。「oslevel -s」は「導入と起動でoslevel -sを用い、Technology」を指し、Technology Levelではos・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 容量確認 Technology Level 0556**

    - 検証目的: 導入と起動のoslevel -s 容量確認 Technology Level 0556について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認076-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0556A
    ```

    画面・出力には AIX0556A が表示され、oslevel -s 容量確認 Technology Level 0556 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0556B
    ```

    画面・出力には AIX0556B が表示され、oslevel -s 容量確認 Technology Level 0556 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
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
    確認コード AIX0556C
    ```

    画面・出力には AIX0556C が表示され、oslevel -s 容量確認 Technology Level 0556 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0556A が画面・出力に表示されること
    ② ステップ2 の AIX0556B が画面・出力に表示されること
    ③ ステップ3 の AIX0556C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 容量確認 altinst_rootvg 0080 {#c01-i0788}
*分類: 導入と起動*  ・  難易度: 中級

青葉点検ではAIX 7.3の導入と起動で oslevel -s を確認します。青葉点検の導入と起動では altinst_rootvg と代替ディスク状態を引継ぎ票へ保管します。青葉点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。青葉点検の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、青葉点検を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 容量確認 altinst_rootvg 0080を同一分類のifconfig en0 性能確認 EtherChannel 0081と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでifconfig en0を用い・EtherChannel とMTU属性を確認する。
    - B. コマンドまたは機能の用途はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。
    - C. コマンドまたは機能の用途はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。
    - D. コマンドまたは機能の用途は導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でoslevel -sを用い、altinst_rootvg」に対応する項目は容量確認 altinst_rootv（容量・osle）です。容量に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、altinst_rootvg」で、確認対象はos・容量です。性能・ifcoのA:は「ネットワークでifconfig en0を用い」を述べ、対象は性能確認 EtherChannel（性能・ifco）です。バック・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。変更前・routのC:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・rout）です。「oslevel -s」は「導入と起動でoslevel -sを用い、altinst_rootvg」を指し、容量確認 altinst_rootvではos・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 容量確認 altinst_rootvg 0080**

    - 検証目的: 導入と起動のoslevel -s 容量確認 altinst_rootvg 0080について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認080-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0080A
    ```

    画面・出力には AIX0080A が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の入力欄確認を確認できます。

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
    確認コード AIX0080B
    ```

    画面・出力には AIX0080B が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の証跡表示確認を確認できます。

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
    確認コード AIX0080C
    ```

    画面・出力には AIX0080C が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0080A が画面・出力に表示されること
    ② ステップ2 の AIX0080B が画面・出力に表示されること
    ③ ステップ3 の AIX0080C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 起動確認 fileset level 0367 {#c01-i0789}
*分類: 導入と起動*  ・  難易度: 初級

夕凪記録ではAIX 7.3の導入と起動で oslevel -s を確認します。夕凪記録の導入と起動では fileset level とfileset一覧を点検票へ整理します。夕凪記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。夕凪記録の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、夕凪記録を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 起動確認 fileset level 0367の設定や表示を読む前に役割を確認します。ifconfig en0 属性確認 Media Speed Running 0368ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。
    - B. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・Available と診断対象表示を確認する。
    - C. 対象資源に対する働きは導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。 ✅
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（起動・osle）です。起動に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・起動です。属性・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。監査・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は監査記録 Available（監査・boot）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 起動確認 fileset level 0367**

    - 検証目的: 導入と起動のoslevel -s 起動確認 fileset level 0367について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認007-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0367A
    ```

    画面・出力には AIX0367A が表示され、oslevel -s 起動確認 fileset level 0367 の入力欄確認を確認できます。

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
    確認コード AIX0367B
    ```

    画面・出力には AIX0367B が表示され、oslevel -s 起動確認 fileset level 0367 の証跡表示確認を確認できます。

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
    確認コード AIX0367C
    ```

    画面・出力には AIX0367C が表示され、oslevel -s 起動確認 fileset level 0367 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0367A が画面・出力に表示されること
    ② ステップ2 の AIX0367B が画面・出力に表示されること
    ③ ステップ3 の AIX0367C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 起動確認 fileset level 0427 {#c01-i0790}
*分類: 導入と起動*  ・  難易度: 中級

風花評価ではAIX 7.3の導入と起動で oslevel -s を確認します。風花評価の導入と起動では fileset level とfileset一覧を点検票へ整理します。風花評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花評価の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、風花評価を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 起動確認 fileset level 0427について構成や状態を確認します。ifconfig en0 属性確認 Media Speed Running 0428ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。
    - B. 対象資源に対する働きは導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。 ✅
    - C. 対象資源に対する働きはデバイス管理でlsmpio -l hdisk0を用い・location code と診断対象表示を確認する。
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（起動・osle）です。起動に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・起動です。属性・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（運用・lsmp）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 起動確認 fileset level 0427**

    - 検証目的: 導入と起動のoslevel -s 起動確認 fileset level 0427について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認067-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0427A
    ```

    画面・出力には AIX0427A が表示され、oslevel -s 起動確認 fileset level 0427 の入力欄確認を確認できます。

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
    確認コード AIX0427B
    ```

    画面・出力には AIX0427B が表示され、oslevel -s 起動確認 fileset level 0427 の証跡表示確認を確認できます。

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
    確認コード AIX0427C
    ```

    画面・出力には AIX0427C が表示され、oslevel -s 起動確認 fileset level 0427 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0427A が画面・出力に表示されること
    ② ステップ2 の AIX0427B が画面・出力に表示されること
    ③ ステップ3 の AIX0427C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 障害切り分け altinst_rootvg 0397 {#c01-i0791}
*分類: 導入と起動*  ・  難易度: 中級

冬晴記録ではAIX 7.3の導入と起動で oslevel -s を確認します。冬晴記録の導入と起動では altinst_rootvg と起動デバイス設定を採取票へ記録します。冬晴記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。冬晴記録の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、冬晴記録を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 障害切り分け altinst_rootvg 0397を保守記録に説明する必要があります。ifconfig en0 バックアウト確認 Gateway 0398と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はネットワークでifconfig en0を用い・Gateway とアダプター一覧を確認する。ifconfig en0 バックアウト確認 Gateway 0398固有の属性も確認対象に含める。
    - B. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。
    - C. 保守作業で参照する機能は導入と起動でoslevel -sを用い・altinst_rootvg と起動デバイス設定を確認する。 ✅
    - D. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でoslevel -sを用い、altinst_rootvg」に対応する項目は障害切り分け altinst_roo（障害・osle）です。障害切に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、altinst_rootvg」で、確認対象はos・障害切です。バック・ifcoのA:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・ifco）です。状態・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。監査・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、altinst_rootvg」を指し、障害切り分け altinst_rooではos・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 障害切り分け altinst_rootvg 0397**

    - 検証目的: 導入と起動のoslevel -s 障害切り分け altinst_rootvg 0397について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け037-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0397A
    ```

    画面・出力には AIX0397A が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の入力欄確認を確認できます。

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
    確認コード AIX0397B
    ```

    画面・出力には AIX0397B が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の証跡表示確認を確認できます。

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
    確認コード AIX0397C
    ```

    画面・出力には AIX0397C が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0397A が画面・出力に表示されること
    ② ステップ2 の AIX0397B が画面・出力に表示されること
    ③ ステップ3 の AIX0397C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en




## AIX 7.3 > 性能監視

### chdev 変更前確認 識別値 {#c01-i0792}
*分類: 性能監視*  ・  難易度: 初級

AIX 7.3 の 性能監視 で扱う「chdev 変更前確認 識別値」は、デバイス属性を変更する管理コマンドを変更前確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-007を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** chdev 変更前確認 識別値の設定や表示を読む前に役割を確認します。lscfg 復旧前確認 障害記録ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は構成済みデバイスと VPD を表示するコマンドである。
    - B. 一次資料が示す主目的は性能管理でtopas -Dを用い・fre とAME統計を確認する。
    - C. 一次資料が示す主目的はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。
    - D. 一次資料が示す主目的はデバイス属性を変更する管理コマンドである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「デバイス属性を変更する管理コマンドである」に対応する項目は変更前確認 識別値（変更・chde）です。性能監視の仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・変更前です。復旧前・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は復旧前確認 障害記録（復旧・lscf）です。監査・topaのB:は「性能管理でtopas -Dを用い、fre とAME統計を確認する」を述べ、対象は監査記録 fre（監査・topa）です。障害切・syslのC:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、変更前確認 識別値ではch・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **chdev 変更前確認 識別値**

    - 検証目的: 性能監視のchdev 変更前確認 識別値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には Page が含まれ、chdev 変更前確認 識別値の証跡を確認できます。

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



### chdev 状態判定 対象ノード {#c01-i0793}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「chdev 状態判定 対象ノード」は、デバイス属性を変更する管理コマンドを状態判定の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-047を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** chdev 状態判定 対象ノードの設定や表示を読む前に役割を確認します。lscfg 属性照合 時刻情報ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはデバイス属性を変更する管理コマンドである。 ✅
    - B. 状態を読み取るための働きは構成済みデバイスと VPD を表示するコマンドである。
    - C. 状態を読み取るための働きはLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。
    - D. 状態を読み取るための働きは性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「デバイス属性を変更する管理コマンドである」に対応する項目は状態判定 対象ノード（状態・chde）です。性能監視の仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・状態・対象です。属性・時刻・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は属性照合 時刻情報（属性・lscf）です。属性・chlvのC:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（属性・chlv）です。容量・topaのD:は「性能管理でtopas -Dを用い、Busy%」を述べ、対象は容量確認 Busy%（容量・topa）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、状態判定 対象ノードではch・状態・対象に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **chdev 状態判定 対象ノード**

    - 検証目的: 性能監視のchdev 状態判定 対象ノードについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には Page が含まれ、chdev 状態判定 対象ノードの証跡を確認できます。

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



### errpt 属性照合 ログ採取 {#c01-i0794}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「errpt 属性照合 ログ採取」は、AIX エラーログから要約または詳細レポートを生成するコマンドを属性照合の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-055を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** errpt 属性照合 ログ採取の設定や表示を読む前に役割を確認します。lsattr 障害切り分け 実行結果ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。
    - B. 一次資料が示す主目的はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。
    - C. 一次資料が示す主目的は性能管理でsvmon -Gを用い・fre とtopasディスク表示を確認する。
    - D. 一次資料が示す主目的はAIX エラーログから要約または詳細レポートを生成するコマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は属性照合 ログ採取（属性・errp）です。性能監視の仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・属性・ログです。障害切・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は障害切り分け 実行結果（障害・lsat）です。運用引・lslvのB:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。障害切・svmoのC:は「性能管理でsvmon -Gを用い、fre」を述べ、対象は障害切り分け fre（障害・svmo）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、属性照合 ログ採取ではer・属性・ログに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **errpt 属性照合 ログ採取**

    - 検証目的: 性能監視のerrpt 属性照合 ログ採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には System が含まれ、errpt 属性照合 ログ採取の証跡を確認できます。

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



### errpt 復旧前確認 再読込 {#c01-i0795}
*分類: 性能監視*  ・  難易度: 初級

AIX 7.3 の 性能監視 で扱う「errpt 復旧前確認 再読込」は、AIX エラーログから要約または詳細レポートを生成するコマンドを復旧前確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-015を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** errpt 復旧前確認 再読込の設定や表示を読む前に役割を確認します。lsattr 一覧確認 対象ファイルではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはデバイスや sys0 などの属性値を表示するコマンドである。
    - B. 対象資源に対する働きはセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。
    - C. 対象資源に対する働きは導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。
    - D. 対象資源に対する働きはAIX エラーログから要約または詳細レポートを生成するコマンドである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は復旧前確認 再読込（復旧・errp）です。性能監視の仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・復旧前です。一覧・対象・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は一覧確認 対象ファイル（一覧・lsat）です。変更後・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（変更・rbac）です。状態・instのC:は「導入と起動でinstallp -Cを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（状態・inst）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、復旧前確認 再読込ではer・復旧前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **errpt 復旧前確認 再読込**

    - 検証目的: 性能監視のerrpt 復旧前確認 再読込について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には System が含まれ、errpt 復旧前確認 再読込の証跡を確認できます。

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



### lslv 一覧確認 サンプル採取 {#c01-i0796}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「lslv 一覧確認 サンプル採取」は、論理ボリュームの属性と割り当て情報を表示するコマンドを一覧確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-023を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lslv 一覧確認 サンプル採取の設定や表示を読む前に役割を確認します。lsps 詳細確認 メッセージ行ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - B. 状態を読み取るための働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 ✅
    - C. 状態を読み取るための働きはセキュリティでlsroleを用い・roles と監査設定を確認する。
    - D. 状態を読み取るための働きは導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は一覧確認 サンプル採取（一覧・lslv）です。性能監視の仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・一覧・サンです。詳細・メッ・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は詳細確認 メッセージ行（詳細・lsps）です。属性・lsroのC:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。容量・osleのD:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、一覧確認 サンプル採取ではls・一覧・サンに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lslv 一覧確認 サンプル採取**

    - 検証目的: 性能監視のlslv 一覧確認 サンプル採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には LABEL が含まれ、lslv 一覧確認 サンプル採取の証跡を確認できます。

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



### lslv 障害切り分け 起動確認 {#c01-i0797}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「lslv 障害切り分け 起動確認」は、論理ボリュームの属性と割り当て情報を表示するコマンドを障害切り分けの観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-063を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lslv 障害切り分け 起動確認の設定や表示を読む前に役割を確認します。lsps 性能確認 停止確認ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - B. 対象資源に対する働きはLVMでlsvgを用い・PP SIZE とミラーコピー状態を確認する。
    - C. 対象資源に対する働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 ✅
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は障害切り分け 起動確認（障害・lslv）です。性能監視の仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・障害切です。性能・停止・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は性能確認 停止確認（性能・lsps）です。変更後・lsvgのB:は「LVMでlsvgを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（変更・lsvg）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、障害切り分け 起動確認ではls・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lslv 障害切り分け 起動確認**

    - 検証目的: 性能監視のlslv 障害切り分け 起動確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には LABEL が含まれ、lslv 障害切り分け 起動確認の証跡を確認できます。

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



### lspv 性能確認 保持設定 {#c01-i0798}
*分類: 性能監視*  ・  難易度: 上級

AIX 7.3 の 性能監視 で扱う「lspv 性能確認 保持設定」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを性能確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-071を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lspv 性能確認 保持設定の設定や表示を読む前に役割を確認します。lsvg 変更前確認 再開位置ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - B. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 ✅
    - C. 状態を読み取るための働きはJFS2でdefragfsを用い・agblksize とマウントオプションを確認する。
    - D. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は性能確認 保持設定（性能・lspv）です。性能監視の仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・性能・保持です。変更前・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は変更前確認 再開位置（変更・lsvg）です。属性・defrのC:は「JFS2でdefragfsを用い、agblksize」を述べ、対象は属性確認 agblksize（属性・defr）です。性能・usrcのD:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、性能確認 保持設定ではls・性能・保持に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lspv 性能確認 保持設定**

    - 検証目的: 性能監視のlspv 性能確認 保持設定について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e71        rootvg          active
    hdisk1          00f6a1b2c3d5e71        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には VOLUME が含まれ、lspv 性能確認 保持設定の証跡を確認できます。

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



### lspv 詳細確認 装置一覧 {#c01-i0799}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「lspv 詳細確認 装置一覧」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを詳細確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-031を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lspv 詳細確認 装置一覧の設定や表示を読む前に役割を確認します。lsvg 状態判定 製品レベルではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - B. 一次資料が示す主目的は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 ✅
    - C. 一次資料が示す主目的はデバイス管理でlsmpio -l hdisk0を用い・microcode levelである。
    - D. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は詳細確認 装置一覧（詳細・lspv）です。性能監視の仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・詳細・装置です。状態・製品・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は状態判定 製品レベル（状態・lsvg）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はmicrocode level（運用・lsmp）です。障害切・routのD:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、詳細確認 装置一覧ではls・詳細・装置に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lspv 詳細確認 装置一覧**

    - 検証目的: 性能監視のlspv 詳細確認 装置一覧について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e31        rootvg          active
    hdisk1          00f6a1b2c3d5e31        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には VOLUME が含まれ、lspv 詳細確認 装置一覧の証跡を確認できます。

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


