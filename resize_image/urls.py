from django.urls import path
from . import views

app_name = 'resize_image'

urlpatterns = [
    path('create', views.CreateProduct.as_view(), name='create'),
    path('list', views.ListProduct.as_view(), name='list'),
]
