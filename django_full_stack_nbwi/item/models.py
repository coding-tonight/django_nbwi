from django.db import models
from app.models import Base
# Create your models here.


# item types for filtering data in the reports
JAR = 'Jr'
CRTN = 'Ct'

ITEM_TYPES = [
    (JAR , 'Jar'),
    (CRTN , 'Crtn')
]

class Item(Base):
    item_code = models.CharField(null=True, blank=True, max_length=10)
    item_name = models.CharField(null=False, blank=False, max_length=45)
    item_qty = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    item_unit = models.CharField(null=True, blank=True, max_length=8)
    opening_stock = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=2)
    purchase_rate = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=2)
    item_type = models.CharField(max_length=25, choices=ITEM_TYPES, default=CRTN)

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'item'
