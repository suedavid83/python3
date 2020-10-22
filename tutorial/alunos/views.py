from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext as _
from .forms import MateriaForm
from .models import (Materia, AlunoMateria, AlunoMateriaNota, view_materias_usuarios, view_notasusuarios, Perguntas,
    view_perguntas_materia, Respostas, view_provas)
from .functions import (deletarMateria, getViewUsuariosMaterias, checkUsuarioMateria, getNotasUsuario,
    getDatasNotas, getNotasUsuarioData, getUsuariosNota, getNotasPorUsuario, checkMateriaUsuario, deletarUsuarioMateria,
    getNrPergunta, deletarPergunta, checkPerguntaCriada, deleteProvaAluno, getProvaAluno, getProvasResumo, getProvasAluno,
    atualizarResposta, finalizarProva, atualizaCorrecaoProva, getDataProva, getProvasResumoAluno, checkUsuarioNota,
    updateNotaUsuario, fazBackupProva, getProvaID, getProvasHistory, getProvaHistory, getDetalhesProva, getProvaIDHistory,
    checkPergunta, checkPerguntaHistory, checkPesoMateria, getMateriasHistory, getAlunosHistory, getProvaHistoryMateria,
    getProvasAlunoHistory, getUsersNota, inserirNotaUsuario, getProvaUserID, checkPesoTotalMateria, checkNotaUsuario)
from usuarios.models import view_user_grupo
from decimal import Decimal
import decimal

# Create your views here

def homeMaterias(request):
    materias = Materia.objects.all()
    context = {
        'materias': materias
    }
    return render(request, "homeMaterias.html", context)

def viewMateriasUsuario(request, materia_id):
    pass

def cadastrarMateria(request):
    mensagem = ""
    form = MateriaForm(request.POST)
    nome = request.POST.get("nome")
    nota_minima = request.POST.get("nota_minima")
    nota_maxima = request.POST.get("nota_maxima")
    img_materia = request.FILES.get("img_materia")
    materias = Materia.objects.all()
    if form.is_valid():
        materia = form.save(commit=False)
        materia.nome = nome
        materia.nota_minima = nota_minima
        materia.nota_maxima = nota_maxima
        if img_materia:
            materia.img_materia = img_materia
        materia.save()
        mensagem = _("Matéria cadastrada com sucesso!")
        context = {
            'mensagem': mensagem,
            'materias': materias
        }
        return render(request, "alterarMateria.html", context)
    else:
        print('form is not valid')
        print(form.errors)
    context = {
        'form': form
    }
    return render(request, "materias.html", context)

def alterarMateria(request):
    materias = Materia.objects.all()
    context = {
        'materias': materias
    }
    return render(request, "alterarMateria.html", context)

def editarMateria(request, materia_id):
    materia = Materia.objects.get(id=materia_id)
    context = {
        'materia': materia
    }
    return render(request, "editarMateria.html", context)

def salvarAlteracoesMateria(request, materia_id):
    materia = Materia.objects.get(id=materia_id)
    nome = request.POST.get("nome")
    nota_minima = request.POST.get("nota_minima")
    nota_maxima = request.POST.get("nota_maxima")
    img_materia = request.POST.get("img_materia")
    materia = Materia.objects.get(id=materia_id)
    materia.nome = nome
    materia.nota_minima = nota_minima
    materia.nota_maxima = nota_maxima
    if img_materia:
        materia.img_materia = img_materia
    materia.save()
    materias = Materia.objects.all()
    context = {
        'materia': materia,
        'materias': materias
    }
    return render(request, "alterarMateria.html", context)


def deleteMateria(request, materia_id):
    mensagem = ""
    materia = Materia.objects.get(id=materia_id)
    nome_materia = materia.nome
    userMaterias = AlunoMateria.objects.all()
    materias = Materia.objects.all()
    delete = True
    for mat in userMaterias:
        if nome_materia in mat.materias:
            mensagem = _("Não é possível excluir matéria pois a mesma está associada a um ou mais usuários")
            delete = False
            context = {
                'materias': materias,
                'mensagem': mensagem
            }
            return render(request, "alterarMateria.html", context)
    if delete == True:
        deletar = deletarMateria(request, materia_id)
        mensagem = _("Matéria deletada com sucesso!")
    context = {
        'materias': materias,
        'mensagem': mensagem
    }
    return render(request, "alterarMateria.html", context)

