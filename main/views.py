from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Главная',
        'content': 'Главная страница магазина "Home"'
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title' : 'Home - О нас',
        'content' : 'О нас',
        'text_on_page': 'Текст почему этот магазин такой крутой'
    }
    return render(request, 'main/about.html', context)