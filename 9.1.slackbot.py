# https://api.slack.com/community
# https://api.slack.com/community#python
# v1 avec ce client :
# https://github.com/loisaidasam/pyslack
from pyslack import SlackClient

# https://api.slack.com/apps

botUserOAuthAccessToken = input("Quelle est la division ? ")

print ("Bot User OAuth Access Token : ", botUserOAuthAccessToken)

client = SlackClient(botUserOAuthAccessToken)

client.chat_post_message('#dev', "Hello ", username='pybot')