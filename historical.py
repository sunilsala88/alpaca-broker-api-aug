


#crypto,option ,stock
#1 min,5 min ,1 day
#start and end

from alpaca.data.historical import CryptoHistoricalDataClient
from datetime import datetime,timedelta

# setup crypto historical data client
crypto_historical_data_client = CryptoHistoricalDataClient()
from zoneinfo import ZoneInfo
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit


# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/cryptobars-1
now = datetime.now(ZoneInfo("America/New_York"))
req = CryptoBarsRequest(
    symbol_or_symbols = "ETH/USD",
    timeframe=TimeFrame(amount = 5, unit = TimeFrameUnit.Minute), # specify timeframe
    start = now - timedelta(days = 10),                          # specify start datetime, default=the beginning of the current day.
    # end_date=None,                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
)
data=crypto_historical_data_client.get_crypto_bars(req).df
print(data)