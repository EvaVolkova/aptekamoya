from django.conf.urls import url, include
from django.contrib import admin
from products import views
from products.views import ProductList

urlpatterns = [
    url(r'^products/', ProductList.as_view(), name='index'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]

