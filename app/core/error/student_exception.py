from app.core.error.base_exception import BaseError


class StudentNotFoundError(BaseError):
    message = 'Student does not exist!'


class StudentsNotFoundError(BaseError):
    message = 'Students do not exist!'


class StudentAlreadyExistsError(BaseError):
    message = 'Student already exists!'

class StudentNameValid(BaseError):
    message = 'Username should not be blank!'
    
class StudentIsDeleted(BaseError):
    message = 'Student is already marked as deleted'