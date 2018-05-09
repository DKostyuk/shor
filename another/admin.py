from django.contrib import admin
from .models import *


class AnotherTrickAdmin (admin.ModelAdmin):
    list_display = [field.name for field in AnotherTrick._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = AnotherTrick


admin.site.register(AnotherTrick, AnotherTrickAdmin)


class ProductFileCSVAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductFileCSV._meta.fields]

    class Meta:
        model = ProductFileCSV


admin.site.register(ProductFileCSV, ProductFileCSVAdmin)
