from fastapi import Depends, HTTPException, status

from app.features.course.dependencies import get_hash_table_use_case
from app.features.course.domain.usecase.hash_table_course import GetHashTableForCourseUseCase
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import ErrorMSGCoursesNotFound
from app.core.error.course_exception import CoursesNotFoundError

@router.get("/hash-table/id/", 
            response_model=dict, 
            status_code=status.HTTP_200_OK,
            responses={status.HTTP_404_NOT_FOUND: {
            'model': ErrorMSGCoursesNotFound
                    }
                },
            )
async def get_hash_table(use_case: GetHashTableForCourseUseCase = Depends(get_hash_table_use_case)):
    try:
        courses_table = await use_case()
    except CoursesNotFoundError as e:
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
    
    return courses_table
