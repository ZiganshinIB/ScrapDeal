# Generated by Django 4.2.9 on 2024-08-26 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_responsible', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Обновил'),
        ),
    ]
