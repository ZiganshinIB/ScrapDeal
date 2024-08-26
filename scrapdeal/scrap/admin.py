from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Material, MaterialType, Order, OrderItem


class OrderItemInline(TabularInline):
    model = OrderItem
    fields = ('material', 'quantity')
    extra = 0


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    fields = ('title', 'category')
    list_display = ('title', 'category')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    fields = ('code', 'title', 'unit', 'material_type')
    list_display = ('code', 'title', 'unit', 'material_type')
    list_filter = ('code', 'title', 'unit', 'material_type')
    search_fields = ('code', 'title', 'unit', 'material_type')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
    list_display = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
    list_filter = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
    search_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
    readonly_fields = ('created_at', 'updated_at',)

    inlines = [
        OrderItemInline
    ]

# Register your models here.


