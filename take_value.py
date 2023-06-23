# this function take value from one column, example index = 0 similar column 1M
import bs4, requests



def take_data(time_value,url):
    all_coin = {}
    res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    page = bs4.BeautifulSoup(res.text, "html.parser")
    for index in time_value:
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
            each_coin["gap"] = float(row_1.select('td')[3].text.strip().strip('%'))  # gap
            coin.append(each_coin)
        all_coin[index] = coin

    return all_coin


