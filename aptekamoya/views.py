from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

from products.models import *


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_tablets = products_images.filter(product__category__id=1)
    products_images_virus = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())
