from abc import abstractmethod

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.course_exception import CoursesNotFoundError

class GetHashTableForCourseUseCase(BaseUseCase[None, dict]):
    unique_id: UniqueID
    
    @abstractmethod
    async def __call__(self) -> dict:
        raise NotImplementedError()


class GetHashTableForCourseUseCaseImp(GetHashTableForCourseUseCase):
    def __init__(self, unique_id: UniqueID):
        self.unique_id: UniqueID = unique_id

    async def __call__(self) -> dict:
        try:
            courses_table = self.unique_id.get_table(ObjectToSTR.COURSE.value)
            if not courses_table:
                raise CoursesNotFoundError()
            
            return courses_table
        except Exception as e:
            raise e 
