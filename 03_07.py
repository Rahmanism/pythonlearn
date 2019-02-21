# Chapter 3 - Unit 7 - employees info
import mysql.connector
from random import randint

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1')
cur = cnx.cursor()


########### IF THERE IS NO DATABASE BEFORE
query = "create database if not exists company"
cur.execute(query)
cur.execute('use company')
query = """\
create table if not exists people (
    name varchar(20),
    height int,
    weight int
)
"""
cur.execute(query)

# insert some random data if there isn't already.
query = 'select count(*) from people'
cur.execute(query)
count = cur.fetchone()
if count[0] < 1:
    query = "insert into people (name, height, weight) values "
    for i in range(4):
        query += "('name" + str(randint(1,100)) + "', "
        query += str(randint(100, 250)) + ", "
        query += str(randint(50, 150)) + "),"

    query = query[:-1]
    cur.execute(query)
    cnx.commit()

####################################
########## THE MAIN PART OF EXERCISE

query = "select name, weight, height from people order by height desc, weight"
cur.execute(query)
for (name, height, weight) in cur:
    print("%s %i %i" % (name, height, weight))
cur.close()
cnx.close()
