#!/usr/bin/env python
# coding: utf-8

# # Numpyの基本問題
# numpyはPythonで使える計算用のライブラリです。基本的な数学の計算に必要な機能や、テンソル・行列・ベクトルの計算機能を提供しています。numpyはimportで取り込んでから使います。また、毎回プログラムの中でnumpyと書くのは面倒なのでnpと省略することが多く、省略するにはasを使います。
# 
# 
# 記述例  
# 
# ```python  
# import numpy as np    # numpyを取り込み、npという名前で使う、という命令
# 
# print(np.sin(3.14))   # 約sin(π)の値を表示する
# ```

# ---
# ### 問題　ネイピア数
# ライブラリnumpyを使ってネイピア数 $ e $ の値を表示せよ。
# 
# 
# <details><summary>■【ヒント】（Click）</summary><div>
#     
# numpyの中に、いくつか定数が定義されており、その中にネイピア数 $ e $ もある。定数の呼び出しには()は不要である。
#     
# </div></details>
# 
# 
#   
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。  
#     
# ```python  
# import numpy as np
# 
# print(np.e)   # ネイピア数を表示
# ```  
# 
# <br>
# 次の様に表示される。  
#     
#     2.718281828459045  
#     
# </div></details>

# ---
# ### 問題　円周率
# ライブラリnumpyを使って円周率$\pi$の値を表示せよ。
# 
# <details><summary>■【ヒント】（Click）</summary><div>
#     
# numpyの中に、いくつか定数が定義されており、その中に $ \pi $ もある。定数の呼び出しには()は不要である。
#     
# </div></details>
# 
# 
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
# 解答例を以下に示す。  
#     
# ```python  
# import numpy as np
# 
# print(np.pi)   # 円周率を表示
# ```  
# 
# <br>
# 次の様に表示される。
#     
#     3.141592653589793  
# 
# </div></details>
# 

# ---
# ### 問題　自然対数の計算
# 　$ \ln 2 $をライブラリnumpyを使って計算せよ。
#   
#   
# <details><summary>■【ヒント】（Click）</summary><div>
#     
# 　自然対数を数学では $ \ln $ と書く。自然対数は底がネイピア数の対数です。$ \ln x = \log_e x $ 
#     
# </div></details>
# 
#   
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
# 解答例を以下に示す。numpyの中で自然対数を計算する関数はlog。  
#     
# ```python  
# import numpy as np
# 
# print(np.log(2))   # 表示させて確認
# ```  
#     
# <br>
# 次の様に表示される。  
#     
#     0.6931471805599453
# 
# <br>
# なお、自然対数は底がネイピア数なので、np.log(np.e)で1.0と表示される。
#     
# </div></details>

# ---
# ### 問題　常用対数の計算
# 　$ \log_{10} 2 $ をライブラリnumpyを使って計算せよ。
#   
# <details><summary>■【ヒント】（Click）</summary><div>
#     
# 　常用対数は底が10の対数です。xの常用対数を求める式は　$ \log_{10} x $　です。例えば、　$ \log_{10} 100 = 2 $　となります。常用対数自体は、計測値の桁数が大きく変化する際などで対数表示する際に使います。
#     
# </div></details>
# 
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
# 解答例を以下に示す。numpyの中で常用対数を計算する関数はlog10です。
#     
# ```python  
# import numpy as np
# 
# print(np.log10(2))   # 表示させて確認
# ```  
#     
# <br>
# 次の様に表示される。   
#     
#     0.3010299956639812  
#     
# <br>
# また、常用対数は底が10なので、np.log10(100)だと2.0と表示される。
#     
# </div></details>

# ---
# ### 問題　expの計算
#   ネイピア数 $ e $ の累乗 $ e^3 $ をライブラリnumpyの関数を使って計算せよ。
#   
# <details><summary>■【ヒント】（Click）</summary><div>
#     
# numpyの中で $ e^x $ を計算する関数はexp。数学や工学でよく出てくるので覚えておこう。
#     
# </div></details>
#   
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。
#     
# ```python  
# import numpy as np
# 
# print(np.exp(3))   # 表示させて確認
# ```  
# 
# <br>
# 次の様に表示される。  
#     
#     20.085536923187668  
# 
# <br><br>
# ネイピア数は約2.7なので、 $ 3^3=27 $ であるので感覚的に合っているとわかるだろう。
# ちなみに非推奨だが、累乗演算子\*\*を使えば、expを使わなくても $ e^x $ を計算できる。  
#     
# ```python  
# import numpy as np
# 
# print(np.e**3)   # 表示させて確認
# ```  
#     
# </div></details>

# ---
# ### 問題　三角関数の計算
# $ \sin{2.7 \pi} $をライブラリnumpyを使って計算せよ。
#   
# <details><summary>■【ヒント】（Click）</summary><div>
# numpyの中でsinを計算する関数はsin。
# </div></details>
#   
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。  
#     
# ```python  
# import numpy as np
# 
# print(np.sin(2.7 * np.pi))   # 表示させて確認
# ```  
#     
# <br>
# 次の様に表示される。 
#     
#     0.8090169943749476  
#     
# np.sin(3.14 / 2)で約$\theta=90$°なので約1.0と表示されることも確認しておこう。
#     
# </div></details>

