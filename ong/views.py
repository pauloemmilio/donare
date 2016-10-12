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

class ResistrarOng(CreateView):
    model = Ong
    template_name = "index.html"
    form_class = OngForm
    success_url = reverse_lazy('ongs_list')

def ongs_list(request,template_name='index.html' ):
    ongs = Ong.objects.all()
    data = {}
    data['object_list'] = ongs
    return render(request, template_name, data)

def criar_ong(request, template_name='index.html'):
    form = OngForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core:index')
    return render(request, template_name, {'form':form})

def alterar_ong(request, pk, template_name='servers/server_form.html'):
    ongs = get_object_or_404(Server, pk=pk)
    form = OngForm(request.POST or None, instance=ong)
    if form.is_valid():
        form.save()
        return redirect('core:index')
    return render(request, template_name, {'form':form})
def deletar_ong(request, pk, template_name='inde.html'):
    ong = get_object_or_404(Ong, pk=pk)
    if request.method=='POST':
        ong.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':ong})
