from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.classroom_exception import ClassroomsNotFoundError
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.domain.repository.classroom_unite_of_work import ClassroomUnitOfWork

class GetClassroomsUsecase(BaseUseCase[None, Sequence[ClassroomDisplay]]):       #use Tuple or not??
    uow: ClassroomUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: None = None) -> Sequence[ClassroomDisplay]:
        raise NotImplementedError()
    
class GetClassroomsUsecaseImp(GetClassroomsUsecase):
    def __init__(self, uow: ClassroomUnitOfWork):
        self.uow: ClassroomUnitOfWork = uow

    async def __call__(self, args: None = None) -> Sequence[ClassroomDisplay]:
        try:
            classrooms = await self.uow.service.find_all_objects()
            if not classrooms:
                raise ClassroomsNotFoundError()
            
            return classrooms
        except Exception as e:
            raise e