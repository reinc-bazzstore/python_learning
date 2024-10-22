# Python での入力と出力を学ぼう

## はじめに

プログラムにおいて、ユーザーからの入力を受け取ることは非常に重要です。Python では、`input()`関数を使ってユーザーからの入力を受け取ることができます。また、`print()`関数を使って出力を表示します。

このガイドでは、ユーザーの名前と年齢を入力として受け取り、それに基づいてメッセージを表示するプログラムを作成します。

## 入力と出力の基本

### 1. ユーザーからの入力を受け取る

`input()`関数を使用して、ユーザーからの入力を受け取ります。この関数は、ユーザーが入力したデータを文字列として返します。

```python
name = input("What is your name? ")
```

### 2. 入力内容を表示する

`print()`関数を使用して、受け取った入力を表示します。f 文字列を使うことで、変数の値を簡単に出力することができます。

```python
print(f"Hello, {name}!")
```

## 例：ユーザーからの入力を受け取って出力するプログラム

以下のコードは、ユーザーに名前と年齢を入力してもらい、それに基づいてメッセージを表示します。

```python
# 入力を受け取って出力する
name = input("What is your name? ")
print(f"Hello, {name}!")

# 数値の入力を受け取る
age = int(input("How old are you? "))
print(f"You are {age} years old.")
```

### プログラムの説明:

1. `input("What is your name? ") `でユーザーに名前を尋ね、その名前を `name` 変数に格納します。
2. `print(f"Hello, {name}!")`で挨拶を表示します。
3. 次に、`input("How old are you? ") `でユーザーに年齢を尋ね、`int()`を使って整数に変換します。
4. 最後に、年齢を出力します。

### 出力例:

```
What is your name? Alice
Hello, Alice!
How old are you? 25
You are 25 years old.
```

## 実行手順

```python
# 入力を受け取って出力する
name = input("What is your name? ")
print(f"Hello, {name}!")

# 数値の入力を受け取る
age = int(input("How old are you? "))
print(f"You are {age} years old.")
```

コードをエディタにコピーして、新しいファイル（例：`user_input.py`）という名前で保存します。
コマンドプロンプトやターミナルを開き、ファイルが保存されたディレクトリに移動します。
次のコマンドを実行してプログラムを実行します：

```bash
python user_input.py
```

## 練習課題

1. 名前を 2 回入力してみよう
   `name`を 2 回入力させて、「Hello, `<名前 1>` and `<名前 2>`!」というメッセージを表示するようにプログラムを変更してみましょう。

2. 年齢に基づいてメッセージを表示しよう
   年齢が 18 歳未満の場合は「未成年です。」、18 歳以上の場合は「成人です。」と表示する条件を追加してみましょう。
