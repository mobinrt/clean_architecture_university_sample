from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.course_exception import CourseNotFoundError
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork

class GetCourseUsecase(BaseUseCase[Tuple[int], CourseDisplay]):
    uow: CourseUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> CourseDisplay:
        raise NotImplementedError()
    
class GetCourseUsecaseImp(GetCourseUsecase):
    def __init__(self, uow: CourseUnitOfWork):
        self.uow: CourseUnitOfWork = uow

    async def __call__(self, args: Tuple[int]) -> CourseDisplay:
        id = args[0]

        try:
            print('course')
            course = await self.uow.service.find_object_by_id(id)
            print(course)
            if not course:
                raise CourseNotFoundError()
            
            return course
        except Exception as e:
            raise e 
