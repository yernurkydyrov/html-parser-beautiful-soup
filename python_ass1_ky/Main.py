
from pycoingecko import CoinGeckoAPI

coin = CoinGeckoAPI()


class Coin:
    name: object

    def __init__(self, first, Name, money) -> object:
        self.first = first
        self.name = Name
        self.money = money

    def __str__(self) -> object:
        return {self.name}


print("first N cryptocurrencies")

inTop = input()

print("Get all information about cryptocurrencies")
foo = coin.get_coins_markets(vs_currency='usd')

foo = sorted(foo, key=lambda k: k['market_cap'], reverse = True)
print(f"----First Top {inTop}----")
first = 1
arr: list[Coin] = []
crypto: object
for crypto in foo:
    name: object = crypto['symbol'].upper()
    money = crypto['market_cap']
    coin = Coin( first = first, Name = name, money = money)
    arr.append(coin)
    first = first + 1
    if not first <= int(inTop):
        break

for i in arr:
    print(f"{i.first}. {i.name} - {int(i.money)}")

