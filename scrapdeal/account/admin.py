from django.contrib import admin
from django.forms import forms, ModelMultipleChoiceField, ModelForm, Widget
from django.utils.html import format_html
from django.urls import reverse
from .models import Workshop, Profile, Position





class WorkshopAdminForm(ModelForm):

    class Meta:
        model = Workshop
        fields = ('number', 'name', 'head')


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    form = WorkshopAdminForm



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'last_name', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
