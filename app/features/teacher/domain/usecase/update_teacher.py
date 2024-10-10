from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.auth_exceptions import AuthErrorForUser
from app.core.util.id_manager import UniqueID
from app.core.enum.object_type_str import ObjectToSTR
from app.core.use_cases.use_case import BaseUseCase

from app.features.teacher.domain.entities.teacher_schema import TeacherUpdate, TeacherDisplay
from app.features.teacher.domain.repository.teacher_unit_of_work import TeacherUnitOfWork
from app.features.teacher.domain.auth.auth_teacher import TeacherAuthService
from app.features.teacher.data.model.convert_teacher import ConvertTeacher
from app.core.util import hash 


class UpdateTeacherUseCase(BaseUseCase[Tuple[str, TeacherUpdate], TeacherDisplay]):
    uow: TeacherUnitOfWork
    auth: TeacherAuthService
    unique_id: UniqueID
    
    @abstractmethod
    async def __call__(self, args: Tuple[str, TeacherUpdate]) -> TeacherDisplay:
        raise NotImplementedError()
    
class UpdateTeacherUseCaseImp(UpdateTeacherUseCase):
    
    def __init__(self, uow: TeacherUnitOfWork, auth: TeacherAuthService, unique_id: UniqueID):
        self.uow: TeacherUnitOfWork = uow
        self.auth: TeacherAuthService = auth
        self.unique_id: UniqueID = unique_id
        
        
    async def __call__(self, args: Tuple[str, TeacherUpdate]) -> TeacherDisplay:
        token = args[0]
        update_teacher = args[1]
        current_user = await self.auth.get_current_user(token)
        
        if current_user is None:
            raise AuthErrorForUser()
        
        if not update_teacher.name:
            update_teacher.name = current_user.name
        update_teacher.password = hash.get_password_hash(update_teacher.password) if update_teacher.password else current_user.password
        
        update_entity = ConvertTeacher.updated_model(update_teacher, current_user)
        
        current_entity = ConvertTeacher.to_entity(current_user)
        
        try:
            updated = await self.uow.repository.update_obj(update_entity, current_entity)
            print(updated.name)
            self.unique_id.update_name(ObjectToSTR.TEACHER.value, updated.id, updated.name)
            
            await self.uow.commit()
            
            return updated
        except Exception as e:
            raise e
