from abc import abstractmethod
from typing import cast ,Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.teacher.domain.entities.teacher_schema import TeacherCreate, TeacherDisplay
from app.features.teacher.domain.entities.teacher_entity import TeacherEntity
from app.features.teacher.domain.repository.teacher_unite_of_work import TeacherUnitOfWork
from app.core.enum.object_type_digit import ObjectDigits
from app.core.enum.object_type_str import ObjectToSTR
from app.core.util import hash
from app.core.error.teacher_exception import TeacherNameValid
from app.features.teacher.data.model.convert_teacher import ConvertTeacher

class CreateTeacherUseCase(BaseUseCase[Tuple[TeacherCreate], TeacherDisplay]):
    uow: TeacherUnitOfWork

    @abstractmethod
    async def __call__(self, args: Tuple[TeacherCreate]) -> TeacherDisplay:
        raise NotImplementedError()

class CreateTeacherUseCaseImp(CreateTeacherUseCase):
    def __init__(self, uow: TeacherUnitOfWork, unique_id: UniqueID):
        self.uow: TeacherUnitOfWork = uow
        self.unique_id: UniqueID = unique_id
        
    async def __call__(self, args: Tuple[TeacherCreate]) -> TeacherDisplay:
        data = args[0]
        
        if not data.name:
            raise TeacherNameValid()
            
        teacher_id = self.unique_id.insert(ObjectDigits.TEACHER.value, ObjectToSTR.TEACHER.value)
        hashed_password = hash.get_password_hash(data.password)
        
        new_Teacher = TeacherEntity(
            id=teacher_id,
            password=hashed_password,
            **data.model_dump(exclude={"password", "confirm_password"})
        )
        try:
            await self.uow.repository.create_object(new_Teacher, teacher_id)
            self.unique_id.save_to_dict(new_Teacher.name, new_Teacher.id, ObjectToSTR.TEACHER.value)
            await self.uow.commit()
            return ConvertTeacher.from_entity(new_Teacher)
        except Exception as e:
            await self.uow.rollback()
            raise e
        
        
