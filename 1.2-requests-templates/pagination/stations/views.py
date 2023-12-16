from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from csv import DictReader
from pagination import settings
def index(request):
    return redirect(reverse('bus_stations'))

content = []
def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r' ,newline='', encoding='utf-8') as f:
        bus_stations = list(DictReader(f))
        paginator = Paginator(bus_stations, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
