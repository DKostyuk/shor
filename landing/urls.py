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
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration_profile/$', views.registration_profile, name='registration_profile'),
    url(r'^registration_profile/(?P<email_1>[.@0-9A-Za-z_\-]+)/$', views.registration_profile, name='registration_profile'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<cosmetolog_url>[\w-]+)/$', views.profile_cosmetolog, name='profile_cosmetolog'),
    url(r'^profile_service_edit/(?P<cosmetolog_url>[\w-]+)/(?P<service_slug>[\w-]+)/$', views.profile_cosmetolog_edit_service, name='profile_cosmetolog_edit_service'),
    # url(r'^service/(?P<slug1>[\w-]+)/(?P<slug>[\w-]+)/$', views.service, name='service'),
    # url(r'^profile/(?P<cosmetolog_url>[\w-]+)/(?P<q_2>[\w-]+)/$', views.profile, name='profile'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^reset/$', views.reset, name='reset'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^password_reset/$', PasswordResetView.as_view(template_name='landing/password_reset.html',
                                                        email_template_name='landing/password_reset_email.html',
                                                        from_email='kostiukkosta@gmail.com'), name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        PasswordResetConfirmView.as_view(template_name='landing/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^password_reset_complete/$',
        PasswordResetCompleteView.as_view(template_name='landing/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^password_reset_done/$',
        PasswordResetDoneView.as_view(template_name='landing/password_reset_done.html'),
        name='password_reset_done'),

    url(r'^search_ajax/$', views.search_ajax),
    url(r'^search_ajax_service/$', views.search_ajax_service),
    url(r'^search_ajax_city/$', views.search_ajax_city),
    url(r'^search_ajax_street/$', views.search_ajax_street),

    url(r'^uslugi-kosmetologicheskie/$', views.salon, name='salon'),

    url(r'^uslugi-kosmetologicheskie/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/(?P<q_4>[\w-]+)/(?P<q_5>[\w-]+)/(?P<q_6>[\w-]+)/$',
        views.search_service_address, name='search_service_address'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^warsztaty/$', views.training, name='training'),
    url(r'^warsztaty/(?P<slug>[\w-]+)/$', views.training_item, name='training_item'),

    url(r'^activate_training/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_training, name='activate_training'),

    url(r'^test_ajax/$', views.test_ajax, name='test_ajax'),
]
