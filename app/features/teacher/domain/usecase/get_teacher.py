from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.teacher_exception import TeacherNotFoundError
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.repository.teacher_unit_of_work import TeacherUnitOfWork

class GetTeacherUsecase(BaseUseCase[Tuple[int], TeacherDisplay]):
    uow: TeacherUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> TeacherDisplay:
        raise NotImplementedError()
    
class GetTeacherUsecaseImp(GetTeacherUsecase):
    def __init__(self, uow: TeacherUnitOfWork):
        self.uow: TeacherUnitOfWork = uow

    async def __call__(self, args: Tuple[int]) -> TeacherDisplay:
        id = args[0]

        try:
            teacher = await self.uow.service.find_object_by_id(id)
            if not teacher:
                raise TeacherNotFoundError()
            
            return teacher
        except Exception as e:
            raise e