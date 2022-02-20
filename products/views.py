from django.shortcuts import render
from products.models import *
from utils.get_product_details import get_items_product_bundle_home, get_products_in_sales
import operator


def product(request, slug1=None, slug=None):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # Product Item --- поиск и отбор продукта - включает данные по продукту
    try:
        product_show = Product.objects.get(slug=slug)
        print('products--------------------', product_show)
        product_item = ProductItem.objects.filter(name=product_show.name)
        # получаем параметры для айтема продукта - SALES; - Проверить включить проверку косметолога ЗДЕСЬ
        p_sales = list()
        for p in product_item:
            try:
                product_sales = ProductItemSales.objects.get(is_active=True, product_item=p)

                sales_item = {'name': p.name, 'volume': p.volume, 'volume_type': p.volume_type,
                              'ref_number': p.ref_number,
                              'price_old': product_sales.price_old, 'price_current': product_sales.price_current,
                              'discount': product_sales.discount, 'product_sales_id': product_sales.id}
                p_sales.append(sales_item)
            except:
                pass
        p_sales.sort(key=operator.itemgetter('price_current'))
        print('9999999999999999999999999999999999999', p_sales)
    except:
        print('НИЧЕГО НЕТ')
        product_show = None

    if product_show is not None: # показываем страничку Продукта для простого Айтема
        print('HEr-HEr')
        return render(request, 'products/product.html', locals())

    else:   # BundleProduct --- поиск и отбор продукта - включает данные по продукту
        try:
            bundle_sales = BundleSale.objects.get(slug=slug)  # нашли уникальный Бандл
            bundle_product_items = ProductInBundle.objects.filter(bundle=bundle_sales) # фильтруем СЕТ (более 1) айтема в Бендле
            print(bundle_product_items)
            p_product = list()
            for bp_item in bundle_product_items:
                product_name = bp_item.product_item.name
                print('--------Volume', bp_item.product_item.volume)
                try:
                    p = Product.objects.get(name=product_name) # находим продукт в бандле
                    print('----product_bundle---------', p)
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
                                         'description_4': p.description_4, 'description_5': p.description_5
                                         }
                    p_product.append(product_page_item)
                except:
                    pass
        except:
            pass
    return render(request, 'products/product_bundle.html', locals())


def product_line(request, slug):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    try:
        product_line = ProductCategory.objects.get(slug=slug)
    except:
        product_line = None

    p_items, b_sales = get_items_product_bundle_home(slug)

    # SAlES

    products_sales = ProductItemSales.objects.filter(is_active=True, product_item__category=product_line)
    p_sales = get_products_in_sales(products_sales)
    print('----9876545----------', len(p_sales))
    # b_sales = get_bundles_in_sales(bundles_sales)
    p_sales = p_sales + b_sales
    print(len(p_sales), len(b_sales))

    return render(request, 'products/product_line.html', locals())
