# Chapter 2 - Unit 13 - OOP Project
import random

class Human:
    def __init__(self, name):
        self.name = name
    
class Footballist(Human):
    A, B = 0, 0
    def __init__(self, name):
        super().__init__(name)
        self.set_team()
    def set_team(self):
        team = random.choice(['A', 'B'])
        if team == 'A':
            Footballist.A += 1
        else:
            Footballist.B += 1
        if Footballist.A > 11:
            Footballist.A -= 1
            team = 'B'
            Footballist.B += 1
        elif Footballist.B > 11:
            Footballist.B -= 1
            team = 'A'
            Footballist.A += 1
        self.team = team
    def __str__(self):
        return '%s, %s' % (self.name, self.team)

footballists = list()
footballists.append(Footballist('Hosein'))
footballists.append(Footballist('Mazyar'))
footballists.append(Footballist('Akbar'))
footballists.append(Footballist('Nima'))
footballists.append(Footballist('Mahdi'))
footballists.append(Footballist('Farhad'))
footballists.append(Footballist('Mohammad'))
footballists.append(Footballist('Xashayar'))
footballists.append(Footballist('Milad'))
footballists.append(Footballist('Mostafa'))
footballists.append(Footballist('Amin'))
footballists.append(Footballist('Saeed'))
footballists.append(Footballist('Puya'))
footballists.append(Footballist('Purya'))
footballists.append(Footballist('Reza'))
footballists.append(Footballist('Ali'))
footballists.append(Footballist('Behzad'))
footballists.append(Footballist('Soheil'))
footballists.append(Footballist('Behruz'))
footballists.append(Footballist('Shahruz'))
footballists.append(Footballist('Saman'))
footballists.append(Footballist('Mohsen'))

for i in footballists:
    print(str(i))
