from alpaca.data.historical import StockHistoricalDataClient
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo

from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

from alpaca.data.enums import Adjustment

api_key='PKB872RM09BHVAMWPS9P'
secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'

# setup stock historical data client
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key)

symbol='SPY'

# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/stockbars-1
# now = datetime.now(ZoneInfo("America/New_York"))
# req = StockBarsRequest(
#     symbol_or_symbols = symbol,
#     timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Day), # specify timeframe
#     start = now - timedelta(days = 1000),                          # specify start datetime, default=the beginning of the current day.
#     # end_date=None,                                        # specify end datetime, default=now
#     # limit = 2,                                               # specify limit
# )
# data=stock_historical_data_client.get_stock_bars(req).df
# print(data)



now = datetime.now(ZoneInfo("America/New_York"))
req = StockBarsRequest(
    symbol_or_symbols = symbol,
    timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Day), # specify timeframe
    start = datetime(2024,6,1),                          # specify start datetime, default=the beginning of the current day.
    end_date=datetime(2024,7,24),                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
    adjustment=Adjustment.ALL
)
data=stock_historical_data_client.get_stock_bars(req).df
print(data)