

#getting all active orders
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus

api_key='PKB872RM09BHVAMWPS9P'
secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'
trading_client = TradingClient(api_key, secret_key, paper=True)

# params to filter orders by
request_params = GetOrdersRequest(
                    status=QueryOrderStatus.OPEN
                   
                 )

# orders that satisfy params
orders = trading_client.get_orders(filter=request_params)
# print(orders)

new_order=[]
for elem in orders:
    new_order.append(dict(elem))
print(new_order)
import pandas as pd
order_df=pd.DataFrame(new_order)

print(order_df.to_csv('order.csv'))
