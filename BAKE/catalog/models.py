from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название")
    price = models.PositiveIntegerField(blank=True, default=0)
    description = models.TextField(blank=True, default='')


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название")

    def __str__(self):
        return self.name
