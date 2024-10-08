from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.classroom_exception import ClassroomNotFoundError
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.domain.services.classroom_service import ClassroomService

class GetClassroomUsecase(BaseUseCase[Tuple[int], ClassroomDisplay]):
    serivce: ClassroomService
    
    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> ClassroomDisplay:
        raise NotImplementedError()
    
class GetClassroomUsecaseImp(GetClassroomUsecase):
    def __init__(self, service: ClassroomService):
        self.service: ClassroomService = service

    async def __call__(self, args: Tuple[int]) -> ClassroomDisplay:
        id = args[0]

        try:
            classroom = await self.service.find_object_by_id(id)
            if not classroom:
                raise ClassroomNotFoundError()
            
            return classroom
        except Exception as e:
            raise e