from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.course_exception import CourseNotFoundError
from app.features.course.dependencies import get_course_use_case
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.usecase.get_course import GetCourseUsecase
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import ErrorMSGCourseNotFound

@router.get('/{id}/', 
            response_model=CourseDisplay, status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGCourseNotFound
                    }
                },
            )
async def get_course(id: int, get_course_use_case_: GetCourseUsecase = Depends(get_course_use_case)):
    try:
        course = await get_course_use_case_((id, ))
    except CourseNotFoundError as e:
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
