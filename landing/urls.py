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
from django.urls import include, re_path, path
from django.contrib import admin
from landing import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [

    re_path(r'^$', views.home, name='home'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^landing/$', views.landing, name='landing'),
    re_path(r'^registration/$', views.registration, name='registration'),
    re_path(r'^registration_profile/$', views.registration_profile, name='registration_profile'),
    re_path(r'^registration_profile/(?P<email_1>[.@0-9A-Za-z_\-]+)/$', views.registration_profile, name='registration_profile'),

    re_path(r'^activation_link_request/$', views.activation_link_request, name='activation_link_request'),
    re_path(r'^cabinet/$', views.cabinet, name='cabinet'),

    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/(?P<cosmetolog_url>[\w-]+)/$', views.profile_cosmetolog, name='profile_cosmetolog'),
    re_path(r'^profile_service_edit/(?P<cosmetolog_url>[\w-]+)/(?P<service_slug>[\w-]+)/$', views.profile_cosmetolog_edit_service, name='profile_cosmetolog_edit_service'),
    # url(r'^service/(?P<slug1>[\w-]+)/(?P<slug>[\w-]+)/$', views.service, name='service'),
    # url(r'^profile/(?P<cosmetolog_url>[\w-]+)/(?P<q_2>[\w-]+)/$', views.profile, name='profile'),

    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    # url(r'^reset/$', views.reset, name='reset'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),

    re_path(r'^password_reset/$', PasswordResetView.as_view(template_name='landing/password_reset.html',
                                                        email_template_name='landing/password_reset_email.html',
                                                        from_email='dmyto.kostyuk@gmail.com'), name='password_reset'),
    re_path(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        PasswordResetConfirmView.as_view(template_name='landing/password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^password_reset_complete/$',
        PasswordResetCompleteView.as_view(template_name='landing/password_reset_complete.html'),
        name='password_reset_complete'),
    re_path(r'^password_reset_done/$',
        PasswordResetDoneView.as_view(template_name='landing/password_reset_done.html'),
        name='password_reset_done'),

    re_path(r'^search_ajax/$', views.search_ajax),
    re_path(r'^search_ajax_service/$', views.search_ajax_service),
    re_path(r'^search_ajax_city/$', views.search_ajax_city),
    re_path(r'^search_ajax_street/$', views.search_ajax_street),

    re_path(r'^uslugi-kosmetologicheskie/$', views.salon, name='salon'),

    re_path(r'^uslugi-kosmetologicheskie/(?P<q_1>[\w-]+)/(?P<q_2>[\w-]+)/(?P<q_3>[\w-]+)/(?P<q_4>[\w-]+)/(?P<q_5>[\w-]+)/(?P<q_6>[\w-]+)/$',
        views.search_service_address, name='search_service_address'),

    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^warsztaty/$', views.training, name='training'),
    re_path(r'^warsztaty/(?P<slug>[\w-]+)/$', views.training_item, name='training_item'),

    re_path(r'^activate_training/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_training, name='activate_training'),

    re_path(r'^test_ajax/$', views.test_ajax, name='test_ajax'),
]
