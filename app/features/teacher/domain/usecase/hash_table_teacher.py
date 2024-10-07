from abc import abstractmethod

from app.core.error.teacher_exception import TeachersNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.core.enum.object_type_str import ObjectToSTR

class GetHashTableForTeacherUseCase(BaseUseCase[None, dict]):
    @abstractmethod
    async def __call__(self) -> dict:
        raise NotImplementedError()

class GetHashTableForTeacherUseCaseImp(GetHashTableForTeacherUseCase):
    def __init__(self, unique_id: UniqueID):
        self.unique_id = unique_id

    async def __call__(self) -> dict:
        try:
            teacher_table = self.unique_id.get_table(ObjectToSTR.TEACHER.value)
            if not teacher_table:
                raise TeachersNotFoundError()
            
            return teacher_table
        except Exception as e:
            raise e