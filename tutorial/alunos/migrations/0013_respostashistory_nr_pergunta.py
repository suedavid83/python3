# Generated by Django 3.0.5 on 2020-10-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0012_respostashistory_pergunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostashistory',
            name='nr_pergunta',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]