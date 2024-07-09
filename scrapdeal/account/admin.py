from django.contrib import admin

from .models import Workshop, Profile, User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'
    extra = 0

    def get_queryset(self, request):
        return super().get_queryset(request).filter(user__is_active=True)


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    fields = ('number', 'name', 'head')
    inlines = [
        ProfileInline
    ]

