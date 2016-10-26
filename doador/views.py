from doador.forms import DoadorForm
from doador.models import Doador

from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def profile(request, doador_id):
	doador = Doador.objects.get(pk=doador_id)
	context_dict = {'doador': doador}
	return render(request, 'profile.html', context=context_dict)

def cadastrar_doador(request):

    form = DoadorForm()
    context_dict = {'form': form}
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = DoadorForm()
    return render(request, 'cadastrar.html', context_dict)

def editar_doador(request,doador_id):
    template_name='editDoador.html'
    doador = Doador.objects.get(pk = doador_id)
    if request.method == 'POST':
        form = DoadorForm(request.POST, instance=doador)
        form.save()
    else:
        form = DoadorForm(instance=doador)
    context_dict = {'form': form, 'doador_id': doador_id}
    return render(request, template_name,context_dict)

def deletar_doador(request, doador_id):
    doador = Doador.objects.get(pk = doador_id)
    doador.delete()
    return redirect('index')

