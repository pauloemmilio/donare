from django.contrib.auth.forms import UserCreationForm
from ong.models import Ong

class OngForm(UserCreationForm):
        class Meta:
            model = Ong.objects.all()
            fields = ['nome',
            'categoria',
            'cnpj',
            'telefone',
            'email',
            'senha',
            'endereco',
            'agencia',
            'conta' ,
            'nomeTitular',
            'fotos',
            'videoUrl',
            'descricao']
        
