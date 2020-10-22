from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . classes import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('cadastrarUsuario/', views.cadastrarUsuario, name="cadastrarUsuario"),
    path('logout/', views.user_logout, name="user_logout"),
    path('alterarSenha/', views.alterarSenha, name="alterarSenha"),
    path('resetPassword/', password_reset, name="resetPassword"),
    path('resetPassword/password_reset_done/', password_reset_done, name="password_reset_done"),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name="password_reset_confirm"),
    path('reset/done/', password_reset_complete, name="password_reset_complete"),
    path('cadastrarPerfil/', views.cadastrarPerfil, name="cadastrarPerfil"),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('salvarAlteracoesUsuario/<slug:username>/', views.salvarAlteracoesUsuario, name="salvarAlteracoesUsuario"),
    path('salvarGrupoUsuario/', views.salvarGrupoUsuario, name="salvarGrupoUsuario"),
    path('listarUsuarios/', views.listarUsuarios, name="listarUsuarios"),
    path('editarUsuario/<int:user_id>/', views.editarUsuario, name="editarUsuario"),
    path('deleteUsuario/<int:user_id>/', views.deleteUsuario, name="deleteUsuario"),
    path('salvarAlteracoesUser/<int:user_id>/', views.salvarAlteracoesUser, name="salvarAlteracoesUser")
]
