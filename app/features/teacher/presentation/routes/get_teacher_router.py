from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.teacher_exception import TeacherNotFoundError
from app.features.teacher.dependencies import get_teacher_use_case
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.usecase.get_teacher import GetTeacherUsecase
from app.features.teacher.presentation.routes import router
from app.features.teacher.presentation.schemas.teacher_error_msg import ErrorMSGTeacherNotFound

@router.get('/{id}/', 
            response_model=TeacherDisplay, status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGTeacherNotFound
                    }
                },
            )
async def get_teacher(id: int, get_teacher_use_case_: GetTeacherUsecase = Depends(get_teacher_use_case)):
    try:
        teacher = await get_teacher_use_case_((id, ))
    except TeacherNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return teacher
