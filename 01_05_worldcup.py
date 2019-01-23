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

sorting = list()
for i in range(len(standings) - 1):
    iPlusOne = False
    if standings[i][1]['points'] == standings[i + 1][1]['points']:
        if standings[i][1]['wins'] >= standings[i + 1][1]['wins']:
            if standings[i][0] > standings[i + 1][0]:
                iPlusOne = True
            else:
                iPlusOne = False
        else:
            iPlusOne = False
    else:
        iPlusOne = False

    if iPlusOne:
        sorting.append(i + 1)
    else:
        sorting.append(i)

if iPlusOne:
    sorting.append(i)
else:
    sorting.append(i + 1)

lastList = [x for _,x in sorted(zip(sorting,standings))]

for i in lastList:
    print('%s  wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d' % \
          (i[0], i[1]['wins'], i[1]['loses'], i[1]['draws'], i[1]['goal difference'], i[1]['points']))
