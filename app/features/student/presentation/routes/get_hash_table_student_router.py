from fastapi import Depends, HTTPException, status

from app.core.enum.object_type_str import ObjectToSTR
from app.features.student.dependencies import get_hash_table_use_case
from app.features.student.domain.usecase.hash_table_student import GetHashTableForStudentUseCase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGStudentsNotFound
from app.core.error.student_exception import StudentsNotFoundError

@router.get("/hash-table/id/", 
            response_model=dict, 
            status_code=status.HTTP_200_OK,
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGStudentsNotFound
                    }
                },
            )
async def get_hash_table(use_case: GetHashTableForStudentUseCase = Depends(get_hash_table_use_case)):
    try:
        students_table = await use_case()
    except StudentsNotFoundError as e:
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
    
    return students_table
