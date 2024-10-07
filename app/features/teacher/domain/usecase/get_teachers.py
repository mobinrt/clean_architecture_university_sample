from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.student_exception import StudentsNotFoundError
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.services.student_service import StudentService

class GetStudentsUsecase(BaseUseCase[None, Sequence[StudentDisplay]]):       #use Tuple or not??
    service: StudentService
    
    @abstractmethod
    async def __call__(self, args: None = None) -> Sequence[StudentDisplay]:
        raise NotImplementedError()
    
class GetStudentsUsecaseImp(GetStudentsUsecase):
    def __init__(self, service: StudentService):
        self.service: StudentService = service

    async def __call__(self, args: None = None) -> Sequence[StudentDisplay]:
        try:
            students = await self.service.find_all_objects()
            if not students:
                raise StudentsNotFoundError()
            
            return students
        except Exception as e:
            raise e