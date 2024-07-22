from app.fastapi_app import app
from core.database.connection import init_database
from database import models
from core.redis.connection import redis_connection
from fastapi import Request
from fastapi.responses import JSONResponse
from core.exceptions.base import CustomException
from core.schema.validate import transform_pydantic_errors
from fastapi.exceptions import RequestValidationError




@app.exception_handler(CustomException)
async def my_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code, 
        content={
            "message": exc.message,
            "code": exc.status_code,
            "errors": exc.errors
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    transformed_errors = transform_pydantic_errors(exc.errors())
    return JSONResponse(
        status_code=400,
        content=transformed_errors,
    )




async def run_server():
    await init_database()
    await redis_connection()