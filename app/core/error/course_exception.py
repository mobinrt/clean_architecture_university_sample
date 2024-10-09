from app.core.error.base_exception import BaseError


class CourseNotFoundError(BaseError):
    message = 'Course does not exist.'


class CoursesNotFoundError(BaseError):
    message = 'Courses do not exist'

class CourseAlreadyExistsError(BaseError):
    message = 'Course already exists'

class CourseNameValidError(BaseError):
    message = 'Course name is invalid.'
    
class CourseIsDeletedError(BaseError):
    message = 'Course is already marked as deleted'
    
class CourseDateValidError(BaseError):
    message = 'The date for the course length is invalid.'
    
class TeacherNotFoundError(BaseError):
    message = 'Teacher do not exist!'

class ClassroomNotFoundError(BaseError):
    message = 'Classroom do not exist!'