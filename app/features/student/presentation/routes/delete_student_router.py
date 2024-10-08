from fastapi import Depends, HTTPException, status

from app.core.error.student_exception import StudentNotFoundError, StudentIsDeletedError
from app.features.student.dependencies import get_delete_student_use_case
from app.features.student.domain.usecase.delete_student import DeleteStudentUseCase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGStudentNotFound, ErrorMSGStudentIsDeleted
from app.features.student.domain.entities.student_schema import StudentDisplay

@router.delete('/{id}', 
            response_model=StudentDisplay,
            status_code=status.HTTP_200_OK, 
            responses={
            status.HTTP_404_NOT_FOUND: {
                'model': ErrorMSGStudentNotFound
            },
            status.HTTP_400_BAD_REQUEST: {
                'model': ErrorMSGStudentIsDeleted
            },
            
        },
    )
async def delete_student(id: int, delete_student_use_case: DeleteStudentUseCase = Depends(get_delete_student_use_case)):
    try:
        del_student = await delete_student_use_case((id, ))
    except StudentNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except StudentIsDeletedError as ex:
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
        
    return del_student