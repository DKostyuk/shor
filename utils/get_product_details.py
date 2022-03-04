from products.models import *


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
