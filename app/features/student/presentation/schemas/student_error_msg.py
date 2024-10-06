from pydantic import BaseModel, Field

from app.core.error.student_exception import (
    StudentNotFoundError,
    StudentsNotFoundError,
    StudentAlreadyExistsError,
    StudentNameValid
)


class ErrorMSGStudentNotFound(BaseModel):
    detail: str = Field(example=StudentNotFoundError.message)


class ErrorMSGStudentsNotFound(BaseModel):
    detail: str = Field(example=StudentsNotFoundError.message)


class ErrorMSGStudentAlreadyExists(BaseModel):
    detail: str = Field(example=StudentAlreadyExistsError.message)


class ErrorMSGStudentNameNotValid(BaseModel):
    detail: str = Field(example=StudentNameValid.message)
