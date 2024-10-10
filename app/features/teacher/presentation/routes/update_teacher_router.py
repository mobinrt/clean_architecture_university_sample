from fastapi import Depends, HTTPException, status

from app.core.error.auth_exceptions import AuthErrorForUser
from app.features.teacher.dependencies import get_update_teacher_use_case
from app.features.teacher.domain.entities.teacher_schema import TeacherUpdate, TeacherDisplay
from app.features.teacher.domain.usecase.update_teacher import UpdateTeacherUseCase
from app.features.teacher.presentation.routes import router
from app.features.teacher.presentation.schemas.teacher_error_msg import ErrorMSGInvalidAuth
from app.features.auth.data.service import oauth2_sc

@router.put('/update/current/',
        response_model=TeacherDisplay,
        status_code=status.HTTP_200_OK,
        responses={
            status.HTTP_401_UNAUTHORIZED: {
                'model': ErrorMSGInvalidAuth
            }
        }
)
async def update_teacher(
    data: TeacherUpdate,
    token: str = Depends(oauth2_sc),
    update_teacher_use_case: UpdateTeacherUseCase = Depends(get_update_teacher_use_case)
):
    try:
        teacher = await update_teacher_use_case((token, data))
    except AuthErrorForUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return teacher
