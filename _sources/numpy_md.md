## 解説 numpy
numpyはPythonで使える計算用のライブラリです。基本的な数学の計算に必要な機能や、テンソル・行列・ベクトルの計算機能を提供しています。numpyはimportで取り込んでから使います。また、毎回プログラムの中でnumpyと書くのは面倒なのでnpと省略することが多いです。省略するにはasを使います。


記述例  

```python  
import numpy as np    # numpyを取り込み、npという名前で使う、という命令

print(np.sin(3.14))   # 約sin(π)の値を表示する
```

---
### 問題　ネイピア数
ライブラリnumpyを使ってネイピア数$e$の値を表示せよ。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。numpyの中に、いくつか定数が定義されており、その中に$e$もある。定数の呼び出しには()は不要である。  
    
```python  
import numpy as np

print(np.e)   # ネイピア数を表示
```  
    
2.718281828459045  
と表示される。

</details>


```python

```

---
### 問題　円周率
ライブラリnumpyを使って円周率$\pi$の値を表示せよ。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。numpyの中に、いくつか定数が定義されており、その中に$\pi$もある。定数の呼び出しには()は不要である。  
    
```python  
import numpy as np

print(np.pi)   # 円周率を表示
```  
    
3.141592653589793  
と表示される。

</details>



```python

```

---
### 問題　自然対数の計算
$ \ln 2 $をライブラリnumpyを使って計算せよ。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
補足：自然対数を数学では$\ln$と書く。自然対数は底がネイピア数の対数です。$ \ln x = \log_e x $<br>
解答例を以下に示す。numpyの中で自然対数を計算する関数はlog。  
    
```python  
import numpy as np

print(np.log(2))   # 表示させて確認
```  
    
0.6931471805599453  
と表示される。
自然対数は底がネイピア数なので、np.log(np.e)で1.0と表示される。
    
</details>


```python

```

---
### 問題　常用対数の計算
$ \log_{10} 2$をライブラリnumpyを使って計算せよ。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。numpyの中で常用対数を計算する関数はlog10。  
    
```python  
import numpy as np

print(np.log10(2))   # 表示させて確認
```  
    
0.3010299956639812  
と表示される。
常用対数は底が10なので、np.log10(100)で2.0と表示される。
    
</details>


```python

```

---
### 問題　expの計算
$ e^3 $をライブラリnumpyの関数を使って計算せよ。ここで、$e$はネイピア数である。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。numpyの中で$ e^x $を計算する関数はexp。数学や工学でよく出てくるので覚えておこう。
    
```python  
import numpy as np

print(np.exp(3))   # 表示させて確認
```  
    
20.085536923187668  
と表示される。ネイピア数は約2.7なので、$ 3^3=27 $であるので感覚的に合っているとわかるだろう。

ちなみに非推奨だが、累乗演算子\*\*を使えば、expを使わなくても$ e^x $を計算できる。  
    
```python  
import numpy as np

print(np.e**3)   # 表示させて確認
```  
    
</details>


```python

```

---
### 問題　三角関数の計算
$ \sin{2.7 \pi} $をライブラリnumpyを使って計算せよ。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。numpyの中でsinを計算する関数はsin。  
    
```python  
import numpy as np

print(np.sin(2.7 * np.pi))   # 表示させて確認
```  
    
0.8090169943749476  
と表示される。
np.sin(3.14 / 2)で約$\theta=90$°なので約1.0と表示されることも確認しておこう。
    
</details>


```python

```

---
### 問題　等差数列
0から10までの等差数列をライブラリnumpyを使って作れ。ただし、公差を2とする。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。numpyの中で数列を作る関数は2つある。そのうち、公差を指定するタイプの関数がarange。
以下の例では、変数aはndarray型となる。  
    
```python  
import numpy as np

a = np.arange(0, 11, 2)   # 第2引数の1つ前が最後の値になるので、10よりは少し大きくする
print(a)   # 表示させて確認
```  
    
