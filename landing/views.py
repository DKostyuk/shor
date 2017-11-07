from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import SubscriberForm
from products.models import *
from landing.models import *
from blogs.models import *
from cosmetologs.models import *
from addresses.models import *


def landing(request):
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
    name = "DimaKostyuk"
    current_day = "31.05.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # print (request.POST)
        # print (form.cleaned_data)
        data = form.cleaned_data
        # print (data["name"])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
    address_cosmetologs = Cosmetolog.objects.filter(is_active=True)
    cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
    search_active_addresses = Address.objects.filter(is_active=True)
    active_addresses = search_active_addresses.filter(
        Q(type_id=5) |
        Q(type_id=4)
    ).order_by('type_id')
    service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
    service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)
    service_products_images_all = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                                     service_product__is_active=True,
                                                                     service_product__is_visible=True)
    service_products_images = service_products_images_all[:4]
    cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)
    slider_mains = SliderMain.objects.filter(is_active=True)
    slider_mains_counts = range(slider_mains.count() - 1)
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
    blogs_images_all = BlogImage.objects.filter(is_active=True, is_main=True)
    blogs_images = blogs_images_all[:4]
    products_images_all = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images = products_images_all[:4]
    products_images_new = products_images_all.filter(product__category__id=1)
    products_images_popular = products_images_all.filter(product__category__id=2)

    return render(request, 'landing/home.html', locals())


def salon(request):
    if 'q' in request.GET:
        q_full_address = request.GET.get('q')
        q_service = request.GET.get('q1')
        print('salon - q_full_address:', q_full_address)
        print(type(q_full_address))
        print('salon - q_service:', q_service)

        if not q_full_address and not q_service:
            error = True
            return HttpResponseRedirect(reverse(home), {'error': error})
        else:
            url_address = str()
            url_service = str()
            if q_full_address:
                search_active_addresses = Address.objects.filter(is_active=True)
                search_active_addresses_url = search_active_addresses.get(display_address=q_full_address)
                url_address = search_active_addresses_url.url
            if q_service:
                service_set = set()
                service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
                for i in service_categories:
                    service_set.add(i.name)
                if q_service in service_set:
                    url_service = slugify(q_service)
                else:
                    subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
                    subservice_categories_url = subservice_categories.get(subcategory_category=q_service)
                    url_service = subservice_categories_url.url

            url_full = url_service + url_address + "/"
            print('url_address  ', url_address)
            print('url_service  ', url_service)
            print('url_full', url_full)
            if q_full_address and not q_service:
                return HttpResponseRedirect('/cosmetolog-in' + url_full)
            elif not q_full_address and q_service:
                return HttpResponseRedirect('/service-in-Poland/' + url_full)
            else:
                return HttpResponseRedirect(url_full)
    else:
        return HttpResponseRedirect(reverse(home))


def get_city_id(q_city):
    q_address_url = '/' + q_city
    search_active_addresses = Address.objects.filter(is_active=True)
    search_city_active_addresses = search_active_addresses.get(url__exact=q_address_url)
    city_id = search_city_active_addresses.id

    cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
    search_cosmetolog_addresses = cosmetolog_addresses.filter(address_id=city_id)
    cosmetolog_set = set()
    for j in search_cosmetolog_addresses:
        cosmetolog_set.add(j.cosmetolog_id)

    return city_id, cosmetolog_set


def get_delnica_ulica_id(q_city, q_delnica_ulica):
    q_address_url = '/' + q_city + '/' + q_delnica_ulica
    search_active_addresses = Address.objects.filter(is_active=True)
    search_city_active_addresses = search_active_addresses.get(url__exact=q_address_url)
    delnica_ulica_id = search_city_active_addresses.id
    delnica_ulica_type_id = search_city_active_addresses.type_id
    delnica_ulica_parent_id = search_city_active_addresses.parent_id

    return delnica_ulica_id, delnica_ulica_type_id, delnica_ulica_parent_id


def q_search_in_url(q_city, q_delnica_ulica):
    cosmetolog_set = set()
    cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True,
                                                            address_name__url__icontains=q_city and q_delnica_ulica)
    for i in cosmetolog_addresses:
        cosmetolog_set.add(i.cosmetolog_id)

    if q_delnica_ulica != q_city:
        delnica_ulica_id, delnica_ulica_type_id, delnica_ulica_parent_id = get_delnica_ulica_id(q_city, q_delnica_ulica)
        if delnica_ulica_type_id == 10:
            print('Это улица   ', delnica_ulica_type_id)
            cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True,
                                                                    cosmetolog_id__exact=delnica_ulica_parent_id)
            for j in cosmetolog_addresses:
                cosmetolog_set.add(j.cosmetolog_id)
        elif delnica_ulica_type_id == 5:
            print('Это дельница   ', delnica_ulica_type_id)

    return cosmetolog_set


