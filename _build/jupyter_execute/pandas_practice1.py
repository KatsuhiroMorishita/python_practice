#!/usr/bin/env python
# coding: utf-8

# # pandasの基本問題
# pandasはPythonで使える表形式データ処理用のライブラリです。
# 列間の演算、条件抽出、集計、異常値への対応、表同士の結合（マージ）、簡易統計、各種形式での出力、グラフ作成、などが行えます。
# Excelでは手に負えないサイズの表を、Excelよりも素早く処理できるので、数百万行程度ならかなり便利に利用できます。
# 利用するにはpandasをimportします。
# 
# 
# **記述例**  
# 
# ```python  
# import pandas as pd    # pandasを取り込み、pdという名前で使う、という命令
# 
# df = pd.DataFrame()           # 空のDataFrameを作成。型はDataFrame。
# df["A"] = [11,32,3,7,53,12]   # A列にデータを追加
# print(df[df["A"] > 20])       # A列で20より大きい値を抽出して表示
# ```
# ```text
#     A
# 1  32
# 4  53
# ```
# と表示される。
# 
# <br>
# 
# **よく使う関数（メソッド）**    
# 
# - pd.read_csv(file_name)  
#   csvファイルを読み込む。文字コードの指定が必要なことも。
# - pd.read_excel(file_name)  
#   Excelファイルを読み込む。シート名・番号を指定しないと、0番目が読まれる。
# - pd.read_html(url)   
#   Webサイトに埋め込まれた表を読み込む。DataFrame型の要素を持つlist型が返る。
# - df.head()   
#   DataFrame型の変数dfがあるとして、dfの上から5行が表示される。行が多い場合に利用。
# - df.dropna()  
#   DataFrame型の変数dfがあるとして、dfから非値nanを含む行を削除する。特定の列を指定するには引数subsetを指定する。
# 
# <br>
# 
# **よく使う書き方** 
# 
# - df["A"].values  # DataFrame型の変数dfがあるとして、そのA列を取り出してndarray型に変える

# ---
# ### 問題　Web上の表の読み込み
# 気象庁はアメダスの観測データをインターネットで閲覧できるようにしています。その表を1つ読み込んでみましょう。読み込む対象のURLを以下に示します。  
# 
# https://www.data.jma.go.jp/obd/stats/etrn/view/10min_a1.php?prec_no=86&block_no=0846&year=2021&month=10&day=01&view=p1
# 
# 気象データを格納した表を表示できればOKです。  
# ＊将来的に公開方法が変更になり、表を読み込めなくなるかもしれません。  
# 
# 【注意】  
# もしlxmlモジュールがない、というエラーが出たら、下記のコマンドを実行してインストールしてください。
# 
# ```bash
# !pip install lxml
# ```
# 
# ローカル環境で実行している場合は以下のコマンドかもしれません。実行後はカーネルをリセットしてください。
# ```bash
# !py -m pip install lxml
# ```
# 
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。
# ここでは、列名などは特に何も手を加えていない。
#     
# ```python  
# import pandas as pd   # pandasを読み込んで、pdという名前で使う宣言
# 
# # urlの指定、読み込み、表示
# url = "https://www.data.jma.go.jp/obd/stats/etrn/view/10min_a1.php?prec_no=86&block_no=0846&year=2021&month=10&day=01&view=p1"
# dfs = pd.read_html(url)    # Webページ内の全tableを読み込む
# df = dfs[0]   # 気象データの入ったDataFrameを取り出す
# print(df)     # 表の表示（jupyterやColaboratoryならセルの最期に変数名だけ書いた方が良いが、ここではprint()で表示）
# ```  
#     
# ブラウザで見れる気象データと同じものが表示されれば良い。
# 
# </div></details>

# In[ ]:





# ---
# <b>以下は問題作成用のコード</b>  
# 無視してください。

# In[1]:


import pandas as pd    # pandasを取り込み、pdという名前で使う、という命令

df = pd.DataFrame()           # 空のDataFrame
df["A"] = [11,32,3,7,53,12]   # A列にデータを追加
print(df[df["A"] > 20])       # A列で20より大きい値を抽出して表示

