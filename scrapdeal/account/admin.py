from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import forms, ModelMultipleChoiceField, ModelForm, Widget
from django.utils.html import format_html

from .models import Profile



# class WorkerTransferWidget(Widget):
#     template_name = 'widgets/worker_transfer.html'
#
#     def __init__(self, attrs=None):
#         super().__init__(attrs)
#         self.unassigned_workers = None
#         self.assigned_workers = None
#
#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         context.update({
#             'unassigned_workers': self.unassigned_workers,
#             'assigned_workers': self.assigned_workers,
#             'name': name,
#         })
#         return context
#
#     def value_from_datadict(self, data, files, name):
#         unassigned_workers = data.getlist(f"{name}-unassigned")
#         assigned_workers = data.getlist(f"{name}-assigned")
#         return {
#             'unassigned_workers': [int(id) for id in unassigned_workers],
#             'assigned_workers': [int(id) for id in assigned_workers]
#         }

class ProfileForm(ModelForm):
    # workers = ModelMultipleChoiceField(queryset=Worker.objects.all(), required=False, widget=WorkerTransferWidget)
    class Meta:
        model = Profile
        fields = '__all__'

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    form = ProfileForm
    add_form = ProfileForm
    add_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'surname', 'email', 'photo')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Аккаунт', {'fields': ('date_joined', 'last_login')}),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'surname', 'email', 'photo')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Аккаунт', {'fields': ('date_joined', 'last_login')}),
    )

