from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('forma_de_pagamento', models.CharField(max_length=100, verbose_name='Forma de Pagamento')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor total do Item')),
                ('parcelamento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantidade de Parcelas')),
                ('link_produto', models.URLField(verbose_name='Link do Produto')),
            ],
        ),
    ]
