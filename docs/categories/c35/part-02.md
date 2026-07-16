---
search:
  exclude: true
---

# Windows Server 2022 — 詳細 (2/2)

[← Windows Server 2022 の概要へ戻る](index.md)


## Windows Server 2022 > 更新管理

### イベントログ 状態確認 監査060 {#c35-i0092}
*分類: 更新管理*  ・  難易度: 中級

第六十観点 イベントログ は Windows Server 2022 の 更新管理 を説明するための項目です（第六十観点）。第六十観点 資料上は 認証、DHCP、DNS、NPS、RDS、セキュリティなどの運用証跡を記録するログとして扱います（第六十観点）。第六十観点 SECLOG060 を起点に設定値を戻し、認証基盤と名前解決の整合確認を点検します（第六十観点）。第六十観点 確認経路は Server Manager、WAC、PowerShell、Event Viewer の別を Windows記録060に残します（第六十観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第六十証跡です。更新管理 の設定更新後に SECLOG060 を再確認します。確認観点は イベントログ、状態確認、監査 です。認証基盤と名前解決の整合確認を満たす記録方法として、管理画面とログを結ぶものはどれか。

    - A. サーバー管理 の一般メモを採り、SECLOG060、役割名、ログ時刻の対応を記録外に置き、Windows誤記060として後続調査を止めてしまう。
    - B. イベントログ の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延060として再確認を先送りする。
    - C. 証跡票に SECLOG060 と PowerShell コマンド出力 を並べ、イベントログ の状態を Windows正060として確定する。 ✅
    - D. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在060として残す。

    正解: **C** ／ 難易度: 中級

    **解説:** 第六十観点 照合結果: Cは SECLOG060 を役割名や時刻と一緒に残すため、再確認時にも根拠を追えます（第六十観点）。第六十観点 保護背景: BitLocker、Credential Guard、Defender は資格情報とデータ保護の確認点になります（第六十観点）。第六十観点 誤答差分: Aは設定値除外、Bは警告イベント未読、Dはサーバー差の隠蔽が理由です（第六十観点）。第六十観点 用語区分: Storage Replica は複製機能です（第六十観点）。第六十観点 Storage Spaces Direct は内蔵ドライブを束ねます（第六十観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **イベントログ 状態確認 監査060**

    - 検証目的: 更新管理における イベントログ の状態確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=SECLOG060
    - セッション環境: Remote Desktop Services / RD Gateway / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により イベントログ の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    PowerShell
    COMMAND ===> Get-RDServer
    → Enter を押す
    ```

    画面・出力:
    ```text
    Server                   Roles
    RDS12.corp.example     RDS-RD-SERVER,RDS-GATEWAY
    ```

    画面・出力には Server が含まれる。Server を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により イベントログ の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    Server Manager
    COMMAND ===> Remote Desktop Services > Collections
    → Enter を押す
    ```

    画面・出力:
    ```text
    Collection SessionCollection12
    User groups and RemoteApp programs listed
    ```

    画面・出力には Collection が含まれる。Collection を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により イベントログ の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Applications and Services Logs > Microsoft > Windows > TerminalServices-Gateway
    → Enter を押す
    ```

    画面・出力:
    ```text
    RD Gateway log
    Event ID 302 connection authorization evaluated for SECLOG060
    ```

    画面・出力には RD Gateway が含まれる。RD Gateway を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: Server が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: Collection が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: RD Gateway が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview




## Windows Server 2022 > 監査ログ

### DHCPサーバー レプリケーション確認 接続095 {#c35-i0093}
*分類: 監査ログ*  ・  難易度: 上級

第九十五観点 監査ログ の変更作業では DHCPサーバー の現在値を先に固定します（第九十五観点）。第九十五観点 役割は クライアントへIPアドレスとTCP/IP構成を配布し、リースと更新を管理する役割という範囲です（第九十五観点）。第九十五観点 \\SOFS23\Share095 を起点に設定値を戻し、資格情報保護の有効化確認を点検します（第九十五観点）。第九十五観点 確認経路は Server Manager、WAC、PowerShell、Event Viewer の別を Windows記録095に残します（第九十五観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第九十五証跡です。Storage Spaces Direct のプール状態 を採取した後の扱いを選びます。確認観点は DHCPサーバー、レプリケーション確認、接続 です。Storage Spaces Direct のプール状態 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS23\Share095、役割名、ログ時刻の対応を記録外に置き、Windows誤記095として後続調査を止めてしまう。
    - B. DHCPサーバー の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延095として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在095として残す。
    - D. 証跡票に \\SOFS23\Share095 と Storage Spaces Direct のプール状態 を並べ、DHCPサーバー の状態を Windows正095として確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 第九十五観点 記録理由: Dは \\SOFS23\Share095 の取得経路を残すため、後日の再調査に耐えます（第九十五観点）。第九十五観点 背景確認: 監査ログでは管理画面とイベントログが分かれて表示されます（第九十五観点）。第九十五観点 誤答整理: Aは一般メモ偏重、BはEvent Viewer除外、Cは再現性不足が理由です（第九十五観点）。第九十五観点 用語確認: AD DS はディレクトリサービスです（第九十五観点）。第九十五観点 DNS は名前をIPアドレスへ対応させます（第九十五観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **DHCPサーバー レプリケーション確認 接続095**

    - 検証目的: 監査ログにおける DHCPサーバー のレプリケーション確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS23\Share095
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により DHCPサーバー の値を確認し、対象の現在値を固定する。
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

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、資格情報保護の有効化確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により DHCPサーバー の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、資格情報保護の有効化確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により DHCPサーバー の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS23\Share095
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、資格情報保護の有効化確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



### DHCPサーバー 可用性確認 確認035 {#c35-i0094}
*分類: 監査ログ*  ・  難易度: 中級

第三十五観点 監査ログ の変更作業では DHCPサーバー の現在値を先に固定します（第三十五観点）。第三十五観点 役割は クライアントへIPアドレスとTCP/IP構成を配布し、リースと更新を管理する役割という範囲です（第三十五観点）。第三十五観点 \\SOFS11\Share035 を起点に設定値を戻し、資格情報保護の有効化確認を点検します（第三十五観点）。第三十五観点 確認経路は Server Manager、WAC、PowerShell、Event Viewer の別を Windows記録035に残します（第三十五観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第三十五証跡です。Storage Spaces Direct のプール状態 を採取した後の扱いを選びます。確認観点は DHCPサーバー、可用性確認、確認 です。Storage Spaces Direct のプール状態 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS11\Share035、役割名、ログ時刻の対応を記録外に置き、Windows誤記035として後続調査を止めてしまう。
    - B. DHCPサーバー の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延035として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在035として残す。
    - D. 証跡票に \\SOFS11\Share035 と Storage Spaces Direct のプール状態 を並べ、DHCPサーバー の状態を Windows正035として確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第三十五観点 採用理由: Dは DHCPサーバー の状態を画面とログの両方から確認するため、記録として妥当です（第三十五観点）。第三十五観点 ストレージ背景: Storage Spaces Direct はSMB3、CSV、Software Storage Busを組み合わせます（第三十五観点）。第三十五観点 誤答内訳: Aは役割状態欠落、Bはログ名不足、Cは証跡再利用が理由です（第三十五観点）。第三十五観点 用語確認: AD DS はディレクトリサービスです（第三十五観点）。第三十五観点 DNS は名前をIPアドレスへ対応させます（第三十五観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **DHCPサーバー 可用性確認 確認035**

    - 検証目的: 監査ログにおける DHCPサーバー の可用性確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS11\Share035
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により DHCPサーバー の値を確認し、対象の現在値を固定する。
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

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、資格情報保護の有効化確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により DHCPサーバー の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、資格情報保護の有効化確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により DHCPサーバー の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS11\Share035
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、資格情報保護の有効化確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



### RD Gateway 更新確認 確認059 {#c35-i0095}
*分類: 監査ログ*  ・  難易度: 中級

第五十九観点 監査ログ の変更作業では RD Gateway の現在値を先に固定します（第五十九観点）。第五十九観点 役割は HTTPSでRDP接続を中継し、公開ポートを抑えて条件付きアクセスへつなぐ役割という範囲です（第五十九観点）。第五十九観点 Windows Admin Center の管理画面 の値を \\SOFS11\Share059 と合わせ、管理ツール間の値合わせを記録します（第五十九観点）。第五十九観点 証跡には資料IDと確認値を併記し、Windows記録059として保存します（第五十九観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第五十九証跡です。RD Gateway の差分を同じサーバーで確認します。確認観点は RD Gateway、更新確認、確認 です。Windows Admin Center の管理画面 を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS11\Share059、役割名、ログ時刻の対応を記録外に置き、Windows誤記059として後続調査を止めてしまう。
    - B. RD Gateway の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延059として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在059として残す。
    - D. 証跡票に \\SOFS11\Share059 と Windows Admin Center の管理画面 を並べ、RD Gateway の状態を Windows正059として確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第五十九観点 採用理由: Dは RD Gateway の状態を画面とログの両方から確認するため、記録として妥当です（第五十九観点）。第五十九観点 ストレージ背景: Storage Spaces Direct はSMB3、CSV、Software Storage Busを組み合わせます（第五十九観点）。第五十九観点 誤答内訳: Aは役割状態欠落、Bはログ名不足、Cは証跡再利用が理由です（第五十九観点）。第五十九観点 用語メモ: CSV はクラスター共有ボリュームです（第五十九観点）。第五十九観点 SMB3 はファイル共有で使います（第五十九観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **RD Gateway 更新確認 確認059**

    - 検証目的: 監査ログにおける RD Gateway の更新確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS11\Share059
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により RD Gateway の値を確認し、対象の現在値を固定する。
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

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、管理ツール間の値合わせのため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により RD Gateway の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、管理ツール間の値合わせのため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により RD Gateway の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS11\Share059
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、管理ツール間の値合わせのため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



### Storage Spaces Direct レプリケーション確認 接続047 {#c35-i0096}
*分類: 監査ログ*  ・  難易度: 中級

第四十七観点 監査ログ の変更作業では Storage Spaces Direct の現在値を先に固定します（第四十七観点）。第四十七観点 役割は 複数サーバーの内蔵ドライブをまとめ、ソフトウェア定義の共有ストレージを作る機能という範囲です（第四十七観点）。第四十七観点 Remote Desktop Services の接続ログ と \\SOFS23\Share047 を同じ証跡に置き、暗号化状態の証跡化を管理します（第四十七観点）。第四十七観点 後続確認ではサーバー名、役割名、ログ名、時刻の対応を Windows記録047から再現します（第四十七観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第四十七証跡です。監査ログ で障害原因を調べます。確認観点は S2D、レプリケーション確認、接続 です。Remote Desktop Services の接続ログ を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS23\Share047、役割名、ログ時刻の対応を記録外に置き、Windows誤記047として後続調査を止めてしまう。
    - B. Storage Spaces Direct の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延047として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在047として残す。
    - D. 証跡票に \\SOFS23\Share047 と Remote Desktop Services の接続ログ を並べ、S2D の状態を Windows正047として確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第四十七観点 記録理由: Dは \\SOFS23\Share047 の取得経路を残すため、後日の再調査に耐えます（第四十七観点）。第四十七観点 背景確認: 監査ログでは管理画面とイベントログが分かれて表示されます（第四十七観点）。第四十七観点 誤答整理: Aは一般メモ偏重、BはEvent Viewer除外、Cは再現性不足が理由です（第四十七観点）。第四十七観点 用語整理: NPS はRADIUS認証に関係します（第四十七観点）。第四十七観点 Event Viewer はイベントログ確認の入口です（第四十七観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **Storage Spaces Direct レプリケーション確認 接続047**

    - 検証目的: 監査ログにおける Storage Spaces Direct のレプリケーション確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS23\Share047
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により Storage Spaces Direct の値を確認し、対象の現在値を固定する。
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

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、暗号化状態の証跡化のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により Storage Spaces Direct の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、暗号化状態の証跡化のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により Storage Spaces Direct の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS23\Share047
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、暗号化状態の証跡化のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



### Windows Admin Center ログ確認 接続071 {#c35-i0097}
*分類: 監査ログ*  ・  難易度: 中級

第七十一観点 監査ログ の変更作業では Windows Admin Center の現在値を先に固定します（第七十一観点）。第七十一観点 役割は サーバー、クラスター、Storage Spaces Directなどをブラウザーから管理するという範囲です（第七十一観点）。第七十一観点 Event Viewer のイベントログ とイベント行を同じ確認票に置き、認証基盤と名前解決の整合確認を説明可能にします（第七十一観点）。第七十一観点 記録では役割状態、コマンド出力、イベントログ、管理画面のどこを見たかを Windows記録071へ書きます（第七十一観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第七十一証跡です。監査ログ の再起動前に Windows Admin Center を確認します。確認観点は WAC、ログ確認、接続 です。Event Viewer のイベントログ を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS23\Share071、役割名、ログ時刻の対応を記録外に置き、Windows誤記071として後続調査を止めてしまう。
    - B. Windows Admin Center の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延071として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在071として残す。
    - D. 証跡票に \\SOFS23\Share071 と Event Viewer のイベントログ を並べ、WAC の状態を Windows正071として確定する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 第七十一観点 記録理由: Dは \\SOFS23\Share071 の取得経路を残すため、後日の再調査に耐えます（第七十一観点）。第七十一観点 背景確認: 監査ログでは管理画面とイベントログが分かれて表示されます（第七十一観点）。第七十一観点 誤答整理: Aは一般メモ偏重、BはEvent Viewer除外、Cは再現性不足が理由です（第七十一観点）。第七十一観点 用語関係: BitLocker はボリューム暗号化です（第七十一観点）。第七十一観点 TPM は改ざん検知に関係します（第七十一観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **Windows Admin Center ログ確認 接続071**

    - 検証目的: 監査ログにおける Windows Admin Center のログ確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS23\Share071
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により Windows Admin Center の値を確認し、対象の現在値を固定する。
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

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により Windows Admin Center の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により Windows Admin Center の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS23\Share071
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



### Windows Admin Center 状態確認 確認011 {#c35-i0098}
*分類: 監査ログ*  ・  難易度: 初級

第十一観点 監査ログ の変更作業では Windows Admin Center の現在値を先に固定します（第十一観点）。第十一観点 役割は サーバー、クラスター、Storage Spaces Directなどをブラウザーから管理するという範囲です（第十一観点）。第十一観点 Event Viewer のイベントログ とイベント行を同じ確認票に置き、認証基盤と名前解決の整合確認を説明可能にします（第十一観点）。第十一観点 記録では役割状態、コマンド出力、イベントログ、管理画面のどこを見たかを Windows記録011へ書きます（第十一観点）。

**出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview

??? question "確認問題（1問）"
    **問題.** 運用第十一証跡です。監査ログ の再起動前に Windows Admin Center を確認します。確認観点は WAC、状態確認、確認 です。Event Viewer のイベントログ を証跡に残す判断として、あとから再確認しやすいものはどれか。

    - A. リモートアクセス の一般メモを採り、\\SOFS11\Share011、役割名、ログ時刻の対応を記録外に置き、Windows誤記011として後続調査を止めてしまう。
    - B. Windows Admin Center の名称を確認しても、PowerShell出力、管理画面、Event Viewer の状態を読まず、Windows遅延011として再確認を先送りする。
    - C. 前回の正常イベントを今回分として採用し、Server Manager、Windows Admin Center、PowerShell の差と時刻差を記録せず、Windows混在011として残す。
    - D. 証跡票に \\SOFS11\Share011 と Event Viewer のイベントログ を並べ、WAC の状態を Windows正011として確定する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 第十一観点 採用理由: Dは WAC の状態を画面とログの両方から確認するため、記録として妥当です（第十一観点）。第十一観点 ストレージ背景: Storage Spaces Direct はSMB3、CSV、Software Storage Busを組み合わせます（第十一観点）。第十一観点 誤答内訳: Aは役割状態欠落、Bはログ名不足、Cは証跡再利用が理由です（第十一観点）。第十一観点 用語関係: BitLocker はボリューム暗号化です（第十一観点）。第十一観点 TPM は改ざん検知に関係します（第十一観点）。

    **出典:** Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview


??? note "検証手順（1件）"
    **Windows Admin Center 状態確認 確認011**

    - 検証目的: 監査ログにおける Windows Admin Center の状態確認を机上で確認する。
    - 前提条件: Windows Server 2022 の対象サーバー、役割、PowerShell出力、管理画面、イベントログを確認済み。対象=\\SOFS11\Share011
    - セッション環境: Windows Security / PowerShell / Event Viewer

    **ステップ 1**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。状態表示により Windows Admin Center の値を確認し、対象の現在値を固定する。
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

    画面・出力には ProtectionStatus が含まれる。ProtectionStatus を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。定義照合により Windows Admin Center の値を確認し、定義と資料上の項目を照合する。
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

    画面・出力には RealTimeProtectionEnabled が含まれる。RealTimeProtectionEnabled を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Windows Server 2022 の確認画面またはログ表示である。ログ確認により Windows Admin Center の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Event Viewer
    COMMAND ===> Windows Logs > Security
    → Enter を押す
    ```

    画面・出力:
    ```text
    Security log
    Event ID 4688 process audit entry recorded for \\SOFS11\Share011
    ```

    画面・出力には Security log が含まれる。Security log を読み取り、認証基盤と名前解決の整合確認のため対象の現在値を記録する。

    - 合格条件: ステップ1: ProtectionStatus が画面または出力に表示され、対象サーバーや役割が取り違えられていないこと。
    ステップ2: RealTimeProtectionEnabled が画面または出力に表示され、管理画面、PowerShell、ログの対応が確認できること。
    ステップ3: Security log が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: Windows_Server_2022_Documentation / WS2022_020_ad_ds_overview / WS2022_041_dns_overview / WS2022_042_dhcp_overview / WS2022_045_ipam_overview / WS2022_051_storage_spaces_direct / WS2022_052_storage_replica / WS2022_030_security_overview / WS2022_036_bitlocker / WS2022_070_rds_overview



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


