from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserProfileForm
from .models import UserProfile, view_user_grupo
from .functions import (getGrupos, associarGrupoUsuario, getUserGrupo, deleteGrupoUsuario, getAllGrupos,
    getAllUsers, getAllUsersRestaurante, getAllUsersEscola, getUsuario, removerUsuario, checkUserMateria, checkUserProva,
    checkUserPedido)
from principal.functions import getIdiomaSystem
from django.conf.urls.i18n import i18n_patterns
from django.utils import translation


def login_user(request):
    idioma = getIdiomaSystem(request)
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        idioma = translation.get_language()
        return redirect("/" + idioma + "/tutorial/")
    context = {
        'idioma': idioma,
    }
    return render(request, "loginUser.html", context)

def cadastrarUsuario(request):
    grupos = getAllGrupos(request)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            grupo = request.POST.get("grupo")
            usuario = User.objects.get(username=username)
            user_id = usuario.id
            criarGrupo = associarGrupoUsuario(request, user_id, grupo)
            return render(request, "index.html")
        else:
            form = RegistrationForm()
            context = {
                'form': form,
                'grupos': grupos
            }
            return render(request, "cadastrarUsuario.html", context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
            'grupos': grupos
        }
        return render(request, "cadastrarUsuario.html", context)

def user_logout(request):
    print("entrou no logout")
    logout(request)
    idioma = translation.get_language()
    return redirect("/" + idioma + "/tutorial/")

def alterarSenha(request):
    idioma = getIdiomaSystem(request)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "index.html")
        else:
            return redirect('/tutorial/')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
	     'form': form,
         'idioma': idioma
	}
    return render(request, "alterarSenha.html", context)

def cadastrarPerfil(request):
    idioma = getIdiomaSystem(request)
    form = UserProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/tutorial/')
    else:
        print('form is not valid')
        print(form.errors)
    context = {
        'form': form,
        'idioma': idioma
    }
    return render(request, "cadastrarPerfil.html", context)

def editarPerfil(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
        usuario = User.objects.get(username=user)
        profile = UserProfile.objects.get(user=user)
        user_grupo = getUserGrupo(request, user_id)
        grupo_id = user_grupo[0]['grupo_id']
        grupo_nome = user_grupo[0]['nome_grupo']
        grupos = getGrupos(request, grupo_id)
    else:
        usuario = ""
        profile = ""
    context = {
        'usuario': usuario,
        'profile': profile,
        'grupos': grupos,
        'grupo_id': grupo_id,
        'grupo_nome': grupo_nome
    }
    return render(request, "editarPerfil.html", context)

def salvarAlteracoesUsuario(request, username):
    usuario = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=usuario.id)
    user = request.POST.get("user")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    telefone = request.POST.get("telefone")
    endereco_completo = request.POST.get("endereco_completo")
    idade = request.POST.get("idade")
    usuario.username = username
    usuario.first_name = first_name
    usuario.last_name = last_name
    usuario.email = email
    usuario.save()
    profile.telefone = telefone
    profile.endereco_completo = endereco_completo
    profile.idade = idade
    profile.save()
    return redirect('/tutorial/')

def salvarGrupoUsuario(request):
    user_id = request.POST.get("user")
    grupo_id = request.POST.get("grupo")
    removeGrupo = deleteGrupoUsuario(request, user_id)
    criarGrupo = associarGrupoUsuario(request, user_id, grupo_id)
    logout(request)
    idioma = translation.get_language()
    return redirect("/" + idioma + "/usuarios/")

def listarUsuarios(request):
    user_id = request.user.id
    grupo = view_user_grupo.objects.get(user_id=user_id)
    grupo_nome = grupo.nome_grupo
    if grupo_nome == 'admin':
        usuarios = getAllUsersRestaurante(request)
    elif grupo_nome == 'professor':
        usuarios = getAllUsersEscola(request)
    else:
        usuarios = getAllUsers(request)
    context = {
        'usuarios': usuarios
    }
    return render(request, "listarUsuarios.html", context)

def editarUsuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user_id=user_id)
    user_grupo = getUserGrupo(request, user_id)
    grupo_id = user_grupo[0]['grupo_id']
    grupo_nome = user_grupo[0]['nome_grupo']
    grupos = getGrupos(request, grupo_id)
    context = {
        'usuario': usuario,
        'profile': profile,
        'grupo_id': grupo_id,
        'grupo_nome': grupo_nome,
        'grupos': grupos
    }
    return render(request, "editarUsuario.html", context)

def salvarAlteracoesUser(request, user_id):
    usuario = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user_id=user_id)
    user = request.POST.get("user")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    telefone = request.POST.get("telefone")
    endereco_completo = request.POST.get("endereco_completo")
    idade = request.POST.get("idade")
    grupo = request.POST.get("grupo")
    removeGrupo = deleteGrupoUsuario(request, user_id)
    criarGrupo = associarGrupoUsuario(request, user_id, grupo)
    usuario.id = user
    usuario.first_name = first_name
    usuario.last_name = last_name
    usuario.email = email
    usuario.save()
    profile.telefone = telefone
    profile.endereco_completo = endereco_completo
    profile.idade = idade
    profile.save()
    usuarios = getAllUsers(request)
    context = {
        'usuarios': usuarios
    }
    return render(request, "listarUsuarios.html", context)

def deleteUsuario(request, user_id):
    mensagem = ""
    userGrupo = view_user_grupo.objects.get(user_id=user_id)
    nome_grupo = userGrupo.nome_grupo
    if nome_grupo == 'aluno':
        check = checkUserMateria(request, user_id)
        if check == []:
            usuario = User.objects.get(id=user_id)
            username = usuario.username
            check2 = checkUserProva(request, username)
            if check2 == []:
                removeUser = removerUsuario(request, user_id)
                mensagem = _("Usuário deletado com sucesso!")
            else:
                mensagem = _("Usuário não pode ser deletado pois está associado a uma prova!")
        else:
            mensagem = _("Usuário não pode ser deletado pois está associado a uma ou mais matérias")
    elif nome_grupo == 'usuario':
        check3 = checkUserPedido(request, user_id)
        if check3 == []:
            removeUser = removerUsuario(request, user_id)
            mensagem = _("Usuário deletado com sucesso!")
        else:
            mensagem = _("Usuário não pode ser deletado pois está associado a um ou mais pedidos")
    elif nome_grupo == 'admin' or nome_grupo == 'professor':
        mensagem = _("Usuário não pode ser deletado pois ele é admin")
    else:
        removeUser = removerUsuario(request, user_id)
        mensagem = _("Usuário deletado com sucesso!")
    usuarios = getAllUsers(request)
    context = {
        'usuarios': usuarios,
        'mensagem': mensagem
    }
    return render(request, "listarUsuarios.html", context)
