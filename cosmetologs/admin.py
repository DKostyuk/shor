from django.contrib import admin
from .models import *


class CosmetologCategoryInline(admin.TabularInline):
    model = CosmetologCategory
    extra = 0


class CosmetologAddressInline(admin.TabularInline):
    model = CosmetologAddress
    extra = 0


class CosmetologAddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CosmetologAddress._meta.fields]

    class Meta:
        model = CosmetologAddress


admin.site.register(CosmetologAddress, CosmetologAddressAdmin)


class CosmetologEmailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CosmetologEmail._meta.fields]

    class Meta:
        model = CosmetologEmail


admin.site.register(CosmetologEmail, CosmetologEmailAdmin)


class CosmetologPhoneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CosmetologPhone._meta.fields]

    class Meta:
        model = CosmetologPhone


admin.site.register(CosmetologPhone, CosmetologPhoneAdmin)


class CosmetologAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cosmetolog._meta.fields]
    inlines = [CosmetologCategoryInline]

    class Meta:
        model = Cosmetolog


admin.site.register(Cosmetolog, CosmetologAdmin)


class CosmetologTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CosmetologType._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = CosmetologType


admin.site.register(CosmetologType, CosmetologTypeAdmin)


class CategoryForCosmetologAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryForCosmetolog._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = CategoryForCosmetolog


admin.site.register(CategoryForCosmetolog, CategoryForCosmetologAdmin)


class SubCategoryForCosmetologAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SubCategoryForCosmetolog._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = SubCategoryForCosmetolog


admin.site.register(SubCategoryForCosmetolog, SubCategoryForCosmetologAdmin)


class ServiceProductImageInline(admin.TabularInline):
    model = ServiceProductImage
    extra = 0


class ServiceProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceProduct._meta.fields]
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceProductImageInline]

    class Meta:
        model = ServiceProduct


admin.site.register(ServiceProduct, ServiceProductAdmin)


# class SubscriberCosmetologAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in SubscriberCosmetolog._meta.fields]
#
#     class Meta:
#         model = SubscriberCosmetolog
#
# admin.site.register(SubscriberCosmetolog, SubscriberCosmetologAdmin)


class CosmetologAddFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CosmetologAddFile._meta.fields]

    class Meta:
        model = CosmetologAddFile


admin.site.register(CosmetologAddFile, CosmetologAddFileAdmin)


class ServiceAddFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceAddFile._meta.fields]

    class Meta:
        model = ServiceAddFile


admin.site.register(ServiceAddFile, ServiceAddFileAdmin)
