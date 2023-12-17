from django.db import models
from app.models import Base

# Create your models here.


class Account(Base):
    account_name = models.CharField(null=False, blank=False, max_length=45)
    account_number = models.CharField(null=False, blank=False, max_length=15)
    opening_balance = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=3)

    def __str__(self):
        return self.account_name

    class Meta:
        db_table = 'account'
