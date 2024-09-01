

#getting all active orders
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
import pandas as pd
api_key='PKB872RM09BHVAMWPS9P'
secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'
trading_client = TradingClient(api_key, secret_key, paper=True)


def get_all_open_orders():
    # params to filter orders by
    request_params = GetOrdersRequest(
                        status=QueryOrderStatus.OPEN
                    )

    # orders that satisfy params
    orders = trading_client.get_orders(filter=request_params)
    new_order=[]
    for elem in orders:
        new_order.append(dict(elem))

    order_df=pd.DataFrame(new_order)
    return order_df

def get_all_position():

    pos=trading_client.get_all_positions()
    print(pos)

    new_pos=[]
    for elem in pos:
        new_pos.append(dict(elem))

    pos_df=pd.DataFrame(new_pos)
    pos_df.to_csv('pos.csv')
    return pos_df


def close_this_position(ticker_name):
    position = trading_client.get_open_position(ticker_name)
    print(position)
    if len(position)==0:
        print('we dont have any position ')
        return 0

def close_this_order(ticker_name):
    pass


def closs_all_orders():

    # attempt to cancel all open orders
   trading_client.cancel_orders()

def close_all_positions():
    trading_client.close_all_positions()

# df=get_all_open_orders()
# print(df)

# df=get_all_position()
# print(df)
# close_all_positions()



money=trading_client.get_account().cash
print(money)