from django import forms
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext_lazy
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.core.exceptions import ValidationError

from .models import Profile

UserModel = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Логин',
            'name': 'username'
        })
    )
    password = forms.CharField(
        required=True,
        label=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Пароль',
            'name': 'password'
        })
    )

    error_messages = {
        "invalid_login": gettext_lazy(
            "Пожалуйста, введите правильный  %(username)s и пароль. Обратите внимание, что оба"
            "поля могут быть чувствительны к регистру."
        ),
        "inactive": gettext_lazy("Этот аккаунт заблокирован."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields["username"].max_length = username_max_length
        self.fields["username"].widget.attrs["maxlength"] = username_max_length

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": "username"},
        )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control  mb-3',
                'placeholder': 'E-mail',
                'name': 'EMAIL'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        # Если пользователь с такой почтой не существует
        if not UserModel.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError('Пользователь с такой почтой не существует')
        return email


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Имя',
                'name': 'first_name'
            }
        ),
        error_messages={'required': 'Пожалуйста, введите ваше имя.'}
    )
    last_name = forms.CharField(
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Фамилия',
                'name': 'last_name'
            }
        ),
        error_messages={'required': 'Пожалуйста, введите вашу фамилию.'}
    )
    email = forms.EmailField(
        required=True,
        label=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'E-mail',
                'name': 'email'
            }
        ),
        error_messages={'required': 'Пожалуйста, введите вашу почту.'}
    )

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'photo',
        ]
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Фото',
                    'name': 'photo'
                }
            ),
        }
        labels = {
            'photo': '',
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if UserModel.objects.filter(email=data).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже существует')
        return data

