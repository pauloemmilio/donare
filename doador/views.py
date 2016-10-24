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
