# Chapter 04
import requests
from bs4 import BeautifulSoup
import re

try:
    print('before request')
    r = requests.get('http://google.com')
    print(r)
except:
    print('test')

# get bitcoin price from livecoin using API
r = requests.get('https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD')
price = r.json()
print('highest price of bitcoin: %.2f' % price['high'])

# pip install  beautifulsoup4
r = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?price=20-50')
soup = BeautifulSoup(r.text, 'html.parser')
# find first h2
val = soup.find('h2')
# this is equal to following two lines
all_cars = soup.find_all('h2')
val = all_cars[0]
print(val.attrs['class'])
print(re.sub(r'\s+', ' ', val.text).strip())

for car in all_cars:
    print(re.sub(r'\s+', ' ', car.text).strip())
