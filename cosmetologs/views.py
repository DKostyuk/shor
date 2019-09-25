from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.shortcuts import render
from cosmetologs.models import *
from orders.forms import ServiceOrderForm
from landing.forms import LetterForm
from products.models import *
from landing.models import LetterTemplate, LetterEmail
from django.template.loader import render_to_string
from django.template import Context, Template



def cosmetolog(request, slug):
    cosmetolog = Cosmetolog.objects.get(slug=slug)
    cosmetolog_address = str(cosmetolog.street_cosmetolog.display_address) + ', ' + cosmetolog.house_cosmetolog
    services = ServiceProduct.objects.filter(cosmetolog = cosmetolog.id)
    service_products_images = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                                 service_product__is_active=True,
                                                                 service_product__is_visible=True,
                                                                 service_product__cosmetolog=cosmetolog.id)
    products = Product.objects.filter(cosmetolog=cosmetolog.id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True,
                                                                 product__is_active=True,
                                                                 product__cosmetolog=cosmetolog.id)
    # Need to do only first three or think about all service - Button
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # print(request.session.session_key)
    form = LetterForm()
    if request.POST:
        new_letter_form = LetterForm(request.POST)
        if new_letter_form.is_valid():
            new_letter = new_letter_form.save(commit=False)
            new_letter.cosmetolog = cosmetolog
            new_letter.cosmetolog_email = cosmetolog.order_email
            data = new_letter_form.cleaned_data
            new_letter.save()

            letter_template = LetterTemplate.objects.get(name="Request to Cosmetolog", is_active=True)
            to_list = [cosmetolog.order_email]
            bcc_email = [settings.EMAIL_HOST_USER]
            letter_emails = LetterEmail.objects.filter(letter_template_name=letter_template)
            if letter_emails:
                for letter_email in letter_emails:
                    bcc_email.append(letter_email.email_receiver)
            subject = letter_template.subject + ' --- ' + request.POST.get('subject', '')
            template = Template(letter_template.message)
            context = Context({"from_name": request.POST.get('from_name', ''),
                              "city_sender": request.POST.get('city_sender', ''),
                              "email_sender": request.POST.get('email_sender', ''),
                              "phone_sender": request.POST.get('phone_sender', '')
                               })
            message = render_to_string('cosmetologs/email_request_to_cosmetolog.html', {
                'template_message': template.render(context),
                'original_message': request.POST.get('message', ''),
            })
            from_email = settings.EMAIL_HOST_USER
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            msg = EmailMultiAlternatives(subject, message, from_email, to_list, bcc=bcc_email)
            msg.send()
            letter_success = "success"
        else:
            form = new_letter_form
            print(form.errors)

    return render(request, 'cosmetologs/cosmetolog.html', locals())


def service(request, slug2, slug1, slug):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    service_product = ServiceProduct.objects.get(slug=slug)
    cosmetolog = Cosmetolog.objects.get(slug=slug2)
    cosmetolog_address = str(cosmetolog.street_cosmetolog.display_address) + ', ' + cosmetolog.house_cosmetolog
    service_products_images = ServiceProductImage.objects.filter(is_active=True, is_main=True,
                                                                 service_product__is_active=True,
                                                                 service_product__is_visible=True,
                                                                 service_product__cosmetolog=cosmetolog.id).exclude(service_product=service_product)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True,
                                                  product__is_active=True,
                                                  product__cosmetolog=cosmetolog.id)
    form_service_order = ServiceOrderForm(request.POST or None)

    if request.POST:
        new_service_order_form = ServiceOrderForm(request.POST)
        if new_service_order_form.is_valid():
            new_service_order = new_service_order_form.save(commit=False)
            new_service_order.cosmetolog_id = cosmetolog
            new_service_order.cosmetolog = cosmetolog.name
            new_service_order.cosmetolog_email = cosmetolog.order_email
            new_service_order.service_product = service_product.name
            new_service_order.service_id = service_product
            new_service_order.price01 = service_product.price01
            new_service_order.price02 = service_product.price02
            new_service_order.discount = service_product.discount
            # session_key - condition has not to be send the same request/order during XX hours
            data = new_service_order_form.cleaned_data
            new_service_order.save()

            letter_template = LetterTemplate.objects.get(name="Service Order", is_active=True)
            to_list = [cosmetolog.order_email]
            bcc_email = [settings.EMAIL_HOST_USER]
            letter_emails = LetterEmail.objects.filter(letter_template_name=letter_template)
            if letter_emails:
                for letter_email in letter_emails:
                    bcc_email.append(letter_email.email_receiver)
            subject = letter_template.subject + ' --- ' + request.POST.get('subject', '')
            template = Template(letter_template.message)
            context = Context({"from_name": request.POST.get('customer_name', ''),
                               "city_sender": request.POST.get('customer_city', ''),
                               "email_sender": request.POST.get('customer_email', ''),
                               "phone_sender": request.POST.get('customer_phone', ''),
                               "service_product_name": service_product.name,
                               "service_product_price01": service_product.price01,
                               "service_product_price02": service_product.price02,
                               "service_product_discount": service_product.discount
                               })
            message = render_to_string('cosmetologs/email_service_order_to_cosmetolog.html', {
                'template_message': template.render(context),
                'original_message': request.POST.get('comments', ''),
            })
            from_email = settings.EMAIL_HOST_USER
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            msg = EmailMultiAlternatives(subject, message, from_email, to_list, bcc=bcc_email)
            msg.send()
            letter_success = "success"
        else:
            form_service_order = new_service_order_form
            print(form_service_order.errors)

    return render(request, 'cosmetologs/service.html', locals())
