from django.db import models
# from landing.models import Subscriber
from addresses.models import Address
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from shor.current_user import get_current_user
from ckeditor.fields import RichTextField
import openpyxl
# from django.utils import timezone
# from django.utils.text import slugify
from uuslug import slugify
# from django.utils import unique_slug_generator
from django.utils import timezone


class CategoryForCosmetolog(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CategoryForCosmetolog'
        verbose_name_plural = 'CategoriesForCosmetolog'


def subcategory_category_creator(self):
    subcategory_category = self.name + ', ' + self.category.name
    url = self.category.slug + '/' + self.slug

    return subcategory_category, url


class SubCategoryForCosmetolog(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory_category = models.CharField(max_length=64, blank=True, null=True, default=None)
    url = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.name, self.category)

    def __unicode__(self):
        # return "%s" % self.name
        return "%s, %s, %s" % (self.name, self.category, self.url)

    class Meta:
        verbose_name = 'SubCategoryForCosmetolog'
        verbose_name_plural = 'SubCategoriesForCosmetolog'

    def save(self, *args, **kwargs):
        self.subcategory_category, self.url = subcategory_category_creator(self)

        super(SubCategoryForCosmetolog, self).save(*args, **kwargs)


class CosmetologType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=32, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CosmetologType'
        verbose_name_plural = 'CosmetologTypes'


class Cosmetolog(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    type = models.ForeignKey(CosmetologType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    city = models.CharField(max_length=16, blank=True, null=True, default=None)
    certificate_image = models.ImageField(upload_to='certificate_images/', default=None)
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Cosmetolog'
        verbose_name_plural = 'Cosmetologs'


class CosmetologEmail(models.Model):
    email = models.EmailField(blank=True, null=True, default=None)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.email

    class Meta:
        verbose_name = 'CosmetologEmail'
        verbose_name_plural = 'CosmetologEmails'


class CosmetologPhone(models.Model):
    phone = models.CharField(max_length=10, blank=True, null=True, default=None)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.phone

    class Meta:
        verbose_name = 'CosmetologPhone'
        verbose_name_plural = 'CosmetologPhones'


class CosmetologCategory(models.Model):
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryForCosmetolog, blank=True, null=True, default=None,
                                    on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'CosmetologCategory'
        verbose_name_plural = 'CosmetologCategories'


class ServiceProduct(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=64, unique=True)
    price01 = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    price02 = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    price_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # (price01+price02)/2
    price_action = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForCosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategoryForCosmetolog, blank=True, null=True, default=None,
                                    on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    duration = models.CharField(max_length=18, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name
        # return "%s, %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'ServiceProduct'
        verbose_name_plural = 'ServiceProducts'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user
            # if not self.id:
            #     self.created_by = user
        super(ServiceProduct, self).save(*args, **kwargs)


class ServiceProductImage(models.Model):
    service_product = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'ServiceProductPhoto'
        verbose_name_plural = 'ServiceProductPhotos'


def create_slug(sender, instance):
    print(123456789, sender)
    slug = slugify(instance.name)
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        last = sender.objects.last()
        new_slug = "%s-%s" % (slug, last.id)
        return new_slug
    else:
        return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    # if not instance.headline:
    #     instance.headline = instance.description[:70]
    if not instance.slug:
        instance.slug = create_slug(sender, instance)
        # instance.slug = unique_slug_generator(instance)


# pre_save.connect(pre_save_post_receiver, sender=CategoryForCosmetolog)
# pre_save.connect(pre_save_post_receiver, sender=Cosmetolog)
# pre_save.connect(pre_save_post_receiver, sender=ServiceProduct)


class CosmetologAddress(models.Model):
    cosmetolog_name = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cosmetolog_id = models.IntegerField(blank=True, null=True, default=None)
    service_name = models.ForeignKey(ServiceProduct, blank=True, null=True, default=None, on_delete=models.CASCADE)
    service_id = models.IntegerField(blank=True, null=True, default=None)
    address_name = models.ForeignKey(Address, blank=True, null=True, default=None, on_delete=models.CASCADE)
    address_id = models.IntegerField(blank=True, null=True, default=None)
    address_type_id = models.IntegerField(blank=True, null=True, default=None)
    city_id = models.IntegerField(blank=True, null=True, default=-1)
    district_id = models.IntegerField(blank=True, null=True, default=-1)
    street_id = models.IntegerField(blank=True, null=True, default=-1)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'CosmetologAddress'
        verbose_name_plural = 'CosmetologAddresses'

    def save(self, *args, **kwargs):
        self.cosmetolog_id = self.cosmetolog_name_id
        self.address_id = self.address_name_id
        self.service_id = self.service_name_id
        print(9999, self.address_name.type_id)
        self.address_type_id = self.address_name.type_id
        if self.address_type_id == 10:
            self.street_id = self.address_id
            self.district_id = self.address_name.parent_id.id
            print(1234, self.address_name.parent_id.parent_id.id)
            print(1234, type(self.address_name.parent_id.parent_id.id))
            self.city_id = self.address_name.parent_id.parent_id.id
        elif self.address_type_id == 5:
            self.district_id = self.address_type_id
        # self.city_id = 4

        super(CosmetologAddress, self).save(*args, **kwargs)


class CosmetologAddFile(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    cosmetolog_file = models.FileField(upload_to='product_file_add/')
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
        verbose_name = 'CosmetologAddFile'
        verbose_name_plural = 'CosmetologAddFiles'

    def save(self, *args, **kwargs):
        file_opened = openpyxl.load_workbook(filename=self.cosmetolog_file)  # put attention for Excel file version
        active_sheet = file_opened.active
        data_file = active_sheet.values
        data_file = list(data_file)
        for i in range(0, len(data_file)):
            site_url = data_file[i][0]
            print('site-url-------------', site_url)
            name = data_file[i][1]
            type_text = data_file[i][2]
            logo_image = data_file[i][4]
            description = data_file[i][5]
            description_region = data_file[i][6]
            working_hours = data_file[i][7]
            order_phone = data_file[i][8]
            type = CosmetologType.objects.get(id=1)
            print('logo', logo_image)
            new_cosmetolog = Cosmetolog(
                site_url=site_url,
                name=name,
                description=description,
                description_region=description_region,
                working_hours=working_hours,
                order_phone=order_phone,
                logo_image=logo_image,
                type_text=type_text,
                type=type,
                is_active=True,
                is_visible=True,
                registration_time=timezone.now()
            )
            new_cosmetolog.save()

            super(CosmetologAddFile, self).save(*args, **kwargs)


class ServiceAddFile(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    service_file = models.FileField(upload_to='product_file_add/')
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
        verbose_name = 'ServiceAddFile'
        verbose_name_plural = 'ServiceAddFiles'

    def save(self, *args, **kwargs):
        file_opened = openpyxl.load_workbook(filename=self.service_file)  # put attention for Excel file version
        active_sheet = file_opened.active
        data_file = active_sheet.values
        data_file = list(data_file)
        for i in range(0, len(data_file)):
            cosmetolog = Cosmetolog.objects.get(site_url=data_file[i][0])
            print('cosmetolog ID -------', cosmetolog)
            # print('site-url-------------', site_url)
            service_name = data_file[i][1]
            print('service name  -------', service_name)
            # service_price = data_file[i][2]
            service_price = int(data_file[i][2].replace(' грн', ''))
            # print('price ----', service_price, type(service_price))
            duration = data_file[i][3]
            description = data_file[i][4]
            category = CategoryForCosmetolog.objects.get(id=data_file[i][7])
            subcategory = SubCategoryForCosmetolog.objects.get(id=data_file[i][8])
            new_service = ServiceProduct(
                cosmetolog=cosmetolog,
                name=service_name,
                description=description,
                duration=duration,
                price01=service_price,
                price02=service_price,
                category = category,
                subcategory = subcategory,
                # logo_image=logo_image,
                is_active=True,
                is_visible=True,
            )
            new_service.save()
            try:
                service_product = ServiceProduct.objects.get(cosmetolog=cosmetolog, name=service_name,
                                                             price01=service_price, duration=duration)
                print('111111111111111111111------------', service_product)
            except:
                service_product = ServiceProduct.objects.filter(cosmetolog=cosmetolog, name=service_name)
                print('222222222222222222222222222------------', service_product)
            # print('qwerty -------------', service_product)
            image = data_file[i][6]
            new_service_image = ServiceProductImage(
                service_product=service_product,
                image=image,
                is_active=True,
                is_main=True,
            )
            new_service_image.save()

            super(ServiceAddFile, self).save(*args, **kwargs)
