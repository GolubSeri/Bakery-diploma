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
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
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


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    name = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Имя пользователя")
    phone = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Телефон")
    address = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Адрес")
    delivery = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Доставка")
    floor = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Этаж")
    flat = models.CharField(max_length=255, blank=True, default='', verbose_name=u"Домофон")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ №{self.pk}'


class OrderProductsCount(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    count = models.PositiveIntegerField(blank=True, default=0)
