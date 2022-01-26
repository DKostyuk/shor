from .models import ProductInBasket
from landing.models import LogoImage, Subscriber
from products.models import ProductCategory
from django.contrib import auth


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        #workaround for newer Django versions
        request.session["session_key"] = 123
        #re-apply value
        request.session.cycle_key()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    products_total_nmb = products_in_basket.count()
    logo_images = LogoImage.objects.get(is_active=True, is_main=True)
    # print('u_user', u_user, type(u_user))
    username = auth.get_user(request).username
    product_lines = ProductCategory.objects.filter(is_active=True)
    return locals()
