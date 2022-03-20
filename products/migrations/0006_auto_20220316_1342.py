# Generated by Django 3.2.11 on 2022-03-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220313_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'IngredientType',
                'verbose_name_plural': 'IngredientTypes',
            },
        ),
        migrations.AlterModelOptions(
            name='productitem',
            options={'verbose_name': 'ProductItem', 'verbose_name_plural': 'ProductItems'},
        ),
    ]
