from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=30)
    nota_minima = models.FloatField(blank=True, null=True)
    nota_maxima = models.FloatField(blank=True, null=True)
    img_materia = models.FileField(upload_to='alunos/alunos.images', blank=True, null=True)

class AlunoMateria(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    materias = models.CharField(max_length=300, null=True, blank=True)

class AlunoMateriaNota(models.Model):
    prova_id = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=30, null=True, blank=True)
    materia = models.CharField(max_length=30, null=True, blank=True)
    nota = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data = models.DateField(null=True, blank=True)

class Perguntas(models.Model):
    materia_id = models.IntegerField()
    nr_pergunta = models.IntegerField()
    pergunta = models.CharField(max_length=1000, null=True, blank=True)
    peso = models.IntegerField(blank=True, null=True)

class Respostas(models.Model):
    prova_id = models.IntegerField()
    data = models.DateField(blank=True, null=True)
    materia_id = models.IntegerField()
    pergunta_id = models.IntegerField()
    resposta = models.CharField(max_length=1000, null=True, blank=True)
    usuario = models.CharField(max_length=30)
    status = models.CharField(max_length=20, null=True, blank=True, default="Criada")
    resultado = models.CharField(max_length=20, null=True, blank=True)
    nota = models.IntegerField(blank=True, null=True)

class RespostasHistory(models.Model):
    prova_id = models.IntegerField()
    data = models.DateField(blank=True, null=True)
    materia_id = models.IntegerField()
    pergunta_id = models.IntegerField()
    nr_pergunta = models.IntegerField()
    pergunta = models.CharField(max_length=1000, null=True, blank=True)
    resposta = models.CharField(max_length=1000, null=True, blank=True)
    user_id = models.IntegerField()
    resultado = models.CharField(max_length=20, null=True, blank=True)
    peso = models.IntegerField(blank=True, null=True)

class ProvasHistory(models.Model):
    prova_id = models.IntegerField()
    user_id = models.IntegerField()
    materia_id = models.IntegerField()
    qtde_perguntas = models.IntegerField()
    status = models.CharField(max_length=30)
    nota = models.IntegerField(null=True, blank=True)

class view_materias_usuarios(models.Model):
    usuario_id = models.IntegerField()
    username = models.CharField(max_length=30)
    materias = models.CharField(max_length=300)
    class Meta:
        managed = False
        db_table = 'view_materias_usuarios'

class view_notasusuarios(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=30)
    materia_id = models.IntegerField()
    data = models.DateField()
    materia = models.CharField(max_length=30)
    nota = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nota_minima = models.FloatField(blank=True, null=True)
    nota_maxima = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_notasusuarios'

class view_perguntas_materia(models.Model):
    materia_id = models.IntegerField()
    nr_pergunta = models.IntegerField()
    pergunta = models.CharField(max_length=1000, null=True, blank=True)
    nome_materia = models.CharField(max_length=30, null=True, blank=True)
    peso = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_perguntas_materia'

class view_provas(models.Model):
    prova_id = models.IntegerField()
    usuario = models.CharField(max_length=30)
    user_id = models.IntegerField()
    data = models.DateField()
    materia_id = models.IntegerField()
    nome_materia = models.CharField(max_length=30)
    pergunta_id = models.IntegerField()
    nr_pergunta = models.IntegerField()
    peso = models.IntegerField()
    pergunta = models.CharField(max_length=1000, null=True, blank=True)
    resposta = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    resultado = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_provas'

class view_provas_resumo(models.Model):
    prova_id = models.IntegerField()
    usuario = models.CharField(max_length=30)
    user_id = models.IntegerField()
    materia_id = models.IntegerField()
    nome_materia = models.CharField(max_length=30)
    qtde_perguntas = models.IntegerField()
    status = models.CharField(max_length=30)
    nota = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_provas_resumo'

class view_provas_resumo_history(models.Model):
    prova_id = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=30)
    materia_id = models.IntegerField()
    nome_materia = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    nota = models.IntegerField(null=True, blank=True)
    qtde_perguntas = models.IntegerField()
    nota_minima = models.FloatField(blank=True, null=True)
    nota_maxima = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_provas_resumo_history'

class view_provas_history(models.Model):
    prova_id = models.IntegerField()
    user_id = models.IntegerField()
    data = models.DateField()
    username = models.CharField(max_length=30)
    materia_id = models.IntegerField()
    nome_materia = models.CharField(max_length=30)
    pergunta_id = models.IntegerField()
    nr_pergunta = models.IntegerField()
    peso = models.IntegerField()
    pergunta = models.CharField(max_length=1000, null=True, blank=True)
    resposta = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=30)
    nota = models.IntegerField(null=True, blank=True)
    resultado = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'view_provas_history'
