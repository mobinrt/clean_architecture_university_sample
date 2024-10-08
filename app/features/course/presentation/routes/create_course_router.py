from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.course_exception import CourseNameValidError
from app.features.course.dependencies import get_create_course_use_case
from app.features.course.domain.entities.course_schema import CourseCreate, CourseDisplay
from app.features.course.domain.usecase.create_course import CreateCourseUseCase
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import ErrorMSGCourseNameNotValid

@router.post('/create', 
            response_model=CourseDisplay, status_code=status.HTTP_201_CREATED, 
            responses={status.HTTP_400_BAD_REQUEST: {
            'model': ErrorMSGCourseNameNotValid
                    }
                },
            )
async def create_course(course: CourseCreate, create_course_use_case: CreateCourseUseCase = Depends(get_create_course_use_case)):
    try:
        new_course = await create_course_use_case((course, ))
    except CourseNameValidError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_course
