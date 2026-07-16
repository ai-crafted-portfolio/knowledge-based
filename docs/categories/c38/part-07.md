---
search:
  exclude: true
---

# z/OS System Programming — 詳細 (7/7)

[← z/OS System Programming の概要へ戻る](index.md)


## z/OS System Programming > トレース診断

### トレース診断 システムトレース ログとの照合 TRC07 {#c38-i0289}
*分類: トレース診断*  ・  難易度: 上級

ログとの照合では トレース診断 の トレース状態 を主操作として TRC07 を判定します。時刻と対象識別子への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC07 に残します。ログとの照合を補助する バッファ指定 では IEE839I を補助値として TRC07 へ保存します。主判定のログとの照合ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC07 へ残します。証跡照合のログとの照合ではトレース診断・システムトレースの IEE843I と IEE839I を TRC07 に保存します。記録対応のログとの照合ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC07 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** ログとの照合で トレース診断 の トレース状態 と バッファ指定 を使い 操作とログを対応 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読み対象 TRC07 を切り分ける確認方法はどれですか。

    - A. IEE843Iを含むトレース状態の応答行を保存する。その応答を得るためD TRACEを使用する。対象TRC07のTRACE STATUSとBUFFERとして記録する。 ✅
    - B. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。SYSTEMをIEE843Iと同じ判定値とみなし対象TRC07の主証跡にする。システムトレースの時刻と対象識別子は確認済みとして扱う。さらにIP SYSTRACEのSYSTEMをIEE843Iと同種の値として併記する。
    - C. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。
    - D. システムトレースの停止または再定義を実施する。その後にD TRACEでIEE843Iを採取する。

    正解: **A** ／ 難易度: 上級

    **解説:** 適切な判定: Aはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として操作とログを対応しTRC07に残します。
    機能の仕組み: ログとの照合ではバッファ指定を補助操作としシステムトレースの時刻と対象識別子をIEE839Iと対象TRC07で照合します。
    各候補の評価: トレース状態とバッファ指定の役割を分けるとA: IEE843Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではTRACE STATUSとBUFFERを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではTRACE STATUSとBUFFERを証明できない点でTRACE STATUSとBUFFERを確認できません、D: 変更前のTRACE STATUSとBUFFERを失う点でバッファ指定の範囲を越えます。結論としてログとの照合のトレース診断・システムトレースで判定する対象は TRC07 です。
    用語の定義: ログとの照合で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC07へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース ログとの照合 TRC07**

    - 検証目的: トレース診断のシステムトレースについて操作とログを対応し、TRC07のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC07のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC07のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC07のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0007 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 代替経路の確認 TRC10 {#c38-i0290}
*分類: トレース診断*  ・  難易度: 上級

代替経路の確認では トレース診断 の トレース状態 を主操作として TRC10 を判定します。主経路との役割差への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC10 に残します。代替経路の確認を補助する バッファ指定 では IEE839I を補助値として TRC10 へ保存します。主判定の代替経路の確認ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC10 へ残します。証跡照合の代替経路の確認ではトレース診断・システムトレースの IEE843I と IEE839I を TRC10 に保存します。記録対応の代替経路の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC10 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 代替経路の確認で トレース診断 の トレース状態 と バッファ指定 を照合し 主経路との役割差 を確かめます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読む前に対象 TRC10 へ行う確認はどれですか。

    - A. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。
    - B. システムトレースの停止または再定義を実施する。その後にD TRACEでIEE843Iを採取する。
    - C. APF管理のDSNAMEとVOLSERを確認する。その値をトレース診断のTRC10にも適用する。
    - D. D TRACEとTRACE ST,2Mの対象名をそろえる。前者のIEE843IをTRACE STATUSとBUFFERの判定値として採用する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正しい判定結果: Dはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として代替手段の成立を確認しTRC10に残します。
    運用上の背景: 代替経路の確認ではバッファ指定を補助操作としシステムトレースの主経路との役割差をIEE839Iと対象TRC10で照合します。
    候補別の検討: トレース状態とバッファ指定の役割を分けるとA: 入力記録だけではTRACE STATUSとBUFFERを証明できない点で一次資料と一致しません、B: 変更前のTRACE STATUSとBUFFERを失う点でTRACE STATUSとBUFFERを確認できません、C: APF管理の値ではIEE843Iを確認できない点でバッファ指定の範囲を越えます、D: 同じ対象名のIEE843Iを採用する点で現在値を示します。結論として代替経路の確認のトレース診断・システムトレースで判定する対象は TRC10 です。
    重要用語の定義: 代替経路の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC10へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 代替経路の確認 TRC10**

    - 検証目的: トレース診断のシステムトレースについて代替手段の成立を確認し、TRC10のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC10のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC10のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC10のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0010 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 変更前の確認 TRC02 {#c38-i0291}
*分類: トレース診断*  ・  難易度: 上級

変更前の確認では トレース診断 の バッファ指定 を主操作として TRC02 を判定します。変更対象と非対象の境界への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC02 に残します。変更前の確認を補助する IPCS表示 では SYSTEM を補助値として TRC02 へ保存します。主判定の変更前の確認ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC02 へ残します。証跡照合の変更前の確認ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC02 に保存します。記録対応の変更前の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC02 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更前の確認で トレース診断 の バッファ指定 と IPCS表示 を実施し システムトレース の役割を確認します。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC02 の証跡を取る方法はどれですか。

    - A. TRACE ST,2Mを対象名なしで実行する。一覧の先頭行をTRC02の結果として記録する。
    - B. 前回保存したTRACE ST,2Mの結果を使う。今回のIP SYSTRACEの結果と同一時点の証跡として比較する。
    - C. 保存済みのTRC02の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。
    - D. 対象TRC02についてTRACE ST,2Mの応答からIEE839Iを確認する。IP SYSTRACEは補助証跡として時刻をそろえて保存する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 採用理由: Dはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として変更前の証跡を保存しTRC02に残します。
    動作の背景: 変更前の確認ではIPCS表示を補助操作としシステムトレースの変更対象と非対象の境界をSYSTEMと対象TRC02で照合します。
    各選択肢の検討: バッファ指定とIPCS表示の役割を分けるとA: 先頭行はTRC02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でバッファ指定を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でトレース診断に使いません、D: IEE839Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のトレース診断・システムトレースで判定する対象は TRC02 です。
    初出用語の定義: 変更前の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC02へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 変更前の確認 TRC02**

    - 検証目的: トレース診断のシステムトレースについて変更前の証跡を保存し、TRC02のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC02のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC02のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0002 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC02のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
    ② ステップ2 の SYSTEM が画面・出力に表示されること
    ③ ステップ3 の IEE843I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 変更後の確認 TRC03 {#c38-i0292}
*分類: トレース診断*  ・  難易度: 上級

変更後の確認では トレース診断 の IPCS表示 を主操作として TRC03 を判定します。反映値と残存値への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC03 に残します。変更後の確認を補助する トレース状態 では IEE843I を補助値として TRC03 へ保存します。主判定の変更後の確認ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC03 へ残します。証跡照合の変更後の確認ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC03 に保存します。記録対応の変更後の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC03 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 変更後の確認で トレース診断 の IPCS表示 と トレース状態 を用い 変更結果を検証 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。SYSTEM で対象 TRC03 の TRACE STATUSとBUFFER を再現できる記録はどれですか。

    - A. D TRACEで周辺状態を押さえる。その後にIP SYSTRACEでSYSTEMを確認して変更結果を検証する。 ✅
    - B. システムトレースの停止または再定義を実施する。その後にIP SYSTRACEでSYSTEMを採取する。
    - C. SAF連携のSAF RCとRACF RCを確認する。その値をトレース診断のTRC03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。
    - D. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。

    正解: **A** ／ 難易度: 上級

    **解説:** 正答の根拠: AはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として変更結果を検証しTRC03に残します。
    内部の仕組み: 変更後の確認ではトレース状態を補助操作としシステムトレースの反映値と残存値をIEE843Iと対象TRC03で照合します。
    誤答を含む比較: IPCS表示とトレース状態の役割を分けるとA: 周辺状態の後にSYSTEMを確認する点でTRC03を判定できます、B: 変更前のTRACE STATUSとBUFFERを失う点でトレース状態の範囲を越えます、C: SAF連携の値ではSYSTEMを確認できないうえに追加前提も不正な点でTRC03の値を示しません、D: 補助操作の成功ではSYSTEMを確定できない点で変更後の確認に合いません。結論として変更後の確認のトレース診断・システムトレースで判定する対象は TRC03 です。
    用語定義: 変更後の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC03へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 変更後の確認 TRC03**

    - 検証目的: トレース診断のシステムトレースについて変更結果を検証し、TRC03のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC03のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0003 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC03のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC03のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
    ② ステップ2 の IEE843I が画面・出力に表示されること
    ③ ステップ3 の IEE839I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 引継ぎ記録 TRC09 {#c38-i0293}
*分類: トレース診断*  ・  難易度: 上級

引継ぎ記録では トレース診断 の IPCS表示 を主操作として TRC09 を判定します。次担当者が追跡できる証跡への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC09 に残します。引継ぎ記録を補助する トレース状態 では IEE843I を補助値として TRC09 へ保存します。主判定の引継ぎ記録ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC09 へ残します。証跡照合の引継ぎ記録ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC09 に保存します。記録対応の引継ぎ記録ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC09 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 引継ぎ記録で トレース診断 の IPCS表示 と トレース状態 を用い 再現可能な記録を作成 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。SYSTEM で対象 TRC09 の TRACE STATUSとBUFFER を再現できる記録はどれですか。

    - A. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。
    - B. IP SYSTRACEを対象名なしで実行する。一覧の先頭行をTRC09の結果として記録する。
    - C. 対象名TRC09を指定してIP SYSTRACEを実行する。応答中のSYSTEMと時刻を保存する。D TRACEで周辺状態を補完する。 ✅
    - D. 前回保存したIP SYSTRACEの結果を使う。今回のD TRACEの結果と同一時点の証跡として比較する。

    正解: **C** ／ 難易度: 上級

    **解説:** 採用操作の理由: CはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として再現可能な記録を作成しTRC09に残します。
    製品内の仕組み: 引継ぎ記録ではトレース状態を補助操作としシステムトレースの次担当者が追跡できる証跡をIEE843Iと対象TRC09で照合します。
    選択肢別の説明: IPCS表示とトレース状態の役割を分けるとA: 補助操作の成功ではSYSTEMを確定できない点でTRC09の値を示しません、B: 先頭行はTRC09と確定できない点で引継ぎ記録に合いません、C: SYSTEMと時刻を保存する点でIPCS表示に合います、D: 採取時刻が異なる点でトレース診断に使いません。結論として引継ぎ記録のトレース診断・システムトレースで判定する対象は TRC09 です。
    用語を初めて使う際の定義: 引継ぎ記録で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC09へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 引継ぎ記録 TRC09**

    - 検証目的: トレース診断のシステムトレースについて再現可能な記録を作成し、TRC09のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC09のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0009 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC09のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC09のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
    ② ステップ2 の IEE843I が画面・出力に表示されること
    ③ ステップ3 の IEE839I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 復旧後の確認 TRC06 {#c38-i0294}
*分類: トレース診断*  ・  難易度: 上級

復旧後の確認では トレース診断 の IPCS表示 を主操作として TRC06 を判定します。再発していないことを示す値への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC06 に残します。復旧後の確認を補助する トレース状態 では IEE843I を補助値として TRC06 へ保存します。主判定の復旧後の確認ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC06 へ残します。証跡照合の復旧後の確認ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC06 に保存します。記録対応の復旧後の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC06 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧後の確認で トレース診断 の IPCS表示 と トレース状態 の役割を分け 再発していないことを示す値 を調べます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC06 を誤判定しない進め方はどれですか。

    - A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をトレース診断のTRC06にも適用する。
    - B. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象TRC06へ引き継げるものとする。システムトレースの再発していないことを示す値は確認済みとして扱う。さらにTRACE ST,2MのIEE839IをSYSTEMと同種の値として併記する。
    - C. IP SYSTRACEを対象名なしで実行する。一覧の先頭行をTRC06の結果として記録する。
    - D. IP SYSTRACEでSYSTEMを取得してからTRACE ST,2MでIEE839Iを照合する。TRC06のTRACE STATUSとBUFFERを両出力から確定する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 正答内容: DはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として復旧後の安定性を確認しTRC06に残します。
    構成上の背景: 復旧後の確認ではトレース状態を補助操作としシステムトレースの再発していないことを示す値をIEE843Iと対象TRC06で照合します。
    候補ごとの理由: IPCS表示とトレース状態の役割を分けるとA: Cross Memoryの値ではSYSTEMを確認できない点でトレース状態の範囲を越えます、B: 補助操作の成功ではSYSTEMを確定できないうえに追加前提も不正な点でTRC06の値を示しません、C: 先頭行はTRC06と確定できない点で復旧後の確認に合いません、D: SYSTEMとIEE839Iを順に照合する点でIPCS表示に合います。結論として復旧後の確認のトレース診断・システムトレースで判定する対象は TRC06 です。
    初出用語: 復旧後の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC06へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 復旧後の確認 TRC06**

    - 検証目的: トレース診断のシステムトレースについて復旧後の安定性を確認し、TRC06のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC06のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0006 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC06のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC06のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
    ② ステップ2 の IEE843I が画面・出力に表示されること
    ③ ステップ3 の IEE839I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 復旧準備 TRC05 {#c38-i0295}
*分類: トレース診断*  ・  難易度: 上級

復旧準備では トレース診断 の バッファ指定 を主操作として TRC05 を判定します。再開前に必要な整合性への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC05 に残します。復旧準備を補助する IPCS表示 では SYSTEM を補助値として TRC05 へ保存します。主判定の復旧準備ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC05 へ残します。証跡照合の復旧準備ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC05 に保存します。記録対応の復旧準備ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC05 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 復旧準備で トレース診断 の バッファ指定 と IPCS表示 を組み合わせる際は システムトレース が割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能という仕組みを前提にします。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE839I と TRACE STATUSとBUFFER を対象 TRC05 で確認する組合せはどれですか。

    - A. 前回保存したTRACE ST,2Mの結果を使う。今回のIP SYSTRACEの結果と同一時点の証跡として比較する。
    - B. 保存済みのTRC05の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。
    - C. 変更を加えずTRACE ST,2Mを実行する。IEE839Iを保存する。差分はIP SYSTRACEの結果と対象名で対応させる。 ✅
    - D. IP SYSTRACEのSYSTEMをTRACE STATUSとBUFFERの主判定に採用する。TRACE ST,2Mの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。

    正解: **C** ／ 難易度: 上級

    **解説:** 選定理由: Cはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として復旧条件を確認しTRC05に残します。
    処理の仕組み: 復旧準備ではIPCS表示を補助操作としシステムトレースの再開前に必要な整合性をSYSTEMと対象TRC05で照合します。
    選択結果の内訳: バッファ指定とIPCS表示の役割を分けるとA: 採取時刻が異なる点でバッファ指定を代替しません、B: 過去出力では今回の復旧準備を示せない点でトレース診断に使いません、C: 変更前のIEE839Iを保存する点で正答です、D: SYSTEMはIEE839Iを代替しないうえに追加前提も不正な点でTRC05を採用できません。結論として復旧準備のトレース診断・システムトレースで判定する対象は TRC05 です。
    用語の説明: 復旧準備で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC05へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 復旧準備 TRC05**

    - 検証目的: トレース診断のシステムトレースについて復旧条件を確認し、TRC05のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC05のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC05のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0005 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC05のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
    ② ステップ2 の SYSTEM が画面・出力に表示されること
    ③ ステップ3 の IEE843I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 構成監査 TRC08 {#c38-i0296}
*分類: トレース診断*  ・  難易度: 上級

構成監査では トレース診断 の バッファ指定 を主操作として TRC08 を判定します。定義値と稼働値の一致への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC08 に残します。構成監査を補助する IPCS表示 では SYSTEM を補助値として TRC08 へ保存します。主判定の構成監査ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC08 へ残します。証跡照合の構成監査ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC08 に保存します。記録対応の構成監査ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC08 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 構成監査で トレース診断 の バッファ指定 と IPCS表示 を実施し システムトレース の役割を確認します。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC08 の証跡を取る方法はどれですか。

    - A. 保存済みのTRC08の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。
    - B. IP SYSTRACEの結果だけでは確定しない。TRACE ST,2MのIEE839Iを主証跡として構成差分を監査する。 ✅
    - C. IP SYSTRACEのSYSTEMをTRACE STATUSとBUFFERの主判定に採用する。TRACE ST,2Mの応答は採取対象から外す。
    - D. D TRACEのIEE843IをIEE839Iと同義の成功表示として扱う。TRACE ST,2Mは実行しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 技術上の正答: Bはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として構成差分を監査しTRC08に残します。
    実行時の背景: 構成監査ではIPCS表示を補助操作としシステムトレースの定義値と稼働値の一致をSYSTEMと対象TRC08で照合します。
    四つの候補の理由: バッファ指定とIPCS表示の役割を分けるとA: 過去出力では今回の構成監査を示せない点でトレース診断に使いません、B: IEE839Iを主証跡として区別する点で正答です、C: SYSTEMはIEE839Iを代替しない点でTRC08を採用できません、D: IEE843IとIEE839Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のトレース診断・システムトレースで判定する対象は TRC08 です。
    初出語定義: 構成監査で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC08へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 構成監査 TRC08**

    - 検証目的: トレース診断のシステムトレースについて構成差分を監査し、TRC08のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC08のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC08のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0008 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC08のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
    ② ステップ2 の SYSTEM が画面・出力に表示されること
    ③ ステップ3 の IEE843I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 通常状態の確認 TRC01 {#c38-i0297}
*分類: トレース診断*  ・  難易度: 上級

通常状態の確認では トレース診断 の トレース状態 を主操作として TRC01 を判定します。基準値と現在値の差への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC01 に残します。通常状態の確認を補助する バッファ指定 では IEE839I を補助値として TRC01 へ保存します。主判定の通常状態の確認ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC01 へ残します。証跡照合の通常状態の確認ではトレース診断・システムトレースの IEE843I と IEE839I を TRC01 に保存します。記録対応の通常状態の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC01 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 通常状態の確認で トレース診断 の トレース状態 と バッファ指定 を使い 通常状態を確定 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読み対象 TRC01 を切り分ける確認方法はどれですか。

    - A. TRACE ST,2MのIEE839IをTRACE STATUSとBUFFERの主判定に採用する。D TRACEの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。
    - B. IP SYSTRACEのSYSTEMをIEE843Iと同義の成功表示として扱う。D TRACEは実行しない。
    - C. D TRACEを先に実行する。対象TRC01のIEE843IをTRACE STATUSとBUFFERとして記録する。続いてTRACE ST,2Mで同一対象を照合する。 ✅
    - D. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。

    正解: **C** ／ 難易度: 上級

    **解説:** 正解の説明: Cはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として通常状態を確定しTRC01に残します。
    背景・仕組み: 通常状態の確認ではバッファ指定を補助操作としシステムトレースの基準値と現在値の差をIEE839Iと対象TRC01で照合します。
    選択肢の理由: トレース状態とバッファ指定の役割を分けるとA: IEE839IはIEE843Iを代替しないうえに追加前提も不正な点でシステムトレースに使えません、B: SYSTEMとIEE843Iは確認項目が異なる点でTRC01を採用できません、C: IEE843Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではTRACE STATUSとBUFFERを判定できない点で一次資料と一致しません。結論として通常状態の確認のトレース診断・システムトレースで判定する対象は TRC01 です。
    用語の初出定義: 通常状態の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC01へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 通常状態の確認 TRC01**

    - 検証目的: トレース診断のシステムトレースについて通常状態を確定し、TRC01のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC01のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC01のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC01のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0001 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### トレース診断 システムトレース 障害切り分け TRC04 {#c38-i0298}
*分類: トレース診断*  ・  難易度: 上級

障害切り分けでは トレース診断 の トレース状態 を主操作として TRC04 を判定します。最初に失敗した処理への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC04 に残します。障害切り分けを補助する バッファ指定 では IEE839I を補助値として TRC04 へ保存します。主判定の障害切り分けではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC04 へ残します。証跡照合の障害切り分けではトレース診断・システムトレースの IEE843I と IEE839I を TRC04 に保存します。記録対応の障害切り分けではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC04 を結びます。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12

??? question "確認問題（1問）"
    **問題.** 障害切り分けで トレース診断 の トレース状態 と バッファ指定 を照合し 最初に失敗した処理 を確かめます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読む前に対象 TRC04 へ行う確認はどれですか。

    - A. IP SYSTRACEのSYSTEMをIEE843Iと同義の成功表示として扱う。D TRACEは実行しない。補助出力があれば主出力の未採取を補えるものとする。
    - B. D TRACEの出力でTRC04とIEE843Iが同じ応答にあることを確認する。TRACE STATUSとBUFFERをその応答から採取する。 ✅
    - C. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。
    - D. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。

    正解: **B** ／ 難易度: 上級

    **解説:** 正しい操作の説明: Bはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として障害範囲を限定しTRC04に残します。
    技術的背景: 障害切り分けではバッファ指定を補助操作としシステムトレースの最初に失敗した処理をIEE839Iと対象TRC04で照合します。
    四択の評価: トレース状態とバッファ指定の役割を分けるとA: SYSTEMとIEE843Iは確認項目が異なるうえに追加前提も不正な点でTRC04を採用できません、B: TRC04とIEE843Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではTRACE STATUSとBUFFERを判定できない点で一次資料と一致しません、D: 入力記録だけではTRACE STATUSとBUFFERを証明できない点でTRACE STATUSとBUFFERを確認できません。結論として障害切り分けのトレース診断・システムトレースで判定する対象は TRC04 です。
    初出語の意味: 障害切り分けで使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC04へ適用します。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12


??? note "検証手順（1件）"
    **トレース診断 システムトレース 障害切り分け TRC04**

    - 検証目的: トレース診断のシステムトレースについて障害範囲を限定し、TRC04のTRACE STATUSとBUFFERを実出力で確認する。
    - 前提条件: z/OS System Programmingの参照権限を持ち、対象TRC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC04のトレース状態を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> D TRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE843I 19.36.21 TRACE DISPLAY 490
    SYSTEM STATUS INFORMATION
    ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
    ```

    画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC04のバッファ指定を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> TRACE ST,2M
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
    ```

    画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC04のIPCS表示を表示します。
    操作（入力）:
    ```text
    z/OS System Programming 操作画面
    COMMAND ===> IP SYSTRACE
    → Enter を押す
    ```

    画面・出力:
    ```text
    SYSTEM TRACE TABLE CPU 0000 ASID 0004 EVENT SVC
    ```

    画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
    ② ステップ2 の IEE839I が画面・出力に表示されること
    ③ ステップ3 の SYSTEM が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12



### 共通サービス域 ログ確認 運用確認084 {#c38-i0299}
*分類: トレース診断*  ・  難易度: 上級

第八十四観点 z/OS System Programming の トレース診断 では 共通サービス域 を障害調査で照合します（第八十四観点）。第八十四観点 資料上は CSAなど複数アドレス空間から参照される共通ストレージ領域として扱います（第八十四観点）。第八十四観点 ISGLOCK を起点に表示値を戻し、共通ストレージ変更の記録を点検します（第八十四観点）。第八十四観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録084へ書きます（第八十四観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第八十四証跡です。z/OS System Programming の トレース診断 で切分けを行います。確認観点は 共通サービス域、ログ確認、運用確認 です。共通ストレージ変更の記録を満たす記録方法として、表示値と定義を結ぶものはどれか。

    - A. SVC処理 の一般メモを採り、ISGLOCK、メッセージID、時刻の対応を記録外に置き、zOSSP誤記084として調査範囲を狭める。
    - B. 共通サービス域 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延084として扱う。
    - C. SWITCH SMF後のSMF切替記録 と ISGLOCK を同一票へ記録し、共通サービス域 を zOSSP正084で確定する。 ✅
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在084として残す。

    正解: **C** ／ 難易度: 上級

    **解説:** 第八十四観点 照合結果: Cは ISGLOCK をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十四観点）。第八十四観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第八十四観点）。第八十四観点 誤答確認: Aは ISGLOCK 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第八十四観点）。第八十四観点 初出定義: PSWは実行状態を示す語です（第八十四観点）。第八十四観点 SVCは監視プログラム呼出しです（第八十四観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **共通サービス域 ログ確認 運用確認084**

    - 検証目的: 共通サービス域 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / SMF

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により 共通サービス域 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D SMF,O
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE974I 11.01.12 SMF DATA SET STATUS
    NAME       VOLSER  STATUS
    SMF.MAN1   SMS001  ACTIVE
    SMF.MAN2   SMS002  EMPTY
    ```

    画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により 共通サービス域 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SWITCH SMF
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
    IEE360I SMF NOW RECORDING ON SMF.MAN2
    ```

    画面・出力には IEE360I が含まれる。IEE360I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により 共通サービス域 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    JES2 SDSF ST
    COMMAND ===> S IFASMFD12
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEF403I IFASMFD12 - STARTED
    IFASMFDP SYSPRINT
    INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
    ```

    画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110



### 私用域 ログ確認 運用確認034 {#c38-i0300}
*分類: トレース診断*  ・  難易度: 中級

第三十四観点 私用域 は z/OS System Programming の トレース診断 で扱う管理項目です（第三十四観点）。第三十四観点 各アドレス空間内で利用者プログラムが使う独立した仮想記憶領域という説明を操作結果と照合します（第三十四観点）。第三十四観点 SRB=00AF1100、SWITCH SMF後のSMF切替記録、定義メンバーを照合し、共通ストレージ変更の記録を確認します（第三十四観点）。第三十四観点 証跡には資料IDと確認値を併記し、zOSSP記録034として保存します（第三十四観点）。

**出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110

??? question "確認問題（1問）"
    **問題.** 運用第三十四証跡です。z/OS System Programming の トレース診断 で切分けを行います。確認観点は 私用域、ログ確認、運用確認 です。共通ストレージ変更の記録のために、SWITCH SMF後のSMF切替記録 を使った運用記録として最も適切な扱いはどれか。

    - A. SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を同一票へ記録し、私用域 を zOSSP正034で確定する。 ✅
    - B. APF管理 の一般メモを採り、SRB=00AF1100、メッセージID、時刻の対応を記録外に置き、zOSSP誤記034として調査範囲を狭める。
    - C. 私用域 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延034として扱う。
    - D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在034として残す。

    正解: **A** ／ 難易度: 中級

    **解説:** 第三十四観点 正答根拠: Aは SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を結び付けるため、対象システムの取り違えを防げます（第三十四観点）。第三十四観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第三十四観点）。第三十四観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第三十四観点）。第三十四観点 用語説明: WTOは通知メッセージです（第三十四観点）。第三十四観点 WTORは応答を求めるメッセージです（第三十四観点）。

    **出典:** ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


??? note "検証手順（1件）"
    **私用域 ログ確認 運用確認034**

    - 検証目的: 私用域 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。
    - 前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。
    - セッション環境: MVS console / parmlib review

    **ステップ 1**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により 私用域 の値を確認し、対象の現在値を固定する。
    操作（入力）:
    ```text
    ISPF browse
    COMMAND ===> BROWSE SYS1.PARMLIB(PROGSP)
    → Enter を押す
    ```

    画面・出力:
    ```text
    APF FORMAT(DYNAMIC)
    APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
    LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
    ```

    画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 2**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により 私用域 の値を確認し、定義と資料上の項目を照合する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> SET PROG=SP
    → Enter を押す
    ```

    画面・出力:
    ```text
    IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
    IEE536I PROG VALUE SP NOW IN EFFECT
    ```

    画面・出力には IEE252I が含まれる。IEE252I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    **ステップ 3**
    現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により 私用域 の値を確認し、同じ対象として記録できることを確認する。
    操作（入力）:
    ```text
    MVS console
    COMMAND ===> D PROG,APF
    → Enter を押す
    ```

    画面・出力:
    ```text
    CSV450I 06.10.10 PROG,APF DISPLAY 833
    FORMAT=DYNAMIC
    ENTRY VOLUME DSNAME
      12  MPRES3 MYPROG.LOADLIB
    ```

    画面・出力には CSV450I が含まれる。CSV450I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。

    - 合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
    ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
    ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。
    - 検証状態: 机上
    - 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110


