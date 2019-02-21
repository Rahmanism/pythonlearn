# Chapter 3 - Unit 7 - employees info
import mysql.connector
from random import randint

# to check if the string contains any digit
def has_number(s):
    return any(char.isdigit() for char in s)

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1')
cur = cnx.cursor()


########### IF THERE IS NO DATABASE BEFORE
query = "create database if not exists maktabxune"
cur.execute(query)
cur.execute('use maktabxune')
query = """\
create table if not exists people (
    email varchar(255),
    password varchar(20)
)
"""
cur.execute(query)

########## THE MAIN PART OF EXERCISE

email = ''
password = ''
email_error = 'Wrong email! Try again. Correct pattern: expression@string.string'
query = 'insert into people (email, password) values (%s, %s)'
while not email == 'end':
    email_is_correct = False
    while not email_is_correct:
        email = input('email (type end to finish): ')
        if email == 'end':
            break
        email_parts = email.split('@')
        if len(email_parts) != 2:
            print(email_error)
            continue
        email_domain_parts = email_parts[1].split('.')
        if len(email_domain_parts) != 2:
            # actually it may be correct for more than two parts, i.e. someone@domain.co.uk
            # but to rule the expression@string.string
            # we call it wrong email address!
            print(email_error)
            continue
        if has_number(email_domain_parts[0]) or has_number(email_domain_parts[1]):
            print(email_error)
            continue
        email_is_correct = True

    if email == 'end':
        break
    
    password = input('password: ')
    
    data = (email, password)
    cur.execute(query, data)
    cnx.commit()

query = 'select email, password from people'
cur.execute(query)
print('------------')
print('Here\'s the list:')
for (email, password) in cur:
    print('%s, %s' % (email, password))

cur.close()
cnx.close()
