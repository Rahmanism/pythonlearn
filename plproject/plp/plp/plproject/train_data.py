from . import models
from sklearn import tree
from sklearn import preprocessing
from .models import Car

"""
db_file = 'C:\\Users\\Rahmani\\tmp\\pythonlearn\\plproject\\plp\\plp\\db.sqlite3'
conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute('select * from plproject_cars')
rows = cur.fetchall()
for row in rows:
    print(row)
"""

def train(request, trainAgain = ''):
    msg = ''
    if trainAgain == 'y':
        x, y = [[],[],[]], []
        cars = Car.objects.all()
        if len(cars) < 1:
            return 'No data to train!'
        leX = []
        for i in range(3):
            leX.append(preprocessing.LabelEncoder())
        leY = preprocessing.LabelEncoder()
        for car in cars:
            x[0].append(car.name)
            x[1].append(car.year)
            x[2].append(car.km)
            y.append(car.price)

        # check this:
        # https://stackoverflow.com/questions/52112414/valueerror-bad-input-shape-in-sklearn-python
        leXt = [[],[],[]]
        leXt[0] = leX[0].fit_transform(x[0])
        leXt[1] = leX[1].fit_transform(x[1])
        leXt[2] = leX[2].fit_transform(x[2])
        leYt = leY.fit_transform(y)

        leXt_final = []
        for i in range(len(leXt[0])):
            leXt_final.append([leXt[0][i], leXt[1][i], leXt[2][i]])
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(leXt_final, leYt)

        msg += '<h3>Trained!</h3>'

    msg += '***'
    # TODO: get data to predict from reqeust
    

    # h += '<table border="1" cellpadding="3" style="border-collapse: collapse;">'
    # h += '<tr><th>No.</th><th>Name</th><th>Year</th><th>KM</th><th>Price</th></tr>'
    # for i in range(len(x)):
    #     t = '<tr>'
    #     t += '<td>%i</td><td>%s</td><td>%i</td><td>%s</td><td>%s</td>' % (i+1, x[i][0], x[i][1], x[i][2], y[i])
    #     t += '</tr>'
    #     h += t
    # h += '</table>'

    return msg
