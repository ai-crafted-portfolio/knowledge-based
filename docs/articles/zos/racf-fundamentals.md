---
title: "RACF Security 基本 — SAF / 認証 / 認可 / 監査"
description: "z/OS のセキュリティ製品 RACF と統一インタフェース SAF を解説。ユーザ認証、認可モデル、SMF type 80 監査、運用上の罠まで。"
ms.date: 2026-06-04
ms.topic: conceptual
ms.service: zos
ms.subservice: racf
author: zos-kb-agent
ms.author: zos-kb-agent
ms.custom: zos-atom-derived
keywords: "z/OS, RACF, SAF, セキュリティ, 認証, 認可, SMF type 80, データセットプロファイル"
breadcrumb_path: /zos/racf/fundamentals
source_atom: ZOS-RACF-001
---

# RACF Security 基本 — SAF / 認証 / 認可 / 監査

**Applies to:** z/OS 2.4 以降 / RACF (SAF 互換のため ACF2 / Top Secret にも一部適用可)

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

RACF (Resource Access Control Facility) は z/OS のセキュリティ製品で、**ユーザ認証 / リソース認可 / 監査ログ** を統合提供します。z/OS は **SAF (System Authorization Facility)** という統一インタフェースを持ち、データセット OPEN・ジョブ SUBMIT・CICS トランザクション・Db2 BIND/EXEC・USS ファイルアクセスのすべてを SAF 経由で許可判定します。RACF は SAF の実装の 1 つです。

> [!IMPORTANT]
> OS は SAF call の判定理由を知りません。「とりあえず権限を絞る」だけでは内部統制要件を満たせません。**誰が・いつ・何に・どう判定されたか** を後から再現できる監査体制 (SMF type 80 集中分析) を初期構築フェーズで決めてください。

## 仕組み

**認証**: ユーザ ID (1〜8 文字) + パスワード / パスフレーズ / 証明書。TSO / CICS / IMS / Db2 / Web すべてが RACF を経由します。

**認可** は以下を組み合わせます。

| 要素                           | 例                                             |
| ------------------------------ | ---------------------------------------------- |
| データセットプロファイル       | `USER.PROD.**` のような generic profile        |
| 一般リソースクラス             | CICS=`TCICSTRN`、Db2、JES など 500+ クラス     |
| ユーザ属性                     | SPECIAL / AUDITOR / OPERATIONS / PROTECTED     |
| グループ                       | ACL にグループ単位で許可可能                   |

**監査**: SMF type 80 に全アクセス記録。`AUDIT` 設定で成功も含めるか失敗のみかを選択します。

権限判定は **ユーザ → グループ → ACL → UACC → 警告** の決定木を辿ります。`LISTDSD AUTHUSER` で「誰が・どの経路で・何の権限を持つか」を可視化できます。

> [!TIP]
> RACF データベースは in-memory cache されるため、変更後 `SETROPTS REFRESH` を打たないと反映されません。

## 前提知識

- データセット概念 (データセット入門)
- SMF (SMF 入門)
- ACL モデル、認証と認可の区別

## サンプル

```tso
ADDUSER USER01 DFLTGRP(APPGRP) NAME('Taro Suzuki') -
        PASSWORD(initpw01) OWNER(APPGRP)

ADDSD 'USER.PROD.**' UACC(NONE) OWNER(APPGRP) -
      AUDIT(SUCCESS(UPDATE) FAILURES(READ))

PERMIT 'USER.PROD.**' CLASS(DATASET) ID(APPGRP) ACCESS(READ)
PERMIT 'USER.PROD.**' CLASS(DATASET) ID(BATCHUSER) ACCESS(UPDATE)

SETROPTS REFRESH RACLIST(DATASET)
LISTDSD DA('USER.PROD.**') AUTHUSER
```

## 運用上の注意点

- **`UACC(READ)` で全公開事故**: 新規プロファイルは `UACC(NONE)` を必須化し、`PERMIT` で個別許可
- **WARNING モード放置**: テスト用の `WARNING` を本番で外し忘れると権限管理が効かないステルス障害になる。月次棚卸し SOP を設ける
- **退職者の権限残置**: `LISTDSD AUTHUSER` を定期実行し、グループ統廃合とユーザライフサイクルを連動させる
- **`SETROPTS REFRESH` 忘れ**: 変更が反映されず「権限変えたのに変わらない」現象

> [!WARNING]
> `UACC(READ)` を 1 つの本番プロファイルに付けるだけで、全社員から本番データが読める状態になります。新規プロファイルのデフォルトを `UACC(NONE)` に強制する RACF 自動チェックを CI に組み込んでください。

## 採否判断のポイント

- **個別 PERMIT vs グループ経由**: 監査では「誰経由」で許可されたかが SMF type 80 に残るため、業務ロールはグループに寄せ、例外のみ個別 PERMIT
- **AUDIT SUCCESS(UPDATE) vs ALL**: ALL はログ肥大、UPDATE は読み取りを取りこぼす。データ種別で使い分け
- **PROTECTED 属性**: バッチユーザ ID は PROTECTED を付けて対話ログオン不可にする運用が安全

## 次のステップ

- [CICS Transaction 管理](./cics-fundamentals.md)
- [TSO/E + ISPF 操作入門](./tso-ispf-fundamentals.md)

## 関連記事

- [JCL 入門](./jcl-fundamentals.md)
- [z/OS UNIX サブシステム入門](./uss-fundamentals.md)

## フィードバック

この記事へのフィードバックは内部 issue tracker までお寄せください。記事 ID `ZOS-RACF-001` を併記すると追跡しやすくなります。
