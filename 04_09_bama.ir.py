# Chapter 4 - Unit 9 - bama.ir

import sys

import mysql.connector
import requests
from bs4 import BeautifulSoup

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1')
cur = cnx.cursor()

########### IF THERE IS NO DATABASE BEFORE
query = "create database if not exists maktabxune"
cur.execute(query)
cur.execute('use maktabxune')
query = """\
create table if not exists bama (
    car varchar(255),
    car_name varchar(255),
    price_pre varchar(100),
    price_monthly varchar(100),
    km varchar(100)
)
"""
cur.execute(query)
########## end of creating DB and table


# query = 'insert into bama (car, car_name, price_pre, price_monthly, km) values (%s, %s, %s, %s)'
# # create data
# data = ('car', car name', 'prepay price', 'price monthly', 'distance km')
# cur.execute(query, data)
# cnx.commit()
cur.close()
cnx.close()


searched_car = input()
url = ('https://bama.ir/car/%s' % searched_car)
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
cars = soup.find_all('div', {'class':'listdata'})
for car in cars:
    print(car)