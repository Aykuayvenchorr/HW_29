from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=400)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(models.Model):
    ROLES = (
        ('admin', 'Администратор'),
        ('member', 'Пользователь'),
        ('moderator', 'Модератор')
    )

    first_name = models.CharField(verbose_name='Имя', max_length=20, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=40, null=True)
    username = models.SlugField(verbose_name='Логин', max_length=40, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=40)
    role = models.CharField(choices=ROLES, default='member', max_length=20)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'