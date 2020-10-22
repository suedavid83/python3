from django.db import models, connection
from .models import view_grupos, view_user_grupo
from alunos.models import AlunoMateria, Respostas
from pedidos.models import MeusPedidos


def getAllGrupos(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_grupos")
        row = dictfetchall(cursor)
        class Meta:
            model = view_grupos
            fields = ['id_grupo', 'nome']
    return row

def getAllUsersRestaurante(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_user_grupo where nome_grupo in ('admin', 'usuario', 'cozinha', 'garcom') and username <> 'admin'")
        row = dictfetchall(cursor)
        class Meta:
            model = view_user_grupo
            fields = ['grupo_id', 'nome_grupo']
    return row

def getAllUsersEscola(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_user_grupo where nome_grupo in ('professor', 'aluno')")
        row = dictfetchall(cursor)
        class Meta:
            model = view_user_grupo
            fields = ['grupo_id', 'nome_grupo']
    return row

def getGrupos(self, grupo_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_grupos WHERE id_grupo <> %s ", [grupo_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_grupos
            fields = ['id_grupo', 'nome']
    return row

def getUserGrupo(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_user_grupo WHERE user_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_user_grupo
            fields = ['user_id', 'username', 'grupo_id', 'nome_grupo']
    return row

def associarGrupoUsuario(self, user_id, grupo_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO auth_user_groups (user_id, group_id) VALUES (%s , %s)", [user_id, grupo_id])
    return True

def deleteGrupoUsuario(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM auth_user_groups WHERE user_id = %s", [user_id])
    return True

def getAllUsers(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_user_grupo")
        row = dictfetchall(cursor)
        class Meta:
            model = view_user_grupo
            fields = ['user_id', 'username', 'grupo_id', 'nome_grupo', 'first_name', 'last_name', 'email']
    return row

def getUsuario(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_user_grupo WHERE user_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_user_grupo
            fields = ['user_id', 'username', 'grupo_id', 'nome_grupo', 'first_name', 'last_name', 'email']
    return row

def checkUserMateria(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos_alunomateria WHERE usuario_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = AlunoMateria
            fields = ['materias', 'usuario_id']
    return row

def checkUserProva(self, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos_respostas WHERE usuario = %s", [username])
        row = dictfetchall(cursor)
        class Meta:
            model = Respostas
            fields = ['materia_id', 'pergunta_id', 'resposta', 'usuario', 'status', 'resultado', 'data', 'total_peso', 'prova_id']
    return row

def checkUserPedido(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM pedidos_meuspedidos WHERE user_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = MeusPedidos
            fields = ['nr_pedido', 'produto_id', 'quantidade', 'preco_unitario', 'valor_total', 'user_id', 'status_pedido']
    return row

def removerUsuario(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM auth_user_groups where user_id = %s", [user_id])
        cursor.execute("DELETE FROM usuarios_userprofile where user_id = %s", [user_id])
        cursor.execute("DELETE FROM auth_user where id = %s", [user_id])
    return True

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
