import random
import time
import datetime
import pandas as pd

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


    new_pos=[]
    for elem in pos:
        new_pos.append(dict(elem))

    pos_df=pd.DataFrame(new_pos)
    # pos_df.to_csv('pos.csv')
    return pos_df


def main_strategy_code():
    pos_df=get_all_position()
    ord_df=get_all_open_orders()
    print(pos_df)
    print(ord_df)


current_time=datetime.datetime.now()
print(current_time)

start_hour,start_min=15,16
end_hour,end_min=15,45

start_time=datetime.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min)
end_time=datetime.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min)

print(start_time)
print(end_time)

while datetime.datetime.now()<start_time:
    print(datetime.datetime.now())
    time.sleep(1)

candle_size=60

while True:
    if datetime.datetime.now()>end_time:
        break
    print(datetime.datetime.now())
    print('before run')
    main_strategy_code()
    print('after run')
    seconds_till_next_min= candle_size- datetime.datetime.now().second
    print('sleeping for',seconds_till_next_min)
    time.sleep(seconds_till_next_min)

print('strategy stopped')




