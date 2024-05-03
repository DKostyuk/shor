from django.contrib import admin
from .models import *

# Register your models here.


class BonusEventStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusEventStatus._meta.fields]

    class Meta:
        model = BonusEventStatus


admin.site.register(BonusEventStatus, BonusEventStatusAdmin)


class BonusAccountTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusAccountType._meta.fields]

    class Meta:
        model = BonusAccountType


admin.site.register(BonusAccountType, BonusAccountTypeAdmin)


class BalanceSumStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BalanceSumStatus._meta.fields]

    class Meta:
        model = BalanceSumStatus


admin.site.register(BalanceSumStatus, BalanceSumStatusAdmin)


class BonusEventTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusEventType._meta.fields]

    class Meta:
        model = BonusEventType


admin.site.register(BonusEventType, BonusEventTypeAdmin)


class BonusAccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusAccount._meta.fields]

    class Meta:
        model = BonusAccount


admin.site.register(BonusAccount, BonusAccountAdmin)


class BonusAccountCosmetologAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusAccountCosmetolog._meta.fields]

    class Meta:
        model = BonusAccountCosmetolog


admin.site.register(BonusAccountCosmetolog, BonusAccountCosmetologAdmin)


class BonusAccountEventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusAccountEvent._meta.fields]

    class Meta:
        model = BonusAccountEvent


admin.site.register(BonusAccountEvent, BonusAccountEventAdmin)


class BonusCosmetologMonthlySumAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BonusCosmetologMonthlySum._meta.fields]

    class Meta:
        model = BonusCosmetologMonthlySum


admin.site.register(BonusCosmetologMonthlySum, BonusCosmetologMonthlySumAdmin)
