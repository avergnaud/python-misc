# https://api.slack.com/community
# https://api.slack.com/community#python
# v3 avec ce client :
# https://github.com/os/slacker
# (pas mentionné sur son github : faire un "pip install slacker")
from slacker import Slacker

# https://api.slack.com/apps

botUserOAuthAccessToken = input("Bot User OAuth Access Token ? ")

print("Bot User OAuth Access Token : ", botUserOAuthAccessToken)

slack = Slacker(botUserOAuthAccessToken)

# Send a message to #general channel
slack.chat.post_message('#aleatoire', 'Hello fellow slackers! (9.3.slackbot.py)')

# Get users list
response = slack.users.list()
users = response.body['members']
# print(users) 