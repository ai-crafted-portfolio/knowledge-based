---
search:
  exclude: true
---

# Tivoli NetView z/OS 自動化 — 詳細 (28/32)

[← Tivoli NetView z/OS 自動化 の概要へ戻る](index.md)


## Tivoli NetView z/OS 自動化 > 管理リファレンス

### INIT.TCPCONN {#c32-i4070}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.TCPCONNは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.145) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.145)

??? question "確認問題（1問）"
    **問題.** 終端照合の管理リファレンスに関係する INIT.TCPCONN の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端照合で再確認できる形にする。 ✅
    - B. INIT.TCPCONN の名称と担当者名のみを残して終端照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では INIT.TCPCONN は「INIT.TCPCONN の用途をネットビューの表示で確認する終端照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では IBM Z NetViewの INIT.TCPCONN と DSI633I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明のみに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では INIT.TCPCONN を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INIT.TIMER {#c32-i4071}
*分類: 管理リファレンス*  ・  難易度: 中級

INIT.TIMERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.146) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.146)

??? question "確認問題（1問）"
    **問題.** 探索照合の管理リファレンスで INIT.TIMER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. INIT.TIMER の出力を取らず探索照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索照合の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して探索照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では INIT.TIMER は「探索照合の管理リファレンスに関係する定義値と表示行を照合する探索照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では INIT.TIMER の属性行と DSI633I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明のみに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では INIT.TIMER を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### INSTALLOPT {#c32-i4072}
*分類: 管理リファレンス*  ・  難易度: 中級

INSTALLOPTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.436) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.436)

??? question "確認問題（1問）"
    **問題.** 上書照合の管理リファレンスでネットビューの運用確認を行います。INSTALLOPT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書照合の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書照合の根拠を固定する。 ✅
    - D. INSTALLOPT の属性行を読まず上書照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では INSTALLOPT は「IBM Z NetViewで INSTALLOPT の扱いを記録する上書照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では INSTALLOPT の表示結果と DSI633I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明のみに寄り、判定名は上書照合不足です。上書照合資料では INSTALLOPT の使い方を出典欄から追跡し、資料名は上書照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IO_QUEUE_THRESHOLD {#c32-i4073}
*分類: 管理リファレンス*  ・  難易度: 中級

IO_QUEUE_THRESHOLDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.534) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.534)

??? question "確認問題（1問）"
    **問題.** 条件照合の管理リファレンスに関係する IO_QUEUE_THRESHOLD の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、条件照合の証跡として残す。 ✅
    - B. IO_QUEUE_THRESHOLD の名称と担当者名のみを残して条件照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では IO_QUEUE_THRESHOLD は「IO_QUEUE_THRESHOLD の用途をネットビューの表示で確認する条件照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では IBM Z NetViewの IO_QUEUE_THRESHOLD と DSI633I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明のみに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では IO_QUEUE_THRESHOLD を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPCONN {#c32-i4074}
*分類: 管理リファレンス*  ・  難易度: 中級

IPCONNは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.438) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.438)

??? question "確認問題（1問）"
    **問題.** 区切照合の管理リファレンスで IPCONN の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IPCONN の出力を取らず区切照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切照合の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して区切照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では IPCONN は「区切照合の管理リファレンスに関係する定義値と表示行を照合する区切照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では IPCONN の属性行と DSI633I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明のみに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では IPCONN を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPHOST {#c32-i4075}
*分類: 管理リファレンス*  ・  難易度: 中級

IPHOSTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.439) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.439)

??? question "確認問題（1問）"
    **問題.** 範囲照合の管理リファレンスでネットビューの運用確認を行います。IPHOST の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲照合の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲照合の根拠にする。 ✅
    - D. IPHOST の属性行を読まず範囲照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では IPHOST は「IBM Z NetViewで IPHOST の扱いを記録する範囲照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では IPHOST の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明のみに寄り、判定名は範囲照合不足です。範囲照合資料では IPHOST の使い方を出典欄から追跡し、資料名は範囲照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPINFC {#c32-i4076}
*分類: 管理リファレンス*  ・  難易度: 中級

IPINFCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.442) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.442)

??? question "確認問題（1問）"
    **問題.** 優先照合の管理リファレンスに関する IPINFC の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先照合の管理リファレンスの証跡として保存して根拠にする。
    - C. IPINFC の変更点を出力本文から切り離して優先照合の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、優先照合の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では IPINFC は「IPINFC の状態と出力メッセージを結び付ける優先照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では IPINFC の出力行と DSI633I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明のみに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では IPINFC を IBM Z NetViewの確認記録に残し、対象名は優先照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPLOG {#c32-i4077}
*分類: 管理リファレンス*  ・  難易度: 中級

IPLOGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.147) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.147)


### IPNAMESERV {#c32-i4078}
*分類: 管理リファレンス*  ・  難易度: 中級

IPNAMESERVは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.444) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.444)

??? question "確認問題（1問）"
    **問題.** 比較照合の管理リファレンスで IPNAMESERV の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IPNAMESERV の出力を取らず比較照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較照合として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して比較照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では IPNAMESERV は「比較照合の管理リファレンスに関係する定義値と表示行を照合する比較照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では IPNAMESERV の属性行と DSI633I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明のみに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では IPNAMESERV を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPPORT {#c32-i4079}
*分類: 管理リファレンス*  ・  難易度: 中級

IPPORTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.446) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.446)

??? question "確認問題（1問）"
    **問題.** 順序照合の管理リファレンスでネットビューの運用確認を行います。IPPORT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序照合の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序照合の確認にする。 ✅
    - D. IPPORT の属性行を読まず順序照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では IPPORT は「IBM Z NetViewで IPPORT の扱いを記録する順序照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では IPPORT の表示結果と DSI633I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明のみに寄り、判定名は順序照合不足です。順序照合資料では IPPORT の使い方を出典欄から追跡し、資料名は順序照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPROUTER {#c32-i4080}
*分類: 管理リファレンス*  ・  難易度: 中級

IPROUTERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.448) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.448)

??? question "確認問題（1問）"
    **問題.** 値域照合の管理リファレンスに関する IPROUTER の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域照合の管理リファレンスの証跡として保存して根拠にする。
    - C. IPROUTER の変更点を出力本文から切り離して値域照合の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、値域照合の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では IPROUTER は「IPROUTER の状態と出力メッセージを結び付ける値域照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では IPROUTER の出力行と DSI633I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明のみに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では IPROUTER を IBM Z NetViewの確認記録に残し、対象名は値域照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPTELNET {#c32-i4081}
*分類: 管理リファレンス*  ・  難易度: 中級

IPTELNETは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.451) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.451)

??? question "確認問題（1問）"
    **問題.** 警告照合の管理リファレンスに関係する IPTELNET の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告照合で再確認できる形にする。 ✅
    - B. IPTELNET の名称と担当者名のみを残して警告照合の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告照合の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告照合の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では IPTELNET は「IPTELNET の用途をネットビューの表示で確認する警告照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では IBM Z NetViewの IPTELNET と DSI633I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明のみに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では IPTELNET を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告照合用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPTN3270 {#c32-i4082}
*分類: 管理リファレンス*  ・  難易度: 中級

IPTN3270は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.451) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.451)

??? question "確認問題（1問）"
    **問題.** 復旧照合の管理リファレンスで IPTN3270 の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. IPTN3270 の出力を取らず復旧照合の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧照合の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して復旧照合の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧照合の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では IPTN3270 は「復旧照合の管理リファレンスに関係する定義値と表示行を照合する復旧照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では IPTN3270 の属性行と DSI633I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明のみに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では IPTN3270 を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧照合初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### IPv6Env {#c32-i4083}
*分類: 管理リファレンス*  ・  難易度: 中級

IPv6Envは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.147) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.147)

??? question "確認問題（1問）"
    **問題.** 監査照合の管理リファレンスでネットビューの運用確認を行います。IPv6Envの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査照合の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査照合の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査照合の根拠を固定する。 ✅
    - D. IPv6Envの属性行を読まず監査照合の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では IPv6Env は「IBM Z NetViewで IPv6Envの扱いを記録する監査照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では IPv6Envの表示結果と DSI633I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明のみに寄り、判定名は監査照合不足です。監査照合資料では IPv6Envの使い方を出典欄から追跡し、資料名は監査照合資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### ISPAN {#c32-i4084}
*分類: 管理リファレンス*  ・  難易度: 中級

ISPANは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.340) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.340)

??? question "確認問題（1問）"
    **問題.** 変更照合の管理リファレンスに関する ISPAN の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更照合の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更照合の管理リファレンスの証跡として保存して根拠にする。
    - C. ISPAN の変更点を出力本文から切り離して変更照合の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を変更照合で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では ISPAN は「ISPAN の状態と出力メッセージを結び付ける変更照合項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では ISPAN の出力行と DSI633I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明のみに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では ISPAN を IBM Z NetViewの確認記録に残し、対象名は変更照合対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Inform Policy Member {#c32-i4085}
*分類: 管理リファレンス*  ・  難易度: 上級

Inform Policy Memberは、Tivoli NetView z/OS 自動化の管理リファレンスでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Administration Reference (p.487) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.487)

??? question "確認問題（1問）"
    **問題.** 復旧確認の管理リファレンスで Inform 機能の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. Inform 機能の出力を取らず復旧確認の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧確認の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して復旧確認の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧確認の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では Inform 機能 は「復旧確認の管理リファレンスに関係する定義値と表示行を照合する復旧確認項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では Inform 機能の属性行と DSI633I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明のみに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では Inform 機能を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧確認初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### JAPANESE {#c32-i4086}
*分類: 管理リファレンス*  ・  難易度: 中級

JAPANESEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.552) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.552)

??? question "確認問題（1問）"
    **問題.** 展開追跡の管理リファレンスで JAPANESE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. JAPANESE の出力を取らず展開追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開追跡の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して展開追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では JAPANESE は「展開追跡の管理リファレンスに関係する定義値と表示行を照合する展開追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では JAPANESE の属性行と DSI633I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明のみに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では JAPANESE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### JesJobLog {#c32-i4087}
*分類: 管理リファレンス*  ・  難易度: 中級

JesJobLogは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.149) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.149)

??? question "確認問題（1問）"
    **問題.** 呼出追跡の管理リファレンスでネットビューの運用確認を行います。JesJobLogの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出追跡の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出追跡の根拠にする。 ✅
    - D. JesJobLogの属性行を読まず呼出追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では JesJobLog は「IBM Z NetViewで JesJobLogの扱いを記録する呼出追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では JesJobLogの表示結果と DSI633I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明のみに寄り、判定名は呼出追跡不足です。呼出追跡資料では JesJobLogの使い方を出典欄から追跡し、資料名は呼出追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### KCLASS {#c32-i4088}
*分類: 管理リファレンス*  ・  難易度: 中級

KCLASSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.341) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.341)

??? question "確認問題（1問）"
    **問題.** 置換追跡の管理リファレンスに関する KCLASS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. KCLASS の変更点を出力本文から切り離して置換追跡の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、置換追跡の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では KCLASS は「KCLASS の状態と出力メッセージを結び付ける置換追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では KCLASS の出力行と DSI633I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明のみに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では KCLASS を IBM Z NetViewの確認記録に残し、対象名は置換追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### KEYCLASS {#c32-i4089}
*分類: 管理リファレンス*  ・  難易度: 中級

KEYCLASSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.345) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.345)

??? question "確認問題（1問）"
    **問題.** 終端追跡の管理リファレンスに関係する KEYCLASS の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、終端追跡の採否を説明欄に結び付ける。 ✅
    - B. KEYCLASS の名称と担当者名のみを残して終端追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では KEYCLASS は「KEYCLASS の用途をネットビューの表示で確認する終端追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では IBM Z NetViewの KEYCLASS と DSI633I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明のみに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では KEYCLASS を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LASTLINE {#c32-i4090}
*分類: 管理リファレンス*  ・  難易度: 中級

LASTLINEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.345) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.345)

