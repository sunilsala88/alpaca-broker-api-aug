import random
import time
import datetime


def main_strategy_code():
    t=random.randint(1,30)
    print(t)
    time.sleep(t)


current_time=datetime.datetime.now()
print(current_time)

while True:
    print(datetime.datetime.now())
    print('before run')
    main_strategy_code()
    print('after run')
    seconds_till_next_min= 60- datetime.datetime.now().second
    print(seconds_till_next_min)
    time.sleep(seconds_till_next_min)
    




