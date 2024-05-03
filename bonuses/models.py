import datetime

from django.db import models
from django.contrib.auth.models import User
from cosmetologs.models import Cosmetolog
from landing.models import Feature
from orders.models import Order, OrderPayment, StatusPayment
from shor.current_user import get_current_user
from django.db.models.signals import post_save
from django.dispatch import receiver

# def your_view(request):
    # Your logic to detect the error condition
from utils.main import datetime_string


class BonusEventStatus(models.Model):
    ref_number = models.CharField(max_length=2, blank=True, null=True, default=None, unique=True)
    name = models.CharField(max_length=8, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'BonusEventStatus'
        verbose_name_plural = 'BonusEventStatuses'


class BonusAccountType(models.Model):
    ref_number = models.CharField(max_length=2, blank=True, null=True, default=None, unique=True)
    name = models.CharField(max_length=8, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'BonusAccountType'
        verbose_name_plural = 'BonusAccountTypes'


class BalanceSumStatus(models.Model):
    ref_number = models.CharField(max_length=2, blank=True, null=True, default=None, unique=True)
    name = models.CharField(max_length=8, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'BalanceSumStatus'
        verbose_name_plural = 'BalanceSumStatuses'


class BonusEventType(models.Model):
    ref_number = models.CharField(max_length=2, blank=True, null=True, default=None, unique=True)
    name = models.CharField(max_length=16, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'BonusEventType'
        verbose_name_plural = 'BonusEventTypes'


class BonusAccount(models.Model):
    ref_number = models.CharField(max_length=2, blank=True, null=True, default=None, unique=True)
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    category = models.ForeignKey(BonusAccountType, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    uah_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    usd_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'BonusAccount'
        verbose_name_plural = 'BonusAccounts'


class BonusAccountCosmetolog(models.Model):
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    bonus_account = models.ForeignKey(BonusAccount, blank=True, null=True, default=None, on_delete=models.CASCADE)
    balance_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    balance_sum_status = models.ForeignKey(BalanceSumStatus, blank=True, null=True, default=None,
                                           on_delete=models.CASCADE)

    def __str__(self):
        # return "%s" % self.id
        return "%s, %s, %s" % (self.cosmetolog, self.bonus_account, self.balance_sum)

    def __unicode__(self):
        # return "%s" % self.id
        return "%s, %s, %s" % (self.cosmetolog, self.bonus_account, self.balance_sum)

    class Meta:
        verbose_name = 'BonusAccountCosmetolog'
        verbose_name_plural = 'BonusAccountCosmetologs'


class BonusCosmetologMonthlySum(models.Model):
    cosmetolog = models.ForeignKey(Cosmetolog, blank=True, null=True, default=None, on_delete=models.CASCADE)
    balance_monthly_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    month_start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    month_end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, default=None)
    month_year = models.CharField(max_length=16, blank=True, null=True, default=None)

    def __str__(self):
        # return "%s" % self.id
        return "%s, %s" % (self.cosmetolog, self.balance_monthly_sum)

    def __unicode__(self):
        # return "%s" % self.id
        return "%s, %s" % (self.cosmetolog, self.balance_monthly_sum)

    class Meta:
        verbose_name = 'BonusCosmetologMonthlySum'
        verbose_name_plural = 'BonusCosmetologMonthlySums'


class BonusAccountEvent(models.Model):
    bonus_cosmetolog = models.ForeignKey(BonusAccountCosmetolog, blank=True, null=True, default=None,
                                         on_delete=models.DO_NOTHING, related_name='bonus_cosmetolog_event')
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    event_type = models.ForeignKey(BonusEventType, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    event_status = models.ForeignKey(BonusEventStatus, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    order_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance_num = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.bonus_cosmetolog

    class Meta:
        verbose_name = 'BonusAccountEvent'
        verbose_name_plural = 'BonusAccountEvents'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.modified_by = user

        super(BonusAccountEvent, self).save(*args, **kwargs)


def get_create_bonus_account_cosmetolog(cosmetolog, bonus_account):
    bac = None
    month_now_s = datetime_string('m_s')
    try:
        bac = BonusAccountCosmetolog.objects.get(cosmetolog=cosmetolog, bonus_account=bonus_account,
                                                 start_date=month_now_s)
    except BonusAccountCosmetolog.MultipleObjectsReturned:
        print('BonusAccountCosmetolog has more than 1 bonus program')
    #     Think - maybe we have to return Somewhere in UI signal about it - or just Report page for Admin
    except BonusAccountCosmetolog.DoesNotExist:
        bac = BonusAccountCosmetolog(cosmetolog=cosmetolog)
        bac.bonus_account = bonus_account
        bac.balance_sum_status = BalanceSumStatus.objects.get(ref_number='11')
        bac.start_date = month_now_s
        bac.end_date = datetime_string('m_e')
        bac.save()

    return bac


def create_bonus_event(instance, bonus_account_cosmetolog):
    be = BonusAccountEvent(order=instance)
    be.bonus_cosmetolog = bonus_account_cosmetolog
    be.event_type = BonusEventType.objects.get(ref_number="11")
    be.event_status = BonusEventStatus.objects.get(ref_number='11')
    print('event_status -- ', be.event_status)
    be.order_sum = instance.total_price
    print('bonus_account_cosmetolog.bonus_account.uah_rate ---  ', bonus_account_cosmetolog.bonus_account.uah_rate)
    be.balance_num = instance.total_price * bonus_account_cosmetolog.bonus_account.uah_rate / 100
    be.comments = "нема нічого сказати - все добре"
    print('Event before save--- ', be)
    be.save()
    print('Event after save--- ', be)
    return be


def check_bonus_event_exist(instance, ba_ref_number):
    bonus_event_exist = BonusAccountEvent.objects.filter(
        order=instance, bonus_cosmetolog__bonus_account__ref_number=ba_ref_number).exists()
    return bonus_event_exist


def check_compare_payments_order(instance):
    order_payment_status = StatusPayment.objects.get(status_number=9)
    payments_received_set = OrderPayment.objects.filter(order=instance, status=order_payment_status)
    payment_total = 0
    bonus_event_needed = False
    for pr in payments_received_set:
        payment_total += pr.payment_sum
    if payment_total == instance.total_price:
        bonus_event_needed = True
    return bonus_event_needed, payment_total


def calculate_monthly_discount_awards():
    # month_prev = datetime_string('m_p')
    # month_prev = datetime.date(2023, 9, 1)    # for test purpose
    balance_sum_status = BalanceSumStatus.objects.get(ref_number='11')
    print(balance_sum_status)
    bonus_account = BonusAccount.objects.get(ref_number='29')
    bac_set = BonusAccountCosmetolog.objects.filter(bonus_account=bonus_account, balance_sum_status=balance_sum_status)
    # get all conditions for Monthly Cunulative programs
    number_list = [22, 23, 24, 25, 26, 27, 28]
    bonus_account_set = BonusAccount.objects.filter(ref_number__in=number_list)
    sorted_bonus_account_set = bonus_account_set.order_by('-usd_rate')
    print('sorted_bonus_account_set  ', sorted_bonus_account_set)
    print('bac_set  ', bac_set)
    for bac in bac_set:
        print('bac in set   ', bac)
        bac_balance_sum = bac.balance_sum
        print('bac_balance_sum', bac_balance_sum)
        for bonus_account in sorted_bonus_account_set:
            print('bonus_account in sorted_bonus_account_set  ', bonus_account)
            if bac_balance_sum >= bonus_account.usd_rate:
                # Logic - to create bonus for the current month, and deactivate Monthly Cum account
                bac_monthly_discount = get_create_bonus_account_cosmetolog(bac.cosmetolog, bonus_account)
                print('bac_monthly_discount   ', bac_monthly_discount)
                bac_monthly_discount.balance_sum = bonus_account.uah_rate
                bac.balance_sum_status = BalanceSumStatus.objects.get(ref_number='99')
                bac_monthly_discount.save()
                bac.save()
                break


def change_status():  # Think about How to change status for BAC if cosmetolog get ability to use bonus-Token
    return True


@receiver(post_save, sender=Order)  # Logic for Order is moved to final positive status, but Payment is already Done
def add_bonus_event_plus(sender, instance, created, update_fields, *args, **kwargs):
    feature_bonus = Feature.objects.get(feature_code=202)
    print('update_fields in Order ---   ', update_fields)
    if feature_bonus.is_active:
        bonus_event_needed = False
        if update_fields is not None and instance.status.status_number == 99 and (created or 'status' in update_fields):
            # Check all bonus programs
            # 1 - Check if the Bonus Event is already implemented for this ORDER - Token
            bonus_event_token_exists = check_bonus_event_exist(instance, '11')
            # 2 - Check if the Bonus Event is already implemented for this ORDER - Monthly Cumulative
            bonus_event_cum_exists = check_bonus_event_exist(instance, '22')

            if not bonus_event_token_exists or not bonus_event_cum_exists:
                # Check if payments were received for this ORDER
                bonus_event_needed, payments_total = check_compare_payments_order(instance)

            if bonus_event_needed:
                print('222 Executing the bonus balance update...')
                # Perform your bonus balance update logic here
                if not bonus_event_token_exists:
                    bonus_account = BonusAccount.objects.get(ref_number="11")
                    bac = get_create_bonus_account_cosmetolog(instance.cosmetolog, bonus_account)
                    create_bonus_event(instance, bac)

                if not bonus_event_cum_exists:
                    bonus_account = BonusAccount.objects.get(ref_number="29")
                    bac = get_create_bonus_account_cosmetolog(instance.cosmetolog, bonus_account)
                    create_bonus_event(instance, bac)

            else:
                # Display an error message to the user
                pass
    else:
        print('Bonus Program is NOT active')

# @receiver(post_save, sender=OrderPayment)
# # Logic for Payment is moved to final positive status, but Order is already Done
# def change_bonus_balance_plus(sender, instance, created, update_fields, *args, **kwargs):
#     bonus_event_needed = False
#     if instance.status.status_number == 99 and (created or 'status' in update_fields):
#         # Check if the Bonus Event is already implemented for this ORDER
#         bonus_event_exists = BonusAccountEvent.objects.filter(order=instance).exists()
#         if not bonus_event_exists:
#             # Check if payments were received for this ORDER
#             order_payment_status = StatusPayment.objects.get(status_number=9)
#             payments_received_set = OrderPayment.objects.filter(order=instance, status=order_payment_status)
#             payment_total = 0
#             bonus_event_needed = False
#             for pr in payments_received_set:
#                 payment_total += pr.payment_sum
#             if payment_total == instance.total_price:
#                 bonus_event_needed = True
#
#         if bonus_event_needed:
#             print('Executing the bonus balance update...')
#             # Perform your bonus balance update logic here
#             be = BonusAccountEvent.objects.create(order=instance)
#             bonus_account = BonusAccount.objects.get(ref_number="11")
#             be.bonus_cosmetolog = BonusAccountCosmetolog.objects.get(cosmetolog=instance.cosmetolog,
#                                                                      bonus_account=bonus_account)
#             be.event_type = BonusEventType.objects.get(ref_number="11")
#             be.order_sum = instance.total_price
#             be.balance_num = instance.total_price * 1
#             be.comments = "нема нічого сказати - все добре"
#             be.save(force_update=True)
#         else:
#             # Display an error message to the user
#             pass


@receiver(post_save, sender=BonusAccountEvent)  # Logic for update Bonus Balance based on Event
def change_bonus_balance(sender, instance, created, update_fields, *args, **kwargs):
    print('Event Bonus Instance --- ', instance)
    print('BonusAccountEvent instance.event_type.ref_number', instance.event_type.ref_number)
    print('BonusAccountEvent instance.event_status.ref_number', instance.event_status.ref_number)
    if instance.event_status.ref_number == "11":  # Check if event is Active or already Done
        if instance.event_type.ref_number in ("11", "12"):  # Check event type (plus or minus or what to do)
            print("URA PLUS")
            bac = BonusAccountCosmetolog.objects.get(id=instance.bonus_cosmetolog.id,
                                                     balance_sum_status=BalanceSumStatus.objects.get(ref_number='11'))
            print(bac.balance_sum)
            bac.balance_sum += instance.balance_num
            # bac.start_date = datetime_string('m_s')
            # # bac.end_date =
            print(bac.balance_sum)
            bac.save(force_update=True)
            instance.event_status = BonusEventStatus.objects.get(ref_number='99')
            instance.save(force_update=True)

        elif instance.event_type.ref_number in ("21", "22", "23"):
            print("MiNUS")
            bac = BonusAccountCosmetolog.objects.get(id=instance.bonus_cosmetolog.id)
            print(bac.balance_sum)
            bac.balance_sum -= instance.balance_num
            print(bac.balance_sum)
            bac.save(force_update=True)
            instance.event_status = BonusEventStatus.objects.get(ref_number='99')
            instance.save(force_update=True)

        elif instance.event_type.ref_number in ("31",):
            print("ZERO-BLOCKED")
        else:
            print('Logic for others')
    else:
        print('Provide logic for NOT Active statuses - if any')
        pass
