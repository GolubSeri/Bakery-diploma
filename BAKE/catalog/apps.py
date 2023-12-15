from django.apps import AppConfig
from django.db.models.signals import post_migrate


def my_callback(sender, **kwargs):
    from .creation import initialize
    initialize()
    pass
        

class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    verbose_name = "Меню"

    def ready(self):
        post_migrate.connect(my_callback, sender=self)
