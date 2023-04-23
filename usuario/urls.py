from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('area_palestrante/', area_palestrante, name='area_palestrante'),
]