from django.shortcuts import render, HttpResponse
import requests
import sys, json
from json import dumps, loads
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .functions import checkProdutoExiste, checkCategoriaExiste, getCategoriaId
#from .models import Produto, Categoria


def recebeProdutos(request):
    data_body = request.body
    data = json.loads(data_body)
    try:
        for obj in data:
            nome_produto = obj['nome_produto']
            codigo_produto = obj['codigo_produto']
            descricao_produto = obj['descricao_produto']
            preco_produto = obj['preco_produto']
            status_produto = obj['status_produto']
            idioma = obj['idioma']
            checkProduto = checkProdutoExiste(request, nome_produto, idioma)
            if checkProduto:
                mensagem = 'Produto ' + nome_produto + ' já existe!'
            else:
                prod_instance = Produto.objects.create(nome_produto=nome_produto, codigo_produto=codigo_produto, descricao_produto=descricao_produto, preco_produto=preco_produto, status_produto=status_produto, idioma=idioma)
                mensagem = 'Produto' + nome_produto + ' incluído com sucesso!'
    except ValueError:
        mensagem = 'Arquivo JSON não é válido'
    return HttpResponse(mensagem)

@csrf_protect
def recebeJsonCompleto(request):
    mensagem = ""
    data_body = request.body
    data = json.loads(data_body)
    try:
        for obj in data['categorias']:
            nome_categoria = obj['nome_categoria']
            descricao_categoria = obj['des_categoria']
            status_categoria = obj['status_categoria']
            idioma = obj['idioma']
            checkCategoria = checkCategoriaExiste(request, nome_categoria, idioma)
            if checkCategoria:
                mensagem = mensagem + " Categoria " + nome_categoria + " já existe!"
            else:
                criarCategoria = Categoria.objects.create(nome_categoria=nome_categoria, des_categoria=descricao_categoria, status_categoria=status_categoria, idioma=idioma)
                mensagem = mensagem + " Categoria " + nome_categoria + " criada com sucesso!"
    except Exception as ex:
        mensagem = mensagem + str(ex)
    try:
        for obj in data['produtos']:
            nome_produto = obj['nome_produto']
            codigo_produto = obj['codigo_produto']
            descricao_produto = obj['descricao_produto']
            preco_produto = obj['preco_produto']
            status_produto = obj['status_produto']
            idioma = obj['idioma']
            categoria_pai = obj['categoria_pai']
            checkProduto = checkProdutoExiste(request, nome_produto, idioma)
            if checkProduto:
                print("produto ja existe")
                mensagem = mensagem + " Produto " + nome_produto + " já existe!"
            else:
                print("categoria_pai")
                print(categoria_pai)
                categoria_produto = getCategoriaId(request, categoria_pai)
                cat_id = categoria_produto[0]['id']
                print("cat_id")
                print(cat_id)
                criarProduto = Produto.objects.create(nome_produto=nome_produto, codigo_produto=codigo_produto, descricao_produto=descricao_produto, preco_produto=preco_produto, status_produto=status_produto, idioma=idioma, categoria_id=cat_id)
                mensagem = mensagem + " Produto " + nome_produto + " criado com sucesso!"
    except Exception as ex:
          mensagem = mensagem + str(ex)
    return HttpResponse(mensagem)
