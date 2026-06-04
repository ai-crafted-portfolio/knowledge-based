---
title: "CICS Transaction 管理 — OLTP ミドルウェアの基礎"
description: "CICS Transaction Server の中核概念 (リージョン / Tranid / COMMAREA / SYNCPOINT) と Pseudo-Conversational 設計、運用の罠を解説。"
ms.date: 2026-06-04
ms.topic: conceptual
ms.service: zos
ms.subservice: cics
author: zos-kb-agent
ms.author: zos-kb-agent
ms.custom: zos-atom-derived
keywords: "z/OS, CICS, Transaction Server, OLTP, COMMAREA, BMS, SYNCPOINT, Pseudo-Conversational"
breadcrumb_path: /zos/cics/fundamentals
source_atom: ZOS-CICS-001
---

# CICS Transaction 管理 — OLTP ミドルウェアの基礎

**Applies to:** z/OS 2.4 以降 / CICS Transaction Server 5.x 以降

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

CICS (Customer Information Control System) は **ミリ秒単位のオンライントランザクション処理 (OLTP)** ミドルウェアです。JCL ベースのバッチが秒〜時間単位なのに対し、CICS は ATM 残高照会のような瞬時応答を裏で支えます。1 リージョンで秒間 1 万 TPS 越えを狙えるのが Java EE 普及後も生き残る理由です。

> [!IMPORTANT]
> CICS は **アプリ層と OS 層の境界を意図的にぼかした設計** です。task scheduling / lock 管理 / log writing / recovery を内製化してコンテキストスイッチを削減し、TPS を稼いでいます。microservices / REST と発想が真逆である点を意識しないと設計判断がブレます。

## 仕組み

中核概念は以下のとおりです。

| 概念              | 説明                                                                 |
| ----------------- | -------------------------------------------------------------------- |
| **リージョン**    | CICS の実行アドレススペース                                          |
| **Tranid**        | 4 文字のトランザクション ID (`MENU` `INQR` `UPDT` 等)                |
| **COMMAREA**      | トランザクション間で受け渡すデータ領域 (最大 32K)                    |
| **BMS マップ**    | 3270 端末画面定義                                                    |
| **CSD**           | CICS System Definition。リソース定義の格納先                         |
| **SYNCPOINT**     | `EXEC CICS SYNCPOINT` で COMMIT、`SYNCPOINT ROLLBACK` で UNDO        |

Tranid を起動するたびに新規 **Task** が作られ、Task は SYNCPOINT 〜 SYNCPOINT 単位で 1 つ以上の **Unit-of-Work (UOW)** を保持します。

> [!TIP]
> **Pseudo-Conversational 方式** は「画面 1 枚 = 1 Task」で、ユーザ思考時間中はリソースを完全解放します。Conversational に倒すと TPS が桁違いに落ちるので、設計時に画面遷移の切り目をどこに置くかが即座にスループット設計になります。

## 前提知識

- VSAM ([VSAM 入門](../vsam/fundamentals.md)) — CICS のリソース DB
- [RACF Security 基本](./racf-fundamentals.md) — トランザクション認可
- データセット概念 + JCL (CICS 起動 JCL)
- トランザクション概念 (COMMIT / ROLLBACK)、3270 プロトコル

## サンプル

COBOL からの典型的な VSAM READ + 送信処理:

```cobol
EXEC CICS READ FILE('CUSTFILE')
               INTO(WS-CUST-REC)
               RIDFLD(WS-CUST-ID)
               RESP(WS-RESP)
END-EXEC.

IF WS-RESP = DFHRESP(NOTFND)
    MOVE 'CUSTOMER NOT FOUND' TO WS-MSG
ELSE IF WS-RESP NOT = DFHRESP(NORMAL)
    EXEC CICS ABEND ABCODE('ERR1') END-EXEC
END-IF.

EXEC CICS SEND MAP('CUSTMAP') MAPSET('CUSTSET')
               FROM(CUSTMAP-AREA) ERASE
END-EXEC.

EXEC CICS RETURN TRANSID('INQR')
                 COMMAREA(WS-COMMAREA)
END-EXEC.
```

CEMT で新ロードを反映:

```cemt
CEMT SET PROGRAM(MYPROG) NEWCOPY
```

## 運用上の注意点

- **PPT / PCT 登録忘れ**: ロード LIB に置いただけでは呼べない。CSD の `DEFINE PROGRAM/TRANSACTION` + `CEMT SET PROGRAM(...) NEWCOPY` が必要
- **NEWCOPY せずに変更反映を期待**: 旧モジュールがメモリに残り「直したのに直ってない」現象
- **COMMAREA 32K 超え**: CICS TS 3.1 以降の **Channel/Container** に切り替える
- **HANDLE CONDITION / RESP の漏れ**: VSAM / Db2 操作後は必ず `RESP` 値を確認
- **Conversational 誤用**: 新人が「待ち状態のままメモリ保持」で書くと TPS が劇的に下がる

> [!WARNING]
> プロダクション CICS の再起動は **数秒数百万円失う** ケースがあります。プログラム更新は再起動ではなく `NEWCOPY` で反映するのが原則です。

## 採否判断のポイント

- **Db2 接続: RRSAF vs CAF**: 新規システムで CAF を選ぶ理由は無い (2 phase commit 不可)。RRSAF 一択
- **COMMAREA vs Channel/Container**: 32K を超える可能性のある画面遷移は最初から Channel
- **Pseudo-Conversational vs Conversational**: 業務要件に関係なく Pseudo が原則

## 次のステップ

- [RACF Security 基本](./racf-fundamentals.md)
- [JCL 入門](./jcl-fundamentals.md)

## 関連記事

- [TSO/E + ISPF 操作入門](./tso-ispf-fundamentals.md)
- [z/OS UNIX サブシステム入門](./uss-fundamentals.md)

## フィードバック

この記事へのフィードバックは内部 issue tracker までお寄せください。記事 ID `ZOS-CICS-001` を併記すると追跡しやすくなります。
