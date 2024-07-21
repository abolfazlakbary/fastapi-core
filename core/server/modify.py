from app.fastapi_app import app
from core.database.connection import init_database
from database import models
from core.redis.connection import redis_connection
from fastapi import Request, status
from fastapi.responses import JSONResponse
from core.exceptions.base import CustomException



@app.exception_handler(CustomException)
async def my_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, 
        content={
            "message": exc.message,
            "code": exc.status_code,
            "errors": exc.errors
        }
    )




async def run_server():
    await init_database()
    await redis_connection()