# Python のループを学ぼう

## はじめに

ループは、繰り返し処理を行うときに使用します。Python には主に 2 つのループがあります：

1. **for ループ** - リストやタプルなどのコレクションを反復処理するのに使用します。
2. **while ループ** - 指定した条件が満たされる限り繰り返し処理を行います。
   このガイドでは、これらのループの基本を学び、シンプルなプログラムを作成して実際に使ってみましょう。

## for ループ

`for`ループは、リストなどのコレクションを一つ一つの要素に対して繰り返し処理を行うために使います。

### 例:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
   print(f"I like {fruit}")
```

### プログラムの説明:

- `fruits`というリストに、3 つのフルーツが格納されています。
- `for`ループはリスト内の各要素（`apple`、`banana`、`cherry`）を順番に処理します。
- 各要素に対して、`I like <フルーツ名>`というメッセージが表示されます。

### 出力例:

```
I like apple
I like banana
I like cherry
```

## while ループ

`while`ループは、指定した条件が `True` である限り繰り返し処理を行います。条件が `False` になるとループが終了します。

### 例:

```python
counter = 5

while counter > 0:
   print(f"Counter: {counter}")
   counter -= 1
```

### プログラムの説明:

- 変数 `counter` が 5 から始まります。
- `wile` ループは `counter > 0` が `True` の間、繰り返し処理を行います。
- ループの中で、カウントダウンが表示され、`counter` の値が 1 ずつ減ります。
- `counter` が 0 になった時点でループが終了します。

### 出力例:

```
Counter: 5
Counter: 4
Counter: 3
Counter: 2
Counter: 1
```

## 演習

次のコードをエディタに入力して実行し、結果を確認しましょう。

```python

# for ループ

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
   print(f"I like {fruit}")

# while ループ

counter = 5
while counter > 0:
   print(f"Counter: {counter}")
   counter -= 1
```

コードをエディタにコピーして、新しいファイル（例：`loops_example.py`） として保存します。
コマンドプロンプトやターミナルを開き、ファイルを保存したディレクトリに移動します。
次のコマンドを実行してコードを実行します：

```bash
python loops_example.py
```

## 練習課題

1. for ループを練習しよう
   fruits リストに新しいフルーツを追加してみましょう。例えば、grape や orange を追加し、その結果を確認してみてください。

2. while ループを練習しよう
   counter を 10 に設定し、カウントダウンをもっと長くしてみましょう。逆に、counter が 0 になったら「カウント終了」と表示するコードを追加してみましょう。
