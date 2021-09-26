import requests
from bs4 import BeautifulSoup

r = requests.get('https://ambcrypto.com/binance-coin-aave-decred-price-analysis-23-september/')


htmlParser = BeautifulSoup(r.text, 'html.parser')
for i in htmlParser.find_all('p'):
    print(i.get_text())
