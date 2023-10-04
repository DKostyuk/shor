from django.contrib import admin
from .models import *


class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PurchaseItem._meta.fields]

    class Meta:
        model = PurchaseItem


admin.site.register(PurchaseItem, PurchaseItemAdmin)


class StockTotalAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in StockTotal._meta.fields]
    list_display = ['product_item', 'category', 'num_total', 'price_total_usd', 'price_total_uah',
                    'created', 'updated', 'modified_by',]
    readonly_fields = ['product_item', 'num_total', 'price_total_usd', 'price_total_uah',
                       'created', 'updated', 'modified_by', ]

    class Meta:
        model = StockItemPlus


admin.site.register(StockTotal, StockTotalAdmin)


class StockItemPurchaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockItemPurchase._meta.fields]

    class Meta:
        model = StockItemPurchase


admin.site.register(StockItemPurchase, StockItemPurchaseAdmin)


class StockItemPlusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockItemPlus._meta.fields]
    # list_display = ['id_purchase', 'product_item', 'due_date', 'num_plus', 'price_plus_usd', 'comments', 'is_active',]
    fields = ['id_purchase', 'product_item', 'due_date', 'num_plus', 'price_plus_usd', 'comments', 'is_active', ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['id_purchase', 'product_item', 'due_date', 'num_plus', 'price_plus_usd', 'comments', 'is_active']
        else:
            return []

    class Meta:
        model = StockItemPlus


admin.site.register(StockItemPlus, StockItemPlusAdmin)


class StockFilePlusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockFilePlus._meta.fields]

    class Meta:
        model = StockFilePlus


admin.site.register(StockFilePlus, StockFilePlusAdmin)


class StockItemMinusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockItemMinus._meta.fields]
    # fields = ['product_item', 'due_date', 'num_minus', 'comments', 'is_active']

    class Meta:
        model = StockItemMinus


admin.site.register(StockItemMinus, StockItemMinusAdmin)


class StockItemReservedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockItemReserved._meta.fields]
    # fields = ['product_item', 'due_date', 'num_minus', 'comments', 'is_active']

    class Meta:
        model = StockItemReserved


admin.site.register(StockItemReserved, StockItemReservedAdmin)


class StockItemRestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockItemRest._meta.fields]
    # fields = ['product_item', 'due_date', 'num_minus', 'comments', 'is_active']

    class Meta:
        model = StockItemRest


admin.site.register(StockItemRest, StockItemRestAdmin)


# class BlogAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Blog._meta.fields]
#     prepopulated_fields = {'slug': ('title_name',)}
#     inlines = [BlogImageInline]
#
#     class Meta:
#         model = Blog
#
# admin.site.register(Blog, BlogAdmin)
#
#
# class BlogImageAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in BlogImage._meta.fields]
#
#     class Meta:
#         model = BlogImage
#
# admin.site.register(BlogImage, BlogImageAdmin)
