from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bama_clone.settings')

app = Celery('bama_clone')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['notification'])

app.conf.beat_schedule = {
    'send-notification-every-minute': {
        'task': 'notification.tasks.send_notifications',
        'schedule': crontab(minute='*')
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
