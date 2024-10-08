from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Sequence

from ..model import CourseModel
from app.features.course.domain.services.course_service import CourseService
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.data.model.convert_course import ConvertCourse

class CourseServiceImp(CourseService):
    
    def __init__(self, session: Session):
        self.session: Session = session

    def to_read_model(self, course_model: CourseModel) -> CourseDisplay:
        return ConvertCourse.to_read_model(course_model)

    async def find_object_by_id(self, id: int) -> CourseDisplay:
        result = await self.session.execute(select(CourseModel).filter(CourseModel.id == id))
        model_instance = result.scalars().first()
        return self.to_read_model(model_instance) if model_instance else None

    async def find_all_objects(self) -> Sequence[CourseDisplay]:
        result = await self.session.execute(select(CourseModel))
        model_instances = result.scalars().all()
        return [self.to_read_model(model_instance) for model_instance in model_instances]