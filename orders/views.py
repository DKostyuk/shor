from django.http import JsonResponse
from .models import *
from products.models import ProductImage
from django.shortcuts import render
from .forms import CheckoutContactForm
from django.contrib import auth


def basket_adding(request):
    #// request is data-dictionary that is recieving from JQuery code
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    print('--------', data)

    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")
    product_price = data.get("price")
    check_me = data.get("check_me")
    what_case = int(data.get("what_case"))
    print('---CHECK ME-----', check_me)
    print('---What Case-----', what_case, '----', type(what_case))

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     price_per_item=product_price, is_active=True,
                                                                     defaults={"nmb": nmb})
        if not created and what_case == 1:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

        if not created and what_case == 2:
            new_product.nmb -= 1
            new_product.save(force_update=True)

        if not created and what_case == 3:
            new_product.nmb += 1
            new_product.save(force_update=True)

        if not created and what_case == 4:
            new_product.nmb = nmb
            new_product.save(force_update=True)

    #common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        print('ЧТО-ЧТО', item.id)
        product_dict["name"] = item.product.name
        product_dict["product_id"] = item.product.id
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        product_dict["total_price"] = item.total_price
        print('-----Total Price---------------', type(product_dict["total_price"]))
        product_dict["modal_product_image_url"] = ProductImage.objects.get(product=item.product, is_active=True,
                                                                           is_main=True, product__is_active=True).image.url
        # product_dict["modal-product_image_url"] = 'somu undefined URL'
        return_dict["products"].append(product_dict)
    print(return_dict)
    # return this data in AJAX
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    form = CheckoutContactForm(request.POST or None)

    if request.POST:
        form_01 = request.POST
        print('--------CheckOUT----------', request.POST)
    #     возможно для не авторизированныхъ надо ввести проверку валидации формы
        data = request.POST

        order = Order.objects.create(user=username, status_id=1)

        for name, value in data.items():
            if name.startswith('product_in_basket_'):
                product_in_basket_id = name.split('product_in_basket_')[1]
                product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                product_in_basket.nmb = value

                product_in_basket.save(force_update=True)

                ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb,
                                              order=order)
                # price_per_item = product_in_basket.price_per_item,
                # total_price = product_in_basket.total_price,


                product_in_basket.order = order
                product_in_basket.is_active = False
                product_in_basket.save(force_update=True)

    return render(request, 'orders/checkout.html', locals())
