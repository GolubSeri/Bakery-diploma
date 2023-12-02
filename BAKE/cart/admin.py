from django.contrib import admin

from cart.models import OrderProductsCount, Order


# Register your models here.
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