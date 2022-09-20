from django.contrib import admin
from django.urls import path
from .views import user_login, user_register, logout_view

urlpatterns = [
    path('login/', user_login),
    path('register/', user_register),
    path('logout/', logout_view)
]
