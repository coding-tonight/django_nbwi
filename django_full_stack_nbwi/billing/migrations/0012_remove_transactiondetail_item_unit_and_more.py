# Generated by Django 4.2.4 on 2023-10-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0011_alter_transaction_reference_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactiondetail',
            name='item_unit',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reference_id',
            field=models.CharField(default='d0b2cf2fce5a413ab912026ae4bae467', max_length=32),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='reference_id',
            field=models.CharField(default='d0b2cf2fce5a413ab912026ae4bae467', max_length=32),
        ),
    ]