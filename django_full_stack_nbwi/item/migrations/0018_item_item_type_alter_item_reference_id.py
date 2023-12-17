# Generated by Django 4.2.4 on 2023-10-17 10:28
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_alter_item_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('Jr', 'Jar'), ('Ct', 'Crtn')], default='Ct', max_length=25),
        ),
        migrations.AlterField(
            model_name='item',
            name='reference_id',
            field=models.UUIDField(default=uuid.uuid4().hex),
        ),
    ]