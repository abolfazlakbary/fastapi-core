from core.database.connection import AsyncSession
from core.exceptions.exc import BadRequestException
import re


class Validate:

    @staticmethod
    async def validate(db: AsyncSession, form_data: dict, record_id: int | None = None):
        errors = {}
        if hasattr(form_data, "create_validation"):
            errors = await form_data.create_validation(db, errors)
        elif hasattr(form_data, "update_validation"):
            errors = await form_data.update_validation(db, errors, record_id)
            
        if errors != {}:
            raise BadRequestException(errors=errors)



def check_email_is_valid(input: str) -> bool:
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return email_pattern.match(input)


def error_handler(error_message: str, fied_name: str, errors):
    if fied_name in errors:
        errors[fied_name].append(error_message)
    else:
        errors[fied_name] = [error_message]