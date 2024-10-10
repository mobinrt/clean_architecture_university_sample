from fastapi import Depends, HTTPException, status

from app.core.error.auth_exceptions import AuthErrorForUser
from app.features.student.dependencies import get_update_student_use_case
from app.features.student.domain.entities.student_schema import StudentUpdate, StudentDisplay
from app.features.student.domain.usecase.update_student import UpdateStudentUseCase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGInvalidAuth
from app.features.auth.data.service import oauth2_sc

@router.put(
    '/update/student/',
    response_model=StudentDisplay,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            'model': ErrorMSGInvalidAuth
        }
    }
)
async def update_student(
    data: StudentUpdate,
    token: str = Depends(oauth2_sc),
    update_student_use_case: UpdateStudentUseCase = Depends(get_update_student_use_case)
):
    try:
        student = await update_student_use_case((token, data))
    except AuthErrorForUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return student