??? question "確認問題（1問）"
    **問題.** 探索追跡の管理リファレンスで LASTLINE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LASTLINE の出力を取らず探索追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索追跡として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して探索追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では LASTLINE は「探索追跡の管理リファレンスに関係する定義値と表示行を照合する探索追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では LASTLINE の属性行と DSI633I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明のみに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では LASTLINE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-AGG-BUNDLE-INTERVAL {#c32-i4091}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-AGG-BUNDLE-INTERVALは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.552) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.552)

??? question "確認問題（1問）"
    **問題.** 上書追跡の管理リファレンスでネットビューの運用確認を行います。LCON-AGG-BUNDLE-INTERVAL の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書追跡の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書追跡の確認にする。 ✅
    - D. LCON-AGG-BUNDLE-INTERVAL の属性行を読まず上書追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では LCON-AGG-BUNDLE-INTERVAL は「IBM Z NetViewで LCON-AGG-BUNDLE-INTERVAL の扱いを記録する上書追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では LCON-AGG-BUNDLE-INTERVAL の表示結果と DSI633I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明のみに寄り、判定名は上書追跡不足です。上書追跡資料では LCON-AGG-BUNDLE-INTERVAL の使い方を出典欄から追跡し、資料名は上書追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-AGGRST-REQUIRED {#c32-i4092}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-AGGRST-REQUIREDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.553) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.553)

??? question "確認問題（1問）"
    **問題.** 出力追跡の管理リファレンスに関する LCON-AGGRST-REQUIRED の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-AGGRST-REQUIRED の変更点を出力本文から切り離して出力追跡の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、出力追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では LCON-AGGRST-REQUIRED は「LCON-AGGRST-REQUIRED の状態と出力メッセージを結び付ける出力追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では LCON-AGGRST-REQUIRED の出力行と DSI633I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明のみに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では LCON-AGGRST-REQUIRED を IBM Z NetViewの確認記録に残し、対象名は出力追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-AIP-RESET-INTERVAL {#c32-i4093}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-AIP-RESET-INTERVALは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.553) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.553)

??? question "確認問題（1問）"
    **問題.** 条件追跡の管理リファレンスに関係する LCON-AIP-RESET-INTERVAL の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件追跡で再確認できる形にする。 ✅
    - B. LCON-AIP-RESET-INTERVAL の名称と担当者名のみを残して条件追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では LCON-AIP-RESET-INTERVAL は「LCON-AIP-RESET-INTERVAL の用途をネットビューの表示で確認する条件追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では IBM Z NetViewの LCON-AIP-RESET-INTERVAL と DSI633I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明のみに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では LCON-AIP-RESET-INTERVAL を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-ALERT-CMD-TIMEOUT {#c32-i4094}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-ALERT-CMD-TIMEOUTは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.554) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.554)

??? question "確認問題（1問）"
    **問題.** 区切追跡の管理リファレンスで LCON-ALERT-CMD-TIMEOUT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LCON-ALERT-CMD-TIMEOUT の出力を取らず区切追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切追跡の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して区切追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では LCON-ALERT-CMD-TIMEOUT は「区切追跡の管理リファレンスに関係する定義値と表示行を照合する区切追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では LCON-ALERT-CMD-TIMEOUT の属性行と DSI633I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明のみに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では LCON-ALERT-CMD-TIMEOUT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-ASSOCIATE-NULL-NODE-WITH-LINK {#c32-i4095}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-ASSOCIATE-NULL-NODE-WITH-LINKは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.554) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.554)

??? question "確認問題（1問）"
    **問題.** 範囲追跡の管理リファレンスでネットビューの運用確認を行います。LCON-ASSOCIATE-NULL-NODE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲追跡の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲追跡の根拠を固定する。 ✅
    - D. LCON-ASSOCIATE-NULL-NODE の属性行を読まず範囲追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では LCON-ASSOCIATE-NULL-NODE は「IBM Z NetViewで LCON-ASSOCIATE-NULL-NODE の扱いを記録する範囲追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では LCON-ASSOCIATE-NULL-NODE の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明のみに寄り、判定名は範囲追跡不足です。範囲追跡資料では LCON-ASSOCIATE-NULL-NODE の使い方を出典欄から追跡し、資料名は範囲追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-EVCHANGE-BUFFER-INTERVAL {#c32-i4096}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-EVCHANGE-BUFFER-INTERVALは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.555) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.555)

??? question "確認問題（1問）"
    **問題.** 優先追跡の管理リファレンスに関する LCON-EVCHANGE-BUFFER-INT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-EVCHANGE-BUFFER-INT の変更点を出力本文から切り離して優先追跡の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を優先追跡で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では LCON-EVCHANGE-BUFFER-INT は「LCON-EVCHANGE-BUFFER-INT の状態と出力メッセージを結び付ける優先追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では LCON-EVCHANGE-BUFFER-INT の出力行と DSI633I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明のみに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では LCON-EVCHANGE-BUFFER-INT を IBM Z NetViewの確認記録に残し、対象名は優先追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-HEX-SUBVECTOR-DISPLAY {#c32-i4097}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-HEX-SUBVECTOR-DISPLAYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.555) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.555)

??? question "確認問題（1問）"
    **問題.** 記録追跡の管理リファレンスに関係する LCON-HEX-SUBVECTOR-DISPL の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、記録追跡の証跡として残す。 ✅
    - B. LCON-HEX-SUBVECTOR-DISPL の名称と担当者名のみを残して記録追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では LCON-HEX-SUBVECTOR-DISPL は「LCON-HEX-SUBVECTOR-DISPL の用途をネットビューの表示で確認する記録追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では IBM Z NetViewの LCON-HEX-SUBVECTOR-DISPL と DSI633I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明のみに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では LCON-HEX-SUBVECTOR-DISPL を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-LOCATE-RESOURCE-VIEWS {#c32-i4098}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-LOCATE-RESOURCE-VIEWSは、Tivoli NetView z/OS 自動化の管理リファレンスでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。IBM Z NetView 6.4 Administration Reference (p.556) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.556)

??? question "確認問題（1問）"
    **問題.** 比較追跡の管理リファレンスで LCON-MAX-LOCATE-RESOURCE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LCON-MAX-LOCATE-RESOURCE の出力を取らず比較追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較追跡の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して比較追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では LCON-MAX-LOCATE-RESOURCE は「比較追跡の管理リファレンスに関係する定義値と表示行を照合する比較追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では LCON-MAX-LOCATE-RESOURCE の属性行と DSI633I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明のみに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では LCON-MAX-LOCATE-RESOURCE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-DBSERVER {#c32-i4099}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-DBSERVERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.556) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.556)

??? question "確認問題（1問）"
    **問題.** 順序追跡の管理リファレンスでネットビューの運用確認を行います。LCON-MAX-QUEUE-DBSERVER の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序追跡の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序追跡の根拠にする。 ✅
    - D. LCON-MAX-QUEUE-DBSERVER の属性行を読まず順序追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では LCON-MAX-QUEUE-DBSERVER は「IBM Z NetViewで LCON-MAX-QUEUE-DBSERVER の扱いを記録する順序追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では LCON-MAX-QUEUE-DBSERVER の表示結果と DSI633I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明のみに寄り、判定名は順序追跡不足です。順序追跡資料では LCON-MAX-QUEUE-DBSERVER の使い方を出典欄から追跡し、資料名は順序追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-EVENTMGR {#c32-i4100}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-EVENTMGRは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.557) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.557)

??? question "確認問題（1問）"
    **問題.** 値域追跡の管理リファレンスに関する LCON-MAX-QUEUE-EVENTMGR の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-MAX-QUEUE-EVENTMGR の変更点を出力本文から切り離して値域追跡の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、値域追跡の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では LCON-MAX-QUEUE-EVENTMGR は「LCON-MAX-QUEUE-EVENTMGR の状態と出力メッセージを結び付ける値域追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では LCON-MAX-QUEUE-EVENTMGR の出力行と DSI633I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明のみに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では LCON-MAX-QUEUE-EVENTMGR を IBM Z NetViewの確認記録に残し、対象名は値域追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-IPC {#c32-i4101}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-IPCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.558) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.558)

??? question "確認問題（1問）"
    **問題.** 警告追跡の管理リファレンスに関係する LCON-MAX-QUEUE-IPC の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、警告追跡の採否を説明欄に結び付ける。 ✅
    - B. LCON-MAX-QUEUE-IPC の名称と担当者名のみを残して警告追跡の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告追跡の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告追跡の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では LCON-MAX-QUEUE-IPC は「LCON-MAX-QUEUE-IPC の用途をネットビューの表示で確認する警告追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では IBM Z NetViewの LCON-MAX-QUEUE-IPC と DSI633I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明のみに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では LCON-MAX-QUEUE-IPC を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告追跡用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-IRMGR {#c32-i4102}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-IRMGRは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.558) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.558)

??? question "確認問題（1問）"
    **問題.** 復旧追跡の管理リファレンスで LCON-MAX-QUEUE-IRMGR の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LCON-MAX-QUEUE-IRMGR の出力を取らず復旧追跡の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧追跡として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して復旧追跡の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧追跡の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では LCON-MAX-QUEUE-IRMGR は「復旧追跡の管理リファレンスに関係する定義値と表示行を照合する復旧追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では LCON-MAX-QUEUE-IRMGR の属性行と DSI633I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明のみに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では LCON-MAX-QUEUE-IRMGR を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧追跡初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-MAINTASK {#c32-i4103}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-MAINTASKは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.559) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.559)

??? question "確認問題（1問）"
    **問題.** 監査追跡の管理リファレンスでネットビューの運用確認を行います。LCON-MAX-QUEUE-MAINTASK の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査追跡の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査追跡の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査追跡の確認にする。 ✅
    - D. LCON-MAX-QUEUE-MAINTASK の属性行を読まず監査追跡の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では LCON-MAX-QUEUE-MAINTASK は「IBM Z NetViewで LCON-MAX-QUEUE-MAINTASK の扱いを記録する監査追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では LCON-MAX-QUEUE-MAINTASK の表示結果と DSI633I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明のみに寄り、判定名は監査追跡不足です。監査追跡資料では LCON-MAX-QUEUE-MAINTASK の使い方を出典欄から追跡し、資料名は監査追跡資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-NETCMD {#c32-i4104}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-NETCMDは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.560) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.560)

??? question "確認問題（1問）"
    **問題.** 変更追跡の管理リファレンスに関する LCON-MAX-QUEUE-NETCMD の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更追跡の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更追跡の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-MAX-QUEUE-NETCMD の変更点を出力本文から切り離して変更追跡の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、変更追跡の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では LCON-MAX-QUEUE-NETCMD は「LCON-MAX-QUEUE-NETCMD の状態と出力メッセージを結び付ける変更追跡項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では LCON-MAX-QUEUE-NETCMD の出力行と DSI633I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明のみに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では LCON-MAX-QUEUE-NETCMD を IBM Z NetViewの確認記録に残し、対象名は変更追跡対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-NETCON {#c32-i4105}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-NETCONは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.560) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.560)

??? question "確認問題（1問）"
    **問題.** 構文検査の管理リファレンスに関係する LCON-MAX-QUEUE-NETCON の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文検査で再確認できる形にする。 ✅
    - B. LCON-MAX-QUEUE-NETCON の名称と担当者名のみを残して構文検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では LCON-MAX-QUEUE-NETCON は「LCON-MAX-QUEUE-NETCON の用途をネットビューの表示で確認する構文検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では IBM Z NetViewの LCON-MAX-QUEUE-NETCON と DSI633I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明のみに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では LCON-MAX-QUEUE-NETCON を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-OPERIF {#c32-i4106}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-OPERIFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.561) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.561)

??? question "確認問題（1問）"
    **問題.** 展開検査の管理リファレンスで LCON-MAX-QUEUE-OPERIF の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LCON-MAX-QUEUE-OPERIF の出力を取らず展開検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開検査の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して展開検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では LCON-MAX-QUEUE-OPERIF は「展開検査の管理リファレンスに関係する定義値と表示行を照合する展開検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では LCON-MAX-QUEUE-OPERIF の属性行と DSI633I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明のみに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では LCON-MAX-QUEUE-OPERIF を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-RCMGR {#c32-i4107}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-RCMGRは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.562) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.562)

??? question "確認問題（1問）"
    **問題.** 呼出検査の管理リファレンスでネットビューの運用確認を行います。LCON-MAX-QUEUE-RCMGR の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検査の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出検査の根拠を固定する。 ✅
    - D. LCON-MAX-QUEUE-RCMGR の属性行を読まず呼出検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では LCON-MAX-QUEUE-RCMGR は「IBM Z NetViewで LCON-MAX-QUEUE-RCMGR の扱いを記録する呼出検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では LCON-MAX-QUEUE-RCMGR の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明のみに寄り、判定名は呼出検査不足です。呼出検査資料では LCON-MAX-QUEUE-RCMGR の使い方を出典欄から追跡し、資料名は呼出検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-RTMGR {#c32-i4108}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-RTMGRは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.563) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.563)

??? question "確認問題（1問）"
    **問題.** 置換検査の管理リファレンスに関する LCON-MAX-QUEUE-RTMGR の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換検査の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-MAX-QUEUE-RTMGR の変更点を出力本文から切り離して置換検査の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を置換検査で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では LCON-MAX-QUEUE-RTMGR は「LCON-MAX-QUEUE-RTMGR の状態と出力メッセージを結び付ける置換検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では LCON-MAX-QUEUE-RTMGR の出力行と DSI633I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明のみに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では LCON-MAX-QUEUE-RTMGR を IBM Z NetViewの確認記録に残し、対象名は置換検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-VIEWMGR {#c32-i4109}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-VIEWMGRは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.563) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.563)

??? question "確認問題（1問）"
    **問題.** 終端検査の管理リファレンスに関係する LCON-MAX-QUEUE-VIEWMGR の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、終端検査の証跡として残す。 ✅
    - B. LCON-MAX-QUEUE-VIEWMGR の名称と担当者名のみを残して終端検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では LCON-MAX-QUEUE-VIEWMGR は「LCON-MAX-QUEUE-VIEWMGR の用途をネットビューの表示で確認する終端検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では IBM Z NetViewの LCON-MAX-QUEUE-VIEWMGR と DSI633I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明のみに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では LCON-MAX-QUEUE-VIEWMGR を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-MAX-QUEUE-VSTATMGR {#c32-i4110}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-MAX-QUEUE-VSTATMGRは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.564) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.564)

??? question "確認問題（1問）"
    **問題.** 探索検査の管理リファレンスで LCON-MAX-QUEUE-VSTATMGR の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LCON-MAX-QUEUE-VSTATMGR の出力を取らず探索検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索検査の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して探索検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では LCON-MAX-QUEUE-VSTATMGR は「探索検査の管理リファレンスに関係する定義値と表示行を照合する探索検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では LCON-MAX-QUEUE-VSTATMGR の属性行と DSI633I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明のみに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では LCON-MAX-QUEUE-VSTATMGR を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-NCC-RETRY-LIMIT {#c32-i4111}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-NCC-RETRY-LIMITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.565) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.565)

??? question "確認問題（1問）"
    **問題.** 上書検査の管理リファレンスでネットビューの運用確認を行います。LCON-NCC-RETRY-LIMIT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書検査の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書検査の根拠にする。 ✅
    - D. LCON-NCC-RETRY-LIMIT の属性行を読まず上書検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では LCON-NCC-RETRY-LIMIT は「IBM Z NetViewで LCON-NCC-RETRY-LIMIT の扱いを記録する上書検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では LCON-NCC-RETRY-LIMIT の表示結果と DSI633I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明のみに寄り、判定名は上書検査不足です。上書検査資料では LCON-NCC-RETRY-LIMIT の使い方を出典欄から追跡し、資料名は上書検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-NCC-RSC-LIMIT {#c32-i4112}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-NCC-RSC-LIMITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.565) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.565)

??? question "確認問題（1問）"
    **問題.** 出力検査の管理リファレンスに関する LCON-NCC-RSC-LIMIT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力検査の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-NCC-RSC-LIMIT の変更点を出力本文から切り離して出力検査の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、出力検査の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では LCON-NCC-RSC-LIMIT は「LCON-NCC-RSC-LIMIT の状態と出力メッセージを結び付ける出力検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では LCON-NCC-RSC-LIMIT の出力行と DSI633I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明のみに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では LCON-NCC-RSC-LIMIT を IBM Z NetViewの確認記録に残し、対象名は出力検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-NMG-POLL-INTERVAL {#c32-i4113}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-NMG-POLL-INTERVALは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.566) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.566)

??? question "確認問題（1問）"
    **問題.** 条件検査の管理リファレンスに関係する LCON-NMG-POLL-INTERVAL の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、条件検査の採否を説明欄に結び付ける。 ✅
    - B. LCON-NMG-POLL-INTERVAL の名称と担当者名のみを残して条件検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では LCON-NMG-POLL-INTERVAL は「LCON-NMG-POLL-INTERVAL の用途をネットビューの表示で確認する条件検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では IBM Z NetViewの LCON-NMG-POLL-INTERVAL と DSI633I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明のみに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では LCON-NMG-POLL-INTERVAL を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-OPERATOR-CMD-AUDIT {#c32-i4114}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-OPERATOR-CMD-AUDITは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.567) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.567)

??? question "確認問題（1問）"
    **問題.** 区切検査の管理リファレンスで LCON-OPERATOR-CMD-AUDIT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LCON-OPERATOR-CMD-AUDIT の出力を取らず区切検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切検査として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して区切検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では LCON-OPERATOR-CMD-AUDIT は「区切検査の管理リファレンスに関係する定義値と表示行を照合する区切検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では LCON-OPERATOR-CMD-AUDIT の属性行と DSI633I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明のみに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では LCON-OPERATOR-CMD-AUDIT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-REPORT-UNKNOWN-STATUS {#c32-i4115}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-REPORT-UNKNOWN-STATUSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.567) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.567)

??? question "確認問題（1問）"
    **問題.** 範囲検査の管理リファレンスでネットビューの運用確認を行います。LCON-REPORT-UNKNOWN-STAT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲検査の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲検査の確認にする。 ✅
    - D. LCON-REPORT-UNKNOWN-STAT の属性行を読まず範囲検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では LCON-REPORT-UNKNOWN-STAT は「IBM Z NetViewで LCON-REPORT-UNKNOWN-STAT の扱いを記録する範囲検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では LCON-REPORT-UNKNOWN-STAT の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明のみに寄り、判定名は範囲検査不足です。範囲検査資料では LCON-REPORT-UNKNOWN-STAT の使い方を出典欄から追跡し、資料名は範囲検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-STATUS-DELAY-MAX {#c32-i4116}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-STATUS-DELAY-MAXは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.568) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.568)

??? question "確認問題（1問）"
    **問題.** 優先検査の管理リファレンスに関する LCON-STATUS-DELAY-MAX の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先検査の管理リファレンスの証跡として保存して根拠にする。
    - C. LCON-STATUS-DELAY-MAX の変更点を出力本文から切り離して優先検査の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、優先検査の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では LCON-STATUS-DELAY-MAX は「LCON-STATUS-DELAY-MAX の状態と出力メッセージを結び付ける優先検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では LCON-STATUS-DELAY-MAX の出力行と DSI633I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明のみに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では LCON-STATUS-DELAY-MAX を IBM Z NetViewの確認記録に残し、対象名は優先検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LCON-STATUS-DELAY-TIME {#c32-i4117}
*分類: 管理リファレンス*  ・  難易度: 中級

LCON-STATUS-DELAY-TIMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.568) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.568)

??? question "確認問題（1問）"
    **問題.** 記録検査の管理リファレンスに関係する LCON-STATUS-DELAY-TIME の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録検査で再確認できる形にする。 ✅
    - B. LCON-STATUS-DELAY-TIME の名称と担当者名のみを残して記録検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では LCON-STATUS-DELAY-TIME は「LCON-STATUS-DELAY-TIME の用途をネットビューの表示で確認する記録検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では IBM Z NetViewの LCON-STATUS-DELAY-TIME と DSI633I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明のみに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では LCON-STATUS-DELAY-TIME を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LEVEL {#c32-i4118}
*分類: 管理リファレンス*  ・  難易度: 中級

LEVELは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.569) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.569)

??? question "確認問題（1問）"
    **問題.** 比較検査の管理リファレンスで LEVEL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LEVEL の出力を取らず比較検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較検査の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して比較検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では LEVEL は「比較検査の管理リファレンスに関係する定義値と表示行を照合する比較検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では LEVEL の属性行と DSI633I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明のみに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では LEVEL を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LOADEXIT {#c32-i4119}
*分類: 管理リファレンス*  ・  難易度: 上級

LOADEXITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.149) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.149)

??? question "確認問題（1問）"
    **問題.** 順序検査の管理リファレンスでネットビューの運用確認を行います。LOADEXIT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序検査の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序検査の根拠を固定する。 ✅
    - D. LOADEXIT の属性行を読まず順序検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では LOADEXIT は「IBM Z NetViewで LOADEXIT の扱いを記録する順序検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では LOADEXIT の表示結果と DSI633I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明のみに寄り、判定名は順序検査不足です。順序検査資料では LOADEXIT の使い方を出典欄から追跡し、資料名は順序検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LOCKIND {#c32-i4120}
*分類: 管理リファレンス*  ・  難易度: 中級

LOCKINDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.347) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.347)

??? question "確認問題（1問）"
    **問題.** 警告検査の管理リファレンスに関係する LOCKIND の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、警告検査の証跡として残す。 ✅
    - B. LOCKIND の名称と担当者名のみを残して警告検査の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告検査の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告検査の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では LOCKIND は「LOCKIND の用途をネットビューの表示で確認する警告検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では IBM Z NetViewの LOCKIND と DSI633I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明のみに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では LOCKIND を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告検査用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LOGINIT {#c32-i4121}
*分類: 管理リファレンス*  ・  難易度: 中級

LOGINITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.348) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.348)

??? question "確認問題（1問）"
    **問題.** 監査検査の管理リファレンスでネットビューの運用確認を行います。LOGINIT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査検査の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査検査の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査検査の根拠にする。 ✅
    - D. LOGINIT の属性行を読まず監査検査の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では LOGINIT は「IBM Z NetViewで LOGINIT の扱いを記録する監査検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では LOGINIT の表示結果と DSI633I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明のみに寄り、判定名は監査検査不足です。監査検査資料では LOGINIT の使い方を出典欄から追跡し、資料名は監査検査資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LOGONPW {#c32-i4122}
*分類: 管理リファレンス*  ・  難易度: 中級

LOGONPWは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.150) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.150)

??? question "確認問題（1問）"
    **問題.** 変更検査の管理リファレンスに関する LOGONPW の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更検査の管理リファレンスの証跡として保存して根拠にする。
    - C. LOGONPW の変更点を出力本文から切り離して変更検査の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、変更検査の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では LOGONPW は「LOGONPW の状態と出力メッセージを結び付ける変更検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では LOGONPW の出力行と DSI633I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明のみに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では LOGONPW を IBM Z NetViewの確認記録に残し、対象名は変更検査対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LOG_LEVEL {#c32-i4123}
*分類: 管理リファレンス*  ・  難易度: 中級

LOG_LEVELは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.535) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.535)

??? question "確認問題（1問）"
    **問題.** 復旧検査の管理リファレンスで LOG_LEVEL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LOG_LEVEL の出力を取らず復旧検査の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧検査の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して復旧検査の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧検査の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では LOG_LEVEL は「復旧検査の管理リファレンスに関係する定義値と表示行を照合する復旧検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では LOG_LEVEL の属性行と DSI633I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明のみに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では LOG_LEVEL を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧検査初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LSTHRESH {#c32-i4124}
*分類: 管理リファレンス*  ・  難易度: 中級

LSTHRESHは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.454) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.454)

??? question "確認問題（1問）"
    **問題.** 構文判定の管理リファレンスに関係する LSTHRESH の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、構文判定の採否を説明欄に結び付ける。 ✅
    - B. LSTHRESH の名称と担当者名のみを残して構文判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では LSTHRESH は「LSTHRESH の用途をネットビューの表示で確認する構文判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では IBM Z NetViewの LSTHRESH と DSI633I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明のみに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では LSTHRESH を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### LUC {#c32-i4125}
*分類: 管理リファレンス*  ・  難易度: 中級

LUCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.151) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.151)

??? question "確認問題（1問）"
    **問題.** 展開判定の管理リファレンスで LUC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. LUC の出力を取らず展開判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開判定として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して展開判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では LUC は「展開判定の管理リファレンスに関係する定義値と表示行を照合する展開判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では LUC の属性行と DSI633I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明のみに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では LUC を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### Location of Statements and Samples {#c32-i4126}
*分類: 管理リファレンス*  ・  難易度: 中級

Location of Statements and Samplesは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。Tivoli NetView z/OS 自動化 の運用では、対象機能と確認すべき状態を結び付けて読みます

**出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference

??? question "確認問題（1問）"
    **問題.** 値域検査の管理リファレンスに関する Location 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域検査の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域検査の管理リファレンスの証跡として保存して根拠にする。
    - C. Location 機能の変更点を出力本文から切り離して値域検査の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を値域検査で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では Location 機能 は「Location 機能の状態と出力メッセージを結び付ける値域検査項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では Location 機能の出力行と DSI633I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明のみに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では Location 機能を IBM Z NetViewの確認記録に残し、対象名は値域検査対象です。

    **出典:** NetView_6.4_Automation_Guide / NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Administration_Reference / NetView_6.4_Security_Reference



### M (Maximum) {#c32-i4127}
*分類: 管理リファレンス*  ・  難易度: 中級

M (Maximum)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.350) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.350)

??? question "確認問題（1問）"
    **問題.** 呼出判定の管理リファレンスでネットビューの運用確認を行います。M (Maximum)の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出判定の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出判定の確認にする。 ✅
    - D. M (Maximum)の属性行を読まず呼出判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では M (Maximum) は「IBM Z NetViewで M (Maximum)の扱いを記録する呼出判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では M (Maximum)の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明のみに寄り、判定名は呼出判定不足です。呼出判定資料では M (Maximum)の使い方を出典欄から追跡し、資料名は呼出判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MAPSESS {#c32-i4128}
*分類: 管理リファレンス*  ・  難易度: 中級

MAPSESSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.351) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.351)

??? question "確認問題（1問）"
    **問題.** 置換判定の管理リファレンスに関する MAPSESS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換判定の管理リファレンスの証跡として保存して根拠にする。
    - C. MAPSESS の変更点を出力本文から切り離して置換判定の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、置換判定の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では MAPSESS は「MAPSESS の状態と出力メッセージを結び付ける置換判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では MAPSESS の出力行と DSI633I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明のみに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では MAPSESS を IBM Z NetViewの確認記録に残し、対象名は置換判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MAX_CHUNK {#c32-i4129}
*分類: 管理リファレンス*  ・  難易度: 中級

MAX_CHUNKは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.535) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.535)

??? question "確認問題（1問）"
    **問題.** 終端判定の管理リファレンスに関係する MAX_CHUNK の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端判定で再確認できる形にする。 ✅
    - B. MAX_CHUNK の名称と担当者名のみを残して終端判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では MAX_CHUNK は「MAX_CHUNK の用途をネットビューの表示で確認する終端判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では IBM Z NetViewの MAX_CHUNK と DSI633I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明のみに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では MAX_CHUNK を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MAX_SEGMENT_NUM {#c32-i4130}
*分類: 管理リファレンス*  ・  難易度: 中級

MAX_SEGMENT_NUMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.536) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.536)

??? question "確認問題（1問）"
    **問題.** 探索判定の管理リファレンスで MAX_SEGMENT_NUM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MAX_SEGMENT_NUM の出力を取らず探索判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索判定の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して探索判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では MAX_SEGMENT_NUM は「探索判定の管理リファレンスに関係する定義値と表示行を照合する探索判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では MAX_SEGMENT_NUM の属性行と DSI633I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明のみに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では MAX_SEGMENT_NUM を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MAX_WINDOW_NUM {#c32-i4131}
*分類: 管理リファレンス*  ・  難易度: 中級

MAX_WINDOW_NUMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.536) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.536)

??? question "確認問題（1問）"
    **問題.** 上書判定の管理リファレンスでネットビューの運用確認を行います。MAX_WINDOW_NUM の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書判定の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書判定の根拠を固定する。 ✅
    - D. MAX_WINDOW_NUM の属性行を読まず上書判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では MAX_WINDOW_NUM は「IBM Z NetViewで MAX_WINDOW_NUM の扱いを記録する上書判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では MAX_WINDOW_NUM の表示結果と DSI633I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明のみに寄り、判定名は上書判定不足です。上書判定資料では MAX_WINDOW_NUM の使い方を出典欄から追跡し、資料名は上書判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MLINDENT {#c32-i4132}
*分類: 管理リファレンス*  ・  難易度: 中級

MLINDENTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.353) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.353)

??? question "確認問題（1問）"
    **問題.** 条件判定の管理リファレンスに関係する MLINDENT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、条件判定の証跡として残す。 ✅
    - B. MLINDENT の名称と担当者名のみを残して条件判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では MLINDENT は「MLINDENT の用途をネットビューの表示で確認する条件判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では IBM Z NetViewの MLINDENT と DSI633I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明のみに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では MLINDENT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MLOG_LEVEL {#c32-i4133}
*分類: 管理リファレンス*  ・  難易度: 中級

MLOG_LEVELは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.537) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.537)

??? question "確認問題（1問）"
    **問題.** 区切判定の管理リファレンスで MLOG_LEVEL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MLOG_LEVEL の出力を取らず区切判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切判定の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して区切判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では MLOG_LEVEL は「区切判定の管理リファレンスに関係する定義値と表示行を照合する区切判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では MLOG_LEVEL の属性行と DSI633I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明のみに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では MLOG_LEVEL を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MODE {#c32-i4134}
*分類: 管理リファレンス*  ・  難易度: 中級

MODEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.353) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.353)

??? question "確認問題（1問）"
    **問題.** 範囲判定の管理リファレンスでネットビューの運用確認を行います。MODE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲判定の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲判定の根拠にする。 ✅
    - D. MODE の属性行を読まず範囲判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では MODE は「IBM Z NetViewで MODE の扱いを記録する範囲判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では MODE の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明のみに寄り、判定名は範囲判定不足です。範囲判定資料では MODE の使い方を出典欄から追跡し、資料名は範囲判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MODIFY.TOWER {#c32-i4135}
*分類: 管理リファレンス*  ・  難易度: 中級

MODIFY.TOWERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。`MODIFY.TOWER` は CNMSTYLE 初期化メンバーで定義する設定文。Specifies the time interval in minutes that memStore tests for usage. (出典 p.154)

**出典:** IBM Z NetView 6.4 Administration Reference (p.154)

??? question "確認問題（1問）"
    **問題.** 優先判定の管理リファレンスに関する MODIFY.TOWER の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先判定の管理リファレンスの証跡として保存して根拠にする。
    - C. MODIFY.TOWER の変更点を出力本文から切り離して優先判定の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、優先判定の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では MODIFY.TOWER は「MODIFY.TOWER の状態と出力メッセージを結び付ける優先判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では MODIFY.TOWER の出力行と DSI633I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明のみに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では MODIFY.TOWER を IBM Z NetViewの確認記録に残し、対象名は優先判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MONIT {#c32-i4136}
*分類: 管理リファレンス*  ・  難易度: 中級

MONITは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.455) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.455)

??? question "確認問題（1問）"
    **問題.** 記録判定の管理リファレンスに関係する MONIT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、記録判定の採否を説明欄に結び付ける。 ✅
    - B. MONIT の名称と担当者名のみを残して記録判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では MONIT は「MONIT の用途をネットビューの表示で確認する記録判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では IBM Z NetViewの MONIT と DSI633I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明のみに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では MONIT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MONITOR {#c32-i4137}
*分類: 管理リファレンス*  ・  難易度: 中級

MONITORは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.457) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.457)

??? question "確認問題（1問）"
    **問題.** 比較判定の管理リファレンスで MONITOR の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MONITOR の出力を取らず比較判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較判定として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して比較判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では MONITOR は「比較判定の管理リファレンスに関係する定義値と表示行を照合する比較判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では MONITOR の属性行と DSI633I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明のみに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では MONITOR を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MSG.TECROUTE {#c32-i4138}
*分類: 管理リファレンス*  ・  難易度: 中級

MSG.TECROUTEは、Tivoli NetView z/OS 自動化の管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。`MSG.TECROUTE` は CNMSTYLE 初期化メンバーで定義する設定文。Specifies the time interval in minutes that memStore tests for usage. (出典 p.155)

**出典:** IBM Z NetView 6.4 Administration Reference (p.155)

??? question "確認問題（1問）"
    **問題.** 順序判定の管理リファレンスでネットビューの運用確認を行います。MSG.TECROUTE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序判定の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序判定の確認にする。 ✅
    - D. MSG.TECROUTE の属性行を読まず順序判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では MSG.TECROUTE は「IBM Z NetViewで MSG.TECROUTE の扱いを記録する順序判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では MSG.TECROUTE の表示結果と DSI633I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明のみに寄り、判定名は順序判定不足です。順序判定資料では MSG.TECROUTE の使い方を出典欄から追跡し、資料名は順序判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MSGCFG {#c32-i4139}
*分類: 管理リファレンス*  ・  難易度: 中級

MSGCFGは、Tivoli NetView z/OS 自動化の管理リファレンスでメッセージや異常終了の原因を切り分けるための項目です。メッセージ ID、戻りコード、発生した機能の順に確認すると、対応範囲を絞れます。IBM Z NetView 6.4 Administration Reference (p.513) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.513)

??? question "確認問題（1問）"
    **問題.** 値域判定の管理リファレンスに関する MSGCFG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域判定の管理リファレンスの証跡として保存して根拠にする。
    - C. MSGCFG の変更点を出力本文から切り離して値域判定の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、値域判定の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では MSGCFG は「MSGCFG の状態と出力メッセージを結び付ける値域判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では MSGCFG の出力行と DSI633I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明のみに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では MSGCFG を IBM Z NetViewの確認記録に残し、対象名は値域判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MTRACE_TYPE {#c32-i4140}
*分類: 管理リファレンス*  ・  難易度: 上級

MTRACE_TYPEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.537) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.537)

??? question "確認問題（1問）"
    **問題.** 警告判定の管理リファレンスに関係する MTRACE_TYPE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告判定で再確認できる形にする。 ✅
    - B. MTRACE_TYPE の名称と担当者名のみを残して警告判定の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告判定の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告判定の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では MTRACE_TYPE は「MTRACE_TYPE の用途をネットビューの表示で確認する警告判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では IBM Z NetViewの MTRACE_TYPE と DSI633I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明のみに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では MTRACE_TYPE を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告判定用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVS {#c32-i4141}
*分類: 管理リファレンス*  ・  難易度: 中級

MVSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.354) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.354)

??? question "確認問題（1問）"
    **問題.** 復旧判定の管理リファレンスで MVS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. MVS の出力を取らず復旧判定の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧判定の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して復旧判定の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧判定の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では MVS は「復旧判定の管理リファレンスに関係する定義値と表示行を照合する復旧判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では MVS の属性行と DSI633I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明のみに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では MVS を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧判定初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVSPARM.ActionDescCodes {#c32-i4142}
*分類: 管理リファレンス*  ・  難易度: 中級

MVSPARM.ActionDescCodesは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.156) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.156)

??? question "確認問題（1問）"
    **問題.** 監査判定の管理リファレンスでネットビューの運用確認を行います。MVSPARM 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査判定の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査判定の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査判定の根拠を固定する。 ✅
    - D. MVSPARM 属性の属性行を読まず監査判定の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では MVSPARM 属性 は「IBM Z NetViewで MVSPARM 属性の扱いを記録する監査判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では MVSPARM 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明のみに寄り、判定名は監査判定不足です。監査判定資料では MVSPARM 属性の使い方を出典欄から追跡し、資料名は監査判定資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVSPARM.DEFAUTH {#c32-i4143}
*分類: 管理リファレンス*  ・  難易度: 中級

MVSPARM.DEFAUTHは、Tivoli NetView z/OS 自動化の管理リファレンスで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Administration Reference (p.158) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.158)

??? question "確認問題（1問）"
    **問題.** 変更判定の管理リファレンスに関する MVSPARM.DEFAUTH の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更判定の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更判定の管理リファレンスの証跡として保存して根拠にする。
    - C. MVSPARM.DEFAUTH の変更点を出力本文から切り離して変更判定の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を変更判定で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では MVSPARM.DEFAUTH は「MVSPARM.DEFAUTH の状態と出力メッセージを結び付ける変更判定項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では MVSPARM.DEFAUTH の出力行と DSI633I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明のみに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では MVSPARM.DEFAUTH を IBM Z NetViewの確認記録に残し、対象名は変更判定対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### MVSPARM.OperRecvBrdcst {#c32-i4144}
*分類: 管理リファレンス*  ・  難易度: 中級

MVSPARM.OperRecvBrdcstは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.162) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.162)

??? question "確認問題（1問）"
    **問題.** 構文整理の管理リファレンスに関係する MVSPARM 属性の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、構文整理の証跡として残す。 ✅
    - B. MVSPARM 属性の名称と担当者名のみを残して構文整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では MVSPARM 属性 は「MVSPARM 属性の用途をネットビューの表示で確認する構文整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景では IBM Z NetViewの MVSPARM 属性と DSI633I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明のみに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では MVSPARM 属性を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.DESTPPI {#c32-i4145}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.DESTPPIは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.163) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.163)

??? question "確認問題（1問）"
    **問題.** 展開整理の管理リファレンスで NACMD.DESTPPI の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NACMD.DESTPPI の出力を取らず展開整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開整理の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して展開整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では NACMD.DESTPPI は「展開整理の管理リファレンスに関係する定義値と表示行を照合する展開整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では NACMD.DESTPPI の属性行と DSI633I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明のみに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では NACMD.DESTPPI を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.INTCONINACT {#c32-i4146}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.INTCONINACTは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.164) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.164)

??? question "確認問題（1問）"
    **問題.** 呼出整理の管理リファレンスでネットビューの運用確認を行います。NACMD.INTCONINACT の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出整理の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出整理の根拠にする。 ✅
    - D. NACMD.INTCONINACT の属性行を読まず呼出整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では NACMD.INTCONINACT は「IBM Z NetViewで NACMD.INTCONINACT の扱いを記録する呼出整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では NACMD.INTCONINACT の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明のみに寄り、判定名は呼出整理不足です。呼出整理資料では NACMD.INTCONINACT の使い方を出典欄から追跡し、資料名は呼出整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.INTCONNACT {#c32-i4147}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.INTCONNACTは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.164) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.164)

??? question "確認問題（1問）"
    **問題.** 置換整理の管理リファレンスに関する NACMD.INTCONNACT の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換整理の管理リファレンスの証跡として保存して根拠にする。
    - C. NACMD.INTCONNACT の変更点を出力本文から切り離して置換整理の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、置換整理の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では NACMD.INTCONNACT は「NACMD.INTCONNACT の状態と出力メッセージを結び付ける置換整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では NACMD.INTCONNACT の出力行と DSI633I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明のみに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では NACMD.INTCONNACT を IBM Z NetViewの確認記録に残し、対象名は置換整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.INTHEALTH {#c32-i4148}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.INTHEALTHは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.165) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.165)

??? question "確認問題（1問）"
    **問題.** 終端整理の管理リファレンスに関係する NACMD.INTHEALTH の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、終端整理の採否を説明欄に結び付ける。 ✅
    - B. NACMD.INTHEALTH の名称と担当者名のみを残して終端整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では NACMD.INTHEALTH は「NACMD.INTHEALTH の用途をネットビューの表示で確認する終端整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景では IBM Z NetViewの NACMD.INTHEALTH と DSI633I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明のみに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では NACMD.INTHEALTH を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.INTSESSACT {#c32-i4149}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.INTSESSACTは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.165) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.165)

??? question "確認問題（1問）"
    **問題.** 探索整理の管理リファレンスで NACMD.INTSESSACT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NACMD.INTSESSACT の出力を取らず探索整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索整理として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して探索整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では NACMD.INTSESSACT は「探索整理の管理リファレンスに関係する定義値と表示行を照合する探索整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では NACMD.INTSESSACT の属性行と DSI633I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明のみに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では NACMD.INTSESSACT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.LCLPPIRV {#c32-i4150}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.LCLPPIRVは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.166) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.166)

??? question "確認問題（1問）"
    **問題.** 上書整理の管理リファレンスでネットビューの運用確認を行います。NACMD.LCLPPIRV の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書整理の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書整理の確認にする。 ✅
    - D. NACMD.LCLPPIRV の属性行を読まず上書整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では NACMD.LCLPPIRV は「IBM Z NetViewで NACMD.LCLPPIRV の扱いを記録する上書整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では NACMD.LCLPPIRV の表示結果と DSI633I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明のみに寄り、判定名は上書整理不足です。上書整理資料では NACMD.LCLPPIRV の使い方を出典欄から追跡し、資料名は上書整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.OPID {#c32-i4151}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.OPIDは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.166) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.166)

??? question "確認問題（1問）"
    **問題.** 出力整理の管理リファレンスに関する NACMD.OPID の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力整理の管理リファレンスの証跡として保存して根拠にする。
    - C. NACMD.OPID の変更点を出力本文から切り離して出力整理の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、出力整理の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では NACMD.OPID は「NACMD.OPID の状態と出力メッセージを結び付ける出力整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では NACMD.OPID の出力行と DSI633I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明のみに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では NACMD.OPID を IBM Z NetViewの確認記録に残し、対象名は出力整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.PERSIST {#c32-i4152}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.PERSISTは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.167) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.167)

??? question "確認問題（1問）"
    **問題.** 条件整理の管理リファレンスに関係する NACMD.PERSIST の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件整理で再確認できる形にする。 ✅
    - B. NACMD.PERSIST の名称と担当者名のみを残して条件整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では NACMD.PERSIST は「NACMD.PERSIST の用途をネットビューの表示で確認する条件整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景では IBM Z NetViewの NACMD.PERSIST と DSI633I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明のみに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では NACMD.PERSIST を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.ROWSxxx {#c32-i4153}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.ROWSxxxは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.168) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.168)

??? question "確認問題（1問）"
    **問題.** 区切整理の管理リファレンスで NACMD.ROWSxxxの点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NACMD.ROWSxxxの出力を取らず区切整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切整理の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して区切整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では NACMD.ROWSxxx は「区切整理の管理リファレンスに関係する定義値と表示行を照合する区切整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では NACMD.ROWSxxxの属性行と DSI633I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明のみに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では NACMD.ROWSxxxを Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.SUBNODE {#c32-i4154}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.SUBNODEは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.169) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.169)

??? question "確認問題（1問）"
    **問題.** 範囲整理の管理リファレンスでネットビューの運用確認を行います。NACMD.SUBNODE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲整理の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲整理の根拠を固定する。 ✅
    - D. NACMD.SUBNODE の属性行を読まず範囲整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では NACMD.SUBNODE は「IBM Z NetViewで NACMD.SUBNODE の扱いを記録する範囲整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では NACMD.SUBNODE の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明のみに寄り、判定名は範囲整理不足です。範囲整理資料では NACMD.SUBNODE の使い方を出典欄から追跡し、資料名は範囲整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NACMD.WAITSECS {#c32-i4155}
*分類: 管理リファレンス*  ・  難易度: 中級

NACMD.WAITSECSは、Tivoli NetView z/OS 自動化の管理リファレンスで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.170) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.170)

??? question "確認問題（1問）"
    **問題.** 優先整理の管理リファレンスに関する NACMD.WAITSECS の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先整理の管理リファレンスの証跡として保存して根拠にする。
    - C. NACMD.WAITSECS の変更点を出力本文から切り離して優先整理の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を優先整理で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では NACMD.WAITSECS は「NACMD.WAITSECS の状態と出力メッセージを結び付ける優先整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では NACMD.WAITSECS の出力行と DSI633I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明のみに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では NACMD.WAITSECS を IBM Z NetViewの確認記録に残し、対象名は優先整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NCPRECOV (SNA) {#c32-i4156}
*分類: 管理リファレンス*  ・  難易度: 中級

NCPRECOV (SNA)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.457) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.457)

??? question "確認問題（1問）"
    **問題.** 記録整理の管理リファレンスに関係する NCPRECOV (SNA)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、記録整理の証跡として残す。 ✅
    - B. NCPRECOV (SNA)の名称と担当者名のみを残して記録整理の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録整理の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録整理の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では NCPRECOV (SNA) は「NCPRECOV (SNA)の用途をネットビューの表示で確認する記録整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景では IBM Z NetViewの NCPRECOV (SNA)と DSI633I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明のみに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では NCPRECOV (SNA)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録整理用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NETCONV_IP {#c32-i4157}
*分類: 管理リファレンス*  ・  難易度: 中級

NETCONV_IPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.355) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.355)

??? question "確認問題（1問）"
    **問題.** 比較整理の管理リファレンスで NETCONV_IP の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NETCONV_IP の出力を取らず比較整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較整理の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して比較整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では NETCONV_IP は「比較整理の管理リファレンスに関係する定義値と表示行を照合する比較整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では NETCONV_IP の属性行と DSI633I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明のみに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では NETCONV_IP を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.AMLUTDLY {#c32-i4158}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.AMLUTDLYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.171) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.171)

??? question "確認問題（1問）"
    **問題.** 復旧整理の管理リファレンスで NLDM.AMLUTDLY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.AMLUTDLY の出力を取らず復旧整理の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧整理として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して復旧整理の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧整理の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では NLDM.AMLUTDLY は「復旧整理の管理リファレンスに関係する定義値と表示行を照合する復旧整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では NLDM.AMLUTDLY の属性行と DSI633I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明のみに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では NLDM.AMLUTDLY を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧整理初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.AUTHDOM {#c32-i4159}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.AUTHDOMは、Tivoli NetView z/OS 自動化の管理リファレンスで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Administration Reference (p.171) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.171)

??? question "確認問題（1問）"
    **問題.** 監査整理の管理リファレンスでネットビューの運用確認を行います。NLDM.AUTHDOM の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査整理の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査整理の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査整理の確認にする。 ✅
    - D. NLDM.AUTHDOM の属性行を読まず監査整理の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では NLDM.AUTHDOM は「IBM Z NetViewで NLDM.AUTHDOM の扱いを記録する監査整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では NLDM.AUTHDOM の表示結果と DSI633I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明のみに寄り、判定名は監査整理不足です。監査整理資料では NLDM.AUTHDOM の使い方を出典欄から追跡し、資料名は監査整理資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.AUTHORIZ {#c32-i4160}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.AUTHORIZは、Tivoli NetView z/OS 自動化の管理リファレンスで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。IBM Z NetView 6.4 Administration Reference (p.172) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.172)

??? question "確認問題（1問）"
    **問題.** 変更整理の管理リファレンスに関する NLDM.AUTHORIZ の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更整理の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更整理の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.AUTHORIZ の変更点を出力本文から切り離して変更整理の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、変更整理の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では NLDM.AUTHORIZ は「NLDM.AUTHORIZ の状態と出力メッセージを結び付ける変更整理項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では NLDM.AUTHORIZ の出力行と DSI633I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明のみに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では NLDM.AUTHORIZ を IBM Z NetViewの確認記録に残し、対象名は変更整理対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.CDRMDEF {#c32-i4161}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.CDRMDEFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.173) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.173)

??? question "確認問題（1問）"
    **問題.** 構文記録の管理リファレンスに関係する NLDM.CDRMDEF の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文記録で再確認できる形にする。 ✅
    - B. NLDM.CDRMDEF の名称と担当者名のみを残して構文記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では NLDM.CDRMDEF は「NLDM.CDRMDEF の用途をネットビューの表示で確認する構文記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景では IBM Z NetViewの NLDM.CDRMDEF と DSI633I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明のみに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では NLDM.CDRMDEF を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.CDTIME {#c32-i4162}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.CDTIMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.174) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.174)

??? question "確認問題（1問）"
    **問題.** 展開記録の管理リファレンスで NLDM.CDTIME の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.CDTIME の出力を取らず展開記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開記録の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して展開記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では NLDM.CDTIME は「展開記録の管理リファレンスに関係する定義値と表示行を照合する展開記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では NLDM.CDTIME の属性行と DSI633I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明のみに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では NLDM.CDTIME を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.DRDELAY {#c32-i4163}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.DRDELAYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.175) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.175)

??? question "確認問題（1問）"
    **問題.** 呼出記録の管理リファレンスでネットビューの運用確認を行います。NLDM.DRDELAY の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出記録の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出記録の根拠を固定する。 ✅
    - D. NLDM.DRDELAY の属性行を読まず呼出記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では NLDM.DRDELAY は「IBM Z NetViewで NLDM.DRDELAY の扱いを記録する呼出記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では NLDM.DRDELAY の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明のみに寄り、判定名は呼出記録不足です。呼出記録資料では NLDM.DRDELAY の使い方を出典欄から追跡し、資料名は呼出記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.DSRBO {#c32-i4164}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.DSRBOは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.175) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.175)

??? question "確認問題（1問）"
    **問題.** 置換記録の管理リファレンスに関する NLDM.DSRBO の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換記録の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.DSRBO の変更点を出力本文から切り離して置換記録の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を置換記録で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では NLDM.DSRBO は「NLDM.DSRBO の状態と出力メッセージを結び付ける置換記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では NLDM.DSRBO の出力行と DSI633I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明のみに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では NLDM.DSRBO を IBM Z NetViewの確認記録に残し、対象名は置換記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.ERCOUNT {#c32-i4165}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.ERCOUNTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.176) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.176)

??? question "確認問題（1問）"
    **問題.** 終端記録の管理リファレンスに関係する NLDM.ERCOUNT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、終端記録の証跡として残す。 ✅
    - B. NLDM.ERCOUNT の名称と担当者名のみを残して終端記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では NLDM.ERCOUNT は「NLDM.ERCOUNT の用途をネットビューの表示で確認する終端記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景では IBM Z NetViewの NLDM.ERCOUNT と DSI633I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明のみに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では NLDM.ERCOUNT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.FCTIME {#c32-i4166}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.FCTIMEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.176) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.176)

??? question "確認問題（1問）"
    **問題.** 探索記録の管理リファレンスで NLDM.FCTIME の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.FCTIME の出力を取らず探索記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、探索記録の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して探索記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では NLDM.FCTIME は「探索記録の管理リファレンスに関係する定義値と表示行を照合する探索記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では NLDM.FCTIME の属性行と DSI633I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明のみに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では NLDM.FCTIME を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.KEEPDISC {#c32-i4167}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.KEEPDISCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.177) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.177)

??? question "確認問題（1問）"
    **問題.** 上書記録の管理リファレンスでネットビューの運用確認を行います。NLDM.KEEPDISC の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書記録の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて上書記録の根拠にする。 ✅
    - D. NLDM.KEEPDISC の属性行を読まず上書記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では NLDM.KEEPDISC は「IBM Z NetViewで NLDM.KEEPDISC の扱いを記録する上書記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では NLDM.KEEPDISC の表示結果と DSI633I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明のみに寄り、判定名は上書記録不足です。上書記録資料では NLDM.KEEPDISC の使い方を出典欄から追跡し、資料名は上書記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.KEEPMEM {#c32-i4168}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.KEEPMEMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.177) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.177)

??? question "確認問題（1問）"
    **問題.** 出力記録の管理リファレンスに関する NLDM.KEEPMEM の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力記録の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.KEEPMEM の変更点を出力本文から切り離して出力記録の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、出力記録の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では NLDM.KEEPMEM は「NLDM.KEEPMEM の状態と出力メッセージを結び付ける出力記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では NLDM.KEEPMEM の出力行と DSI633I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明のみに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では NLDM.KEEPMEM を IBM Z NetViewの確認記録に残し、対象名は出力記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.KEEPPIU {#c32-i4169}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.KEEPPIUは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.178) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.178)

??? question "確認問題（1問）"
    **問題.** 条件記録の管理リファレンスに関係する NLDM.KEEPPIU の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、条件記録の採否を説明欄に結び付ける。 ✅
    - B. NLDM.KEEPPIU の名称と担当者名のみを残して条件記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では NLDM.KEEPPIU は「NLDM.KEEPPIU の用途をネットビューの表示で確認する条件記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では IBM Z NetViewの NLDM.KEEPPIU と DSI633I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明のみに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では NLDM.KEEPPIU を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.KEEPRTM {#c32-i4170}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.KEEPRTMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.178) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.178)

??? question "確認問題（1問）"
    **問題.** 区切記録の管理リファレンスで NLDM.KEEPRTM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.KEEPRTM の出力を取らず区切記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、区切記録として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して区切記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では NLDM.KEEPRTM は「区切記録の管理リファレンスに関係する定義値と表示行を照合する区切記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では NLDM.KEEPRTM の属性行と DSI633I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明のみに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では NLDM.KEEPRTM を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.KEEPSESS {#c32-i4171}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.KEEPSESSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.178) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.178)

??? question "確認問題（1問）"
    **問題.** 範囲記録の管理リファレンスでネットビューの運用確認を行います。NLDM.KEEPSESS の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲記録の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲記録の確認にする。 ✅
    - D. NLDM.KEEPSESS の属性行を読まず範囲記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では NLDM.KEEPSESS は「IBM Z NetViewで NLDM.KEEPSESS の扱いを記録する範囲記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では NLDM.KEEPSESS の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明のみに寄り、判定名は範囲記録不足です。範囲記録資料では NLDM.KEEPSESS の使い方を出典欄から追跡し、資料名は範囲記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.LOG {#c32-i4172}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.LOGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.179) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.179)

??? question "確認問題（1問）"
    **問題.** 優先記録の管理リファレンスに関する NLDM.LOG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先記録の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.LOG の変更点を出力本文から切り離して優先記録の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、優先記録の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では NLDM.LOG は「NLDM.LOG の状態と出力メッセージを結び付ける優先記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では NLDM.LOG の出力行と DSI633I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明のみに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では NLDM.LOG を IBM Z NetViewの確認記録に残し、対象名は優先記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.LUCOUNT {#c32-i4173}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.LUCOUNTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.180) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.180)

??? question "確認問題（1問）"
    **問題.** 記録記録の管理リファレンスに関係する NLDM.LUCOUNT の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録記録で再確認できる形にする。 ✅
    - B. NLDM.LUCOUNT の名称と担当者名のみを残して記録記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では NLDM.LUCOUNT は「NLDM.LUCOUNT の用途をネットビューの表示で確認する記録記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では IBM Z NetViewの NLDM.LUCOUNT と DSI633I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明のみに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では NLDM.LUCOUNT を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.MACRF {#c32-i4174}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.MACRFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.180) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.180)

??? question "確認問題（1問）"
    **問題.** 比較記録の管理リファレンスで NLDM.MACRF の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.MACRF の出力を取らず比較記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、比較記録の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して比較記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では NLDM.MACRF は「比較記録の管理リファレンスに関係する定義値と表示行を照合する比較記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では NLDM.MACRF の属性行と DSI633I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明のみに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では NLDM.MACRF を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.MAXEND {#c32-i4175}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.MAXENDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.181) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.181)

??? question "確認問題（1問）"
    **問題.** 順序記録の管理リファレンスでネットビューの運用確認を行います。NLDM.MAXEND の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序記録の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて順序記録の根拠を固定する。 ✅
    - D. NLDM.MAXEND の属性行を読まず順序記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では NLDM.MAXEND は「IBM Z NetViewで NLDM.MAXEND の扱いを記録する順序記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では NLDM.MAXEND の表示結果と DSI633I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明のみに寄り、判定名は順序記録不足です。順序記録資料では NLDM.MAXEND の使い方を出典欄から追跡し、資料名は順序記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.NETID {#c32-i4176}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.NETIDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.181) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.181)

??? question "確認問題（1問）"
    **問題.** 値域記録の管理リファレンスに関する NLDM.NETID の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域記録の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.NETID の変更点を出力本文から切り離して値域記録の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を値域記録で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では NLDM.NETID は「NLDM.NETID の状態と出力メッセージを結び付ける値域記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では NLDM.NETID の出力行と DSI633I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明のみに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では NLDM.NETID を IBM Z NetViewの確認記録に残し、対象名は値域記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.PDDNM {#c32-i4177}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.PDDNMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.182) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.182)

??? question "確認問題（1問）"
    **問題.** 警告記録の管理リファレンスに関係する NLDM.PDDNM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、警告記録の証跡として残す。 ✅
    - B. NLDM.PDDNM の名称と担当者名のみを残して警告記録の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告記録の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告記録の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では NLDM.PDDNM は「NLDM.PDDNM の用途をネットビューの表示で確認する警告記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では IBM Z NetViewの NLDM.PDDNM と DSI633I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明のみに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では NLDM.PDDNM を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告記録用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.PERFMEM {#c32-i4178}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.PERFMEMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.182) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.182)

??? question "確認問題（1問）"
    **問題.** 復旧記録の管理リファレンスで NLDM.PERFMEM の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.PERFMEM の出力を取らず復旧記録の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、復旧記録の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して復旧記録の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧記録の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では NLDM.PERFMEM は「復旧記録の管理リファレンスに関係する定義値と表示行を照合する復旧記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では NLDM.PERFMEM の属性行と DSI633I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明のみに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では NLDM.PERFMEM を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧記録初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.PEXLSTxx {#c32-i4179}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.PEXLSTxxは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.183) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.183)

??? question "確認問題（1問）"
    **問題.** 監査記録の管理リファレンスでネットビューの運用確認を行います。NLDM.PEXLSTxxの根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査記録の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査記録の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて監査記録の根拠にする。 ✅
    - D. NLDM.PEXLSTxxの属性行を読まず監査記録の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では NLDM.PEXLSTxx は「IBM Z NetViewで NLDM.PEXLSTxxの扱いを記録する監査記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では NLDM.PEXLSTxxの表示結果と DSI633I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明のみに寄り、判定名は監査記録不足です。監査記録資料では NLDM.PEXLSTxxの使い方を出典欄から追跡し、資料名は監査記録資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.PIUTNUM {#c32-i4180}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.PIUTNUMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.184) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.184)

??? question "確認問題（1問）"
    **問題.** 変更記録の管理リファレンスに関する NLDM.PIUTNUM の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更記録の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更記録の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.PIUTNUM の変更点を出力本文から切り離して変更記録の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、変更記録の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では NLDM.PIUTNUM は「NLDM.PIUTNUM の状態と出力メッセージを結び付ける変更記録項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では NLDM.PIUTNUM の出力行と DSI633I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明のみに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では NLDM.PIUTNUM を IBM Z NetViewの確認記録に残し、対象名は変更記録対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.PIUTSIZE {#c32-i4181}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.PIUTSIZEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.185) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.185)

??? question "確認問題（1問）"
    **問題.** 構文分離の管理リファレンスに関係する NLDM.PIUTSIZE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、構文分離の採否を説明欄に結び付ける。 ✅
    - B. NLDM.PIUTSIZE の名称と担当者名のみを残して構文分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では NLDM.PIUTSIZE は「NLDM.PIUTSIZE の用途をネットビューの表示で確認する構文分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では IBM Z NetViewの NLDM.PIUTSIZE と DSI633I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明のみに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では NLDM.PIUTSIZE を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.RETRY {#c32-i4182}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.RETRYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.185) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.185)

??? question "確認問題（1問）"
    **問題.** 展開分離の管理リファレンスで NLDM.RETRY の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.RETRY の出力を取らず展開分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、展開分離として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して展開分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では NLDM.RETRY は「展開分離の管理リファレンスに関係する定義値と表示行を照合する展開分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では NLDM.RETRY の属性行と DSI633I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明のみに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では NLDM.RETRY を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.RTDASD {#c32-i4183}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.RTDASDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.185) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.185)

??? question "確認問題（1問）"
    **問題.** 呼出分離の管理リファレンスでネットビューの運用確認を行います。NLDM.RTDASD の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出分離の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出分離の確認にする。 ✅
    - D. NLDM.RTDASD の属性行を読まず呼出分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では NLDM.RTDASD は「IBM Z NetViewで NLDM.RTDASD の扱いを記録する呼出分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では NLDM.RTDASD の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明のみに寄り、判定名は呼出分離不足です。呼出分離資料では NLDM.RTDASD の使い方を出典欄から追跡し、資料名は呼出分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.RTM {#c32-i4184}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.RTMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.186) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.186)

??? question "確認問題（1問）"
    **問題.** 置換分離の管理リファレンスに関する NLDM.RTM の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず置換分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換分離の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.RTM の変更点を出力本文から切り離して置換分離の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、置換分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では NLDM.RTM は「NLDM.RTM の状態と出力メッセージを結び付ける置換分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では NLDM.RTM の出力行と DSI633I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明のみに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では NLDM.RTM を IBM Z NetViewの確認記録に残し、対象名は置換分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.RTMDISP {#c32-i4185}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.RTMDISPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.186) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.186)

??? question "確認問題（1問）"
    **問題.** 終端分離の管理リファレンスに関係する NLDM.RTMDISP の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端分離で再確認できる形にする。 ✅
    - B. NLDM.RTMDISP の名称と担当者名のみを残して終端分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず終端分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では NLDM.RTMDISP は「NLDM.RTMDISP の用途をネットビューの表示で確認する終端分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では IBM Z NetViewの NLDM.RTMDISP と DSI633I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明のみに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では NLDM.RTMDISP を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.SAW {#c32-i4186}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.SAWは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.187) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.187)

??? question "確認問題（1問）"
    **問題.** 探索分離の管理リファレンスで NLDM.SAW の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.SAW の出力を取らず探索分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、探索分離の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して探索分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では NLDM.SAW は「探索分離の管理リファレンスに関係する定義値と表示行を照合する探索分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では NLDM.SAW の属性行と DSI633I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明のみに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では NLDM.SAW を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.SAWNUM {#c32-i4187}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.SAWNUMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.187) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.187)

??? question "確認問題（1問）"
    **問題.** 上書分離の管理リファレンスでネットビューの運用確認を行います。NLDM.SAWNUM の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず上書分離の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて上書分離の根拠を固定する。 ✅
    - D. NLDM.SAWNUM の属性行を読まず上書分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では NLDM.SAWNUM は「IBM Z NetViewで NLDM.SAWNUM の扱いを記録する上書分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では NLDM.SAWNUM の表示結果と DSI633I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明のみに寄り、判定名は上書分離不足です。上書分離資料では NLDM.SAWNUM の使い方を出典欄から追跡し、資料名は上書分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.SAWSIZE {#c32-i4188}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.SAWSIZEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.188) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.188)

??? question "確認問題（1問）"
    **問題.** 出力分離の管理リファレンスに関する NLDM.SAWSIZE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず出力分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力分離の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.SAWSIZE の変更点を出力本文から切り離して出力分離の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を出力分離で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では NLDM.SAWSIZE は「NLDM.SAWSIZE の状態と出力メッセージを結び付ける出力分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では NLDM.SAWSIZE の出力行と DSI633I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明のみに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では NLDM.SAWSIZE を IBM Z NetViewの確認記録に残し、対象名は出力分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.SDDNM {#c32-i4189}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.SDDNMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.188) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.188)

??? question "確認問題（1問）"
    **問題.** 条件分離の管理リファレンスに関係する NLDM.SDDNM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、条件分離の証跡として残す。 ✅
    - B. NLDM.SDDNM の名称と担当者名のみを残して条件分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず条件分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では NLDM.SDDNM は「NLDM.SDDNM の用途をネットビューの表示で確認する条件分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景では IBM Z NetViewの NLDM.SDDNM と DSI633I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明のみに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では NLDM.SDDNM を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.SESSMAX {#c32-i4190}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.SESSMAXは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.188) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.188)

??? question "確認問題（1問）"
    **問題.** 区切分離の管理リファレンスで NLDM.SESSMAX の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.SESSMAX の出力を取らず区切分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、区切分離の確認記録にまとめる。 ✅
    - C. BROWSE CANZLOG を省略して区切分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では NLDM.SESSMAX は「区切分離の管理リファレンスに関係する定義値と表示行を照合する区切分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では NLDM.SESSMAX の属性行と DSI633I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明のみに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では NLDM.SESSMAX を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.SESSTATS {#c32-i4191}
*分類: 管理リファレンス*  ・  難易度: 中級

NLDM.SESSTATSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.189) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.189)

??? question "確認問題（1問）"
    **問題.** 範囲分離の管理リファレンスでネットビューの運用確認を行います。NLDM.SESSTATS の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず範囲分離の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて範囲分離の根拠にする。 ✅
    - D. NLDM.SESSTATS の属性行を読まず範囲分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では NLDM.SESSTATS は「IBM Z NetViewで NLDM.SESSTATS の扱いを記録する範囲分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では NLDM.SESSTATS の表示結果と DSI633I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明のみに寄り、判定名は範囲分離不足です。範囲分離資料では NLDM.SESSTATS の使い方を出典欄から追跡し、資料名は範囲分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.TRACEGW {#c32-i4192}
*分類: 管理リファレンス*  ・  難易度: 上級

NLDM.TRACEGWは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.189) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.189)

??? question "確認問題（1問）"
    **問題.** 優先分離の管理リファレンスに関する NLDM.TRACEGW の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず優先分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先分離の管理リファレンスの証跡として保存して根拠にする。
    - C. NLDM.TRACEGW の変更点を出力本文から切り離して優先分離の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と DSI633I を読み、優先分離の結果として保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では NLDM.TRACEGW は「NLDM.TRACEGW の状態と出力メッセージを結び付ける優先分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では NLDM.TRACEGW の出力行と DSI633I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明のみに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では NLDM.TRACEGW を IBM Z NetViewの確認記録に残し、対象名は優先分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.TRACELU {#c32-i4193}
*分類: 管理リファレンス*  ・  難易度: 上級

NLDM.TRACELUは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.190) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.190)

??? question "確認問題（1問）"
    **問題.** 記録分離の管理リファレンスに関係する NLDM.TRACELU の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG で得た表示本文を使い、記録分離の採否を説明欄に結び付ける。 ✅
    - B. NLDM.TRACELU の名称と担当者名のみを残して記録分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず記録分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 上級

    **解説:** 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では NLDM.TRACELU は「NLDM.TRACELU の用途をネットビューの表示で確認する記録分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景では IBM Z NetViewの NLDM.TRACELU と DSI633I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明のみに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では NLDM.TRACELU を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NLDM.TRACESC {#c32-i4194}
*分類: 管理リファレンス*  ・  難易度: 上級

NLDM.TRACESCは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.190) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.190)

??? question "確認問題（1問）"
    **問題.** 比較分離の管理リファレンスで NLDM.TRACESC の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NLDM.TRACESC の出力を取らず比較分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、比較分離として引き継ぐ。 ✅
    - C. BROWSE CANZLOG を省略して比較分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 上級

    **解説:** 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では NLDM.TRACESC は「比較分離の管理リファレンスに関係する定義値と表示行を照合する比較分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では NLDM.TRACESC の属性行と DSI633I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明のみに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では NLDM.TRACESC を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NMCSTATUS (Control File Entry) {#c32-i4195}
*分類: 管理リファレンス*  ・  難易度: 中級

NMCSTATUS (Control File Entry)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.356) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.356)

??? question "確認問題（1問）"
    **問題.** 順序分離の管理リファレンスでネットビューの運用確認を行います。NMCSTATUS 属性の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず順序分離の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序分離の確認にする。 ✅
    - D. NMCSTATUS 属性の属性行を読まず順序分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では NMCSTATUS 属性 は「IBM Z NetViewで NMCSTATUS 属性の扱いを記録する順序分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では NMCSTATUS 属性の表示結果と DSI633I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明のみに寄り、判定名は順序分離不足です。順序分離資料では NMCSTATUS 属性の使い方を出典欄から追跡し、資料名は順序分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NMCstatus.errorDSN {#c32-i4196}
*分類: 管理リファレンス*  ・  難易度: 中級

NMCstatus.errorDSNは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.191) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.191)

??? question "確認問題（1問）"
    **問題.** 値域分離の管理リファレンスに関する NMCstatus.errorDSN の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず値域分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域分離の管理リファレンスの証跡として保存して根拠にする。
    - C. NMCstatus.errorDSN の変更点を出力本文から切り離して値域分離の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、値域分離の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では NMCstatus.errorDSN は「NMCstatus.errorDSN の状態と出力メッセージを結び付ける値域分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では NMCstatus.errorDSN の出力行と DSI633I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明のみに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では NMCstatus.errorDSN を IBM Z NetViewの確認記録に残し、対象名は値域分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NOPREFIX {#c32-i4197}
*分類: 管理リファレンス*  ・  難易度: 中級

NOPREFIXは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.369) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.369)

??? question "確認問題（1問）"
    **問題.** 警告分離の管理リファレンスに関係する NOPREFIX の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告分離で再確認できる形にする。 ✅
    - B. NOPREFIX の名称と担当者名のみを残して警告分離の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告分離の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず警告分離の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では NOPREFIX は「NOPREFIX の用途をネットビューの表示で確認する警告分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景では IBM Z NetViewの NOPREFIX と DSI633I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明のみに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では NOPREFIX を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告分離用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NORMAL {#c32-i4198}
*分類: 管理リファレンス*  ・  難易度: 中級

NORMALは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.370) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.370)

??? question "確認問題（1問）"
    **問題.** 復旧分離の管理リファレンスで NORMAL の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NORMAL の出力を取らず復旧分離の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、復旧分離の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して復旧分離の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧分離の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では NORMAL は「復旧分離の管理リファレンスに関係する定義値と表示行を照合する復旧分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では NORMAL の属性行と DSI633I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明のみに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では NORMAL を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧分離初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NORMQMAX {#c32-i4199}
*分類: 管理リファレンス*  ・  難易度: 上級

NORMQMAXは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.371) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.371)

??? question "確認問題（1問）"
    **問題.** 監査分離の管理リファレンスでネットビューの運用確認を行います。NORMQMAX の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査分離の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず監査分離の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて監査分離の根拠を固定する。 ✅
    - D. NORMQMAX の属性行を読まず監査分離の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 上級

    **解説:** 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では NORMQMAX は「IBM Z NetViewで NORMQMAX の扱いを記録する監査分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では NORMQMAX の表示結果と DSI633I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明のみに寄り、判定名は監査分離不足です。監査分離資料では NORMQMAX の使い方を出典欄から追跡し、資料名は監査分離資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NOSTART {#c32-i4200}
*分類: 管理リファレンス*  ・  難易度: 中級

NOSTARTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.514) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.514)

??? question "確認問題（1問）"
    **問題.** 変更分離の管理リファレンスに関する NOSTART の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. BROWSE CANZLOG の結果を残さず変更分離の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更分離の管理リファレンスの証跡として保存して根拠にする。
    - C. NOSTART の変更点を出力本文から切り離して変更分離の管理リファレンスの承認欄のみ残す。
    - D. DSI633I を含む表示を保存し、説明欄との差分を変更分離で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では NOSTART は「NOSTART の状態と出力メッセージを結び付ける変更分離項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では NOSTART の出力行と DSI633I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明のみに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では NOSTART を IBM Z NetViewの確認記録に残し、対象名は変更分離対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NOTIFY {#c32-i4201}
*分類: 管理リファレンス*  ・  難易度: 中級

NOTIFYは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.460) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.460)

??? question "確認問題（1問）"
    **問題.** 構文読解の管理リファレンスに関係する NOTIFY の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. BROWSE CANZLOG の結果から対象行を抜き出し、構文読解の証跡として残す。 ✅
    - B. NOTIFY の名称と担当者名のみを残して構文読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. DSI633I の有無を見ず構文読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では NOTIFY は「NOTIFY の用途をネットビューの表示で確認する構文読解項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景では IBM Z NetViewの NOTIFY と DSI633I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明のみに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では NOTIFY を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.ALCACHE {#c32-i4202}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.ALCACHEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.191) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.191)

??? question "確認問題（1問）"
    **問題.** 展開読解の管理リファレンスで NPDA.ALCACHE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NPDA.ALCACHE の出力を取らず展開読解の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、展開読解の確認記録にまとめる。 ✅
    - C. NPDA を省略して展開読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では NPDA.ALCACHE は「展開読解の管理リファレンスに関係する定義値と表示行を照合する展開読解項目」と NPDA または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では NPDA.ALCACHE の属性行と BNH160I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明のみに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では NPDA.ALCACHE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.ALERTFWD {#c32-i4203}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.ALERTFWDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.193) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.193)

??? question "確認問題（1問）"
    **問題.** 呼出読解の管理リファレンスでネットビューの運用確認を行います。NPDA.ALERTFWD の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出読解の管理リファレンスを確認した扱いにする。
    - B. BNH160I の有無を確認せず呼出読解の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて呼出読解の根拠にする。 ✅
    - D. NPDA.ALERTFWD の属性行を読まず呼出読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では NPDA.ALERTFWD は「IBM Z NetViewで NPDA.ALERTFWD の扱いを記録する呼出読解項目」と NPDA または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では NPDA.ALERTFWD の表示結果と BNH160I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明のみに寄り、判定名は呼出読解不足です。呼出読解資料では NPDA.ALERTFWD の使い方を出典欄から追跡し、資料名は呼出読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.ALERTLOG {#c32-i4204}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.ALERTLOGは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.195) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.195)

??? question "確認問題（1問）"
    **問題.** 置換読解の管理リファレンスに関する NPDA.ALERTLOG の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. NPDA の結果を残さず置換読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを置換読解の管理リファレンスの証跡として保存して根拠にする。
    - C. NPDA.ALERTLOG の変更点を出力本文から切り離して置換読解の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と BNH160I を読み、置換読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では NPDA.ALERTLOG は「NPDA.ALERTLOG の状態と出力メッセージを結び付ける置換読解項目」と NPDA または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では NPDA.ALERTLOG の出力行と BNH160I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明のみに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では NPDA.ALERTLOG を IBM Z NetViewの確認記録に残し、対象名は置換読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.ALRTINFP {#c32-i4205}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.ALRTINFPは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.196) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.196)

??? question "確認問題（1問）"
    **問題.** 終端読解の管理リファレンスに関係する NPDA.ALRTINFP の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. NPDA で得た表示本文を使い、終端読解の採否を説明欄に結び付ける。 ✅
    - B. NPDA.ALRTINFP の名称と担当者名のみを残して終端読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で終端読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず終端読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では NPDA.ALRTINFP は「NPDA.ALRTINFP の用途をネットビューの表示で確認する終端読解項目」と NPDA または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景では IBM Z NetViewの NPDA.ALRTINFP と BNH160I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明のみに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では NPDA.ALRTINFP を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は終端読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.ALT_ALERT {#c32-i4206}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.ALT_ALERTは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.197) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.197)

??? question "確認問題（1問）"
    **問題.** 探索読解の管理リファレンスで NPDA.ALT_ALERT の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NPDA.ALT_ALERT の出力を取らず探索読解の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、探索読解として引き継ぐ。 ✅
    - C. NPDA を省略して探索読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を探索読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では NPDA.ALT_ALERT は「探索読解の管理リファレンスに関係する定義値と表示行を照合する探索読解項目」と NPDA または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では NPDA.ALT_ALERT の属性行と BNH160I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明のみに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では NPDA.ALT_ALERT を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は探索読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.AUTORATE {#c32-i4207}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.AUTORATEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.197) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.197)

??? question "確認問題（1問）"
    **問題.** 上書読解の管理リファレンスでネットビューの運用確認を行います。NPDA.AUTORATE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で上書読解の管理リファレンスを確認した扱いにする。
    - B. BNH160I の有無を確認せず上書読解の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書読解の確認にする。 ✅
    - D. NPDA.AUTORATE の属性行を読まず上書読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では NPDA.AUTORATE は「IBM Z NetViewで NPDA.AUTORATE の扱いを記録する上書読解項目」と NPDA または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では NPDA.AUTORATE の表示結果と BNH160I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明のみに寄り、判定名は上書読解不足です。上書読解資料では NPDA.AUTORATE の使い方を出典欄から追跡し、資料名は上書読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.DSRBO {#c32-i4208}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.DSRBOは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.198) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.198)

??? question "確認問題（1問）"
    **問題.** 出力読解の管理リファレンスに関する NPDA.DSRBO の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. NPDA の結果を残さず出力読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを出力読解の管理リファレンスの証跡として保存して根拠にする。
    - C. NPDA.DSRBO の変更点を出力本文から切り離して出力読解の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、出力読解の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では NPDA.DSRBO は「NPDA.DSRBO の状態と出力メッセージを結び付ける出力読解項目」と NPDA または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では NPDA.DSRBO の出力行と BNH160I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明のみに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では NPDA.DSRBO を IBM Z NetViewの確認記録に残し、対象名は出力読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.DSRBU {#c32-i4209}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.DSRBUは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.199) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.199)

??? question "確認問題（1問）"
    **問題.** 条件読解の管理リファレンスに関係する NPDA.DSRBU の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件読解で再確認できる形にする。 ✅
    - B. NPDA.DSRBU の名称と担当者名のみを残して条件読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で条件読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず条件読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では NPDA.DSRBU は「NPDA.DSRBU の用途をネットビューの表示で確認する条件読解項目」と NPDA または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景では IBM Z NetViewの NPDA.DSRBU と BNH160I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明のみに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では NPDA.DSRBU を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は条件読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.ERR_RATE {#c32-i4210}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.ERR_RATEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.199) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.199)

??? question "確認問題（1問）"
    **問題.** 区切読解の管理リファレンスで NPDA.ERR_RATE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NPDA.ERR_RATE の出力を取らず区切読解の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、区切読解の確認値として扱う。 ✅
    - C. NPDA を省略して区切読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を区切読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では NPDA.ERR_RATE は「区切読解の管理リファレンスに関係する定義値と表示行を照合する区切読解項目」と NPDA または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では NPDA.ERR_RATE の属性行と BNH160I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明のみに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では NPDA.ERR_RATE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は区切読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.MACRF {#c32-i4211}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.MACRFは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.200) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.200)

??? question "確認問題（1問）"
    **問題.** 範囲読解の管理リファレンスでネットビューの運用確認を行います。NPDA.MACRF の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で範囲読解の管理リファレンスを確認した扱いにする。
    - B. BNH160I の有無を確認せず範囲読解の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて範囲読解の根拠を固定する。 ✅
    - D. NPDA.MACRF の属性行を読まず範囲読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では NPDA.MACRF は「IBM Z NetViewで NPDA.MACRF の扱いを記録する範囲読解項目」と NPDA または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では NPDA.MACRF の表示結果と BNH160I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明のみに寄り、判定名は範囲読解不足です。範囲読解資料では NPDA.MACRF の使い方を出典欄から追跡し、資料名は範囲読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.MDSIND {#c32-i4212}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.MDSINDは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.200) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.200)

??? question "確認問題（1問）"
    **問題.** 優先読解の管理リファレンスに関する NPDA.MDSIND の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. NPDA の結果を残さず優先読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを優先読解の管理リファレンスの証跡として保存して根拠にする。
    - C. NPDA.MDSIND の変更点を出力本文から切り離して優先読解の管理リファレンスの承認欄のみ残す。
    - D. BNH160I を含む表示を保存し、説明欄との差分を優先読解で確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では NPDA.MDSIND は「NPDA.MDSIND の状態と出力メッセージを結び付ける優先読解項目」と NPDA または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では NPDA.MDSIND の出力行と BNH160I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明のみに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では NPDA.MDSIND を IBM Z NetViewの確認記録に残し、対象名は優先読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.PDDNM {#c32-i4213}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.PDDNMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.201) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.201)

??? question "確認問題（1問）"
    **問題.** 記録読解の管理リファレンスに関係する NPDA.PDDNM の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. NPDA の結果から対象行を抜き出し、記録読解の証跡として残す。 ✅
    - B. NPDA.PDDNM の名称と担当者名のみを残して記録読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で記録読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず記録読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では NPDA.PDDNM は「NPDA.PDDNM の用途をネットビューの表示で確認する記録読解項目」と NPDA または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景では IBM Z NetViewの NPDA.PDDNM と BNH160I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明のみに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では NPDA.PDDNM を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は記録読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.PDFILTER {#c32-i4214}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.PDFILTERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.201) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.201)

??? question "確認問題（1問）"
    **問題.** 比較読解の管理リファレンスで NPDA.PDFILTER の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NPDA.PDFILTER の出力を取らず比較読解の管理リファレンスの説明文と承認印のみを残す。
    - B. 出典欄の説明と運用出力を照合し、比較読解の確認記録にまとめる。 ✅
    - C. NPDA を省略して比較読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を比較読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では NPDA.PDFILTER は「比較読解の管理リファレンスに関係する定義値と表示行を照合する比較読解項目」と NPDA または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では NPDA.PDFILTER の属性行と BNH160I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明のみに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では NPDA.PDFILTER を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は比較読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.PRELOAD_BER {#c32-i4215}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.PRELOAD_BERは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.202) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.202)

??? question "確認問題（1問）"
    **問題.** 順序読解の管理リファレンスでネットビューの運用確認を行います。NPDA.PRELOAD_BER の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で順序読解の管理リファレンスを確認した扱いにする。
    - B. BNH160I の有無を確認せず順序読解の管理リファレンスを正常終了として記録する。
    - C. 属性行、戻り表示、メッセージ見出しを合わせて順序読解の根拠にする。 ✅
    - D. NPDA.PRELOAD_BER の属性行を読まず順序読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では NPDA.PRELOAD_BER は「IBM Z NetViewで NPDA.PRELOAD_BER の扱いを記録する順序読解項目」と NPDA または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では NPDA.PRELOAD_BER の表示結果と BNH160I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明のみに寄り、判定名は順序読解不足です。順序読解資料では NPDA.PRELOAD_BER の使い方を出典欄から追跡し、資料名は順序読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.R (Ratio) {#c32-i4216}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.R (Ratio)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.203) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.203)

??? question "確認問題（1問）"
    **問題.** 値域読解の管理リファレンスに関する NPDA.R (Ratio)の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. NPDA の結果を残さず値域読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを値域読解の管理リファレンスの証跡として保存して根拠にする。
    - C. NPDA.R (Ratio)の変更点を出力本文から切り離して値域読解の管理リファレンスの承認欄のみ残す。
    - D. 同じ画面で対象行と BNH160I を読み、値域読解の結果として保存する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では NPDA.R (Ratio) は「NPDA.R (Ratio)の状態と出力メッセージを結び付ける値域読解項目」と NPDA または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では NPDA.R (Ratio)の出力行と BNH160I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明のみに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では NPDA.R (Ratio)を IBM Z NetViewの確認記録に残し、対象名は値域読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.RATE {#c32-i4217}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.RATEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.204) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.204)

??? question "確認問題（1問）"
    **問題.** 警告読解の管理リファレンスに関係する NPDA.RATE の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. NPDA で得た表示本文を使い、警告読解の採否を説明欄に結び付ける。 ✅
    - B. NPDA.RATE の名称と担当者名のみを残して警告読解の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で警告読解の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず警告読解の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では NPDA.RATE は「NPDA.RATE の用途をネットビューの表示で確認する警告読解項目」と NPDA または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景では IBM Z NetViewの NPDA.RATE と BNH160I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明のみに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では NPDA.RATE を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は警告読解用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.REPORTS {#c32-i4218}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.REPORTSは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.205) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.205)

??? question "確認問題（1問）"
    **問題.** 復旧読解の管理リファレンスで NPDA.REPORTS の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NPDA.REPORTS の出力を取らず復旧読解の管理リファレンスの説明文と承認印のみを残す。
    - B. 資料上の説明と画面上の表示行を突き合わせ、復旧読解として引き継ぐ。 ✅
    - C. NPDA を省略して復旧読解の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を復旧読解の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では NPDA.REPORTS は「復旧読解の管理リファレンスに関係する定義値と表示行を照合する復旧読解項目」と NPDA または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では NPDA.REPORTS の属性行と BNH160I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明のみに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では NPDA.REPORTS を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は復旧読解初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.SDDNM {#c32-i4219}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.SDDNMは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.206) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.206)

??? question "確認問題（1問）"
    **問題.** 監査読解の管理リファレンスでネットビューの運用確認を行います。NPDA.SDDNM の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で監査読解の管理リファレンスを確認した扱いにする。
    - B. BNH160I の有無を確認せず監査読解の管理リファレンスを正常終了として記録する。
    - C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査読解の確認にする。 ✅
    - D. NPDA.SDDNM の属性行を読まず監査読解の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では NPDA.SDDNM は「IBM Z NetViewで NPDA.SDDNM の扱いを記録する監査読解項目」と NPDA または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では NPDA.SDDNM の表示結果と BNH160I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明のみに寄り、判定名は監査読解不足です。監査読解資料では NPDA.SDDNM の使い方を出典欄から追跡し、資料名は監査読解資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.TECROUTE {#c32-i4220}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.TECROUTEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.206) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.206)

??? question "確認問題（1問）"
    **問題.** 変更読解の管理リファレンスに関する NPDA.TECROUTE の引き継ぎです。後続担当者へ残すべき確認はどれですか。

    - A. NPDA の結果を残さず変更読解の管理リファレンスの担当者名と日時のみを記録する。
    - B. 別製品のメッセージを変更読解の管理リファレンスの証跡として保存して根拠にする。
    - C. NPDA.TECROUTE の変更点を出力本文から切り離して変更読解の管理リファレンスの承認欄のみ残す。
    - D. IBM Z NetViewの表示形式に沿って根拠行を採り、変更読解の点検結果を残す。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では NPDA.TECROUTE は「NPDA.TECROUTE の状態と出力メッセージを結び付ける変更読解項目」と NPDA または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では NPDA.TECROUTE の出力行と BNH160I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明のみに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では NPDA.TECROUTE を IBM Z NetViewの確認記録に残し、対象名は変更読解対象です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NPDA.W (Wrap) {#c32-i4221}
*分類: 管理リファレンス*  ・  難易度: 中級

NPDA.W (Wrap)は、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.207) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.207)

??? question "確認問題（1問）"
    **問題.** 構文検分の管理リファレンスに関係する NPDA.W (Wrap)の設問です。一次資料に沿って採るべき確認はどれですか。

    - A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文検分で再確認できる形にする。 ✅
    - B. NPDA.W (Wrap)の名称と担当者名のみを残して構文検分の管理リファレンスの表示本文を確認対象に含めない。
    - C. ネットビュー以外の画面で構文検分の管理リファレンスを確認し同じ証跡として扱ったことにする。
    - D. BNH160I の有無を見ず構文検分の管理リファレンスの戻り値と時刻を主な根拠にして完了にする。

    正解: **A** ／ 難易度: 中級

    **解説:** 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では NPDA.W (Wrap) は「NPDA.W (Wrap)の用途をネットビューの表示で確認する構文検分項目」と NPDA または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景では IBM Z NetViewの NPDA.W (Wrap)と BNH160I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明のみに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では NPDA.W (Wrap)を Tivoli NetView z/OS 自動化で扱う確認対象とし、用語名は構文検分用語です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NQNSUP.USE {#c32-i4222}
*分類: 管理リファレンス*  ・  難易度: 中級

NQNSUP.USEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.210) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.210)

??? question "確認問題（1問）"
    **問題.** 展開検分の管理リファレンスで NQNSUP.USE の点検記録を作ります。証跡として扱える確認はどれですか。

    - A. NQNSUP.USE の出力を取らず展開検分の管理リファレンスの説明文と承認印のみを残す。
    - B. 机上確認でも実出力の見出しに合わせ、展開検分の確認値として扱う。 ✅
    - C. BROWSE CANZLOG を省略して展開検分の管理リファレンスの記録番号と時刻のみを残す。
    - D. 隣接項目の結果を展開検分の管理リファレンスへ転記して同じ結果として扱う。

    正解: **B** ／ 難易度: 中級

    **解説:** 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では NQNSUP.USE は「展開検分の管理リファレンスに関係する定義値と表示行を照合する展開検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では NQNSUP.USE の属性行と DSI633I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明のみに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では NQNSUP.USE を Tivoli NetView z/OS 自動化の運用手順で確認し、初出名は展開検分初出です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide



### NRM.CMODE {#c32-i4223}
*分類: 管理リファレンス*  ・  難易度: 中級

NRM.CMODEは、Tivoli NetView z/OS 自動化の管理リファレンスで自動化処理や復旧動作を確認する項目です。起動条件、停止条件、失敗時の代替動作を分けて確認します。IBM Z NetView 6.4 Administration Reference (p.210) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます

**出典:** IBM Z NetView 6.4 Administration Reference (p.210)

??? question "確認問題（1問）"
    **問題.** 呼出検分の管理リファレンスでネットビューの運用確認を行います。NRM.CMODE の根拠にできる作業はどれですか。

    - A. IBM Z NetViewと無関係な一覧で呼出検分の管理リファレンスを確認した扱いにする。
    - B. DSI633I の有無を確認せず呼出検分の管理リファレンスを正常終了として記録する。
    - C. 参照資料名、表示行、メッセージをそろえて呼出検分の根拠を固定する。 ✅
    - D. NRM.CMODE の属性行を読まず呼出検分の管理リファレンスの画面名と利用者名のみを保存する。

    正解: **C** ／ 難易度: 中級

    **解説:** 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では NRM.CMODE は「IBM Z NetViewで NRM.CMODE の扱いを記録する呼出検分項目」と BROWSE CANZLOG または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では NRM.CMODE の表示結果と DSI633I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明のみに寄り、判定名は呼出検分不足です。呼出検分資料では NRM.CMODE の使い方を出典欄から追跡し、資料名は呼出検分資料です。

    **出典:** NetView_6.4_Command_Reference_Vol1_A-N / NetView_6.4_Command_Reference_Vol2_O-Z / NetView_6.4_Automation_Guide


