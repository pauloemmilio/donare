from django.forms import ModelForm
from ong.models import Ong, Despesas

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
class DespesasForm(ModelForm):
    class Meta:
            model = Despesas
            fields = ['tipo',
            'descricao',
            'valor']