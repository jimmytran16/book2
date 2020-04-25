from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('register',views.register,name='register'),
    path('userLogin',views.login,name='login'),
    path('adminpage',views.adminpage,name='adminLogin'),
    path('users',views.users,name='users'),
    path('register',views.register,name='register'),
    path('invalid',views.invalid,name='invalid'),
    path('accountRegister',views.accountRegister,name='accountRegister'),
]
