from django.db import models, connection
from .models import SystemConfiguration

def setSystemIdioma(self, idioma, descricao):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE principal_systemconfiguration set codigo = %s, descricao = %s", [idioma, descricao])
        row = cursor.fetchone()
    return row

def getIdiomaSystem(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, codigo FROM principal_systemconfiguration")
        row = dictfetchall(cursor)
        class Meta:
            model = SystemConfiguration
            fields = ['id', 'codigo']
    return row[0]['codigo']

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
