from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.conf import settings
from PIL import Image
from django.dispatch import receiver

UserModel = settings.AUTH_USER_MODEL


# Цех
class Workshop(models.Model):
    number = models.CharField(
        max_length=6,
        unique=True,
        verbose_name='Номер цеха'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название цеха'
    )
    head = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Начальник цеха',
        related_name='workshop_head'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.name}"

    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цехи'


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь',
        unique=True
    )
    photo = models.ImageField(
        upload_to='mediausers/%Y/%m/%d',
        default='static/profile_default.jpg',
        blank=True,
        verbose_name='Фото'
    )
    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Цех',
        related_name='workers'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
