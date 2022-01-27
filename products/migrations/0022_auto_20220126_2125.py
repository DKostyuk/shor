# Generated by Django 3.2.11 on 2022-01-26 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20220126_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]