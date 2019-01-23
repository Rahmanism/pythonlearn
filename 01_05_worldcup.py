# Chaper 01 - Unit 05 - Worl Cup Group B standings
import sys

"""
Order of games:
Iran - Spain
Iran - Portugal
Iran - Morocco
Spain - Portugal
spain - Morocco
Portugal - Morocco
"""

def calc(first, second, result):
    x, y = result.split('-')
    x = int(x)
    y = int(y)
    if x > y:
        first['wins'] += 1
        second['loses'] += 1
    elif x == y:
        first['draws'] += 1
        second['draws'] += 1
    else:
        first['loses'] += 1
        second['wins'] += 1
    first['goal difference'] += x - y
    second['goal difference'] += y - x

def calc_points(s):
    for i in s:
        s[i]['points'] = s[i]['wins'] * 3 + s[i]['draws']


results = list()
for i in range(6):
    results.append(input())

iran = {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
spain = {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
portugal = {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
morocco = {'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}

unsortedStandings = {'Iran': iran, 'Spain': spain, 'Portugal': portugal, 'Morocco': morocco}

calc(iran, spain, results[0])
calc(iran, portugal, results[1])
calc(iran, morocco, results[2])
calc(spain, portugal, results[3])
calc(spain, morocco, results[4])
calc(portugal, morocco, results[5])

calc_points(unsortedStandings)

standings = list(unsortedStandings.items())
standings.sort(key=lambda x:x[1]['points'], reverse=True)

sorting = list()
for i in range(len(standings) - 1):
    print(i)
    print(standings[i], standings[i][1]['points'])
    print(standings[i+1], standings[i + 1][1]['points'])
    if standings[i][1]['points'] == standings[i + 1][1]['points']:
        if standings[i][1]['wins'] >= standings[i + 1][1]['wins']:
            if standings[i][0] > standings[i + 1][0]:
                sorting.append(i + 1)
    else:
        sorting.append(i)
    print(sorting)
    input()
    

print(sorting)
sys.exit()

top = 'Iran'
for i in unsortedStandings:
    if unsortedStandings[i]['points'] >= unsortedStandings[top]['points'] \
        and unsortedStandings[i]['wins'] >= unsortedStandings[top]['wins'] \
        and i > top:
        top = i

standings.append({top: unsortedStandings[top]})

for i in unsortedStandings:
    print(i)

print('================')
print(results)
print(unsortedStandings)
print(standings)


