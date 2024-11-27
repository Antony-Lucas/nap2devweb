from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    complement = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.username
    
class Encomenda(models.Model):
    remetente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    etiqueta = models.CharField(max_length=100)
    cpf_destinatario = models.CharField(max_length=14)
    endereco_saida = models.CharField(max_length=255)
    endereco_destino = models.CharField(max_length=255)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Encomenda {self.etiqueta} - {self.remetente} para {self.destinatario}"