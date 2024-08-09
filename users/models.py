from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )

    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo/avatars/',
        verbose_name='Аватар',
    )
    phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Введите номер телефона',
    )
    country = models.CharField(
        max_length=150,
        verbose_name='Страна',
        help_text='Введите название страны',
    )
    token = models.CharField(
        max_length=100,
        verbose_name='Токен',
        blank=True,
        null=True,
        help_text='Токен для авторизации',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email







