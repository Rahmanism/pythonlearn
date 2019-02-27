from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch/', views.fetch, name='fetch'),
    path('fetch/<int:howManyToFetch>', views.fetch, name='fetch_count'),
]
