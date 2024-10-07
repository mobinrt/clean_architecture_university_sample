from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.student_exception import StudentNameValid
from app.features.student.dependencies import get_create_student_use_case
from app.features.student.domain.entities.student_schema import StudentCreate, StudentDisplay
from app.features.student.domain.usecase.create_student import CreateStudentUseCase
from app.features.student.presentation.routes import router
from app.features.student.presentation.schemas.student_error_msg import ErrorMSGStudentNameNotValid

@router.post('/create', 
            response_model=StudentDisplay, status_code=status.HTTP_201_CREATED, 
            responses={status.HTTP_400_BAD_REQUEST: {
            'model': ErrorMSGStudentNameNotValid
                    }
                },
            )
async def create_student(student: StudentCreate, create_student_use_case: CreateStudentUseCase = Depends(get_create_student_use_case)):
    try:
        new_student = await create_student_use_case((student, ))
    except StudentNameValid as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_student