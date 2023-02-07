import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hyde.settings")
app = Celery("hyde")
app.conf.update(settings.CELERY)
app.autodiscover_tasks()