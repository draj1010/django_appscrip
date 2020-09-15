
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('name', views.get_name, name='get_name'),
    path('que_one', views.que_one, name='que_one'),
    path('que_two', views.que_two, name='que_two'),
    path('summary', views.summary, name='summary'),
    path('history', views.history, name='history'),
]