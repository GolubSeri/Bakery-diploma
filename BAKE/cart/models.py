from django.db import models


# Create your models here.
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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата и время заказа')

    def __str__(self):
        return f'Заказ №{self.pk}'


class OrderProductsCount(models.Model):
    class Meta:
        verbose_name = "Количество товара"
        verbose_name_plural = "Количество товаров"

    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name=u'Заказ')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name=u'Товар')
    count = models.PositiveIntegerField(blank=True, default=0, verbose_name=u'Количество')

    def __str__(self):
        return ''


