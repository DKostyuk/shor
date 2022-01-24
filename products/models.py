from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import openpyxl
from django.contrib.auth.models import User
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
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    producer = models.CharField(max_length=64, blank=True, null=True, default=None)
    ref_number = models.CharField(max_length=10, blank=True, null=True, default=None)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_pl = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=64, unique=True)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    volume = models.ForeignKey(ProductVolume, blank=True, null=True, default=None, on_delete=models.CASCADE)
    volume_type = models.ForeignKey(ProductVolumeType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    volume_equivalent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    name_description = models.CharField(max_length=64, blank=True, null=True, default=None)
    # description = RichTextField()
    description = models.TextField(blank=True, null=True, default=None)
    name_description_1 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_1 = RichTextField()
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
        # return "%s" % self.name
        return "%s, %s" % (self.ref_number, self.name)

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


class ProductAddFile(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
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
        for i in range(0, len(data_file)):
            print("---------111111111111111------------", data_file[i])
            category = ProductCategory.objects.get(id=data_file[i][0])
            type_skin_title = "Тип шкіри"
            type_skin = data_file[i][1]
            name = data_file[i][2]
            name_pl = data_file[i][3]
            ref_number = data_file[i][4]
            volume = ProductVolume.objects.get(id=data_file[i][5])
            volume_type = ProductVolumeType.objects.get(id=data_file[i][6])
            acid_title = "Кислотність"
            acid = data_file[i][7]
            volume_acid_title = "Вміст кислот"
            volume_acid = data_file[i][8]
            product_description_title = "Опис"
            product_description = data_file[i][9]
            product_usage_title = "Спосіб застосування"
            product_usage = data_file[i][10]
            product_inside_title = "Активні інгридієнти"
            product_inside = data_file[i][11]
            new_product = Product(
                category=category,
                name_description=type_skin_title,
                description=type_skin,
                name=name,
                name_pl=name_pl,
                ref_number=ref_number,
                volume=volume,
                volume_type=volume_type,
                name_description_4=acid_title,
                description_4=acid,
                name_description_5=volume_acid_title,
                description_5=volume_acid,
                name_description_1=product_description_title,
                description_1=product_description,
                name_description_2=product_usage_title,
                description_2=product_usage,
                name_description_3=product_inside_title,
                description_3=product_inside,
                is_active=True)
            print('New-product----------', new_product)
            new_product.save()

            super(ProductAddFile, self).save(*args, **kwargs)
