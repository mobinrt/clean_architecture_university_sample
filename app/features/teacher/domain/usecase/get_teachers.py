from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.teacher_exception import TeachersNotFoundError
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.repository.teacher_unite_of_work import TeacherUnitOfWork

class GetTeachersUsecase(BaseUseCase[None, Sequence[TeacherDisplay]]):       #use Tuple or not??
    uow: TeacherUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: None = None) -> Sequence[TeacherDisplay]:
        raise NotImplementedError()
    
class GetTeachersUsecaseImp(GetTeachersUsecase):
    def __init__(self, uow: TeacherUnitOfWork):
        self.uow: TeacherUnitOfWork = uow

    async def __call__(self, args: None = None) -> Sequence[TeacherDisplay]:
        try:
            teachers = await self.uow.service.find_all_objects()
            if not teachers:
                raise TeachersNotFoundError()
            
            return teachers
        except Exception as e:
            raise e