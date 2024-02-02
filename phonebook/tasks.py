from celery import shared_task
from phonebook.utils import load_csv_data_to_database


@shared_task
def process_csv_data():
    load_csv_data_to_database()
