
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

desnecessarias = ['a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes','desgraça', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria','seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam','bom','doque', 'do que','anão', 'arrombado', 'baba-ovo', 'babaca', 'baitola','bicha', 'bisca', 'bixa', 'boazuda', 'boceta', 'boiola', 'bolagato', 'boquete', 'bosta', 'brecha', 'brexa', 'brioco', 'buça', 'buceta', 'bunda', 'burra', 'burro', 'cachorra', 'cachorro', 'cadela', 'caga', 'cagado', 'cagão', 'cagona', 'canalha', 'caralho', 'casseta', 'cassete', 'chibumba', 'chifruda', 'chifrudo', 'chochota', 'chota', 'chupada', 'chupado', 'clitoris', 'cocaina', 'coco', 'corna', 'corno', 'cornuda', 'cornudo', 'corrupta', 'corrupto', 'cretina', 'cretino', 'cu', 'culhao', 'curalho', 'cuzão', 'cuzona', 'débil', 'debiloide', 'defunto', 'desgraçada', 'desgraçado', 'estupida', 'estupidez', 'estupido', 'favelada', 'fedida', 'fedorenta', 'feia', 'feio', 'fela-da-puta', 'fela-de-puta', 'filha da puta', 'filho da puta', 'foda', 'fodão', 'fode', 'foder', 'fudendo', 'fudeção', 'fudido', 'galinha', 'gay', 'golpista', 'idiota', 'imbecil', 'infiel', 'inútil', 'jegue', 'jerico', 'ladrão', 'lixo', 'loca', 'louca', 'louco', 'macaca', 'macaco', 'maconha', 'malandro', 'maldita', 'maldito', 'mamação', 'mamão', 'manguaça', 'mané', 'mariquinha', 'mendiga', 'merda', 'mijada', 'mijado', 'mijo', 'minhoca', 'miserável', 'molenga', 'moleque', 'mulherengo', 'negro', 'negrão', 'ninfeta', 'nojenta', 'nojento', 'otaria', 'otario', 'paspalho', 'pau', 'pau-duro', 'pau-mandado', 'pau-no-cu', 'pau-no-rabo', 'pauzudo', 'peida', 'peidão', 'peido', 'peituda', 'pencas', 'pênis', 'pentelho', 'perereca', 'periquita', 'perneta', 'piranha', 'pistoleira', 'pistoleiro', 'porcaria', 'prostituta', 'punheta', 'puta', 'putaria', 'puto', 'quenga', 'racista', 'rapariga', 'retardada', 'retardado', 'rola', 'saco', 'sapata', 'sapatão', 'sapatona', 'semen', 'sexo', 'sifilítica', 'sifilítico', 'sórdida', 'sórdido', 'tarada', 'tarado', 'testículo', 'tetuda', 'tinhoso', 'tiranete', 'trouxa', 'vaca', 'vagabunda', 'vagabundo', 'viado', 'víbora', 'xana', 'xaninha', 'xereca', 'xexéu', 'xibiu', 'xibumba', 'xota', 'xoxota', 'zoada', 'zoado', 'zona','puta merda', 'filho da puta', 'foda-se', 'caralho', 'merda', 'porra', 'cu', 'buceta', 'pinto', 'piroca', 'rola', 'xoxota', 'vai tomar no cu', 'cuzão', 'arrombado', 'viado', 'veado', 'baitola', 'bicha', 'boiola', 'gay', 'sapatao', 'traveco', 'corna', 'cornudo', 'piranha', 'vagabunda', 'vagabundo', 'galinha', 'cacete', 'punheta', 'punheteiro', 'punhetinha', 'punhetao', 'peido', 'peidar', 'mijar', 'mijo', 'bosta', 'cagão', 'cagada', 'cagar', 'porra', 'caralho','pqp', 'crlh', 'v1ado', 'v14d0', 'p044@']