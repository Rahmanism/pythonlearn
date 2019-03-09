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

    # check this:
    # https://stackoverflow.com/questions/52112414/valueerror-bad-input-shape-in-sklearn-python
    leX.fit_transform(x[0])
    leX.fit_transform(x[1])
    leX.fit_transform(x[2])
    leY.fit_transform(y)
    xt = []
    yt = []
    for i in range(len(x)):
        xt.append([leX.transform(x[i][0]), leX.transform(x[i][1]), leX.transform(x[i][2])])
        yt.append(leY.transform(y[i]))

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(xt, yt)

    h = ''
    h += '<h3>Trained!</h3>'

    h += '<table border="1" cellpadding="3" style="border-collapse: collapse;">'
    h += '<tr><th>No.</th><th>Name</th><th>Year</th><th>KM</th><th>Price</th></tr>'
    for i in range(len(x)):
        t = '<tr>'
        t += '<td>%i</td><td>%s</td><td>%i</td><td>%s</td><td>%s</td>' % (i+1, x[i][0], x[i][1], x[i][2], y[i])
        t += '</tr>'
        h += t
    h += '</table>'

    return h
