# SlackMessenger

SlackMessengerは、指定されたSlackチャンネルに簡単にメッセージを送信するためのPythonクラスです。

## 特徴

- Slackチャンネルへの簡単なメッセージ送信。
- YAMLファイルからの設定読み込み。

## 使い方

```python
from main import SlackMessenger

messenger = SlackMessenger(token_file_path='path/to/your/tokenfile.yaml')
messenger.send_slack_message("こんにちは、Slack!")
```

## インストール
このライブラリを使用するには、必要な依存関係をインストールする必要があります。以下のコマンドでインストールできます。
```bash
pip install -r requirements.txt
```