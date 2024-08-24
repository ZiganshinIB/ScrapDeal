from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, Group
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.conf import settings
from PIL import Image
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

from .managers import ProfileManager

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

class Position(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Цех',
        related_name='positions'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

# Customer User
class Profile(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
        blank=True,
    )
    surname = models.CharField(
        max_length=100,
        verbose_name='Отчество',
        blank=True,
    )
    email = models.EmailField(
        _("email address"),
        blank=True
    )
    phone = PhoneNumberField(
        verbose_name='Телефон',
        blank=True
    )
    work_phone = models.CharField(
        verbose_name='Рабочий телефон',
        max_length=12,
        blank=True
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        blank=True
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Должность',
        related_name='workers'
    )
    photo = models.ImageField(
        upload_to='media/%Y/%m/%d',
        default='static/profile_default.jpg',
        blank=True,
        verbose_name='Фото'
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = ProfileManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        if self.email and self.objects.filter(email=self.email).exists():
            raise ValidationError("Пользователь с такой почтой уже существует")
        if self.phone and self.objects.filter(phone=self.phone).exists():
            raise ValidationError("Пользователь с таким телефоном уже существует")
        if self.work_phone and self.objects.filter(work_phone=self.work_phone).exists():
            raise ValidationError("Пользователь с таким рабочим телефоном уже существует")

    def get_full_name(self):
        """
        Возвращает фамилии, имя и отчество с пробелом между ними
        """
        full_name = "%s %s %s" % (self.last_name, self.name, self.surname)
        return full_name.strip()

    def get_short_name(self):
        """Возвращает Фамилию и инициалы."""
        if self.name and self.last_name:
            if self.surname:
                short_name = f"{self.last_name} {self.name[0]}. {self.surname[0]}."
            else:
                short_name = f"{self.last_name} {self.name[0]}."
            return short_name
        return self.name

    def has_group(self, group_name):
        """Возвращает True, если пользователь состоит в указанной группе."""
        if self.is_superuser:
            return True
        try:
            groups = self.groups.filter(name=group_name)
            return True
        except Group.DoesNotExist:
            return False

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Отправляет электронное письмо этому пользователю."""
        send_mail(subject, message, from_email, [self.email], **kwargs)










