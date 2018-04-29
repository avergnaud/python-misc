# https://api.slack.com/community
# https://api.slack.com/community#python
# v2 avec ce client :
# https://github.com/loisaidasam/pyslack
from slackclient import SlackClient
import os

# https://api.slack.com/apps

botUserOAuthAccessToken = input("Bot User OAuth Access Token ? ")

print ("Bot User OAuth Access Token : ", botUserOAuthAccessToken)

slack_token = os.environ[botUserOAuthAccessToken]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="dev",
  text="Hello from Python (v2) ! :tada:"
)