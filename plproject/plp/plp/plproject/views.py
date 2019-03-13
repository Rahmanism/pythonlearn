from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . import fetch_data
from . import train_data
from . import show_data
from django.views.decorators.csrf import csrf_exempt


def index(request):
    name = "کاربر"
    t = get_template("index.html")
    html = t.render({'name': name})
    return HttpResponse(html)


def fetch(request, howManyToFetch=0):
    t = get_template("fetch.html")
    message = fetch_data.fetch(howManyToFetch)
    html = t.render({'message': message})
    return HttpResponse(html)


@csrf_exempt
def train(request, trainAgain='y'):
    t = get_template("train.html")
    message = train_data.train(request, trainAgain)
    html = t.render({'message': message})
    return HttpResponse(html)


def data(request):
    t = get_template("data.html")
    message = show_data.show_data()
    html = t.render({'message':message})
    return HttpResponse(html)


def about(request):
    t = get_template("about.html")
    html = t.render()
    return HttpResponse(html)
