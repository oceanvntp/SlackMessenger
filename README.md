# SlackMessenger

SlackMessengerは、指定されたSlackチャンネルに簡単にメッセージを送信するためのPythonクラスです。

## 特徴

- Slackチャンネルへの簡単なメッセージ送信。
- YAMLファイルからの設定読み込み。

## 使い方

```python
from slack_messenger.main import SlackMessenger

messenger = SlackMessenger(token_file_path='path/to/your/tokenfile.yaml')
messenger.send_slack_message("こんにちは、Slack!")
```

- YAMLファイルに以下を記載する。
    - token: SlackのBot OAuth Token 
    - channel: チャンネルのコード(Cから始まるもの)

### Slack Appの作成（2023/12/12確認）
1. slack api (https://api.slack.com/apps) にアクセスし、ログインする。
2. Create New Appをクリック。
    - From scratchを選択
    - App Nameとworkspaceを選択
3. 左側のFeatures → OAuth & Permissionsを選択。
    - Scopesより、Bot Token Scopesに`chat:write`を付与。
    - Bot User OAuth Tokenをコピーし上記のYAMLにペースト。
4. Features → App Homeを選択。
    - Your App's Presence in Slackより、Display Name(Bot Name)をコピー。
#### 以下、Slackアプリの設定
5. 通知を送りたいチャンネルを選び、`/invite@Bot Name`(Bot Nameは上記でコピーしたもの)で、チャンネルにBotを加える。
6. チャンネル名を右クリックし、チャンネル詳細を表示するをクリックする。
7. ポップアップの下にチャンネルIDがあるので、それをYAMLのchannelに記載する。


## インストール
このライブラリを使用するには、必要な依存関係をインストールする必要があります。以下のコマンドでインストールできます。
```bash
pip install -r requirements.txt
```