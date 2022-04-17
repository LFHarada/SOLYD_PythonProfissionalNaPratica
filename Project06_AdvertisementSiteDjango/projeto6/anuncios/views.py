from django.shortcuts import render, get_object_or_404

from .models import Categoria
from .models import Anuncio


def home(request):
    categorias = Categoria.objects.all()
    # ultimos_anuncios = Anuncio.objects.search('')

    return render(request, 'home.html', {'categorias': categorias,
                                        # 'anuncios': ultimos_anuncios
                                         })


def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.filter(categoria=categoria)

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios,
                                         'categoria': categoria
                                         })


def anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, id=anuncio_id)
    categorias = Categoria.objects.all()

    return render(request, 'anuncio.html', {'categorias': categorias,
                                            'anuncio': anuncio
                                            })


def resultado(request):
    valor_digitado = request.GET.get('resultado', 'This is a default value')
    anuncios = Anuncio.objects.search(valor_digitado)
    categorias = Categoria.objects.all()
    context = {'valor_digitado': valor_digitado,
               'anuncios': anuncios,
               'categorias': categorias
               }
    return render(request, 'resultado.html', context)