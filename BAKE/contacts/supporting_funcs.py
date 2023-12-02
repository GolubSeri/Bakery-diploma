from .models import Contacts

def create_contacts():
    models_to_check = [Contacts]

    for model in models_to_check:
        if len(model.objects.all()) == 0:
            model.objects.create()