from django.db import models
from django.contrib.auth.models import User
from  django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.IntegerField(null=True, blank=True)
    endereco_completo = models.CharField(max_length=500, blank=True, null=True)
    idade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class view_grupos(models.Model):
    id_grupo = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=15, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_grupos'

class view_user_grupo(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    grupo_id = models.IntegerField(null=True, blank=True)
    nome_grupo = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_user_grupo'
