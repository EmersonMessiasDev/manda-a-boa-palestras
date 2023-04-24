from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('area_palestrante/', area_palestrante, name='area_palestrante'),
    path('cadastro/', cadastro, name='cadastro'), 
    path('validar_login/', validar_login, name='validar_login'),
    path('admin_palestrante/', admin_palestrante, name='admin_palestrante'),
    path('sair/', sair, name="sair")
    
]