def usuariosMaterias(request):
    usuarios = view_user_grupo.objects.filter(nome_grupo='usuario')
    materias = Materia.objects.all()
    context = {
        'usuarios': usuarios,
        'materias': materias
    }
    return render(request, "usuariosMaterias.html", context)

def salvarUsuariosMaterias(request):
    user_id = request.POST.get("usuario")
    usuario = User.objects.get(id=user_id)
    materias = request.POST.getlist("materias")
    checkUsuario = checkUsuarioMateria(request, user_id)
    if checkUsuario:
        mensagem = _("Usuário ja cadastrado!")
        viewMateriasUsuario = getViewUsuariosMaterias(request)
        context = {
            'mensagem': mensagem,
            'viewMateriasUsuario': viewMateriasUsuario,
        }
        return render(request, "listarUsuariosMaterias.html", context)
    else:
        lista_materias = []
        for mat in materias:
            materia = Materia.objects.get(id=mat)
            lista_materias.append(materia.nome)
        criarUsuarioMateria = AlunoMateria.objects.create(usuario=usuario, materias=lista_materias)
        mensagem = _("Usuário cadastrado com sucesso!")
        context = {
            'mensagem': mensagem
        }
        return render(request, "index.html", context)

def listarUsuariosMaterias(request):
    viewMateriasUsuario = getViewUsuariosMaterias(request)
    context = {
        'viewMateriasUsuario': viewMateriasUsuario,
    }
    return render(request, "listarUsuariosMaterias.html", context)

def deleteUsuarioMateria(request, username):
    mensagem = ""
    checkUser = checkMateriaUsuario(request, username)
    if checkUser:
        mensagem = _("Nao é possível excluir usuário pois o mesmo possui notas associadas a ele!")
    else:
        usuario = User.objects.get(username=username)
        user_id = usuario.id
        delete = deletarUsuarioMateria(request, user_id)
        mensagem = _("Usuário deletado com sucesso!")
    viewMateriasUsuario = getViewUsuariosMaterias(request)
    context = {
        'viewMateriasUsuario': viewMateriasUsuario,
        'mensagem': mensagem
    }
    return render(request, "listarUsuariosMaterias.html", context)

def viewNotasUsuarios(request):
    viewNotas = getNotasUsuario(request)
    datas = getDatasNotas(request)
    usuarios = getUsuariosNota(request)
    materias = Materia.objects.all()
    context = {
        'viewNotas': viewNotas,
        'datas': datas,
        'usuarios': usuarios,
        'materias': materias
    }
    return render(request, "viewNotasUsuarios.html", context)

def filtrarNotasUsuarioData(request):
    data = request.POST.get("data")
    usuarios = getUsuariosNota(request)
    datas = getDatasNotas(request)
    if not data:
        viewNotas = getNotasUsuario(request)
    else:
        viewNotas = getNotasUsuarioData(request, data)
    context = {
        'viewNotas': viewNotas,
        'datas': datas,
        'usuarios': usuarios
    }
    return render(request, "viewNotasUsuarios.html", context)

def filtrarNotasUsuario(request):
    usuario = request.POST.get("user")
    usuarios = getUsuariosNota(request)
    datas = getDatasNotas(request)
    if not usuario:
        viewNotas = getNotasUsuario(request)
    else:
        viewNotas = getNotasPorUsuario(request, usuario)
    context = {
        'viewNotas': viewNotas,
        'datas': datas,
        'usuarios': usuarios
    }
    return render(request, "viewNotasUsuarios.html", context)

def listarMateriasNotas(request):
    data = request.POST.get("data")
    user_id = request.POST.get("usuario")
    user = User.objects.get(id=user_id)
    username = user.username
    respostas = getProvasResumoAluno(request, username)
    context = {
        'respostas': respostas,
        'data': data
    }
    return render(request, "viewAlunoProva.html", context)

