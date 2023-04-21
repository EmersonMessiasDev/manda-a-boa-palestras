from django.shortcuts import render
from .models import Evento, Palestrante, Pergunta
from datetime import datetime
import qrcode
from django.core.files.images import ImageFile

data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')

# Create your views here.

def home(request):
    return render(request, 'evento/index.html')


def eventos(request):
    evento = Evento.objects.filter(data=data_formatada)
    
    context = {'eventos':evento}
    
    return render(request, 'evento/eventos.html', context)


def qrCorde(request, id):
    return render(request, 'evento/qrCode.html')


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
