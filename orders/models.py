import requests
from django.db import models
# from bonuses.models import BonusAccountCosmetolog
from products.models import SalesProduct
from cosmetologs.models import ServiceProduct, Cosmetolog
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from shor.current_user import get_current_user
from utils.emails import SendingMessage
from products.models import CurrencyExchange


class StatusPayment(models.Model):
    status_number = models.IntegerField(default=0)
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'StatusPayment'
        verbose_name_plural = 'StatusPayments'


class StatusOrder(models.Model):
    status_number = models.IntegerField(default=0)
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'StatusOrder'
        verbose_name_plural = 'StatusOrders'


class Order(models.Model):
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    order_number = models.IntegerField(default=0)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cosmetolog_bonus = models.ForeignKey(to='bonuses.BonusAccountCosmetolog', blank=True, null=True, default=None,
                                         on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total price for all products in order
    receiver_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    receiver_surname = models.CharField(max_length=64, blank=True, null=True, default=None)
    receiver_father_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    receiver_email = models.EmailField(blank=True, null=True, default=None)
    receiver_phone = models.CharField(max_length=16, blank=True, null=True, default=None)
    receiver_delivery_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s %s" % (self.order_number, self.status.name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    pb_sale = models.ForeignKey(SalesProduct, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.pb_sale

    class Meta:
        verbose_name = 'ProductInOrder'
        verbose_name_plural = 'ProductInOrders'

    def save(self, *args, **kwargs):
        # price_per_item = self.product.price_current
        # Проверить - а вообще подумать над логикой если изменяется цена продукта в то время когда лежит товар в корзине
        # Проверить - а вообще подумать над логикой изменения товара в ORDER - все модификации должны быть там
        # self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    user = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    pb_sale = models.ForeignKey(SalesProduct, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.pb_sale

    class Meta:
        verbose_name = 'ProductInBasket'
        verbose_name_plural = 'ProductInBaskets'

    def save(self, *args, **kwargs):
        if self.user == "Anonymous":
            price_per_item = self.pb_sale.price_visitor_current
        else:
            price_per_item = self.pb_sale.price_current
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * self.price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)


# Order of Service
# ___________________________________

class ServiceOrder(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    cosmetolog_id = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cosmetolog = models.CharField(max_length=128, blank=True, null=True, default=None)
    cosmetolog_email = models.EmailField(blank=True, null=True, default=None)
    service_product = models.CharField(max_length=64, blank=True, null=True, default=None)
    service_id = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price01 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price02 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(blank=True, null=True, default=0)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_city = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(StatusOrder, blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "ServiceOrder %s" % self.id

    class Meta:
        verbose_name = 'ServiceOrder'
        verbose_name_plural = 'ServiceOrders'

    def save(self, *args, **kwargs):

        super(ServiceOrder, self).save(*args, **kwargs)


class OrderPayment(models.Model):
    status = models.ForeignKey(StatusPayment, default=None, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    payment_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "Order %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'OrderPayment'
        verbose_name_plural = 'OrderPayments'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user

        super(OrderPayment, self).save(*args, **kwargs)


@receiver(post_save, sender=Order)
def create_order_number(sender, instance, created, *args, **kwargs):
    if created:
        print('----after Order creation----')
        instance.order_number = 100100 + instance.id
        instance.save(force_update=True)
        # msg = SendingMessage()
        # msg.sending_msg()
        # TOKEN = '6074504475:AAF3aSo-sxwZl4ACvQcKAbBJV50iHV6OkVA'
        # chat_id = '595065850'
        # message = "hello from YOUR 2023 telegram bot"
        # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        # print(requests.get(url).json())  # this sends the message


@receiver(post_save, sender=SalesProduct)
def update_price_per_item(sender, instance, created, *args, **kwargs):
    # usd_rate = instance.usd_price_uah
    products_in_order = ProductInOrder.objects.filter(pb_sale=instance, is_active=True)
    for p in products_in_order:
        # p.price_per_item = instance.price_current
        # p.price_old = p.price_old_usd * usd_rate
        # p.price_current = p.price_current_usd * usd_rate
        p.save()


def product_in_order_post_save(sender, instance, created, **kwargs):
    print('SAVE ORDER in admin yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    # print('cosmetolog_bonus    ', instance.order.cosmetolog_bonus.bonus_account.ref_number)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    if instance.order.cosmetolog_bonus is not None and instance.order.cosmetolog_bonus.bonus_account.ref_number == '22':
        print('11111111111111111111111111 MONTHLY     ----------------', order_total_price)
        order_total_price = order_total_price * (100-instance.order.cosmetolog_bonus.bonus_account.uah_rate)/100
        print('22222222222222222222222222222222222 MONTHLY     ----------------', order_total_price)
        print('333333333333333333333 MONTHLY     ----------------', instance.order.cosmetolog_bonus.bonus_account.uah_rate)
    instance.order.total_price = order_total_price
    print('instance         ', instance.order.total_price)
    instance.order.save(force_update=True)
    print('instance         ', instance.order.total_price)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


# @receiver(post_save, sender=ProductInOrder)
# def product_in_order_post_save(sender, instance, created, **kwargs):
#     print('SAVE ORDER in admin llllllllllllllllllllllllllllllllllllllllllllllllllll')
#     order = instance.order
#     all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
#     print('cosmetolog_bonus    ', instance.order.cosmetolog_bonus)
#     order_total_price = 0
#     for item in all_products_in_order:
#         order_total_price += item.total_price
#
#     instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)


@receiver(post_save, sender=ProductInOrder)
def xxxxxx(sender, instance, created, *args, **kwargs):
    print('TEST-TEST-TESt-TEST')


@receiver(post_save, sender=SalesProduct)
def update_price_per_item(sender, instance, created, *args, **kwargs):
    # usd_rate = instance.usd_price_uah
    products_in_basket = ProductInBasket.objects.filter(pb_sale=instance, is_active=True)
    for p in products_in_basket:
        # p.price_per_item = instance.price_current
        # p.price_old = p.price_old_usd * usd_rate
        # p.price_current = p.price_current_usd * usd_rate
        p.save()


@receiver(post_save, sender=Order)
def update_order_total_price(sender, instance, created, *args, **kwargs):
    order_payments = OrderPayment.objects.filter(order=instance)
    for op in order_payments:
        op.order_total_price = instance.total_price
        op.save(force_update=True)


# @receiver(post_save, sender=Order)
# def autofill_cosmo_info(sender, instance, created, *args, **kwargs):
#     cosmetolog = Cosmetolog.objects.get(id=instance.cosmetolog.id)
#     print(instance.cosmetolog.cosmetolog_name, "             TUTATUTAAAAAAAAAAAAAAAA")
#     instance.receiver_name = cosmetolog.cosmetolog_name
#     instance.save(force_update=True)