def salvarNotaUsuario(request, data, aluno, prova_id):
    usuario = User.objects.get(username=aluno)
    user_id = usuario.id
    materias = request.POST.getlist("materia")
    notas = request.POST.getlist("nota")
    lista_materias = []
    lista_notas = []
    index = 0
    for nota in notas:
        lista_notas.append(nota)
    for materia in materias:
        lista_materias.append(materia)
    index = 0
    for materia in lista_materias:
        nota = lista_notas[index]
        check = checkUsuarioNota(request, materia, user_id)
        if not check:
            create = AlunoMateriaNota.objects.create(prova_id=prova_id, materia=materia, nota=nota, user_id=user_id, data=data, username=usuario)
        else:
            update = updateNotaUsuario(request, materia, nota, user_id, data, prova_id)
        index = index + 1
    mensagem = _("Nota incluída com sucesso!")
    context = {
        'mensagem': mensagem
    }
    return render(request, "index.html", context)

def editarMateriaUsuario(request, username):
    usuario = User.objects.get(username=username)
    user_id = usuario.id
    materias = Materia.objects.all()
    materias_user = view_materias_usuarios.objects.get(username=username)
    lista_materias = materias_user.materias
    context = {
        'username': username,
        'user_id': user_id,
        'lista_materias': lista_materias,
        'materias': materias
    }
    return render(request, "editarMateriaUsuario.html", context)

def salvarUserMaterias(request, username):
    materias = request.POST.getlist("materias")
    usuario = User.objects.get(username=username)
    user_id = usuario.id
    lista_users = []
    for mat in materias:
        materia = Materia.objects.get(id=mat)
        lista_users.append(materia.nome)
    delete = deletarUsuarioMateria(request, user_id)
    criarUsuarioMateria = AlunoMateria.objects.create(usuario=usuario, materias=lista_users)
    viewMateriasUsuario = getViewUsuariosMaterias(request)
    context = {
        'viewMateriasUsuario': viewMateriasUsuario
    }
    return render(request, "listarUsuariosMaterias.html", context)

def viewMateriasUsuario(request, materia_id):
    user_id = request.user.id
    materia = Materia.objects.get(id=materia_id)
    viewUsuariosNotas = view_notasusuarios.objects.filter(user_id=user_id, materia_id=materia_id)
    context = {
        'viewUsuariosNotas': viewUsuariosNotas,
        'materia': materia
    }
    return render(request, "verNotasUsuarioMateria.html", context)

def criarPergunta(request):
    materias = Materia.objects.all()
    context = {
        'materias': materias
    }
    return render(request, "criarPergunta.html", context)

def inserirPergunta(request):
    mensagem = ""
    materias = Materia.objects.all()
    materia_id = request.POST.get("materia")
    materia = Materia.objects.get(id=materia_id)
    nome_materia = materia.nome
    pergunta = request.POST.get("pergunta")
    peso = request.POST.get("peso")
    numero_pergunta = getNrPergunta(request, materia_id)
    if numero_pergunta[0]['nr_pergunta'] == None:
        numero_pergunta = 1
    else:
        numero_pergunta = numero_pergunta[0]['nr_pergunta'] + 1
    checkPeso = checkPesoMateria(request, materia_id, numero_pergunta)
    if checkPeso[0]['peso'] == None:
        checkPeso = 0
    else:
        checkPeso = checkPeso[0]['peso']
    if int(peso) + int(checkPeso) > 10:
        mensagem = _("Este peso não pode ser utilizado pois ultrapassa o limite de 10")
        context = {
            'materias': materias,
            'mensagem': mensagem,
            'materia_id': materia_id,
            'nome_materia': nome_materia,
            'pergunta': pergunta,
            'peso': peso,
        }
        return render(request, "criarPergunta.html", context)
    else:
        criar = Perguntas.objects.create(pergunta=pergunta, materia_id=materia_id, nr_pergunta=numero_pergunta, peso=peso)
    context = {
        'materias': materias,
        'mensagem': mensagem
    }
    return render(request, "index.html")

def listarPerguntasMateria(request):
    materias = Materia.objects.all()
    context = {
        'materias': materias
    }
    return render(request, "listarPerguntasMateria.html", context)

def listarPerguntas(request):
    materias = Materia.objects.all()
    materia_id = request.POST.get("materia")
    perguntas = Perguntas.objects.filter(materia_id=materia_id)
    context = {
        'materias': materias,
        'perguntas': perguntas
    }
    return render(request, "listarPerguntasMateria.html", context)

