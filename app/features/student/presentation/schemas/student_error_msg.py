from pydantic import BaseModel, Field

from app.core.error.auth_exceptions import AuthErrorForUser
from app.core.error.student_exception import (
    StudentNotFoundError,
    StudentsNotFoundError,
    StudentAlreadyExistsError,
    StudentNameValidError,
    StudentIsDeletedError
)


class ErrorMSGStudentNotFound(BaseModel):
    detail: str = Field(default=StudentNotFoundError.message)


class ErrorMSGStudentsNotFound(BaseModel):
    detail: str = Field(default=StudentsNotFoundError.message)


class ErrorMSGStudentAlreadyExists(BaseModel):
    detail: str = Field(default=StudentAlreadyExistsError.message)


class ErrorMSGStudentNameNotValid(BaseModel):
    detail: str = Field(default=StudentNameValidError.message)

class ErrorMSGStudentIsDeleted(BaseModel):
    detail: str = Field(default=StudentIsDeletedError.message)
    
class ErrorMSGInvalidAuth(BaseModel):
    detail: str = Field(default=AuthErrorForUser.message)