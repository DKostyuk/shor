# Generated by Django 3.2.11 on 2022-04-22 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cosmetologs', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('receiver_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('receiver_surname', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('receiver_father_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('receiver_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('receiver_phone', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('receiver_delivery_address', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='StatusOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_number', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'StatusOrder',
                'verbose_name_plural': 'StatusOrders',
            },
        ),
        migrations.CreateModel(
            name='StatusPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_number', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'StatusPayment',
                'verbose_name_plural': 'StatusPayments',
            },
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('cosmetolog', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('cosmetolog_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('service_product', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('price01', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price02', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('customer_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('customer_city', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cosmetolog_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.cosmetolog')),
                ('service_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cosmetologs.serviceproduct')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.statusorder')),
            ],
            options={
                'verbose_name': 'ServiceOrder',
                'verbose_name_plural': 'ServiceOrders',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('pb_sale', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.salesproduct')),
            ],
            options={
                'verbose_name': 'ProductInOrder',
                'verbose_name_plural': 'ProductInOrders',
            },
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('pb_sale', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.salesproduct')),
            ],
            options={
                'verbose_name': 'ProductInBasket',
                'verbose_name_plural': 'ProductInBaskets',
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.statuspayment')),
            ],
            options={
                'verbose_name': 'OrderPayment',
                'verbose_name_plural': 'OrderPayments',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.statusorder'),
        ),
    ]