def editarPergunta(request, pergunta_id):
    materia = view_perguntas_materia.objects.get(id=pergunta_id)
    nome_materia = materia.nome_materia
    context = {
        'nome_materia': nome_materia,
        'materia': materia
    }
    return render(request, "editarPergunta.html", context)

def salvarAlteracoesPergunta(request, pergunta_id):
    materias = Materia.objects.all()
    pergunta = Perguntas.objects.get(id=pergunta_id)
    materia_id = pergunta.materia_id
    materia = view_perguntas_materia.objects.get(id=pergunta_id)
    nome_materia = materia.nome_materia
    nr_pergunta = request.POST.get("nr_pergunta")
    pergunta = request.POST.get("pergunta")
    peso = request.POST.get("peso")
    objeto = Perguntas.objects.get(id=pergunta_id)
    checkPeso = checkPesoMateria(request, materia_id, nr_pergunta)
    checkPeso = checkPeso[0]['peso']
    if int(peso) + int(checkPeso) > 10:
        mensagem = _("Este peso não pode ser utilizado pois ultrapassa o limite de 10")
        context = {
            'materias': materias,
            'mensagem': mensagem,
            'materia': materia,
            'nome_materia': nome_materia,
            'pergunta': pergunta,
            'peso': peso,
        }
        return render(request, "editarPergunta.html", context)
    else:
        objeto.nr_pergunta = nr_pergunta
        objeto.pergunta = pergunta
        objeto.peso = peso
        objeto.save()
        mensagem = _("Pergunta alterada com sucesso!")
        context = {
            'mensagem': mensagem,
            'materias': materias
        }
    return render(request, "listarPerguntasMateria.html", context)


def deletePergunta(request, materia_id, pergunta_id):
    check = checkPergunta(request, materia_id, pergunta_id)
    if check == []:
        deletar = deletarPergunta(request, materia_id, pergunta_id)
        mensagem = _("Pergunta deletada com sucesso!")
    else:
        mensagem = _("Pergunta não pode ser deletada pois a mesma está associada a uma prova!")
    materias = Materia.objects.all()
    context = {
        'mensagem': mensagem,
        'materias': materias
    }
    return render(request, "listarPerguntasMateria.html", context)

def listarMateriasProva(request):
    materias = Materia.objects.all()
    context = {
        'materias': materias
    }
    return render(request, "listarMateriasProva.html", context)

def listarAlunosMateria(request):
    mensagem = ""
    materias = Materia.objects.all()
    materia = request.POST.get("materia")
    alunos = "Alunos:"
    list_alunos = []
    if not materia:
        mensagem = _("Selecione uma matéria")
    else:
        materias_user = view_materias_usuarios.objects.all()
        nome_materia = Materia.objects.get(id=materia)
        nome_materia = nome_materia.nome
        for user in materias_user:
            if nome_materia in user.materias:
                list_alunos.append(user.username)
    context = {
        'materias': materias,
        'list_alunos': list_alunos,
        'alunos': alunos,
        'mensagem': mensagem,
        'nome_materia': nome_materia
    }
    return render(request, "agendarProva.html", context)

def criarProva(request):
    materias = Materia.objects.all()
    nome_materia = request.POST.get("nome_materia")
    materia = Materia.objects.get(nome=nome_materia)
    materia_id = materia.id
    alunos = request.POST.getlist("aluno")
    for aluno in alunos:
        perguntas = Perguntas.objects.filter(materia_id=materia_id)
        if not perguntas:
            mensagem = _("Não existem perguntas criadas para essa matéria")
            context = {
                'mensagem': mensagem,
                'materias': materias
            }
            return render(request, "listarMateriasProva.html", context)
        else:
            check = checkPerguntaCriada(request, materia_id, aluno)
            if check:
                mensagem = _("Já existe prova criada para esse aluno nessa matéria")
                context = {
                    'mensagem': mensagem,
                    'materias': materias
                }
                return render(request, "listarMateriasProva.html", context)
            else:
                check2 = checkPesoTotalMateria(request, materia_id)
                if check2[0]['peso'] < 10 or check2 == []:
                    mensagem = _("O peso total das perguntas dessa matéria é menor do que 10. Não é possível criar prova!")
                    context = {
                        'mensagem': mensagem,
                        'materias': materias
                    }
                    return render(request, "listarMateriasProva.html", context)
                else:
                    prova_id = getProvaID(request)
                    if prova_id[0]['prova_id'] == None:
                        prova_id = getProvaIDHistory(request)
                        if prova_id[0]['prova_id'] == None:
                            prova_id = 1
                        else:
                            prova_id = int(prova_id[0]['prova_id']) + 1
                    else:
                        prova_id = int(prova_id[0]['prova_id']) + 1
                    for pergunta in perguntas:
                        criarItemResposta = Respostas.objects.create(prova_id=prova_id, materia_id=materia_id, pergunta_id=pergunta.id, usuario=aluno)
    return render(request, "index.html")

