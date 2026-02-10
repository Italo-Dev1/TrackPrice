from django.db import models

class Produto(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    nome = models.CharField(verbose_name='Nome do Produto', max_length=100)
    forma_de_pagamento = models.CharField(verbose_name='Forma de Pagamento', max_length=100)
    valor_total = models.DecimalField(verbose_name='Valor total do Item', max_digits=10, decimal_places=2)
    parcelamento = models.IntegerField(verbose_name='Quantidade de Parcelas')
    link_produto = models.URLField(verbose_name='Link do Produto')

    def __str__(self):
        return self.nome






