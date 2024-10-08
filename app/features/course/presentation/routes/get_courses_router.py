from fastapi import Depends, HTTPException, status
from typing import Sequence

from app.core.error.course_exception import CoursesNotFoundError
from app.features.course.dependencies import get_courses_use_case
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.usecase.get_courses import GetCoursesUsecase
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import ErrorMSGCoursesNotFound

@router.get('/', 
            response_model=Sequence[CourseDisplay], status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGCoursesNotFound
                    }
                },
            )
async def get_courses(get_courses_use_case_: GetCoursesUsecase = Depends(get_courses_use_case)):
    try:
        course = await get_courses_use_case_()
    except CoursesNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return course
