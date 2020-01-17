from django.shortcuts import render
from django.http import HttpResponse
from .models import Prodcuts


def index(request):
    products = Prodcuts.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('new products')