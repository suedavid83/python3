# Generated by Django 3.0.5 on 2020-10-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0006_respostas_total_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunomaterianota',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
