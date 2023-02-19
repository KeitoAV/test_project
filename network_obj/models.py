from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from user.models import User


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200, unique=False)
    model = models.CharField(verbose_name='Модель', max_length=200)
    providers = models.ManyToManyField('NetworkObject', verbose_name='Продавец/Покупатель', blank=True)
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода продукта на рынок')

    def save(self, *args, **kwargs):
        if not self.id:
            self.release_date = timezone.now()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class NetworkObject(models.Model):
    class LinkLevel(models.IntegerChoices):
        factory = 0, 'Завод'
        retail_network = 1, 'Розничная сеть'
        individual_entrepreneur = 2, 'ИП'

    class Status(models.IntegerChoices):
        salesman = 1, 'Продавец'
        buyer = 2, 'Покупатель'

    title = models.CharField(verbose_name='Название', max_length=200, unique=True)
    link_level = models.PositiveSmallIntegerField(
        verbose_name='Уровень', choices=LinkLevel.choices, default=LinkLevel.factory
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус', choices=Status.choices, default=Status.salesman
    )
    email = models.EmailField(verbose_name='Email', max_length=150, unique=True)
    country = models.CharField(verbose_name='Страна', max_length=150, blank=True)
    city = models.CharField(verbose_name='Город', max_length=100, blank=True)
    street = models.CharField(verbose_name='Улица', max_length=150, blank=True)
    number_home = models.CharField(verbose_name='Номер дома', max_length=15, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    products = models.ManyToManyField('Product', verbose_name='Товары', blank=True)
    debt = models.FloatField(verbose_name="Задолженность", default=0.0,
                             validators=([MinValueValidator(0)]))

    user = models.ForeignKey(User, verbose_name="Сотрудник", related_name='user',
                             on_delete=models.CASCADE, null=True,
                             blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Объект торговой сети'
        verbose_name_plural = 'Объекты торговой сети'

    def __str__(self):
        return self.title
