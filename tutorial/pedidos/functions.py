from django.db import models, connection
import datetime
from produtos.models import Produto
from .models import view_meus_pedidos, view_pedidos_clientes, view_pedidos_detalhes, view_pedidoshistory

def getNrPedido(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT max(nr_pedido) nr_pedido FROM pedidos_meuspedidos where user_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Produto
            fields = ['nr_pedido']
    return row

def getMeusPedidosUser(request, user_id, status):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nr_pedido, nome_produto, preco_unitario, quantidade, valor_total, status_pedido, user_id, username, datetime(dt_hr_insercao) dt_hr_insercao, datetime(dt_hr_pronto) dt_hr_pronto, datetime(dt_hr_entregue) dt_hr_entregue FROM view_meus_pedidos where user_id = %s and status_pedido = %s", [user_id, status])
        row = dictfetchall(cursor)
        class Meta:
            model = view_meus_pedidos
            fields = ['nr_pedido', 'nome_produto', 'preco_unitario', 'quantidade', 'valor_total', 'status_pedido', 'user_id', 'username', 'dt_hr_insercao', 'dt_hr_pronto', 'dt_hr_entregue']
    return row

def getViewPedidosCliente(self, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_meus_pedidos where username = %s", [username])
        row = dictfetchall(cursor)
        class Meta:
            model = view_meus_pedidos
            fields = ['id', 'nr_pedido', 'nome_produto', 'preco_unitario', 'quantidade', 'valor_total', 'status_pedido', 'user_id', 'username', 'dt_hr_insercao', 'dt_hr_pronto', 'dt_hr_entregue']
    return row

def getPedidosStatus(request, status):
    with connection.cursor() as cursor:
        cursor.execute("SELECT nr_pedido, nome_produto, preco_unitario, quantidade, valor_total, status_pedido, user_id, username, datetime(dt_hr_insercao) dt_hr_insercao, datetime(dt_hr_pronto) dt_hr_pronto, datetime(dt_hr_entregue) dt_hr_entregue FROM view_meus_pedidos WHERE status_pedido = %s ORDER BY dt_hr_insercao", [status])
        row = dictfetchall(cursor)
        class Meta:
            model = view_meus_pedidos
            fields = ['nr_pedido', 'nome_produto', 'preco_unitario', 'quantidade', 'valor_total', 'status_pedido', 'user_id', 'username', 'dt_hr_insercao', 'dt_hr_pronto', 'dt_hr_entregue']
    return row

def atualizaStatusPedido(self, nr_pedido, user_id, status_pedido):
    with connection.cursor() as cursor:
        now = datetime.datetime.now()
        dt_time= (now.strftime("%Y-%m-%d %H:%M:%S"))
        if status_pedido == "Pronto":
            cursor.execute("UPDATE pedidos_meuspedidos set status_pedido = %s, dt_hr_pronto = %s where nr_pedido = %s and user_id = %s", [status_pedido, dt_time, nr_pedido, user_id])
        elif status_pedido == "Entregue":
            cursor.execute("UPDATE pedidos_meuspedidos set status_pedido = %s, dt_hr_entregue = %s where nr_pedido = %s and user_id = %s", [status_pedido, dt_time, nr_pedido, user_id])
    return True

def getPedidosCliente(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_pedidos_clientes ORDER BY username")
        row = dictfetchall(cursor)
        class Meta:
            model = view_pedidos_clientes
            fields = ['username', 'user_id', 'qtde_pedidos']
    return row

def getDetalhesPedidos(self, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_pedidos_detalhes where username = %s",[username])
        row = dictfetchall(cursor)
        class Meta:
            model = view_pedidos_clientes
            fields = ['username', 'user_id', 'status_pedido', 'qtde_pedidos']
    return row

def checkPedidosPendentes(self, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(1) cont FROM view_pedidos_detalhes WHERE status_pedido <> 'Entregue' AND username = %s", [username])
        row = dictfetchall(cursor)
        class Meta:
            model = view_pedidos_detalhes
            fields = ['cont']
    return row

def excluiPedidosCliente(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM pedidos_meuspedidos where user_id = %s", [user_id])
    return True

def excluirPedidoCliente(self, nr_pedido, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM pedidos_meuspedidos where nr_pedido = %s and user_id = %s", [nr_pedido, user_id])
    return True

def fazBackupPedidos(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO pedidos_pedidoshistory (nr_pedido, produto_id, quantidade, preco_unitario, valor_total, user_id, status_pedido, dt_hr_insercao, dt_hr_pronto, dt_hr_entregue) SELECT nr_pedido, produto_id, quantidade, preco_unitario, valor_total, user_id, status_pedido, dt_hr_insercao, dt_hr_pronto, dt_hr_entregue FROM pedidos_meuspedidos where user_id = %s", [user_id])
    return True

def getDatesHistory(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct dt_pedido FROM view_pedidoshistory")
        row = dictfetchall(cursor)
        class Meta:
            model = view_pedidoshistory
            fields = ['dt_pedido']
    return row

def getPedidosHistory(self, data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, nr_pedido, nome_produto, quantidade, preco_unitario, valor_total, status_pedido, dt_pedido, datetime(dt_hr_insercao) dt_hr_insercao, datetime(dt_hr_pronto) dt_hr_pronto, datetime(dt_hr_entregue) dt_hr_entregue FROM view_pedidoshistory where dt_pedido = %s", [data])
        row = dictfetchall(cursor)
        class Meta:
            model = view_pedidoshistory
            fields = ['username', 'nr_pedido', 'nome_produto', 'quantidade', 'preco_unitario', 'valor_total', 'status_pedido', 'dt_pedido', 'dt_hr_insercao', 'dt_hr_pronto', 'dt_hr_entregue']
    return row

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
