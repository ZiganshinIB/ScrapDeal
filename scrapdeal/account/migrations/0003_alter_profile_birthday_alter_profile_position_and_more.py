# Generated by Django 4.2.9 on 2024-08-24 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_email_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers', to='account.position', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Рабочий телефон'),
        ),
    ]
