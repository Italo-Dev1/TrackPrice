from django.shortcuts import render
from django.db.models import Avg, Min, Max
from django.http import HttpResponse
from .models import Produto
import csv


def dashboard(request):
    produtos = Produto.objects.all()

    context = {
        "total_produtos": produtos.count(),
        "preco_medio": produtos.aggregate(
            Avg("valor_total")
        )["valor_total__avg"] or 0,

        "menor_preco": produtos.aggregate(
            Min("valor_total")
        )["valor_total__min"] or 0,

        "maior_preco": produtos.aggregate(
            Max("valor_total")
        )["valor_total__max"] or 0,

        "produto_mais_caro": produtos.order_by("-valor_total").first(),
        "produto_mais_barato": produtos.order_by("valor_total").first(),

        "produtos": produtos[:100],
    }

    return render(request, "index.html", context)



def produtos(request):
    produtos = Produto.objects.all()

    nome = request.GET.get("q")
    forma_pagamento = request.GET.get("forma")
    preco_min = request.GET.get("preco_min")
    preco_max = request.GET.get("preco_max")
    ordenar = request.GET.get("ordenar")

    if nome:
        produtos = produtos.filter(nome__icontains=nome)

    if forma_pagamento:
        produtos = produtos.filter(forma_de_pagamento__icontains=forma_pagamento)

    if preco_min:
        produtos = produtos.filter(valor_total__gte=preco_min)

    if preco_max:
        produtos = produtos.filter(valor_total__lte=preco_max)

    if ordenar == "menor_preco":
        produtos = produtos.order_by("valor_total")
    elif ordenar == "maior_preco":
        produtos = produtos.order_by("-valor_total")

    return render(request, "produtos.html", {"produtos": produtos})


def exportar_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="produtos.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "ID", "Produto", "Forma de Pagamento",
        "Valor Total", "Parcelas", "Link"
    ])

    for p in Produto.objects.all():
        writer.writerow([
            p.id,
            p.nome,
            p.forma_de_pagamento,
            p.valor_total,
            p.parcelamento,
            p.link_produto
        ])

    return response


def index(request):
    produtos = Produto.objects.all()

    context = {
        "produtos": produtos,
        "total_produtos": produtos.count(),
        "preco_medio": produtos.aggregate(Avg("valor_total"))["valor_total__avg"] or 0,
        "maior_preco": produtos.aggregate(Max("valor_total"))["valor_total__max"] or 0,
        "menor_preco": produtos.aggregate(Min("valor_total"))["valor_total__min"] or 0,
    }

    return render(request, "index.html", context)
