from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ong(request):
	return render(request, 'ongs.html')

def editOng(request):
	return render(request, 'editOng.html')
