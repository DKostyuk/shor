from django.contrib import admin
from .models import *
from utils.emails import SendingEmail


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0
    fields = ['pb_sale', 'due_date', 'nmb', 'price_per_item', 'total_price', 'is_active']
    readonly_fields = ['total_price']


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
    fields = (
        ('status', 'total_price', 'order_number'),
        ('cosmetolog', 'receiver_name', 'receiver_surname', 'receiver_father_name'),
        ('receiver_email', 'receiver_phone', 'receiver_delivery_address'),
        ('comments', 'cosmetolog_bonus'),
    )
    inlines = [ProductInOrderInline, OrderPaymentInline]
    search_fields = ['cosmetolog__cosmetolog_name', 'cosmetolog__tel_number']
    readonly_fields = ('order_number', 'total_price')

    def save_model(self, request, obj, form, change):
        update_fields = None
        cosmo_populate = False
        email_send = False
        if change:
            print('Order has been changed by Admin')
            update_fields = form.changed_data
            print('update_fields - just after assigning  ', update_fields)
            if 'cosmetolog' in form.changed_data:
                cosmo_populate = True
            if 'status' in form.changed_data and obj.status.status_number == 33:
                email_send = True
        # Check if the order is being created (not modified)
        if not change:
            if obj.cosmetolog:
                cosmo_populate = True
        if email_send:
            try:
                email = SendingEmail()
                email.sending_email(type_id=4, email_details=obj)
                message = 'Новий Shor заказ з ADMIN - ' + str(obj.order_number)
                msg = SendingMessage()
                msg.sending_msg(message=message)
            except:
                pass
        if cosmo_populate:
            obj.receiver_email = obj.cosmetolog.email
            obj.receiver_name = obj.cosmetolog.cosmetolog_name
            obj.receiver_surname = obj.cosmetolog.cosmetolog_surname
            obj.receiver_father_name = obj.cosmetolog.cosmetolog_father_name
            obj.receiver_phone = obj.cosmetolog.tel_number

        # super().save_model(request, obj, form, change)

        obj.save(update_fields=update_fields)
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            print('9999999999999999', instance)
            if hasattr(instance, 'price_per_item'):
                # Auto-populate the price for ProductInOrder items here
                if instance.price_per_item or instance.price_per_item == 0:
                    # Calculate the price based on your logic
                    instance.price_per_item = instance.pb_sale.price_current
                instance.save()
        formset.save_m2m()

        # Recalculate and update the total_price for the Order
        order = form.instance
        order_total_price = sum([item.total_price for item in order.productinorder_set.all()])
        order.total_price = order_total_price
        order.save()

        super().save_formset(request, form, formset, change)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',  # jquery
            'js/scripts.js',  # project static folder
            # 'app/js/scripts.js',  # app static folder
        )

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == 'Новий':
            print('New Order status NEW')
            return self.readonly_fields + ('total_price',)
        return self.readonly_fields

    # inlines = [OrderPaymentInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]
    readonly_fields = ['order', 'pb_sale', 'total_price', ]

    def save_model(self, request, obj, form, change):
        print('Start from here----')
        product_populate = False
        update_fields = []
        for key, value in form.cleaned_data.items():
            # True if something changed in model
            if value != form.initial[key]:
                update_fields.append(key)
        update_fields.append('total_price')

        obj.save(update_fields=update_fields)
        # super().save_model(request, obj, form, change)

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
