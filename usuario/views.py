from django.shortcuts import render, redirect
from .utils import password_is_valid
from django.contrib import messages
from django.contrib.messages import constants
from hashlib import sha256
from .models import Usuario

# Create your views here.

def area_palestrante(request):
    return render(request, 'usuario/login.html')

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

            
 
def validar_login(request):
    pass      
        