import time
from urllib.request import Request, urlopen
from take_value import take_data
from datetime import datetime

while (True):
    count_coin = {}
    data = take_data()
    coin_gap_dict = {}

    for value in data.values():
        for coin in value:
            coin_name = coin['name']
            if coin_name in count_coin:
                count_coin[coin_name] += 1
            else:

                coin_gap_dict[coin_name] = coin['gap']
                count_coin[coin_name] = 1
    sort_count_coin = dict(sorted(
        count_coin.items(), key=lambda x: x[1], reverse=True))
    print("------------------------------{current_time}--------------------------------".format(
        current_time=datetime.now()))
    print(sort_count_coin)
    for coin, value in sort_count_coin.items():
        if value >= 4:
            print(coin+":"+coin_gap_dict[coin])
    print("-----------------------------end--------------------------------------------\n")
    time.sleep(10)
