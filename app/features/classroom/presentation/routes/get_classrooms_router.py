from fastapi import Depends, HTTPException, status
from typing import Sequence

from app.core.error.classroom_exception import ClassroomsNotFoundError
from app.features.classroom.dependencies import get_classrooms_use_case
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.domain.usecase.get_classrooms import GetClassroomsUsecase
from app.features.classroom.presentation.routes import router
from app.features.classroom.presentation.schemas.classroom_error_msg import ErrorMSGClassroomsNotFound

@router.get('/', 
            response_model=Sequence[ClassroomDisplay], status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGClassroomsNotFound
                    }
                },
            )
async def get_classrooms(get_classrooms_use_case_: GetClassroomsUsecase = Depends(get_classrooms_use_case)):
    try:
        classrooms = await get_classrooms_use_case_()
    except ClassroomsNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return classrooms
