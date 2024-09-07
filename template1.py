import random
import time
import datetime


def main_strategy_code():
    t=random.randint(1,30)
    print('executing the code it will take',t,'seconds')
    time.sleep(t)



current_time=datetime.datetime.now()
print(current_time)

start_hour,start_min=15,16
end_hour,end_min=15,20

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




