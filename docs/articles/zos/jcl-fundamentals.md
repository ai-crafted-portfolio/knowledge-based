---
title: "JCL 入門 — JOB / EXEC / DD の基礎"
description: "z/OS のバッチジョブ起動言語 JCL の 3 文 (JOB/EXEC/DD)、実行モデル、主要パラメータ、運用上の落とし穴をまとめます。"
ms.date: 2026-06-04
ms.topic: conceptual
ms.service: zos
ms.subservice: jcl
author: zos-kb-agent
ms.author: zos-kb-agent
ms.custom: zos-atom-derived
keywords: "z/OS, JCL, JOB statement, EXEC statement, DD statement, JES2, JES3, バッチ"
breadcrumb_path: /zos/jcl/fundamentals
source_atom: ZOS-JCL-001
---

# JCL 入門 — JOB / EXEC / DD の基礎

**Applies to:** z/OS 2.4 以降 / JES2 / JES3

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

JCL (Job Control Language) は z/OS のバッチジョブ起動プロトコルです。プログラム本体 (COBOL / PL/I / Java など) を呼び出す前に、使用するデータセットと実行環境を **静的かつ宣言的** に記述します。プログラム側は論理名 (DDNAME) で I/O を受け取るため、ソースを変えずに本番 / 開発 / 災対の入出力を差し替えられます。

> [!IMPORTANT]
> JCL は「プログラムの一部」ではなく **実行時点の運用環境契約** です。論理名で I/O を要求する側 (プログラム) と物理リソースに束ねる契約書 (JCL) のレイヤ分離を意識してください。

## 仕組み

JCL は 3 種類の文で構成されます。

| 文       | 役割                | 例                                                            |
| -------- | ------------------- | ------------------------------------------------------------- |
| **JOB**  | ジョブ全体の宣言    | `//MYJOB JOB acct,name,CLASS=A,MSGCLASS=X,REGION=128M`        |
| **EXEC** | ステップの実行      | `//STEP01 EXEC PGM=COBPROG,PARM='ABC'`                        |
| **DD**   | データ定義 (I/O 束) | `//SYSIN DD DSN=USER.IN,DISP=SHR`                             |

JES2 / JES3 はジョブを **変換 → 解釈 → 実行 → 出力 → パージ** の 5 フェーズで処理します。`JCL ERROR` は変換で落ちており本体未実行、`IEF212I DATASET NOT FOUND` は解釈で落ちており前ステップは既にコミット済み、という切り分けが障害解析の鍵です。

> [!TIP]
> `COND=(4,LT)` は「前ステップ RC が 4 未満なら **skip** する」条件です。読み下しを間違えると全ステップ skip で「正常終了」と誤認します。新規 JCL は `IF/THEN/ELSE/ENDIF` を推奨します。

## 前提知識

- データセット概念 ([データセット入門](../dataset/fundamentals.md))
- カタログ ([カタログ入門](../catalog/fundamentals.md))
- 環境変数による I/O 抽象化 (DDNAME はその強烈版)

## サンプル

```jcl
//MYJOB    JOB (ACCT),'NAME',CLASS=A,MSGCLASS=X,REGION=128M,
//             NOTIFY=&SYSUID
//STEP01   EXEC PGM=IEBGENER
//SYSPRINT DD SYSOUT=*
//SYSIN    DD DUMMY
//SYSUT1   DD DSN=USER.PROD.IN,DISP=SHR
//SYSUT2   DD DSN=USER.PROD.OUT,DISP=(NEW,CATLG,DELETE),
//             SPACE=(CYL,(5,1)),DCB=(*.SYSUT1)
//STEP02   EXEC PGM=COBPROG,COND=(4,LT,STEP01)
//STEPLIB  DD DSN=PROD.LOAD,DISP=SHR
//SYSIN    DD DSN=USER.PROD.OUT,DISP=SHR
//SYSPRINT DD SYSOUT=*
```

IF/THEN/ELSE 構文 (新規 JCL 推奨):

```jcl
//IF (STEP01.RC <= 4) THEN
//STEP03 EXEC PGM=POSTPGM
//ENDIF
```

## 運用上の注意点

- **COND の逆論理**: `COND=(0,EQ)` は「RC=0 なら **skip**」。素直に読みたければ `IF/THEN/ELSE` を使う
- **STEPLIB に古いロード残置**: 連結は左から検索。古いデータセットを除去せず追加すると古いモジュールが hit
- **REGION=0M で OOM 連鎖**: 0M は上限なし。本番は 256M / 512M など明示的サイズが原則
- **PROC シンボル終端ピリオド忘れ**: `&DSN.` で終端しないと続く文字と連結されて解決失敗
- **NOTIFY 漏れで深夜障害に気付かない**: 全 JCL に `NOTIFY=&SYSUID` を必須化する SOP を構文チェッカで強制する

> [!WARNING]
> 同名ジョブが Active な状態で 2 個目を投入すると `IEF453I JOB FAILED - JCL ERROR` または待機状態に入ります。ジョブ名には世代 suffix (YYYYMMDDHHMM 等) を付ける運用が安全です。

## 採否判断のポイント

- **COND vs IF/THEN/ELSE**: 新規は IF/THEN/ELSE。既存 JCL は一斉書換リスクを避け COND のまま保守
- **JOBLIB vs STEPLIB**: 全ステップ共通なら JOBLIB 1 行、ステップ毎に切り替えるなら STEPLIB
- **PROC vs INCLUDE**: シンボル置換が必要なら PROC、定型コピペなら INCLUDE
- **CLASS / MSGCLASS**: サイトのクラス設計を理解せずに `CLASS=A` 固定で出すと、夜間バッチに紛れて翌朝走る事故あり

## 次のステップ

- [TSO/E + ISPF 操作入門](./tso-ispf-fundamentals.md)
- [z/OS UNIX サブシステム入門](./uss-fundamentals.md)

## 関連記事

- [RACF Security 基本](./racf-fundamentals.md)
- [CICS Transaction 管理](./cics-fundamentals.md)

## フィードバック

この記事へのフィードバックは内部 issue tracker までお寄せください。記事 ID `ZOS-JCL-001` を併記すると追跡しやすくなります。
