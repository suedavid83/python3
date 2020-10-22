from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model: UserProfile
    list_display = ['user','telefone', 'endereco_completo', 'idade']
    search_fields = ['user']
    list_filter = ['user', 'idade']
    save_on_top = True

admin.site.register(UserProfile, UserProfileAdmin)
