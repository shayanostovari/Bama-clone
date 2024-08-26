from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('hamrah_mechanic')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-notifications-every-minute': {
        'task': 'your_app.tasks.send_notifications',
        'schedule': crontab(),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
