# Generated by Django 4.2.9 on 2024-11-10 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_birthday_alter_profile_position_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='head',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='work_phone',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='Workshop',
        ),
    ]
