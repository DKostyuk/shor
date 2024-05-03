# Generated by Django 3.2.11 on 2023-03-18 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220718_1152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0005_auto_20230312_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitemplus',
            name='product_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_product_item_plus', to='products.productitem'),
        ),
        migrations.CreateModel(
            name='StockItemMinus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_minus', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_product_item_minus', to='products.productitem')),
            ],
            options={
                'verbose_name': 'StockItemMinus',
                'verbose_name_plural': 'StockItemMinus',
            },
        ),
    ]
