from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import *


class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient)
admin.site.register(Product, ProductAdmin)
