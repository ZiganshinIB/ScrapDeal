from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, ModelMultipleChoiceField, ModelForm, Widget




class WorkerTransferWidget(Widget):
    template_name = 'widgets/worker_transfer.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.unassigned_workers = None
        self.assigned_workers = None

from .models import Profile


class ProfileCreateForm(UserCreationForm):
    # workers = ModelMultipleChoiceField(queryset=Worker.objects.all(), required=False, widget=WorkerTransferWidget)
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name')

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name')

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    form = ProfileChangeForm
    add_form = ProfileCreateForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2')}
        ),
        ('Личные данные', {
            'fields': ('first_name', 'last_name', 'surname', 'email', 'photo')}
        ),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}
        ),
        ('Личные данные', {
            'fields': ('first_name', 'last_name', 'surname', 'email', 'photo')}
        ),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
        ('Аккаунт', {
            'fields': ('date_joined', 'last_login')}
        ),
    )
