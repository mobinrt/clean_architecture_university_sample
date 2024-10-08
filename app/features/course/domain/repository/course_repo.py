from app.entity_repository.entity_repo import EntityRepo
from app.features.course.domain.entities.course_entity import CourseEntity  
from app.features.course.data.model import CourseModel 

from typing import Type, TypeVar
from abc import abstractmethod

_MODEL = TypeVar('_MODEL')  


class CourseRepository(EntityRepo[CourseEntity]):
    
    @abstractmethod
    async def find_object_by_id_filter_model(self, object_id: int, model: Type[_MODEL]) -> _MODEL:
        raise NotImplementedError()

    '''
    @abstractmethod
    async def delete_mark(self, id: int) -> StudentEntity | None:
        raise NotImplementedError()
    '''