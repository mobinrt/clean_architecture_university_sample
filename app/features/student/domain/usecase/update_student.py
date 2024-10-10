from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.auth_exceptions import AuthErrorForUser
from app.core.use_cases.use_case import BaseUseCase
from app.features.student.domain.entities.student_schema import StudentUpdate, StudentDisplay
from app.features.student.domain.repository.student_unit_of_work import StudentUnitOfWork
from app.features.student.domain.auth.auth_student import StudentAuthService
from app.features.student.data.model.convert_student import ConvertStudent
from app.core.util import hash 


class UpdateStudentUseCase(BaseUseCase[Tuple[str, StudentUpdate], StudentDisplay]):
    uow: StudentUnitOfWork
    auth: StudentAuthService
    
    @abstractmethod
    async def __call__(self, args: Tuple[str, StudentUpdate]) -> StudentDisplay:
        raise NotImplementedError()
    
class UpdateStudentUseCaseImp(UpdateStudentUseCase):
    
    def __init__(self, uow: StudentUnitOfWork, auth: StudentAuthService):
        self.uow = uow
        self.auth = auth
        
    async def __call__(self, args: Tuple[str, StudentUpdate]) -> StudentDisplay:
        token = args[0]
        update_student = args[1]
        
        current_user = await self.auth.get_current_user(token)
        if current_user is None:
            raise AuthErrorForUser()
        
        update_student.password = hash.get_password_hash(update_student.password) if update_student.password else current_user.password
        update_entity = ConvertStudent.updated_model(update_student, current_user)
        current_entity = ConvertStudent.to_entity(current_user)
        
        try:
            updated = await self.uow.repository.update_obj(update_entity, current_entity)
            await self.uow.commit()
            
            return updated
        except Exception as e:
            raise e
