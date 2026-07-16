---
title: "z/OS UNIX サブシステム入門 — USS / HFS / zFS"
description: "z/OS 内蔵の POSIX 互換 UNIX サブシステム USS の役割、HFS / zFS、MVS データセット連携、EBCDIC / ASCII タグ運用を解説。"
ms.date: 2026-06-04
ms.topic: conceptual
ms.service: zos
ms.subservice: uss
author: zos-kb-agent
ms.author: zos-kb-agent
ms.custom: zos-atom-derived
keywords: "z/OS, USS, UNIX System Services, HFS, zFS, OMVS, BPXPRMxx, chtag, EBCDIC, ASCII"
breadcrumb_path: /zos/uss/fundamentals
source_atom: ZOS-USS-001
---

# z/OS UNIX サブシステム入門 — USS / HFS / zFS

**Applies to:** z/OS 2.4 以降 / zFS (HFS は legacy)

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

USS (UNIX System Services、旧名 OpenEdition MVS) は **z/OS 内蔵の POSIX 互換 UNIX サブシステム** です。伝統的な MVS データセット世界の隣に、Linux/Unix 風のファイルシステム + シェル + 標準 C ランタイムを並列稼動させます。Java / Python / Apache / OpenSSH / Git などの OSS 移植、TCP/IP サーバ、DevOps ツールチェーンの実行基盤として必須です。

> [!IMPORTANT]
> USS は **POSIX 互換層であって POSIX 完全実装ではありません**。Linux 由来 OSS のビルドが、ファイル属性・改行・エンコーディング・signal 動作・fork 性能のいずれかで失敗することがあります。「Linux で動いた」を即「USS で動く」と読み替えないでください。

## 仕組み

| 領域                 | 内容                                                                  |
| -------------------- | --------------------------------------------------------------------- |
| **ファイルシステム** | HFS (旧式) / **zFS** (新式、マルチユーザ並行対応)                      |
| **物理実体**         | VSAM LDS。USS から `/u/user01/file.txt`、MVS から `OMVS.USER01.ZFS`    |
| **マウント**         | `BPXPRMxx` parmlib メンバまたは動的 `MOUNT FILESYSTEM(...) TYPE(ZFS)` |
| **シェル**           | `/bin/sh` (Korn shell + 拡張) と bash                                  |
| **ユーザ管理**       | RACF + OMVS segment (UID / GID) の両方が必要                            |
| **接続**             | TSO `OMVS` コマンド、または ssh 直接                                   |

MVS データセット連携:

- USS から MVS: `cat "//USER.PROD.PS"` 構文
- MVS から USS: JCL の `PATH=` 指定 (`//DD1 DD PATH='/u/x/file'`)
- **EBCDIC / ASCII**: `chtag` でファイルに ISO8859-1 等を宣言すると自動変換が有効になる

> [!TIP]
> USS の標準シェルは **Korn shell (ksh) 互換** が中核です。bash も導入できますが、運用組み込み済の自動スクリプトは ksh で書かれていることが多く、`${var:-default}` `${var##pattern}` `print -r` `integer` 等の挙動が bash と異なる場面があります。プロジェクトで bash か ksh かを先に決めてください。

## 前提知識

- データセット入門
- VSAM 入門 — zFS / HFS の実体
- [RACF Security 基本](./racf-fundamentals.md) — OMVS segment が必須
- POSIX、Unix シェル、`rwx` 権限

## サンプル

zFS の動的マウントと chtag 運用:

```ksh
# 動的マウント (オペレータコマンド)
MOUNT FILESYSTEM('OMVS.APP01.ZFS') TYPE(ZFS) MODE(RDWR) MOUNTPOINT('/u/app01')

# 既存ファイルに ASCII (ISO8859-1) タグを付ける
chtag -tc ISO8859-1 /u/app01/config.txt

# タグ確認
ls -T /u/app01/

# MVS データセットを USS から読む
cat "//USER.PROD.PS" | head -20

# USS から MVS データセットへ書き出し
cp localfile.txt "//USER.PROD.OUT"
```

## 運用上の注意点

- **OMVS segment 漏れ**: RACF ユーザは作ったが OMVS segment 未付与で USS ログイン不可
- **chtag 忘れ**: ASCII ファイルを EBCDIC と扱って文字化け、`grep` がヒットしないなど
- **zFS aggregate のフラグメント**: 長期運用で I/O 性能劣化。定期的な `ioeagfmt` / `zfsadm grow` 検討
- **fork 性能**: Linux と比べ fork コストが高い。多 fork スクリプト (autotools / 大量 pipe) は遅い
- **改行コード**: MVS テキストは EBCDIC + NL (0x15)、USS は LF (0x25 EBCDIC / 0x0A ASCII)。`iconv` で変換

> [!WARNING]
> 本番 zFS を **read-only マウントで起動するか、専用 RACF プロファイルで保護** しないと、USS ログインしたユーザの誤操作で `rm -rf` が走るリスクがあります。MVS 側の DISP=SHR と USS 側のファイル権限は別レイヤです。

## 採否判断のポイント

- **HFS vs zFS**: 新規は zFS 必須。HFS はマルチユーザ並行性能が低く非推奨
- **bash vs ksh**: 既存サイトに合わせる。新規プロジェクトは ksh が安全 (z/OS native スクリプトとの互換)
- **MVS dataset vs USS ファイル**: バッチ I/O は MVS、OSS ツールチェーンや TCP/IP サーバ系は USS

## 次のステップ

- [TSO/E + ISPF 操作入門](./tso-ispf-fundamentals.md)
- [JCL 入門](./jcl-fundamentals.md)

## 関連記事

- [RACF Security 基本](./racf-fundamentals.md)
- [CICS Transaction 管理](./cics-fundamentals.md)

## フィードバック

この記事へのフィードバックは内部 issue tracker までお寄せください。記事 ID `ZOS-USS-001` を併記すると追跡しやすくなります。
