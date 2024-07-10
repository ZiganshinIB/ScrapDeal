from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.shortcuts import render

from . import views
from . import forms

app_name = 'account'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             form_class=forms.UserLoginForm,
             template_name='registration/login.html',
         ),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='registration/logged_out.html'

         ),
         name='logout'),



    # Сброс пароля
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             form_class=forms.UserPasswordResetForm,
             template_name='registration/password_reset_form.html',
             email_template_name='registration/password_reset_email.html',
             success_url=reverse_lazy('storage:password_reset_done'),
             from_email=settings.EMAIL_HOST_USER,
         ),
         name='password_reset'),

    # Сброс пароля: После отправки письма
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    # Сброс пароля: Ссылка в письме
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             success_url=reverse_lazy('storage:password_reset_complete'),
         ),
         name='password_reset_confirm'),

    # Сброс пароля: ввод ногового пароля
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]