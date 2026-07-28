# KnowledgeMgr AIX 7.3 ナレッジ定義

## 登録するフォーマット

- FormatID: `AIX73-TECH`
- FormatName: `AIX 7.3 技術項目`
- フォーマット定義: `formats\AIX73-TECH.txt`
- ナレッジ配置: `data\AIX73-TECH\<KnowledgeNo>.txt`
- 文字コード: Shift_JIS（CP932）
- 改行: CRLF

## フィールド定義

| FieldName | FieldType | Required | searchTarget | 定義 |
|---|---|---:|---:|---|
| タイトル | 単一行 | 必須 | 対象 | 記事の表題 |
| 分類 | 単一行 | 必須 | 対象 | AIX内の技術分類 |
| 難易度 | 選択 | 必須 | 対象外 | 想定する理解水準 |
| 形式 | 選択 | 必須 | 対象外 | 公式実例型または公式汎化型 |
| IBM公式記述 | 複数行 | 必須 | 対象 | IBM Docsの目的または説明 |
| IBM公式構文 | 複数行 | 必須 | 対象 | IBM Docsの構文 |
| IBM公式オプション | 複数行 | 任意 | 対象 | IBM DocsのFlags節 |
| IBM公式例 | 複数行 | 任意 | 対象 | IBM DocsのExamples節 |
| IBM Docs URL | 単一行 | 必須 | 対象外 | 一次資料へのリンク |

`KnowledgeNo`、`FormatID`、`CreatedAt`、`UpdatedAt` はKnowledgeMgrのシステムキーであり、フォーマットのフィールド定義には含めません。

## ナレッジ・スタンザ

各レコードは `###KnowledgeNo###` から始め、次の `###Key###` までを値として扱います。連結ファイルは搬送用であり、`split_knowledge_mgr_bundle.py` により1件1ファイルへ分解してからdataフォルダーへ配置します。

この資材には、ADR-0158の公式DOM構造ゲートを通過した 1804 件だけを含めます。公式DOMを取得・解析できなかった 12 件は含めません。CP932転送時に表現できない記号は、別紙の転送正規化台帳で明示した等価表記へ変換します。
