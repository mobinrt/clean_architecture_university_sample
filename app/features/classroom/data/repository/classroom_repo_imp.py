from ..model import ClassroomModel
from ...domain.repository.classroom_repo import ClassroomRepository
from ...domain.entities.classroom_schema import ClassroomCreate
from ...domain.entities.classroom_entity import ClassroomEntity
from app.features.classroom.data.model.convert_classroom import ConvertClassroom

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class ClassroomRepositoryImp(ClassroomRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, ClassroomModel)
    
    def to_entity(self, model_instance: ClassroomModel) -> ClassroomEntity:
        return ConvertClassroom.to_entity(model_instance)

    def from_entity(self, entity: ClassroomEntity) -> ClassroomModel:
        return ConvertClassroom.from_entity(entity)
        
    async def create_object(self, new_classroom: ClassroomEntity) -> ClassroomModel:
        model_instance = ClassroomModel(
            number=new_classroom.number
        )
        self.session.add(model_instance)
        return model_instance
    
    async def find_classroom_by_number(self, class_num: int) -> ClassroomEntity | None:
        result = await self.session.execute(select(ClassroomModel).filter(ClassroomModel.number == class_num))
        model_instance = result.scalars().first()
        return self.to_entity(model_instance) if model_instance else None