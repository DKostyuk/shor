from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductType._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = ProductType


admin.site.register(ProductType, ProductTypeAdmin)


class ProductVolumeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductVolume._meta.fields]

    class Meta:
        model = ProductVolume


admin.site.register(ProductVolume, ProductVolumeAdmin)


class ProductVolumeTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductVolumeType._meta.fields]

    class Meta:
        model = ProductVolumeType


admin.site.register(ProductVolumeType, ProductVolumeTypeAdmin)


class ProductAdmin (admin.ModelAdmin):
    list_display = ['producer', 'category','name', 'name_pl', 'slug', 'name_description','description',
                    'name_description_1', 'descript_1', 'name_description_2', 'descript_2',
                    'name_description_3', 'descript_3', 'name_description_4', 'description_4', 'name_description_5',
                    'description_5', 'short_description', 'is_active', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

    def descript_1(self, obj):
        return obj.description_1[:20]

    def descript_2(self, obj):
        return obj.description_2[:20]

    def descript_3(self, obj):
        return obj.description_3[:20]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


# class ProductImageAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductImage._meta.fields]
#
#     class Meta:
#         model = ProductImage
#
#
# admin.site.register(ProductImage, ProductImageAdmin)


class ProductAddFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductAddFile._meta.fields]

    class Meta:
        model = ProductAddFile


admin.site.register(ProductAddFile, ProductAddFileAdmin)


class ProductJoinAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductJoin._meta.fields]

    class Meta:
        model = ProductJoin


admin.site.register(ProductJoin, ProductJoinAdmin)


class ProductItemAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductItem._meta.fields]

    class Meta:
        model = ProductItem


admin.site.register(ProductItem, ProductItemAdmin)


# class ProductItemSalesAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductItemSales._meta.fields]
#     readonly_fields = ('price_old', 'price_current', 'price_current_usd', 'exchange_rate', 'created',
#                        'updated', 'modified_by',)
#
#     class Meta:
#         model = ProductItemSales
#
#
# admin.site.register(ProductItemSales, ProductItemSalesAdmin)


class CurrencyExchangeAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in CurrencyExchange._meta.fields]
    readonly_fields = ('usd_price_uah', 'created', 'updated', 'modified_by',
                       'usd_rate_before', 'date_before', 'usd_diff',)
    fields = (
        ('usd_price_uah', 'usd_rate_initial', 'usd_rate_correct'),
        ('usd_rate_before', 'date_before', 'usd_diff'),
        ('modified_by', 'updated'),
        'created'
    )

    class Meta:
        model = CurrencyExchange


admin.site.register(CurrencyExchange, CurrencyExchangeAdmin)


class SalesProductTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SalesProductType._meta.fields]

    class Meta:
        model = SalesProductType


admin.site.register(SalesProductType, SalesProductTypeAdmin)


class SaleProductItemInline(admin.TabularInline):
    model = SaleProductItem
    extra = 0


class SalesProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SalesProduct._meta.fields]
    readonly_fields = ('price_old', 'price_current', 'price_current_usd', 'exchange_rate', 'slug', 'created',
                       'updated', 'modified_by',)
    inlines = [SaleProductItemInline]
    list_editable = ['rank']

    class Meta:
        model = SalesProduct


admin.site.register(SalesProduct, SalesProductAdmin)


class SaleProductItemAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SaleProductItem._meta.fields]

    class Meta:
        model = SaleProductItem


admin.site.register(SaleProductItem, SaleProductItemAdmin)


class IngredientProductInline(admin.TabularInline):
    model = IngredientProduct
    extra = 0


class IngredientAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Ingredient._meta.fields]
    inlines = [IngredientProductInline]

    class Meta:
        model = Ingredient


admin.site.register(Ingredient, IngredientAdmin)


class IngredientTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in IngredientType._meta.fields]

    class Meta:
        model = IngredientType


admin.site.register(IngredientType, IngredientTypeAdmin)


class IngredientProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in IngredientProduct._meta.fields]

    class Meta:
        model = IngredientProduct


admin.site.register(IngredientProduct, IngredientProductAdmin)
