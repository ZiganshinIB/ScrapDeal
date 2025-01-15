from django import forms
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from .models import Order, Factory


class OrderForm(forms.ModelForm):
    factory = forms.ModelChoiceField(queryset=Factory.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ['title', 'description', 'factory', 'material_name', 'material_category', 'date_start', 'date_end']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30, 'class': 'form-control'}),
            'factory': forms.Select(attrs={'class': 'form-control'}),
            'material_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите материал'}),
            'material_category': forms.Select(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Получаем пользователя из аргументов
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['factory'].queryset = Factory.objects.filter(customers=user.customer)