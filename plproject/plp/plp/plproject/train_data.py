from . import models
from sklearn import tree
from sklearn import preprocessing
from .models import Car
from . import tools

"""
db_file = 'C:\\Users\\Rahmani\\tmp\\pythonlearn\\plproject\\plp\\plp\\db.sqlite3'
conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute('select * from plproject_cars')
rows = cur.fetchall()
for row in rows:
    print(row)
"""


def train(request, trainAgain='y'):
    msg = ''
    # if trainAgain == 'y':
    x, y = [[], []], []
    leX = []
    for i in range(2):
        leX.append(preprocessing.LabelEncoder())

    cars = Car.objects.all()
    if len(cars) < 1:
        return 'داده‌ای برای آموزش در بانک اطلاعاتی وجود ندارد!'

    leX = []
    for i in range(2):
        leX.append(preprocessing.LabelEncoder())

    for car in cars:
        x[0].append(car.name.strip())
        x[1].append(car.meta.strip())
        y.append(car.price)

    leXt = [[], []]
    for i in range(2):
        leXt[i] = leX[i].fit_transform(x[i])

    leXt_final = []
    for i in range(len(leXt[0])):
        leXt_final.append(
            [leXt[0][i], leXt[1][i], cars[i].year, cars[i].km])
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(leXt_final, y)

    msg += '<small>آموزش ماشین انجام شد!</small><br/><br/>'

    if request.method == 'POST':
        try:
            newData = [[leX[0].transform([request.POST['car_name'].strip()])[0], leX[1].transform([request.POST['car_meta'].strip()])[
                0], tools.safe_cast(request.POST['car_year'].strip(), int, 0), tools.safe_cast(request.POST['car_km'].strip(), int, 0)]]
            answer = clf.predict(newData)
        except:
            answer = 'نتوانستم قیمت را پیش بینی کنم!'
        msg += 'قیمت احتمالی: %s<br>' % answer

    return msg
