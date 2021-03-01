from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Product

class CreateProduct(CreateView):
    model = Product
    fields = ['name', 'image']
    success_url = reverse_lazy('resize_image:list')

class ListProduct(ListView):
    model = Product
