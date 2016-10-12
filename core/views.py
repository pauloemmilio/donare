from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    context_dict = {'nome_do_prato': "Pizza de Pepperoni"}
    return render(request, 'index.html', context=context_dict)

def ong(request):
	return render(request, 'projects.html')
