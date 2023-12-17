import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def uuid_generator():
    return uuid.uuid4().hex 


class Base(models.Model):
    reference_id = models.UUIDField(max_length=32, default=uuid_generator(), unique=False)
    created_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", db_column="created_by", null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", db_column="updated_by", null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True

    """
      if uuid already exist or not then create new one
    """
    def save(self, *args, **kwargs):
        if not self.pk:
            while True:
                existing = self.__class__.objects.filter(reference_id=self.reference_id).exists()
                if not existing:
                    break
                self.reference_id = uuid.uuid4().hex
        super().save(*args, **kwargs)
