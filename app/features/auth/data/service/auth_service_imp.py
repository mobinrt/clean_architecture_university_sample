from ...domain.services.auth_service import AuthService
from app.core.util import hash
from app.core.models.person import Person
from app.core.error.auth_exceptions import AuthErrorForUser, InvalidCredentialsError
from app.core.models.person import Person
from ...domain.entities.auth_schemas import TokenDisplay
from fastapi.security import OAuth2PasswordBearer

import os
from typing import TypeVar, Generic, Type
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from typing import TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timedelta, timezone
import secrets

SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
oauth2_sc = OAuth2PasswordBearer(tokenUrl='token')

_MODEL = TypeVar('_MODEL', bound=Person)

class AuthServiceImp(AuthService[_MODEL], Generic[_MODEL]):
    def __init__(self, session: AsyncSession, model: Type[_MODEL]):
        self.session = session
        self.model = model 

    async def get_user_by_id(self, user_id: int) -> _MODEL | None:
        result = await self.session.execute(select(self.model).where(self.model.id == user_id))
        return result.scalar_one_or_none()

    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return hash.verify_password(plain_password, hashed_password)

    async def create_access_token(self, data: dict) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        data.update({"exp": expire})
        return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    async def get_current_user(self, token: str) -> _MODEL:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("sub")
            if not user_id:
                raise AuthErrorForUser()
        except JWTError:
            raise AuthErrorForUser()

        user = await self.get_user_by_id(int(user_id))
        if not user:
            raise AuthErrorForUser()

        return user

    async def get_token(self, request: OAuth2PasswordRequestForm) -> TokenDisplay:
        #headers={"WWW-Authenticate": "bearer"}
        
        user = await self.get_user_by_id(request.username)
        if not user or not await self.verify_password(request.password, user.password):
            raise InvalidCredentialsError

        access_token = await self.create_access_token(data={'sub': str(user.id)})
        return TokenDisplay(access_token=access_token, token_type='bearer')