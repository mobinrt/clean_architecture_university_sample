from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.student.domain.entities.student_schema import StudentCreate
from app.features.student.domain.entities.student_entity import StudentEntity
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.repository.student_unite_of_work import StudentUnitOfWork
from app.core.enum.object_type_digit import ObjectDigits
from app.core.enum.object_type_str import ObjectToSTR
from app.core.util import hash
from app.core.error.student_exception import StudentNameValid
from app.features.student.data.model.convert_student import ConvertStudent

class CreateStudentUseCase(BaseUseCase[Tuple[StudentCreate], StudentDisplay]):
    uow: StudentUnitOfWork

    @abstractmethod
    async def __call__(self, args: Tuple[StudentCreate]) -> StudentDisplay:
        raise NotImplementedError()

class CreateStudentUseCaseImp(CreateStudentUseCase):
    def __init__(self, uow: StudentUnitOfWork, unique_id: UniqueID):
        self.uow: StudentUnitOfWork = uow
        self.unique_id: UniqueID = unique_id
        
    async def __call__(self, args: Tuple[StudentCreate]) -> StudentDisplay:
        data = args[0]
        
        if not data.name:
            raise StudentNameValid()
            
        stu_id = self.unique_id.insert(ObjectDigits.STUDENT.value, ObjectToSTR.STUDENT.value)
        hashed_password = hash.get_password_hash(data.password)
        
        new_student = StudentEntity(
            id=stu_id,
            password=hashed_password,
            **data.model_dump(exclude={"password", "confirm_password"})
        )
        try:
            await self.uow.repository.create_object(new_student, stu_id)
            self.unique_id.save_to_dict(new_student.name, new_student.id, ObjectToSTR.STUDENT.value)
            await self.uow.commit()
            return ConvertStudent.from_entity(new_student)
        except Exception as e:
            await self.uow.rollback()
            raise e
        
        
