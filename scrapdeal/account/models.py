from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, Group
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image
from .managers import ProfileManager


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
    first_name = models.CharField(
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
        blank=True,
        null=True
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


    def get_full_name(self):
        """
        Возвращает фамилии, имя и отчество с пробелом между ними
        """
        full_name = "%s %s %s" % (self.last_name, self.first_name, self.surname)
        return full_name.strip()

    def get_short_name(self):
        """Возвращает Фамилию и инициалы."""
        if self.first_name and self.last_name:
            if self.surname:
                short_name = f"{self.last_name} {self.first_name[0]}. {self.surname[0]}."
            else:
                short_name = f"{self.last_name} {self.first_name[0]}."
            return short_name
        return self.first_name

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










