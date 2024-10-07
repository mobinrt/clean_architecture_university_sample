from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.teacher_exception import TeacherNotFoundError
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.services.teacher_service import TeacherService

class GetTeacherUsecase(BaseUseCase[Tuple[int], TeacherDisplay]):
    serivce: TeacherService
    
    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> TeacherDisplay:
        raise NotImplementedError()
    
class GetTeacherUsecaseImp(GetTeacherUsecase):
    def __init__(self, service: TeacherService):
        self.service: TeacherService = service

    async def __call__(self, args: Tuple[int]) -> TeacherDisplay:
        id = args[0]

        try:
            teacher = await self.service.find_object_by_id(id)
            if not teacher:
                raise TeacherNotFoundError()
            
            return teacher
        except Exception as e:
            raise e