from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from ong.models import Ong, Despesas
from ong.form import OngForm, DespesasForm

def index(request):
    return render(request, 'index.html')

def ong(request, ong_id):
    ong = Ong.objects.get(pk=ong_id)
    despesas = Despesas.objects.get(ong = ong_id)
    context_dict = {'ong': ong, 'despesas': despesas}
    return render(request, 'ongs.html', context=context_dict)

def ongs_list(request):
    ongs = Ong.objects.all()
    data = {}
    data['object_list'] = ongs
    return render(request, 'index.html', data)

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

def alterar_ong(request,ong_id):
    template_name='editOng.html'
    ong = Ong.objects.get(pk = ong_id)
    if request.method == 'POST':
        form = OngForm(request.POST, instance=ong)
        form.save()
    else:
        form = OngForm(instance=ong)
    context_dict = {'form': form, 'ong_id': ong_id}
    return render(request, template_name,context_dict)

def deletar_ong(request, ong_id):
    ong = Ong.objects.get(pk = ong_id)
    ong.delete()
    return redirect('index')


def Despesas_list(request):
    despesas = Despesas.objects.all()
    data = {}
    data['object_list'] = despesas
    return render(request, 'index.html', data)

def criar_despesas(request):

    form = DespesasForm()
    context_dict = {'form': form}

    if request.method == 'POST':
        form = DespesasForm(request.POST)

        form.save()
        return redirect('index')
    else:
        form = DespesasForm()
    return render(request, 'cadastrarDespesas.html', context_dict)

def alterar_despesas(request,despesas_id):
    template_name='editDespesas.html'
    despesas = Despesas.objects.get(pk = despesas_id)
    if request.method == 'POST':
        form = DespesasForm(request.POST, instance=despesas)
        form.save()
    else:
        form = DespesasForm(instance=despesas)
    context_dict = {'form': form, 'despesas_id': despesas_id}
    return render(request, template_name,context_dict)

def deletar_despesas(request, despesas_id):
    despesas = Despesas.objects.get(pk = despesas_id)
    despesas.delete()
    return redirect('index')
