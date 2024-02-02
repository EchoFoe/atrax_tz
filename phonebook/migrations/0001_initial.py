# Generated by Django 5.0.1 on 2024-02-01 11:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumberRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата редактирования')),
                ('region_code', models.CharField(max_length=256, verbose_name='Код региона')),
                ('number_from', models.CharField(max_length=10, verbose_name='Диапазон от')),
                ('number_to', models.CharField(max_length=10, verbose_name='Диапазон до')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='Емкость')),
                ('operator', models.CharField(max_length=100, verbose_name='Оператор')),
                ('region', models.CharField(max_length=200, verbose_name='Регион')),
                ('inn', models.CharField(max_length=15, verbose_name='ИНН')),
            ],
            options={
                'verbose_name': 'Данные по телефонам',
                'verbose_name_plural': 'Данные по телефонам',
                'indexes': [models.Index(fields=['region_code', 'number_from', 'number_to'], name='phonebook_p_region__f27ddb_idx')],
            },
        ),
    ]
