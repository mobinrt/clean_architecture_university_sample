from app.shared.entity_repository.entity_repo import EntityRepo
from app.features.course.domain.entities.course_entity import CourseEntity  


class CourseRepository(EntityRepo[CourseEntity]):
    
    pass
    '''
    @abstractmethod
    async def delete_mark(self, id: int) -> StudentEntity | None:
        raise NotImplementedError()
    '''