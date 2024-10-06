from fastapi import Depends, HTTPException, status

from app.core.error.student_exception import StudentNotFoundError
from app.features.student.dependencies import get_delete_student_use_case
from app.features.student.domain.usecase.delete_student import DeleteStudentUseCase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGStudentNotFound
from app.features.student.domain.entities.student_schema import StudentDisplay

@router.delete('/{id}', 
            response_model=StudentDisplay,
            status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGStudentNotFound
                    }
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
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return del_student