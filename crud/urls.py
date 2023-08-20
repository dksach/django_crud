from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.student),
    path('upload',views.upload),
    path('insert',views.insert),
    
]
