from fastapi import Depends, HTTPException, status

from app.core.error.classroom_exception import ClassroomNotFoundError, ClassroomIsDeleted
from app.features.classroom.dependencies import get_delete_classroom_use_case
from app.features.classroom.domain.usecase.delete_classroom import DeleteClassroomUseCase
from app.features.classroom.presentation.routes import router
from app.features.classroom.presentation.schemas.classroom_error_msg import ErrorMSGClassroomNotFound, ErrorMSGClassroomIsDeleted
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay

@router.delete('/{id}', 
            response_model=ClassroomDisplay,
            status_code=status.HTTP_200_OK, 
            responses={
            status.HTTP_404_NOT_FOUND: {
                'model': ErrorMSGClassroomNotFound
            },
            status.HTTP_400_BAD_REQUEST: {
                'model': ErrorMSGClassroomIsDeleted
            },
            
        },
    )
async def delete_classroom(id: int, delete_classroom_use_case: DeleteClassroomUseCase = Depends(get_delete_classroom_use_case)):
    try:
        del_classroom = await delete_classroom_use_case((id, ))
    except ClassroomNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except ClassroomIsDeleted as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ex.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=_e.message
        )
        
    return del_classroom