import os

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request: HttpRequest) -> HttpResponse:
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request: HttpRequest) -> HttpResponse:
    current_time = datetime.now().strftime('%H:%m')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request: HttpRequest) -> HttpResponse:
    dirs = os.listdir(path=r'C:\Users\riddi\PycharmProjects\dj-home\dj-homeworks\1.1-first-project\first_project')
    return HttpResponse(' '.join([dir for dir in dirs]))
