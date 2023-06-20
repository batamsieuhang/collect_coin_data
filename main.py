import time
from urllib.request import Request, urlopen
from take_value import take_data


while (True):
    count_coin = {}
    data = take_data()

    for value in data.values():
        for coin in value:
            coin_name = coin['name']
            if coin_name in count_coin:
                count_coin[coin_name] += 1
            else:
                count_coin[coin_name] = 1
    sort_count_coin = dict(sorted(
        count_coin.items(), key=lambda x: x[1], reverse=True))
    print("---------------------------------------------------------------------------")
    print(sort_count_coin)
    print("---------------------------------------------------------------------------\n")
    time.sleep(10)
