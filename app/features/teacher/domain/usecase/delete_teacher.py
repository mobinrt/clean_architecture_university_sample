from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.teacher.domain.entities.teacher_entity import TeacherEntity
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.domain.repository.teacher_unite_of_work import TeacherUnitOfWork
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.teacher_exception import TeacherNotFoundError, TeacherIsDeleted
from app.features.teacher.data.model.convert_teacher import ConvertTeacher

class DeleteTeacherUseCase(BaseUseCase[Tuple[int], TeacherDisplay]):
    uow: TeacherUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> TeacherDisplay:
        raise NotImplementedError()

class DeleteTeacherUseCaseImpl(DeleteTeacherUseCase):
    def __init__(self, uow: TeacherUnitOfWork, unique_id: UniqueID):
        self.uow: TeacherUnitOfWork = uow
        self.unique_id: UniqueID = unique_id

    async def __call__(self, args: Tuple[int]) -> TeacherDisplay:
        id = args[0]
        existing_stu_db = await self.uow.repository.find_object_by_id(id)
        
        if existing_stu_db is None:
            raise TeacherNotFoundError()
        
        existing_stu_entity = self.uow.repository.to_entity(existing_stu_db)
        
        try:
            if existing_stu_db.is_deleted:
                raise TeacherIsDeleted()
                        
            marked_stu_entity = existing_stu_entity.mark_entity_as_deleted()
            marked_stu_db = self.uow.repository.from_entity(marked_stu_entity)
            await self.uow.session.merge(marked_stu_db)
            await self.uow.commit()
        except Exception as e:
            await self.uow.rollback()
            raise e
        finally:
            pass
        
        return marked_stu_db
        