from django.urls import path
from livros import views

app_name = 'livros'


urlpatterns = [
    path('', views.index, name="index"),
    path('cadastra_livro/', views.cadastra_livro, name='cadastra_livro'),
    path('exibe_livro/<int:id>/', views.exibe_livro, name='exibe_livro'),
    path('edita_livro/<int:id>/', views.edita_livro, name='edita_livro'),
    path('remove_livro/', views.remove_livro, name='remove_livro'),

]
