from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.teacher_exception import TeacherNameValid
from app.features.teacher.dependencies import get_create_teacher_use_case
from app.features.teacher.domain.entities.teacher_schema import TeacherCreate, TeacherDisplay
from app.features.teacher.domain.usecase.create_teacher import CreateTeacherUseCase
from app.features.teacher.presentation.routes import router
from app.features.teacher.presentation.schemas.teacher_error_msg import ErrorMSGTeacherNameNotValid

@router.post('/create', 
            response_model=TeacherDisplay, status_code=status.HTTP_201_CREATED, 
            responses={status.HTTP_400_BAD_REQUEST: {
            'model': ErrorMSGTeacherNameNotValid
                    }
                },
            )
async def create_teacher(teacher: TeacherCreate, create_teacher_use_case: CreateTeacherUseCase = Depends(get_create_teacher_use_case)):
    try:
        new_teacher = await create_teacher_use_case((teacher, ))
    except TeacherNameValid as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_teacher