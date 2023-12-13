import requests 
import yaml

class SlackMessenger:
    """
    SlackMessengerは、指定されたSlackチャンネルにメッセージを送信するためのクラスです。

    Attributes:
        token (str): Slack APIトークン。
        channel (str): メッセージを送信するSlackチャンネルのID。

    Methods:
        send_slack_message(message): 指定されたメッセージをSlackチャンネルに送信します。
    """

    def __init__(self, token_file_path: str, file_type='yaml'):
        """
        SlackMessengerクラスのコンストラクタ。

        トークンとチャンネルIDを含むファイルを読み込み、Slack APIでの認証に使用します。

        Parameters:
            token_file_path (str): トークンとチャンネルIDが含まれるファイルのパス。
            file_type (str): ファイルの形式（デフォルトは'yaml'）。
        """
        # ファイルタイプがyamlの場合、yamlファイルを読み込みます
        if file_type == 'yaml':
            with open(token_file_path, 'r') as f:
                keys = yaml.safe_load(f)  # yamlファイルからトークンとチャンネルを読み込む
            
            self.token = keys['token']  # Slack APIトークン
            self.channel = keys['channel']  # SlackチャンネルID

    def send_slack_message(self, message):
        """
        指定されたメッセージをSlackチャンネルに送信します。

        Slack APIのchat.postMessageエンドポイントを使用してメッセージを送信します。

        Parameters:
            message (str): 送信するメッセージ。

        Returns:
            dict: Slack APIのレスポンス。
        """
        url = 'https://slack.com/api/chat.postMessage'  # Slack APIエンドポイント
        headers = {'Authorization': 'Bearer ' + self.token}  # 認証用ヘッダー
        data = {'channel': self.channel, 'text': message}  # 送信データ

        # Slack APIにリクエストを送信し、レスポンスを返す
        response = requests.post(url, headers=headers, data=data)
        return response.json()