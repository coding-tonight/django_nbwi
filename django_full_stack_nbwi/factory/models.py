from django.db import models
from app.models import Base

# Create your models here.


class FactoryOwner(Base):
    owner_name = models.CharField(null=False, blank=False, max_length=45)
    address = models.CharField(null=False, blank=False, max_length=60)
    phone_number = models.CharField(null=False, blank=False, max_length=15)
    opening_balance = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=3)

    class Meta:
        db_table = 'factoryOwner'

    def __str__(self):
        return self.owner_name


class Factory(Base):
    factory_name = models.CharField(null=False, blank=False, max_length=45)
    factory_address = models.CharField(null=False, blank=False, max_length=45)
    phone_number = models.CharField(null=False, blank=False, max_length=15)
    owner_id = models.OneToOneField(
        FactoryOwner, related_name="+", on_delete=models.PROTECT, db_column="owner_id", null=True)

    class Meta:
        db_table = 'factory'

    def __str__(self):
        return self.factory_name
