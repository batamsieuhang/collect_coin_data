import time
from take_value import take_data
from datetime import datetime
from count_coin import count_num_coin
import sys

time_value = sys.argv[1:(len(sys.argv)-1)]

map_time_value = {"1": 0, "2": 1, "3": 2,
                  "4": 3, "5": 4, "10": 5, "15": 6, "20": 7}

map_value = []

for i in time_value:
    for key, value in map_time_value.items():
        if i == key:
            map_value.append(value)
sort_value = int(sys.argv[len(sys.argv)-1])

while (True):
    count_coin = {}
    coin_gap_dict = {}

    count_coin, coin_gap_dict = count_num_coin(take_data(map_value))

    sort_count_coin = dict(sorted(
        count_coin.items(), key=lambda x: x[1], reverse=True))
    print("------------------------------{current_time}--------------------------------".format(
        current_time=datetime.now()))
    print(sort_count_coin)
    for coin, value in sort_count_coin.items():
        if value >= sort_value:
            print(coin+":"+coin_gap_dict[coin])
    print("-----------------------------end--------------------------------------------\n")
    time.sleep(10)
