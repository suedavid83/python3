from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import datetime
from django.utils import translation
from django.conf.urls import i18n
from django.db.models import Sum
from django.utils.translation import gettext as _
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm
from .functions import (excluirProduto, getCategoriaProduto, getNomeCategoria, excluirCategoria,
    checkProdutoExiste, checkCategoriaExiste, getCategoriaId)
from principal.functions import getIdiomaSystem
from principal.models import SystemConfiguration
from pedidos.functions import getNrPedido

def homeProdutos(request):
    idioma = translation.get_language()
    produtos = Produto.objects.all()
    categorias = Categoria.objects.filter(idioma=idioma)
    context = {
        'produtos': produtos,
        'idioma': idioma,
        'categorias': categorias
    }
    return render(request, "produtos.html", context)

def filtrarCategorias(request):
    idioma = translation.get_language()
    categoria = request.POST.get("categoria")
    categorias = Categoria.objects.filter(idioma=idioma)
    produtos = Produto.objects.filter(categoria_id=categoria)
    context = {
        'produtos': produtos,
        'idioma': idioma,
        'categorias': categorias
    }
    return render(request, "produtos.html", context)

def cadastrarProduto(request):
    idioma = translation.get_language()
    idiomas = SystemConfiguration.objects.all()
    form = ProdutoForm(request.POST, request.FILES)
    categorias = Categoria.objects.filter(idioma=idioma)
    if form.is_valid():
        form.save()
        return redirect('/' + idioma + '/produtos/')
    else:
        form = ProdutoForm(request.POST, request.FILES)
        print("form is not valid")
        print(form.errors)
    context = {
        'form': form,
        'idiomas': idiomas,
        'categorias': categorias
    }
    return render(request, "cadastrarProduto.html", context)

def editarProduto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    language = produto.idioma
    idiomas = SystemConfiguration.objects.exclude(codigo=language)
    categorias = Categoria.objects.all()
    cat_produto = getCategoriaProduto(request, produto_id)
    cat_id = cat_produto[0]['categoria_id']
    categoria = getNomeCategoria(request, cat_id)
    nome_categoria = categoria[0]['nome_categoria']
    categorias = Categoria.objects.exclude(nome_categoria=nome_categoria)
    context = {
        'produto': produto,
        'idiomas': idiomas,
        'categorias': categorias,
        'nome_categoria': nome_categoria
    }
    return render(request, "editarProduto.html", context)

def salvarAlteracoesProduto(request, produto_id):
    idioma = translation.get_language()
    produto = Produto.objects.get(id=produto_id)
    codigo_produto = request.POST.get("codigo_produto")
    nome_produto = request.POST.get("nome_produto")
    descricao_produto = request.POST.get("descricao_produto")
    preco_produto = request.POST.get("preco_produto")
    status_produto = request.POST.get("status_produto")
    img_produto = request.FILES.get("img_produto")
    idioma = request.POST.get("idioma")
    categoria = request.POST.get("categoria")
    produto.codigo_produto = codigo_produto
    produto.nome_produto = nome_produto
    produto.descricao_produto = descricao_produto
    produto.status_produto = status_produto
    produto.preco_produto = preco_produto
    produto.idioma = idioma
    produto.categoria_id = categoria
    if img_produto:
        produto.img_produto = img_produto
    produto.save()
    return redirect('/produtos/')

def deleteProduto(request, produto_id):
    idioma = translation.get_language()
    excluir = excluirProduto(request, produto_id)
    return redirect('/' + idioma + '/produtos/')

def ativarProduto(request):
    idioma = translation.get_language()
    produtos = Produto.objects.filter(status_produto="inativo")
    context = {
        'produtos': produtos,
        'idioma': idioma
    }
    return render(request, "ativarProduto.html", context)

def salvarAtivarProduto(request):
    produto_id = request.POST.get("nome_produto")
    produto = Produto.objects.get(id=produto_id)
    status_produto = request.POST.get("status_produto")
    produto.status_produto = status_produto
    produto.save()
    return redirect('/produtos/')

def menuCategorias(request):
    idioma = translation.get_language()
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'idioma': idioma
    }
    return render(request, "menuCategorias.html", context)

def viewDetalhesProduto(request, produto_id):
    idioma = translation.get_language()
    produto = Produto.objects.get(id=produto_id)
    context = {
        'produto': produto,
        'idioma': idioma
    }
    return render(request, "detalhesProduto.html", context)

def viewProdutosCategoria(request, cat_id):
    idioma = translation.get_language()
    produtos = Produto.objects.filter(categoria_id=cat_id)
    context = {
        'idioma': idioma,
        'produtos': produtos
    }
    return render(request, "listProdutos.html", context)

def cadastrarCategoria(request):
    idioma = translation.get_language()
    idiomas = SystemConfiguration.objects.all()
    form = CategoriaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/' + idioma + '/produtos/menuCategorias/')
    else:
        form = CategoriaForm(request.POST, request.FILES)
        print("form is not valid")
        print(form.errors)
    context = {
        'form': form,
        'idiomas': idiomas
    }
    return render(request, "cadastrarCategoria.html", context)

def homeCategorias(request):
    idioma = translation.get_language()
    categorias = Categoria.objects.all()
    context = {
        'idioma': idioma,
        'categorias': categorias
    }
    return render(request, "categorias.html", context)

def editarCategoria(request, cat_id):
    categoria = Categoria.objects.get(id=cat_id)
    language = categoria.idioma
    idiomas = SystemConfiguration.objects.exclude(codigo=language)
    context = {
        'categoria': categoria,
        'idiomas': idiomas
    }
    return render(request, "editarCategoria.html", context)

def salvarAlteracoesCategoria(request, cat_id):
    categoria = Categoria.objects.get(id=cat_id)
    nome_categoria = request.POST.get("nome_categoria")
    descricao_categoria = request.POST.get("des_categoria")
    status_categoria = request.POST.get("status_categoria")
    img_categoria = request.FILES.get("img_categoria")
    idioma = request.POST.get("idioma")
    categoria.nome_categoria = nome_categoria
    categoria.des_categoria = descricao_categoria
    categoria.status_categoria = status_categoria
    if img_categoria:
        categoria.img_categoria = img_categoria
    categoria.idioma = idioma
    categoria.save()
    return redirect('/produtos/categorias/')

def deleteCategoria(request, cat_id):
    mensagem = ""
    idioma = translation.get_language()
    categorias = Categoria.objects.all()
    try:
        excluir = excluirCategoria(request, cat_id)
        mensagem = _("Categoria excluída com sucesso!")
    except Exception as ex:
        mensagem = _("Existem produtos associados a essa Categoria. Não é possível excluí-la")
    context = {
        'mensagem': mensagem,
        'idioma': idioma,
        'categorias': categorias
    }
    return render(request, "categorias.html", context)
