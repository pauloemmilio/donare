from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from ong.models import Ong, Despesas
from ong.form import OngForm, DespesasForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    ongs = Ong.objects.all()
    filtro = request.GET.get('q')
    if filtro:
        ongs = ongs.filter(name__icontains = filtro)
        ong = ongs.filter(categoria__icontains = filtro)
    paginator = Paginator(ongs, 6)
    page = request.GET.get('page', 1)
    ongs = paginator.page(page)
    print("deu certo")
    return render(request, 'index.html',{'ongs': ongs, 'filtro': filtro })

def ong(request, ong_id):
    ong = Ong.objects.get(pk=ong_id)

    despesas = Despesas.objects.all()
    context_dict = {'ong': ong, 'despesas': despesas}
    return render(request, 'ongs.html', context=context_dict)


def ongs_list(request):
    ongs = Ong.objects.all()
    data = {}
    data['object_list'] = ongs
    return render(request, 'index.html', data)

class Busca_Ong(ListView):  
    ong = Ong.objects.all()
    context_dict = {'ong': ong}
    paginate_by = 6

    def get_queryset(self):
        result = super(Busca_Ong, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Ong(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Ong(tipo__icontains=q) for q in query_list))
            )

        return result
def criar_ong(request):

    form = OngForm()
    context_dict = {'form': form}
    if request.method == 'POST':
        form = OngForm(request.POST)
        new_ong = form.save()
        return redirect('ong', ong_id = new_ong.id)
    else:
        form = OngForm()
    return render(request, 'register.html', context_dict)

def alterar_ong(request, ong_id):
	template_name = 'editOng.html'
	ong = Ong.objects.get(pk = ong_id)
	if request.method == 'POST':
		form = OngForm(request.POST, instance=ong)
		form.save()
		return redirect('ong', ong_id = ong.id)
	else:
		form = OngForm(instance=ong)
	context_dict = {'form': form, 'ong_id': ong_id}
	return render(request, template_name, context_dict)

def deletar_ong(request, ong_id):
    ong = Ong.objects.get(pk = ong_id)
    ong.delete()
    return redirect('index')


def Despesas_list(request):
    despesas = Despesas.objects.all()
    data = {}
    data['object_list'] = despesas
    return render(request, 'index.html', data)

def criar_despesas(request, ong_id):
    form = DespesasForm()
    context_dict = {'form': form}
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        new_despesa = form.save()
        return redirect('ong', ong_id)
    else:
        form = DespesasForm()
    return render(request, 'cadastrarDespesas.html', context_dict)

def alterar_despesas(request, ong_id, despesas_id):
	template_name = 'editDespesas.html'
	despesas = Despesas.objects.get(pk = despesas_id)
	if request.method == 'POST':
		form = DespesasForm(request.POST, instance=despesas)
		new_despesa = form.save()
		return redirect('ong', ong_id)
	else:
		form = DespesasForm(instance = despesas)
	context_dict = {'form': form, 'despesas_id': despesas_id}
	return render(request, template_name, context_dict)

def deletar_despesas(request, ong_id, despesas_id):
    despesas = Despesas.objects.get(pk = despesas_id)
    despesas.delete()
    return redirect('ong', ong_id)
