from .models import ProductInBasket
from landing.models import LogoImage, Feature, Subscriber
from products.models import ProductCategory
from django.contrib import auth
from cosmetologs.models import *


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        #workaround for newer Django versions
        request.session["session_key"] = 123
        #re-apply value
        request.session.cycle_key()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    try:
        logo_images = LogoImage.objects.get(is_active=True, is_main=True)
    except:
        pass
    product_lines = ProductCategory.objects.filter(is_active=True).order_by('id')

    username = auth.get_user(request).username
    username_id = auth.get_user(request).id
    try:
        # print('---CONTEXT-------username_id-----', username_id, username)
        cosmetolog = Cosmetolog.objects.get(user=username_id, is_active=True)
    except:
        cosmetolog = None
    # print('--CONTEXT-----HERE HOM and COSMO -----', cosmetolog, type(cosmetolog))
    try:
        sale_feature = Feature.objects.get(feature_code=101, is_active=True)
        bonus_feature = Feature.objects.get(feature_code=202, is_active=True)
    except:
        sale_feature = None
        bonus_feature = None

    return locals()
