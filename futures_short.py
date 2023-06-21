import time
from take_value import take_data
from datetime import datetime
from count_coin import count_num_coin
import sys

time_value = sys.argv[1:(len(sys.argv)-1)]

map_time_value = {"1m": 0, "2m": 1, "3m": 2,
                  "4m": 3, "5m": 4, "10m": 5, "15m": 6, "20m": 7,"30m":8,"1h":9,"2h":10,"4h":11,"6h":12,"12h":13,"13h":14}
url = "https://ckcoin.top/Futures/Short"
map_value = []

for i in time_value:
    for key, value in map_time_value.items():
        if i == key:
            map_value.append(value)
sort_value = int(sys.argv[len(sys.argv)-1])

while (True):
    count_coin = {}
    coin_gap_dict = {}

    count_coin, coin_gap_dict = count_num_coin(take_data(map_value,url))

    sort_count_coin = dict(sorted(
        count_coin.items(), key=lambda x: x[1], reverse=True))
    print("----------{sort_value}--------------------{current_time}------------{time_value}--------".format(
        current_time=datetime.now(),time_value=time_value,sort_value=sort_value))
    print(sort_count_coin)
    for coin, value in sort_count_coin.items():
        if value >= sort_value:
            print(coin+":"+coin_gap_dict[coin])
    print("-----------------------------FUTURES_SHORT--------------------------------------------\n")
    time.sleep(3)
