# Sakura Aoi

![葵桜](https://s3.akarinext.org/assets/*/sakura-aoi.png)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F2F36AA7M)

## 概要

葵桜はMi.pyを使用したMisskeyBotです。基本的に会話や計算などといった機能を追加する予定です。

## 使い方

.envをプロジェクト内に作成し以下の変数を定義してください

```dotenv
TOKEN=example
URI=wss:example.com/streaming
MEGA_EMAIL=example@example.com
MEGA_PASSWORD=example
```

各変数の説明は以下のとおりです

|変数名|説明|
|---|---|
|TOKEN|BotにするアカウントのTOKEN|
|URI|BOTにするアカウントがあるインスタンスのWebSocketURL|
|PG_USER_NAME|Misskeyインスタンスのデータベースに接続できるPostgresqlのユーザー名|
|PG_USER_PASSWORD|PG_USER_NAMEのパスワード|
|PG_HOST|対象のデータベースがあるhostのip|
|PG_PORT|対象のデータベースのPort|
|PG_DB_NAME|Misskeyのデータベース名|
|MEGA_EMAIL|MEGA（オンラインストレージサービス）にバックアップを保存する場合に使用するアカウントのEmailです|
|MEGA_PASSWORD|MEGA_EMAILと同様で、MEGAで使用するアカウントのパスワードです|

URIに関してはローカル（テスト環境）等のような暗号化されていないhttpなどの場合は ws:
//という形になります。このBotを実際に使用しているAkariRNの場合だと
`wss:rn.akarinext.org/streaming`となります。

```bash
pip install -r requirements.txt
# データベースの初期化
python main.py --db -i

Ctrl + C

python main.py
```
