from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import *
from products.models import *
from landing.models import *
from blogs.models import *
from cosmetologs.models import *
from addresses.models import *
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail
from django.conf import settings
import random


def another(request):
    tricks_all = AnotherTrick.objects.filter(is_active=True)
    name = "DimaKostyuk"
    current_day = "24.04.2018"

    return render(request, 'another/another.html', locals())
#
#
# def validate_save_user_send_email(request, newuser_form, email_1, username_original):
#     # if newuser_form.is_valid():
#     args_1 = {}
#     newuser = newuser_form.save(commit=False)
#     newuser.is_active = False
#     newuser.save()
#     # subscriber_current = Subscriber.objects.get(email=email_1)
#     subscriber_current = Subscriber.objects.get(user__username=email_1)
#     subscriber_current.email = email_1
#     subscriber_current.name = username_original
#     subscriber_current.save()
#     # Email sending code:
#     current_site = get_current_site(request)
#     mail_subject = 'Activate your blog account on Site RENEW for example.'
#     message = render_to_string('landing/acc_confirmation_email.html', {
#         'user': newuser,
#         'domain': current_site.domain,
#         'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
#         'token': account_activation_token.make_token(newuser),
#     })
#     to_email = newuser_form.cleaned_data.get('email')
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     email.send()
#     args_1['registration_success'] = \
#         '999999999 Please confirm your email address to complete the registration'
#     # return render(request, 'landing/registration_profile.html', locals())
#     print(999999999999999999999999)
#     # return redirect('registration_profile', email_1=email_1)
#     return args_1
#
#
# def registration(request):
#     args = {}
#     # form1 = UserCreationForm()
#     form = UserRegistrationForm()
#     if request.POST:
#         username_original = request.POST.get('username', '')
#         email_1 = request.POST.get('email', '')
#         password_11 = request.POST.get('password1', '')
#         request.POST = request.POST.copy()
#         request.POST['username'] = email_1
#         request.POST['password2'] = password_11
#         newuser_form = UserRegistrationForm(request.POST)
#
#         # Check email is the same or not
#         user_old = User.objects.filter(username=email_1).first()
#         if user_old:
#             if user_old.is_active:
#                 args['registration_error'] =\
#                     'THE SAME E-MAIL and Account is active Please, use option FORGET THE PASSWORD'
#                 return render(request, 'landing/registration.html', args)
#             else:
#                 now_again = '_AGAIN_'+'-'.join(('_'.join(str(datetime.datetime.now()).split(sep=' '))).split(sep=':'))
#                 user_old.username = str(user_old.username)+now_again
#                 user_old.email = str(user_old.email)+now_again
#                 user_old.save()
#                 validate_save_user_send_email(request, newuser_form, email_1, username_original)
#                 return redirect('registration_profile')
#         else:
#         # users = User.objects.filter(is_active=True)
#         # email_set = set()
#         # for i in users:
#         #     email_set.add(i.email)
#         # if email_1 in email_set:
#         #     args['registration_error'] = 'THE SAME E-MAIL and Account is active Please, use option FORGET THE PASSWORD'
#         #     return render(request, 'landing/registration.html', args)
#         # else:
#             if newuser_form.is_valid():
#                 validate_save_user_send_email(request, newuser_form, email_1, username_original)
#                 # newuser = newuser_form.save(commit=False)
#                 # newuser.is_active = False
#                 # newuser.save()
#                 # subscriber_current = Subscriber.objects.get(email=email_1)
#                 # subscriber_current.name = username_original
#                 # subscriber_current.save()
#                 # # Email sending code:
#                 # current_site = get_current_site(request)
#                 # mail_subject = 'Activate your blog account on Site RENEW for example.'
#                 # message = render_to_string('landing/acc_confirmation_email.html', {
#                 #     'user': newuser,
#                 #     'domain': current_site.domain,
#                 #     'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
#                 #     'token': account_activation_token.make_token(newuser),
#                 # })
#                 # to_email = newuser_form.cleaned_data.get('email')
#                 # email = EmailMessage(mail_subject, message, to=[to_email])
#                 # email.send()
#                 # args['registration_success'] = \
#                 #     '999999999 Please confirm your email address to complete the registration'
#                 # # return render(request, 'landing/registration_profile.html', locals())
#                 return redirect('registration_profile')
#             else:
#                 form = newuser_form
#                 print(form.error_messages)
#     return render(request, 'landing/registration.html', locals())
#
#
# def registration_profile(request):
#     aswer = "wefewrfergrtgrtgersd"
#     return render(request, 'landing/registration_profile.html', locals())
#
#
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         auth.login(request, user)
#         profile = Subscriber.objects.get(email=user.email)
#         profile.email_confirm = True
#         profile.save()
#         # return render(request, 'landing/profile.html', locals())
#         return redirect('profile')
#         # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')
#
#
# def profile(request):
#     form = SubscriberForm()
#     if request.POST:
#         # subscriber_id = request.POST.get('user_id', '')
#         user_profile = Subscriber.objects.filter(pk=request.POST.get('user_id', '')).first()
#         user_profile_form = SubscriberForm(request.POST, instance=user_profile)
#         # user_profile.index = request.POST.get('index', '')
#         # user_profile.save()
#         if user_profile_form.is_valid():
#             user_profile_form.save()
#             profile_success = "success"
#         else:
#             form = user_profile_form
#             print(99999999999999)
#     return render(request, 'landing/profile.html', locals())
#
#
# def login(request):
#     args = {}
#     # args.update(csrf(request))
#     if request.POST:
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse(home))
#         else:
#             login_error = "NO NO NO NO NO NO NO"
#             return render(request, 'landing/login.html')
#             # return render_to_response('login.html', args)
#     else:
#         return render(request, 'landing/login.html', locals())
#         # return render_to_response('login.html', args)
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse(home))
#     # return redirect("/")
#
#
# # def reset(request):
# #     args = {}
# #     if request.POST:
# #         email_1 = request.POST.get('email', '')
# #         users = User.objects.filter(is_active=True)
# #         email_set = set()
# #         for i in users:
# #             email_set.add(i.email)
# #         if email_1 in email_set:
# #             print('999999999')
# #         else:
# #             args['reset_error'] = 'NO SUCH E-MAIL'
# #             return render(request, 'landing/reset.html', args)
# #     form = PasswordResetForm()
# #     return render(request, 'landing/reset.html', locals())
#
#
# def home(request):
#     # username = auth.get_user(request).username
#     subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
#     address_cosmetologs = Cosmetolog.objects.filter(is_active=True)
#     cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
#     search_active_addresses = Address.objects.filter(is_active=True)
#     active_addresses = search_active_addresses.filter(
#         Q(type_id=5) |
#         Q(type_id=4)
#     ).order_by('type_id')
#     service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
#     service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)
#     service_products_images_all = ServiceProductImage.objects.filter(is_active=True, is_main=True,
#                                                                      service_product__is_active=True,
#                                                                      service_product__is_visible=True)
#     service_products_images = service_products_images_all[:4]
#     cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)
#     slider_mains = SliderMain.objects.filter(is_active=True, is_main=True)
#     slider_mains_counts = range(slider_mains.count() - 1)
#     advert_all = SliderMain.objects.filter(is_active=True, is_main=False)
#     advert_left = advert_all.get(position=1)
#     advert_right = advert_all.get(position=2)
#     advert_right_up = advert_all.get(position=3)
#     advert_right_down = advert_all.get(position=4)
#     blogs_images_all = BlogImage.objects.filter(is_active=True, is_main=True)
#     blogs_images = blogs_images_all[:4]
#     products_images_all = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
#     products_images = products_images_all[:4]
#     products_images_new = products_images_all.filter(product__category__id=1)
#     products_images_popular = products_images_all.filter(product__category__id=2)
#
#     return render(request, 'landing/home.html', locals())
#
#
# def salon(request):
#     if 'q' in request.GET:
#         q_full_address = request.GET.get('q')
#         q_service = request.GET.get('q1')
#         print('salon - q_full_address:', q_full_address)
#         print(type(q_full_address))
#         print('salon - q_service:', q_service)
#
#         if not q_full_address and not q_service:
#             error = True
#             return HttpResponseRedirect(reverse(home), {'error': error})
#         else:
#             url_address = str()
#             url_service = str()
#             if q_full_address:
#                 search_active_addresses = Address.objects.filter(is_active=True)
#                 search_active_addresses_url = search_active_addresses.get(display_address=q_full_address)
#                 url_address = search_active_addresses_url.url
#             if q_service:
#                 service_set = set()
#                 service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
#                 for i in service_categories:
#                     service_set.add(i.name)
#                 if q_service in service_set:
#                     url_service = slugify(q_service)
#                 else:
#                     subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
#                     subservice_categories_url = subservice_categories.get(subcategory_category=q_service)
#                     url_service = subservice_categories_url.url
#
#             url_full = url_service + url_address + "/"
#             print('url_address  ', url_address)
#             print('url_service  ', url_service)
#             print('url_full', url_full)
#             if q_full_address and not q_service:
#                 return HttpResponseRedirect('/cosmetolog-in' + url_full)
#             elif not q_full_address and q_service:
#                 return HttpResponseRedirect('/service-in-Poland/' + url_full)
#             else:
#                 return HttpResponseRedirect(url_full)
#     else:
#         return HttpResponseRedirect(reverse(home))
#
#
# def get_city_id(q_city):
#     q_address_url = '/' + q_city
#     search_active_addresses = Address.objects.filter(is_active=True)
#     search_city_active_addresses = search_active_addresses.get(url__exact=q_address_url)
#     city_id = search_city_active_addresses.id
#
#     cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
#     search_cosmetolog_addresses = cosmetolog_addresses.filter(address_id=city_id)
#     cosmetolog_set = set()
#     for j in search_cosmetolog_addresses:
#         cosmetolog_set.add(j.cosmetolog_id)
#
#     return city_id, cosmetolog_set
#
#
# def get_delnica_ulica_id(q_city, q_delnica_ulica):
#     q_address_url = '/' + q_city + '/' + q_delnica_ulica
#     search_active_addresses = Address.objects.filter(is_active=True)
#     search_city_active_addresses = search_active_addresses.get(url__exact=q_address_url)
#     delnica_ulica_id = search_city_active_addresses.id
#     delnica_ulica_type_id = search_city_active_addresses.type_id
#     delnica_ulica_parent_id = search_city_active_addresses.parent_id
#
#     return delnica_ulica_id, delnica_ulica_type_id, delnica_ulica_parent_id
#
#
# def q_search_in_url(q_city, q_delnica_ulica):
#     cosmetolog_set = set()
#     cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True,
#                                                             address_name__url__icontains=q_city and q_delnica_ulica)
#     for i in cosmetolog_addresses:
#         cosmetolog_set.add(i.cosmetolog_id)
#
#     if q_delnica_ulica != q_city:
#         delnica_ulica_id, delnica_ulica_type_id, delnica_ulica_parent_id = get_delnica_ulica_id(q_city, q_delnica_ulica)
#         if delnica_ulica_type_id == 10:
#             print('Это улица   ', delnica_ulica_type_id)
#             cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True,
#                                                                     cosmetolog_id__exact=delnica_ulica_parent_id)
#             for j in cosmetolog_addresses:
#                 cosmetolog_set.add(j.cosmetolog_id)
#         elif delnica_ulica_type_id == 5:
#             print('Это дельница   ', delnica_ulica_type_id)
#
#     return cosmetolog_set
#
#
# def search_service_address(request, q_1, q_2=None, q_3=None, q_4=None):
#
#     print('search - q1:', q_1)
#     print('search - q2', q_2)
#     print('search - q3', q_3)
#     print('search - q4', q_4)
#     logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
#
#     #проверка - является ли q2 субсервисом
#     subservice_set = set()
#     subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
#     for i in subservice_categories:
#         subservice_set.add(i.slug)
#     service_set = set()
#     if q_2 in subservice_set:
#         # надо выбрать всех косметологов у которых установлен этот СУБ_сервис q_2
#         print('YES YES YES YES')
#         service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
#                                                          subcategory__slug__icontains=q_2)
#         print(service_products)
#         for i in service_products:
#             service_set.add(i.cosmetolog_id)
#         print('только для суб сервиса', service_set)
#         query_service = q_1.capitalize() + ', ' + q_2.capitalize()
#         # соответсвенно q_3 является городом
#         # проверяем наличие q_4
#         if q_4:
#             # пишем код для q_3 и q_4
#             # выбираем всех косметологов у которых есть адресс q_3 и q_4 (на них фокус), или q_3
#             cosmetolog_address_set = q_search_in_url(q_3, q_4)
#             print('после вызова функции - только city and delnica/ulica q_3 q_4  ', cosmetolog_address_set)
#             city_id, cosmetolog_set = get_city_id(q_3)
#             cosmetolog_address_set.update(cosmetolog_set)
#             print('после вызова функции - только city and delnica/ulica q_3 q_4 +++++ ', cosmetolog_address_set)
#             query_address = q_3.capitalize() + ', ' + q_4.capitalize()
#
#         else:
#             # пишем код для q_3 (вызываем функцию с параметром q_3, в которой
#             # выбираем всех косметологов у которых есть адрес q3 включая вглубь
#             cosmetolog_address_set = q_search_in_url(q_3, q_3)
#             print('после вызова функции - только city q_3  ', cosmetolog_address_set)
#             query_address = q_3.capitalize()
#
#         # пересекаем множества сервиса и косметологов
#         search_cosmetologs_set = service_set & cosmetolog_address_set
#         print('final search_cosmetologs_set    ', search_cosmetologs_set)
#         cosmetolog_count = len(search_cosmetologs_set)
#     else:
#         # q_2 не является субсервисом
#         # надо выбрать всех косметолголов у которых установлен этот Сервис q_1
#         print('NO NO NO NO')
#         service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
#                                                          category__slug__icontains=q_1)
#         print(service_products)
#         for i in service_products:
#             service_set.add(i.cosmetolog_id)
#         print('только для суб сервиса', service_set)
#         query_service = q_1.capitalize()
#         # соответсвенно q_2 является городом
#         # проверяем наличие q_3
#         if q_3:
#             # пишем код для q_2 и q_3
#             # выбираем всех косметологов у которых есть адресс q_2 и q_3 (на них фокус), или q_2
#             cosmetolog_address_set = q_search_in_url(q_2, q_3)
#             print('после вызова функции - только city and delnica/ulica q_3 q_4  ', cosmetolog_address_set)
#             city_id, cosmetolog_set = get_city_id(q_2)
#             cosmetolog_address_set.update(cosmetolog_set)
#             print('после вызова функции - только city and delnica/ulica q_3 q_4 +++++ ', cosmetolog_address_set)
#             query_address = q_2.capitalize() + ', ' + q_3.capitalize()
#         else:
#             # пишем код для q_2 (вызываем функцию с параметром q_2, в которой
#             # выбираем всех косметологов у которых есть адрес q2 включая вглубь
#             cosmetolog_address_set = q_search_in_url(q_2, q_2)
#             print('после вызова функции - только city q_2  ', cosmetolog_address_set)
#             query_address = q_2.capitalize()
#         search_cosmetologs_set = service_set & cosmetolog_address_set
#         print('final search_cosmetologs_set    ', search_cosmetologs_set)
#         cosmetolog_count = len(search_cosmetologs_set)
#
#     # address_cosmetologs = Cosmetolog.objects.filter(is_active=True)
#     # cosmetolog_addresses = CosmetologAddress.objects.filter(is_active=True)
#     # search_active_addresses = Address.objects.filter(is_active=True)
#     # service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
#     # service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True)
#
#
#     cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True)
#
#     search_service_products_images = ServiceProductImage.objects.filter(
#         is_active=True, is_main=True, service_product__is_active=True,
#         service_product__is_visible=True, service_product__cosmetolog__id__in=search_cosmetologs_set)
#     # search_service_products_images = service_products_images_all.filter(
#     #     Q(service_product__in=d)
#     # )
#     # service_products_images = service_products_images_all[:4]
#     search_cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True, id__in=search_cosmetologs_set)
#
#     search_service_address_999 = 999
#
#     if cosmetolog_count != 0:
#         return render(request, 'landing/search_results.html', locals())
#     else:
#         return render(request, 'landing/no_search_results.html', locals())
#
#
# def search_service(request, q_1, q_2=None, q_3=None):
#     logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
#
#     search_active_addresses = Address.objects.filter(is_active=True)
#     active_addresses = search_active_addresses.filter(
#         Q(type_id=5) |
#         Q(type_id=4)
#     ).order_by('type_id')
#
#     active_addresses_towns = active_addresses.filter(type_id=4)
#     for i in active_addresses_towns:
#         i.slug = slugify(i.name)
#     subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
#     service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
#     # Ввели сервис но нету адресу - выводим список косметологов с таким сервисом по всей стране
#     # фокус на адресс - ВВЕДИТЕ поиск по адресу
#     service_set = set()
#     if q_2:
#         service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
#                                                          subcategory__slug__icontains=q_2)
#         print(service_products)
#         for i in service_products:
#             service_set.add(i.cosmetolog_id)
#         print('только для суб сервиса', service_set)
#         query_service_item = subservice_categories.get(slug=q_2)
#         query_service = query_service_item.subcategory_category
#
#         search_cosmetologs_set = service_set
#         print('final search_cosmetologs_set    ', search_cosmetologs_set)
#         cosmetolog_count = len(search_cosmetologs_set)
#     else:
#         service_products = ServiceProduct.objects.filter(is_active=True, is_visible=True,
#                                                          category__slug__icontains=q_1)
#         print(service_products)
#         for i in service_products:
#             service_set.add(i.cosmetolog_id)
#         print('только для суб сервиса', service_set)
#         query_service_item = service_categories.get(slug=q_1)
#         query_service = query_service_item.name
#
#         search_cosmetologs_set = service_set
#         print('final search_cosmetologs_set    ', search_cosmetologs_set)
#         cosmetolog_count = len(search_cosmetologs_set)
#
#     search_cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True, id__in=search_cosmetologs_set)
#     search_service_products_images = ServiceProductImage.objects.filter(
#         is_active=True, is_main=True, service_product__is_active=True,
#         service_product__is_visible=True, service_product__cosmetolog__id__in=search_cosmetologs_set)
#     search_service_999 = 999
#     if cosmetolog_count != 0:
#         return render(request, 'landing/search_results.html', locals())
#     else:
#         return render(request, 'landing/no_search_results.html', locals())
#
#
# def search_address(request, q_1, q_2=None, q_3=None):
#     # Ввели аддрес но нету сервиса - выводим список косметологов по этому адресу с любым сервисом
#     # фокус на сервис - ВЫБЕРИТЕ СЕРВИС
#     logo_images = LogoImage.objects.filter(is_active=True, is_main=True)
#
#     search_active_addresses = Address.objects.filter(is_active=True)
#     active_addresses = search_active_addresses.filter(
#         Q(type_id=5) |
#         Q(type_id=4)
#     ).order_by('type_id')
#
#     # active_addresses_towns = active_addresses.filter(type_id=4)
#     # for i in active_addresses_towns:
#     #     i.slug = slugify(i.name)
#     subservice_categories = SubCategoryForCosmetolog.objects.filter(is_active=True)
#     service_categories = CategoryForCosmetolog.objects.filter(is_active=True)
#     if q_2:
#         # пишем код для q_1 и q_2
#         # выбираем всех косметологов у которых есть адресс q_2 и q_3 (на них фокус), или q_2
#         cosmetolog_address_set = q_search_in_url(q_1, q_2)
#         print('после вызова функции - только city and delnica/ulica q_1 q_2  ', cosmetolog_address_set)
#         city_id, cosmetolog_set = get_city_id(q_1)
#         cosmetolog_address_set.update(cosmetolog_set)
#         print('после вызова функции - только city and delnica/ulica q_1 q_2 +++++ ', cosmetolog_address_set)
#         query_address_id, w2, w3 = get_delnica_ulica_id(q_1, q_2)
#         query_address = Address.objects.get(id=query_address_id).display_address
#     else:
#         # пишем код для q_1 (вызываем функцию с параметром q_1, в которой
#         # выбираем всех косметологов у которых есть адрес q1 включая вглубь
#         cosmetolog_address_set = q_search_in_url(q_1, q_1)
#         print('после вызова функции - только city q_1  ', cosmetolog_address_set)
#         query_address_id, w2_set = get_city_id(q_1)
#         query_address = Address.objects.get(id=query_address_id).display_address
#     search_cosmetologs_set = cosmetolog_address_set
#     print('final search_cosmetologs_set    ', search_cosmetologs_set)
#     cosmetolog_count = len(search_cosmetologs_set)
#
#     search_cosmetologs = Cosmetolog.objects.filter(is_active=True, is_visible=True, id__in=search_cosmetologs_set)
#     search_service_products_images = ServiceProductImage.objects.filter(
#         is_active=True, is_main=True, service_product__is_active=True,
#         service_product__is_visible=True, service_product__cosmetolog__id__in=search_cosmetologs_set)
#     search_address_999 = 999
#
#     if cosmetolog_count != 0:
#         return render(request, 'landing/search_results.html', locals())
#     else:
#         return render(request, 'landing/no_search_results.html', locals())
#
#
# def navbar_01(request):
#
#     return render(request, 'landing/navbar_01.html', locals())
#
#
# def contact(request):
#     session_key = request.session.session_key
#     args = {}
#     form = LetterForm()
#     print(request.POST)
#
#     if request.POST:
#         new_letter_form = LetterForm(request.POST)
#         if new_letter_form.is_valid():
#             username = auth.get_user(request).username
#             if username:
#                 user_current = Subscriber.objects.filter(email=username).first()
#                 new_letter = new_letter_form.save(commit=False)
#                 new_letter.user_name = user_current.name
#                 new_letter.user_email = user_current.email
#                 data = new_letter_form.cleaned_data
#                 new_letter.save()
#             else:
#                 data = new_letter_form.cleaned_data
#                 new_letter = new_letter_form.save()
#
#             subject = 'message from site renew-polska.pl/contact' + request.POST.get('subject', '')
#             message = request.POST.get('message', '')
#             from_email = settings.EMAIL_HOST_USER
#             to_list = ['biuro@renew-polska.pl', settings.EMAIL_HOST_USER]
#             send_mail(subject, message, from_email, to_list, fail_silently=True)
#
#             letter_success = "success"
# #           return redirect('registration_profile')
#             print(letter_success, letter_success)
#         else:
#             form = new_letter_form
#             # print(form.error_messages)
#
#     return render(request, 'landing/contact.html', locals())
#
#
# def about(request):
#     session_key = request.session.session_key
#     args = {}
#     about_text_object = Page.objects.get(is_active=True, page_name="About")
#     print(about_text_object)
#     # about_text = about_text_object.page_text
#
#     return render(request, 'landing/about.html', locals())
#
#
# def training(request):
#     session_key = request.session.session_key
#     args = {}
#     trainings_all = Training.objects.filter(is_active=True)
#
#     return render(request, 'landing/warsztaty.html', locals())
#
#
# def validate_training_send_email(request, trainee_name, trainee_email, email_message):
#     # Email sending code:
#     new_trainee = TrainingUser.objects.filter(trainee_email=trainee_email).first()
#     current_site = get_current_site(request)
#     mail_subject = 'Confirm Your Registration for' + trainee_name + 'at Renew-Polska.pl'
#     message = render_to_string(email_message, {
#         'user': trainee_name,
#         'domain': current_site.domain,
#         'uid': urlsafe_base64_encode(force_bytes(new_trainee.pk)),
#         'token': account_activation_token.make_token(new_trainee),
#     })
#     to_email = trainee_email
#     email = EmailMessage(mail_subject, message, to=[to_email])
#     email.send()
#     print(999999999999999999999999)
#     return 999


