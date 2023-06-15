import requests
import bs4
import re
from urllib.request import Request, urlopen


def take_data():
    url = "https://ckcoin.top/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page = bs4.BeautifulSoup(webpage, "html.parser")


url = "https://ckcoin.top/"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page = bs4.BeautifulSoup(webpage, "html.parser")
page.find_all("div", {"class": "col-md-4"})

col_1 = page.find_all("div", {"class": "col-md-4"})[0]
rows = col_1.find_all('tr')
print(rows[2].select('a')[0].text.strip())
