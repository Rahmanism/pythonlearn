from bs4 import BeautifulSoup
import requests
from . import models

# It should fetch data from a website!
def fetch(howManyToFetch = 20):
    BAMA_URL = 'https://bama.ir/car/'
    r = requests.get('https://bama.ir/car')
    soup = BeautifulSoup(r.text, 'html.parser')

    count = 0
    page = 1
    searched_car = input()
    # query = "insert into bama (car_name, price, km) values (%s, %s, %s)"
    # while count < howManyToFetch:
    #     if page == 1:
    #         url = (BAMA_URL + searched_car)
    #     else:
    #         url = (BAMA_URL + searched_car + '?page=' + str(page))
    #     r = requests.get(url, allow_redirects=False)
    #     soup = BeautifulSoup(r.text, 'html.parser')
    #     # this means there's no other pages for this car
    #     if soup.text == '':
    #         break
    #     cars = soup.find_all('div', {'class':'listdata'})
    #     for car in cars:
    #         car_name_tag = car.findChildren('h2', {'itemprop':'name'})
    #         if car_name_tag != None:
    #             n = car_name_tag[0].text.strip()
    #             car_name = re.sub(r'\s{2,}', ' ', n)
    #             price_tag = car.findChildren('p', {'class':'cost'})
    #             price = price_tag[0].text.strip().replace('\n\n', ' - ')
    #             km_tag = car.findChildren('p', {'class':'price hidden-xs'})
    #             km = km_tag[0].text.strip().replace('کارکرد ', '')
    #             data = (car_name, price, km)
    #             cur.execute(query, data)
    #             count += 1
    #             if count >= howManyToFetch:
    #                 break
    #     page += 1




    title = soup.find('title')
    return title.text
