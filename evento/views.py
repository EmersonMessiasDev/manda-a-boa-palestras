from django.shortcuts import render,redirect
from .models import Evento, Palestrante, Pergunta
from datetime import datetime
import qrcode
from django.core.files.images import ImageFile
from django.contrib.messages import constants
from django.contrib import messages
import re
#! from django_ajax.decorators import ajax
from better_profanity import profanity 
from .palavrasOf import lista_negra
from django.http import Http404, JsonResponse


data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')

# Create your views here.

def home(request):
    if request.session.get('usuario'): 
        return redirect('usuario:admin_palestrante')
    
    return render(request, 'evento/index.html')



def eventos(request):  
    return render(request, 'evento/eventos.html')



def validar_pin(request):
    pin = request.POST.get('pin')
    if not pin:
        messages.add_message(request, constants.ERROR, 'Insira o pin e clique em ACESSAR!')
    else:
        try:
            pin = int(pin)
            evento = Evento.objects.filter(pin=pin)
        except:
            messages.add_message(request, constants.ERROR, 'Insira um pin valido!')
            return  redirect('evento:eventos')
            
        if len(evento) == 0:
            print('não tem evento')
            messages.add_message(request, constants.ERROR, 'PIN invalido!')
        
        elif len(evento) > 0:
            data_evento = Evento.objects.get(pin=pin)
            data = data_evento.data.strftime('%Y-%m-%d')    
            if data != data_formatada:
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
    
    if nome.strip() == '':
            messages.add_message(request, constants.SUCCESS, f'Seu nome não pode ficar vazio!')
            return redirect('evento:pergunta', id=evento_id.id)
    
    if nome_palestrante == '':
        nome_palestrante = 'Um dos palestrantes'


    #! Tratamento de palavras ofensivas
    pergunta = request.POST.get('pergunta')
    if pergunta.strip() == '':
            messages.add_message(request, constants.SUCCESS, f'O campo pergunta não pode ficar vazio!')
            return redirect('evento:pergunta', id=evento_id.id)
        
    for palavra in lista_negra:
        if palavra in pergunta:
            messages.add_message(request, constants.SUCCESS, f'ERRO!Foi identificada palavras ofencisva na sua pergunta! se persistir você sera bloqueado!')
            return redirect('evento:pergunta', id=evento_id.id)
    
    
    pergunta = Pergunta.objects.create(
        nome = nome,
        palestrante = nome_palestrante,
        pegunta = pergunta,
        evento = evento_id
    )
    messages.add_message(request, constants.SUCCESS, 'Sua pergunta foi enviada!')

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
