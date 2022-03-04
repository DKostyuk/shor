from django.shortcuts import render
from products.models import *
import operator


def product(request, slug1=None, slug=None):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    try:
        # Product Item --- поиск и отбор продукта - включает данные по продукту
        # for Visitor
        product_show = Product.objects.get(slug=slug)
        product_item = ProductItem.objects.filter(product=product_show.id)
        product_sales = SalesProduct.objects.filter(is_active=True, slug=slug)
        # получаем параметры для айтема продукта - SALES; - Проверить включить проверку косметолога ЗДЕСЬ
        products_in_sale = SaleProductItem.objects.filter(is_active=True, product_item__in=product_item)
        p_sales = list()
        for p in products_in_sale:
            try:
                sales_item = {'name': p.sales_product.name, 'volume': p.product_item.volume,
                              'volume_type': p.product_item.volume_type, 'ref_number': p.product_item.ref_number,
                              'price_old': p.sales_product.price_old, 'price_current': p.sales_product.price_current,
                              'discount': p.sales_product.discount, 'product_sales_id': p.sales_product.id}
                p_sales.append(sales_item)
            except:
                pass
        p_sales.sort(key=operator.itemgetter('price_current'))
    except:
        print('НИЧЕГО НЕТ')
        product_show = None

    if product_show is not None: # показываем страничку Продукта для простого Айтема
        print('HEr-HEr')
        return render(request, 'products/product.html', locals())

    else:   # BundleProduct --- поиск и отбор продукта - включает данные по продукту
        try:
            # Bundle --- поиск и отбор бандла - включает данные по всем продуктам внутри
            # for Visitor
            bundle_sales = SalesProduct.objects.get(is_active=True, slug=slug)
            in_bundle_products = SaleProductItem.objects.filter(sales_product=bundle_sales.id)
            p_product = list()
            for bp_item in in_bundle_products:
                product_name = bp_item.product_item.name
                p = Product.objects.get(name=product_name)  # находим продукт в бандле
                for_id = p.name.replace(" ", "_")
                product_page_item = {'name': bundle_sales.name, 'name_pl': bundle_sales.name_pl,
                                     'product_name': p.name, 'product_name_pl': p.name_pl,
                                     'image_url': bundle_sales.image.url, 'category': p.category,
                                     'name_description': p.name_description, 'description': p.description,
                                     'description_1': p.description_1,
                                     'name_description_2': p.name_description_2, 'description_2': p.description_2,
                                     'name_description_3': p.name_description_3, 'description_3': p.description_3,
                                     'for_id': for_id, 'volume': bp_item.product_item.volume,
                                     'volume_type': bp_item.product_item.volume_type,
                                     'ref_number': bp_item.product_item.ref_number,
                                     'description_4': p.description_4, 'description_5': p.description_5}
                p_product.append(product_page_item)
        except:
            pass
        return render(request, 'products/product_bundle.html', locals())


def product_line(request, slug=None):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    if slug:
        try:
            product_line = ProductCategory.objects.get(slug=slug)
        except:
            product_line = None
        # Find and range products for Visitor
        sale_product_item = SaleProductItem.objects.filter(is_active=True, product_item__category__slug=slug).values_list('sales_product', flat=True)
        sales_product = SalesProduct.objects.filter(is_active=True, id__in=sale_product_item, duplicate=12).order_by('rank')
        p_items = sales_product

        # # Find and range products for Cosmetolog - SAlES
        pb_home_2 = SalesProduct.objects.filter(is_active=True, id__in=sale_product_item).order_by('rank')
        p_home_2 = pb_home_2.filter(type=1)
        b_home_2 = pb_home_2.filter(type=2)
        print('--------1111111111111111-----------', p_home_2)
        print('--------22222222222222222222-----------', b_home_2)
        products_in_sale = SaleProductItem.objects.filter(is_active=True, sales_product__in=p_home_2)
        p_sales = list()
        for p in products_in_sale:
            try:
                if p.sales_product.type.id == 1:
                    sales_item = {'name_sales': p.sales_product.name, 'volume': p.product_item.volume,
                                  'volume_type': p.product_item.volume_type, 'slug': p.sales_product.slug,
                                  'price_old': p.sales_product.price_old, 'price_current': p.sales_product.price_current,
                                  'discount': p.sales_product.discount, 'rank': p.sales_product.rank,
                                  'image_url': p.sales_product.image_url}
                    p_sales.append(sales_item)

            except:
                pass
        for b in b_home_2:
            sales_item = {'name_sales': b.name, 'volume': 'див',
                          'volume_type': '. ', 'slug': b.slug,
                          'price_old': b.price_old, 'price_current': b.price_current,
                          'discount': b.discount, 'rank': b.rank,
                          'image_url': b.image_url}
            p_sales.append(sales_item)
        p_sales.sort(key=operator.itemgetter('rank'))

        return render(request, 'products/product_line.html', locals())

    if slug is None:
        return render(request, 'products/product_line_no_product.html', locals())


def product_no(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # Find and range products for visitors
    pb_home_1 = SalesProduct.objects.filter(is_active=True, duplicate=12, rank__lt=12).order_by('rank')
    p_items = pb_home_1
    # Find and range products for Cosmetolog
    pb_home_2 = SalesProduct.objects.filter(is_active=True, rank__lt=12).order_by('rank')
    # p_sales = pb_home_2
    p_home_2 = pb_home_2.filter(type=1)
    b_home_2 = pb_home_2.filter(type=2)
    products_in_sale = SaleProductItem.objects.filter(is_active=True, sales_product__in=p_home_2)
    p_sales = list()
    for p in products_in_sale:
        try:
            if p.sales_product.type.id == 1:
                sales_item = {'name_sales': p.sales_product.name, 'volume': p.product_item.volume,
                              'volume_type': p.product_item.volume_type, 'slug': p.sales_product.slug,
                              'price_old': p.sales_product.price_old,
                              'price_current': p.sales_product.price_current,
                              'discount': p.sales_product.discount, 'rank': p.sales_product.rank,
                              'image_url': p.sales_product.image_url}
                p_sales.append(sales_item)

        except:
            pass
    for b in b_home_2:
        sales_item = {'name_sales': b.name, 'volume': 'див',
                      'volume_type': '. ', 'slug': b.slug,
                      'price_old': b.price_old, 'price_current': b.price_current,
                      'discount': b.discount, 'rank': b.rank,
                      'image_url': b.image_url}
        p_sales.append(sales_item)
    p_sales.sort(key=operator.itemgetter('rank'))

    return render(request, 'products/product_no.html', locals())
