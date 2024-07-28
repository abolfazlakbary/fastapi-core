FastAPI boiler plate

Including :

1 - FastAPI for producing rest APIs

2 - SQLALchemy for interacting with databases (Support for sqlite, mysql and postgresql)

3 - Pydantic for data validation

4 - Redis for data cache and as celery broker

5 - Celery for doing repeating tasks

6 - Docker for containerizing the project

7 - Complete structure capable of developing

8 - Simple error responses (Like laravel)

9 - async structure in order to have better performance

10 - Simple authentication based on JWT and capable of modification



How to run celery:

1: celery -A celery_manager.celery_app worker --loglevel=info
2: celery -A celery_manager.celery_app beat --loglevel=info
