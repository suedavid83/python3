from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):

    STATUS_CAT = (
        (u'ativa', u'Ativa'),
        (u'inativa', u'Inativa'),
    )
    SIGLA_IDIOMA = (
        (u'pt', u'pt'),
        (u'en', u'en'),
    )

    nome_categoria = models.CharField(max_length=30)
    des_categoria = models.CharField(max_length=50, blank=True, null=True)
    img_categoria = models.FileField(upload_to='produtos/produtos.images', blank=True, null=True)
    status_categoria = models.CharField(choices=STATUS_CAT, max_length=10, default=0)
    idioma = models.CharField(choices=SIGLA_IDIOMA, max_length=10)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    STATUS_PROD = (
        (u'ativo', u'Ativo'),
        (u'inativo', u'Inativo'),
    )
    SIGLA_IDIOMA = (
        (u'pt', u'pt'),
        (u'en', u'en'),
    )

    nome_produto = models.CharField(max_length=50)
    codigo_produto = models.CharField(max_length=10, blank=True)
    descricao_produto = models.CharField(max_length=200, null=True, blank=True)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img_produto = models.FileField(upload_to='produtos.images/', blank=True)
    status_produto = models.CharField(choices=STATUS_PROD, max_length=10, default=0)
    idioma = models.CharField(choices=SIGLA_IDIOMA, max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
