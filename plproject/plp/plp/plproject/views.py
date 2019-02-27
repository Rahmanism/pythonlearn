from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . import fetch_data

def index(request):
    name = "User"
    t = get_template("index.html")
    html = t.render({'name':name})
    return HttpResponse(html)

def fetch(request):
    # return HttpResponse("Hello from FETCH!")
    return HttpResponse(fetch_data.fetch())
