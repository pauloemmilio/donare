from django import forms
from ong.models import Ong, Despesas, Doacao

class OngForm(forms.ModelForm):
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
class DespesasForm(forms.ModelForm):
    class Meta:
            model = Despesas
            fields = ['tipo',
            'descricao',
            'valor',
	        'ong']

class LoginForm(forms.Form):
    
	class Meta:

		fields = [
			'username',
			'password',
		]

		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
			'password': forms.CharField(widget=forms.PasswordInput())
		}

class DoacaoForm (forms.ModelForm):
      class Meta:
            model = Doacao
            fields=['name',
            'dataDeNascimento',
            'cpf',
            'valor',
            'ong']
