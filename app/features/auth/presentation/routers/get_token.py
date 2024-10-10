from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, status, Depends
from typing import Union
from app.features.auth.data.service import oauth2_sc
from app.features.auth.domain.entities.auth_schemas import TokenDisplay, UserDisplay
from app.features.student.dependencies import get_auth_service
from app.features.auth.data.service.auth_service_imp import AuthServiceImp

router = APIRouter(tags=['authentication'])

@router.post('/token', response_model=TokenDisplay, status_code=status.HTTP_200_OK)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    auth_service: AuthServiceImp = Depends(get_auth_service)
):
    return await auth_service.get_token(form_data)

@router.get("/dev-login-token")
async def get_dev_token(auth_service: AuthServiceImp = Depends(get_auth_service)):
    user_type = "dev"  

    token = await auth_service.create_access_token(data={"sub": "dev_user"}, user_type=user_type)

    return {"access_token": token, "token_type": "bearer"}


@router.get("/read/users/me", response_model=UserDisplay)
async def read_users_me(token: str = Depends(oauth2_sc), auth_service: AuthServiceImp = Depends(get_auth_service)):
    return await auth_service.get_current_user(token)