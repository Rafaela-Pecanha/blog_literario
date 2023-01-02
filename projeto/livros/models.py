from django.db import models
from genero.models import Genero

class Livros(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    autor = models.CharField(max_length=70)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=70)
    isbn = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70)
    imagem = models.ImageField(upload_to='images/')
    sinopse = models.CharField(max_length=1500)
    quantidade = models.IntegerField()

    class Meta:
        db_table='livros'
    
    def __str__(self):
        return self.nome