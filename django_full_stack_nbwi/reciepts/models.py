from django.db import models

from app.models import Base
from factory.models import FactoryOwner
from account.models import Account

# Create your models here.


class Receipts(Base):
    date = models.DateField()
    owner = models.ForeignKey(FactoryOwner , related_name="+" , on_delete=models.PROTECT)
    mode_of_payment = models.ForeignKey(Account , related_name="+" , on_delete=models.PROTECT , db_column="mode_of_payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.mode_of_payment)

    class Meta:
        db_table = 'receipts'
