from abc import abstractmethod
from app.entity_repository.entity_repo import EntityRepo
from app.features.course.domain.entities.course_entity import CourseEntity  
from app.features.course.data.model import CourseModel 

class CourseRepository(EntityRepo[CourseEntity]):
    pass

    '''
    @abstractmethod
    async def delete_mark(self, id: int) -> StudentEntity | None:
        raise NotImplementedError()
    '''