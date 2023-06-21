import time
from urllib.request import Request, urlopen
from take_value import take_data
from datetime import datetime
from count_coin import count_num_coin

while (True):
    count_coin = {}
    data = take_data()
    coin_gap_dict = {}

    count_coin, coin_gap_dict = count_num_coin(take_data())

    sort_count_coin = dict(sorted(
        count_coin.items(), key=lambda x: x[1], reverse=True))
    print("------------------------------{current_time}--------------------------------".format(
        current_time=datetime.now()))
    print(sort_count_coin)
    for coin, value in sort_count_coin.items():
        if value >= 2:
            print(coin+":"+coin_gap_dict[coin])
    print("-----------------------------end--------------------------------------------\n")
    time.sleep(10)
