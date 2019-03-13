from .models import Car
from . import tools


def show_data(max_count=100):
    msg = ''
    carCount = Car.objects.all().count()
    cars = Car.objects.all().order_by('-id')[:max_count]
    if len(cars) < 1:
        return 'داده‌ای در بانک اطلاعاتی وجود ندارد!'

    msg += '<p>تعداد کل رکوردها: <strong>%i</strong></p>' % carCount
    msg += '<table><tr><th>ID</th><th>Name</th><th>Meta</th><th>Year</th><th>KM</th></th>'
    for car in cars:
        msg += '<tr><td>%i</td><td>%s</td><td>%s</td><td>%i</td><td>%i</td></tr>' % (
            car.id, car.name, car.meta, car.year, car.km)
    msg += '</table>'

    return msg
