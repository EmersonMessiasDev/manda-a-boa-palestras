from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'evento'

urlpatterns = [
    path('', home, name='home'),
    path('eventos/', eventos, name='eventos'),
    path('pergunta/<int:id>', pergunta, name='pergunta'),
    path('faz_pergunta/<int:id>', faz_pergunta, name='faz_pergunta'),
    path('chat/<int:id>', chat, name='chat'),
    path('qrcode/<int:id>', qrCorde, name='qrcode'),
    path('validar_pin/', validar_pin, name='validar_pin')
]