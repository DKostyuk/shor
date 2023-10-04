from django.db import models
from cosmetologs.models import Cosmetolog
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from shor.current_user import get_current_user


class Subscriber(models.Model):
    email = models.EmailField()
    email_confirm = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=56, blank=True, null=True, default=None)
    index = models.CharField(max_length=6, blank=True, null=True, default=None)
    street = models.CharField(max_length=30, blank=True, null=True, default=None)
    locality = models.CharField(max_length=10, blank=True, null=True, default=None)
    tel_number = models.CharField(max_length=11, blank=True, null=True, default=None)
    company_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    nip = models.CharField(max_length=10, blank=True, null=True, default=None)
    company_confirm = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return "User %s %s %s %s" % (self.id, self.name, self.email, self.city)

    # def save(self, *args, **kwargs):
    #     email = self.user.email
    #     self.email = email
    #     # self.total_price = int(self.nmb) * price_per_item
    #
    #     super(Subscriber, self).save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Subscriber.objects.create(user=instance, email=str(instance))

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.subscriber.save()

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'


class SubscriberCosmetolog(models.Model):
    subscriber_name = models.ForeignKey(Subscriber, blank=True, null=True, default=None, on_delete=models.CASCADE)
    subscriber_id = models.IntegerField(blank=True, null=True, default=None)
    cosmetolog_name = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    cosmetolog_id = models.IntegerField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    class Meta:
        verbose_name = 'SubscriberCosmetolog'
        verbose_name_plural = 'SubscriberCosmetologs'


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
    alt = models.CharField(max_length=64, default='Please')
    image = models.ImageField(upload_to='slider_images/')
    url = models.URLField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    position = models.IntegerField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    activation_date = models.DateField(blank=True, default=None)
    deactivation_date = models.DateField(blank=True, default=None)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'SliderMain'
        verbose_name_plural = 'SliderMains'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user

        super(SliderMain, self).save(*args, **kwargs)


class LetterTemplate(models.Model):
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    name_sender = models.CharField(max_length=32)
    email_sender = models.EmailField(blank=True, null=True, default=None)
    message = models.TextField(blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'LetterTemplate'
        verbose_name_plural = 'LetterTemplates'


class Letter(models.Model):
    type = models.ForeignKey(LetterTemplate, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=64)
    from_name = models.CharField(max_length=32)
    email_sender = models.EmailField(blank=True, null=True, default=None)
    phone_sender = models.CharField(max_length=13, blank=True, null=True, default=None)
    city_sender = models.CharField(max_length=32)
    message = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    user_email = models.EmailField(blank=True, null=True, default=None)
    who_answer = models.CharField(max_length=64)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user

        super(Letter, self).save(*args, **kwargs)


class LetterEmail(models.Model):
    letter_template_name = models.ForeignKey(LetterTemplate, blank=True, null=True, default=None, on_delete=models.CASCADE)
    email_receiver = models.EmailField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    class Meta:
        verbose_name = 'LetterEmail'
        verbose_name_plural = 'LetterEmails'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user

        super(LetterEmail, self).save(*args, **kwargs)


class Page(models.Model):
    page_name = models.CharField(max_length=32)
    is_main_menu = models.BooleanField(default=False)
    rate_main_menu = models.IntegerField(blank=True, null=True, default=None)
    page_text = RichTextUploadingField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user

        super(Page, self).save(*args, **kwargs)


class Training(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    type = models.CharField(max_length=16)
    description = RichTextUploadingField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='training/', default='../img/bg_image.png')
    start_date = models.DateTimeField(default=None)
    duration = models.CharField(max_length=8)
    location = models.CharField(max_length=64)
    audience = models.CharField(max_length=32)
    goal = models.CharField(max_length=128)
    agenda = RichTextField(blank=True, null=True, default=None)
    trainer = models.CharField(max_length=32)
    total_place = models.IntegerField(blank=True, null=True, default=20)
    registered_place = models.IntegerField(blank=True, null=True, default=None)
    left_place = models.IntegerField(blank=True, null=True, default=None)
    left_place_shown = models.IntegerField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'

    def save(self, *args, **kwargs):
        self.left_place = int(self.total_place) - self.registered_place

        super(Training, self).save(*args, **kwargs)


class TrainingUser(models.Model):
    trainee_name = models.CharField(max_length=64)
    trainee_email = models.EmailField()
    is_active = models.BooleanField(default=False)
    trainee_tel_number = models.CharField(max_length=11, blank=True, null=True, default=None)
    tel_number_confirm = models.BooleanField(default=False)
    training = models.ForeignKey(Training, blank=True, null=True, default=None, on_delete=models.CASCADE)
    registration_confirmed = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    user_name = models.CharField(max_length=32)
    user_email = models.EmailField()

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'TrainingUser'
        verbose_name_plural = 'TrainingUsers'


class Feature(models.Model):
    feature_name = models.CharField(max_length=64)
    feature_code = models.IntegerField(blank=True, null=True, default=101)
    behaviour_code = models.IntegerField(blank=True, null=True, default=99)
    feature_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
