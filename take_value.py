# this function take value from one column, example index = 0 similar column 1M
import requests
import bs4
import re
from urllib.request import Request, urlopen


def take_data():
    url = "https://ckcoin.top/"
    all_coin = {}
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page = bs4.BeautifulSoup(webpage, "html.parser")
    for index in range(0, 8):
        coin = []
        col = page.find_all(
            "div", {"class": "col-md-4"})[index]  # index(=0~1m)
        for i in range(1, 11):
            row_1 = col.find_all('tr')[i]
            each_coin = {}
            each_coin["name"] = row_1.select('a')[0].text.strip()  # name coin
            each_coin["old_price"] = row_1.select(
                'td')[1].text.strip()  # oldprice
            each_coin["new_price"] = row_1.select(
                'td')[2].text.strip()  # newprice
            each_coin["gap"] = row_1.select('td')[3].text.strip()  # gap
            coin.append(each_coin)
        all_coin[index] = coin

    return all_coin
