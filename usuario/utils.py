
import re
from django.contrib import messages
from django.contrib.messages import constants
from .models import *
from django.core.mail import EmailMultiAlternatives



def password_is_valid(request, password, confirm_password, usuario, email):

    # if len(nome.strip())  == 0:
    #     messages.add_message(request, constants.ERROR, 'Seu nome não pode ficar em branco')
    #     return False
    
    if len(usuario.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Seu usuario não pode ficar em branco')
        return False

    if len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Seu usuario não pode ficar em branco')
        return False

    if not re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]', email):
        messages.add_message(request, constants.ERROR, 'E-mail Invalido!')
        return False


    if len(password.strip()) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False

    user = Usuario.objects.filter( username=usuario)
    if user.exists():
        messages.add_message(request, constants.ERROR, 'Username  já cadastrado!')
        return False
    
    userEmail = Usuario.objects.filter( email=email)
    if userEmail.exists():
        messages.add_message(request, constants.ERROR, 'Email já cadastrado!')
        return False

    return True