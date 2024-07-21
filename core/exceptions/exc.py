from core.exceptions.base import CustomException
from fastapi import status



class NotFoundException(CustomException):
    message = "Item not found"
    status_code = status.HTTP_404_NOT_FOUND
    def __init__(self, message=None, status_code=None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code