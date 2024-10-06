from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Sequence

from app.core.error.student_exception import StudentNotFoundError
from ..model import StudentModel, student_course_association
from app.features.student.domain.services.student_service import StudentService
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.data.model.convert_student import ConvertStudent

class StudentServiceImp(StudentService):
    
    def __init__(self, session: Session):
        self.session: Session = session

    def to_read_model(self, student_model: StudentModel) -> StudentDisplay:
        return ConvertStudent.to_read_model(student_model)

    async def find_object_by_id(self, id: int) -> StudentDisplay:
        result = await self.session.execute(select(StudentModel).filter(StudentModel.id == id))
        model_instance = result.scalars().first()
        return self.to_read_model(model_instance) if model_instance else None

    async def find_all_objects(self) -> Sequence[StudentDisplay]:
        result = await self.session.execute(select(StudentModel))
        model_instances = result.scalars().all()
        return [self.to_read_model(model_instance) for model_instance in model_instances]

    async def is_student_enrolled_in_course(self, course_id: int, student_id: int):
        student_enrollment_query = await self.session.execute(
        select(StudentModel.id).join(student_course_association).where(
            student_course_association.c.course_id == course_id,
            student_course_association.c.student_id == student_id
            )
        )
        return student_enrollment_query.scalar() is not None
    
    async def get_student_courses(self, student_id: str):       #TODO:  add courses to student display
        stu = select(StudentModel).filter(StudentModel.id == student_id)
        result = await self.session.execute(stu)
        student = result.scalars().first()
        
        if not student:
            StudentNotFoundError()
            
        return student.courses