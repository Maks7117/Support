import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoInnowise.settings')


app = Celery('djangoInnowise')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-spam-every-1-minute': {
        'task': 'support.tasks.support_answer',
        'schedule': crontab(minute='*/20'),
    },
}

