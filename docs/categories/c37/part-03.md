---
search:
  exclude: true
---

# z/OS 3.1 Core Operations — 詳細 (3/3)

[← z/OS 3.1 Core Operations の概要へ戻る](index.md)


## 結合機構確認


<section class="kb-item" id="c37-i0300"><h3>結合機構確認 Coupling Facility構造 障害切り分け CF04</h3><p class="kb-meta">分類: 結合機構確認 ・ 難易度: 中級</p><p>障害切り分けでは 結合機構確認 の CF一覧 を主操作として CF04 を判定します。最初に失敗した処理への注意として「DEGRADED接続を構造全体の停止と取り違える危険があります」を CF04 に残します。障害切り分けを補助する 構造表示 では IXC360I を補助値として CF04 へ保存します。主判定の障害切り分けでは結合機構確認・構造の CF一覧 から IXL150I を読み CF04 へ残します。証跡照合の障害切り分けでは結合機構確認・構造の IXL150I と IXC360I を CF04 に保存します。記録対応の障害切り分けでは結合機構確認・構造の STRUCTUREとCONNECTION の証跡へ CF04 を結びます。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで 結合機構確認 の CF一覧 と 構造表示 の役割を分け 最初に失敗した処理 を調べます。Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みです。DEGRADED接続を構造全体の停止と取り違える危険があります。対象 CF04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D XCF,CF,CFNAME=CF01のIXC361IをIXL150Iと同義の成功表示として扱う。D CFは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D CFが応答を返した時点で正常とする。応答中のIXL150Iの値は記録しない。</li><li>C. D CFのコマンド文字列だけを記録する。IXL150Iを含む応答行は保存しない。</li><li>D. D CFの出力でCF04とIXL150Iが同じ応答にあることを確認する。STRUCTUREとCONNECTIONをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: DはCF一覧で IXL150I を読みSTRUCTUREとCONNECTIONの主値として障害範囲を限定しCF04に残します。
技術的背景: 障害切り分けでは構造表示を補助操作としCoupling Facility構造の最初に失敗した処理をIXC360Iと対象CF04で照合します。
四択の評価: CF一覧と構造表示の役割を分けるとA: IXC361IとIXL150Iは確認項目が異なるうえに追加前提も不正な点でCF04を採用できません、B: 応答の有無だけではSTRUCTUREとCONNECTIONを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではSTRUCTUREとCONNECTIONを証明できない点で一次資料と一致しません、D: CF04とIXL150Iを同じ応答で結ぶ点でCF04を判定できます。結論として障害切り分けの結合機構確認・構造で判定する対象は CF04 です。
初出語の意味: 障害切り分けで使う Coupling Facility構造 はXESがCF内のキャッシュ、リスト、ロック構造へ接続し、Sysplexデータ共有を支える仕組みを表しSTRUCTUREとCONNECTIONを判定する際にCF04へ適用します。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>結合機構確認 Coupling Facility構造 障害切り分け CF04</strong></p><p>検証目的: 結合機構確認のCoupling Facility構造について障害範囲を限定し、CF04のSTRUCTUREとCONNECTIONを実出力で確認する。</p><p>前提条件: z/OS 3.1 Core Operationsの参照権限を持ち、対象CF04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS 3.1 Core Operationsの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD CFを指定し、CF04のCF一覧を表示します。
［操作（入力）］
z/OS 3.1 Core Operations 操作画面
COMMAND ===&gt; D CF
→ Enter を押す
［画面・出力］
IXL150I CF DISPLAY CFNAME CF01 STATUS AVAILABLE
画面・出力にあるIXL150Iを読み、STRUCTUREとCONNECTIONと対象CF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,STR,STRNAME=CF04を指定し、CF04の構造表示を表示します。
［操作（入力）］
z/OS 3.1 Core Operations 操作画面
COMMAND ===&gt; D XCF,STR,STRNAME=CF04
→ Enter を押す
［画面・出力］
IXC360I STRUCTURE CF04 STATUS ALLOCATED CFNAME CF01 CONNECTIONS 2
画面・出力にあるIXC360Iを読み、STRUCTUREとCONNECTIONと対象CF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS 3.1 Core Operationsの結合機構確認を確認する入力画面です。COMMAND入力口へD XCF,CF,CFNAME=CF01を指定し、CF04のCF活動を表示します。
［操作（入力）］
z/OS 3.1 Core Operations 操作画面
COMMAND ===&gt; D XCF,CF,CFNAME=CF01
→ Enter を押す
［画面・出力］
IXC361I CF01 ACTIVE COUPLING FACILITY LEVEL 25
画面・出力にあるIXC361Iを読み、STRUCTUREとCONNECTIONと対象CF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IXL150I が画面・出力に表示されること
② ステップ2 の IXC360I が画面・出力に表示されること
③ ステップ3 の IXC361I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: OS MVS System Commands（zOS31_ieag100） / OS MVS System Management Facilities SMF（zOS31_ieag200） / zOS31_ieam600 / zOS31_ieah700 / zOS31_e0zpdz00 / zOS31_e0zh300 / zOS31_erba200 / zOS31_izua300</p></div></details></section>
