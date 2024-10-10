from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.student_exception import StudentsNotFoundError
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.repository.student_unit_of_work import StudentUnitOfWork
from app.features.student.data.model.convert_student import ConvertStudent

class GetStudentsUsecase(BaseUseCase[None, Sequence[StudentDisplay]]):       #use Tuple or not??
    uow: StudentUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: None = None) -> Sequence[StudentDisplay]:
        raise NotImplementedError()
    
class GetStudentsUsecaseImp(GetStudentsUsecase):
    def __init__(self, uow: StudentUnitOfWork):
        self.uow: StudentUnitOfWork = uow

    async def __call__(self, args: None = None) -> Sequence[StudentDisplay]:
        try:
            students = await self.uow.service.find_all_objects()
            if not students:
                raise StudentsNotFoundError()
            
            return students
        except Exception as e:
            raise e