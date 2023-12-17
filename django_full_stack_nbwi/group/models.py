from django.db import models
from app.models import Base

# Create your models here.


class Group(Base):
    group_name = models.CharField(null=False, blank=False, max_length=45)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'salegroup'
