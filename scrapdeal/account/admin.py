from django.contrib import admin
from django.forms import forms, ModelMultipleChoiceField, ModelForm, Widget
from django.utils.html import format_html
from django.urls import reverse
from .models import Workshop, Profile, Position


class WorkerTransferWidget(Widget):
    template_name = 'widgets/worker_transfer.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.unassigned_workers = None
        self.assigned_workers = None

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context.update({
            'unassigned_workers': self.unassigned_workers,
            'assigned_workers': self.assigned_workers,
            'name': name,
        })
        return context

    def value_from_datadict(self, data, files, name):
        unassigned_workers = data.getlist(f"{name}-unassigned")
        assigned_workers = data.getlist(f"{name}-assigned")
        return {
            'unassigned_workers': [int(id) for id in unassigned_workers],
            'assigned_workers': [int(id) for id in assigned_workers]
        }

class WorkshopAdminForm(ModelForm):
    workers = ModelMultipleChoiceField(
        queryset=Profile.objects.all(),
        required=False,
        widget=WorkerTransferWidget
    )

    class Meta:
        model = Workshop
        fields = ('number', 'name', 'head', 'workers')

    def save(self, commit=True):
        workshop = super().save(commit=False)
        workshop.save()

        workers_data = self.cleaned_data['workers']
        unassigned_workers = Profile.objects.filter(id__in=workers_data['unassigned_workers'])
        assigned_workers = Profile.objects.filter(id__in=workers_data['assigned_workers'])

        workshop.workers.set(assigned_workers)
        for worker in unassigned_workers:
            worker.workshop = workshop
            worker.save()

        return workshop

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    form = WorkshopAdminForm

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('workers')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'last_name', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
