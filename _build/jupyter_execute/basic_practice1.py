#!/usr/bin/env python
# coding: utf-8

# # ifとforの組み合わせ問題

# ---
# ## FizzBuzzゲーム
# ### ゲーム内容
# - 複数人でやるゲーム
# - 順番に、1から数字を読み上げる
# - 3で割り切れるときは"Fizz"という
# - また、5で割り切れるときは"Buzz"という
# - ただし、3でも5でも割り切れるときは"FizzBuzz"という
# - 間違えた人が負け
# 
# これをfor文で文字として出力しよう。ただし、Pythonでは（特に指定しなければ）print命令は改行コードも一緒に出力するので注意しよう。
# 
# <br>
# <details><summary>■【ヒント：割り切れるかの検査方法】（Click）</summary><div>
#     割り切れるかどうかは、次のように書いて判断する。  
#     この評価式がTrueになると、この場合は100は5で割り切れることがわかる。  
#     <br><br>
#     
# ```python  
# 100 % 5 == 0  
# ```
#     
# <br>
# </div></details>
# 
# 
# 
# <details><summary>■【ヒント：range関数で1からの連番を作る方法】（Click）</summary><div>
#     range関数は、標準では0から数字を作ってしまう。
#     以下の例では、[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]と表示される。  
# <br>
#     
# ```python  
# print(list(range(10)))  
# ```
#     
# <br>
#     そこで、for文で1から数字を作る方法が必要となる。
#     以下に2通りのやり方を示す。  
# <br>
#     
# ```python  
# # 0から始まるなら1を足せばいいじゃない方式  
# for i in range(5):  
#     j = i + 1  
#     print(j)  # 1～5が表示される  
#     
# # range関数の引数を調整して、1以上の数を作らせればいいじゃない方式  
# for i in range(1, 5):  
#     print(i)   # 1～4が表示される  
# ```  
#     
# <br>
# </div></details>
# 
# 
# 
# <details><summary>■【ヒント：複雑な条件分岐の書き方】（Click）</summary><div>
#     Pythonでは、条件文ifにてAを満たさない場合にもしBを満たしたらという場合にはelif（else if）を使う。いずれの条件にも合致しない場合は、elseを使う。
# <br>
#     
# ```python  
# # pythonのelse ifの書き方  
# if True:   # 条件A  
#     pass   # passは何もしない、という命令
# elif True: # 条件B：Aではなく、もし～なら  
#     pass  
# else:      # いずれの条件も満たさない場合 
#     pass  
# ``` 
#     
# <br>    
# </div></details>
# 
# 
# <details><summary>■【ヒント：複数の評価式の並べ方】（Click）</summary><div>
#     複数の条件を評価式に並べたい場合、andやorが使える。以下に使用例を示す。もし、先に判定して欲しい部分があれば丸カッコ()で括ること。
#     
# ```python
# print(True and True)
# print(True or True)
# print(True and False)
# print(True or False)
# print(False and False)
# print(False or False)
# ```
#     
# これを実行すすると、以下のように表示される。  
#     
#     True  
#     True  
#     False  
#     True  
#     False  
#     False  
#     
# </div></details>
# 
# 
# 
# <br>
# <details>
# <summary>■解答例の表示（Click）</summary><div>
#     解答例を以下に示す。 
# <br><br>
#     
# ```python  
# # FizzBuzzゲーム解答例　1
# for i in range(1, 101): # iは1～100となる
#     #print(i)      # 確認用なので、もしもに備えてコメントアウトした状態にしておく
#     
#     if i % 15 == 0:  # 15で割り切れる場合
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# ```  
#     
# <br>
#     
# ```python  
# # FizzBuzzゲーム解答例　2
# for i in range(1, 101): # iは1～100となる
#     #print(i)      # 確認用なので、もしもに備えてコメントアウトした状態にしておく
#     
#     if i % 3 == 0 and i % 5 == 0:  # 3でも5でも割り切れる場合
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# ```  
# 
# </div></details>
# 

# In[ ]:




