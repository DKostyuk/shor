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
                search_active_addresses_url = search_active_addresses.get(id=q_full_address)
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
                    subservice_categories_url = subservice_categories.get(id=q_service)
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
            # if q_full_address and not q_service:
            # # return HttpResponseRedirect(url_full) -
            # # надо возвращать для разных вариантов разные реьд - с инфо + призыв ввести полный поисковый запос
            # #надо вернуть список всех косметологов с активного адреса с любым сервисом - подумать о порядке сортировки
            # elif not q_full_address and q_service:
            #     # надо вернуть список всех косметологов с таким сервисом - подумать опордяке сортировки
            # else:
            #
            # return HttpResponseRedirect(reverse(home))


        # return HttpResponseRedirect(reverse(search, args=[query1, query]))
        # return HttpResponseRedirect(url + "?%s" % params)
        # return render(request, 'landing/search.html', locals())
        # return HttpResponseRedirect(reverse('salon', args=(query1, query,)))
    else:
        return HttpResponseRedirect(reverse(home))


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
    if q_2 in subservice_set:
        # надо выбрать всех косметологов у которых установлен этот СУБ_сервис
        print('YES YES YES YES')

    else:
        # надо выбрать всех косметолголов у которых установлен этот Сервис
        print('NO NO NO NO')

    address_cosmetologs = Cosmetolog.objects.filter(is_active=True)
    cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
    search_active_addresses = Address.objects.filter(is_active=True)
    service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
    service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)
    service_products_images_all = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                                     service_product__is_active=True,
                                                                     service_product__is_visible=True)
    service_products_images = service_products_images_all[:4]
    cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)
    # query = request.GET.get('q')
    # query1 = request.GET.get('q1')

    return render(request, 'landing/search.html', locals())


def search_service(request, q1, q2=None, q3=None):
    # Ввели сервис но нету адресу - выводим список косметологов с таким сервисом по всей стране
    # фокус на адресс - ВВЕДИТЕ поиск по адресу
    print('search - q1:', q1)
    print('search - q2', q2)
    print('search - q3', q3)
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
    q_service = q1
    service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)
    service_products_images_all = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                                     service_product__is_active=True,
                                                                     service_product__is_visible=True)
    service_products_images = service_products_images_all[:4]
    cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)
    search_service_products = service_products.filter(
        Q(category__name__icontains=q_service)
    )
    d = set()
    for n in search_service_products:
        d.add(n.id)
    search_service_products_images = service_products_images_all.filter(
        Q(service_product__in=d)
    )
    return render(request, 'landing/search_service.html', locals())


def search_address(request, q1, q2=None, q3=None):
    # Ввели аддрес но нету сервиса - выводим список косметологов по этому адресу с любым сервисом
    # фокус на сервис - ВЫБЕРИТЕ СЕРВИС
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
    q_city = q1.capitalize()
    q_address = q1.capitalize()
    q_address_url = '/' + q1
    search_active_addresses = Address.objects.filter(is_active=True)
    search_city_active_addresses = search_active_addresses.get(url__exact=q_address_url)
    search_city_id = search_city_active_addresses.id
    cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
    search_cosmetolog_addresses = cosmetolog_addresses.filter(address_id=search_city_id)
    cosmetolog_set = set()
    for j in search_cosmetolog_addresses:
        cosmetolog_set.add(j.cosmetolog_id)
    cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)
    if q2:
        q_address_url += '/' + q2
        q_address += ', ' + q2.capitalize()
        search_delnica_active_addresses = search_active_addresses.get(url__exact=q_address_url)
        search_delnica_id = search_delnica_active_addresses.id
        search_cosmetolog_addresses = cosmetolog_addresses.filter(address_id=search_delnica_id)
        for j in search_cosmetolog_addresses:
            cosmetolog_set.add(j.cosmetolog_id)
        search_cosmetologs = cosmetologs.filter(
            Q(id__in=cosmetolog_set)
        )
        # if q3:    # это если будет приходить (то есть будем давать выбор искать по номеру дома)
        #     q_address_url += '/' + q3
        #     q_ulica = q3.capitalize()
        #     search_ulica_active_addresses = search_active_addresses.get(url__exact=q_address_url)
        #     search_ulica_id = search_ulica_active_addresses.id
    else:
        search_city_active_addresses = search_active_addresses.filter(
            Q(url__icontains=q_city)
        )
        search_city_active_addresses_id_set = set()
        for i in search_active_addresses:
            search_city_active_addresses_id_set.add(i.id)
        search_cosmetolog_addresses = cosmetolog_addresses.filter(
            Q(address_id__in=search_city_active_addresses_id_set)
        )
        for j in search_cosmetolog_addresses:
            cosmetolog_set.add(j.cosmetolog_id)
        search_cosmetologs = cosmetologs.filter(
            Q(id__in=cosmetolog_set)
        )



    # address_cosmetologs = Cosmetolog.objects.filter(is_active=True)


    # service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
    # service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)
    # service_products_images_all = ServiceProductImage.objects.filter(is_active=True, is_main=True,
    #                                                                  service_product__is_active=True,
    #                                                                  service_product__is_visible=True)
    # service_products_images = service_products_images_all[:4]
    #

    # search_active_addresses = search_active_addresses.filter(
    #     Q(url__icontains=q_address)
    # )

    # search_service_products = service_products.filter(
    #     Q(cosmetolog_id__in=a)
    # )
    # d = set()
    # for n in search_service_products:
    #     d.add(n.id)
    # search_service_products_images = service_products_images_all.filter(
    #     Q(service_product__in=d)
    # )

    return render(request, 'landing/search_address.html', locals())
