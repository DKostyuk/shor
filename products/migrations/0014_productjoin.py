# Generated by Django 3.2.11 on 2022-01-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220123_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ProductJoin',
                'verbose_name_plural': 'ProductJoin',
            },
        ),
    ]
