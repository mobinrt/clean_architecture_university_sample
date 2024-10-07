from fastapi import Depends, HTTPException, status
from typing import Sequence

from app.core.error.teacher_exception import TeachersNotFoundError
from app.features.teacher.dependencies import get_teachers_use_case
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.usecase.get_teachers import GetTeachersUsecase
from app.features.teacher.presentation.routes import router
from app.features.teacher.presentation.schemas.teacher_error_msg import ErrorMSGTeachersNotFound

@router.get('/', 
            response_model=Sequence[TeacherDisplay], status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGTeachersNotFound
                    }
                },
            )
async def get_teachers(get_teachers_use_case_: GetTeachersUsecase = Depends(get_teachers_use_case)):
    try:
        teachers = await get_teachers_use_case_()
    except TeachersNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return teachers
