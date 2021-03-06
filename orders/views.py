from django.http import JsonResponse
from .models import *
from products.models import ProductImage, Product
from landing.models import Page
from django.shortcuts import render
from .forms import OrderForm
from django.contrib import auth
from utils.emails import SendingEmail
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
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,
                                                                     pb_sale_id=product_sales_id,
                                                                     price_per_item=product_price, is_active=True,
                                                                     defaults={"nmb": nmb})
        print('created--------', new_product)

        if not created and (what_case == 11 or what_case == 12):
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

        if not created and (what_case == 21 or what_case == 22):
            new_product.nmb -= 1
            new_product.save(force_update=True)

        if not created and (what_case == 31 or what_case == 32):
            new_product.nmb += 1
            new_product.save(force_update=True)

        if not created and (what_case == 41 or what_case == 42):
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
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        product_dict["total_price"] = item.total_price

        product_dict["name"] = item.pb_sale.name_sales
        product_dict["product_id"] = item.pb_sale.id
        # product_dict["sales_type"] = 'item' - ???????????????????? ???????? ???? ?????? ???????? ?? ??????????????
        product_dict["modal_product_image_url"] = item.pb_sale.image_url
        # product_dict["product_volume"] = item.pb_sale.volume.name

        # product_dict["modal-product_image_url"] = 'somu undefined URL'
        return_dict["products"].append(product_dict)
    # return this data in AJAX
    return JsonResponse(return_dict)


def order_history(request):
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

    form = OrderForm(request.POST or None)

    if request.POST:
        new_order_form = OrderForm(request.POST)
        if new_order_form.is_valid() and products_in_basket:
            print('YEs-TES')
            # products_in_basket_1 = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
            # print(products_in_basket_1)

            # ?????????????? ?????????? ?????????????? ???????? ???? ???????????????????? ?? ???????????? ??????????
            new_order = new_order_form.save(commit=False)
            try:
                status = StatusOrder.objects.get(status_number=11)
                new_order.status_id = status.id
            except:
                status = None
            username_id = auth.get_user(request).id
            try:
                cosmetolog = Cosmetolog.objects.get(user=username_id, is_active=True)
                new_order.cosmetolog = cosmetolog
            except:
                new_order.cosmetolog = None
            new_order.save()

            # ?????????????? ???????????????? ?? ???????????? ???? ???????????? ????????, ?????? ???????????????? ?? ?????????????? -
            # #?????????????????? ?????????? ???????????????????? ?????????????? ????????????????
            for p in products_in_basket:
                ProductInOrder.objects.create(pb_sale=p.pb_sale, nmb=p.nmb, price_per_item=p.price_per_item,
                                              order=new_order)
                p.is_active = False
                p.save(force_update=True)
            try:
                order_text_object = Page.objects.get(is_active=True, page_name="ORDER_SUCCESS")
            except:
                order_text_object = None
            form = OrderForm()
            request.session["order_number"] = new_order.order_number
            #  ???????????????? email - ?? ???????????????? ???????????? ?????? ?????????? ??????????????
            try:
                email = SendingEmail()
                email.sending_email(type_id=3, email_details=new_order)
            except:
                pass

            return render(request, 'orders/order_success.html', locals())

        else:
            print('NO valid')

    return render(request, 'orders/checkout.html', locals())


def basket_update(request):
    #// request is data-dictionary that is recieving from JQuery code
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_basket_id = data.get("product_basket_id")
    nmb = data.get("nmb")
    try:
        new_product = ProductInBasket.objects.get(session_key=session_key, id=product_basket_id, is_active=True)
        new_product.nmb = nmb
        new_product.save(force_update=True)
    except:
        print('??????-???? ?????????? ???? ?????? - ???????????????? ?? ?????????????? ???? ??????????????')

    return JsonResponse(return_dict)
