from typing import TypeVar
from app.core.services.auth.base_auth_services import AbstractAuthServices
from app.core.models.person import Person 

_MODEL = TypeVar('_MODEL', bound=Person)

class AuthService(AbstractAuthServices[_MODEL]):
    pass
    