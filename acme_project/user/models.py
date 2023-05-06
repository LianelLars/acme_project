# user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
