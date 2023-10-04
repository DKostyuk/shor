from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import CurrencyExchange
from stock.models import StockItemPlus, StockTotal, StockItemMinus, StockItemPurchase


@receiver(post_save, sender=StockItemPlus)
def update_create_stock_total(sender, instance, created, *args, **kwargs):
    if created:
        exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        stock_product_item = instance.product_item
        num_plus = instance.num_plus
        total_price_usd = instance.total_price_plus_usd
        total_price_uah = instance.total_price_plus_uah
        modified_by = instance.modified_by
        new_stock_product, created_total = StockTotal.objects.get_or_create(product_item=stock_product_item)

        if created_total:
            new_stock_product.category = instance.category
            new_stock_product.num_total = num_plus
            new_stock_product.price_total_usd = total_price_usd
            new_stock_product.price_total_uah = total_price_uah
            new_stock_product.modified_by = modified_by
            new_stock_product.save(force_update=True)
            print('created total ===', created_total)
        else:
            new_stock_product.num_total += num_plus
            new_stock_product.price_total_usd += total_price_usd
            new_stock_product.price_total_uah = new_stock_product.price_total_usd * exchange_rate
            new_stock_product.modified_by = modified_by
            new_stock_product.save(force_update=True)
            print('UPDATED total ===', created_total)


@receiver(post_save, sender=StockItemPlus)
def create_stock_item_purchase(sender, instance, created, *args, **kwargs):
    if created:
        new_stock_purchase = StockItemPurchase.objects.create(id_purchase=instance.id_purchase,
                                                              category=instance.category,
                                                              product_item=instance.product_item,
                                                              num_item=instance.num_plus,
                                                              price_usd=instance.price_plus_usd,
                                                              price_uah=instance.price_plus_uah,
                                                              total_price_usd=instance.total_price_plus_usd,
                                                              total_price_uah=instance.total_price_plus_uah,
                                                              due_date=instance.due_date,
                                                              comments=instance.comments,
                                                              is_active=True,
                                                              modified_by=instance.modified_by)
        new_stock_purchase.save(force_update=True)


@receiver(post_save, sender=StockItemMinus)
def update_stock_item_purchase(sender, instance, created, *args, **kwargs):
    if created:
        exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        stock_product_item = instance.product_item
        num_minus = instance.num_minus
        modified_by = instance.modified_by
        stock_product = StockItemPurchase.objects.get(id_purchase=instance.id_purchase, product_item=stock_product_item)
        # think - How to rise the problem if no item on stock
        stock_product.num_item -= num_minus
        stock_product.price_uah = stock_product.price_usd * exchange_rate
        stock_product.total_price_usd = stock_product.price_usd * stock_product.num_item
        stock_product.total_price_uah = stock_product.price_uah * stock_product.num_item
        stock_product.modified_by = modified_by
        stock_product.save(force_update=True)


@receiver(post_save, sender=StockItemMinus)
def update_stock_total(sender, instance, created, *args, **kwargs):
    if created:
        exchange_rate = CurrencyExchange.objects.get(id=1).usd_price_uah
        stock_product_item = instance.product_item
        num_minus = instance.num_minus
        modified_by = instance.modified_by
        stock_product = StockTotal.objects.get(product_item=stock_product_item)
        stock_item_plus = StockItemPlus.objects.get(id_purchase=instance.id_purchase, product_item=stock_product_item)
        # think - How to rise the problem if no item on stock
        stock_product.num_total -= num_minus
        print(stock_item_plus.price_plus_usd, "*", stock_product.num_total)
        stock_product.price_total_usd = stock_product.price_total_usd - (stock_item_plus.price_plus_usd * num_minus)
        stock_product.price_total_uah = stock_product.price_total_usd * exchange_rate
        stock_product.modified_by = modified_by
        stock_product.save(force_update=True)


