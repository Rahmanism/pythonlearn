# find passwords from hashes!!!

import csv
import hashlib

f = open('2.csv')
reader = csv.reader(f)

# we know passwords are numbers with maximum length of 4.
# so we produces hashes for all of them,
# then we will search for each hash to find the corresponging password.

hashes = dict()
for i in range(0, 9999):
    hashOfi = hashlib.sha256(str(i).encode('utf-8')).hexdigest()
    hashes[hashOfi] = i

passwords = dict()
for row in reader:
    passwords[row[0]] = hashes[row[1]]

for i in passwords:
    print('Password of %s is %s.' %(i, passwords[i]))

