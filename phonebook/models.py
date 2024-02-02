from django.db import models

from .bases import DateTimeBaseModel


class PhoneNumberRange(DateTimeBaseModel):
    """
    Модель для хранения информации о диапазонах номеров телефонов, унаследованная от DateTimeBaseModel.

    Атрибуты:
        region_code (str): Код региона.
        number_from (str): Начальный номер диапазона.
        number_to (str): Конечный номер диапазона.
        capacity (str): Емкость диапазона.
        operator (str): Название оператора связи.
        region (str): Название региона или регионов, к которому относится диапазон номеров.
        inn (str): ИНН оператора связи.
    """

    region_code = models.CharField(max_length=256, verbose_name='Код региона')
    number_from = models.CharField(max_length=10, verbose_name='Диапазон от')
    number_to = models.CharField(max_length=10, verbose_name='Диапазон до')
    capacity = models.CharField(verbose_name='Емкость')
    operator = models.CharField(max_length=300, verbose_name='Оператор')
    region = models.CharField(max_length=300, verbose_name='Регион')
    inn = models.CharField(max_length=15, verbose_name='ИНН')

    class Meta:
        verbose_name = 'Данные по телефонам'
        verbose_name_plural = 'Данные по телефонам'
        indexes = [
            models.Index(fields=['region_code', 'number_from', 'number_to']),
        ]

    def __str__(self):
        """ Возвращает строковое представление объекта PhoneNumberRange. """
        return f'{self.region_code} ({self.number_from} - {self.number_to}): {self.operator} - {self.region}'
