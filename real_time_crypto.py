

# from alpaca.trading.stream import TradingStream

# api_key='PKB872RM09BHVAMWPS9P'
# secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'
# trading_stream = TradingStream(api_key, secret_key, paper=True)

# async def update_handler(data):
#     # trade updates will arrive in our async handler
#     print(data)

# # subscribe to trade updates and supply the handler as a parameter
# trading_stream.subscribe_trade_updates(update_handler)

# # start our websocket streaming
# trading_stream.run()

from alpaca.data.live import StockDataStream,CryptoDataStream

import credentials as cs

api_key='PKB872RM09BHVAMWPS9P'
secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'

symbol="BTC/USD"

wss_client = CryptoDataStream(api_key,secret_key)

# async handler
async def quote_data_handler(data):
    # quote data will arrive here

    print("$$$$$$$$",data.symbol,data.timestamp,data.ask_price)

wss_client.subscribe_quotes(quote_data_handler, symbol)
# wss_client.subscribe_quotes(quote_data_handler, 'ETH/USD')

wss_client.run()

