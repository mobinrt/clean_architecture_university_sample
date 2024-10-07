from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.student_exception import StudentsNotFoundError

class GetHashTableForStudentUseCase(BaseUseCase[None, dict]):
    @abstractmethod
    async def __call__(self) -> dict:
        raise NotImplementedError()


class GetHashTableForStudentUseCaseImp(GetHashTableForStudentUseCase):
    def __init__(self, unique_id: UniqueID):
        self.unique_id = unique_id

    async def __call__(self) -> dict:
        try:
            students_table = self.unique_id.get_table(ObjectToSTR.STUDENT.value)
            if not students_table:
                raise StudentsNotFoundError()
            
            return students_table
        except Exception as e:
            raise e