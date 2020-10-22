from django.contrib import admin
from .models import Produto, Categoria


class ProdutoAdmin(admin.ModelAdmin):
    model: Produto
    list_display = ['nome_produto', 'codigo_produto', 'descricao_produto', 'preco_produto', 'img_produto']
    search_fields = ['nome_produto']
    list_filter = ['status_produto']
    save_on_top = True

class CategoriaAdmin(admin.ModelAdmin):
    model: Categoria
    list_display = ['nome_categoria', 'des_categoria', 'status_categoria', 'idioma', 'img_categoria']
    search_fields = ['nome_categoria']
    list_filter = ['status_categoria']
    save_on_top = True

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
