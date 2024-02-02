import os
import pandas as pd
import requests
import logging
from typing import List

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from django.conf import settings
from phonebook.models import PhoneNumberRange

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DOWNLOAD_URL = 'https://opendata.digital.gov.ru/downloads/'
CSV_FILES: List[str] = ['ABC-3xx.csv', 'ABC-4xx.csv', 'ABC-8xx.csv', 'DEF-9xx.csv']


def download_csv_file(url: str, file_path: str):
    """
    Функция для скачивания CSV файла по указанному URL.

    Аргументы:
        url (str): URL для скачивания CSV файла.
        file_path (str): Путь для сохранения CSV файла.
    """
    response = requests.get(url, verify=False)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def process_csv_file(file_path: str):
    """
    Функция для обработки CSV файла и добавления/обновления данных в базе данных.

    Аргументы:
        file_path (str): Путь к CSV файлу.
    """
    df = pd.read_csv(file_path, sep=';')
    df.columns = [column.strip() for column in df.columns]
    for _, row in df.iterrows():
        region_code = str(row['АВС/ DEF'])
        number_from = str(row['От'])
        number_to = str(row['До'])
        capacity = str(row['Емкость'])
        operator = str(row['Оператор'])
        region = str(row['Регион'])
        inn = str(row['ИНН'])
        obj, created = PhoneNumberRange.objects.update_or_create(
            region_code=region_code,
            number_from=number_from,
            number_to=number_to,
            defaults={
                'capacity': capacity,
                'operator': operator,
                'region': region,
                'inn': inn
            }
        )
        logger.info(f"{'Создан' if created else 'Обновлен'} PhoneNumberRange объект: {obj}")


def load_csv_data_to_database():
    """Функция для загрузки данных из CSV файлов в базу данных."""
    for csv_file in CSV_FILES:
        url = f'{BASE_DOWNLOAD_URL}{csv_file}'
        file_path = os.path.join(settings.BASE_DIR, 'csv_data', csv_file)
        logger.info(f'Скачивание файла: {url}')
        download_csv_file(url, file_path)
        logger.info(f'Процесс загрузки файла в БД: {file_path}')
        process_csv_file(file_path)
