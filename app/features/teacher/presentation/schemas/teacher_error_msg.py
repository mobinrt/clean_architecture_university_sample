from pydantic import BaseModel, Field

from app.core.error.teacher_exception import (
    TeacherNotFoundError,
    TeachersNotFoundError,
    TeacherAlreadyExistsError,
    TeacherNameValid,
    TeacherIsDeleted
)


class ErrorMSGTeacherNotFound(BaseModel):
    detail: str = Field(example=TeacherNotFoundError.message)


class ErrorMSGTeachersNotFound(BaseModel):
    detail: str = Field(example=TeachersNotFoundError.message)


class ErrorMSGTeacherAlreadyExists(BaseModel):
    detail: str = Field(example=TeacherAlreadyExistsError.message)


class ErrorMSGTeacherNameNotValid(BaseModel):
    detail: str = Field(example=TeacherNameValid.message)

class ErrorMSGTeacherIsDeleted(BaseModel):
    detail: str = Field(example=TeacherIsDeleted.message)