import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bootcampproject.settings')

app = Celery('bootcampproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_welcome_email': {
        'task': 'core.views.trigger_task',
        'schedule': crontab(minute='*'),
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.update(
    worker_pool='solo',
    broker_connection_retry_on_startup=True,
)


