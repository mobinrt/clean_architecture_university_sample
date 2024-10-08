from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.classroom_exception import ClassroomNumberValid, ClassroomAlreadyExistsError
from app.features.classroom.dependencies import get_create_classroom_use_case
from app.features.classroom.domain.entities.classroom_schema import ClassroomCreate, ClassroomDisplay
from app.features.classroom.domain.usecase.create_classroom import CreateClassroomUseCase
from app.features.classroom.presentation.routes import router
from app.features.classroom.presentation.schemas.classroom_error_msg import ErrorMSGClassroomNumberNotValid, ErrorMSGClassroomAlreadyExists

@router.post('/create', 
            response_model=ClassroomDisplay, status_code=status.HTTP_201_CREATED, 
            responses={
                status.HTTP_400_BAD_REQUEST: {
                'model': ErrorMSGClassroomNumberNotValid
                    },
                status.HTTP_409_CONFLICT: {
                    'model': ErrorMSGClassroomAlreadyExists
                    }
                },
            )
async def create_classroom(classroom: ClassroomCreate, create_classroom_use_case: CreateClassroomUseCase = Depends(get_create_classroom_use_case)):
    try:
        new_classroom = await create_classroom_use_case((classroom, ))
    except ClassroomNumberValid as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except ClassroomAlreadyExistsError as ex:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=ex.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_classroom