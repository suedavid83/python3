# Generated by Django 3.0.5 on 2020-10-10 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0013_respostashistory_nr_pergunta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respostas',
            old_name='total_peso',
            new_name='nota',
        ),
        migrations.RemoveField(
            model_name='provashistory',
            name='total_peso',
        ),
    ]
