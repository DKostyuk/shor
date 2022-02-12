from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderPaymentInline(admin.TabularInline):
    model = OrderPayment
    extra = 0
    readonly_fields = ['order_total_price', 'modified_by']


class StatusPaymentAdmin (admin.ModelAdmin):
    list_display = [field.name for field in StatusPayment._meta.fields]

    class Meta:
        model = StatusPayment


admin.site.register(StatusPayment, StatusPaymentAdmin)


class StatusOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in StatusOrder._meta.fields]

    class Meta:
        model = StatusOrder


admin.site.register(StatusOrder, StatusOrderAdmin)


class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline, OrderPaymentInline]
    search_fields = ['cosmetolog__cosmetolog_name', 'cosmetolog__tel_number']
    # inlines = [OrderPaymentInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket, ProductInBasketAdmin)


# class ServiceOrderAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ServiceOrder._meta.fields]
#     # inlines = [ProductInOrderInline]
#
#     class Meta:
#         model = ServiceOrder
#
#
# admin.site.register(ServiceOrder, ServiceOrderAdmin)


class OrderPaymentAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OrderPayment._meta.fields]
    search_fields = ['order__order_number']
    readonly_fields = ['order_total_price', 'modified_by']
    raw_id_fields = ['order']

    class Meta:
        model = OrderPayment


admin.site.register(OrderPayment, OrderPaymentAdmin)
