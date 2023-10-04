import openpyxl
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import ProductInOrder, Order
from products.models import ProductItem, CurrencyExchange, ProductCategory, SaleProductItem
from shor.current_user import get_current_user
from cosmetologs.models import Cosmetolog


# class BlogCategory(models.Model):
#     name = models.CharField(max_length=32, blank=True, null=True, default=None)
#     slug = models.SlugField(max_length=32, unique=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return "%s" % self.name
#
#     class Meta:
#         verbose_name = 'CategoryBlog'
#         verbose_name_plural = 'CategoryBlogs'

class PurchaseItem(models.Model):
    id_purchase = models.CharField(max_length=16, blank=True, null=True, default=None)
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id_purchase

    class Meta:
        verbose_name = 'PurchaseItem'
        verbose_name_plural = 'PurchaseItems'


class StockTotal(models.Model):
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                     related_name='stock_total_product_item')
    num_total = models.IntegerField(default=0)
    price_total_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_total_uah = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.product_item
        # return "%s, %s" % (self.price, self.name)

    def __unicode__(self):
        return "%s" % self.product_item

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'


class StockItemPurchase(models.Model):
    id_purchase = models.ForeignKey(PurchaseItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                    related_name='stock_purchase_item')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                     related_name='stock_purchase_product_item')
    num_item = models.IntegerField(default=0)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_uah = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price_uah = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'StockItemPurchase'
        verbose_name_plural = 'StockItemPurchases'

    def save(self, *args, **kwargs):
        if self.is_active:
            user = get_current_user()
            if user and user.is_authenticated:
                self.modified_by = user
        else:
            print('HERE nothing to save to Stock plus 2023')

        super(StockItemPurchase, self).save(*args, **kwargs)


class StockFilePlus(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    stock_file = models.FileField(upload_to='stock_file_add/', blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'StockFilePlus'
        verbose_name_plural = 'StockFilePluses'

    def save(self, *args, **kwargs):
        if self.is_active:
            user = get_current_user()
            if user and user.is_authenticated:
                self.modified_by = user
            exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
            if self.stock_file:
                file_opened = openpyxl.load_workbook(filename=self.stock_file)  # put attention for Excel file version
                active_sheet = file_opened.active
                data_file = active_sheet.values
                data_file = list(data_file)
                for i in range(1, len(data_file)):
                    print('len file ----', len(data_file))
                    print("---------Add_Stock_Sale------------", data_file[i])
                    product_item_ref_number = str(data_file[i][3]).strip()
                    print(product_item_ref_number, type(product_item_ref_number))
                    print('due date -----', data_file[i][8])
                    product_item = ProductItem.objects.get(ref_number=product_item_ref_number)
                    new_stock_product_item = StockItemPlus(
                        product_item=product_item,
                        id_purchase=data_file[i][2],
                        num_plus=data_file[i][5],
                        price_plus_usd=data_file[i][6],
                        price_plus_uah=data_file[i][6] * exchange_rate,
                        due_date=data_file[i][8],
                        comments=data_file[i][9],
                        is_active=True
                    )
                    new_stock_product_item.save()
                    print('Add_Stock_Product_Item--------', new_stock_product_item)
        else:
            print('HERE nothing to save to Stock plus 2023')

        super(StockFilePlus, self).save(*args, **kwargs)


class StockItemPlus(models.Model):
    id_purchase = models.ForeignKey(PurchaseItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                    related_name='stock_purchase_item_plus')
    # id_purchase = models.CharField(max_length=16, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                     related_name='stock_product_item_plus')
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    num_plus = models.IntegerField(default=0)
    price_plus_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_plus_uah = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price_plus_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price_plus_uah = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'StockItemPlus'
        verbose_name_plural = 'StockItemPluses'

    def save(self, *args, **kwargs):
        if self.is_active:
            user = get_current_user()
            if user and user.is_authenticated:
                self.modified_by = user
            self.category = self.product_item.category
            exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
            print('HERE will be save Stock plus')
            self.price_plus_uah = self.price_plus_usd * exchange_rate
            self.total_price_plus_usd = self.price_plus_usd * self.num_plus
            self.total_price_plus_uah = self.price_plus_uah * self.num_plus
        else:
            print('HERE nothing to save to Stock plus 2023')

        super(StockItemPlus, self).save(*args, **kwargs)


class StockItemMinus(models.Model):
    id_purchase = models.ForeignKey(PurchaseItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                    related_name='stock_purchase_item_minus')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                     related_name='stock_product_item_minus')
    num_minus = models.IntegerField(default=0)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'StockItemMinus'
        verbose_name_plural = 'StockItemMinus'

    def save(self, *args, **kwargs):
        if self.is_active:
            user = get_current_user()
            if user and user.is_authenticated:
                self.modified_by = user
            self.category = self.product_item.category
        else:
            print('HERE nothing to save to Stock minus 2023')

        super(StockItemMinus, self).save(*args, **kwargs)


class StockItemReserved(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                     related_name='stock_product_item_reserved')
    num_reserved = models.IntegerField(default=0)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'StockItemReserved'
        verbose_name_plural = 'StockItemReserved'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
        self.category = self.product_item.category

        super(StockItemReserved, self).save(*args, **kwargs)


class StockItemRest(models.Model):
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING,
                                     related_name='stock_product_item_rest')
    num_rest = models.IntegerField(default=0)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, )
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'StockItemRest'
        verbose_name_plural = 'StockItemRest'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
        self.category = self.product_item.category

        super(StockItemRest, self).save(*args, **kwargs)


