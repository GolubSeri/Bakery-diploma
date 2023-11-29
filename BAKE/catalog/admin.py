from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Product)


class OrderCountAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


admin.site.register(OrderProductsCount, OrderCountAdmin)


class OrderCountInline(admin.TabularInline):
    model = OrderProductsCount
    extra = 1

    verbose_name = "Товары"
    verbose_name_plural = "Товары"


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderCountInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Order, OrderAdmin)
