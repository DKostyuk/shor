# Generated by Django 3.2.11 on 2022-01-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_productitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='productaddfile',
            name='title',
            field=models.CharField(choices=[('Add_Product_Item', 'Add_Product_Item'), ('Add_Product_Join', 'Add_Product_Join'), ('Add_Nothing', 'Add_Nothing')], default='Add_Nothing', max_length=16),
        ),
    ]