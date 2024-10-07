from app.core.error.base_exception import BaseError

class TeacherNotFoundError(BaseError):
    message = 'Teacher does not exist.'


class TeachersNotFoundError(BaseError):
    message = 'Teachers do not exist'


class TeacherAlreadyExistsError(BaseError):
    message = 'Teacher already exists'

class TeacherNameValid(BaseError):
    message = 'Username should not be blank!'
    
class TeacherIsDeleted(BaseError):
    message = 'Teacher is already marked as deleted'