# Generated by Django 3.2.11 on 2023-08-28 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_productinorder_due_date'),
        ('bonuses', '0003_auto_20230828_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusAccountEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance_num', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('comments', models.CharField(blank=True, default=None, max_length=124, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('bonus_cosmetolog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bonus_cosmetolog_event', to='bonuses.bonusaccountcosmetolog')),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order')),
            ],
            options={
                'verbose_name': 'BonusAccountEvent',
                'verbose_name_plural': 'BonusAccountEvents',
            },
        ),
    ]
