# Generated by Django 4.2.4 on 2023-10-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0016_alter_transaction_reference_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference_id',
            field=models.UUIDField(default='32fbf0eebb614ee295ff79561748d61a'),
        ),
        migrations.AlterField(
            model_name='transactiondetail',
            name='reference_id',
            field=models.UUIDField(default='32fbf0eebb614ee295ff79561748d61a'),
        ),
    ]
