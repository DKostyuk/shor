from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=56, default='Unknown')

    def __str__(self):
        return "User %s %s %s %s" % (self.id, self.name, self.email, self.city)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'


class LogoImage(models.Model):
    image = models.ImageField(upload_to='logo_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'LogoPhoto'
        verbose_name_plural = 'LogoPhotos'


class SliderMain(models.Model):
    ad_name = models.CharField(max_length=64)
    ad_customer = models.CharField(max_length=64)
    ad_description = models.TextField(blank=True, null=True, default=None)
    ad_title = models.CharField(max_length=128)
    ad_text = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='advert_images/')
    url = models.URLField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    activation_date = models.DateField(blank=True, default=None)
    deactivation_date = models.DateField(blank=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'SliderMain'
        verbose_name_plural = 'SliderMains'
