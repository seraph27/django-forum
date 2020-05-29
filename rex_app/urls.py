from django.urls import path

from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('inc_age', views.inc_age, name='inc_age'),
    path('question/create', views.create_question, name='create_question'),
    path('answer/create/<int:question_pk>', views.create_answer, name='create_answer'),
    path('question/<int:pk>', views.question_detail, name='question_detail'),

    
    
]

