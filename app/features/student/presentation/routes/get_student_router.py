from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.student_exception import StudentNotFoundError
from app.features.student.dependencies import get_student_use_case
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.usecase.get_student import GetStudentUsecase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGStudentNotFound

@router.get('/{id}/', 
            response_model=StudentDisplay, status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGStudentNotFound
                    }
                },
            )
async def get_student(id: int, get_student_use_case_: GetStudentUsecase = Depends(get_student_use_case)):
    try:
        student = await get_student_use_case_((id, ))
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
    
    return student
