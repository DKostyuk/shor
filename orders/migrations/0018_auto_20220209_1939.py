# Generated by Django 3.2.11 on 2022-02-09 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0017_statuspayment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuspayment',
            options={'verbose_name': 'StatusPayment', 'verbose_name_plural': 'StatusPayments'},
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
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.statuspayment')),
            ],
            options={
                'verbose_name': 'OrderPayment',
                'verbose_name_plural': 'OrderPayments',
            },
        ),
    ]