@receiver(post_save, sender=ProductInOrder)
def update_stock_item_minus(sender, instance, created, update_fields, *args, **kwargs):
    print('kwards 444-----------', instance.nmb)
    # print('Start SAVE for Product in Bucket')
    # print(update_fields)
    # print(type(update_fields))
    if created:
        print('aswer ------ ', instance.pb_sale)
        pass
        # exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        # stock_product_item = instance.product_item
        # num_minus = instance.num_minus
        # modified_by = instance.modified_by
        # stock_product = StockItemPurchase.objects.get(id_purchase=instance.id_purchase, product_item=stock_product_item)
        # # think - How to rise the problem if no item on stock
        # stock_product.num_item -= num_minus
        # stock_product.price_uah = stock_product.price_usd * exchange_rate
        # stock_product.total_price_usd = stock_product.price_usd * stock_product.num_item
        # stock_product.total_price_uah = stock_product.price_uah * stock_product.num_item
        # stock_product.modified_by = modified_by
        # stock_product.save(force_update=True)
    if update_fields:
        print('aswer update_fields------ ', instance.pb_sale)
        s = SaleProductItem.objects.get(sales_product=instance.pb_sale)
        print('aswer update_fields--111---- ', s.product_item)
        product_item = ProductItem.objects.get(id=s.product_item.id)
        p = StockItemMinus.objects.create(product_item=product_item)
        p.is_active = True
        p.num_minus = instance.nmb
        p.save(force_update=True)
        for i in update_fields:
            print('iiiiiiii----', i, type(i))
        pass
        # print('99999999999999999999999999999999999')
        # print(update_fields)
        # print(type(update_fields))
        # print('9--------------------------------9999999999999999999999999999999999')


@receiver(post_save, sender=StockItemPlus)
def update_create_stock_total(sender, instance, created, *args, **kwargs):
    if created:
        exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        stock_product_item = instance.product_item
        num_plus = instance.num_plus
        total_price_usd = instance.total_price_plus_usd
        total_price_uah = instance.total_price_plus_uah
        modified_by = instance.modified_by
        new_stock_product, created_total = StockTotal.objects.get_or_create(product_item=stock_product_item)

        if created_total:
            new_stock_product.category = instance.category
            new_stock_product.num_total = num_plus
            new_stock_product.price_total_usd = total_price_usd
            new_stock_product.price_total_uah = total_price_uah
            new_stock_product.modified_by = modified_by
            new_stock_product.save(force_update=True)
            print('created total ===', created_total)
        else:
            new_stock_product.num_total += num_plus
            new_stock_product.price_total_usd += total_price_usd
            new_stock_product.price_total_uah = new_stock_product.price_total_usd * exchange_rate
            new_stock_product.modified_by = modified_by
            new_stock_product.save(force_update=True)
            print('UPDATED total ===', created_total)


