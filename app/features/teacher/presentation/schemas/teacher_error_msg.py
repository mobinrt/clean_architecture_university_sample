from pydantic import BaseModel, Field

from app.core.error.teacher_exception import (
    TeacherNotFoundError,
    TeachersNotFoundError,
    TeacherAlreadyExistsError,
    TeacherNameValid,
    TeacherIsDeleted
)


class ErrorMSGTeacherNotFound(BaseModel):
    detail: str = Field(default=TeacherNotFoundError.message)


class ErrorMSGTeachersNotFound(BaseModel):
    detail: str = Field(default=TeachersNotFoundError.message)


class ErrorMSGTeacherAlreadyExists(BaseModel):
    detail: str = Field(default=TeacherAlreadyExistsError.message)


class ErrorMSGTeacherNameNotValid(BaseModel):
    detail: str = Field(default=TeacherNameValid.message)

class ErrorMSGTeacherIsDeleted(BaseModel):
    detail: str = Field(default=TeacherIsDeleted.message)