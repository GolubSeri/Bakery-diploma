from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название")
    price = models.PositiveIntegerField(blank=True, default=0)
    description = models.TextField(blank=True, default='')
    photo = models.ImageField(upload_to="products")
    weight = models.PositiveIntegerField(blank=True, default=0)
    calories = models.PositiveIntegerField(blank=True, default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, )
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название")

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название", db_index=True)
    image = models.ImageField(upload_to="categories")

    def __str__(self):
        return self.name
