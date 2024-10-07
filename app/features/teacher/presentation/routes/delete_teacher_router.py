from fastapi import Depends, HTTPException, status

from app.core.error.teacher_exception import TeacherNotFoundError, TeacherIsDeleted
from app.features.teacher.dependencies import get_delete_teacher_use_case
from app.features.teacher.domain.usecase.delete_teacher import DeleteTeacherUseCase
from app.features.teacher.presentation.routes import router
from app.features.teacher.presentation.schemas.teacher_error_msg import ErrorMSGTeacherNotFound, ErrorMSGTeacherIsDeleted
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay

@router.delete('/{id}', 
            response_model=TeacherDisplay,
            status_code=status.HTTP_200_OK, 
            responses={
            status.HTTP_404_NOT_FOUND: {
                'model': ErrorMSGTeacherNotFound
            },
            status.HTTP_400_BAD_REQUEST: {
                'model': ErrorMSGTeacherIsDeleted
            },
            
        },
    )
async def delete_teacher(id: int, delete_teacher_use_case: DeleteTeacherUseCase = Depends(get_delete_teacher_use_case)):
    try:
        del_teacher = await delete_teacher_use_case((id, ))
    except TeacherNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except TeacherIsDeleted as ex:
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
        
    return del_teacher