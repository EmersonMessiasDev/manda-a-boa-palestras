from django.shortcuts import render,redirect
from .models import Evento, Palestrante, Pergunta
from datetime import datetime
import qrcode
from django.core.files.images import ImageFile
from django.contrib.messages import constants
from django.contrib import messages

data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')

# Create your views here.

def home(request):
    return render(request, 'evento/index.html')


def eventos(request):  
    return render(request, 'evento/eventos.html')


def validar_pin(request):
    pin = request.POST.get('pin')
    evento = Evento.objects.filter(pin=pin)
    data_evento = Evento.objects.get(pin=pin)
    data = data_evento.data.strftime('%Y-%m-%d')
        
    if not pin:
        messages.add_message(request, constants.ERROR, 'Insira o pin e clique em ACESSAR!')
        
    elif len(evento) == 0:
        print('não tem evento')
        messages.add_message(request, constants.ERROR, 'PIN invalido!')
        
    elif data != data_formatada:
        messages.add_message(request, constants.ERROR, 'Esse evento acabou!')
        
    elif data == data_formatada:
        return  redirect('evento:pergunta', id=data_evento.id)

        
    
        
    return render(request, 'evento/eventos.html')




def qrCorde(request, id):
    evento_id = Evento.objects.get(id=id)
    
    context = {'evento':evento_id,
               }
    
    return render(request, 'evento/qrCode.html', context)


def faz_pergunta(request, id):
    evento_id = Evento.objects.get(id=id)
    palestrante= Palestrante.objects.filter(evento_id=id)
    nome = request.POST.get('nome')
    nome_palestrante = request.POST.get('palestrante')
    
    

    print(nome_palestrante)
    pergunta = request.POST.get('pergunta')

    
    pergunta = Pergunta.objects.create(
        nome = nome,
        palestrante = nome_palestrante,
        pegunta = pergunta,
        evento = evento_id
    )
    
    pergunta.save()
    
    context = {'evento':evento_id,
               'palestrante':palestrante}
    
    return render(request, 'evento/pergunta.html', context)
    


def pergunta(request, id):
    evento_id = Evento.objects.get(id=id)
    palestrante = Palestrante.objects.filter(evento_id=id)
  
    context = {'evento':evento_id,
               'palestrante':palestrante}

    return render(request, 'evento/pergunta.html', context)


def chat(request, id):
    evento_id = Evento.objects.get(id=id)
    chat = Pergunta.objects.filter(evento_id=id)
    
    context = {'evento':evento_id,
               'chat':chat}
    
    
    return render(request, 'evento/chat.html', context)
