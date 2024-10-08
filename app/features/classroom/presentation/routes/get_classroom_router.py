from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.classroom_exception import ClassroomNotFoundError
from app.features.classroom.dependencies import get_classroom_use_case
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.domain.usecase.get_classroom import GetClassroomUsecase
from app.features.classroom.presentation.routes import router
from app.features.classroom.presentation.schemas.classroom_error_msg import ErrorMSGClassroomNotFound

@router.get('/{id}/', 
            response_model=ClassroomDisplay, status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGClassroomNotFound
                    }
                },
            )
async def get_classroom(id: int, get_classroom_use_case_: GetClassroomUsecase = Depends(get_classroom_use_case)):
    try:
        classroom = await get_classroom_use_case_((id, ))
    except ClassroomNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return classroom
