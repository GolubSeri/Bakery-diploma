from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contacts(models.Model):
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    phone_number = PhoneNumberField(default='+79999999999', verbose_name=u"Номер телефона")
    vk_link = models.URLField(max_length=255, default='https://vk.com/', blank=True, verbose_name=u"Ссылка на VK")
    tg_link = models.URLField(max_length=255, default='https://web.telegram.org/', blank=True, verbose_name=u"Ссылка на Telegram")

    def __str__(self):
        return "Контакты"


