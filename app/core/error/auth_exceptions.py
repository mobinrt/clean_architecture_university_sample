from app.core.error.base_exception import BaseError

class AuthErrorForUser(BaseError):
    message = 'Invalid credentials'
    
class InvalidCredentialsError(AuthErrorForUser):
    message = 'Incorrect name or password'