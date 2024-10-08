from fastapi import Depends, HTTPException, status

from app.core.error.course_exception import CourseNotFoundError, CourseIsDeletedError
from app.features.course.dependencies import get_delete_course_use_case
from app.features.course.domain.usecase.delete_course import DeleteCourseUseCase
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import ErrorMSGCourseNotFound, ErrorMSGCourseIsDeleted
from app.features.course.domain.entities.course_schema import CourseDisplay

@router.delete('/{id}', 
            response_model=CourseDisplay,
            status_code=status.HTTP_200_OK, 
            responses={
            status.HTTP_404_NOT_FOUND: {
                'model': ErrorMSGCourseNotFound
            },
            status.HTTP_400_BAD_REQUEST: {
                'model': ErrorMSGCourseIsDeleted
            },
            
        },
    )
async def delete_course(id: int, delete_course_use_case: DeleteCourseUseCase = Depends(get_delete_course_use_case)):
    try:
        del_course = await delete_course_use_case((id, ))
    except CourseNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except CourseIsDeletedError as ex:
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
        
    return del_course
