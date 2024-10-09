from pydantic import BaseModel, Field

from app.core.error.course_exception import (
    CourseNotFoundError,
    CoursesNotFoundError,
    CourseAlreadyExistsError,
    CourseNameValidError,
    CourseIsDeletedError,
    TeacherNotFoundError,
    ClassroomNotFoundError,
    CourseDateValidError
)

class ErrorsResponse(BaseModel):
    detail: str
    errors: list[str]

class ErrorMSGCourseNotFound(BaseModel):
    detail: str = Field(default=CourseNotFoundError.message)


class ErrorMSGCoursesNotFound(BaseModel):
    detail: str = Field(default=CoursesNotFoundError.message)


class ErrorMSGCourseAlreadyExists(BaseModel):
    detail: str = Field(default=CourseAlreadyExistsError.message)


class ErrorMSGCourseNameNotValid(BaseModel):
    detail: str = Field(default=CourseNameValidError.message)

class ErrorMSGCourseIsDeleted(BaseModel):
    detail: str = Field(default=CourseIsDeletedError.message)
    
class ErrorMSGCourseValidDate(BaseModel):
    detail: str = Field(default=CourseDateValidError.message)
    
class ErrorMSGTeacherNotFound(BaseModel):
    detail: str = Field(default=TeacherNotFoundError.message)
    
class ErrorMSGClassroomNotFound(BaseModel):
    detail: str = Field(default=ClassroomNotFoundError.message)
    
