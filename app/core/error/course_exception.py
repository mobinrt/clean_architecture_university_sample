from app.core.error.base_exception import BaseError


class CourseNotFoundError(BaseError):
    message = 'Course does not exist.'


class CoursesNotFoundError(BaseError):
    message = 'Courses do not exist'

class CourseAlreadyExistsError(BaseError):
    message = 'Course already exists'

class CourseNameValidError(BaseError):
    message = 'Course name should not be blank!'
    
class CourseIsDeletedError(BaseError):
    message = 'Course is already marked as deleted'
    
class CourseDateValidError(BaseError):
    message = 'The course must be at least 10 days long.'