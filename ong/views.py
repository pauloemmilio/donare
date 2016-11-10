from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from ong.models import Ong, Despesas
from ong.form import OngForm, DespesasForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
def index(request):
    ongs = Ong.objects.all()
    filtro = request.GET.get('q')
    message = "Pegoo"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = request.POST['username']
            senha = request.POST['password']
            user = authenticate(username = nome, password = senha)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    print("deu csssderto")
                    return redirect('index')
                else:
                    message = "Não funcionou"
            else:
                message = "erro"
        else:
            form = LoginForm()
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

def logout_page(request):
    logout(request)
    return redirect('login')
def criar_ong(request):

    form = OngForm()
    context_dict = {'form': form}
    if request.method == 'POST':
        form = OngForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            new_user = User.objects.create_user(login, password=senha)
            new_user.save()
            new_ong = form.save()
        else:
            message = "Informacoes incorretas"
       
        return redirect('ong', ong_id = new_ong.id)
    else:
        form = OngForm()
    return render(request, 'register.html', context_dict)

def login_ong(request):
    message = "Pegoo"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = request.POST['username']
            senha = request.POST['passowrd']
            user = authenticate(username = nome, password = senha)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    print("deu csssderto")
                    return redirect('index')
                else:
                    message = "Não funcionou"
            else:
                message = "erro"
        else:
            form = LoginForm()
    return render(request, 'login.html',{'message':message, 'form':form})
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
    o = Ong.objects.get(pk = ong_id)
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        despesa = Despesas(tipo=request.POST['tipo'], descricao=request.POST['descricao'], valor=request.POST['valor'], ong= o)
        despesa.save()
        # new_despesa = form.save()
        return redirect('ong', ong_id)
    else:
        form = DespesasForm()
    return render(request, 'cadastrarDespesas.html', context_dict)

def alterar_despesas(request, ong_id, despesas_id):
    template_name = 'editDespesas.html'
    despesas = Despesas.objects.get(pk = despesas_id)
    o = Ong.objects.get(pk = ong_id)
    if request.method == 'POST':
        form = DespesasForm(request.POST, instance=despesas)
        despesa = Despesas(tipo=request.POST['tipo'], descricao=request.POST['descricao'], valor=request.POST['valor'], ong= o)
        despesa.save()
        return redirect('ong', ong_id)
    else:
        form = DespesasForm(instance = despesas)
    context_dict = {'form': form, 'despesas_id': despesas_id}
    return render(request, template_name, context_dict)

def deletar_despesas(request, ong_id, despesas_id):
    despesas = Despesas.objects.get(pk = despesas_id)
    despesas.delete()
    return redirect('ong', ong_id)
