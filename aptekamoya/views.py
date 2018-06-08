from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.db import connection

from products.models import *

from aptekamoya.forms import SignUpForm


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_tablets = products_images.filter(product__category__id=1)
    products_images_virus = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def custom(request):
    with connection.cursor() as cursor:
        # товары по возрастанию цены
        cursor.execute("select * from products_product order by price asc")

        # сумма всех заказов
        # cursor.execute("select sum(total_price) from orders_order")

        rows = cursor.fetchall()

    return HttpResponse("<br>".join(map(str, rows)))
