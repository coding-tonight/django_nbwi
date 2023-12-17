from django.db import models
from app.models import Base
from factory.models import Factory
from account.models import Account
from group.models import Group
from item.models import Item

# Create your models here.


class Transaction(Base):
    ref_no = models.CharField(null=False, blank=False , max_length=8)
    date = models.DateField(null=True, blank=True)  
    factory_id = models.ForeignKey(
        Factory, related_name='+', on_delete=models.PROTECT, db_column="factory_id")
    account_id = models.ForeignKey(
        Account, related_name='+', on_delete=models.PROTECT, db_column="account_id")
    total_amount = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=3)
    amount_received = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=3)
    total_vehicle_rent = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=3)
    total_product_charge = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=3)
    total_wrapping = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=3)
    total_label_charge = models.DecimalField(max_digits=10, null=True, decimal_places=3)

    def __str__(self):
        return self.ref_no

    class Meta:
        db_table = "transactions"


class TransactionDetail(Base):
    transaction = models.ForeignKey(
        Transaction, related_name="+", on_delete=models.PROTECT)
    item_id = models.ForeignKey(
        Item, related_name="+", on_delete=models.PROTECT, db_column="item_id")
    group_id = models.ForeignKey(
        Group, related_name="+", on_delete=models.PROTECT, db_column="group_id")
    item_qty = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=3)
    item_rate = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=3)
    vehicle_rent = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=3)
    product_charge = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=3)
    wrapping = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=3)
    label_charge = models.DecimalField(
    null=True, max_digits=7, decimal_places=3)

    class Meta:
        db_table = 'transactiondetail'
