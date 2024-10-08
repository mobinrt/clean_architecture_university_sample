from pydantic import BaseModel, Field

from app.core.error.course_exception import (
    CourseNotFoundError,
    CoursesNotFoundError,
    CourseAlreadyExistsError,
    CourseNameValidError,
    CourseIsDeletedError,
    TeacherNotFoundError,
    ClassroomNotFoundError
)


class ErrorMSGCourseNotFound(BaseModel):
    detail: str = Field(example=CourseNotFoundError.message)


class ErrorMSGCoursesNotFound(BaseModel):
    detail: str = Field(example=CoursesNotFoundError.message)


class ErrorMSGCourseAlreadyExists(BaseModel):
    detail: str = Field(example=CourseAlreadyExistsError.message)


class ErrorMSGCourseNameNotValid(BaseModel):
    detail: str = Field(example=CourseNameValidError.message)

class ErrorMSGCourseIsDeleted(BaseModel):
    detail: str = Field(example=CourseIsDeletedError.message)
    
class ErrorMSGTeacherNotFound(BaseModel):
    detail: str = Field(example=TeacherNotFoundError.message)
    
class ErrorMSGClassroomNotFound(BaseModel):
    detail: str = Field(example=ClassroomNotFoundError.message)