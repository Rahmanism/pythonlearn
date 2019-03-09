from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . import fetch_data
from . import train_data


def index(request):
    name = "User"
    t = get_template("index.html")
    html = t.render({'name': name})
    return HttpResponse(html)


def fetch(request, howManyToFetch=20):
    t = get_template("fetch.html")
    message = fetch_data.fetch(howManyToFetch)
    html = t.render({'message': message})
    return HttpResponse(html)


def train(request, trainAgain=''):
    t = get_template("train.html")
    if trainAgain == 'y':
        message = train_data.train()
    else:
        message = ''
    html = t.render({'message': message})
    return HttpResponse(html)
