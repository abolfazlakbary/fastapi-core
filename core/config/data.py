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


configs = AppData()