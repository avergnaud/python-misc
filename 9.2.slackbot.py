# https://api.slack.com/community
# https://api.slack.com/community#python
# v2 avec ce client :
# https://github.com/kn/slack
import slack
import slack.chat

# https://api.slack.com/apps

botUserOAuthAccessToken = input("Bot User OAuth Access Token ? ")

print ("Bot User OAuth Access Token : ", botUserOAuthAccessToken)

slack.api_token = botUserOAuthAccessToken
slack.chat.post_message('#dev', 'Hello slackers! (9.2.slackbot.py)', username='pybot')

import slack.users
slack.users.list()