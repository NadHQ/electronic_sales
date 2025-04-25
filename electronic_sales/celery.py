import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electronic_sales.settings")

app = Celery("electronic_sales")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
