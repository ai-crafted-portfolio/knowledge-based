---
search:
  exclude: true
---

# Anthropic Claude Support / Console Administration — 詳細 (2/2)

[← Anthropic Claude Support / Console Administration の概要へ戻る](index.md)


## Anthropic Claude Support / Console Administration > 請求と使用量

### 組織メンバー削除 権限照合 保護040 {#c02-i0080}
*分類: 請求と使用量*  ・  難易度: 中級

組織メンバー削除 は 請求と使用量 の運用確認で先に固定する確認対象です（CS040-A）。組織メンバー削除 は ワークスペースまたは組織からメンバーを削除する管理操作という内容をConsole表示と照合します（CS040-B）。組織メンバー削除 は CSLIM040 を起点にロールとキーと請求と同期の値を戻し、ワークスペース別の利用量説明を点検します（CS040-C）。請求と使用量 の点検票では確認者、対象画面、支援記事名、操作時刻を CS040 に残します（CS040-D）。

**出典:** CS01-0001 Claude Support Help Center Guide / CS01-0002 Claude Console Administration Guide / CS01-0003 Claude Identity and Billing Guide

??? note "検証手順（1件）"
    **組織メンバー削除 権限照合 保護040**

    - 検証目的: 請求と使用量における 組織メンバー削除 の権限照合を机上で確認する。
    - 前提条件: Claude Console、Claude Admin、支援記事、監査ログを確認済み。対象=CSLIM040
    - セッション環境: Claude Admin / Audit logs

    **ステップ 1**
    現在の画面は Claude Console、Claude Admin、Claude Code、支援記事の確認画面のいずれかである。状態表示により 組織メンバー削除 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    Claude Admin
    COMMAND ===> Audit logs > Event=CSLIM040
    → ENTER を押す
    ```

    画面・出力:
    ```text
    Audit log event
    org_sso_add_initiated
    Actor admin-16
    確認コード CLD040A
    ```

    画面・出力には CLD040A が含まれる。CLD040A を読み取り、ワークスペース別の利用量説明のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は Claude Console、Claude Admin、Claude Code、支援記事の確認画面のいずれかである。定義照合により 組織メンバー削除 の値を確認し、定義と支援記事上の項目を照合する。
    操作（入力）:
    ```text
    Claude Admin
    COMMAND ===> Audit logs > Domain
    → ENTER を押す
    ```

    画面・出力:
    ```text
    Audit log event
    org_domain_verified
    Domain captured
    確認コード CLD040B
    ```

    画面・出力には CLD040B が含まれる。CLD040B を読み取り、ワークスペース別の利用量説明のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は Claude Console、Claude Admin、Claude Code、支援記事の確認画面のいずれかである。ログ確認により 組織メンバー削除 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    Claude Admin
    COMMAND ===> Audit logs > JIT
    → ENTER を押す
    ```

    画面・出力:
    ```text
    Audit log event
    org_jit_toggled
    Provisioning flag recorded
    確認コード CLD040C
    ```

    画面・出力には CLD040C が含まれる。CLD040C を読み取り、ワークスペース別の利用量説明のため対象の現在値を記録する。

    - 合格条件: ステップ1: CLD040A が画面または出力に表示され、対象の組織設定や管理対象が取り違えられていないこと。
    ステップ2: CLD040B が画面または出力に表示され、Console表示、支援記事、監査ログの対応が確認できること。
    ステップ3: CLD040C が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: CS01-0001 Claude Support Help Center Guide / CS01-0002 Claude Console Administration Guide / CS01-0003 Claude Identity and Billing Guide


