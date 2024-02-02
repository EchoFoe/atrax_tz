from django.core.management.base import BaseCommand

from phonebook.utils import load_csv_data_to_database


class LoadPhoneNumberDataAction(BaseCommand):
    help = 'Скачивает и загружает данные из CSV файлов в базу данных'

    def handle(self, *args, **options):
        load_csv_data_to_database()
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены в базу данных'))
