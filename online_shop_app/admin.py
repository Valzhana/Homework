from django.contrib import admin

# Register your models here.

from .models import Product, Order, User


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """список продуктов"""
    list_display = ['name', 'quantity', 'price']
    ordering = ['name', '-quantity']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    fields = ['name', 'description', 'quantity', 'price']
    readonly_fields = ['name']


class UserAdmin(admin.ModelAdmin):
    """список продуктов"""
    list_display = ['name', 'email', 'phone', 'address', 'date_registered']
    ordering = ['name', 'phone']
    list_filter = ['name']
    search_fields = ['name', 'email', 'phone']
    search_help_text = 'Поиск по полю name (description)'

    """Клиент."""
    fields = ['name', 'email', 'phone', 'address', 'date_registered']
    readonly_fields = ['name', 'date_registered']


class OrderAdmin(admin.ModelAdmin):
    """список продуктов"""

    def _products(self, row):
        return ','.join([x.name for x in row.products.all()])

    def _customer(self, row):
        return row.customer.name

    list_display = ['_customer', '_products', 'total_price', 'date_ordered']
    ordering = ['customer', 'total_price', 'date_ordered']
    list_filter = ['total_price']
    search_fields = ['customer', 'date_ordered']

    fields = ['customer', 'products', 'total_price', 'date_ordered']
    readonly_fields = ['date_ordered']


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