def card_decks():
    cards = {
        "2_1": 2, "2_2": 2, "2_3": 2, "2_4": 2,
        "3_1": 3, "3_2": 3, "3_3": 2, "3_4": 3,
        "4_1": 4, "4_2": 4, "4_3": 4, "4_4": 4,
        "5_1": 5, "5_2": 5, "5_3": 5, "5_4": 5,
        "6_1": 6, "6_2": 6, "6_3": 6, "6_4": 6,
        "7_1": 7, "7_2": 7, "7_3": 7, "7_4": 7,
        "8_1": 8, "8_2": 8, "8_3": 8, "8_4": 8,
        "9_1": 9, "9_2": 9, "9_3": 9, "9_4": 9,
        "10_1": 10, "10_2": 10, "10_3": 10, "10_4": 10,
        "B_1": 10, "B_2": 10, "B_3": 10, "B_4": 10,
        "D_1": 10, "D_2": 10, "D_3": 10, "D_4": 10,
        "K_1": 10, "K_2": 10, "K_3": 10, "K_4": 10,
        "A_1": 11, "A_2": 11, "A_3": 11, "A_4": 11
    }
    deck = 7
    cards_full = {}
    for key, value in cards.items():
        for i in range(1, deck+1):
            new_key = str(i)+'_'+key
            cards_full[new_key] = value
    #         print(cards_full)
    # len(cards_full)
    return cards_full

