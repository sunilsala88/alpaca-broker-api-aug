# from alpaca.data.historical import CryptoHistoricalDataClient
# from alpaca.data.requests import CryptoBarsRequest
# from alpaca.data.timeframe import TimeFrame

# # no keys required for crypto data
# client = CryptoHistoricalDataClient()

# request_params = CryptoBarsRequest(
#                         symbol_or_symbols=["BTC/USD", "ETH/USD"],
#                         timeframe=TimeFrame.Day,
#                         start="2022-07-01"
#                  )

# bars = client.get_crypto_bars(request_params)

# print(bars)


from credentials import key,secret
print(key)
print(secret)

# from alpaca.data.historical import StockHistoricalDataClient
# from alpaca.data.requests import StockLatestQuoteRequest

# # keys required for stock historical data client
# client = StockHistoricalDataClient(key, secret)

# # multi symbol request - single symbol is similar
# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

# latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)
# print(latest_multisymbol_quotes)

# # gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price


from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest

# no keys required
client = CryptoHistoricalDataClient()

# single symbol request
request_params = CryptoLatestQuoteRequest(symbol_or_symbols="ETH/USD")

latest_quote = client.get_crypto_latest_quote(request_params)

# must use symbol to access even though it is single symbol
print(latest_quote["ETH/USD"].ask_price)