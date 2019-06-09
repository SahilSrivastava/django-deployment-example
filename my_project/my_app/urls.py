from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from my_app import views

app_name='my_app'

urlpatterns = [
    path("",views.index,name='index'),
    path("register/",views.register,name='register'),
    path('user_login/',views.user_login,name="user_login"),
]
