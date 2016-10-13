from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from ong.form import OngForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from ong.models import Ong
from ong.form import OngForm
##class OngForm(ModelForm):
    ##class Meta:
        ##model = Ong
        ##fields = ['nome', 'categoria', 'cnpj', 'telefone', 'email', 'senha', 'endereco', 'agencia', 'conta' ,'nomeTitular', 'fotos', 'videoUrl', 'descricao']


def index(request):
    return render(request, 'index.html')

def ong(request, ong_id):
	ong = Ong.objects.get(pk=ong_id)
	context_dict = {'ong': ong}
	return render(request, 'ongs.html', context=context_dict)


def ongs_list(request,template_name='index.html' ):
    ongs = Ong.objects.all()
    data = {}
    data['object_list'] = ongs
    return render(request, template_name, data)

def criar_ong(request):

    form = OngForm()
    context_dict = {'form': form}
    if request.method == 'POST':
        form = OngForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = OngForm()
    return render(request, 'register.html', context_dict)

def alterar_ong(request, pk):
    template_name='editOng.html'
    ong = Ong.objects.get(pk = ong_id)
    if request.method == 'POST':
        form = OngForm(request.POST, instance=ong)
        form.save()
        return HttpResponseRedirect('/ong/')
    else:
        form = OngForm(instance=ong)
    context_dict = {'form': form, 'ong_id': ong_id}
    return render(request, template_name,context_dict)

def deletar_ong(request, pk, template_name='inde.html'):
    ong = get_object_or_404(Ong, pk=pk)
    if request.method=='POST':
        ong.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':ong})
