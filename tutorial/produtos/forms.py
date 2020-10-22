from django import forms
from django.forms import ModelForm
from .models import Produto, Categoria


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'id',
            'codigo_produto',
            'nome_produto',
            'descricao_produto',
            'preco_produto',
            'status_produto',
            'img_produto',
            'idioma',
            'categoria'
        ]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome_categoria',
            'des_categoria',
            'status_categoria',
            'img_categoria',
            'idioma'
        ]
