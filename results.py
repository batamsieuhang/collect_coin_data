import time
from take_value import take_data
from datetime import datetime
from count_coin import count_num_coin

def print_results(url,time_value,sort_value,time_delay):
    map_time_value = {"1m": 0, "2m": 1, "3m": 2,
                    "4m": 3, "5m": 4, "10m": 5, "15m": 6, "20m": 7,"30m":8,"1h":9,"2h":10,"4h":11,"6h":12,"12h":13,"13h":14}
    map_value = []

    for i in time_value:
        for key, value in map_time_value.items():
            if i == key:
                map_value.append(value)

    url_map = {"https://ckcoin.top/Futures/Short":"FUTURES_SHORT","https://ckcoin.top/Futures/Long":"FUTURES_LONG","https://ckcoin.top/Spot/Down":"SPOT_DOWN","https://ckcoin.top/Spot/Up":"SPOT_UP"}

    process_count_coin = {}
    while (True):
        count_coin = {}
        coin_gap_dict = {}

        # count and sort coin in one request
        count_coin, coin_gap_dict = count_num_coin(take_data(map_value,url))
        sort_count_coin = dict(sorted(
            count_coin.items(), key=lambda x: x[1], reverse=True))

        # Count coin and sort coin in whole function
        for coin, value in sort_count_coin.items():
            if value >= sort_value:
                if coin in process_count_coin:
                    process_count_coin[coin] += 1
                else:
                    process_count_coin[coin] = 1
        sort_process_count_coin = dict(sorted(process_count_coin.items(),key=lambda x: x[1],reverse=True))

        sort_process_count_gap_coin = dict(sorted(coin_gap_dict.items(),key=lambda x: x[1],reverse=True))
        
        print("----------delay={delay}s--------------------{current_time}------------{time_value}--------".format(
            current_time=datetime.now(),time_value=time_value,delay=time_delay))
        print("----------------------------Thong ke theo so lan xuat hen cua coin tu {count} o tro len-----------".format(count=sort_value))
        
        print("----------------------------Thong ke theo so lan xuat hen tu thoi diem chay------------------------")
        for coin,value in sort_process_count_coin.items():
            space_1 = "     "
            space_2 = "     "
            space_3 = "     "
            if coin in sort_count_coin and sort_count_coin[coin] >= sort_value:
                print(coin+":"+space_1+str(coin_gap_dict[coin])+"%"+space_2+str(process_count_coin[coin])+space_3+str(count_coin[coin]))

        print("----------------------------Thong ke theo %------------------------")
        for coin,value in sort_process_count_gap_coin.items():
            if coin in sort_count_coin and sort_count_coin[coin] >= sort_value:
                print(coin+":"+space_1+str(coin_gap_dict[coin])+"%"+space_2+str(process_count_coin[coin])+space_3+str(count_coin[coin]))
        print("-----------------------------{url_name}--------------------------------------------\n".format(url_name = url_map[url]))
        time.sleep(time_delay)
