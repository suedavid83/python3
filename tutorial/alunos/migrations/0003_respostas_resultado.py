# Generated by Django 3.0.5 on 2020-09-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_remove_respostas_resultado'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostas',
            name='resultado',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]