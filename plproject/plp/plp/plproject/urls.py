from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch/', views.fetch, name='fetch'),
    path('fetch/<int:howManyToFetch>', views.fetch, name='fetch_count'),
    path('train/', views.train, name='train'),
    path('train/<slug:trainAgain>', views.train, name='train_again'),
    path('data/', views.data, name='data'),
    path('about/', views.about, name='about'),
]
