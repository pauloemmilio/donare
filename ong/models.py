from django.db import models
from django.contrib.auth.models import User
class Ong(models.Model):
    name = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    cnpj = models.IntegerField()
    telefone = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    nomeTitular = models.CharField(max_length=200)
    fotos = models.ImageField(
        null = True,
        blank = True,
        upload_to = 'img/ong',
    )
    videoUrl = models.URLField()
    descricao = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class OngLogin(models.Model):
    ong = models.ForeignKey(Ong, null = False, blank = True, on_delete=models.CASCADE)
    user = models.OneToOneField(User)
    
class Despesas(models.Model):
    tipo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)
    valor = models.IntegerField()
    ong = models.ForeignKey(Ong)
    # def save(self, ong_id):
    #     if not self.pk :
    #        self.ong = ong_id
    #     super(Despesas , self).save()
    def __str__(self):
        return self.tipo
    def __unicode__(self):
        return self.tipo
