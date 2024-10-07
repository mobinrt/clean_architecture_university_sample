from fastapi import Depends, HTTPException, status

from app.features.teacher.dependencies import get_hash_table_use_case
from app.features.teacher.domain.usecase.hash_table_teacher import GetHashTableForTeacherUseCase
from app.features.teacher.presentation.routes import router
from app.features.teacher.presentation.schemas.teacher_error_msg import ErrorMSGTeachersNotFound
from app.core.error.teacher_exception import TeachersNotFoundError

@router.get("/hash-table/id/", 
            response_model=dict, 
            status_code=status.HTTP_200_OK,
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGTeachersNotFound
            }
        },
    )
async def get_hash_table(use_case: GetHashTableForTeacherUseCase = Depends(get_hash_table_use_case)):
    try:
        teachers_table = await use_case()
    except TeachersNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=_e.message
        )
    
    return teachers_table