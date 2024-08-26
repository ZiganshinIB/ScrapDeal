# from django.db import models
# from django.conf import settings
# # signals
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
#
# UserModel = settings.AUTH_USER_MODEL
#
#
# class MaterialType(models.Model):
#     title = models.CharField(max_length=100, verbose_name='Тип материала')
#     category = models.CharField(max_length=100, blank=True, null=True, verbose_name='Категория')
#
#     def __str__(self):
#         return f"{self.title} ({self.category})"
#
#     class Meta:
#         verbose_name = 'Тип материала'
#         verbose_name_plural = 'Типы материалов'
#
#
# class Material(models.Model):
#     code = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Код материала')
#     title = models.CharField(max_length=100, verbose_name='Название')
#     unit = models.CharField(max_length=100, verbose_name='Единица измерения')
#     material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, verbose_name='Тип материала')
#
#     def __str__(self):
#         return f"{self.title} ({self.code})"
#
#     class Meta:
#         verbose_name = 'Материал'
#         verbose_name_plural = 'Материалы'
#
#
# class Order(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
#     created_by = models.ForeignKey(UserModel,
#                                    on_delete=models.SET_NULL,
#                                    null=True,
#                                    related_name='order_created_by',
#                                    verbose_name='Создал')
#     updated_by = models.ForeignKey(UserModel,
#                                    on_delete=models.SET_NULL,
#                                    null=True,
#                                    related_name='order_updated_by',
#                                    verbose_name='Обновил')
#     responsible = models.ForeignKey(UserModel,
#                                     on_delete=models.SET_NULL,
#                                     null=True,
#                                     related_name='order_responsible',
#                                     verbose_name='Ответственный')
#     # date = models.DateField(null=True, blank=True, verbose_name='Дата выгрузки')
#
#     def __str__(self):
#         return f"Заказ {self.pk}"
#
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#
# class OrderItem(models.Model):
#     position = models.PositiveIntegerField(verbose_name='Позиция', default=1)
#     material = models.ForeignKey(Material,
#                                  on_delete=models.CASCADE,
#                                  related_name='orders',
#                                  verbose_name='Материал')
#     order = models.ForeignKey(Order,
#                               on_delete=models.CASCADE,
#                               verbose_name='Заказ',
#                               related_name='items')
#     quantity = models.FloatField(default=1, verbose_name='Количество')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
#
#     def __str__(self):
#         return f"{self.material} ({self.quantity})"
#
#     class Meta:
#         verbose_name = 'Позиция заказа'
#         verbose_name_plural = 'Позиции заказа'
#
#
# # pre_save OrderItem
# @receiver(pre_save, sender=OrderItem)
# def update_order_item(sender, instance, **kwargs):
#     if instance.quantity == 0:
#         instance.delete()
#     elif instance.quantity < 0:
#         raise ValueError("Количество должно быть больше нуля")
#     else:
#         instance.order.updated_at = models.DateTimeField(auto_now=True)
#         instance.order.save()
#         instance.save()
