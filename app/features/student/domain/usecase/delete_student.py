from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.student.domain.entities.student_entity import StudentEntity
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.repository.student_unite_of_work import StudentUnitOfWork
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.student_exception import StudentNotFoundError
from app.features.student.data.model.convert_student import ConvertStudent

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
        existing_stu = await self.uow.repository.find_object_by_id(id)
        print(existing_stu.is_deleted)
        if existing_stu is None:
            raise StudentNotFoundError()
        
        try:
            marked_stu = await self.uow.repository.delete_mark(id)
            print("is deleted:",existing_stu.is_deleted)
            await self.uow.commit()
        except Exception as e:
            await self.uow.rollback()
            raise e
        finally:
            pass
        
        return ConvertStudent.from_entity(marked_stu)
        