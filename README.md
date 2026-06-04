# ナレッジベース

技術ナレッジとリファレンスをまとめた静的サイトです。Microsoft Learn / Oracle Support を参考にした構成で、検索性とカテゴリ階層を重視しています。

## プロジェクト概要

- 形式: MkDocs Material テーマによる静的サイト
- 言語: 日本語 (一部英語混在)
- 用途: 業務で蓄積した技術ナレッジを、検索とカテゴリで横断的に引き出す

## 対象領域

| 領域 | 内容 |
|------|------|
| z/OS | メインフレーム運用、JCL、データセット、TSO/ISPF |
| VBA | Excel 自動化、UserForm、配布パッケージング |
| Excel | ワークシート設計、関数、ピボットテーブル |
| Mainframe | JES、SDSF、Db2 for z/OS など周辺基盤 |
| Security | アクセス制御、監査ログ、PowerShell 実行ポリシー |

## ローカル実行手順

1. Python 3.10 以上をインストールします。
2. 依存関係をインストールします。
   ```
   pip install mkdocs-material
   ```
3. 開発サーバーを起動します。
   ```
   mkdocs serve
   ```
4. ブラウザで `http://127.0.0.1:8000/` を開きます。

## 公開 URL

公開サイト: <https://ai-crafted-portfolio.github.io/knowledge-base/>

`main` ブランチへの push をトリガーに GitHub Actions が自動デプロイします。

## 貢献方法

1. 新しい記事は `docs/articles/<領域>/` 配下に Markdown で追加します。
2. ナビゲーションに載せたい場合は `mkdocs.yml` の `nav:` を更新します。
3. プルリクエストを作成し、レビューを受けてからマージします。
4. 表記揺れは既存記事に合わせ、見出しレベルは H2 から始めてください。
