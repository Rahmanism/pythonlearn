# Chapter 2 - Unit 13 - OOP Project
import random

class Human:
    def __init__(self, name):
        self.name = name
    
class Footballist(Human):
    A, B = 0, 0
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team
    def __str__(self):
        return '%s, %s' % (self.name, self.team)

footballists = list()
def add_footbalist(name):
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
    footballists.append(Footballist(name, team))

add_footbalist('Hosein')
add_footbalist('Mazyar')
add_footbalist('Akbar')
add_footbalist('Nima')
add_footbalist('Mahdi')
add_footbalist('Farhad')
add_footbalist('Mohammad')
add_footbalist('Xashayar')
add_footbalist('Milad')
add_footbalist('Mostafa')
add_footbalist('Amin')
add_footbalist('Saeed')
add_footbalist('Puya')
add_footbalist('Purya')
add_footbalist('Reza')
add_footbalist('Ali')
add_footbalist('Behzad')
add_footbalist('Soheil')
add_footbalist('Behruz')
add_footbalist('Shahruz')
add_footbalist('Saman')
add_footbalist('Mohsen')

for i in footballists:
    print(str(i))