def viewProvasAlunos(request):
    respostas = getProvasResumo(request)
    context = {
        'respostas': respostas
    }
    return render(request, "viewProvasAlunos.html", context)

def deleteProva(request, materia_id, usuario):
    mensagem = ""
    prova = getProvaAluno(request, materia_id=materia_id, usuario=usuario)
    if prova[0]['status'] == "Criada":
        delete = deleteProvaAluno(request, materia_id, usuario)
        mensagem = _("Prova excluída com sucesso!")
    else:
        mensagem = _("Não é possível excluir prova pois a mesma já foi iniciada")
    respostas = getProvasResumo(request)
    context = {
        'respostas': respostas,
        'mensagem': mensagem
    }
    return render(request, "viewProvasAlunos.html", context)

def inicioProvaAluno(request):
    username = request.user.username
    materias = getProvasAluno(request, username)
    context = {
        'materias': materias
    }
    return render(request, "inicioProvaAluno.html", context)


def listarPerguntasProva(request):
    now = datetime.datetime.now()
    data = (now.strftime("%Y-%m-%d"))
    username = request.user.username
    materia_id = request.POST.get("materia")
    materia = Materia.objects.get(id=materia_id)
    nome_materia = materia.nome
    respostas = view_provas.objects.filter(usuario=username, materia_id=materia_id)
    context = {
        'respostas': respostas,
        'nome_materia': nome_materia,
        'data': data
    }
    return render(request, "listarPerguntasProva.html", context)

def salvarProva(request):
    username = request.user.username
    materias = getProvasAluno(request, username)
    materia = request.POST.get("materia")
    data = request.POST.get("data")
    materia_id = Materia.objects.get(nome=materia)
    materia_id = materia_id.id
    nr_pergunta = request.POST.getlist("nr_pergunta")
    resposta = request.POST.getlist("resposta")
    lista_nrpergunta = []
    lista_respostas = []
    for numero_pergunta in nr_pergunta:
        lista_nrpergunta.append(numero_pergunta)
    for res in resposta:
        lista_respostas.append(res)
    index = 0
    for lista in lista_nrpergunta:
        perguntas = Perguntas.objects.get(nr_pergunta=lista, materia_id=materia_id)
        pergunta_id = perguntas.id
        resposta = lista_respostas[index]
        index = index + 1
        incluirResposta = atualizarResposta(request, data, pergunta_id, materia_id, resposta, username)
    context = {
        'materias': materias
    }
    return render(request, "inicioProvaAluno.html", context)

def concluirProva(request, nome_materia):
    username = request.user.username
    materia = Materia.objects.get(nome=nome_materia)
    materia_id = materia.id
    concluirProva = finalizarProva(request, materia_id, username)
    materias = getProvasAluno(request, username)
    context = {
        'materias': materias
    }
    return render(request, "inicioProvaAluno.html", context)

def verProvaAluno(request, materia_id, usuario):
    materia = Materia.objects.get(id=materia_id)
    nome_materia = materia.nome
    aluno = usuario
    prova = getDataProva(request, materia_id, usuario)
    data = prova[0]['data']
    provas = view_provas.objects.filter(materia_id=materia_id, usuario=usuario)
    context = {
        'aluno': aluno,
        'nome_materia': nome_materia,
        'provas': provas,
        'data': data
    }
    return render(request, "viewProvaAlunoMateria.html", context)

