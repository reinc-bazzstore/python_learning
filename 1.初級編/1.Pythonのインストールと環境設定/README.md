# Python インストールと環境設定ガイド

## 1. Python のインストール

### Windows

[Python 公式サイト](https://www.python.org/downloads/)にアクセスし、任意の Python バージョンをダウンロードします。
ダウンロードしたインストーラを実行し、「**Add Python to PATH**」のチェックボックスを必ず選択します。
「**Install Now**」をクリックし、インストールが完了するまで待ちます。

### macOS

macOS にはデフォルトで Python 2 がインストールされていますが、Python 3 をインストールすることを推奨します。
Python 公式サイトから Python 3 をダウンロードします。
ダウンロードしたインストーラを実行し、インストールを完了させます。
ターミナルを開き、

```
python3 --version
```

を実行して、インストールが成功していることを確認します。
Linux (Ubuntu 例)
ターミナルを開き、以下のコマンドを実行して Python 3 をインストールします:

コードをコピーする

```bash
sudo apt update
sudo apt install python3
```

インストールが完了したら、以下のコマンドで確認します:

コードをコピーする

```bash
python3 --version
```

# トラブルシューティング

## 1. コマンドが認識されない

python または pip が認識されない場合、環境変数が正しく設定されていない可能性があります。インストール時に「Add Python to PATH」を選択しなかった場合、手動でパスを設定する必要があります。

## 2. 仮想環境の有効化ができない

Windows では、仮想環境のスクリプトがブロックされている場合があります。以下のコマンドでスクリプトの実行を許可してください:

コードをコピーする

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
