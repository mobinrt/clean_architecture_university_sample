from app.core.error.base_exception import BaseError


class StudentNotFoundError(BaseError):
    message = 'Student does not exist!'


class StudentsNotFoundError(BaseError):
    message = 'Students do not exist!'


class StudentAlreadyExistsError(BaseError):
    message = 'Student already exists!'

class StudentNameValidError(BaseError):
    message = 'Username should not be blank!'
    
class StudentIsDeletedError(BaseError):
    message = 'Student is already marked as deleted'