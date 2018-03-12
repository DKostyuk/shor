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
    logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
    username = auth.get_user(request).username
    user_current = Subscriber.objects.filter(email=username).first()
    if user_current:
        username = user_current.name
        user_email = user_current.email
        user_id = user_current.id
        if user_current.nip:
            user_nip = user_current.nip
        if user_current.company_name:
            user_company_name = user_current.company_name
        user_company_confirm = user_current.company_confirm
        if user_current.tel_number:
            user_tel_number = user_current.tel_number
        if user_current.index:
            user_index = user_current.index
        if user_current.city:
            user_city = user_current.city
        if user_current.street:
            user_street = user_current.street
        if user_current.locality:
            user_locality = user_current.locality

    product_lines = ProductCategory.objects.filter(is_active=True)
    return locals()
