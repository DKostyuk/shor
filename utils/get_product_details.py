from products.models import *


def get_items_product_bundle_home(slug=None):
    if slug is not None:
        products_images = ProductImage.objects.filter(is_active=True, product__is_active=True, is_main=True,
                                                      product__category__is_active=True, product__category__slug=slug)
    else:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
        print('PICTURE - ---------', products_images)
    p_items = list()
    b_sales = list()
    for p_image in products_images:
        product_item = {'name': p_image.product.name, 'image_url': p_image.image.url,
                        'name_pl': p_image.product.name, 'slug': p_image.product.slug}
        p_items.append(product_item)

    bundle_sales = BundleSale.objects.filter(is_active=True) #выбрали все бандлы, но надо бандлы
    # там где есть продукты только этой продуктовой линии
    print(bundle_sales)
    for bundle in bundle_sales:
        # нашли все айтемы которые берут участие в бандлах и включены в эту продуктовую серию
        if slug is not None:
            bundle_product_item = ProductInBundle.objects.filter(bundle=bundle, is_active=True,
                                                                 product_item__category__slug=slug)
        else:
            bundle_product_item = ProductInBundle.objects.filter(bundle=bundle, is_active=True)
        print(bundle_product_item)
        # если таких продакт атемов нету, то закончили формирование списка продуктов для серии
        # если есть продуты, то формируем дополнение и включаем в список
        if len(bundle_product_item) > 0:

            bundle_item = {'name': bundle.name, 'image_url': bundle.image.url,
                           'name_pl': bundle.name_pl, 'slug': bundle.slug}
            bundle_sales = {'name': bundle.name, 'image_url': bundle.image.url, 'price_old': bundle.price_old,
                            'price_current': bundle.price_current, 'discount': bundle.discount, 'slug': bundle.slug}
            b_sales.append(bundle_sales)
            p_items.append(bundle_item)
            print('----------То что отдаем для отражения на ХОУМ', p_items)
            print('----------То что отдаем для отражения на ХОУМ', type(p_items))
            print(type(p_items[0]))
    return p_items, b_sales


def get_product_bundle(product, product_image_url):
    p_product = list()
    for p in product:
        try:
            product_page_item = {'name': p.name, 'name_pl': p.name_pl, 'image_url': product_image_url,
                                 'name_description': p.name_description ,'description': p.description,
                                 'category': p.category , 'description_1': p.description_1,
                                 'name_description_2': p.name_description_2, 'description_2': p.description_2,
                                 'name_description_3': p.name_description_3, 'description_3': p.description_3}
            p_product.append(product_page_item)
        except:
            pass

    return p_product


def get_products_in_sales(products_sales):
    p_sales = list()
    for p in products_sales:
        try:
            product = Product.objects.get(name=p.product_item.name)
            product_image = ProductImage.objects.get(is_active=True, is_main=True, product__is_active=True,
                                                     product=product)
            sales_item = {'name': p.product_item.name, 'image_url': product_image.image.url,
                          'price_old': p.price_old, 'price_current': p.price_current, 'discount': p.discount,
                          'slug': product.slug}
            p_sales.append(sales_item)
        except:
            pass
    return p_sales


def get_bundles_in_sales(bundles_sales):
    b_sales = list()
    for b in bundles_sales:
        try:
            sales_bundle = {'name': b.name, 'image_url': b.image.url,
                          'price_old': b.price_old, 'price_current': b.price_current, 'discount': b.discount,
                          'slug': b.slug}
            b_sales.append(sales_bundle)
        except:
            pass
    return b_sales

