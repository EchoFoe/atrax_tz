import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atrax_tz.settings')

app = Celery('atrax_tz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

