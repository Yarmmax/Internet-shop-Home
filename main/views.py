from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'магазин мебели "Home"',
        'content': 'Главная страница магазина "Home"'
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')