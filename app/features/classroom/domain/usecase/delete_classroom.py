from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.features.classroom.domain.entities.classroom_entity import ClassroomEntity
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.domain.repository.classroom_unite_of_work import ClassroomUnitOfWork
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.classroom_exception import ClassroomNotFoundError, ClassroomIsDeleted
from app.features.classroom.data.model.convert_classroom import ConvertClassroom

class DeleteClassroomUseCase(BaseUseCase[Tuple[int], ClassroomDisplay]):
    uow: ClassroomUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ClassroomDisplay:
        raise NotImplementedError()

class DeleteClassroomUseCaseImpl(DeleteClassroomUseCase):
    def __init__(self, uow: ClassroomUnitOfWork):
        self.uow: ClassroomUnitOfWork = uow
        
    async def __call__(self, args: Tuple[int]) -> ClassroomDisplay:
        id = args[0]
        existing_classroom_db = await self.uow.repository.find_object_by_id(id)
        
        if existing_classroom_db is None:
            raise ClassroomNotFoundError()
        
        existing_classroom_entity = self.uow.repository.to_entity(existing_classroom_db)
        
        try:
            if existing_classroom_db.is_deleted:
                raise ClassroomIsDeleted()
                        
            marked_classroom_entity = existing_classroom_entity.mark_entity_as_deleted()
            marked_classroom_db = self.uow.repository.from_entity(marked_classroom_entity)
            await self.uow.session.merge(marked_classroom_db)
            await self.uow.commit()
        except Exception as e:
            await self.uow.rollback()
            raise e
        finally:
            pass
        
        return marked_classroom_db
        