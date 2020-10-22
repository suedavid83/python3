from django.db import models

class SystemConfiguration(models.Model):
    SIGLA_IDIOMA = (
        (u'pt', u'pt'),
        (u'en', u'en'),
        (u'es', u'es'),
    )

    codigo = models.CharField(choices=SIGLA_IDIOMA, max_length=10, default=0)
    descricao = models.CharField(max_length=20, null=True, blank=True)
