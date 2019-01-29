# Chaper 01 - Unit 05 - Worl Cup Group B standings

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
portugal = {'wins': 0, 'loses': 0, 'draws': 0,
            'goal difference': 0, 'points': 0}
morocco = {'wins': 0, 'loses': 0, 'draws': 0,
           'goal difference': 0, 'points': 0}

unsortedStandings = {'Iran': iran, 'Spain': spain,
                     'Portugal': portugal, 'Morocco': morocco}

calc(iran, spain, results[0])
calc(iran, portugal, results[1])
calc(iran, morocco, results[2])
calc(spain, portugal, results[3])
calc(spain, morocco, results[4])
calc(portugal, morocco, results[5])

calc_points(unsortedStandings)

standings = list(unsortedStandings.items())
standings.sort(key=lambda x: x[1]['points'], reverse=True)

sorting = [0, 1, 2, 3]
n = len(sorting)
for i in range(n):
    for j in range(n-i-1):
        x = sorting[j]
        if standings[x][1]['points'] == standings[x+1][1]['points']:
            if standings[x][1]['wins'] >= standings[x+1][1]['wins']:
                if standings[x][0] > standings[x+1][0]:
                    sorting[j], sorting[j+1] = sorting[j+1], sorting[j]


lastList = [x for _, x in sorted(zip(sorting, standings))]

for i in lastList:
    print('%s  wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d' %
          (i[0], i[1]['wins'], i[1]['loses'], i[1]['draws'], i[1]['goal difference'], i[1]['points']))
