# Generated by Django 4.2.7 on 2023-12-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_image_alter_product_calories_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['my_order'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['my_order'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='category',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='product',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]
