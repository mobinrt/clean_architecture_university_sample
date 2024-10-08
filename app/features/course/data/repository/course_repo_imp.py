from ..model import CourseModel
from ...domain.repository.course_repo import CourseRepository
from ...domain.entities.course_schema import CourseCreate
from ...domain.entities.course_entity import CourseEntity
from app.features.course.data.model.convert_course import ConvertCourse

from typing import Type, TypeVar
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

_MODEL = TypeVar('_MODEL')  

class CourseRepositoryImp(CourseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, CourseModel)
    
    def to_entity(self, model_instance: CourseModel) -> CourseEntity:
        return ConvertCourse.to_entity(model_instance)

    def from_entity(self, entity: CourseEntity) -> CourseModel:
        return ConvertCourse.from_entity(entity)
        
    async def create_object(self, new_course: CourseCreate, course_id: int):
        new_course.id = course_id
        model_instance = self.from_entity(new_course)
        self.session.add(model_instance)
        return self.to_entity(model_instance)
    
    async def find_object_by_id_filter_model(self, object_id: int, model: Type[_MODEL]) -> _MODEL:
        result = await self.session.execute(select(model).filter(model.id == object_id))
        model_instance = result.scalars().first()
        return self.to_entity(model_instance)

    '''
    async def delete_mark(self, id: int) -> CourseEntity | None:
        existing_course_entity = await self.find_object_by_id(id)
        course_db = self.from_entity(existing_course_entity)
        
        self.session.add(course_db)
        await self.session.commit()
        return self.to_entity(course_db)
    '''
