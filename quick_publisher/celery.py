import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quick_publisher.settings')

celery_app = Celery('quick_publisher')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'publisher.tasks.send_view_count_report',
        'schedule': crontab(),
    }
}
