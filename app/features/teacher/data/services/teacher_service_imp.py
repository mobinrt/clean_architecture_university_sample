from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Sequence

from app.core.error.teacher_exception import TeacherNotFoundError
from ..model import TeacherModel
from app.features.teacher.domain.services.teacher_service import TeacherService
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.data.model.convert_teacher import ConvertTeacher

class TeacherServiceImp(TeacherService):
    
    def __init__(self, session: Session):
        self.session: Session = session

    def to_read_model(self, teacher_model: TeacherModel) -> TeacherDisplay:
        return ConvertTeacher.to_read_model(teacher_model)

    async def find_object_by_id(self, id: int) -> TeacherDisplay:
        result = await self.session.execute(select(TeacherModel).filter(TeacherModel.id == id))
        model_instance = result.scalars().first()
        return self.to_read_model(model_instance) if model_instance else None

    async def find_all_objects(self) -> Sequence[TeacherDisplay]:
        result = await self.session.execute(select(TeacherModel))
        model_instances = result.scalars().all()
        return [self.to_read_model(model_instance) for model_instance in model_instances]
