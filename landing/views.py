from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print (data["name"])
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    last_four_products_images = products_images.order_by('-id')[:4]
    products_images_tablets = products_images.filter(product__category__id=1).order_by('?')[:4]
    products_images_virus = products_images.filter(product__category__id=2).order_by('?')[:4]
    return render(request, 'landing/home.html', locals())