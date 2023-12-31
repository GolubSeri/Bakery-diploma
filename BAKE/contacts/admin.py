from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Contacts, ContactsAdmin)
