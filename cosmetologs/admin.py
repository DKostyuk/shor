from django.contrib import admin
from .models import *


class CosmetologCategoryInline(admin.TabularInline):
    model = CosmetologCategory
    extra = 0


class CosmetologAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cosmetolog._meta.fields]
    prepopulated_fields = {'code': ('name',)}
    inlines = [CosmetologCategoryInline]

    class Meta:
        model = Cosmetolog

admin.site.register(Cosmetolog, CosmetologAdmin)


class CategoryForCosmetologAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryForCosmetolog._meta.fields]
    prepopulated_fields = {'code': ('name',)}

    class Meta:
        model = CategoryForCosmetolog

admin.site.register(CategoryForCosmetolog, CategoryForCosmetologAdmin)


class ServiceProductImageInline(admin.TabularInline):
    model = ServiceProductImage
    extra = 0


class ServiceProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceProductImage._meta.fields]

    class Meta:
        model = ServiceProductImage

admin.site.register(ServiceProductImage, ServiceProductImageAdmin)


class ServiceProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceProduct._meta.fields]
    prepopulated_fields = {'code': ('name',)}
    inlines = [ServiceProductImageInline]

    class Meta:
        model = ServiceProduct

admin.site.register(ServiceProduct, ServiceProductAdmin)



