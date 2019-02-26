from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
    ret = '<div>'
    all_posts = Post.objects.all()
    for post in all_posts:
        ret += '<p>' + post.text + '</p>\n'
    ret += '</div>'
    return HttpResponse(ret)
