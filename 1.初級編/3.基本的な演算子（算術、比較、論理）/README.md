# Python 演算子ガイド

## はじめに

Python では、数値や条件を扱うためにさまざまな演算子を使用します。このガイドでは、以下の演算子を学びます：

**算術演算子（数値の計算）**
**比較演算子（条件の比較）**
**論理演算子（複数の条件を組み合わせる）**
それぞれの演算子を学んだ後に、実際にコードを書いてみましょう。

## 1. 算術演算子（Arithmetic Operators）

算術演算子は、数値に対して計算を行うための演算子です。

| 演算子 | 説明             | 例     |
| ------ | ---------------- | ------ |
| +      | 足し算           | x + y  |
| -      | 引き算           | x - y  |
| \*     | 掛け算           | x \* y |
| /      | 割り算           | x / y  |
| %      | 余り（モジュロ） | x % y  |

```python
コード例:

# 算術演算子
x = 10
y = 3

print(x + y) # 足し算 -> 13
print(x - y) # 引き算 -> 7
print(x _ y) # 掛け算 -> 30
print(x / y) # 割り算 -> 3.333...
print(x % y) # 余り -> 1
```

- x + y は 13
- x - y は 7
- x \_ y は 30
- x / y は 3.333...
- x % y は 1（10 を 3 で割った時の余り）

## 2. 比較演算子（Comparison Operators）

比較演算子は、**2 つの値を比較**して、結果として**True（真）** または **False（偽）** を返します。

| 演算子 | 説明       | 例     |
| ------ | ---------- | ------ |
| ==     | 等しい     | x == y |
| >      | より大きい | x > y  |
| <      | より小さい | x < y  |
| !=     | 等しくない | x != y |

```python
コード例:

# 比較演算子

x = 10
y = 3

print(x == y) # 等しいか -> False
print(x > y) # より大きいか -> True
```

- x == y は False（10 と 3 は等しくない）
- x > y は True（10 は 3 より大きい）

## 3. 論理演算子（Logical Operators）

論理演算子は、**複数の条件を組み合わせる**ために使用します。結果は `True` か `False` になります。

| 演算子 | 説明                      | 例      |
| ------ | ------------------------- | ------- |
| and    | 両方が True なら True     | x and y |
| or     | どちらかが True なら True | x or y  |
| not    | 真偽を反転させる          | not x   |

```python
コード例:

# 論理演算子

is_raining = True
is_windy = False

print(is_raining and is_windy) # 両方とも True か -> False
print(is_raining or is_windy) # どちらかが True か -> True
print(not is_raining) # 否定 -> False
```

is_raining and is_windy は `False`（どちらも True ではない）
is_raining or is_windy は `True`（どちらかが True）
not is_raining は `False`（True の反対は False）

## 演習

次のコードをエディタに入力して実行し、結果を確認しましょう。

```python

# 算術演算子

x = 10
y = 3
print(x + y) # 足し算
print(x - y) # 引き算
print(x \* y) # 掛け算
print(x / y) # 割り算
print(x % y) # 余り

# 比較演算子

print(x == y) # 等しいか
print(x > y) # より大きいか

# 論理演算子

is_raining = True
is_windy = False
print(is_raining and is_windy) # 両方とも True か
print(is_raining or is_windy) # どちらかが True か
print(not is_raining) # 否定
```

## 実行方法

コードをエディタにコピーして、新しいファイル（例：`operators.py`）として保存します。
コマンドプロンプトやターミナルを開き、ファイルを保存したディレクトリに移動します。
次のコマンドを実行してコードを実行します：

```bash
python operators.py
```

結果が正しく表示されれば成功です！
