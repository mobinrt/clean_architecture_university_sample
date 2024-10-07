from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.student.domain.entities.student_entity import StudentEntity
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.repository.student_unite_of_work import StudentUnitOfWork
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.student_exception import StudentNotFoundError, StudentIsDeleted
from app.features.student.data.model.convert_student import ConvertStudent
from app.core.error.invalid_operation_exception import InvalidOperationError

class DeleteStudentUseCase(BaseUseCase[Tuple[int], StudentDisplay]):
    uow: StudentUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> StudentDisplay:
        raise NotImplementedError()

class DeleteStudentUseCaseImpl(DeleteStudentUseCase):
    def __init__(self, uow: StudentUnitOfWork, unique_id: UniqueID):
        self.uow: StudentUnitOfWork = uow
        self.unique_id: UniqueID = unique_id

    async def __call__(self, args: Tuple[int]) -> StudentDisplay:
        id = args[0]
        existing_stu_db = await self.uow.repository.find_object_by_id(id)
        
        if existing_stu_db is None:
            raise StudentNotFoundError()
        
        existing_stu_entity = self.uow.repository.to_entity(existing_stu_db)
        
        try:
            if existing_stu_db.is_deleted:
                raise StudentIsDeleted()
                        
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
        