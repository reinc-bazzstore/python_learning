# Python 変数とデータ型ガイド

## はじめに

Python では、データを扱うために変数を使用します。変数には数値、文字列、リスト、タプル、辞書などのさまざまなデータ型を格納できます。このガイドでは、基本的なデータ型について説明し、簡単なコードを書いてみましょう。

### 1. 数値型（Numerical Types）

Python では、整数や小数などの数値データを扱うことができます。

```python
コード例:

age = 25 # 整数

height = 5.8 # 小数
```

age は**整数（int）**
height は**小数（float）**

### 2. 文字列型（String Type）

文字列は、テキストデータを扱うデータ型です。文字列は**ダブルクォーテーション（"）またはシングルクォーテーション（'）で囲みます**。

```python
コード例:

name = "John" # 文字列
```

name は**文字列（str）**

### 3. リスト型（List Type）

リストは**複数のデータを 1 つの変数にまとめて保存できる**データ型です。リストのデータは**変更可能で、カンマ（,）で区切って角括弧（[]）で囲みます**。

```python
コード例:

fruits = ["apple", "banana", "cherry"] # リスト
```

fruits は**リスト（list）**

### 4. タプル型（Tuple Type）

タプルはリストと似ていますが、**変更できない（不変）**データ型です。タプルは**丸括弧（()）で囲みます**。

```python
コード例:

coordinates = (10, 20) # タプル
```

coordinates は**タプル（tuple）**

### 5. 辞書型（Dictionary Type）

辞書は**キーと値のペア**でデータを保存します。**キー（"name"など）を使って値（"Alice"や 30 など）を取得します**。辞書は**波括弧（{}）で囲みます**。

```python
コード例:

person = {
"name": "Alice",
"age": 30
} # 辞書
```

person は**辞書（dictionary）**

### 6. 変数の値を出力する

**print 関数**を使って、変数の値を出力することができます。Python では、**f 文字列（フォーマット文字列）を使って変数の内容を組み合わせて表示できます**。

```python
コード例:

# 変数の値を出力
print(f"Name: {name}, Age: {age}, Height: {height}")
print(f"Fruits: {fruits}")
print(f"Coordinates: {coordinates}")
print(f"Person Info: {person}")
```

f 文字列を使って、変数の値を簡単にフォーマットできます。

### 7. 演習

以下のコードを自分のエディタに書き込み、Python で実行してみましょう。

```python
完成コード:

# 数値型
age = 25
height = 5.8

# 文字列型
name = "John"

# リスト型
fruits = ["apple", "banana", "cherry"]

# タプル型（変更不可）
coordinates = (10, 20)

# 辞書型（キーと値のペア）
person = {
"name": "Alice",
"age": 30
}

# 変数の値を出力
print(f"Name: {name}, Age: {age}, Height: {height}")
print(f"Fruits: {fruits}")
print(f"Coordinates: {coordinates}")
print(f"Person Info: {person}")
```

### 8. 実行方法

上記のコードをエディタにコピーして、新しいファイル（例：`variables.py`）として保存します。
コマンドプロンプトやターミナルを開き、ファイルを保存したディレクトリに移動します。
次のコマンドを実行して、コードを実行します：

```bash
python variables.py
```

結果が表示されれば成功です！
