# Generated by Django 3.2.11 on 2022-03-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_ingredient_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredienttype',
            name='type_ref_number',
            field=models.IntegerField(blank=True, default=0, max_length=2, null=True),
        ),
    ]
