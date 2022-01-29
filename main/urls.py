
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('createUser', createUser, name='createUser'),
    path('logout', logout, name='logout'),
    path('checkUser', checkUser, name='checkUser'),
    path('lists', lists, name='lists'),
    path('createlist', createlist, name='createlist'),
    path('add_question/<int:list_id>', add_question, name='add_question'),
    path('createquestion', createquestion, name='createquestion'),
    path('delete_list/<int:id>', delete_list, name='delete_list'),
    path('view/<int:id>', view, name='view'),
    path('results', results, name='results'),
    path('attempt/<int:id>', attempt, name='attempt'),
    path('submitquizresult', submitquizresult, name='submitquizresult'),
]