def search_service_address(request, q_1, q_2=None, q_3=None, q_4=None):

    print('search - q1:', q_1)
    print('search - q2', q_2)
    print('search - q3', q_3)
    print('search - q4', q_4)
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)

    #проверка - является ли q2 субсервисом
    subservice_set = set()
    subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
    for i in subservice_categories:
        subservice_set.add(i.slug)
    service_set = set()
    if q_2 in subservice_set:
        # надо выбрать всех косметологов у которых установлен этот СУБ_сервис q_2
        print('YES YES YES YES')
        service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
                                                         subcategory__slug__icontains=q_2)
        print(service_products)
        for i in service_products:
            service_set.add(i.cosmetolog_id)
        print('только для суб сервиса', service_set)
        query_service = q_1.capitalize() + ', ' + q_2.capitalize()
        # соответсвенно q_3 является городом
        # проверяем наличие q_4
        if q_4:
            # пишем код для q_3 и q_4
            # выбираем всех косметологов у которых есть адресс q_3 и q_4 (на них фокус), или q_3
            cosmetolog_address_set = q_search_in_url(q_3, q_4)
            print('после вызова функции - только city and delnica/ulica q_3 q_4  ', cosmetolog_address_set)
            city_id, cosmetolog_set = get_city_id(q_3)
            cosmetolog_address_set.update(cosmetolog_set)
            print('после вызова функции - только city and delnica/ulica q_3 q_4 +++++ ', cosmetolog_address_set)
            query_address = q_3.capitalize() + ', ' + q_4.capitalize()

        else:
            # пишем код для q_3 (вызываем функцию с параметром q_3, в которой
            # выбираем всех косметологов у которых есть адрес q3 включая вглубь
            cosmetolog_address_set = q_search_in_url(q_3, q_3)
            print('после вызова функции - только city q_3  ', cosmetolog_address_set)
            query_address = q_3.capitalize()

        # пересекаем множества сервиса и косметологов
        search_cosmetologs_set = service_set & cosmetolog_address_set
        print('final search_cosmetologs_set    ', search_cosmetologs_set)
        cosmetolog_count = len(search_cosmetologs_set)
    else:
        # q_2 не является субсервисом
        # надо выбрать всех косметолголов у которых установлен этот Сервис q_1
        print('NO NO NO NO')
        service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
                                                         category__slug__icontains=q_1)
        print(service_products)
        for i in service_products:
            service_set.add(i.cosmetolog_id)
        print('только для суб сервиса', service_set)
        query_service = q_1.capitalize()
        # соответсвенно q_2 является городом
        # проверяем наличие q_3
        if q_3:
            # пишем код для q_2 и q_3
            # выбираем всех косметологов у которых есть адресс q_2 и q_3 (на них фокус), или q_2
            cosmetolog_address_set = q_search_in_url(q_2, q_3)
            print('после вызова функции - только city and delnica/ulica q_3 q_4  ', cosmetolog_address_set)
            city_id, cosmetolog_set = get_city_id(q_2)
            cosmetolog_address_set.update(cosmetolog_set)
            print('после вызова функции - только city and delnica/ulica q_3 q_4 +++++ ', cosmetolog_address_set)
            query_address = q_2.capitalize() + ', ' + q_3.capitalize()
        else:
            # пишем код для q_2 (вызываем функцию с параметром q_2, в которой
            # выбираем всех косметологов у которых есть адрес q2 включая вглубь
            cosmetolog_address_set = q_search_in_url(q_2, q_2)
            print('после вызова функции - только city q_2  ', cosmetolog_address_set)
            query_address = q_2.capitalize()
        search_cosmetologs_set = service_set & cosmetolog_address_set
        print('final search_cosmetologs_set    ', search_cosmetologs_set)
        cosmetolog_count = len(search_cosmetologs_set)

    # address_cosmetologs = Cosmetolog.objects.filter(is_active=True)
    # cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
    # search_active_addresses = Address.objects.filter(is_active=True)
    # service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
    # service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)


    cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)

    search_service_products_images = ServiceProductImage.objects.filter(
        is_active=True, is_main=True, service_product__is_active=True,
        service_product__is_visible=True, service_product__cosmetolog__id__in=search_cosmetologs_set)
    # search_service_products_images = service_products_images_all.filter(
    #     Q(service_product__in=d)
    # )
    # service_products_images = service_products_images_all[:4]
    search_cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True, id__in=search_cosmetologs_set)

    search_service_address_999 = 999

    if cosmetolog_count != 0:
        return render(request, 'landing/search_results.html', locals())
    else:
        return render(request, 'landing/no_search_results.html', locals())


