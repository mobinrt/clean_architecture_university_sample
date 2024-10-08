from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.course_exception import CoursesNotFoundError
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork

class GetCoursesUsecase(BaseUseCase[None, Sequence[CourseDisplay]]):
    uow: CourseUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: None = None) -> Sequence[CourseDisplay]:
        raise NotImplementedError()
    
class GetCoursesUsecaseImp(GetCoursesUsecase):
    def __init__(self, uow: CourseUnitOfWork):
        self.uow: CourseUnitOfWork = uow

    async def __call__(self, args: None = None) -> Sequence[CourseDisplay]:
        try:
            courses = await self.uow.service.find_all_objects()
            if not courses:
                raise CoursesNotFoundError()
            
            return courses
        except Exception as e:
            raise e
