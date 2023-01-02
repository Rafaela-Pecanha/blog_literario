from django.contrib import admin
from .models import Genero


class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Genero, GeneroAdmin)
