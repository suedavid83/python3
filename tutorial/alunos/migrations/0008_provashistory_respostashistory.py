# Generated by Django 3.0.5 on 2020-10-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0007_alunomaterianota_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvasHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('materia_id', models.IntegerField()),
                ('qtde_perguntas', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('total_peso', models.IntegerField(blank=True, null=True)),
                ('nota', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RespostasHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('materia_id', models.IntegerField()),
                ('pergunta_id', models.IntegerField()),
                ('resposta', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_id', models.IntegerField()),
                ('resultado', models.CharField(blank=True, max_length=20, null=True)),
                ('peso', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
