from django.contrib import admin
from .models import *


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'forma_de_pagamento', 'valor_total','parcelamento','link_produto')
admin.site.register(Produto, ProdutoAdmin)

