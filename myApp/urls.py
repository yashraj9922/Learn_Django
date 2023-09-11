from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.services, name="servics"),
    path("contacts", views.contacts, name="contacts"),
]
