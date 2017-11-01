from django.shortcuts import render
from products.models import *


def product(request, slug):
    product = Product.objects.get(slug=slug)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    # print(request.session.session_key)

    return render(request, 'products/product.html', locals())
