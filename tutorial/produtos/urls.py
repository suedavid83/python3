from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produtos import views
from produtos import apis

urlpatterns = [
    path('', views.homeProdutos, name="homeProdutos"),
    path('cadastrarProduto/', views.cadastrarProduto, name="cadastrarProduto"),
    path('editarProduto/<int:produto_id>/', views.editarProduto, name="editarProduto"),
    path('salvarAlteracoesProduto/<int:produto_id>/', views.salvarAlteracoesProduto, name="salvarAlteracoesProduto"),
    path('deleteProduto/<int:produto_id>/', views.deleteProduto, name="deleteProduto"),
    path('ativarProduto/', views.ativarProduto, name="ativarProduto"),
    path('salvarAtivarProduto/', views.salvarAtivarProduto, name="salvarAtivarProduto"),
    path('menuCategorias/', views.menuCategorias, name="menuCategorias"),
    path('viewDetalhesProduto/<int:produto_id>/', views.viewDetalhesProduto, name="viewDetalhesProduto"),
    path('viewProdutosCategoria/<int:cat_id>/', views.viewProdutosCategoria, name="viewProdutosCategoria"),
    path('recebeProdutos/', apis.recebeProdutos, name="recebeProdutos"),
    path('cadastrarCategoria/', views.cadastrarCategoria, name="cadastrarCategoria"),
    path('filtrarCategorias/', views.filtrarCategorias, name="filtrarCategorias"),
    path('categorias/', views.homeCategorias, name="homeCategorias"),
    path('editarCategoria/<int:cat_id>/', views.editarCategoria, name="editarCategoria"),
    path('deleteCategoria/<int:cat_id>/', views.deleteCategoria, name="deleteCategoria"),
    path('salvarAlteracoesCategoria/<int:cat_id>/', views.salvarAlteracoesCategoria, name="salvarAlteracoesCategoria"),
    path('recebeJsonCompleto/', apis.recebeJsonCompleto, name="recebeJsonCompleto"),
]
