celery -A celery_manager.celery_app worker --loglevel=ERROR &
celery -A celery_manager.celery_app beat --loglevel=ERROR