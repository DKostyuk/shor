# Generated by Django 3.2.11 on 2022-07-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='feature_code',
            field=models.IntegerField(blank=True, default=101, null=True),
        ),
    ]
