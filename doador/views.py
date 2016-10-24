from django.shortcuts import render
from django.forms import ModelForm
from doador.forms import DoadorForm

# Create your views here.

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

