from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from .models import Factory, CategoryMaterial, Customer, Executor, Order


class MaterialInline(StackedInline):
    model = Executor.executmaterials.through
    extra = 0

@admin.register(CategoryMaterial)
class CategoryMaterialAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('user',)
    list_display = ('user',)
    list_filter = ('user',)
    search_fields = ('user',)


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    fields = ('user',)
    list_display = ('user',)
    list_filter = ('user',)
    search_fields = ('user',)
    inlines = [MaterialInline]


class CustomerInline(TabularInline):
    model = Factory.customers.through
    extra = 0


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug')
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    inlines = [CustomerInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer')
    list_filter = ('status','customer', 'executor')
    search_fields = ('title', 'customer', 'executor')
    sortable_by = ('updated_at', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

# class OrderItemInline(TabularInline):
#     model = OrderItem
#     fields = ('material', 'quantity')
#     extra = 0
#
#
# @admin.register(MaterialType)
# class MaterialTypeAdmin(admin.ModelAdmin):
#     fields = ('title', 'category')
#     list_display = ('title', 'category')
#     list_filter = ('title', 'category')
#     search_fields = ('title', 'category')
#
#
# @admin.register(Material)
# class MaterialAdmin(admin.ModelAdmin):
#     fields = ('code', 'title', 'unit', 'material_type')
#     list_display = ('code', 'title', 'unit', 'material_type')
#     list_filter = ('code', 'title', 'unit', 'material_type')
#     search_fields = ('code', 'title', 'unit', 'material_type')
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
#     list_display = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
#     list_filter = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
#     search_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'responsible')
#     readonly_fields = ('created_at', 'updated_at',)
#
#     inlines = [
#         OrderItemInline
#     ]
#
# # Register your models here.
#
#
