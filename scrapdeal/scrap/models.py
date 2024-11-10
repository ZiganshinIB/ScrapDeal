from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField


UserModel = get_user_model()

class CategoryMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория материала'
        verbose_name_plural = 'Категории материалов'


class Customer(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Executor(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name='Пользователь')
    executmaterials = models.ManyToManyField(CategoryMaterial, blank=True,
                                             verbose_name='Категории материала',
                                             related_name='executors')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Factory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название завода')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Ссылка')
    customers = models.ManyToManyField(Customer,
                                       blank=True,
                                       verbose_name='Исполнители',
                                       related_name='factories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Order(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название заказа')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Ссылка')
    description = HTMLField(blank=True, verbose_name='Описание')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик')
    executor = models.ForeignKey(Executor, null=True, blank=True,
                                 on_delete=models.CASCADE, verbose_name='Исполнитель')
    material_name = models.CharField(max_length=100, verbose_name='Название материала')
    material_category = models.ForeignKey(CategoryMaterial, on_delete=models.CASCADE,
                                          verbose_name='Категория материала')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



