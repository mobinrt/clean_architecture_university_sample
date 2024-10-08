from app.core.error.base_exception import BaseError

class ClassroomNotFoundError(BaseError):
    message = 'Classroom does not exist.'


class ClassroomsNotFoundError(BaseError):
    message = 'Classrooms do not exist'

class ClassroomAlreadyExistsError(BaseError):
    message = 'Classroom already exists'

class ClassroomNumberValid(BaseError):
    message = 'Number should be in range of positive!'
    
class ClassroomIsDeleted(BaseError):
    message = 'Classroom is already marked as deleted'