# Generated by Django 4.1.6 on 2023-02-19 08:54

import django.core.validators
from django.db import (
    migrations,
    models
)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='NetworkObject',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'title',
                    models.CharField(
                        max_length=200, unique=True, verbose_name='Название'
                    ),
                ),
                (
                    'link_level',
                    models.PositiveSmallIntegerField(
                        choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'ИП')],
                        default=0,
                        verbose_name='Уровень',
                    ),
                ),
                (
                    'status',
                    models.PositiveSmallIntegerField(
                        choices=[(1, 'Продавец'), (2, 'Покупатель')],
                        default=1,
                        verbose_name='Статус',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        max_length=150, unique=True, verbose_name='Email'
                    ),
                ),
                (
                    'country',
                    models.CharField(blank=True, max_length=150, verbose_name='Страна'),
                ),
                (
                    'city',
                    models.CharField(blank=True, max_length=100, verbose_name='Город'),
                ),
                (
                    'street',
                    models.CharField(blank=True, max_length=150, verbose_name='Улица'),
                ),
                (
                    'number_home',
                    models.CharField(
                        blank=True, max_length=15, verbose_name='Номер дома'
                    ),
                ),
                (
                    'created',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата создания'
                    ),
                ),
                (
                    'debt',
                    models.FloatField(
                        default=0.0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name='Задолженность',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Объект торговой сети',
                'verbose_name_plural': 'Объекты торговой сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                (
                    'release_date',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата выхода продукта на рынок'
                    ),
                ),
                (
                    'providers',
                    models.ManyToManyField(
                        blank=True,
                        to='network_obj.networkobject',
                        verbose_name='Продавец/Покупатель',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='networkobject',
            name='products',
            field=models.ManyToManyField(
                blank=True, to='network_obj.product', verbose_name='Товары'
            ),
        ),
    ]
