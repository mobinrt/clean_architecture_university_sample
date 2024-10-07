from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.teacher_exception import TeachersNotFoundError
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.services.teacher_service import TeacherService

class GetTeachersUsecase(BaseUseCase[None, Sequence[TeacherDisplay]]):       #use Tuple or not??
    service: TeacherService
    
    @abstractmethod
    async def __call__(self, args: None = None) -> Sequence[TeacherDisplay]:
        raise NotImplementedError()
    
class GetTeachersUsecaseImp(GetTeachersUsecase):
    def __init__(self, service: TeacherService):
        self.service: TeacherService = service

    async def __call__(self, args: None = None) -> Sequence[TeacherDisplay]:
        try:
            teachers = await self.service.find_all_objects()
            if not teachers:
                raise TeachersNotFoundError()
            
            return teachers
        except Exception as e:
            raise e