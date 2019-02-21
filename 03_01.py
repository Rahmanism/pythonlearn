# Chapter 3
import mysql.connector

# SQL:
"""
select version();
show variables like '%version%';
create database test;
use test;
create table people (name varchar(20), age int, gender char);
insert into people (name, age, gender) values ('mostafa', 37, 'm');
insert into people (name, age, gender) values ('ali', 10, 'm');
select * from people;
desc people;
"""

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1', database='test')
cur = cnx.cursor()
# query = 'insert into people (name, age, gender) values (\'toktam\', 40, \'f\')'
# cur.execute(query)
# query2 = ("insert into people (name, age, gender) values ('%s', %i, '%s')")
# data = ('hosein', 8, 'm')
# cur.execute(query2 % data)
# query3 = ("insert into people (name, age, gender) values (%(name)s, %(age)s, %(gender)s)")
# data3 = {
#     'name': 'toktam',
#     'age': 40,
#     'gender': 'f'
# }
# cur.execute(query3, data3)
# query4 = ("insert into people (name, age, gender) values (%s, %s, %s)")
# data4 = ('mahdi', 3, 'm')
# cur.execute(query4, data4)
# cnx.commit()
query5 = "select * from people"
cur.execute(query5)
print("name\tage\tgender")
print("--------------------")
for (name, age, gender) in cur:
    print("%s\t%i\t%s" % (name, age, gender))
cur.close()
print('cursor closed.')
cnx.close()
print('connection closed.')
