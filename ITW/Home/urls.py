from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
    path("", views.index,name='Home'),
    path("contactus", views.contactus,name='Home'),
    path("alerts", views.alerts,name='Home'),
    path("about", views.about,name='Home'),
    path("contact", views.contact,name='Home'),
    path("base", views.base,name='Home')
]