from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import datetime
from django.utils import translation
from django.conf.urls import i18n
from django.db.models import Sum
from django.utils.translation import gettext as _
from .models import view_meus_pedidos, view_controlevendas, MeusPedidos
from .functions import (getMeusPedidosUser, atualizaStatusPedido, getPedidosStatus, getPedidosCliente,
    getViewPedidosCliente, checkPedidosPendentes, excluiPedidosCliente, excluirPedidoCliente, getDetalhesPedidos, fazBackupPedidos,
    getDatesHistory, getPedidosHistory, getNrPedido)
from produtos.models import Produto

# Create your views here.
def meusPedidos(request):
    user_id = request.user.id
    meusPedidosPendentes = getMeusPedidosUser(request, user_id, "Pendente")
    meusPedidosProntos = getMeusPedidosUser(request, user_id, "Pronto")
    meusPedidosEntregues = getMeusPedidosUser(request, user_id, "Entregue")
    context = {
        'meusPedidosPendentes': meusPedidosPendentes,
        'meusPedidosProntos': meusPedidosProntos,
        'meusPedidosEntregues': meusPedidosEntregues
    }
    return render(request, "meusPedidos.html", context)

def adicionarProduto(request, produto_id):
    user_id = request.user.id
    produto = Produto.objects.get(id=produto_id)
    quantidade = request.POST.get("quantidade")
    valor_total = int(quantidade) * float(produto.preco_produto)
    now = datetime.datetime.now()
    dt_time= (now.strftime("%Y-%m-%d %H:%M:%S"))
    nr_pedido = getNrPedido(request, user_id)
    nr_pedido = nr_pedido[0]['nr_pedido']
    if nr_pedido:
        nr_pedido = nr_pedido + 1
    else:
        nr_pedido = 1
    criarPedido = MeusPedidos.objects.create(nr_pedido=nr_pedido, produto_id=produto.id, quantidade=quantidade, preco_unitario=produto.preco_produto, valor_total=valor_total, user_id=user_id, status_pedido="Pendente", dt_hr_insercao=dt_time)
    return redirect('/produtos/menuCategorias/')

def pedidosCozinha(request):
    pedidosPendentes = getPedidosStatus(request, 'Pendente')
    pedidosProntos = getPedidosStatus(request, 'Pronto')
    context = {
        'pedidosPendentes': pedidosPendentes,
        'pedidosProntos': pedidosProntos
    }
    return render(request, "cozinha.html", context)

def alteraStatusPedidoCozinha(request, nr_pedido, user_id, status):
    atualiza = atualizaStatusPedido(request, nr_pedido, user_id, status)
    pedidosPendentes = getPedidosStatus(request, 'Pendente')
    pedidosProntos = getPedidosStatus(request, 'Pronto')
    context = {
        'pedidosPendentes': pedidosPendentes,
        'pedidosProntos': pedidosProntos
    }
    return render(request, "cozinha.html", context)

def alteraStatusPedidoGarcom(request, nr_pedido, user_id, status):
    atualiza = atualizaStatusPedido(request, nr_pedido, user_id, status)
    pedidosProntos = getPedidosStatus(request, 'Pronto')
    pedidosEntregues = getPedidosStatus(request, 'Entregue')
    context = {
        'pedidosProntos': pedidosProntos,
        'pedidosEntregues': pedidosEntregues
    }
    return render(request, "garcom.html", context)

def pedidosGarcom(request):
    pedidosProntos = getPedidosStatus(request, 'Pronto')
    pedidosEntregues = getPedidosStatus(request, 'Entregue')
    context = {
        'pedidosProntos': pedidosProntos,
        'pedidosEntregues': pedidosEntregues
    }
    return render(request, "garcom.html", context)

def fecharConta(request):
    pedidos = getPedidosCliente(request)
    context = {
        'pedidos': pedidos,
    }
    return render(request, "fecharConta.html", context)

def imprimirPedido(request, username):
    viewPedidos = getViewPedidosCliente(request, username)
    totalProdutos = view_meus_pedidos.objects.filter(username=username).aggregate(Sum('valor_total')).get('valor_total__sum', 0.00)
    context = {
        'viewPedidos': viewPedidos,
        'username': username,
        'totalProdutos': totalProdutos
    }
    return render(request, "imprimirPedidosCliente.html", context)

def fecharContaCliente(request, username):
    mensagem = ""
    pedidosPendentes = checkPedidosPendentes(request, username)
    cont = pedidosPendentes[0]['cont']
    if cont > 0:
        mensagem = _("Existem Pedidos Pendentes, não é possível fechar a conta")
    else:
        usuario = User.objects.get(username=username)
        user_id = usuario.id
        backup = fazBackupPedidos(request, user_id)
        excluiPedidos = excluiPedidosCliente(request, user_id)
        mensagem = _("Conta Fechada com sucesso!")
    pedidos = getPedidosCliente(request)
    context = {
        'pedidos': pedidos,
        'mensagem': mensagem,
    }
    return render(request, "fecharConta.html", context)

def deletePedidoCliente(request, nr_pedido, user_id):
    excluirPedido = excluirPedidoCliente(request, nr_pedido, user_id)
    mensagem = _("Pedido excluído com sucesso!")
    meusPedidosPendentes = getMeusPedidosUser(request, user_id, "Pendente")
    meusPedidosProntos = getMeusPedidosUser(request, user_id, "Pronto")
    meusPedidosEntregues = getMeusPedidosUser(request, user_id, "Entregue")
    context = {
        'meusPedidosPendentes': meusPedidosPendentes,
        'meusPedidosProntos': meusPedidosProntos,
        'meusPedidosEntregues': meusPedidosEntregues,
        'mensagem': mensagem
    }
    return render(request, "meusPedidos.html", context)

def verDetalhesPedidos(request, username):
    pedidos = getPedidosCliente(request)
    detalhesPedidos = getDetalhesPedidos(request, username)
    lista_pedidos = []
    for det in detalhesPedidos:
        lista_pedidos.append("Pedidos: " + det['status_pedido'])
        lista_pedidos.append(det['qtde_pedidos'])
    context = {
        'pedidos': pedidos,
        'lista_pedidos': lista_pedidos,
        'username': username
    }
    return render(request, "detalhesConta.html", context)

def viewPedidosHistory(request):
    dates = getDatesHistory(request)
    context = {
        'dates': dates
    }
    return render(request, "pedidosHistory.html", context)

def filtrarPedidos(request):
    dates = getDatesHistory(request)
    data = request.POST.get("data")
    pedidos = getPedidosHistory(request, data)
    context = {
        'dates': dates,
        'pedidos': pedidos
    }
    return render(request, "pedidosHistory.html", context)

def controleDeVendas(request):
    produtos = view_controlevendas.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, "controleVendas.html", context)

def filtrarProdutos(request):
    nome_produto = request.POST.get("nome_produto")
    produtos = view_controlevendas.objects.filter(nome_produto__contains=nome_produto)
    context = {
        'produtos': produtos
    }
    return render(request, "controleVendas.html", context)
