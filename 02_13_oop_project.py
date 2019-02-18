# Chapter 2 - Unit 13 - OOP Project
import random

class Human:
    def __init__(self, name):
        self.name = name
    
class Footballist(Human):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team
    def __str__(self):
        return '%s, %s' % (self.name, self.team)

footballists = list()

t = random.choice(['A', 'B'])
t2 = 'B' if t == 'A' else 'A'

footballists.append(Footballist('Hosein', t))
footballists.append(Footballist('Mazyar', t2))
footballists.append(Footballist('Akbar', t))
footballists.append(Footballist('Nima', t2))
footballists.append(Footballist('Mahdi', t))
footballists.append(Footballist('Farhad', t2))
footballists.append(Footballist('Mohammad', t))
footballists.append(Footballist('Xashayar', t2))
footballists.append(Footballist('Milad', t))
footballists.append(Footballist('Mostafa', t2))
footballists.append(Footballist('Amin', t))
footballists.append(Footballist('Saeed', t2))
footballists.append(Footballist('Puya', t))
footballists.append(Footballist('Purya', t2))
footballists.append(Footballist('Reza', t))
footballists.append(Footballist('Ali', t2))
footballists.append(Footballist('Behzad', t))
footballists.append(Footballist('Soheil', t2))
footballists.append(Footballist('Behruz', t))
footballists.append(Footballist('Shahruz', t2))
footballists.append(Footballist('Saman', t))
footballists.append(Footballist('Mohsen', t2))

for i in footballists:
    print(str(i))
