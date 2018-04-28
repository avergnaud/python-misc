# doc API Bittrex https://github.com/thebotguys/golang-bittrex-api/wiki/Bittrex-API-Reference-(Unofficial)

# API Key Bittrex
# Pour voir son api_secret sur Bittrex, il faut créer une nouvelle Key.
# Et on ne peut plus la connaitre une fois qu'on a quitté la page...

# Librairie client utilisée :
# https://github.com/mondeja/bittrex_v2
# Suivre les instructions sur sa page

from bittrex_v2 import Bittrex
b = Bittrex()
c = b.get_market_summaries()
# print(c)

api_key_input = input("api_key ? ")
print("api_key : ", api_key_input)

api_secret_input = input("api_secret ? ")
print("api_secret saisi")

b = Bittrex(api_key=api_key_input, api_secret=api_secret_input)
c = b.get_balance(currency="BTC")
print(c)