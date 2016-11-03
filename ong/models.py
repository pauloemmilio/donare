from django.db import models

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
        upload_to = 'static/img/ong',
    )
    videoUrl = models.URLField()
    descricao = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('alterar_ong', kwargs={'pk': self.pk})

class Despesas(models.Model):
    tipo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)
    valor = models.IntegerField()
    ong = models.ForeignKey(Ong)
    def __str__(self):
        return self.tipo
    def __unicode__(self):
        return self.tipo
