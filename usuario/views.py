import base64
from django.shortcuts import render, redirect
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from .utils import *
from django.contrib import messages
from django.contrib.messages import constants
from hashlib import sha256
from .models import Usuario
from evento.models import *
from nltk.corpus import stopwords
import nltk

# Create your views here.

def area_palestrante(request):
    return render(request, 'usuario/login.html')

def admin_palestrante(request):
    if request.session.get('usuario'):  
        request_usuario = Usuario.objects.get(id=request.session['usuario'])
        eventos = Evento.objects.filter(responsavel=request_usuario)
        nltk.download('stopwords')       
        context = {
            'evento':eventos
        }
        
        return render(request, 'usuario/admin_palestrante.html', context)
    else:
        messages.add_message(request, constants.ERROR, 'Usuário não está logado')
        return redirect('usuario:area_palestrante')
        
        
        
        
def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar-senha')
        
        if not password_is_valid(request, senha, confirmar_senha, usuario, email):
                return redirect('usuario:area_palestrante')
        
        try:
            senha = sha256(senha.encode()).hexdigest()
            
            user = Usuario.objects.create(username = usuario,
                                          email = email,
                                          senha= senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')
            return redirect('usuario:area_palestrante')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema solicite ajuda ao suporte!')
            return redirect('usuario:area_palestrante')

            
 
def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    
    if len(usuario) == 0:
        messages.add_message(request, constants.ERROR, 'Email ou senha invalidos!')
        return redirect('usuario:area_palestrante')
    
    elif len(usuario) > 0:      
        messages.add_message(request, constants.SUCCESS, 'Usuario logado com sucesso!')
        request.session['usuario'] = usuario[0].id
        return redirect('usuario:admin_palestrante')


def relatorio(request, id):
    if request.session.get('usuario'): 
        request_usuario = Usuario.objects.get(id=request.session['usuario'])
        eventos = Evento.objects.filter(responsavel=request_usuario)
        eventos = eventos.get(id=id)
        relatorio_perguntas = Pergunta.objects.filter(evento_id=eventos)
        stop_words = set(stopwords.words('portuguese'))
        stop_words.update(desnecessarias)

        # Converte os dados em uma string 
        text = " ".join([c.pegunta for c in relatorio_perguntas])
        image_mask = np.array(Image.open('templates/static/evento/img/Nuvem.png'))
        # Cria a nuvem de palavras
        wordcloud = WordCloud(width=800, height=800, 
                        background_color='#ffffff00',  
                        mask = image_mask,
                        colormap='Wistia',
                        stopwords=stop_words,
                        mode='RGBA',
                        min_font_size = 10).generate(text) 

        buffer = BytesIO()
        wordcloud.to_image().save(buffer, format='PNG')
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        data_uri = 'data:image/png;base64,' + image_data

        context = {
            'wordcloud_data_uri': data_uri,
        }

        return render(request, 'usuario/relatorio.html', context)




def sair(request):
    messages.add_message(request, constants.SUCCESS, 'Você saiu do portal!')
    request.session.flush()
    return redirect('/')