from django.db import models

# Create your models here.
class MeusPedidos(models.Model):
    nr_pedido = models.IntegerField(null=True, blank=True)
    produto_id = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    status_pedido = models.CharField(max_length=20, null=True, blank=True)
    dt_hr_insercao = models.DateTimeField(blank=True, null=True)
    dt_hr_pronto = models.DateTimeField(blank=True, null=True)
    dt_hr_entregue = models.DateTimeField(blank=True, null=True)

class PedidosHistory(models.Model):
    nr_pedido = models.IntegerField(null=True, blank=True)
    produto_id = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    status_pedido = models.CharField(max_length=20, null=True, blank=True)
    dt_hr_insercao = models.DateTimeField(blank=True, null=True)
    dt_hr_pronto = models.DateTimeField(blank=True, null=True)
    dt_hr_entregue = models.DateTimeField(blank=True, null=True)

class view_meus_pedidos(models.Model):
    nr_pedido = models.IntegerField(null=True, blank=True)
    nome_produto = models.CharField(max_length=50, null=True, blank=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status_pedido = models.CharField(max_length=20, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_meus_pedidos'

class view_pedidos_clientes(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    qtde_pedidos = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_pedidos_clientes'

class view_pedidos_detalhes(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    status_pedido = models.CharField(max_length=20, null=True, blank=True)
    qtde_pedidos = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_pedidos_detalhes'

class view_pedidoshistory(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    nr_pedido = models.IntegerField(null=True, blank=True)
    produto_id = models.IntegerField(null=True, blank=True)
    nome_produto = models.CharField(max_length=50, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status_pedido = models.CharField(max_length=20, null=True, blank=True)
    dt_pedido = models.DateField(blank=True, null=True)
    dt_hr_insercao = models.DateTimeField(blank=True, null=True)
    dt_hr_pronto = models.DateTimeField(blank=True, null=True)
    dt_hr_entregue = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_pedidoshistory'

class view_controlevendas(models.Model):
    produto_id = models.IntegerField(null=True, blank=True)
    nome_produto = models.CharField(max_length=50, null=True, blank=True)
    qtde_vendida = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_controlevendas'
