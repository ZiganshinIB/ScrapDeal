# Generated by Django 4.2.9 on 2024-11-10 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0007_alter_order_options_order_date_end_order_date_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_end',
            field=models.DateField(blank=True, default=datetime.date(2024, 11, 15), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_start',
            field=models.DateField(blank=True, default=datetime.date(2024, 11, 10), verbose_name='Дата начала'),
        ),
    ]
