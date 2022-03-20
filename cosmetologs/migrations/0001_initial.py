# Generated by Django 3.2.11 on 2022-03-09 17:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryForCosmetolog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CategoryForCosmetolog',
                'verbose_name_plural': 'CategoriesForCosmetolog',
            },
        ),
        migrations.CreateModel(
            name='Cosmetolog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosmetolog_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('cosmetolog_surname', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('cosmetolog_father_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('tel_number', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('certificate_image', models.ImageField(default=None, upload_to='certificate_images/')),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cosmetolog',
                'verbose_name_plural': 'Cosmetologs',
            },
        ),
        migrations.CreateModel(
            name='CosmetologType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CosmetologType',
                'verbose_name_plural': 'CosmetologTypes',
            },
        ),
        migrations.CreateModel(
            name='ServiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('price01', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('price02', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('price_avg', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_action', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.IntegerField(default=0)),
                ('description', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
                ('short_description', models.TextField(blank=True, default=None, null=True)),
                ('duration', models.CharField(blank=True, default=None, max_length=18, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.categoryforcosmetolog')),
                ('cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ServiceProduct',
                'verbose_name_plural': 'ServiceProducts',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryForCosmetolog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('subcategory_category', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('url', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.categoryforcosmetolog')),
            ],
            options={
                'verbose_name': 'SubCategoryForCosmetolog',
                'verbose_name_plural': 'SubCategoriesForCosmetolog',
            },
        ),
        migrations.CreateModel(
            name='ServiceProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service_product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.serviceproduct')),
            ],
            options={
                'verbose_name': 'ServiceProductPhoto',
                'verbose_name_plural': 'ServiceProductPhotos',
            },
        ),
        migrations.AddField(
            model_name='serviceproduct',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.subcategoryforcosmetolog'),
        ),
        migrations.CreateModel(
            name='ServiceAddFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('service_file', models.FileField(upload_to='product_file_add/')),
                ('is_active', models.BooleanField(default=False)),
                ('start_import', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ServiceAddFile',
                'verbose_name_plural': 'ServiceAddFiles',
            },
        ),
        migrations.CreateModel(
            name='CosmetologPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
            ],
            options={
                'verbose_name': 'CosmetologPhone',
                'verbose_name_plural': 'CosmetologPhones',
            },
        ),
        migrations.CreateModel(
            name='CosmetologEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
            ],
            options={
                'verbose_name': 'CosmetologEmail',
                'verbose_name_plural': 'CosmetologEmails',
            },
        ),
        migrations.CreateModel(
            name='CosmetologCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.categoryforcosmetolog')),
                ('cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
                ('subcategory', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.subcategoryforcosmetolog')),
            ],
            options={
                'verbose_name': 'CosmetologCategory',
                'verbose_name_plural': 'CosmetologCategories',
            },
        ),
        migrations.CreateModel(
            name='CosmetologAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosmetolog_id', models.IntegerField(blank=True, default=None, null=True)),
                ('service_id', models.IntegerField(blank=True, default=None, null=True)),
                ('address_id', models.IntegerField(blank=True, default=None, null=True)),
                ('address_type_id', models.IntegerField(blank=True, default=None, null=True)),
                ('city_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('district_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('street_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('cosmetolog_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
                ('service_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.serviceproduct')),
            ],
            options={
                'verbose_name': 'CosmetologAddress',
                'verbose_name_plural': 'CosmetologAddresses',
            },
        ),
        migrations.CreateModel(
            name='CosmetologAddFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('cosmetolog_file', models.FileField(upload_to='product_file_add/')),
                ('is_active', models.BooleanField(default=False)),
                ('start_import', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CosmetologAddFile',
                'verbose_name_plural': 'CosmetologAddFiles',
            },
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetologtype'),
        ),
        migrations.AddField(
            model_name='cosmetolog',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
