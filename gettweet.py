# Gets some tweets with the given hashtag
import sys
import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)
    sys.exit()
except:
    print('An error happend connecting to DB.')
    sys.exit()

cur = cnx.cursor()

# IF THERE IS NO DATABASE BEFORE
query = ("create database if not exists tweets "
         "character set utf8 collate utf8_general_ci")
cur.execute(query)
cur.execute('use tweets')
query = """\
create table if not exists tweets (
    id int unsigned auto_increment primary key,
    user varchar(255),
    tweet varchar(280),
    hashtag varchar(255),
    time datetime,
    likes int,
    retweets int,
    replys int
) character set utf8 collate utf8_general_ci
"""
cur.execute(query)
# end of creating DB and table

hashtag = input('What\'s the hashtag you looking for? ')
url = 'https://twitter.com/hashtag/%s' % hashtag
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tweets = soup.fnid_all('div', {'class': 'tweet'})
print(tweets.text)
print(len(tweets))