@receiver(post_save, sender=StockItemPlus)
def create_stock_item_purchase(sender, instance, created, *args, **kwargs):
    if created:
        stock_purchase_product = instance.product_item
        id_purchase = instance.id_purchase
        due_date = instance.due_date
        new_stock_purchase, created_purchase = StockItemPurchase.objects.get_or_create(product_item=stock_purchase_product,
                                                                                    due_date=due_date)
        if created_purchase:
            new_stock_purchase.id_purchase = instance.id_purchase
            new_stock_purchase.category = instance.category
            new_stock_purchase.product_item = instance.product_item
            new_stock_purchase.num_item = instance.num_plus
            new_stock_purchase.price_usd = instance.price_plus_usd
            new_stock_purchase.price_uah = instance.price_plus_uah
            new_stock_purchase.total_price_usd = instance.total_price_plus_usd
            new_stock_purchase.total_price_uah = instance.total_price_plus_uah
            new_stock_purchase.due_date = instance.due_date
            new_stock_purchase.comments = instance.comments
            new_stock_purchase.is_active = True
            new_stock_purchase.modified_by = instance.modified_by
            new_stock_purchase.save(force_update=True)
        else:
            exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
            new_stock_purchase.num_item += instance.num_plus
            new_stock_purchase.price_total_usd += instance.total_price_plus_usd
            new_stock_purchase.price_usd = new_stock_purchase.price_total_usd / new_stock_purchase.num_item
            new_stock_purchase.price_uah = new_stock_purchase.price_usd * exchange_rate
            new_stock_purchase.price_total_uah = new_stock_purchase.price_total_usd * exchange_rate
            new_stock_purchase.modified_by = instance.modified_by

        new_stock_purchase.save(force_update=True)


@receiver(post_save, sender=StockItemPlus)
def create_stock_item_rest(sender, instance, created, *args, **kwargs):
    if created:
        stock_product_rest = instance.product_item
        due_date = instance.due_date
        new_stock_rest, created_rest = StockItemRest.objects.get_or_create(product_item=stock_product_rest,
                                                                           due_date=due_date)
        if created_rest:
            new_stock_rest.category = instance.category
            new_stock_rest.product_item = instance.product_item
            new_stock_rest.num_rest = instance.num_plus
            new_stock_rest.due_date = instance.due_date
            new_stock_rest.modified_by = instance.modified_by
            new_stock_rest.save(force_update=True)
        else:
            exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
            new_stock_rest.num_rest += instance.num_plus
            new_stock_rest.modified_by = instance.modified_by

        new_stock_rest.save(force_update=True)


@receiver(post_save, sender=StockItemMinus)
def update_stock_item_purchase(sender, instance, created, *args, **kwargs):
    if created:
        exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        stock_product_item = instance.product_item
        num_minus = instance.num_minus
        modified_by = instance.modified_by
        stock_product = StockItemPurchase.objects.get(id_purchase=instance.id_purchase, product_item=stock_product_item)
        # think - How to rise the problem if no item on stock
        stock_product.num_item -= num_minus
        stock_product.price_uah = stock_product.price_usd * exchange_rate
        stock_product.total_price_usd = stock_product.price_usd * stock_product.num_item
        stock_product.total_price_uah = stock_product.price_uah * stock_product.num_item
        stock_product.modified_by = modified_by
        stock_product.save(force_update=True)


@receiver(post_save, sender=StockItemMinus)
def update_stock_total(sender, instance, created, *args, **kwargs):
    if created:
        exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        stock_product_item = instance.product_item
        num_minus = instance.num_minus
        modified_by = instance.modified_by
        stock_product = StockTotal.objects.get(product_item=stock_product_item)
        stock_item_plus = StockItemPlus.objects.get(id_purchase=instance.id_purchase, product_item=stock_product_item)
        # think - How to rise the problem if no item on stock
        stock_product.num_total -= num_minus
        print(stock_item_plus.price_plus_usd, "*", stock_product.num_total)
        stock_product.price_total_usd = stock_product.price_total_usd - (stock_item_plus.price_plus_usd * num_minus)
        stock_product.price_total_uah = stock_product.price_total_usd * exchange_rate
        stock_product.modified_by = modified_by
        stock_product.save(force_update=True)
