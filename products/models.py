from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import openpyxl
from django.contrib.auth.models import User
from shor.current_user import get_current_user
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from cosmetologs.models import Cosmetolog
from unidecode import unidecode


class ProductCategory(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=16, unique=True)
    description = RichTextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    product_category_logo_image = models.ImageField(upload_to='logo_images/', default='logo_images/DK_logo.png',
                                                    help_text="optimal size  600x450 - Need to be checked")
    product_category_page_image = models.ImageField(upload_to='logo_images/',
                                                    default='logo_images/DK_logo.png',
                                                    help_text="optimal size  600x450 - Need to be checked")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'


class ProductType(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=16, unique=True)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'


class ProductVolume(models.Model):
    name = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'ProductVolume'
        verbose_name_plural = 'ProductVolumes'


class ProductVolumeType(models.Model):
    name = models.CharField(max_length=4, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'ProductVolumeType'
        verbose_name_plural = 'ProductVolumeTypes'


class Product(models.Model):
    producer = models.CharField(max_length=64, blank=True, null=True, default='Shor')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    name_pl = models.CharField(max_length=128, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128, unique=True)
    name_description = models.CharField(max_length=64, blank=True, null=True, default=None)
    # description = RichTextField()
    description = models.TextField(blank=True, null=True, default=None)
    name_description_1 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_1 = RichTextField(blank=True, null=True, default=None)
    name_description_2 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_2 = models.TextField(blank=True, null=True, default=None)
    name_description_3 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_3 = models.TextField(blank=True, null=True, default=None)
    name_description_4 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_4 = models.TextField(blank=True, null=True, default=None)
    name_description_5 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_5 = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name
        # return "%s, %s" % (self.ref_number, self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


ProductAddFile_choices = [
    ('Add_Product_Item', 'Add_Product_Item'),
    ('Add_Product_Join', 'Add_Product_Join'),
    ('Add_Nothing', 'Add_Nothing'),
]


class ProductAddFile(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    what_to_do = models.CharField(max_length=16, choices=ProductAddFile_choices, default='Add_Nothing')
    product_file = models.FileField(upload_to='product_file_add/')
    is_active = models.BooleanField(default=False)
    start_import = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    def __unicode__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    class Meta:
        verbose_name = 'ProductAddFile'
        verbose_name_plural = 'ProductAddFiles'

    def save(self, *args, **kwargs):
        print("---------------зДЕСЯ --------------------")
        file_opened = openpyxl.load_workbook(filename=self.product_file)  # put attention for Excel file version
        active_sheet = file_opened.active
        data_file = active_sheet.values
        data_file = list(data_file)
        print("---------qqqqqqqqqq------------", data_file)
        choice = self.what_to_do
        if choice == 'Add_Product_Join':
            for i in range(0, len(data_file)):
                print("---------111111111111111------------", data_file[i])
                product = Product.objects.get(id=data_file[i][0])
                product.name_description = "Тип шкіри"
                product.description = data_file[i][1]
                product.name_pl = data_file[i][2]
                product.name_description_4 = "Кислотність"
                product.description_4 = data_file[i][3]
                product.name_description_5 = "Вміст кислот"
                product.description_5 = data_file[i][4]
                product.name_description_1 = "Опис"
                product.description_1 = data_file[i][5]
                product.name_description_2 = "Спосіб застосування"
                product.description_2 = data_file[i][6]
                product.name_description_3 = "Активні інгридієнти"
                product.description_3 = data_file[i][7]
                product.save()

                super(ProductAddFile, self).save(*args, **kwargs)

        elif choice == 'Add_Product_Item':
            for i in range(0, len(data_file)):
                print("---------Add_Product_Item------------", data_file[i])
                category = ProductCategory.objects.get(id=data_file[i][0])
                name = data_file[i][1]
                ref_number = data_file[i][2]
                volume = ProductVolume.objects.get(id=data_file[i][3])
                volume_type = ProductVolumeType.objects.get(id=data_file[i][4])
                product_type = ProductType.objects.get(id=data_file[i][5])
                new_product_item = ProductItem(
                    ref_number=ref_number,
                    name=name,
                    category=category,
                    type=product_type,
                    volume=volume,
                    volume_type=volume_type,
                    is_active=True)
                print('New-product--ITEM--------', new_product_item)
                new_product_item.save()

            products_item_all = ProductItem.objects.all()
            products_item_all_name = set()
            for product in products_item_all:
                products_item_all_name.add(product.name)
            products_all = Product.objects.all()
            products_all_name = set()
            for product in products_all:
                products_all_name.add(product.name)
            for p in products_item_all_name:
                if p not in products_all_name:
                    new_product = Product(
                        name=p,
                        is_active=True)
                    new_product.save()

                super(ProductAddFile, self).save(*args, **kwargs)


def join_products():
    print('----start----')
    products_item_all = ProductItem.objects.all()
    products_item_all_name = set()
    for product in products_item_all:
        print('----start join')
        products_item_all_name.add(product.name)
    print(products_item_all_name)
    products_all = Product.objects.all()
    products_all_name = set()
    for product in products_all:
        print('----start join---222222222')
        products_all_name.add(product.name)
    print(products_all_name)
    for p in products_item_all_name:
        print(p)
        if p in products_all_name:
            print("-------ПРИНТ ТУТУ----", p)
        else:
            new_product = Product(
                name=p,
                is_active=True)
            print('New-product----------', new_product)
            new_product.save()

    return 'test-success'


class ProductJoin(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'ProductJoin'
        verbose_name_plural = 'ProductJoin'

    def save(self, *args, **kwargs):
        s = join_products()
        print(s)
        super(ProductJoin, self).save(*args, **kwargs)


class CurrencyExchange(models.Model):
    usd_price_uah = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    usd_rate_initial = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    usd_rate_correct = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    usd_rate_before = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_before = models.DateTimeField(null=True, blank=True, default=None)
    usd_diff = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.usd_price_uah

    class Meta:
        verbose_name = 'CurrencyExchange'
        verbose_name_plural = 'CurrencyExchange'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
        self.usd_rate_before = self.usd_price_uah
        self.date_before = self.updated
        self.usd_price_uah = self.usd_rate_initial + self.usd_rate_correct
        self.usd_diff = self.usd_price_uah - self.usd_rate_before

        super(CurrencyExchange, self).save(*args, **kwargs)


class ProductItem(models.Model):
    ref_number = models.CharField(max_length=10, blank=True, null=True, default=None)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    volume = models.ForeignKey(ProductVolume, blank=True, null=True, default=None, on_delete=models.CASCADE)
    volume_type = models.ForeignKey(ProductVolumeType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    volume_equivalent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.name, self.volume)

    class Meta:
        verbose_name = 'ProductItem'
        verbose_name_plural = 'ProductItem'


class ProductSalesType(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'ProductSalesType'
        verbose_name_plural = 'ProductSalesTypes'


class ProductItemSales(models.Model):
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_current = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_old_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_current_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exchange_rate = models.ForeignKey(CurrencyExchange, blank=True, null=True, default=1, on_delete=models.DO_NOTHING)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.product_item

    class Meta:
        verbose_name = 'ProductItemSale'
        verbose_name_plural = 'ProductItemSales'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
        self.price_current_usd = self.price_old_usd * (1 - Decimal(str(self.discount / 100)))
        self.price_current = int(self.price_current_usd * self.exchange_rate.usd_price_uah) + 1
        self.price_old = int(self.price_old_usd * self.exchange_rate.usd_price_uah) + 1

        super(ProductItemSales, self).save(*args, **kwargs)

    @receiver(post_save, sender=CurrencyExchange)
    def create_user_profile(sender, instance, created, *args, **kwargs):
        # usd_rate = instance.usd_price_uah
        products_item_sales = ProductItemSales.objects.all()
        for p in products_item_sales:
            p.exchange_rate = instance
            p.save()


class BundleSale(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    name_pl = models.CharField(max_length=128, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=128, unique=True)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_current = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_old_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_current_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exchange_rate = models.ForeignKey(CurrencyExchange, blank=True, null=True, default=1, on_delete=models.DO_NOTHING)
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='bundles_images/', blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'BundleSale'
        verbose_name_plural = 'BundleSales'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
        self.price_current_usd = self.price_old_usd * (1 - Decimal(str(self.discount / 100)))
        self.price_current = int(self.price_current_usd * self.exchange_rate.usd_price_uah) + 1
        self.price_old = int(self.price_old_usd * self.exchange_rate.usd_price_uah) + 1
        self.slug = slugify(self.name)

        super(BundleSale, self).save(*args, **kwargs)

    @receiver(post_save, sender=CurrencyExchange)
    def update_exchange_rate(sender, instance, created, *args, **kwargs):
        # usd_rate = instance.usd_price_uah
        bundle_sales = BundleSale.objects.all()
        for p in bundle_sales:
            p.exchange_rate = instance
            p.save()


class ProductInBundle(models.Model):
    bundle = models.ForeignKey(BundleSale, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product_item

    class Meta:
        verbose_name = 'ProductInBundle'
        verbose_name_plural = 'ProductInBundles'
