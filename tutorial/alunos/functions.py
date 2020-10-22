from django.db import models, connection
import datetime
from .models import (Materia, view_materias_usuarios, view_notasusuarios, Perguntas, view_provas_resumo, view_provas,
    AlunoMateriaNota, view_provas_resumo_history, view_provas_history, Respostas)

def deletarMateria(self, materia_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM alunos_materia where id = %s", [materia_id])
    return True

def getViewUsuariosMaterias(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_materias_usuarios")
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['id', 'usuario_id', 'username', 'materias']
    return row

def checkUsuarioMateria(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_materias_usuarios where usuario_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['id', 'usuario_id', 'username', 'materias']
    return row

def checkNotaUsuario(self, user_id, prova_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos_alunomaterianota where user_id = %s and prova_id = %s", [user_id, prova_id])
        row = dictfetchall(cursor)
        class Meta:
            model = AlunoMateriaNota
            fields = ['materia_id', 'pergunta_id', 'resposta', 'usuario']
    return row

def getNotasUsuario(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_notasusuarios")
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['user_id', 'username', 'data', 'materia', 'nota', 'nota_minima', 'nota_maxima']
    return row

def getUsuariosNota(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct user_id, username FROM view_notasusuarios")
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['user_id', 'username']
    return row

def getDatasNotas(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct date(data) data FROM view_notasusuarios")
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['data']
    return row

def getNotasUsuarioData(self, data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_notasusuarios where data = %s", [data])
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['user_id', 'username', 'data', 'materia', 'nota', 'nota_minima', 'nota_maxima']
    return row

def getNotasPorUsuario(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_notasusuarios where user_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['user_id', 'username', 'data', 'materia', 'nota', 'nota_minima', 'nota_maxima']
    return row

def checkMateriaUsuario(self, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_notasusuarios where username = %s", [username])
        row = dictfetchall(cursor)
        class Meta:
            model = view_materias_usuarios
            fields = ['user_id', 'username', 'data', 'materia', 'nota', 'nota_minima', 'nota_maxima']
    return row

def checkPesoTotalMateria(self, materia_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT sum(peso) peso FROM alunos_perguntas where materia_id = %s", [materia_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['materia_id', 'nr_pergunta', 'pergunta', 'peso']
    return row

def deletarUsuarioMateria(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM alunos_alunomateria where usuario_id = %s", [user_id])
    return True

def getNrPergunta(self, materia_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT max(nr_pergunta) nr_pergunta FROM alunos_perguntas where materia_id = %s", [materia_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['nr_pergunta']
    return row

def deletarPergunta(self, materia_id, pergunta_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM alunos_perguntas where id = %s and materia_id = %s", [pergunta_id, materia_id])
    return True

def checkPerguntaCriada(self, materia_id, aluno):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos_respostas where materia_id = %s and usuario = %s", [materia_id, aluno])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['materia_id', 'pergunta_id', 'resposta', 'usuario']
    return row

def checkPergunta(self, materia_id, pergunta_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos_respostas where materia_id = %s and pergunta_id = %s", [materia_id, pergunta_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Respostas
            fields = ['materia_id', 'pergunta_id', 'resposta', 'usuario']
    return row

def checkPesoMateria(self, materia_id, nr_pergunta):
    with connection.cursor() as cursor:
        cursor.execute("SELECT sum(peso) peso FROM alunos_perguntas where materia_id = %s and nr_pergunta <> %s", [materia_id, nr_pergunta])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['materia_id', 'nr_pergunta', 'pergunta', 'peso']
    return row

def checkPerguntaHistory(self, materia_id, pergunta_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos_respostashistory where materia_id = %s and pergunta_id = %s", [materia_id, pergunta_id])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['materia_id', 'pergunta_id', 'resposta', 'usuario']
    return row

def getUsersNota(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct user_id, usuario FROM view_provas where status = 'Finalizado'")
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo
            fields = ['user_id', 'usuario']
    return row

def getProvasResumo(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo")
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo
            fields = ['materia_id', 'nome_materia', 'qtde_perguntas', 'usuario', 'nota']
    return row

def getProvasResumoAluno(self, aluno):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo where usuario = %s and status = 'Finalizado'", [aluno])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo
            fields = ['materia_id', 'nome_materia', 'usuario', 'nota', 'prova_id']
    return row

def getProvasAluno(self, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct materia_id, nome_materia FROM view_provas where usuario = %s and status in ('Criada', 'Em Andamento')", [username])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas
            fields = ['usuario', 'materia_id', 'nome_materia', 'pergunta_id', 'nr_pergunta', 'pergunta', 'resposta']
    return row

def getProvaAluno(self, materia_id, usuario):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct materia_id, usuario, status FROM alunos_respostas where materia_id = %s and usuario = %s", [materia_id, usuario])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['materia_id', 'usuario', 'status']
    return row

def deleteProvaAluno(self, materia_id, usuario):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM alunos_respostas where materia_id = %s and usuario = %s", [materia_id, usuario])
    return True

def atualizarResposta(self, data, pergunta_id, materia_id, resposta, usuario):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE alunos_respostas set data = %s, resposta = %s, status = 'Em Andamento' where materia_id = %s and pergunta_id = %s and usuario = %s", [data, resposta, materia_id, pergunta_id, usuario])
    return True

def finalizarProva(self, materia_id, username):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE alunos_respostas set status = 'Concluído' where materia_id = %s and usuario = %s", [materia_id, username])
    return True

def atualizaCorrecaoProva(self, materia_id, pergunta_id, resultado, usuario, peso):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE alunos_respostas set nota = %s, status = 'Finalizado', resultado = %s where materia_id = %s and pergunta_id = %s and usuario = %s", [peso, resultado, materia_id, pergunta_id, usuario])
    return True

def getProvaUserID(self, materia_id, usuario):
    with connection.cursor() as cursor:
        cursor.execute("SELECT prova_id FROM view_provas_resumo where materia_id = %s and usuario = %s", [materia_id, usuario])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo
            fields = ['prova_id']
    return row

def inserirNotaUsuario(self, user_id, nome_materia, nota, aluno, prova_id):
    with connection.cursor() as cursor:
        now = datetime.datetime.now()
        data = (now.strftime("%Y-%m-%d"))
        cursor.execute("INSERT INTO alunos_alunomaterianota (user_id, materia, nota, data, username, prova_id) VALUES (%s, %s, %s, %s, %s, %s)", [user_id, nome_materia, nota, data, aluno, prova_id])
    return True

def getDataProva(self, materia_id, usuario):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct data FROM alunos_respostas where materia_id = %s and usuario = %s", [materia_id, usuario])
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['data']
    return row

def checkUsuarioNota(self, materia, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo where nome_materia = %s and user_id = %s", [materia, user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo
            fields = ['prova_id', 'usuario', 'user_id', 'materia_id', 'nome_materia', 'status', 'nota', 'qtde_perguntas']
    return row

def updateNotaUsuario(self, materia, nota, user_id, data, prova_id):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE alunos_alunomaterianota set nota = %s, data = %s where materia = %s and user_id = %s and prova_id = %s", [nota, data, materia, user_id, prova_id])
    return True

def getProvaID(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT max(prova_id) prova_id FROM alunos_respostas")
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['prova_id']
    return row

def getProvaIDHistory(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT max(prova_id) prova_id FROM alunos_respostashistory")
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['prova_id']
    return row

def getProvasHistory(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo_history order by username")
        row = dictfetchall(cursor)
        class Meta:
            model = Perguntas
            fields = ['prova_id', 'user_id', 'username', 'materia_id', 'nome_materia', 'status', 'nota', 'qtde_perguntas', 'nota_minima', 'nota_maxima']
    return row

def getProvaHistory(self, prova_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo_history where prova_id = %s", [prova_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo_history
            fields = ['prova_id', 'user_id', 'username', 'materia_id', 'nome_materia', 'status', 'nota', 'qtde_perguntas', 'nota_minima', 'nota_maxima']
    return row

def getDetalhesProva(self, prova_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_history where prova_id = %s", [prova_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_history
            fields = ['prova_id', 'user_id', 'data', 'username', 'materia_id', 'nome_materia', 'pergunta_id', 'nr_pergunta', 'pergunta', 'peso', 'resposta', 'nota', 'status', 'resultado']
    return row

def getMateriasHistory(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct materia_id, nome_materia FROM view_provas_resumo_history")
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo_history
            fields = ['materia_id', 'nome_materia']
    return row

def getProvaHistoryMateria(self, materia_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo_history where materia_id = %s", [materia_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo_history
            fields = ['prova_id', 'user_id', 'username', 'materia_id', 'nome_materia', 'status', 'nota', 'qtde_perguntas']
    return row

def getAlunosHistory(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct user_id, username FROM view_provas_history")
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_resumo_history
            fields = ['user_id', 'username']
    return row

def getProvasAlunoHistory(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM view_provas_resumo_history where user_id = %s", [user_id])
        row = dictfetchall(cursor)
        class Meta:
            model = view_provas_history
            fields = ['prova_id', 'user_id', 'username', 'materia_id', 'nome_materia', 'status', 'nota', 'qtde_perguntas']
    return row

def fazBackupProva(self, materia_id, user_id, usuario, nome_materia):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO alunos_respostashistory (prova_id, data, materia_id, pergunta_id, resposta, user_id, resultado, peso, nr_pergunta, pergunta) SELECT prova_id, data, materia_id, pergunta_id, resposta, user_id, resultado, peso, nr_pergunta, pergunta from view_provas where materia_id = %s and user_id = %s", [materia_id, user_id])
        cursor.execute("INSERT INTO alunos_provashistory (prova_id, user_id, materia_id, qtde_perguntas, status, nota) SELECT prova_id, user_id, materia_id, qtde_perguntas, status, nota FROM view_provas_resumo where materia_id = %s and user_id = %s", [materia_id, user_id])
        cursor.execute("DELETE FROM alunos_respostas WHERE materia_id = %s and usuario = %s", [materia_id, usuario])
        cursor.execute("DELETE FROM alunos_alunomaterianota WHERE materia = %s and user_id = %s", [nome_materia, user_id])
    return True

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