# Initial deal
def first_deal(cards):
    p1_list = []
    dealer_list = []
    for i in range(2):
        p1 = random.choice(list(cards.keys()))
        p1_list.append(cards[p1])
        del cards[p1]
        dealer = random.choice(list(cards.keys()))
        dealer_list.append(cards[dealer])
        del cards[dealer]
    return cards, p1_list, dealer_list


def trick_item(request, slug=None):
    trick = AnotherTrick.objects.get(slug=slug, is_active=True)
    url_name = slug.replace('-', '_')
    if slug == "file-upload-regular-user":
        form = ProductFileCSVForm()
        print('9999', form)
        if request.method == 'POST':
            form = ProductFileCSVForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('another')
        else:
            form = ProductFileCSVForm()
    if slug == "crm":
        print()
        products_all = Product.objects.filter(is_active=True)
    if slug == "black-jack":
        black_jack = 21
        if request.method == 'POST':
            if request.POST.get('start', '') == "start":
            # form = ProductFileCSVForm(request.POST, request.FILES)
                ccc = card_decks().copy()
                a, b, c = first_deal(ccc)
                print(a)
                print(b)
                print(c)
        # products_all = Product.objects.filter(is_active=True)
    # return render(request, 'another/file_upload_regular_user.html', {'form': form})
    return render(request, 'another/' + url_name + '.html', locals())


def crm_product_item(request, slug=None):
    products_all = Product.objects.filter(is_active=True)
    # trick = AnotherTrick.objects.get(slug=slug, is_active=True)
    # url_name = slug2.replace('-', '_')
    if slug:
        product = Product.objects.get(slug=slug)
    #     form = ProductFileCSVForm()
    #     print('9999', form)
        if request.method == 'POST':
    #         form = ProductFileCSVForm(request.POST, request.FILES)
            print(9999999)
        if request.method == 'GET':
            print(3333333)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('another')
    #     else:
    #         form = ProductFileCSVForm()
        return render(request, 'another/crm_product_item.html', locals())
    return render(request, 'another/crm_product.html', locals())


# def activate_training(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = TrainingUser.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, TrainingUser.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('training')
#     else:
#         return HttpResponse('Activation link is invalid!')
