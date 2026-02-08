from django.shortcuts import render

from core.models import Produto


# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}

    return render(request, 'index.html', context)


def produtos(request):
    return render(request, 'produtos.html')



def error404(request, exception):
    return render(request, '404.html')