from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pedidos import views

urlpatterns = [
    path('meusPedidos/', views.meusPedidos, name="meusPedidos"),
    path('pedidosCozinha/', views.pedidosCozinha, name="pedidosCozinha"),
    path('alteraStatusPedidoCozinha/<int:nr_pedido>/<int:user_id>/<slug:status>/', views.alteraStatusPedidoCozinha, name="alteraStatusPedidoCozinha"),
    path('pedidosGarcom/', views.pedidosGarcom, name="pedidosGarcom"),
    path('alteraStatusPedidoGarcom/<int:nr_pedido>/<int:user_id>/<slug:status>/', views.alteraStatusPedidoGarcom, name="alteraStatusPedidoGarcom"),
    path('fecharConta/', views.fecharConta, name="fecharConta"),
    path('imprimirPedido/<slug:username>/', views.imprimirPedido, name="imprimirPedido"),
    path('fecharContaCliente/<slug:username>/', views.fecharContaCliente, name="fecharContaCliente"),
    path('deletePedidoCliente/<int:nr_pedido>/<int:user_id>/', views.deletePedidoCliente, name="deletePedidoCliente"),
    path('verDetalhesPedidos/<slug:username>/', views.verDetalhesPedidos, name="verDetalhesPedidos"),
    path('viewPedidosHistory/', views.viewPedidosHistory, name="viewPedidosHistory"),
    path('filtrarPedidos/', views.filtrarPedidos, name="filtrarPedidos"),
    path('controleDeVendas/', views.controleDeVendas, name="controleDeVendas"),
    path('filtrarProdutos/', views.filtrarProdutos, name="filtrarProdutos"),
    path('adicionarProduto/<int:produto_id>/', views.adicionarProduto, name="adicionarProduto"),
]
