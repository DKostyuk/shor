from django.http import JsonResponse
from .models import *
from products.models import ProductImage
from landing.models import Page
from django.shortcuts import render
from .forms import OrderForm
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect


def basket_adding(request):
    #// request is data-dictionary that is recieving from JQuery code
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST

    product_sales_id = data.get("product_sales_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")
    product_price = float(data.get("price").replace(",", "."))
    what_case = int(data.get("what_case"))

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_sales_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_sales_id,
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
        product_dict["name"] = item.product.product_item.name
        product_dict["product_volume"] = item.product.product_item.volume.name
        product_dict["product_id"] = item.product.id
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        product_dict["total_price"] = item.total_price
        product = Product.objects.get(name=item.product.product_item.name)
        product_dict["modal_product_image_url"] = ProductImage.objects.get(product=product, is_active=True,
                                                                           is_main=True,
                                                                           product__is_active=True).image.url
        # product_dict["modal-product_image_url"] = 'somu undefined URL'
        return_dict["products"].append(product_dict)
    print(return_dict)
    # return this data in AJAX
    return JsonResponse(return_dict)


def order_history(request):
    print('----ORDER HISTORY---------')
    session_key = request.session.session_key
    order_text_object = Page.objects.get(is_active=True, page_name="ORDER_SUCCESS")
    new_order_number = request.session["order_number"]

    return render(request, 'orders/order_history.html', locals())


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    payment_money_sum = 0
    payment_nmb_sum = 0
    for p in products_in_basket:
        payment_money_sum += p.total_price
        payment_nmb_sum += p.nmb
    print('-----Before--POST---', payment_money_sum, payment_nmb_sum)

    form = OrderForm(request.POST or None)

    if request.POST:
        new_order_form = OrderForm(request.POST)
        print('--------CheckOUT----------', request.POST)
        print('--------CheckOUT322222----------', form)
        print('sdvsdvdsvds-------', products_in_basket)
        print('sdvsdvdsvds---AFTER post----', payment_money_sum, payment_nmb_sum)
        if new_order_form.is_valid() and products_in_basket:
            print('YEs-TES')
            # products_in_basket_1 = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
            # print(products_in_basket_1)

            # создать Заказ включая инфо по Получателю и статус новый
            new_order = new_order_form.save(commit=False)
            status = StatusOrder.objects.get(name='NEW')
            new_order.status_id = status.id
            username_id = auth.get_user(request).id
            cosmetolog = Cosmetolog.objects.get(user=username_id, is_active=True)
            new_order.cosmetolog = cosmetolog
            new_order.save()

            # создать Продукты в Заказе на основе того, что осталось в корзине - Проверить после реализации функции удаления
            for p in products_in_basket:
                print(p)
                ProductInOrder.objects.create(product=p.product, nmb=p.nmb, price_per_item=p.price_per_item,
                                              order=new_order)
                p.is_active = False
                p.save(force_update=True)
            order_text_object = Page.objects.get(is_active=True, page_name="ORDER_SUCCESS")
            form = OrderForm()
            request.session["order_number"] = new_order.order_number

            return render(request, 'orders/order_success.html', locals())
            # return HttpResponseRedirect(reverse(order_history))
            # return render(request, 'orders/order_history.html', locals())

            #  Проверить - отправка email - с деталями заказа или после созвона
            # Проверить подумать Куда направлять - типа УСПЕХ страница и с Вами созвоняться по вопросам Оплаты и Доставки
        #     вот страница Заказов - и какую инфо там показывать - Розетка и/или Эпицентр

        else:
            print('NOW')

    return render(request, 'orders/checkout.html', locals())


def basket_update(request):
    #// request is data-dictionary that is recieving from JQuery code
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_basket_id = data.get("product_basket_id")
    nmb = data.get("nmb")
    new_product = ProductInBasket.objects.get(session_key=session_key, id=product_basket_id, is_active=True)
    new_product.nmb = nmb
    new_product.save(force_update=True)

    return JsonResponse(return_dict)
