import uuid
from django.db import models
from app.models import Base
from group.models import Group
from item.models import Item

# Create your models here.



class Rates(Base):
    group_id = models.ForeignKey(
        Group, related_name="+", on_delete=models.CASCADE, db_column="group_id")
    item_id = models.ForeignKey(
        Item, related_name="+", on_delete=models.CASCADE, db_column="item_id")
    sale_rate = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)
    vehicle_rent = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)
    product_charge = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)
    wrapping = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)
    label_charge = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=3)

    class Meta:
        db_table = 'rates'
