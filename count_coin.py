def count_num_coin(data):
    count_coin = {}
    coin_gap_dict = {}
    for value in data.values():
        for coin in value:
            coin_name = coin['name']
            if coin_name in count_coin:
                count_coin[coin_name] += 1
            else:

                coin_gap_dict[coin_name] = coin['gap']
                count_coin[coin_name] = 1
    return count_coin, coin_gap_dict
