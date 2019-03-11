from bs4 import BeautifulSoup
import requests
from . import models
import re

# It should fetch data from a website!

def fetch(howManyToFetch=0):
    BAMA_URL = 'https://bama.ir/car/'
    BAMA_ALLCAR_URL = BAMA_URL + 'all-brands/all-models/all-trims'

    count = 0
    page = 1
    while count < howManyToFetch:
        url = (BAMA_ALLCAR_URL + '?page=' + str(page))
        r = requests.get(url, allow_redirects=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        # this means there's no other pages for this car
        if soup.text == '':
            break
        cars = soup.find_all('div', {'class': 'listdata'})
        for car in cars:
            car_name_tag = car.findChildren('h2', {'itemprop': 'name'})
            if car_name_tag != None:
                n = car_name_tag[0].text.strip()
                car_name = re.sub(r'\s{2,}', ' ', n)
                car_name_text = car_name.split('،')
                car_year = int(car_name_text[0])
                car_name = ''.join(car_name_text[1:])
                price_tag = car.findChildren('p', {'class': 'cost'})
                car_price = price_tag[0].text.strip().replace('\n\n', ' - ')
                km_tag = car.findChildren('p', {'class': 'price hidden-xs'})
                car_km = km_tag[0].text.strip().replace('کارکرد ', '')
                # to prevent reptitive data
                c = models.Car.objects.filter(
                    name=car_name, year=car_year, km=car_km, price=car_price)
                if len(c) > 0:
                    continue
                else:
                    car = models.Car()
                    car.name = car_name
                    car.year = car_year
                    car.price = car_price
                    car.km = car_km
                    car.save()
                    count += 1
                if count >= howManyToFetch:
                    break
        page += 1

    return 'Data of %i cars imported.' % count
