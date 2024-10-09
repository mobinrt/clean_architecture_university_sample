from abc import ABC

from app.core.services.entity_services import EntityServices
from app.features.course.data.model import CourseModel
from ..entities.course_schema import CourseDisplay

from typing import Type, TypeVar
from abc import abstractmethod

_MODEL = TypeVar('_MODEL')  

class CourseService(EntityServices[CourseDisplay, CourseModel]):
    
    @abstractmethod
    async def find_object_by_id_filter_model(self, object_id: int, model: Type[_MODEL]) -> _MODEL | None:
        raise NotImplementedError()
    
    
    @abstractmethod
    async def find_teacher_by_id(self, teahcer_id: int):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def find_classroom_by_number(self, classroom_num: int):
        raise NotImplementedError()