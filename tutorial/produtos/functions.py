from django.db import models, connection
import datetime
from .models import Produto, Categoria


def excluirProduto(self, produto_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produtos_produto where id = %s", [produto_id])
    return True

def excluirCategoria(self, cat_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produtos_categoria where id = %s", [cat_id])
    return True

def checkProdutoExiste(self, nome_produto, idioma):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos_produto where nome_produto = %s and idioma = %s", [nome_produto, idioma])
        row = dictfetchall(cursor)
        class Meta:
            model = Produto
            fields = ['id', 'nome_produto', 'codigo_produto', 'descricao_produto', 'preco_produto', 'img_produto', 'status_produto', 'idioma', 'categoria_id']
    return row

def checkCategoriaExiste(self, nome_categoria, idioma):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos_categoria where nome_categoria = %s and idioma = %s", [nome_categoria, idioma])
        row = dictfetchall(cursor)
        class Meta:
            model = Produto
            fields = ['id', 'nome_categoria', 'des_categoria', 'status_categoria', 'idioma']
    return row

def getCategoriaId(self, nome_categoria):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos_categoria where nome_categoria = %s", [nome_categoria])
        row = dictfetchall(cursor)
        class Meta:
            model = Categoria
            fields = ['id']
    return row

def getNomeCategoria(self, cat_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos_categoria where id = %s", [cat_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Categoria
            fields = ['nome_categoria']
    return row

def getCategoriaProduto(self, produto_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos_produto where id = %s", [produto_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Produto
            fields = ['categoria_id']
    return row

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
