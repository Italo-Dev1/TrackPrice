from django.shortcuts import render
from django.db.models import Avg, Min, Max
from django.http import HttpResponse
from .models import Produto
import csv

def index(request):
    produtos = Produto.objects.all()

    context = {
        "produtos": produtos,
        "total_produtos": produtos.count(),
        "preco_medio": produtos.aggregate(Avg("valor_total"))["valor_total__avg"] or 0,
        "maior_preco": produtos.aggregate(Max("valor_total"))["valor_total__max"] or 0,
        "menor_preco": produtos.aggregate(Min("valor_total"))["valor_total__min"] or 0,
        "produto_mais_caro": produtos.order_by("-valor_total").first(),
        "produto_mais_barato": produtos.order_by("valor_total").first(),
    }

    return render(request, "index.html", context)


def produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})