def salvarCorrecoes(request):
    mensagem = ""
    aluno = request.POST.get("aluno")
    user = User.objects.get(username=aluno)
    user_id = user.id
    nome_materia = request.POST.get("materia")
    materia = Materia.objects.get(nome=nome_materia)
    materia_id = materia.id
    nr_pergunta = request.POST.getlist("nr_pergunta")
    resultado = request.POST.getlist("resultado")
    data = request.POST.get("data")
    provas = view_provas.objects.filter(materia_id=materia_id, usuario=aluno)
    prova_id = getProvaUserID(request, materia_id, aluno)
    prova_id = prova_id[0]['prova_id']
    lista_nrpergunta = []
    lista_resultado = []
    for numero_pergunta in nr_pergunta:
        lista_nrpergunta.append(numero_pergunta)
    for res in resultado:
        lista_resultado.append(res)
    index = 0
    peso = 0
    nota = 0
    for lista in lista_nrpergunta:
        perguntas = Perguntas.objects.get(nr_pergunta=lista, materia_id=materia_id)
        pergunta_id = perguntas.id
        try:
            resultado = lista_resultado[index]
        except:
            mensagem = _("Respostas devem ser marcadas como correta ou incorreta")
            context = {
                'mensagem': mensagem,
                'aluno': aluno,
                'nome_materia': nome_materia,
                'provas': provas,
                'data': data
            }
            return render(request, "viewProvaAlunoMateria.html", context)
        else:
            resultado = lista_resultado[index]
            if resultado == "Correto":
                peso = perguntas.peso
                nota = nota + peso
            else:
                peso = 0
            index = index + 1
            atualiza = atualizaCorrecaoProva(request, materia_id, pergunta_id, resultado, aluno, peso)
    check = checkNotaUsuario(request, user_id, prova_id)
    if check == []:
        inserirNota = inserirNotaUsuario(request, user_id, nome_materia, nota, aluno, prova_id)
    else:
        now = datetime.datetime.now()
        data = (now.strftime("%Y-%m-%d"))
        updateNota = updateNotaUsuario(request, nome_materia, nota, user_id, data, prova_id)
    respostas = getProvasResumo(request)
    context = {
        'respostas': respostas
    }
    return render(request, "viewProvasAlunos.html", context)

def arquivarProva(request, materia_id, aluno):
    mensagem = ""
    usuario = User.objects.get(username=aluno)
    user_id = usuario.id
    materia = Materia.objects.get(id=materia_id)
    nome_materia = materia.nome
    checkNota = checkUsuarioNota(request, nome_materia, user_id)
    backup = fazBackupProva(request, materia_id, user_id, aluno, nome_materia)
    mensagem = _("Prova arquivada com sucesso!")
    respostas = getProvasResumo(request)
    context = {
        'respostas': respostas,
        'mensagem': mensagem
    }
    return render(request, "viewProvasAlunos.html", context)

def viewProvasHistory(request):
    provas = getProvasHistory(request)
    materias = getMateriasHistory(request)
    usuarios = getAlunosHistory(request)
    context = {
        'provas': provas,
        'materias': materias,
        'usuarios': usuarios
    }
    return render(request, "viewProvasHistory.html", context)

def mostrarDetalhesProva(request, prova_id):
    provas = getProvaHistory(request, prova_id)
    resultados = getDetalhesProva(request, prova_id)
    context = {
        'provas': provas,
        'resultados': resultados
    }
    return render(request, "viewDetalhesProva.html", context)

def filtrarMateriaHistory(request):
    materia_id = request.POST.get("materias")
    provas = getProvaHistoryMateria(request, materia_id)
    usuarios = getAlunosHistory(request)
    materias = getMateriasHistory(request)
    context = {
        'provas': provas,
        'usuarios': usuarios,
        'materias': materias
    }
    return render(request, "viewProvasHistory.html", context)

def filtrarProvaAluno(request):
    user_id = request.POST.get("usuario")
    provas = getProvasAlunoHistory(request, user_id)
    usuarios = getAlunosHistory(request)
    materias = getMateriasHistory(request)
    context = {
        'provas': provas,
        'usuarios': usuarios,
        'materias': materias
    }
    return render(request, "viewProvasHistory.html", context)
