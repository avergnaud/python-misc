from bittrex_v2 import Bittrex
from datetime import datetime

bittrexClient = Bittrex()
retourBittrex = bittrexClient.get_ticks("USDT-BTC","day")

# requêter pour voir : https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=USDT-BTC&tickInterval=day
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# projet à part...