from fastapi import Depends, HTTPException, status
from typing import Sequence

from app.core.error.student_exception import StudentsNotFoundError
from app.features.student.dependencies import get_students_use_case
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.usecase.get_students import GetStudentsUsecase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGStudentsNotFound

@router.get('/', 
            response_model=Sequence[StudentDisplay], status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGStudentsNotFound
                    }
                },
            )
async def get_students(get_students_use_case_: GetStudentsUsecase = Depends(get_students_use_case)):
    try:
        student = await get_students_use_case_()
    except StudentsNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return student
