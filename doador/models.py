from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doador(models.Model):
    name = models.CharField(max_length=300)
    dataDeNascimento = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cpf = models.IntegerField()
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class DoadorLogin(models.Model):
    doador = models.ForeignKey(Doador, null = False, blank = True, on_delete=models.CASCADE)
    user = models.OneToOneField(User)
    