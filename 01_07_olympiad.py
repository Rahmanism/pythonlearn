# Chapter 01 - Unit 07 - List of people registered in Olympiad

"""
Example:
Input: 
4
m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java

Output:
f Mina C
f Sara java
m Ahmad C++
m Hossein python
"""

number_of_people = int(input())

data = list()
for i in range(number_of_people):
    data.append(input())

for i in range(number_of_people):
    data[i] = data[i].split('.')
    data[i][0] = data[i][0].lower()
    data[i][1] = data[i][1].lower()
    data[i][1] = data[i][1][0].upper() + data[i][1][1:]

data.sort(key=lambda x: x[0][0])

for i in range(number_of_people):
    for j in range(number_of_people-i-1):
        if data[j][0] == data[j+1][0]:
            if data[j][1] > data[j+1][1]:
                data[j], data[j+1] = data[j+1], data[j]

for i in range(number_of_people):
    print('%s %s %s' % (data[i][0], data[i][1], data[i][2]))
