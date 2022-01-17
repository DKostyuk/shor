from django.shortcuts import render
from products.models import *
from cosmetologs.models import ServiceProductImage


def product(request, slug1, slug):
    product = Product.objects.get(slug=slug)
    cosmetolog = Cosmetolog.objects.get(slug=slug1)
    # print('-----------', vars(cosmetolog))
    # print('ЧТО-то вместо адресса', str(cosmetolog.street_cosmetolog.display_address))
    if cosmetolog.street_cosmetolog is None:
        cosmetolog_address = "Работа по вызову"
    else:
        cosmetolog_address = str(cosmetolog.street_cosmetolog.display_address) + ', ' + cosmetolog.house_cosmetolog
    # print('ЧТО-то вместо адресса', cosmetolog_address)


    service_products_images = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                                 service_product__is_active=True,
                                                                 service_product__is_visible=True,
                                                                 service_product__cosmetolog=cosmetolog.id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True,
                                                  product__is_active=True,
                                                  product__cosmetolog=cosmetolog.id).exclude(product=product)


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
