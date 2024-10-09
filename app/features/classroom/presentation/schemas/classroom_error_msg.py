from pydantic import BaseModel, Field

from app.core.error.classroom_exception import (
    ClassroomNotFoundError,
    ClassroomsNotFoundError,
    ClassroomAlreadyExistsError,
    ClassroomNumberValid,
    ClassroomIsDeleted
)


class ErrorMSGClassroomNotFound(BaseModel):
    detail: str = Field(default=ClassroomNotFoundError.message)


class ErrorMSGClassroomsNotFound(BaseModel):
    detail: str = Field(default=ClassroomsNotFoundError.message)


class ErrorMSGClassroomAlreadyExists(BaseModel):
    detail: str = Field(default=ClassroomAlreadyExistsError.message)


class ErrorMSGClassroomNumberNotValid(BaseModel):
    detail: str = Field(default=ClassroomNumberValid.message)


class ErrorMSGClassroomIsDeleted(BaseModel):
    detail: str = Field(default=ClassroomIsDeleted.message)