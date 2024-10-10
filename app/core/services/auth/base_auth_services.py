from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from fastapi.security import OAuth2PasswordRequestForm

from app.core.models.person import Person
from ....features.auth.domain.entities.auth_schemas import TokenDisplay 

_MODEL = TypeVar('_MODEL', bound=Person)


class AbstractAuthServices(ABC, Generic[_MODEL]):

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> _MODEL | None:
        raise NotImplementedError()
    
 
    @abstractmethod
    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError()
 

    @abstractmethod
    async def create_access_token(self, data: dict) -> str:
       raise NotImplementedError()
 
 
    @abstractmethod
    async def get_current_user(self, token: str) -> _MODEL:
        raise NotImplementedError()


    @abstractmethod
    async def get_token(self, request: OAuth2PasswordRequestForm) -> TokenDisplay:
        raise NotImplementedError()