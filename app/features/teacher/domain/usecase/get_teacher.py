from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.student_exception import StudentNotFoundError
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.services.student_service import StudentService

class GetStudentUsecase(BaseUseCase[Tuple[int], StudentDisplay]):       #use Tuple or not??
    serivce: StudentService
    
    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> StudentDisplay:
        raise NotImplementedError()
    
class GetStudentUsecaseImp(GetStudentUsecase):
    def __init__(self, service: StudentService):
        self.service: StudentService = service

    async def __call__(self, args: Tuple[int]) -> StudentDisplay:
        id = args[0]

        try:
            student = await self.service.find_object_by_id(id)
            if not student:
                raise StudentNotFoundError()
            
            return student
        except Exception as e:
            raise e