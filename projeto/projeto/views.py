from django.shortcuts import render

from livros.models import Livros

def index(request):
    lista_de_livros = Livros.objects.all().order_by('nome')
    return render(request, 'index.html', { 'livros': lista_de_livros })