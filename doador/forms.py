from django.forms import ModelForm
from doador.models import Doador

class DoadorForm(ModelForm):
        class Meta:
            model = Doador
            fields = ['name',
            'dataDeNascimento',
            'email',
            'senha',
            'cpf']
