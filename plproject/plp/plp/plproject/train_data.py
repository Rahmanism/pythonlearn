from . import models
from sklearn import tree
from sklearn import preprocessing
from .models import Car


def train():
    x = []
    y = []
    cars = Car.objects.all()
    leX = preprocessing.LabelEncoder()
    leY = preprocessing.LabelEncoder()
    for car in cars:
        sample = [car.name, car.year, car.km]
        x.append(sample)
        y.append(car.price)

    del x[:-1]
    del y[:-1]

    leX.fit(x)
    return 'T'
    # leY.fit(y)
    # xt = []
    # yt = []
    # for i in range(len(x)):
    #     xt.append(leX.transform(x[i]))
    #     yt.append(leY.transform(y[i]))

    # clf = tree.DecisionTreeClassifier()
    # clf = clf.fit(xt, yt)

    h = '<table border="1" cellpadding="3" style="border-collapse: collapse;">'
    h += '<tr><th>No.</th><th>Name</th><th>Year</th><th>KM</th><th>Price</th></tr>'
    for i in range(len(x)):
        t = '<tr>'
        # t += '<td>%i</td>' % i
        t += '<td>%i</td><td>%s</td><td>%i</td><td>%s</td><td>%s</td>' % (i+1, x[i][0], x[i][1], x[i][2], y[i])
        t += '</tr>'
        h += t
    h += '</table>'

    return h
