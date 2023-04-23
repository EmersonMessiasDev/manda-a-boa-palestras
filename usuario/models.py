from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=100)
    nome =  models.CharField(max_length=100, blank=True, null=True)
    email =  models.CharField(max_length=100)
    senha = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.username