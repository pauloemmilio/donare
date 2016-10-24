from django.db import models

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

    def get_absolute_url(self):
        return reverse('alterar_doador', kwargs={'pk': self.pk})
