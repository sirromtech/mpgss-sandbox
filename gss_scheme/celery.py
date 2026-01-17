import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gss_scheme.settings')

app = Celery('gss_scheme')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
