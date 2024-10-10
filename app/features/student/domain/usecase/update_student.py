from abc import abstractmethod
from typing import cast, Tuple, Optional

from app.core.error.auth_exceptions import AuthErrorForUser
from app.core.use_cases.use_case import BaseUseCase
from app.features.student.domain.entities.student_schema import StudentUpdate, StudentDisplay
from app.features.student.domain.repository.student_unit_of_work import StudentUnitOfWork
from app.features.student.domain.auth.auth_student import StudentAuthService
from app.features.student.data.model.convert_student import ConvertStudent

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
        
        try:
            updated = await self.uow.repository.update_obj(update_student, current_user)
            await self.uow.commit()
            
            return ConvertStudent.from_entity(updated)
        except Exception as e:
            raise e
