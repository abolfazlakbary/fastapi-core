import os
from dotenv import load_dotenv


load_dotenv()


class AppData:
    app_port = int(os.getenv("APP_PORT"))
    app_host = str(os.getenv("APP_HOST"))
    db_connection = str(os.getenv("DB_CONNECTION"))
    db_name = str(os.getenv("DB_NAME"))
    db_username = str(os.getenv("DB_USERNAME"))
    db_password = str(os.getenv("DB_PASSWORD"))
    db_host = str(os.getenv("DB_HOST"))
    db_port = str(os.getenv("DB_PORT"))
    db_pool_size = int(os.getenv("DB_POOL_SIZE"))
    db_max_overflow = int(os.getenv("DB_MAX_OVERFLOW"))
    redis_host = str(os.getenv("REDIS_HOST"))
    redis_port = int(os.getenv("REDIS_PORT"))
    redis_db_number = int(os.getenv("REDIS_DB_NUMBER"))
    secret_key = str(os.getenv("SECRET_KEY"))
    hashing_algorithm = str(os.getenv("ALGORITHM"))
    access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    celery_broker_type = str(os.getenv("CELERY_BROKER_TYPE"))


configs = AppData()