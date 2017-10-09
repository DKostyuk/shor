from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from landing.models import *
from blogs.models import *
from cosmetologs.models import *


def landing(request):
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
    name = "DimaKostyuk"
    current_day = "31.05.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        print (data["name"])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
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

    # print(products_images_all)

    # query = request.GET.get('q')
    # if query:
    #     queryset_list = queryset_list.filter
    return render(request, 'landing/home.html', locals())

