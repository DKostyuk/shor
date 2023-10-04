from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('product_category', views.product_category),
  path('login', views.login),
]