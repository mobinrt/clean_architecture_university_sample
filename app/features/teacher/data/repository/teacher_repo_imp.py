from ..model import StudentModel, student_course_association
from ...domain.repository import StudentRepository
from ...domain.entities import StudentCreate
from ...domain.entities import StudentEntity
from app.features.student.data.model.convert_student import ConvertStudent

from sqlalchemy.ext.asyncio import AsyncSession

class StudentRepositoryImp(StudentRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session, StudentModel)
    
    def to_entity(self, model_instance: StudentModel) -> StudentEntity:
        return ConvertStudent.to_entity(model_instance)

    def from_entity(self, entity: StudentEntity) -> StudentModel:
        return ConvertStudent.from_entity(entity)
        
    async def create_object(self, new_student: StudentCreate, stu_id: int):
        new_student.id = stu_id
        model_instance = self.from_entity(new_student)
        self.session.add(model_instance)
        return self.to_entity(model_instance)
    
    async def enroll_student_in_course(self, course_id: int, student_id: int):    
        
        await self.session.execute(
        student_course_association.insert().values(
            student_id=student_id,
            course_id=course_id
            )
        )
        await self.session.commit()
        
    '''
    async def delete_mark(self, id: int) -> StudentEntity | None:
        existing_stu_entity = await self.find_object_by_id(id)
        stu_db = self.from_entity(existing_stu_entity)
        
        self.session.add(existing_stu)
        await self.session.commit()
        return self.to_entity(existing_stu)
    '''