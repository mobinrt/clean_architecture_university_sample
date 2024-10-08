from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.course_exception import CourseNameValidError
from app.features.course.dependencies import get_create_course_use_case
from app.features.course.domain.entities.course_schema import CourseCreate, CourseDisplay
from app.features.course.domain.usecase.create_course import CreateCourseUseCase, TeacherNotFoundError, ClassroomNotFoundError
from app.features.course.presentation.routes import router
from app.features.course.presentation.schemas.course_error_msg import ErrorMSGCourseNameNotValid, ErrorMSGClassroomNotFound, ErrorMSGTeacherNotFound

@router.post('/create', 
            response_model=CourseDisplay, status_code=status.HTTP_201_CREATED, 
            responses={
                status.HTTP_400_BAD_REQUEST: {
                'model': ErrorMSGCourseNameNotValid
                    },
                status.HTTP_404_NOT_FOUND: {
                     'model': {
                         "description": "Classroom or Teacher not found to attend in course",
                         "content": {
                             "application/json": {
                                 "schema": {
                                     "anyOf": [
                                         {"$ref": "#/components/schemas/ErrorMSGClassroomNotFound"},
                                         {"$ref": "#/components/schemas/ErrorMSGTeacherNotFound"}
                                    ]
                                }
                            }
                        }
                    }
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
    except ClassroomNotFoundError: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=ErrorMSGClassroomNotFound.detail
            )
    except TeacherNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=ErrorMSGTeacherNotFound.detail
            )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_course
