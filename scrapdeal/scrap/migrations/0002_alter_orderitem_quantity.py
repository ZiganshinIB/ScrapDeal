# Generated by Django 4.2.9 on 2024-07-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.FloatField(default=1),
        ),
    ]
