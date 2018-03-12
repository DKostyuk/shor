from django.shortcuts import render
from products.models import *


def product(request, slug):
    product = Product.objects.get(slug=slug)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    # print(request.session.session_key)

    return render(request, 'products/product.html', locals())


def product_line(request, slug):
    # product = Product.objects.get(slug=slug)
    product_line = ProductCategory.objects.get(slug=slug)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True,
                                                  product__category__is_active=True, product__category__slug=slug)
    print(products_images)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    # print(request.session.session_key)

    return render(request, 'products/product_line.html', locals())
