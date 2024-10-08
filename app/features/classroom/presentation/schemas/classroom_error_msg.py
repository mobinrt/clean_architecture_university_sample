from pydantic import BaseModel, Field

from app.core.error.classroom_exception import (
    ClassroomNotFoundError,
    ClassroomsNotFoundError,
    ClassroomAlreadyExistsError,
    ClassroomNumberValid,
    ClassroomIsDeleted
)


class ErrorMSGClassroomNotFound(BaseModel):
    detail: str = Field(example=ClassroomNotFoundError.message)


class ErrorMSGClassroomsNotFound(BaseModel):
    detail: str = Field(example=ClassroomsNotFoundError.message)


class ErrorMSGClassroomAlreadyExists(BaseModel):
    detail: str = Field(example=ClassroomAlreadyExistsError.message)


class ErrorMSGClassroomNumberNotValid(BaseModel):
    detail: str = Field(example=ClassroomNumberValid.message)


class ErrorMSGClassroomIsDeleted(BaseModel):
    detail: str = Field(example=ClassroomIsDeleted.message)