from django.shortcuts import render
from catalog.models import Product

from django.views.generic import ListView


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
