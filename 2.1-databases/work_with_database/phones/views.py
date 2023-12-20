from django.shortcuts import render, redirect, HttpResponse
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    phone = Phone.objects.all()
    if sort == 'max_price':
        phone = Phone.objects.all().order_by('-price')
    elif sort == 'min_price':
        phone = Phone.objects.all().order_by('price')
    elif sort == 'name':
        phone = Phone.objects.all().order_by('name')
    else:
        phone = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    print(context)
    return render(request, template, context)
