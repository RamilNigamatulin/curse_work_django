from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование категории',
        help_text='Введите наименование категории товара'
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание продукта',
        help_text='Введите описание продукта'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Наименование продукта',
        help_text='Введите наименование продукта'
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание продукта',
        help_text='Введите описание продукта'
    )
    image = models.ImageField(
        upload_to='photo/product',
        blank=True,
        null=True,
        verbose_name='Фото продукта',
        help_text='Загрузите фото'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Введите категорию товара'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена за покупку',
        help_text='Введите цену продукта'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания(записи в БД)',
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего изменения(записи в БД)',
        default=timezone.now,
    )
    manufactured_at = models.DateTimeField(
        verbose_name='Дата произодства',
        help_text='Введите дату производства продукта',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='versions',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Продукт',
    )
    version_number = models.PositiveIntegerField(
        verbose_name='Номер версии',
        help_text='Введите номер версии продукта',
    )
    version_name = models.CharField(
        verbose_name='Имя версии',
        max_length=200,
        help_text='Введите имя версии продукта',
    )
    current_sign = models.BooleanField(
        default=False,
        verbose_name='Признак текущей версии',
    )

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return self.version_name

