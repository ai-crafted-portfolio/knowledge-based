---
search:
  exclude: true
---

# Windows Server 2022 — 詳細 (3/3)

[← Windows Server 2022 の概要へ戻る](index.md)


## Windows Server 2022 > 監査ログ

### Windows Defender ログ確認 接続023 {#c35-i0099}
*分類: 監査ログ*  ・  難易度: 中級

第二十三観点 監査ログ の変更作業では Windows Defender の現在値を先に固定します（第二十三観点）。第二十三観点 役割は サーバー上のマルウェア対策を提供し、定義更新と保護状態を確認する機能という範囲です（第二十三観点）。第二十三観点 \\SOFS23\Share023、DHCPリースと監査ログ、管理ツールの表示を照合し、クラスター所有ノードの確認を確認します（第二十三観点）。第二十三観点 調査票ではGUIとPowerShellの入口を Windows記録023に区別して残します（第二十三観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第二十三証跡です。監査ログ の作業票へ Windows Defender を記録します。確認観点は Windows Defender、ログ確認、接続 です。DHCPリースと監査ログ を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS23\Share023、役割名、ログ時刻の対応を記録外に置き、Windows誤記023として後続調査を止めてしまう。
    - B. Windows Defender の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延023として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在023として残す。
    - D. 証跡票に \\SOFS23\Share023 と DHCPリースと監査ログ を並べ、Windows Defender の状態を Windows正023として確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第二十三観点 記録理由: Dは \\SOFS23\Share023 の取得経路を残すため、後日の再調査に耐えます（第二十三観点）。第二十三観点 背景確認: 監査ログでは管理画面とイベントログが分かれて表示されます（第二十三観点）。第二十三観点 誤答整理: Aは一般メモ偏重、BはEvent Viewer除外、Cは再現性不足が理由です（第二十三観点）。第二十三観点 初出定義: Windows Admin Center はブラウザー型の管理ツールです（第二十三観点）。第二十三観点 Server Manager は役割管理に使います（第二十三観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **Windows Defender ログ確認 接続023**

    - 検証目的: 監査ログにおける Windows Defender のログ確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS23\Share023
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により Windows Defender の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    PowerShell
    COMMAND ===> Get-BitLockerVolume
    → Enter を押す
    ```

    画面・出力:
    ```text
    MountPoint VolumeStatus ProtectionStatus EncryptionPercentage
    C:         FullyEncrypted On               100
    ```

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、クラスター所有ノードの確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により Windows Defender の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    PowerShell
    COMMAND ===> Get-MpComputerStatus
    → Enter を押す
    ```

    画面・出力:
    ```text
    AMServiceEnabled True
    AntivirusEnabled True
    RealTimeProtectionEnabled True
    ```

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、クラスター所有ノードの確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により Windows Defender の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS23\Share023
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、クラスター所有ノードの確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



### Windows Defender 構成確認 確認083 {#c35-i0100}
*分類: 監査ログ*  ・  難易度: 上級

第八十三観点 監査ログ の変更作業では Windows Defender の現在値を先に固定します（第八十三観点）。第八十三観点 役割は サーバー上のマルウェア対策を提供し、定義更新と保護状態を確認する機能という範囲です（第八十三観点）。第八十三観点 \\SOFS11\Share083、DHCPリースと監査ログ、管理ツールの表示を照合し、クラスター所有ノードの確認を確認します（第八十三観点）。第八十三観点 調査票ではGUIとPowerShellの入口を Windows記録083に区別して残します（第八十三観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第八十三証跡です。監査ログ の作業票へ Windows Defender を記録します。確認観点は Windows Defender、構成確認、確認 です。DHCPリースと監査ログ を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS11\Share083、役割名、ログ時刻の対応を記録外に置き、Windows誤記083として後続調査を止めてしまう。
    - B. Windows Defender の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延083として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在083として残す。
    - D. 証跡票に \\SOFS11\Share083 と DHCPリースと監査ログ を並べ、Windows Defender の状態を Windows正083として確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 第八十三観点 採用理由: Dは Windows Defender の状態を画面とログの両方から確認するため、記録として妥当です（第八十三観点）。第八十三観点 ストレージ背景: Storage Spaces Direct はSMB3、CSV、Software Storage Busを組み合わせます（第八十三観点）。第八十三観点 誤答内訳: Aは役割状態欠落、Bはログ名不足、Cは証跡再利用が理由です（第八十三観点）。第八十三観点 初出定義: Windows Admin Center はブラウザー型の管理ツールです（第八十三観点）。第八十三観点 Server Manager は役割管理に使います（第八十三観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **Windows Defender 構成確認 確認083**

    - 検証目的: 監査ログにおける Windows Defender の構成確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS11\Share083
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により Windows Defender の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    PowerShell
    COMMAND ===> Get-BitLockerVolume
    → Enter を押す
    ```

    画面・出力:
    ```text
    MountPoint VolumeStatus ProtectionStatus EncryptionPercentage
    C:         FullyEncrypted On               100
    ```

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、クラスター所有ノードの確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により Windows Defender の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    PowerShell
    COMMAND ===> Get-MpComputerStatus
    → Enter を押す
    ```

    画面・出力:
    ```text
    AMServiceEnabled True
    AntivirusEnabled True
    RealTimeProtectionEnabled True
    ```

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、クラスター所有ノードの確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により Windows Defender の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS11\Share083
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、クラスター所有ノードの確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


