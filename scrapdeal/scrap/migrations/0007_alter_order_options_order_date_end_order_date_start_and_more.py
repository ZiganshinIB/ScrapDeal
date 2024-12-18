# Generated by Django 4.2.9 on 2024-11-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0006_alter_order_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-date_end', 'status', '-created_at', '-updated_at'), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_start',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1_new', 'Новый'), ('2_progress', 'В процессе'), ('3_completed', 'Завершен'), ('4_canceled', 'Отменен')], default='1_new', max_length=15, verbose_name='Статус'),
        ),
    ]
