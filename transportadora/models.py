from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.username