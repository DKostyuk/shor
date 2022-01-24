"""test_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from another import views
from django.views.generic import TemplateView



urlpatterns = [

    re_path(r'^another/$', views.another, name='another'),
    re_path(r'^another/(?P<slug>[\w-]+)/$', views.trick_item, name='trick_item'),
    re_path(r'^another/crm/product/$', views.crm_product_item, name='crm_product_item'),
    re_path(r'^another/crm/product/(?P<slug>[\w-]+)/$', views.crm_product_item, name='crm_product_item'),
    re_path(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    # url(r'^registration/$', views.registration, name='registration'),
    # url(r'^registration_profile/$', views.registration_profile, name='registration_profile'),
    # url(r'^registration_profile/(?P<email_1>[.@0-9A-Za-z_\-]+)/$', views.registration_profile, name='registration_profile'),
    # url(r'^profile/$', views.profile, name='profile'),
    #
    # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    # # url(r'^reset/$', views.reset, name='reset'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    #
    # url(r'^password_reset/$', password_reset,
    #     {'template_name': 'landing/password_reset.html', 'email_template_name': 'landing/password_reset_email.html',
    #      'from_email': 'reset_password@ukr.net'},
    #     name='password-reset'),
    # url(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
    #     {'template_name': 'landing/password_reset_confirm.html'},
    #     name='password_reset_confirm'),
    # url(r'^password_reset_complete/$', password_reset_complete,
    #     {'template_name': 'landing/password_reset_complete.html'},
    #     name='password_reset_complete'),
    # url(r'^password_reset_done/$', password_reset_done,
    #     {'template_name': 'landing/password_reset_done.html'},
    #     name='password_reset_done'),
    #

    #
    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^training/$', views.training, name='training'),
    # url(r'^training/(?P<slug>[\w-]+)/$', views.training_item, name='training_item'),
    #
    # url(r'^activate_training/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate_training, name='activate_training'),

]
