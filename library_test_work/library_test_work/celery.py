import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_test_work.settings')

app = Celery('library_test_work')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
