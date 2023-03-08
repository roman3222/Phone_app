from django.http import Http404
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    context = {
        'phones': phones,
        'sort': sort,
    }
    return render(request, template, context)


def show_product(request, slug):
    try:
        phone = Phone.objects.get(slug=slug)
    except Phone.DoesNotExists:
        raise Http404('Такой модели не найдено')
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
