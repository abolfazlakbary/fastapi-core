from celery import Celery
from core.config.data import configs


celery_app = Celery('tasks', broker=f'redis://{configs.redis_host}:{configs.redis_port}/{configs.redis_db_number}')

celery_app.conf.beat_schedule = {
    'remove-data-daily': {
        'task': 'tasks.remove_data',
        'schedule': 86400.0, # Every day
        'args': ()
    },
}

celery_app.conf.timezone = 'Asia/Tehran'


import tasks