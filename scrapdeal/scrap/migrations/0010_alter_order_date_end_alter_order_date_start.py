# Generated by Django 4.2.9 on 2024-11-10 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0009_alter_order_date_end_alter_order_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_end',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 11, 15, 10, 16, 33, 812237, tzinfo=datetime.timezone.utc), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_start',
            field=models.DateField(blank=True, verbose_name='Дата начала'),
        ),
    ]
