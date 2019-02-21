# Chapter 3 - Unit 7 - employees info
import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1', database='test')
cur = cnx.cursor()
query = "select name, weight, height from people order by height desc, weight"
cur.execute(query)
for (name, height, weight) in cur:
    print("%s %i %i" % (name, height, weight))
cur.close()
cnx.close()
