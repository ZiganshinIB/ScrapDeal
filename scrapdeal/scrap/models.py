from django.utils import timezone
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
    STATUS = (
        ('1_new', 'Новый'),
        ('2_progress', 'В процессе'),
        ('3_completed', 'Завершен'),
        ('4_canceled', 'Отменен'),
    )
    title = models.CharField(max_length=100, verbose_name='Название заказа')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Ссылка')
    description = HTMLField(blank=True, verbose_name='Описание')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_orders',
                                 verbose_name='Заказчик',)
    executor = models.ForeignKey(Executor, null=True, blank=True, related_name='executed_orders',
                                 on_delete=models.SET_NULL, verbose_name='Исполнитель')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='factory_orders',
                                verbose_name='Завод')
    material_name = models.CharField(max_length=100, verbose_name='Название материала')
    material_category = models.ForeignKey(CategoryMaterial, on_delete=models.CASCADE,
                                          verbose_name='Категория материала')
    status = models.CharField(max_length=15, choices=STATUS, default='1_new', verbose_name='Статус')
    date_start = models.DateField(verbose_name='Дата начала', blank=True,)
    date_end = models.DateField(verbose_name='Дата окончания', blank=True,
                                default=(timezone.now() + timezone.timedelta(days=5)))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-date_end','status', '-created_at', '-updated_at', )



class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='comments')
    content = HTMLField(blank=True, verbose_name='Комментарий')
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, related_name='comments',
                               null=True, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.author.get_full_name() + ' - ' + self.order.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)

