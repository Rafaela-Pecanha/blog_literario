from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from livros.forms import PesquisaLivroForm, LivroForm
from livros.models import Livros


def index(request):
    form = PesquisaLivroForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_livros = Livros.objects\
                                   .filter(nome__icontains=nome)\
                                   .order_by('nome')
        paginator = Paginator(lista_de_livros, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_livros)
        print(page_obj)

        return render(request, 'livros/pesquisa_livros.html', { 'livros': page_obj,
                                                                  'form': form,
                                                                  'nome': nome })
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar recuperar um livro.')


def cadastra_livro(request):

    if request.POST:
        livro_id = request.session.get('livro_id')
        print('livro_id na sessão = ' + str(livro_id))
        if livro_id:
            livro = get_object_or_404(Livros, pk=livro_id)
            livro_form = LivroForm(request.POST, request.FILES, instance=livro)
        else:
            livro_form = LivroForm(request.POST, request.FILES)

        if livro_form.is_valid():
            livro = livro_form.save(commit=False)
            livro.slug = slugify(livro.nome)
            livro.save()
            if livro_id:
                messages.add_message(request, messages.INFO, 'Livro alterado com sucesso!')
                del request.session['livro_id']
            else:
                messages.add_message(request, messages.INFO, 'Livro cadastrado com sucesso!')

            return redirect('livros:exibe_livro', id=livro.id)
    else:
        try:
            del request.session['livro_id']
        except KeyError:
            pass
        livro_form = LivroForm()

    return render(request, 'livros/cadastra_livro.html', {'form': livro_form})




def exibe_livro(request, id):
    livro = get_object_or_404(Livros, pk=id)
    request.session['livro_id_del'] = id
    
    return render(request, 'livros/exibe_livro.html', {'livros': livro})


def edita_livro(request, id):
    livro = get_object_or_404(Livros, pk=id)
    livro_form = LivroForm(instance=livro)
    request.session['livro_id'] = id
    return render(request, 'livros/cadastra_livro.html', {'form': livro_form})


def remove_livro(request):
    livro_id = request.session.get('livro_id_del')
    livro = get_object_or_404(Livros, id=livro_id)
    livro.imagem.delete()
    livro.delete()
    del request.session['livro_id_del']
    messages.add_message(request, messages.INFO, 'Livro removido com sucesso.')
    return render(request, 'livros/exibe_livro.html', {'livros': livro})

