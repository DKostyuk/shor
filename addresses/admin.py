from django.contrib import admin
from .models import *


# class AddressTypeInline(admin.TabularInline):
#     model = AddressType
#     extra = 0
#

class AddressTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AddressType._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = AddressType

admin.site.register(AddressType, AddressTypeAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Address

admin.site.register(Address, AddressAdmin)


# class ServiceProductImageInline(admin.TabularInline):
#     model = ServiceProductImage
#     extra = 0
#
#
# class ServiceProductAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ServiceProduct._meta.fields]
#     prepopulated_fields = {'slug': ('name',)}
#     inlines = [ServiceProductImageInline]
#
#     class Meta:
#         model = ServiceProduct
#
# admin.site.register(ServiceProduct, ServiceProductAdmin)
#