---
title: "TSO/E + ISPF 操作入門 — z/OS 対話インタフェース"
description: "z/OS の対話シェル TSO と全画面エディタ ISPF の役割、3270 プロトコル前提の操作モデル、REXX 連携、運用上の罠を解説。"
ms.date: 2026-06-04
ms.topic: conceptual
ms.service: zos
ms.subservice: tso
author: zos-kb-agent
ms.author: zos-kb-agent
ms.custom: zos-atom-derived
keywords: "z/OS, TSO, ISPF, REXX, CLIST, SDSF, 3270, LIBDEF, ISPF.PROFILE"
breadcrumb_path: /zos/tso/fundamentals
source_atom: ZOS-TSO-001
---

# TSO/E + ISPF 操作入門 — z/OS 対話インタフェース

**Applies to:** z/OS 2.4 以降 / ISPF 7.x 以降 / TSO/E

## In this article

- [概要](#概要)
- [仕組み](#仕組み)
- [前提知識](#前提知識)
- [サンプル](#サンプル)
- [運用上の注意点](#運用上の注意点)
- [採否判断のポイント](#採否判断のポイント)
- [次のステップ](#次のステップ)
- [関連記事](#関連記事)

## 概要

TSO (Time Sharing Option) は z/OS の対話インタフェースで、Linux の「ssh + bash」相当ですが **対話 + 全画面エディタ (ISPF) + データセット参照** が一体化しています。バッチ実行 (JCL) と同じデータセット実体を、動的なプロンプト操作で扱えます。

ISPF は TSO 上で動く全画面エディタ + メニューシステムで、**z/OS 開発者が起きている時間の 80% は ISPF 画面を見ている** と言って過言ではありません。

> [!IMPORTANT]
> ISPF は **3270 端末プロトコルを前提とした全画面 UI** です。マウスを使わず、PF1=Help / PF3=Exit / PF7=Up / PF8=Down が全画面で統一されているため、慣れた操作員は GUI より速く操作できます。手の動きが固定化されているからこそ目を離して操作できる、という設計思想を理解してください。

## 仕組み

- TSO セッションは **アドレススペース** 1 つを占有。`LOGON USERID` で起動、`LOGOFF` で消える
- TSO コマンド: `ALLOCATE` `LISTC` `RENAME` `DELETE` `EXEC` `SUBMIT` 等
- **REXX**: TSO 上のスクリプト言語 (CLIST は legacy)
- **ISPF**: `ISPF` コマンドで全画面メニュー起動。`=3.4` のような shortcut で深い階層に直接ジャンプ
- **SDSF**: ISPF 上のスプール閲覧
- 接続は 3270 エミュレータ (PCOMM, TN3270 等)

ISPF は **panel / skeleton / table / message** の 4 リソースタイプを ISPPLIB / ISPSLIB / ISPTLIB / ISPMLIB の検索パスで解決します。自作 ISPF アプリでは `LIBDEF` または LOGON PROC でこれらを正しく連結する必要があります。

> [!TIP]
> ISPF サービスは `ISPEXEC` 接頭辞で REXX から呼べます (`ISPEXEC DISPLAY PANEL(...)`, `ISPEXEC TBOPEN ...`)。データセット操作 + 全画面 UI + テーブル管理が短いコードで実現できるため、社内ツール開発の主流です。

## 前提知識

- データセット入門
- [JCL 入門](./jcl-fundamentals.md)
- シェルとエディタの分離 (Unix の bash + vi) が ISPF では融合している点を理解する

## サンプル

REXX による JCL 投入 + RC 受け取り (ISPF 連携):

```rexx
/* REXX */
SIGNAL ON ERROR
ADDRESS TSO
"ALLOC F(SYSIN) DA('USER.PROD.JCL(DAILYJOB)') SHR REUSE"
"SUBMIT * END($$)"
SAY 'submitted'
"FREE F(SYSIN)"

/* ISPF DM サービス呼び出し */
ADDRESS ISPEXEC
"DISPLAY PANEL(MAINMENU)"
IF RC <> 0 THEN
    SAY 'panel display failed RC='RC
EXIT 0

ERROR:
SAY 'REXX error at line' SIGL 'rc='RC
EXIT 12
```

ISPF DSLIST (`=3.4`) で頻用するコマンド:

```ispf
TSO LISTC ENT('USER.PROD.PS') ALL
TSO ALLOC F(WORK) DA('USER.WORK.PS') NEW CATALOG -
          RECFM(F B) LRECL(80) BLKSIZE(27920) SPACE(5,1) TRACKS
```

## 運用上の注意点

- **3270 コードページ不一致**: PCOMM 等で IBM-930 / IBM-939 に合わせないと日本語が `@@@@` `\\\\` に化ける
- **ISPF EDIT で巨大ファイル**: 80MB 程度超で「LARGE FORMAT FILE - VIEW ONLY」。`BROWSE` か分割
- **TSO セッション残置で REGION 占有**: アイドル自動 LOGOFF が無効になっているサイトに注意
- **REXX `SIGNAL ON ERROR` 漏れ**: TSO コマンド失敗時にスクリプトが平然と続行する。先頭で必ず宣言
- **ALLOC SHR / OLD 混乱**: SHR 指定漏れで OLD (排他) となり、別 TSO/JCL とロック衝突
- **ISPF.PROFILE 肥大**: VSAM CI フラグメントでログオン時の panel 表示が遅くなる。年 1 回の再構築 SOP
- **LIBDEF SCOPE 漏れ**: `SCOPE(PROCESS)` 指定しないと当該パネル抜けると無効化

> [!WARNING]
> ISPF オプション 0 の **Edit Recovery を ON** にしておかないと、VPN / Citrix 経由のセッション切断で編集中データが消失します。デフォルト OFF のサイトもあるため、新規ユーザの onboarding で必ず確認してください。

## 採否判断のポイント

- **REXX vs CLIST**: 新規は REXX 一択。CLIST は既存保守のみ
- **TSO コマンド直接 vs ISPF パネル**: 自動化は REXX、対人操作は ISPF。**ISPF panel から REXX を呼ぶ** が標準パターン
- **bash 風 USS vs TSO REXX**: USS 系処理は USS で、データセット中心の自動化は REXX

## 次のステップ

- [JCL 入門](./jcl-fundamentals.md)
- [z/OS UNIX サブシステム入門](./uss-fundamentals.md)

## 関連記事

- [RACF Security 基本](./racf-fundamentals.md)
- [CICS Transaction 管理](./cics-fundamentals.md)

## フィードバック

この記事へのフィードバックは内部 issue tracker までお寄せください。記事 ID `ZOS-TSO-001` を併記すると追跡しやすくなります。
