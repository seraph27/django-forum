from django.urls import path

from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('inc_age', views.inc_age, name='inc_age'),

    
    
]