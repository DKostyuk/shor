from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from cosmetologs.models import *
from orders.forms import ServiceOrderForm


def cosmetolog(request, slug):
    cosmetolog = Cosmetolog.objects.get(slug=slug)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    # print(request.session.session_key)

    return render(request, 'cosmetologs/cosmetolog.html', locals())


def service(request, slug1, slug):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    service_product = ServiceProduct.objects.get(slug=slug)
    form_service_order = ServiceOrderForm(request.POST or None)

    if request.method == 'POST':
    #     print(form_service_order)
    #     print(request.POST)
    #     print(form_service_order.is_valid())
    #     print(form_service_order.errors)

        data = request.POST
        print(data)
        service_product_id = data.get("service_id")
        service_name = data.get("service_product")
        service_price = data.get("total_price")

        print(service_product_id)
        print(service_name)
        print(service_price)
    # is_delete = data.get("is_delete")

    # if request.method == 'POST' and form_service_order.is_valid():
    #     new_form = form_service_order.save()

        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        # subject = 'Thank you for Order Our Service'
        # message = 'Thank YOU!!!!!!/n One more time thanx/n DKOSTIUK'
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [new_form.customer_email, settings.EMAIL_HOST_USER]

        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        # data = form_service_order.cleaned_data
        # print(data["customer_email"])
        # print(new_form.customer_email)
        # print(from_email)
        # print(to_list)
        # return render(request, 'cosmetologs/thanks.html', locals())
    # session_key = request.session.session_key
    # if not session_key:
    #     request.session.cycle_key()
    #
    # print(request.session.session_key)

    return render(request, 'cosmetologs/service.html', locals())
