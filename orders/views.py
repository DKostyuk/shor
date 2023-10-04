import datetime

from django.http import JsonResponse

from bonuses.models import BonusAccountCosmetolog
from stock.models import StockItemReserved, StockItemRest
from .models import *
from products.models import ProductImage, Product, SaleProductItem, ProductItem
from landing.models import Page
from django.shortcuts import render
from .forms import OrderForm
from django.contrib import auth
from utils.emails import SendingEmail
import requests
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
    print('цена продукта-- пришла', product_price)
    what_case = int(data.get("what_case"))
    username = auth.get_user(request)
    if username.id is not None:
        user_buyer = username.username
    else:
        user_buyer = "Anonymous"
    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_sales_id).update(is_active=False)
    else:
        print('цена продукта-- пришла', product_price)
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,
                                                                     pb_sale_id=product_sales_id, user=user_buyer,
                                                                     price_per_item=product_price, is_active=True,
                                                                     defaults={"nmb": nmb})
        print('created--------', new_product, new_product.price_per_item, new_product.user)

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
        # product_dict["sales_type"] = 'item' - Посмотреть надо ли эта инфо в таблице
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
    username_id = auth.get_user(request).id
    print('username_id   ', username_id)
    try:
        cosmetolog = Cosmetolog.objects.get(user=username_id, is_active=True)
        print('Cosmo    ', cosmetolog)
        bonus_set = BonusAccountCosmetolog.objects.filter(cosmetolog=cosmetolog, balance_sum_status__ref_number='11')
    except:
        cosmetolog = None
        bonus_set = None
    print('bonus_set   ', bonus_set)
    form = OrderForm(request.POST or None)
    bonus_dic = {}
    for b in bonus_set:
        bonus_key_value = str(b.bonus_account) + ' ' + str(b.balance_sum)
        bonus_dic[b.id] = bonus_key_value
    print('bonus_dic    ', bonus_dic)
    bonus_list = bonus_dic.items()
    print('bonus_list   ', bonus_list)
    if request.POST:
        new_order_form = OrderForm(request.POST)
        print('new_order_form    ', new_order_form)
        print('request.POST[cosmetolog_bonus', request.POST)
        if new_order_form.is_valid() and products_in_basket:
            print('YEs-TES')
            # products_in_basket_1 = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
            # print(products_in_basket_1)

            # создать Заказ включая инфо по Получателю и статус новый
            new_order = new_order_form.save(commit=False)

            try:
                status = StatusOrder.objects.get(status_number=11)
                new_order.status_id = status.id
            except:
                status = None

            new_order.cosmetolog = cosmetolog
            new_order.save()

            # создать Продукты в Заказе, Stock Reserved на основе того, что осталось в коpзине -
            # #Проверить после реализации функции удаления
            for p in products_in_basket:
                ProductInOrder.objects.create(pb_sale=p.pb_sale, nmb=p.nmb, price_per_item=p.price_per_item,
                                              order=new_order)
                s = SaleProductItem.objects.get(sales_product=p.pb_sale)
                product_item = ProductItem.objects.get(id=s.product_item.id)
                StockItemReserved.objects.create(product_item=product_item, num_reserved=p.nmb, order=new_order)
                try:
                    product_rest_set = StockItemRest.objects.filter(product_item=product_item)
                    print('--set--set--', product_rest_set)
                    product_due_date = datetime.datetime(9999, 1, 1)
                    for product_rest_item in product_rest_set:
                        if product_rest_item.due_date < product_due_date:
                            product_due_date = product_rest_item.due_date
                            pr_item = product_rest_item
                    pr_item.num_rest -= p.nmb
                    pr_item.save(force_update=True)
                except:
                    pass
                p.is_active = False
                p.order = new_order
                p.save(force_update=True)
            try:
                order_text_object = Page.objects.get(is_active=True, page_name="ORDER_SUCCESS")
            except:
                order_text_object = None
            form = OrderForm()
            request.session["order_number"] = new_order.order_number
            #  Отправка email - с деталями заказа или после созвона
            try:
                email = SendingEmail()
                email.sending_email(type_id=3, email_details=new_order)
                message = 'Новий заказ з сайта - ' + str(new_order.order_number)
                msg = SendingMessage()
                msg.sending_msg(message=message)
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
        print('ЧТО-ТО ПОШЛО НЕ ТАК - продукты в корзине не найдены')

    return JsonResponse(return_dict)


def order_admin_ajax(request):
    data = request.POST
    return_dict = dict()
    return_dict["check"] = 'check_forever'
    cosmetolog_details = Cosmetolog.objects.get(id=data['cosmetolog_id'])
    return_dict = {
        'receiver_name': cosmetolog_details.cosmetolog_name,
        'receiver_surname': cosmetolog_details.cosmetolog_surname,
        'receiver_father_name': cosmetolog_details.cosmetolog_father_name,
        'receiver_email': cosmetolog_details.email,
        'receiver_tel_number': cosmetolog_details.tel_number,
    }

    return JsonResponse(return_dict)
