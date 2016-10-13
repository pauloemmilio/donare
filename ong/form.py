from django.forms import ModelForm
from ong.models import Ong

class OngForm(ModelForm):
        class Meta:
            model = Ong
            fields = ['name',
            'categoria',
            'cnpj',
            'telefone',
            'email',
            'senha',
            'endereco',
            'fotos',
            'agencia',
            'conta' ,
            'nomeTitular',
            'videoUrl',
            'descricao']
