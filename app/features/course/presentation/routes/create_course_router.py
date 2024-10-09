from fastapi import Depends, HTTPException, status

from app.core.error.course_exception import CourseNameValidError
from app.features.course.dependencies import get_create_course_use_case
from app.features.course.domain.entities.course_schema import CourseCreate, CourseDisplay
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import (
    ErrorMSGCourseNameNotValid, 
    ErrorMSGClassroomNotFound, 
    ErrorMSGTeacherNotFound,
    ErrorMSGCourseValidDate,
    ErrorsResponse
    )
from app.features.course.domain.usecase.create_course import (
    CreateCourseUseCase, 
    TeacherNotFoundError, 
    ClassroomNotFoundError,
    CourseDateValidError
    )


@router.post('/create/', 
            response_model=CourseDisplay, status_code=status.HTTP_201_CREATED, 
            responses={
                status.HTTP_400_BAD_REQUEST: {
                    'model': ErrorsResponse
                },
                status.HTTP_404_NOT_FOUND: {
                    'model': ErrorsResponse
                }
            },
        )
async def create_course(course: CourseCreate, create_course_use_case: CreateCourseUseCase = Depends(get_create_course_use_case)):
    try:
        new_course = await create_course_use_case((course, ))
        
    except CourseNameValidError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorsResponse(
                detail=ErrorMSGCourseNameNotValid().detail,
                errors=['Course name should not be blank!']
            ).model_dump()
        )
    except CourseDateValidError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorsResponse(
                detail=ErrorMSGCourseValidDate().detail,
                errors=['The course must be a minimum of 10 days long.']
            ).model_dump()
        )
    except TeacherNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=ErrorsResponse(
                detail=ErrorMSGTeacherNotFound().detail,
                errors=['Teacher with this id is not found! Enter proper id.']
                ).model_dump()
            )    
    except ClassroomNotFoundError: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=ErrorsResponse(
                detail=ErrorMSGClassroomNotFound().detail,
                errors=['Classroom with this id is not found! Enter proper id.']
                ).model_dump()
            )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_course
