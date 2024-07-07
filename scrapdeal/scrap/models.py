from django.db import models
from django.conf import settings
# signals
from django.db.models.signals import pre_save
from django.dispatch import receiver

UserModel = settings.AUTH_USER_MODEL


class MaterialType(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.category})"


class Material(models.Model):
    code = models.CharField(max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.code})"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='order_created_by')
    updated_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='order_updated_by')
    responsible = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='order_responsible')

    def __str__(self):
        return f"Заказ {self.pk}"


class OrderItem(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# pre_save OrderItem
@receiver(pre_save, sender=OrderItem)
def update_order_item(sender, instance, **kwargs):
    if instance.quantity == 0:
        instance.delete()
    elif instance.quantity < 0:
        raise ValueError("Количество должно быть больше нуля")
    else:
        instance.order.updated_at = models.DateTimeField(auto_now=True)
        instance.order.save()
        instance.save()


