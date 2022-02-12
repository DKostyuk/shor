from django.shortcuts import render
from products.models import *
import operator
from landing.views import get_products_in_sales
from cosmetologs.models import ServiceProductImage


def product(request, slug1=None, slug=None):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    try:
        product = Product.objects.get(slug=slug)
    except:
        product = None
    product_item = ProductItem.objects.filter(name=product.name)
    p_sales = list()
    for p in product_item:
        try:
            product = Product.objects.get(name=p.name)
            product_image = ProductImage.objects.get(is_active=True, is_main=True, product__is_active=True,
                                                     product=product)
            product_sales = ProductItemSales.objects.get(is_active=True, product_item=p)
            sales_item = {'name': p.name, 'volume': p.volume, 'volume_type': p.volume_type, 'ref_number': p.ref_number,
                          'price_old': product_sales.price_old, 'price_current': product_sales.price_current,
                          'discount': product_sales.discount, 'product_sales_id': product_sales.id}
        except:
            sales_item = {}
        p_sales.append(sales_item)
    p_sales.sort(key=operator.itemgetter('price_current'))

    # sss = sorted(p_sales, key=operator.itemgetter('price_current'), reverse=True)
    # print('PRINT------------', sss)

    #cosmetolog = Cosmetolog.objects.get(slug=slug1)
    # print('-----------', vars(cosmetolog))
    # print('ЧТО-то вместо адресса', str(cosmetolog.street_cosmetolog.display_address))
    #if cosmetolog.street_cosmetolog is None:
    #    cosmetolog_address = "Работа по вызову"
    #else:
    #    cosmetolog_address = str(cosmetolog.street_cosmetolog.display_address) + ', ' + cosmetolog.house_cosmetolog
    # print('ЧТО-то вместо адресса', cosmetolog_address)


    #service_products_images = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                               #  service_product__is_active=True,
                                                                # service_product__is_visible=True,
                                                                 #service_product__cosmetolog=cosmetolog.id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True,
                                                  product__is_active=True)

    return render(request, 'products/product.html', locals())


def product_line(request, slug):
    # product = Product.objects.get(slug=slug)
    try:
        product_line = ProductCategory.objects.get(slug=slug)
    except:
        product_line = None

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True,
                                                  product__category__is_active=True, product__category__slug=slug)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_sales = ProductItemSales.objects. filter(is_active=True, product_item__category=product_line)
    p_sales = get_products_in_sales(products_sales)

    return render(request, 'products/product_line.html', locals())