[0 2 4 6 8 10]  
と表示される。  

arangeの使い方は、以下のコマンドをセルで実行すれば表示される。ただし、予めnumpyをnpという名前でインポートしておくこと。  
    
```python  
?np.arange
```  

</details>





```python

```

---
### 問題　listからndarrayへの型変換
\[13, 2, 4, 6, 24, 1\]というlist型の配列があるとき、これをlist型からndarray型に変換せよ。なお、型はtypeという標準関数で確認できる。


ヒント：型を確認する例

    
```python  
print(type([1,2,3]))   # 表示させて[1,2,3]の型を確認
```

<class 'list'>と表示され、list型であることがわかる。

<br>
<details open>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。
    
```python  
import numpy as np

a = [13, 2, 4, 6, 24, 1]
b = np.array(a)   # array()にlistを渡すことでndarray型に変換できる
print(type(a), a)   # 変数aの型と中身を表示
print(type(b), b)   # 変数bの型と中身を表示
```  

\<class 'list'\> [13, 2, 4, 6, 24, 1]  
\<class 'numpy.ndarray'\> [13  2  4  6 24  1]  
と表示される。表示された順番から、aがlist型でbはndarray型であることがわかる。

</details>

---
### 問題　ブロードキャストを利用した数式の計算
2～7の整数それぞれについて、$ y=3x^2 + 4x - 4 $を計算せよ。ただし、numpyのブロードキャストを利用すること。
  
<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。複数の値に対応した計算結果が欲しい場合、numpyのブロードキャストを利用する。また、計算そのものは作った関数に行わせる。ndarray型の変数vがあれば、f(v)でvの要素ごとに関数fの結果が格納された配列が作成される。  
    
```python  
import numpy as np

def f(x):    # 数式を表現した関数
    return 3 * x**2 + 4 * x - 4    # 関数の呼び出し基に計算結果をreturnで戻す。**は*や+より結合が強い。
    
a = np.arange(2, 8, 1)   # 第2引数の1つ前が最後の値になるので、7よりは少し大きくする
b = f(a)
print(a)
print(b)   # 表示させて確認
```  
    
[2 3 4 5 6 7]  
[ 16  35  60  91 128 171]  
と表示される。変数aに代入した配列のそれぞれの要素に対応した値が変数bに代入されている。2を代入すると16と簡単に計算できるので、計算結果が正しいことがわかるだろう。

</details>

---
### 問題　ライブラリmathではブロードキャストができない件
次のプログラムは\[1.0, 2.0, 3.0, 4.0\]という出力が得られることを期待しているが、エラーが出る。これはライブラリmathがブロードキャストに対応していないためである。numpyの関数に変えて、エラーが出ないようにせよ。

```python

import math

print("test: ", math.log10(100))       # これはうまく行く
a = np.array([10, 100, 1000, 10000])   # ndarray型の配列を作る
b = math.log10(a)    # これはうまく行かない
print(a)    # 変数名を確認
print(b)    # 表示させて確認

# 出力
test:  2.0
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-0b006c357f04> in <module>
      3 print("test: ", math.log10(100))
      4 a = np.array([10, 100, 1000, 10000])   # ndarray型の配列を作る
----> 5 b = math.log10(a)
      6 print(a)
      7 print(b)   # 表示させて確認

TypeError: only size-1 arrays can be converted to Python scalars

```


<br>
<details>
<summary>■解答例の表示（Click）</summary>
解答例を以下に示す。log10はnumpyにもあるので、numpyの関数に置き換えれば良い。  
    
```python  
import numpy as np

print("test: ", np.log10(100))    # **変更箇所**
a = np.array([10, 100, 1000, 10000])   # ndarray型の配列を作る
b = np.log10(a)    # **変更箇所** これはうまく行く
print(a)    # 変数名を確認
print(b)    # 表示させて確認
```  

test:  2.0  
[   10   100  1000 10000]  
[1. 2. 3. 4.]  
と表示される。

</details>


```python

```
