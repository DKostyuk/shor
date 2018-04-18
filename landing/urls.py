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
from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.contrib.auth.views import password_reset, password_reset_confirm,\
    password_reset_done, password_reset_complete

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration_profile/$', views.registration_profile, name='registration_profile'),
    url(r'^registration_profile/(?P<email_1>[.@0-9A-Za-z_\-]+)/$', views.registration_profile, name='registration_profile'),
    url(r'^profile/$', views.profile, name='profile'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^reset/$', views.reset, name='reset'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^password_reset/$', password_reset,
        {'template_name': 'landing/password_reset.html', 'email_template_name': 'landing/password_reset_email.html',
         'from_email': 'reset_password@ukr.net'},
        name='password-reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
        {'template_name': 'landing/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password_reset_complete/$', password_reset_complete,
        {'template_name': 'landing/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^password_reset_done/$', password_reset_done,
        {'template_name': 'landing/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^uslugi-kosmetyczne/$', views.salon, name='salon'),

    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/$',
        views.search_service_address, name='search_service_address'),
    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/$',
        views.search_service_address, name='search_service_address'),
    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/$',
        views.search_service_address, name='search_service_address'),
    url(r'^uslugi-kosmetyczne/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/(?P<q_4>[\w-]+)/$',
        views.search_service_address, name='search_service_address'),

    url(r'^service-in-Poland/(?P<q_1>[\w-]+)/$', views.search_service, name='search_service'),
    url(r'^service-in-Poland/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/$', views.search_service, name='search_service'),
    url(r'^service-in-Poland/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/$', views.search_service,
        name='search_service'),

    url(r'^cosmetolog-in/(?P<q_1>[\w-]+)/$', views.search_address, name='search_address'),
    url(r'^cosmetolog-in/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/$', views.search_address, name='search_address'),
    url(r'^cosmetolog-in/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/$',views.search_address,
        name='search_address'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^warsztaty/$', views.training, name='training'),
    url(r'^warsztaty/(?P<slug>[\w-]+)/$', views.training_item, name='training_item'),


    url(r'^navbar_01/$', views.navbar_01, name=' navbar_01'),
]
