from unicodedata import name
from django.contrib import admin
from django.urls import path,include,re_path
from . import views


#setting ip urls for our accounts app

app_name='accounts'

urlpatterns =[
    path(r'signup',views.signup,name='signup'),         
    path(r'login',views.login,name='login'),
    path(r'logout',views.logout,name='logout'),
    path(r'shome',views.shome,name='shome'),
    path(r'thome',views.thome,name='thome'),
]