# ---
# ### 問題　等差数列
# 0から10までの等差数列をライブラリnumpyを使って作れ。ただし、公差を2とする。
#   
# <details><summary>■【ヒント】（Click）</summary><div>
# numpyの中で数列を作る関数は2つある。そのうち、公差を指定するタイプの関数がarange。
# </div></details>
#   
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。
# 以下の例では、変数aはndarray型となる。  
#     
# ```python  
# import numpy as np
# 
# a = np.arange(0, 11, 2)   # 第2引数の1つ前が最後の値になるので、10よりは少し大きくする
# print(a)   # 表示させて確認
# ```  
#     
# <br>
# 次の様に表示される。  
#     
#     [0 2 4 6 8 10]  
# 
# <br>
# arangeの使い方は、以下のコマンドをセルで実行すれば表示される。ただし、予めnumpyをnpという名前でインポートしておくこと。  
#     
# ```python  
# ?np.arange
# ```  
# 
# </div></details>
# 

# ---
# ### 問題　listからndarrayへの型変換
# \[13, 2, 4, 6, 24, 1\]というlist型の配列があるとき、これをlist型からndarray型に変換せよ。なお、型はtypeという標準関数で確認できる。
# 
# 
# <details><summary>■【ヒント】（Click）</summary><div>
# 型を確認する例
# 
# ```python  
# print(type([1,2,3]))   # 表示させて[1,2,3]の型を確認
# ```
# 
# \<class 'list'\>と表示され、\[1,2,3\]がlist型であることがわかる。
# </div></details>
#     
# 
# <br>
# <details open>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。
#     
# ```python  
# import numpy as np
# 
# a = [13, 2, 4, 6, 24, 1]
# b = np.array(a)   # array()にlistを渡すことでndarray型に変換できる
# print(type(a), a)   # 変数aの型と中身を表示
# print(type(b), b)   # 変数bの型と中身を表示
# ```  
# 
# <br>
# 次の様に表示される。 表示された順番から、aがlist型でbはndarray型であることがわかる。
#     
#     <class 'list'> [13, 2, 4, 6, 24, 1]  
#     <class 'numpy.ndarray'> [13  2  4  6 24  1]  
#     
# </div></details>

# ---
# ### 問題　ブロードキャストを利用した数式の計算
# 2～7の整数それぞれについて、$ y=3x^2 + 4x - 4 $を計算せよ。ただし、numpyのブロードキャストを利用すること。
#   
# <details><summary>■【ヒント】（Click）</summary><div>
# 複数の値に対応した計算結果が欲しい場合、numpyのブロードキャストを利用すると便利だ。その場合、計算そのものは作った関数に行わせる。ndarray型の変数vがあれば、f(v)でvの要素ごとに関数fの結果が格納された配列が作成される。 
# </div></details>
#   
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。 
#     
# ```python  
# import numpy as np
# 
# def f(x):    # 数式を表現した関数
#     return 3 * x**2 + 4 * x - 4    # 関数の呼び出し基に計算結果をreturnで戻す。**は*や+より結合が強い。
#     
# a = np.arange(2, 8, 1)   # 第2引数の1つ前が最後の値になるので、7よりは少し大きくする
# b = f(a)
# print(a)
# print(b)   # 表示させて確認
# ```  
#     
#     
# <br>
# 次の様に表示される。  
#     
#     [2 3 4 5 6 7]  
#     [ 16  35  60  91 128 171]   
# 
# 変数aに代入した配列のそれぞれの要素に対応した値が変数bに代入されている。2を代入すると16と簡単に計算できるので、計算結果が正しいことがわかるだろう。
# 
# </div></details>

# ---
# ### 問題　ライブラリmathではブロードキャストができない件
# 次のプログラムは\[1.0, 2.0, 3.0, 4.0\]という出力が得られることを期待しているが、エラーが出る。これはライブラリmathがブロードキャストに対応していないためである。numpyの関数に変えて、エラーが出ないようにせよ。
# 
# ```python
# 
# import math
# 
# print("test: ", math.log10(100))       # これはうまく行く
# a = np.array([10, 100, 1000, 10000])   # ndarray型の配列を作る
# b = math.log10(a)    # これはうまく行かない
# print(a)    # 変数名を確認
# print(b)    # 表示させて確認
# 
# # 出力
# test:  2.0
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-29-0b006c357f04> in <module>
#       3 print("test: ", math.log10(100))
#       4 a = np.array([10, 100, 1000, 10000])   # ndarray型の配列を作る
# ----> 5 b = math.log10(a)
#       6 print(a)
#       7 print(b)   # 表示させて確認
# 
# TypeError: only size-1 arrays can be converted to Python scalars
# 
# ```
# 
# <details><summary>■【ヒント】（Click）</summary><div>
# log10はnumpyにもあるので、numpyの関数に置き換えれば良い。
# </div></details>
# 
# 
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     
# 解答例を以下に示す。  
#     
# ```python  
# import numpy as np
# 
# print("test: ", np.log10(100))    # **変更箇所**
# a = np.array([10, 100, 1000, 10000])   # ndarray型の配列を作る
# b = np.log10(a)    # **変更箇所** これはうまく行く
# print(a)    # 変数名を確認
# print(b)    # 表示させて確認  
# ```
#     
# <br>
# 次の様に表示される。  
#     
#     test:  2.0
#     [   10   100  1000 10000]
#     [1. 2. 3. 4.]
# 
# </div></details>
