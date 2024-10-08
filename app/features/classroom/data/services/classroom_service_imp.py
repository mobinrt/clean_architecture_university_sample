from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Sequence

from ..model import ClassroomModel
from app.features.classroom.domain.services.classroom_service import ClassroomService
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.data.model.convert_classroom import ConvertClassroom

class ClassroomServiceImp(ClassroomService):
    
    def __init__(self, session: Session):
        self.session: Session = session

    def to_read_model(self, classroom_model: ClassroomModel) -> ClassroomDisplay:
        return ConvertClassroom.to_read_model(classroom_model)

    async def find_object_by_id(self, id: int) -> ClassroomDisplay:
        result = await self.session.execute(select(ClassroomModel).filter(ClassroomModel.id == id))
        model_instance = result.scalars().first()
        return self.to_read_model(model_instance) if model_instance else None

    async def find_all_objects(self) -> Sequence[ClassroomDisplay]:
        result = await self.session.execute(select(ClassroomModel))
        model_instances = result.scalars().all()
        return [self.to_read_model(model_instance) for model_instance in model_instances]
