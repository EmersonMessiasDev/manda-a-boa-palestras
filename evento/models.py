from random import randint
import uuid
from django.db import models
import qrcode
from django.core.files.images import ImageFile
from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO
    
class Evento(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=255, blank=False, null=False)
    data = models.DateField(null=False)
    local = models.CharField(max_length=255)
    qrCode = models.ImageField(upload_to='qr_codes',blank=True, null=True)
    pin = models.CharField(max_length=5, unique=True)
           
    def __str__(self) -> str:
        return self.nome
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        if not self.pin:
            pin = randint(10000, 99999)
            self.pin = f'{pin:05d}'
            # Se o ID ainda não foi definido, salve o modelo para que o ID seja gerado pelo banco de dados.
            super().save(*args, **kwargs)
        # Define os dados para o QR code
        data = f'http://127.0.0.1:8000/faz_pergunta/{self.id}'

        # Cria o QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color='black', back_color='white')


        # Salva o QR code personalizado
        fname = f'qr_code-{self.nome}'+'.png'
        buffer = BytesIO()
        qr_img.save(buffer, 'PNG')
        self.qrCode.save(fname, File(buffer), save=False)

        super().save(*args, **kwargs)

    
    
class Palestrante(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    telefone= models.IntegerField(blank=True, null=True)
    instituicao = models.CharField(max_length=255, blank=False, null=False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nome


class Pergunta(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    palestrante = models.CharField(max_length=255, blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    pegunta = models.TextField(blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nome
