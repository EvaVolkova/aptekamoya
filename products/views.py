from django.shortcuts import render
from products.models import *


def index(request):
    # products = ProductImage.objects.all()
    products = ProductImage.objects.raw('select * from products_productimage')
    return render(request, 'products/index.html', locals())


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'products/product.html', locals())
