from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.error.student_exception import StudentNotFoundError
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.domain.repository.student_unit_of_work import StudentUnitOfWork
from app.features.student.data.model.convert_student import ConvertStudent

class GetStudentUsecase(BaseUseCase[Tuple[int], StudentDisplay]):       #use Tuple or not??
    uow: StudentUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> StudentDisplay:
        raise NotImplementedError()
    
class GetStudentUsecaseImp(GetStudentUsecase):
    def __init__(self, uow: StudentUnitOfWork):
        self.uow: StudentUnitOfWork = uow

    async def __call__(self, args: Tuple[int]) -> StudentDisplay:
        id = args[0]

        try:
            student = await self.uow.service.find_object_by_id(id)
            if not student:
                raise StudentNotFoundError()
            
            return ConvertStudent.from_entity(student)
        except Exception as e:
            raise e