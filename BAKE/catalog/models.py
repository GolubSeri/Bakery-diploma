from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['my_order']

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название")
    price = models.PositiveIntegerField(blank=True, default=0, verbose_name=u"Цена")
    description = models.TextField(blank=True, default='', verbose_name=u"Описание")
    photo = models.ImageField(upload_to="products", verbose_name=u"Фото")
    weight = models.PositiveIntegerField(blank=True, default=0, verbose_name=u"Вес (г)")
    calories = models.PositiveIntegerField(blank=True, default=0, verbose_name=u"Энергетическая ценность (ккал)")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name=u"Категория")
    ingredients = models.ManyToManyField('Ingredient', verbose_name=u"Состав")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировка")

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
        ordering = ['my_order']

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Название", db_index=True)
    image = models.ImageField(upload_to="categories", verbose_name=u"Изображение")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировка")

    def __str__(self):
        return self.name