def search_service(request, q_1, q_2=None, q_3=None):
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)

    search_active_addresses = Address.objects.filter(is_active=True)
    active_addresses = search_active_addresses.filter(
        Q(type_id=5) |
        Q(type_id=4)
    ).order_by('type_id')

    active_addresses_towns = active_addresses.filter(type_id=4)
    for i in active_addresses_towns:
        i.slug = slugify(i.name)
    subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
    service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
    # Ввели сервис но нету адресу - выводим список косметологов с таким сервисом по всей стране
    # фокус на адресс - ВВЕДИТЕ поиск по адресу
    service_set = set()
    if q_2:
        service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
                                                         subcategory__slug__icontains=q_2)
        print(service_products)
        for i in service_products:
            service_set.add(i.cosmetolog_id)
        print('только для суб сервиса', service_set)
        query_service_item = subservice_categories.get(slug=q_2)
        query_service = query_service_item.subcategory_category

        search_cosmetologs_set = service_set
        print('final search_cosmetologs_set    ', search_cosmetologs_set)
        cosmetolog_count = len(search_cosmetologs_set)
    else:
        service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
                                                         category__slug__icontains=q_1)
        print(service_products)
        for i in service_products:
            service_set.add(i.cosmetolog_id)
        print('только для суб сервиса', service_set)
        query_service_item = service_categories.get(slug=q_1)
        query_service = query_service_item.name

        search_cosmetologs_set = service_set
        print('final search_cosmetologs_set    ', search_cosmetologs_set)
        cosmetolog_count = len(search_cosmetologs_set)

    search_cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True, id__in=search_cosmetologs_set)
    search_service_products_images = ServiceProductImage.objects.filter(
        is_active=True, is_main=True, service_product__is_active=True,
        service_product__is_visible=True, service_product__cosmetolog__id__in=search_cosmetologs_set)
    search_service_999 = 999
    if cosmetolog_count != 0:
        return render(request, 'landing/search_results.html', locals())
    else:
        return render(request, 'landing/no_search_results.html', locals())


def search_address(request, q_1, q_2=None, q_3=None):
    # Ввели аддрес но нету сервиса - выводим список косметологов по этому адресу с любым сервисом
    # фокус на сервис - ВЫБЕРИТЕ СЕРВИС
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)

    search_active_addresses = Address.objects.filter(is_active=True)
    active_addresses = search_active_addresses.filter(
        Q(type_id=5) |
        Q(type_id=4)
    ).order_by('type_id')

    # active_addresses_towns = active_addresses.filter(type_id=4)
    # for i in active_addresses_towns:
    #     i.slug = slugify(i.name)
    subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
    service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
    if q_2:
        # пишем код для q_1 и q_2
        # выбираем всех косметологов у которых есть адресс q_2 и q_3 (на них фокус), или q_2
        cosmetolog_address_set = q_search_in_url(q_1, q_2)
        print('после вызова функции - только city and delnica/ulica q_1 q_2  ', cosmetolog_address_set)
        city_id, cosmetolog_set = get_city_id(q_1)
        cosmetolog_address_set.update(cosmetolog_set)
        print('после вызова функции - только city and delnica/ulica q_1 q_2 +++++ ', cosmetolog_address_set)
        query_address_id, w2, w3 = get_delnica_ulica_id(q_1, q_2)
        query_address = Address.objects.get(id=query_address_id).display_address
    else:
        # пишем код для q_1 (вызываем функцию с параметром q_1, в которой
        # выбираем всех косметологов у которых есть адрес q1 включая вглубь
        cosmetolog_address_set = q_search_in_url(q_1, q_1)
        print('после вызова функции - только city q_1  ', cosmetolog_address_set)
        query_address_id, w2_set = get_city_id(q_1)
        query_address = Address.objects.get(id=query_address_id).display_address
    search_cosmetologs_set = cosmetolog_address_set
    print('final search_cosmetologs_set    ', search_cosmetologs_set)
    cosmetolog_count = len(search_cosmetologs_set)

    search_cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True, id__in=search_cosmetologs_set)
    search_service_products_images = ServiceProductImage.objects.filter(
        is_active=True, is_main=True, service_product__is_active=True,
        service_product__is_visible=True, service_product__cosmetolog__id__in=search_cosmetologs_set)
    search_address_999 = 999

    if cosmetolog_count != 0:
        return render(request, 'landing/search_results.html', locals())
    else:
        return render(request, 'landing/no_search_results.html', locals())
