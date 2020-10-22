# Generated by Django 3.0.5 on 2020-09-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='view_controlevendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('nome_produto', models.CharField(blank=True, max_length=50, null=True)),
                ('qtde_vendida', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'view_controlevendas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='view_meus_pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_pedido', models.IntegerField(blank=True, null=True)),
                ('nome_produto', models.CharField(blank=True, max_length=50, null=True)),
                ('preco_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status_pedido', models.CharField(blank=True, max_length=20, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'view_meus_pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='view_pedidos_clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('qtde_pedidos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'view_pedidos_clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='view_pedidos_detalhes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('status_pedido', models.CharField(blank=True, max_length=20, null=True)),
                ('qtde_pedidos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'view_pedidos_detalhes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='view_pedidoshistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('nr_pedido', models.IntegerField(blank=True, null=True)),
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('nome_produto', models.CharField(blank=True, max_length=50, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('preco_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status_pedido', models.CharField(blank=True, max_length=20, null=True)),
                ('dt_pedido', models.DateField(blank=True, null=True)),
                ('dt_hr_insercao', models.DateTimeField(blank=True, null=True)),
                ('dt_hr_pronto', models.DateTimeField(blank=True, null=True)),
                ('dt_hr_entregue', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'view_pedidoshistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MeusPedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_pedido', models.IntegerField(blank=True, null=True)),
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('preco_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('status_pedido', models.CharField(blank=True, max_length=20, null=True)),
                ('dt_hr_insercao', models.DateTimeField(blank=True, null=True)),
                ('dt_hr_pronto', models.DateTimeField(blank=True, null=True)),
                ('dt_hr_entregue', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidosHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_pedido', models.IntegerField(blank=True, null=True)),
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('preco_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('status_pedido', models.CharField(blank=True, max_length=20, null=True)),
                ('dt_hr_insercao', models.DateTimeField(blank=True, null=True)),
                ('dt_hr_pronto', models.DateTimeField(blank=True, null=True)),
                ('dt_hr_entregue', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]