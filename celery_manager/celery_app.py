from celery import Celery
from core.config.data import configs


match configs.celery_broker_type:
    case "redis":
        celery_app = Celery(
            'celery_tasks',
            broker=f'redis://{configs.redis_host}:{configs.redis_port}/{configs.redis_db_number}'
        )
    case _:
        raise SystemError("This broker type is not defined")



celery_app.conf.beat_schedule = {
    'remove-data-daily': {
        'task': 'remove-data',
        'schedule': 86400.0, # Daily
        'args': ()
    },
}

celery_app.conf.broker_connection_retry_on_startup = True
celery_app.conf.timezone = 'Asia/Tehran'


from celery_manager import celery_tasks