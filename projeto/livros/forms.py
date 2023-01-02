from django import forms
from django.core.validators import RegexValidator
from pycep_correios import get_address_from_cep, WebService, exceptions
from genero.models import Genero
from livros.models import Livros
from projeto import settings
from django.shortcuts import render, redirect, get_object_or_404
import requests


class PesquisaLivroForm(forms.Form):

    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False)


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livros
        fields = ('nome', 'genero', 'sinopse', 'imagem', 'autor', 'isbn', 'quantidade', 'cep', 'rua')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Título duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['sinopse'].error_messages={'required': 'Campo obrigatório'}
        self.fields['sinopse'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['isbn'].error_messages={'required': 'Campo obrigatório',
                                            'unique': 'Isbn duplicado.'}
        self.fields['isbn'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['autor'].error_messages={'required': 'Campo obrigatório'}
        self.fields['autor'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['quantidade'].min_value = 0
        self.fields['quantidade'].widget = forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        }) 
        self.fields['quantidade'].error_messages={'required': 'Campo obrigatório'}
   

        self.fields['cep'].error_messages={'required': 'Campo obrigatório'}
        self.fields['cep'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['rua'].error_messages={'required': 'Campo obrigatório'}
        self.fields['rua'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['genero'].error_messages={'required': 'Campo obrigatório'}
        self.fields['genero'].queryset=Genero.objects.all().order_by('nome')
        self.fields['genero'].empty_label='--- Selecione um gênero ---'
        self.fields['genero'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['imagem'].error_messages={'required': 'Campo obrigatório',
        'invalid_name': 'Imagem inválida'}
        self.fields['imagem'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})



    def clean_isbn(self):
        isbn = str(self.cleaned_data['isbn'])
        i = list(isbn)
        
        if len(isbn) != 10:
            raise forms.ValidationError("ISBN inválido!")

        _sum = 0
        for i in range(9):
            if 0 <= int(isbn[i]) <= 9:
                _sum += int(isbn[i]) * (10 - i)
            else:
                raise forms.ValidationError("ISBN inválido!")
            
        # Checar os dígitos
        if(isbn[9] != 'X' and
        0 <= int(isbn[9]) <= 9):
            raise forms.ValidationError("ISBN inválido!")
        
        # Se o último número for X então soma 10
      
        _sum += 10 if isbn[9] == 'X' else int(isbn[9])
        
        # Ver se a soma é divisível por 11
        if _sum % 11 == 0:
            return isbn
        else:
            raise forms.ValidationError("ISBN inválido!")

    