from django.apps import AppConfig
from django.db.models.signals import post_migrate


def my_callback(sender, **kwargs):
    from .supporting_funcs import create_contacts
    create_contacts()
    pass


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacts'
    verbose_name = 'Контакты'

    def ready(self):
        post_migrate.connect(my_callback, sender=self)
