# Chapter 4 - Unit 9 - bama.ir

import sys

import re
import mysql.connector
import requests
from bs4 import BeautifulSoup

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1')
cur = cnx.cursor()

########### IF THERE IS NO DATABASE BEFORE
query = ("create database if not exists maktabxune "
    "character set utf8 collate utf8_general_ci")
cur.execute(query)
cur.execute('use maktabxune')
query = """\
create table if not exists bama (
    car_name varchar(255),
    price varchar(100),
    km varchar(100)
) character set utf8 collate utf8_general_ci
"""
cur.execute(query)
########## end of creating DB and table

MAX_COUNT = 20
BAMA_URL = 'https://bama.ir/car/'
count = 0
page = 1
searched_car = input()
query = "insert into bama (car_name, price, km) values (%s, %s, %s)"
while count < MAX_COUNT:
    if page == 1:
        url = (BAMA_URL + searched_car)
    else:
        url = (BAMA_URL + searched_car + '?page=' + str(page))
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    # this means there's no other pages for this car
    if soup.text == '':
        break
    cars = soup.find_all('div', {'class':'listdata'})
    for car in cars:
        car_name_tag = car.findChildren('h2', {'itemprop':'name'})
        if car_name_tag != None:
            n = car_name_tag[0].text.strip()
            car_name = re.sub(r'\s{2,}', ' ', n)
            price_tag = car.findChildren('p', {'class':'cost'})
            price = price_tag[0].text.strip().replace('\n\n', ' - ')
            km_tag = car.findChildren('p', {'class':'price hidden-xs'})
            km = km_tag[0].text.strip().replace('کارکرد ', '')
            data = (car_name, price, km)
            cur.execute(query, data)
            count += 1
            if count >= MAX_COUNT:
                break
    page += 1

cnx.commit()

# if you want to see the list:
# query = 'select car_name, price, km from bama'
# cur.execute(query)
# for (car_name, price, km) in cur:
#     print('%s\t%s\t%s' % (car_name, price, km))

cur.close()
cnx.close()
