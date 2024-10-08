from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.features.classroom.domain.entities.classroom_schema import ClassroomCreate, ClassroomDisplay
from app.features.classroom.domain.entities.classroom_entity import ClassroomEntity
from app.features.classroom.domain.repository.classroom_unite_of_work import ClassroomUnitOfWork
from app.features.classroom.data.model.convert_classroom import ConvertClassroom
from app.core.error.classroom_exception import ClassroomNumberValid, ClassroomAlreadyExistsError
class CreateClassroomUseCase(BaseUseCase[Tuple[ClassroomCreate], ClassroomDisplay]):
    uow: ClassroomUnitOfWork

    @abstractmethod
    async def __call__(self, args: Tuple[ClassroomCreate]) -> ClassroomDisplay:
        raise NotImplementedError()

class CreateClassroomUseCaseImp(CreateClassroomUseCase):
    def __init__(self, uow: ClassroomUnitOfWork):
        self.uow: ClassroomUnitOfWork = uow
        
    async def __call__(self, args: Tuple[ClassroomCreate]) -> ClassroomDisplay:
        data = args[0]
        
        if data.number <= 0:
            raise ClassroomNumberValid()
        
        existing_classroom = await self.uow.repository.find_classroom_by_number(data.number)
        if existing_classroom:
            raise ClassroomAlreadyExistsError()
            
        new_classroom = ClassroomEntity(
            **data.model_dump()
        )
        
        
        try:
            classroom = await self.uow.repository.create_object(new_classroom)
            await self.uow.commit()
            await self.uow.refresh(classroom)
        except Exception as e:
            await self.uow.rollback()
            raise e
        
        c =  ConvertClassroom.from_entity(classroom)
        print('convert: ', c)   
        
        return c