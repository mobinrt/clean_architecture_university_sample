from ..model import TeacherModel
from ...domain.repository.teacher_repo import TeacherRepository
from ...domain.entities.teacher_schema import TeacherCreate
from ...domain.entities.teacher_entity import TeacherEntity
from app.features.teacher.data.model.convert_teacher import ConvertTeacher

from sqlalchemy.ext.asyncio import AsyncSession

class TeacherRepositoryImp(TeacherRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, TeacherModel)
    
    def to_entity(self, model_instance: TeacherModel) -> TeacherEntity:
        return ConvertTeacher.to_entity(model_instance)

    def from_entity(self, entity: TeacherEntity) -> TeacherModel:
        return ConvertTeacher.from_entity(entity)
        
    async def create_object(self, new_teacher: TeacherCreate, teacher_id: int):
        new_teacher.id = teacher_id
        model_instance = self.from_entity(new_teacher)
        self.session.add(model_instance)
        return self.to_entity(model_instance)
    
    async def fired_students_from_course(self, course_id: int, student_id: int, current_user: TeacherModel):
        pass