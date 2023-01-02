from django.contrib import admin
from .models import Livros



class LivrosAdmin(admin.ModelAdmin):
    fields = ('genero', 'nome', 'slug', 'imagem', 'sinopse')
    list_display = ['nome', 'slug', 'genero', 'imagem', 'sinopse']
    search_fields = ['nome', 'imagem']
    list_filter = ['genero']
    list_editable = ['genero', 'imagem', 'sinopse']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Livros, LivrosAdmin)